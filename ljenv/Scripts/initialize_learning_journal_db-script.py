#!C:\Users\moshoaib\Documents\UWPCE_PP2\session01\projects\learning-journal\ljenv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'learning-journal==0.0','console_scripts','initialize_learning_journal_db'
__requires__ = 'learning-journal==0.0'
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.exit(
        load_entry_point('learning-journal==0.0', 'console_scripts', 'initialize_learning_journal_db')()
    )
