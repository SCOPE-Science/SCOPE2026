#!/usr/bin/env python3
"""Finite independent checks for truncated characteristic-two algebra retractions."""
from itertools import product
from math import prod
from pathlib import Path
import shutil
import subprocess
import tempfile


def gl(n, q):
    return prod(q**n-q**i for i in range(n))


def count(n, r, q):
    s = n-r
    exponent = n*(2**n-1-n)-r*(2**r-1-r)-s*(2**n-2**r-s)
    assert exponent >= 0
    return (gl(n,q)//(gl(r,q)*gl(s,q)))*q**exponent


def field_mul(a,b,q):
    if q == 2:
        return a&b
    assert q == 4
    p = 0
    for i in range(2):
        for j in range(2):
            if (a>>i)&(b>>j)&1:
                p ^= 1<<(i+j)
    return p^7 if p&4 else p


def poly_mul(a,b,q):
    c=[0]*4
    for i in range(4):
        for j in range(4):
            if (i&j)==0:
                c[i|j]^=field_mul(a[i],b[j],q)
    return tuple(c)


def brute_two(q):
    all_nilpotents=[(0,a,b,c) for a,b,c in product(range(q),repeat=3)]
    counts=[0,0,0]
    for a,b in product(all_nilpotents,repeat=2):
        ab=poly_mul(a,b,q)
        def evaluate(x):
            return tuple((x[0] if j==0 else 0)^field_mul(x[1],a[j],q)
                         ^field_mul(x[2],b[j],q)^field_mul(x[3],ab[j],q)
                         for j in range(4))
        if evaluate(a)!=a or evaluate(b)!=b:
            continue
        A,B,C,D=a[1],a[2],b[1],b[2]
        det=field_mul(A,D,q)^field_mul(B,C,q)
        rank=2 if det else (1 if A or B or C or D else 0)
        counts[rank]+=1
    return counts


def run():
    for q in [2,4]:
        got=brute_two(q)
        expected=[count(2,r,q) for r in range(3)]
        assert got==expected,(q,got,expected)
        print('n=2 q=',q,'cotangent-rank counts=',got)
    cpp=Path(__file__).resolve().with_name('verify.cpp')
    if shutil.which('g++') and cpp.exists():
        with tempfile.TemporaryDirectory() as d:
            exe=Path(d)/'run'
            subprocess.run(['g++','-std=c++17','-O2',str(cpp),'-o',str(exe)],check=True,timeout=60)
            result=subprocess.run([str(exe)],capture_output=True,text=True,check=True,timeout=120)
        expected='\n'.join(' '.join([str(n)]+[str(count(n,r,2)) for r in range(n+1)]) for n in range(1,4))+'\n'
        assert result.stdout==expected,(result.stdout,expected)
        print('n=1,2,3 over F_2 exhaustive independent C++ enumeration:',result.stdout.strip().replace('\n','; '))
    else:
        print('C++ compiler absent; n=3 exhaustive check not run')
    for n in [64,100,256]:
        t=n.bit_length()-1
        def phi(s):
            return (n-s)*2**n+(2*s-n)*2**(n-s)-s
        maximizer=max(range(n+1),key=phi)
        assert t-2<=maximizer<=t+2
    print('VERIFY_OK')

if __name__=='__main__':
    run()
