# Local lint verification

## Incident (2026-11-16): Flake8 rejected three test lines

Python 3.13.9 with Flake8 7.3.0 reproduced the failure using
`venv/bin/python -m flake8 app.py deploy.py tests`. The output reported E501
on `tests/test_app.py` lines 19, 28, and 35. The Jenkins `Lint` stage invokes
this command before the later pipeline stages.

**Fix:** Wrap the three assertions without changing their expectations. The
same local command now exits zero. Actual Jenkins execution remains pending on
`main`.
