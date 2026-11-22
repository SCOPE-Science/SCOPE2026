#!/usr/bin/env python3
"""Run both exhaustive orbit algorithms and the full spatial group computation."""
import pathlib, subprocess, tempfile
root=pathlib.Path(__file__).resolve().parent
for script in ('census.py','symmetry.py'):
    subprocess.run(['python3',str(root/script)],check=True)
with tempfile.TemporaryDirectory() as work:
    exe=pathlib.Path(work)/'floyd_check'
    subprocess.run(['g++','-std=c++17','-O2',str(root/'independent.cpp'),'-o',str(exe)],check=True)
    subprocess.run([str(exe)],check=True)
print('ALL_EXHAUSTIVE_CHECKS_OK')
