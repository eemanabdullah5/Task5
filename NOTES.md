# Git Version Control and Clean Code

A small student-grades script (`grades.py`) used to practise Git branching, merging,
resolving a merge conflict, and refactoring to PEP8 and clean-code standards.

## Workflow

| Step | Branch | What it did |
|---|---|---|
| 1 | `main` | Initial messy `gra# Git Version Control and Clean Code

A small student-grades script (`grades.py`) used to practise Git branching, merging,
resolving a merge conflict, and refactoring to PEP8 and clean-code standards.

## Workflow

| Step | Branch | What it did |
|---|---|---|
| 1 | `main` | Initial messy `grades.py` (75 flake8 issues) |
| 2 | `refactor/pep8` | PEP8 formatting only: flake8 75 -> 0 issues, same output. Fast-forward merge into `main` |
| 3 | `feature/letter-grades` | Changed PASS/FAIL to A/B/C/F letter grades |
| 4 | `refactor/magic-number` | Replaced the magic number `60` with `PASS_MARK`; renamed `Result` to `get_result` |
| 5 | `main` | Merged both branches, which caused a merge conflict that I resolved by hand |
| 6 | `refactor/clean-code` | snake_case names, docstrings, `main()`, no global data, f-strings. Fast-forward merge |

## Git log

```text
* d525bf6 Refactor for clean code: snake_case names, docstrings, main(), no globals
*   625e164 Merge feature/letter-grades: keep letter grades, use named constants
|\  
| * d0ea912 Add letter grades (A/B/C/F) to the report
* | a70fd4a Replace magic number 60 with PASS_MARK; rename Result to get_result
|/  
* 6d47e72 Fix PEP8 formatting (flake8: 75 -> 0 issues)
* 2a05a81 Add initial student grades script
```

## Merge conflict

`feature/letter-grades` and `refactor/magic-number` both changed the `Result` function and the
report line, so merging them gave 2 conflict blocks.

Neither side was fully correct, so no single VS Code button worked:

- **Accept Current** kept `PASS_MARK` and `get_result`, but lost the letter grades and printed `result=`.
- **Accept Incoming** called `Result()`, which no longer existed after the rename (NameError).
- **Accept Both** would have printed every student twice.

**Resolution:** I combined both changes. I kept the letter grades and the new name `get_result`, and
replaced every threshold with a named constant (`GRADE_A = 90`, `GRADE_B = 75`, `PASS_MARK = 60`).

Git had also auto-merged `return "F"` outside the conflict markers. Accepting only the current side
would have produced `PASS` / `F`, a mix of both grading systems. So I reread the whole function and
ran the program to confirm the result was correct, not just conflict-free.

## Clean code changes

| Before | After | Why |
|---|---|---|
| `calc`, `printReport`, `topStudent` | `average`, `print_report`, `top_student` | Clear snake_case names |
| `n`, `a`, `t`, `r`, `s` | `name`, `avg`, `scores`, `raw_scores` | Meaningful variable names |
| Bare `60`, `90`, `75` | `PASS_MARK`, `GRADE_A`, `GRADE_B` | No magic numbers |
| `for i in range(len(l))` loop | `sum(scores) / len(scores)` | Simpler, uses a built-in |
| 10-line best-student loop | `max(..., key=...)` | One clear line |
| Functions read the global `data` | `students` is passed in | Self-contained, easy to test |
| `addStudent` printed errors itself | `add_student` raises `ValueError`; `main()` handles it | The caller decides what to do |
| No documentation | A docstring on every function | Says what each function does |
| Code at module level | `main()` function | A clear entry point |

The output is identical before and after every refactor (checked by running `python grades.py`).

## flake8 before (original code)

Checked on the first commit (`git show 2a05a81:grades.py | python -m flake8 -`), so the lines start
with `stdin:` instead of `grades.py:`. 75 issues in total.

```text
stdin:1:1: F401 'os' imported but unused
stdin:1:1: F401 'sys' imported but unused
stdin:1:10: E401 multiple imports on one line
stdin:1:10: E231 missing whitespace after ','
stdin:2:1: F401 'math' imported but unused
stdin:4:5: E225 missing whitespace around operator
stdin:4:12: E231 missing whitespace after ':'
stdin:4:16: E231 missing whitespace after ','
stdin:4:19: E231 missing whitespace after ','
stdin:4:23: E231 missing whitespace after ','
stdin:4:30: E231 missing whitespace after ':'
stdin:4:34: E231 missing whitespace after ','
stdin:4:37: E231 missing whitespace after ','
stdin:4:41: E231 missing whitespace after ','
stdin:4:48: E231 missing whitespace after ':'
stdin:4:52: E231 missing whitespace after ','
stdin:4:55: E231 missing whitespace after ','
stdin:4:59: E231 missing whitespace after ','
stdin:4:66: E231 missing whitespace after ':'
stdin:4:70: E231 missing whitespace after ','
stdin:4:73: E231 missing whitespace after ','
stdin:5:1: E302 expected 2 blank lines, found 0
stdin:5:10: E741 ambiguous variable name 'l'
stdin:6:6: E225 missing whitespace around operator
stdin:7:27: E701 multiple statements on one line (colon)
stdin:7:27: E231 missing whitespace after ':'
stdin:7:29: E225 missing whitespace around operator
stdin:9:1: E302 expected 2 blank lines, found 0
stdin:10:6: E225 missing whitespace around operator
stdin:11:9: E225 missing whitespace around operator
stdin:11:13: E701 multiple statements on one line (colon)
stdin:11:13: E231 missing whitespace after ':'
stdin:12:9: E701 multiple statements on one line (colon)
stdin:12:9: E231 missing whitespace after ':'
stdin:13:1: E302 expected 2 blank lines, found 0
stdin:14:28: E702 multiple statements on one line (semicolon)
stdin:14:28: E231 missing whitespace after ';'
stdin:16:10: E225 missing whitespace around operator
stdin:17:10: E225 missing whitespace around operator
stdin:18:41: E231 missing whitespace after ','
stdin:19:1: E302 expected 2 blank lines, found 0
stdin:20:9: E225 missing whitespace around operator
stdin:20:14: E702 multiple statements on one line (semicolon)
stdin:20:14: E231 missing whitespace after ';'
stdin:20:22: E225 missing whitespace around operator
stdin:22:10: E225 missing whitespace around operator
stdin:23:13: E225 missing whitespace around operator
stdin:24:20: E225 missing whitespace around operator
stdin:24:22: E702 multiple statements on one line (semicolon)
stdin:24:22: E231 missing whitespace after ';'
stdin:24:27: E225 missing whitespace around operator
stdin:25:12: E711 comparison to None should be 'if cond is None:'
stdin:25:12: E225 missing whitespace around operator
stdin:25:18: E701 multiple statements on one line (colon)
stdin:25:18: E231 missing whitespace after ':'
stdin:27:1: E302 expected 2 blank lines, found 0
stdin:28:10: E225 missing whitespace around operator
stdin:29:18: E701 multiple statements on one line (colon)
stdin:29:18: E231 missing whitespace after ':'
stdin:29:24: E225 missing whitespace around operator
stdin:31:1: E302 expected 2 blank lines, found 0
stdin:31:17: E231 missing whitespace after ','
stdin:33:10: E225 missing whitespace around operator
stdin:34:5: E722 do not use bare 'except'
stdin:37:12: E225 missing whitespace around operator
stdin:38:1: E305 expected 2 blank lines after class or function definition, found 0
stdin:38:12: E225 missing whitespace around operator
stdin:39:23: E231 missing whitespace after ','
stdin:39:29: E231 missing whitespace after ','
stdin:39:34: E231 missing whitespace after ','
stdin:40:21: E231 missing whitespace after ','
stdin:40:26: E231 missing whitespace after ','
stdin:42:80: E501 line too long (135 > 79 characters)
stdin:42:94: E231 missing whitespace after ','
stdin:43:53: E231 missing whitespace after ','
```

## flake8 after (final code)

```text
flake8 grades.py: 0 issues
```des.py` (75 flake8 issues) |
| 2 | `refactor/pep8` | PEP8 formatting only: flake8 75 -> 0 issues, same output. Fast-forward merge into `main` |
| 3 | `feature/letter-grades` | Changed PASS/FAIL to A/B/C/F letter grades |
| 4 | `refactor/magic-number` | Replaced the magic number `60` with `PASS_MARK`; renamed `Result` to `get_result` |
| 5 | `main` | Merged both branches, which caused a merge conflict that I resolved by hand |
| 6 | `refactor/clean-code` | snake_case names, docstrings, `main()`, no global data, f-strings. Fast-forward merge |

