"""Exact rational check of high-threshold prime-period orbit staircase."""
from fractions import Fraction

def necklace(w):
    return min(w[i:]+w[:i] for i in range(len(w)))

def prime(w):
    return all(w != w[j:]+w[:j] for j in range(1,len(w)))

def triple(m):
    q,r=divmod(m,3)
    if r==0: gaps=(q-1,q+1,q)
    elif r==1: gaps=(q,q,q+1)
    else: gaps=(q,q+1,q+1)
    return necklace(''.join('0'+'1'*(g-1) for g in gaps))

checks=0
for m in range(4,19):
    den=2**m-1
    words=sorted({necklace(f'{j:0{m}b}') for j in range(1,2**m-1) if prime(f'{j:0{m}b}')},reverse=True)
    e=(m-1)//3;dmax=(m-1)//2
    initial=['0'+'1'*(m-1)]+['0'+'1'*(d-1)+'0'+'1'*(m-d-1) for d in range(dmax,e-1,-1)]
    expected=len(initial)
    assert words[:expected]==initial,(m,words[:expected],initial)
    u=triple(m)
    assert words[expected]==u,(m,u,words[expected])
    assert u.count('0')==3 and prime(u)
    for d in range(e,dmax+1):
        w='0'+'1'*(d-1)+'0'+'1'*(m-d-1)
        val=Fraction(int(w,2),den)
        assert val>Fraction(int(u,2),den)
        checks+=1
    checks+=3
print(f'VERIFY_OK lengths=4..18 exact_primitive_necklace_orders=15 endpoint_comparisons={checks}')
