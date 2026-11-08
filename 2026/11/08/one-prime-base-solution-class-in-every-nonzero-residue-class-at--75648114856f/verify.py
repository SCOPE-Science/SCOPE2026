"""Finite corroboration of prime-base congruence residue-class lifting."""
from math import comb

def residue(p, a, q):
    m=p**a
    # Each j=p^v*u with p not dividing u; evaluate each p-integral factor modulo m.
    prod=q % m
    for j in range(1,m):
        u=j; v=0
        while u%p==0:
            u//=p; v+=1
        factor=(1+(q-1)*p**(a-v)*pow(u,-1,m))%m
        prod=(prod*factor)%m
    return (prod-pow(q,m,m))%m

for p,maxa in [(2,6),(3,5),(5,4),(7,3)]:
    roots_prev=None
    for a in range(1,maxa+1):
        m=p**a
        roots=[q for q in range(m) if residue(p,a,q)==0]
        assert len(roots)==p and set(x%p for x in roots)==set(range(p))
        assert roots[0]==0 and 1 in roots
        if roots_prev is not None:
            assert set(x% (m//p) for x in roots)==set(roots_prev)
        roots_prev=roots
        if m<=49:
            for q in range(1,12):
                assert (comb(q*m,m)-pow(q,m))%m==residue(p,a,q)
        print(f'CLASS_OK p={p} a={a} m={m} roots={roots}')
print('VERIFY_OK exact_integer_arithmetic finite_only=True')
