"""Exact enumeration of the antiferromagnetic Ising Möbius ladder (no external inputs)."""
from itertools import product

def edges(n):
    # 0..n-1 are top; n..2n-1 are bottom
    es = [(i, n+i) for i in range(n)]
    es += [(i, i+1) for i in range(n-1)]
    es += [(n+i,n+i+1) for i in range(n-1)]
    es += [(n-1,n),(2*n-1,0)]
    assert len(es) == 3*n and len(set(tuple(sorted(x)) for x in es))==3*n
    return es

def energy_e2(n,es,mask,B):
    f=sum(int(((mask>>a)&1)==((mask>>b)&1)) for a,b in es)
    plus=2*n-mask.bit_count()
    minus=mask.bit_count()
    magnet=plus-minus
    return 2*(2*f-3*n)-B*magnet

def pred(n,B):
    # B = 2|h|/J, twice energy
    return min([2*(-3*n), 2*(3*n)-2*n*B] if n%2 else
               [2*(-3*n+4), 2*(-3*n+6)-2*B,2*(3*n)-2*n*B])

def independent_count(n):
    a,b=2,2
    for _ in range(2,n+1):a,b=b,2*b+a
    return b-(-1)**n

def pred_deg(n,B):
    if n%2: return independent_count(n) if B==6 else (2 if B<6 else 1)
    if B<2: return 2*n
    if B==2: return 4*n
    if B<6: return 2*n
    if B==6: return independent_count(n)
    return 1

for n in range(3,10):
    es=edges(n)
    for B in (0,1,2,3,4,5,6,7,8):
        best=None; multiplicity=0
        for m in range(1<<(2*n)):
            ee=energy_e2(n,es,m,B)
            if best is None or ee<best:best,multiplicity=ee,1
            elif ee==best:multiplicity+=1
        assert (best,multiplicity)==(pred(n,B),pred_deg(n,B)),(n,B,(best,multiplicity),(pred(n,B),pred_deg(n,B)))
    print(f'n={n}: 9-field checks passed, all {1<<(2*n)} configurations exhaustively checked')
print('ALL_EXHAUSTIVE_CHECKS_PASS')
