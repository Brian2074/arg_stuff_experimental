# Copilot Instructions

This file provides repository-specific guidance for GitHub Copilot usage.

## Purpose
- Assist with code completion, tests, docs, and small refactors.
- Prefer suggestions that follow existing project patterns and style.

## Usage Guidelines
- Accept suggestions when they match project style and pass tests.
- Edit suggestions to match naming, formatting, and security practices.
- Do not accept suggestions that introduce secrets, hard-coded credentials, or unsafe patterns.

## Examples
- Use Copilot to generate function skeletons, unit tests, or README snippets.
- Review and run all generated code locally before merging.

### Example prompt and expected output
```python
# Prompt: "Create a small function using argparse that returns a dict of parsed args"
def parse_args():
	import argparse

	parser = argparse.ArgumentParser()
	parser.add_argument('--count', type=int, default=1)
	args = parser.parse_args([])
	return vars(args)

# Expected: a simple, well-documented function that uses existing project style
```

## Configuration
- See .github/copilot.yml (if present) for repository-specific settings.

## Contribution
- Report repeating incorrect suggestions by opening an issue with examples.
- Document any repository-specific rules here.
