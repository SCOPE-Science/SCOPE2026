"""Independent compressed Fourier transform via a three-term character formula.
Run: python3 verify_book_formula.py
No third-party dependencies.
"""
from itertools import product
from collections import Counter
I=(1,1j,-1,-1j)

def phase(g,k,x):
    if g=='C4': return I[(k*x)%4]
    return (-1)**(((k&1)&(x&1)) ^ (((k>>1)&1)&((x>>1)&1)))

def compressed(g,n):
    levels=Counter()
    for leaf in product(range(4),repeat=n):
        for beta in range(4):
            # Translationally balanced root frequency is fixed uniquely.
            W=0j
            for d in (1,2,3):
                term=phase(g,beta,d)
                for k in leaf:
                    q=2 if k==0 else -1-phase(g,k,d)
                    term*=q
                W+=term
            W*=4
            assert round(W.real)==W.real and round(W.imag)==W.imag
            assert not(round(W.real) and round(W.imag))
            levels[abs(round(W.real))+abs(round(W.imag))]+=1
    return levels

def expected(g,n):
    if g=='C4':
        return 4*2**n+3*3**n-(-1)**n-2,2**(n//2+3),12*2**n
    return 12*2**n-8,2**(n+2),12*2**n
for g in ('C4','V4'):
    for n in range(1,9):
        levels=compressed(g,n)
        rank=sum(v for k,v in levels.items() if k)
        minimum=min(k for k in levels if k)
        maximum=max(levels)
        assert (rank,minimum,maximum)==expected(g,n),(g,n,rank,minimum,maximum,expected(g,n))
        assert sum(levels.values())==4**(n+1)
        print(g,n,rank,minimum,maximum)
print('PASS: all balanced characters checked through n=8, both groups')
