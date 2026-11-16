"""Exact direct independent Fourier enumeration for proper four-colour book graphs.
Run: python3 verify_book_direct.py
No third-party dependencies.
"""
from itertools import product
from collections import Counter

I=(1+0j,0+1j,-1+0j,0-1j)

def char(group,frequency,color):
    if group=='C4':return I[(frequency*color)%4]
    return 1 if ((frequency&1)&(color&1))^(((frequency>>1)&1)&((color>>1)&1))==0 else -1

def direct(group,n):
    # All frequency characters, all 12*2**n proper colourings, exact Gaussian integer sums.
    F=[z for z in product(range(4),repeat=n+2)]
    palette=range(4)
    colors=[(a,b)+leaves for a in palette for b in palette if a!=b
            for leaves in product([c for c in palette if c not in (a,b)],repeat=n)]
    norms=Counter()
    zeros_balanced=0
    for f in F:
        re=im=0
        for col in colors:
            z=1+0j
            for k,v in zip(f,col):z*=char(group,k,v)
            re+=int(z.real);im+=int(z.imag)
        mag=abs(re)+abs(im)
        assert re==0 or im==0,(group,n,f,re,im)
        norms[mag]+=1
        if mag==0 and (sum(f)%4==0 if group=='C4' else __import__('functools').reduce(lambda a,b:a^b,f,0)==0):zeros_balanced+=1
    return len(colors),norms,zeros_balanced

def expected(group,n):
    if group=='C4': return 4*2**n+3*3**n-(-1)**n-2,2**(n//2+3),12*2**n
    return 12*2**n-8,4*2**n,12*2**n

for group in ('C4','V4'):
    for n in (1,2,3,4):
        configs,levels,zb=direct(group,n)
        rank=sum(v for x,v in levels.items() if x)
        low=min(x for x in levels if x)
        high=max(levels)
        assert configs==12*2**n
        assert (rank,low,high)==expected(group,n),(group,n,rank,low,high,expected(group,n))
        assert zb==4**(n+1)-rank
        print(group,n,rank,low,high,sorted(levels.items()))
print('PASS: independent exact direct Fourier enumeration for both palette groups, n=1..4')
