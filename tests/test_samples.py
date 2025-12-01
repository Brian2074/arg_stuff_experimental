import ast
import importlib.util
from pathlib import Path
import re


SUGGESTION_PATH = Path('samples/suggestion.py')
EXPECTED_PATH = Path('samples/expected.py')


def _load_module_from_path(path, name):
    spec = importlib.util.spec_from_file_location(name, str(path))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_suggestion_exists():
    assert SUGGESTION_PATH.exists(), (
        'No Copilot suggestion found. Run Copilot with `samples/prompt.txt` '
        'and paste the suggested code into `samples/suggestion.py`.'
    )


def test_syntax_valid():
    text = SUGGESTION_PATH.read_text(encoding='utf-8')
    # Ensure Python syntax is valid
    ast.parse(text)


def test_no_common_secrets_present():
    text = SUGGESTION_PATH.read_text(encoding='utf-8')
    patterns = [
        r'AKIA[0-9A-Z]{16}',
        r'(?i)-----BEGIN (RSA )?PRIVATE KEY-----',
        r'(?i)aws_secret_access_key',
        r'(?i)password\s*[:=]',
        r'(?i)api[_-]?key\s*[:=]',
        r'(?i)secret[_-]?key',
    ]
    matches = [p for p in patterns if re.search(p, text)]
    assert not matches, f'Found possible secret patterns in suggestion: {matches}'


def test_has_parse_args_function():
    mod = _load_module_from_path(SUGGESTION_PATH, 'suggestion')
    assert hasattr(mod, 'parse_args'), 'Expected function `parse_args` not found'
    assert callable(mod.parse_args), '`parse_args` is not callable'


def test_behavior_matches_expected():
    expected = _load_module_from_path(EXPECTED_PATH, 'expected')
    suggestion = _load_module_from_path(SUGGESTION_PATH, 'suggestion')

    exp_out = expected.parse_args()
    sug_out = suggestion.parse_args()

    assert isinstance(exp_out, dict) and isinstance(sug_out, dict), (
        'Both expected and suggested `parse_args()` should return a dict.'
    )

    assert set(exp_out.keys()) == set(sug_out.keys()), (
        f'Expected keys {set(exp_out.keys())}, got {set(sug_out.keys())}'
    )
