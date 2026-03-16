# Project Guidelines

## Code Style
- Keep Python code simple and explicit; prefer small pure functions in logic modules.
- Preserve existing naming in this repo unless the task explicitly asks for renaming.
- Avoid adding extra dependencies unless required by the task.

## Architecture
- `app.py` is the Streamlit UI and state orchestration layer.
- `logic_utils.py` is the game-logic layer and should contain testable pure logic.
- `tests/test_game_logic.py` is the baseline test contract for game outcomes.
- For logic changes, update `logic_utils.py` first, then wire UI calls from `app.py`.

## Build and Test
- Install dependencies: `pip install -r requirements.txt`
- Run app: `python -m streamlit run app.py`
- Run tests: `pytest`

## Conventions
- This starter intentionally contains bugs; fix only what the current task asks for.
- Session values in Streamlit must be persisted via `st.session_state` guards to avoid reset-on-rerun issues.
- Keep difficulty range handling consistent with selected difficulty (avoid hardcoding unrelated ranges).
- Respect test expectations: current tests assert `check_guess(...)` returns outcome strings (`"Win"`, `"Too High"`, `"Too Low"`). If behavior changes, update tests only when the task explicitly allows contract changes.