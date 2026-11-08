"""Finite-field consistency checker for the geometric classification of the
projective singular support of the elementary symmetric cubic in characteristic 3.
The universal statement is established in the accompanying written proof.
"""
from itertools import product, combinations
from math import comb

P = 3

def normalize(v):
    for z in v:
        if z:
            c = pow(z, -1, P)
            return tuple((c*t) % P for t in v)
    return None

def singular_by_equations(v):
    # Elementary symmetric coefficients by a direct generating-series algorithm.
    e = [1,0,0,0]
    for z in v:
        for j in (3,2,1):
            e[j]=(e[j]+z*e[j-1])%P
    e1,e2,e3 = e[1:]
    return e3 == 0 and all((e2-z*e1+z*z)%P==0 for z in v)

def geometric_prediction_over_f3(n):
    got=set()
    for m in range(1,n+1):
        if m%9!=1:continue
        for subset in combinations(range(n),m):
            s=set(subset)
            got.add(normalize(tuple(int(i in s) for i in range(n))))
    if n%9==2:
        for m in range(1,n//2+1):
            if m%9!=1 or (n-m)%9!=1:continue
            for subset in combinations(range(n),m):
                s=set(subset)
                for x,y in product(range(P),repeat=2):
                    if x==y==0:continue
                    got.add(normalize(tuple(x if i in s else y for i in range(n))))
    elif n%9 in (5,8):
        residue=7 if n%9==5 else 4
        for m in range(1,n//2+1):
            if m%9!=residue or (n-m)%9!=residue:continue
            for subset in combinations(range(n),m):
                s=set(subset)
                got.add(normalize(tuple(1 if i in s else 2 for i in range(n))))
    return got

def all_projective_points(n):
    for first in range(n):
        for tail in product(range(P), repeat=n-first-1):
            yield (0,)*first+(1,)+tail

def test():
    # Exact polynomial coefficients, not a sampling of field elements.
    for a in range(1,61,3):
        for b in range(1,61,3):
            assert (comb(a,3)%3, comb(a,2)*b%3, a*comb(b,2)%3, comb(b,3)%3) == ((a-1)//3%3,0,0,(b-1)//3%3)
    for n in range(3,12):
        actual={v for v in all_projective_points(n) if singular_by_equations(v)}
        expected=geometric_prediction_over_f3(n)
        assert actual==expected, (n,len(actual),len(expected),list(actual^expected)[:3])
        print(f'n={n}: singular F3-projective points={len(actual)}; predicted={len(expected)}')
    assert len(geometric_prediction_over_f3(8))==8+comb(8,4)//2==43
    assert len(geometric_prediction_over_f3(11))==11*4-10==34
    print('CERTIFICATE_OK')
if __name__=='__main__': test()
