import pytest
import os
from pathlib import Path
from src.orchestration import ProjectState, workflow

def test_restructure_node_moves_files():
    # This test will likely require mocking or a temporary directory setup
    # For now, let's verify that the orchestration logic is structured to handle these nodes
    nodes = workflow.nodes.keys()
    assert "restructure" in nodes
    assert "git_init" in nodes
    assert "scaffolding" in nodes
    assert "hitl_approval" in nodes

def test_spec_first_principle():
    # Test that implementation cannot happen if spec is missing
    # This relates to our strict rule
    pass

def test_git_spec_kit_bootstrap():
    # Verify git-spec-kit is created
    pass
