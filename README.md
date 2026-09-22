# CI RCA Demo Python Project

A medium-sized Python project designed for testing a Root Cause Driven CI/CD analysis system.

## Stack
- Python 3.11+
- pytest
- GitHub Actions
- Pure Python business logic
- No external database required

## Modules
- `src/task_manager/models.py` - domain models
- `src/task_manager/repository.py` - in-memory repository
- `src/task_manager/service.py` - task business logic
- `src/task_manager/analytics.py` - task statistics
- `src/task_manager/validators.py` - validation rules
- `tests/` - pytest test suite

## Run locally

```bash
python -m pip install -r requirements.txt
pytest -q
```

The GitHub Actions workflow is at `.github/workflows/ci.yml`.

The project is intentionally structured so that a future commit can introduce a controlled regression and your RCA system can trace the failure through the test, function, file, diff, blame, and dependency relationships.
