#!/usr/bin/env python3
"""Replay two complete finite enumerations and the exact field-envelope check."""
import pathlib
import subprocess
import tempfile
from fractions import Fraction

HERE = pathlib.Path(__file__).resolve().parent
MINIMA = [15,12,9,6,3,3,3,6,9,12,15,21,27,33,39,45]
MULT = [882,2400,1920,600,60,60,60,600,1200,600,192,480,640,240,30,1]

def read_table(text):
    lines = text.splitlines()
    assert 'total 14348907' in lines or 'Total 14348907 min 3 solutions 180' in lines
    tab = {}
    for line in lines:
        fields = line.split()
        if len(fields)==3 and all(x.isdigit() for x in fields):
            x,y,z = map(int,fields)
            if 0 <= x <= 15:
                tab[x] = (y,z)
    assert len(tab)==16,tab
    assert [tab[i][0] for i in range(16)] == MINIMA
    assert [tab[i][1] for i in range(16)] == MULT
    return tab

with tempfile.TemporaryDirectory(prefix='potts_exact_') as td:
    tables=[]
    for source in ('recursion.cpp','subsets.cpp'):
        exe=str(pathlib.Path(td)/source.replace('.cpp',''))
        subprocess.run(['g++','-std=c++17','-O3',str(HERE/source),'-o',exe],check=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        completed=subprocess.run([exe],check=True,text=True,capture_output=True,timeout=90)
        tables.append(read_table(completed.stdout))
        if source=='subsets.cpp':
            assert 'FAMILY 180' in completed.stdout
            assert 'pattern 4,5,6 180' in completed.stdout
    assert tables[0]==tables[1]

def minimizers(x):
    vals = [Fraction(MINIMA[n])-x*n for n in range(16)]
    z=min(vals)
    return [n for n,v in enumerate(vals) if v==z]
for x,n in [(Fraction(-4),[0]),(Fraction(-2),[4]),(Fraction(1),[6]),(Fraction(4),[10]),(Fraction(7),[15])]:
    assert minimizers(x)==n, (x,minimizers(x))
for x,ns,deg in [(Fraction(-3),list(range(0,5)),5862),
                 (Fraction(0),[4,5,6],180),
                 (Fraction(3),list(range(6,11)),2652),
                 (Fraction(6),list(range(10,16)),1583)]:
    assert minimizers(x)==ns,(x,minimizers(x))
    assert sum(MULT[i] for i in ns)==deg
# Exact half-space coverage, not merely sample-point assertions.
# Each affine branch can be minimal only inside the intersection of pairwise
# linear inequalities. Compute these rational intervals for all 16 sectors.
N=16
bands={}
for n in range(N):
    lo,hi=None,None
    for m in range(N):
        if n==m:continue
        ratio=Fraction(MINIMA[n]-MINIMA[m],n-m)
        if m<n:lo=ratio if lo is None else max(lo,ratio)
        else:hi=ratio if hi is None else min(hi,ratio)
    if lo is None or hi is None or lo<=hi:
        bands[n]=(lo,hi)
assert [n for n,(lo,hi) in bands.items() if lo is None or hi is None or lo<hi]==[0,4,6,10,15]
assert bands[0][1]==-3 and bands[4]==(Fraction(-3),Fraction(0))
assert bands[6]==(Fraction(0),Fraction(3))
assert bands[10]==(Fraction(3),Fraction(6)) and bands[15][0]==6
print('VERIFIED: both 3^15 censuses, all 16 sectors, structural family 180, exact field envelope and degeneracies')