## Git log

```text
* d525bf6 Refactor for clean code: snake_case names, docstrings, main(), no globals
*   625e164 Merge feature/letter-grades: keep letter grades, use named constants
|\  
| * d0ea912 Add letter grades (A/B/C/F) to the report
* | a70fd4a Replace magic number 60 with PASS_MARK; rename Result to get_result
|/  
* 6d47e72 Fix PEP8 formatting (flake8: 75 -> 0 issues)
* 2a05a81 Add initial student grades script
```

## Merge conflict

`feature/letter-grades` and `refactor/magic-number` both changed the `Result` function and the
report line, so merging them gave 2 conflict blocks.

Neither side was fully correct, so no single VS Code button worked:

- **Accept Current** kept `PASS_MARK` and `get_result`, but lost the letter grades and printed `result=`.
- **Accept Incoming** called `Result()`, which no longer existed after the rename (NameError).
- **Accept Both** would have printed every student twice.

**Resolution:** I combined both changes. I kept the letter grades and the new name `get_result`, and
replaced every threshold with a named constant (`GRADE_A = 90`, `GRADE_B = 75`, `PASS_MARK = 60`).

Git had also auto-merged `return "F"` outside the conflict markers. Accepting only the current side
would have produced `PASS` / `F`, a mix of both grading systems. So I reread the whole function and
ran the program to confirm the result was correct, not just conflict-free.

