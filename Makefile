init:
	python -m venv venv
	mkdir -p docs/git-spec-kit src tests outputs
	python src/bootstrapping_git_spec_kit.py

test:
	python -m pytest tests/

orchestrate:
	python src/orchestration.py

restructure:
	# Automated restructuring handled by orchestration.py restructure_node
	python src/orchestration.py --restructure
