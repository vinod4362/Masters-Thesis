# Experimental Tasks Package

This package contains five programming tasks used to compare GitHub Copilot and ChatGPT.
Each task folder includes: `spec.md`, starter code, and (where applicable) a `tests/` folder.

## Tasks
1. task1_quicksort – Implement QuickSort with CLI
2. task2_flask_api – Build a minimal Todo REST API with Flask
3. task3_debugging – Fix a buggy Fibonacci implementation
4. task4_unit_tests – Write pytest unit tests for a text normalizer
5. task5_web_form – Implement a web form with client-side validation

## Evaluation Overview
- Code Quality: static analysis + manual expert review
- Efficiency: time, iterations, error counts
- Usability/Adaptability: post-task ratings + short interview

## Running Notes
- Task 1/3/4: Python 3.10+ recommended; pytest for tests.
- Task 2: `pip install -r requirements.txt` then `python app.py`.
- Task 5: Open `index.html` in a browser.

Logs to collect per participant and task:
- Start/end timestamps, number of runs, test outcomes, static analysis reports, prompts/queries (anonymized).