## Clean code changes

| Before | After | Why |
|---|---|---|
| `calc`, `printReport`, `topStudent` | `average`, `print_report`, `top_student` | Clear snake_case names |
| `n`, `a`, `t`, `r`, `s` | `name`, `avg`, `scores`, `raw_scores` | Meaningful variable names |
| Bare `60`, `90`, `75` | `PASS_MARK`, `GRADE_A`, `GRADE_B` | No magic numbers |
| `for i in range(len(l))` loop | `sum(scores) / len(scores)` | Simpler, uses a built-in |
| 10-line best-student loop | `max(..., key=...)` | One clear line |
| Functions read the global `data` | `students` is passed in | Self-contained, easy to test |
| `addStudent` printed errors itself | `add_student` raises `ValueError`; `main()` handles it | The caller decides what to do |
| No documentation | A docstring on every function | Says what each function does |
| Code at module level | `main()` function | A clear entry point |

The output is identical before and after every refactor (checked by running `python grades.py`).

## flake8 before (original code)

Checked on the first commit (`git show 2a05a81:grades.py | python -m flake8 -`), so the lines start
with `stdin:` instead of `grades.py:`. 75 issues in total.

```text
stdin:1:1: F401 'os' imported but unused
stdin:1:1: F401 'sys' imported but unused
stdin:1:10: E401 multiple imports on one line
stdin:1:10: E231 missing whitespace after ','
stdin:2:1: F401 'math' imported but unused
stdin:4:5: E225 missing whitespace around operator
stdin:4:12: E231 missing whitespace after ':'
stdin:4:16: E231 missing whitespace after ','
stdin:4:19: E231 missing whitespace after ','
stdin:4:23: E231 missing whitespace after ','
stdin:4:30: E231 missing whitespace after ':'
stdin:4:34: E231 missing whitespace after ','
stdin:4:37: E231 missing whitespace after ','
stdin:4:41: E231 missing whitespace after ','
stdin:4:48: E231 missing whitespace after ':'
stdin:4:52: E231 missing whitespace after ','
stdin:4:55: E231 missing whitespace after ','
stdin:4:59: E231 missing whitespace after ','
stdin:4:66: E231 missing whitespace after ':'
stdin:4:70: E231 missing whitespace after ','
stdin:4:73: E231 missing whitespace after ','
stdin:5:1: E302 expected 2 blank lines, found 0
stdin:5:10: E741 ambiguous variable name 'l'
stdin:6:6: E225 missing whitespace around operator
stdin:7:27: E701 multiple statements on one line (colon)
stdin:7:27: E231 missing whitespace after ':'
stdin:7:29: E225 missing whitespace around operator
stdin:9:1: E302 expected 2 blank lines, found 0
stdin:10:6: E225 missing whitespace around operator
stdin:11:9: E225 missing whitespace around operator
stdin:11:13: E701 multiple statements on one line (colon)
stdin:11:13: E231 missing whitespace after ':'
stdin:12:9: E701 multiple statements on one line (colon)
stdin:12:9: E231 missing whitespace after ':'
stdin:13:1: E302 expected 2 blank lines, found 0
stdin:14:28: E702 multiple statements on one line (semicolon)
stdin:14:28: E231 missing whitespace after ';'
stdin:16:10: E225 missing whitespace around operator
stdin:17:10: E225 missing whitespace around operator
stdin:18:41: E231 missing whitespace after ','
stdin:19:1: E302 expected 2 blank lines, found 0
stdin:20:9: E225 missing whitespace around operator
stdin:20:14: E702 multiple statements on one line (semicolon)
stdin:20:14: E231 missing whitespace after ';'
stdin:20:22: E225 missing whitespace around operator
stdin:22:10: E225 missing whitespace around operator
stdin:23:13: E225 missing whitespace around operator
stdin:24:20: E225 missing whitespace around operator
stdin:24:22: E702 multiple statements on one line (semicolon)
stdin:24:22: E231 missing whitespace after ';'
stdin:24:27: E225 missing whitespace around operator
stdin:25:12: E711 comparison to None should be 'if cond is None:'
stdin:25:12: E225 missing whitespace around operator
stdin:25:18: E701 multiple statements on one line (colon)
stdin:25:18: E231 missing whitespace after ':'
stdin:27:1: E302 expected 2 blank lines, found 0
stdin:28:10: E225 missing whitespace around operator
stdin:29:18: E701 multiple statements on one line (colon)
stdin:29:18: E231 missing whitespace after ':'
stdin:29:24: E225 missing whitespace around operator
stdin:31:1: E302 expected 2 blank lines, found 0
stdin:31:17: E231 missing whitespace after ','
stdin:33:10: E225 missing whitespace around operator
stdin:34:5: E722 do not use bare 'except'
stdin:37:12: E225 missing whitespace around operator
stdin:38:1: E305 expected 2 blank lines after class or function definition, found 0
stdin:38:12: E225 missing whitespace around operator
stdin:39:23: E231 missing whitespace after ','
stdin:39:29: E231 missing whitespace after ','
stdin:39:34: E231 missing whitespace after ','
stdin:40:21: E231 missing whitespace after ','
stdin:40:26: E231 missing whitespace after ','
stdin:42:80: E501 line too long (135 > 79 characters)
stdin:42:94: E231 missing whitespace after ','
stdin:43:53: E231 missing whitespace after ','
```

## flake8 after (final code)

```text
flake8 grades.py: 0 issues
```