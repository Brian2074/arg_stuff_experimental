import re
from pathlib import Path


INSTRUCTIONS_PATH = Path('.github/copilot_instructions.md')


def test_file_exists():
    assert INSTRUCTIONS_PATH.exists(), f"{INSTRUCTIONS_PATH} not found"


def _read_text():
    return INSTRUCTIONS_PATH.read_text(encoding='utf-8')


def test_has_required_sections():
    text = _read_text()
    # these headings are expected to appear in the repository instruction file
    required = [
        'Purpose',
        'Usage Guidelines',
        'Examples',
        'Configuration',
        'Contribution',
    ]
    missing = [h for h in required if h.lower() not in text.lower()]
    assert not missing, f"Missing sections in copilot_instructions.md: {missing}"


def test_has_code_examples():
    text = _read_text()
    # ensure there's at least one fenced code block or an inline code example
    assert '```' in text or '`' in text, 'No code block or inline code found in instructions'


def test_no_common_secrets_present():
    text = _read_text()
    patterns = [
        r'AKIA[0-9A-Z]{16}',
        r'(?i)-----BEGIN (RSA )?PRIVATE KEY-----',
        r'(?i)aws_secret_access_key',
        r'(?i)password\s*[:=]',
        r'(?i)api[_-]?key\s*[:=]',
        r'(?i)secret[_-]?key',
    ]
    matches = []
    for p in patterns:
        if re.search(p, text):
            matches.append(p)
    assert not matches, f"Found possible secret patterns in instructions: {matches}"


def test_references_copilot_yml_if_present():
    text = _read_text()
    # It's helpful when instructions reference `.github/copilot.yml` if present
    assert '.github/copilot.yml' in text or 'copilot.yml' in text, 'No reference to .github/copilot.yml found'
