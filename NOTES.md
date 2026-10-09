
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

## flake8 before (original code)
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
Checked on the first commit (`git show 2a05a81:grades.py | python -m flake8 -`), so lines start with `stdin:` instead of `grades.py:`. 75 issues in total.