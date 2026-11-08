from collections import defaultdict
from itertools import product

def nu2(x):
    return (x&-x).bit_length()-1

def templ(m,k,j,c):
    L=1<<k
    return tuple(c if i==j else nu2(abs(i-j))%m for i in range(L))

def count(m,k):
    L=1<<k
    tab=defaultdict(list)
    for j in range(L):
        for c in range(m):
            tab[templ(m,k,j,c)].append((j,c))
    pairs=[v for v in tab.values() if len(v)>1]
    expected={tuple(sorted(((j,(k-1)%m),(j+L//2,(k-1)%m)))) for j in range(L//2)}
    actual={tuple(sorted(p)) for p in pairs}
    assert actual==expected,(m,k,len(actual),len(expected),actual^expected)
    assert len(tab)==(2*m-1)*L//2,(m,k,len(tab))
    allv=set(tab)
    assert all(v[::-1] in allv for v in allv)
    pal=sum(v==v[::-1] for v in allv)
    assert pal==(1 if k==1 else 0),(m,k,pal)
    r=len({min(v,v[::-1]) for v in allv})
    assert r== (m if k==1 else (2*m-1)*L//4),(m,k,r)
    if m<=5 and k<=5:
        size=1<<(k+m+2)
        sequence=tuple(nu2(i+1)%m for i in range(size))
        seen={sequence[i:i+L] for i in range(size-L+1)}
        assert seen==allv,(m,k,len(seen),len(allv))
    return len(tab)

for m in range(2,9):
    for k in range(1,9):
        count(m,k)
print('ALL 56 exact collision, formula, palindrome, reversal cases passed; 20 independent finite prefix comparisons passed.')
