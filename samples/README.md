Samples harness
================

Purpose
-------
This folder contains a prompt and an expected implementation used to verify
Copilot suggestions. The process is semi-automatic: you run Copilot in your
editor, copy the suggested code into `samples/suggestion.py`, and then run the
tests to let CI or local pytest validate the suggestion.

How to use
----------
1. Open a code file in VS Code inside this repository and paste the contents
   of `samples/prompt.txt` as the prompt for Copilot (or type a similar prompt).
2. Accept a Copilot suggestion and paste the suggested code into
   `samples/suggestion.py` (create that file if it doesn't exist).
3. Run the tests locally:

```bash
pip install pytest
pytest tests/test_samples.py -q
```

Expected outcome
----------------
- `samples/suggestion.py` should be valid Python and define a `parse_args()`
  function.
- When called with no external args, `parse_args()` should return a dict
  with the same keys as `samples/expected.py` (`'count'`) and reasonable types.
- The test will also scan for common secret patterns and fail if any are found.
