"""
Unit and regression test for the cookiecutter package.
"""

# Import package, test suite, and other packages as needed
import cookiecutter
import pytest
import sys

def test_cookiecutter_imported():
    """Sample test, will always pass so long as import statement worked"""
    assert "cookiecutter" in sys.modules
