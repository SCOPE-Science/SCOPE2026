#!/usr/bin/env python3
"""Recompute every coefficient and both finite certificates from exact integer programs."""
from pathlib import Path
import tempfile,subprocess

here=Path(__file__).resolve().parent
with tempfile.TemporaryDirectory(prefix='strong_tournament_check_') as dirname:
    d=Path(dirname)
    for name,exe in [('verify_tournament_enumeration.cpp','enum'),('verify_tournament_scc.cpp','scc')]:
        subprocess.run(['g++','-std=c++17','-O3',str(here/name),'-o',str(d/exe)],check=True)
    subprocess.run([str(d/'enum'),'--dump',str(d/'enum.txt'),'--orbits',str(d/'orbits.tsv')],check=True)
    subprocess.run([str(d/'scc'),'--dump',str(d/'scc.txt')],check=True)
    expected=(here/'walsh_coefficients.txt').read_bytes()
    assert (d/'enum.txt').read_bytes()==expected
    assert (d/'scc.txt').read_bytes()==expected
    assert (d/'orbits.tsv').read_bytes()==(here/'tournament_support_orbits.tsv').read_bytes()
print('Complete 32768-character spectrum and 156 orbit classes: exact agreement.')
