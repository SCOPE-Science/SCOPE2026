#!/usr/bin/env python3
"""Compile and compare independent exhaustive enumeration with symbolic polynomial."""
from pathlib import Path
import subprocess
from formula_check import polynomial
root=Path(__file__).resolve().parent
exe=root/'direct_checker_temp'
try:
    subprocess.run(['g++','-O3','-std=c++17',str(root/'direct_enumeration.cpp'),'-o',str(exe)],check=True)
    for n in range(3,7):
        output=subprocess.check_output([str(exe),str(n)],text=True)
        row=output.strip().split(' poly:')[1]
        direct={int(part.split(':')[0]):int(part.split(':')[1]) for part in row.split()}
        symbolic={i:c for i,c in enumerate(polynomial(n)) if c}
        assert direct==symbolic,(n,direct,symbolic)
        print(f'COEFFICIENTWISE_OK n={n}, {len(direct)} nonzero coefficients')
    print('CROSSCHECK_OK')
finally:
    if exe.exists(): exe.unlink()
