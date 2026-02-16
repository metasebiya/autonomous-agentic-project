import os
from pathlib import Path
from typing import TypedDict
from langgraph.graph import StateGraph, END

# Define state schema
class ProjectState(TypedDict):
    constitution: str
    spec: str
    plan: str
    tasks: str
    implementation: str

# Node functions
def constitution_node(state: ProjectState):
    constitution = """# Constitution
1. No code without a spec.
2. Every feature must have at least one test before merge.
3. Documentation auto-generated from specs/tests.
4. All commits must reference a Spec ID.
5. Audit logs preserved for every orchestration run.
"""
    Path("CONSTITUTION.md").write_text(constitution)
    return {"constitution": constitution}

def spec_node(state: ProjectState):
    spec = """# Spec: INIT-001 Project Initialization Agent
As a developer, I want an autonomous agent to initialize a new project repository with scaffolding so I can begin development immediately.
"""
    Path("SPEC.md").write_text(spec)
    return {"spec": spec}

def plan_node(state: ProjectState):
    plan = """# Plan for INIT-001
1. Repo Setup
2. Branching
3. Skeleton
4. SpecKit Bootstrap
5. MCP Integration
"""
    Path("PLAN.md").write_text(plan)
    return {"plan": plan}

def tasks_node(state: ProjectState):
    tasks = """# Tasks
T-001: Initialize Git repo
T-002: Push repo to remote
T-003: Clone repo locally
T-004: Create init-project branch
T-005: Create skeleton dirs/files
"""
    Path("TASKS.md").write_text(tasks)
    return {"tasks": tasks}

def implementation_node(state: ProjectState):
    # Create directories
    for d in ["src", "tests", "docs"]:
        Path(d).mkdir(exist_ok=True)

    # Create baseline files
    Path("src/main.py").write_text('def hello():\n    return "Agentic workspace initialized!"\n')
    Path("tests/test_main.py").write_text(
        "from src.main import hello\n\n"
        "def test_hello():\n"
        "    assert hello() == 'Agentic workspace initialized!'\n"
    )
    Path("requirements.txt").write_text("langgraph\npytest\n")
    Path("Makefile").write_text(
        "init:\n\tpython3 -m venv venv\n\tmkdir -p docs src tests\n"
        "\ttouch requirements.txt Makefile CONSTITUTION.md SPEC.md PLAN.md TASKS.md\n"
    )

    implementation = "Repo skeleton created with src/, tests/, docs/, and baseline files."
    return {"implementation": implementation}

# Build graph
workflow = StateGraph(ProjectState)

workflow.add_node("constitution", constitution_node)
workflow.add_node("spec", spec_node)
workflow.add_node("plan", plan_node)
workflow.add_node("tasks", tasks_node)
workflow.add_node("implementation", implementation_node)

workflow.set_entry_point("constitution")
workflow.add_edge("constitution", "spec")
workflow.add_edge("spec", "plan")
workflow.add_edge("plan", "tasks")
workflow.add_edge("tasks", "implementation")
workflow.add_edge("implementation", END)

app = workflow.compile()

if __name__ == "__main__":
    initial = ProjectState()
    print(f"DEBUG: Initial state type: {type(initial)}")
    final_state = app.invoke(initial)
    print(f"DEBUG: Final state type: {type(final_state)}")
    print(f"DEBUG: Final state dir: {dir(final_state)}")
    
    if hasattr(final_state, 'items'):
        for key, value in final_state.items():
            print(f"\n=== {key.upper()} ===\n{value}")
    else:
        print("Final state does not have .items() method.")
        print(f"Final state content: {final_state}")
