from pathlib import Path

ROOT_DIR = Path('c:/temp/temp2/')
WORK_DIR = ROOT_DIR.joinpath('projectjournal')
PHD_DIR = WORK_DIR.joinpath('phd')
CLANG_DIR = PHD_DIR.joinpath('compilers', 'llvm', 'clang')

if ROOT_DIR.exists():
    print(f'ROOT_DIR exist at {ROOT_DIR}')
else:
    print("ROOT_DIR doesn't exist")

if CLANG_DIR.exists():
    print(f'CLANG_DIR exist at {CLANG_DIR}')
else:
    print("CLANG_DIR doesn't exist")

print('\n\nprintout of values:')
print(f'ROOT_DIR.exists() is {ROOT_DIR.exists()}')
print(f'ROOT_DIR.is_dir() is {ROOT_DIR.is_dir()}')
print(f'CLANG_DIR.exists() is {CLANG_DIR.exists()}')
print(f'CLANG_DIR.is_dir() is {CLANG_DIR.is_dir()}')













# scratch   ///////////////
import os
print('start')
ROOT_DIR = os.path.abspath('/temp/temp2/') #Path(__file__).resolve().parent.parent.parent.parent.parent.parent.parent.parents
WORK_DIR = ROOT_DIR.join('projectjournal')
PHD_DIR = WORK_DIR.join('phd')
CLANG_DIR = PHD_DIR.join('test')
print(f' ROOT_DIR= {ROOT_DIR}')
print(f' WORK_DIR= {WORK_DIR}')
print(f' CLANG_DIR= {CLANG_DIR}')
print(f' using os.path CLANG_DIR= {CLANG_DIR}')
print()

from pathlib import Path

ROOT_DIR = Path('c:/temp/temp2/') #Path(__file__).resolve().parent.parent.parent.parent.parent.parent.parent.parents
WORK_DIR = ROOT_DIR.joinpath('projectjournal')
PHD_DIR = WORK_DIR.joinpath('phd')
CLANG_DIR = PHD_DIR.joinpath('compilers', 'llvm', 'clang')
print(f' ROOT_DIR= {ROOT_DIR}')
print(f' using pathlib CLANG_DIR= {CLANG_DIR}')
print(type(CLANG_DIR))
print(CLANG_DIR)
print(f'data type of CLANG_DIR.is_dir() is {type(CLANG_DIR)}')

if ROOT_DIR.exists():
    print('ROOT_DIR exist')
else:
    print("ROOT_DIR doesn't exist")

if CLANG_DIR.exists():
    print('CLANG_DIR exist')
else:
    print("CLANG_DIR doesn't exist")

