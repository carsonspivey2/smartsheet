# Smartsheets
Find PCR sheets and update them with _automation section_ from template-sheet

## Setup
1. Open your command line tool/terminal and `cd` to a parent directory where you store code
2. Copy this repo with `git clone https://github.com/carsonspivey2/smartsheet`
    > This creates a new `smartsheet` sub-directory including the repo contents/files)
2. Change directory with `cd smartsheet`
3. Install `python3` and `pip` locally
4. Run `pip install smartsheet-python-sdk`
5. To view data, run a get script such as `python3 get_sheet_template.py`
6. To test getting PCR sheets and view counts, run `python3 list_projects.py`
7. To run migration test 1, run `python3 copy_test1.py`
8. To run migration test 2, run `python3 copy_test2.py`
9. To run the full migration, run `python3 copy_automation.py`

## Requires
Python 3.x
