from pathlib import Path

def bootstrap_spec_kit():
    spec_kit_dir = Path("docs/git-spec-kit")
    spec_kit_dir.mkdir(parents=True, exist_ok=True)
    
    templates = {
        "SDD_TEMPLATE.md": "# Software Design Document (SDD)\n\n## Goal\n## Proposed Changes\n## Verification Plan\n",
        "TDD_TEMPLATE.md": "# Test Driven Development (TDD)\n\n## Test Cases\n## Implementation Steps\n## Results\n",
        "SPEC_TEMPLATE.md": "# Spec: [ID] [Title]\n\nAs a [User Role], I want [Goal] so that [Benefit].\n"
    }
    
    for filename, content in templates.items():
        (spec_kit_dir / filename).write_text(content)
    
    print(f"Bootstrapped git-spec-kit at {spec_kit_dir}")

if __name__ == "__main__":
    bootstrap_spec_kit()
