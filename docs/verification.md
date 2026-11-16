# Pipeline verification

## Incident (2026-11-16): Flake8 rejected three test lines

Python 3.13.9 with Flake8 7.3.0 reproduced the failure using `venv/bin/python -m flake8 app.py deploy.py tests`.
The output was `tests/test_app.py:19:80: E501 line too long (80 > 79 characters)`, followed by E501 failures on lines 28 and 35 (81 characters each).
The nine application and deployment tests passed, but the real pipeline lint command would stop before running them.

**Fix:** Wrap the three assertions without changing their expectations.
The named regression check is the Jenkins `Lint` stage, which invokes the same pinned Flake8 command over the application, deployment script, and tests.
The corrected check exits zero; the nine tests pass; coverage reports 100 percent of 22 statements and four branches; Bandit reports no findings.
