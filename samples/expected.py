"""Expected implementation used by the validation tests.

This file defines the minimal, expected behavior for the sample prompt.
Tests will compare a pasted Copilot suggestion against this implementation.
"""

def parse_args():
    """Parse arguments and return them as a dict.

    This implementation parses an optional `--count` argument (int, default 1)
    and returns a dict of the parsed arguments. The function accepts no
    external input (it calls `parse_args([])` to avoid using sys.argv).
    """
    import argparse

    parser = argparse.ArgumentParser(description='Sample parse_args')
    parser.add_argument('--count', type=int, default=1, help='Number of items')
    args = parser.parse_args([])
    return vars(args)


__all__ = ['parse_args']
