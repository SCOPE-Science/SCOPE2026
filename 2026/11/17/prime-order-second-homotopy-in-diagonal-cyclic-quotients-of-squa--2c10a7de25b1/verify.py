"""Finite combinatorial checks for cyclic matching-complex quotients.

Uses only the Python standard library. The topological proof is documented
separately; finite enumerations are not used as proofs for all primes.
"""
from itertools import combinations, permutations
from math import comb, factorial


def faces(p):
    for k in range(1, p+1):
        for rows in combinations(range(p),k):
            for cols in combinations(range(p),k):
                for perm in permutations(cols):
                    yield tuple(sorted(zip(rows,perm)))

def shift(f,p,t=1):
    return tuple(sorted((((i+t)%p),((j+t)%p)) for i,j in f))

def check(p):
    sizes=[0]*p
    fixed=[]
    total=0
    for f in faces(p):
        total+=1
        sizes[len(f)-1]+=1
        if shift(f,p)==f:
            fixed.append(f)
    expected=[comb(p,k)**2*factorial(k) for k in range(1,p+1)]
    assert sizes==expected,(p,sizes,expected)
    assert len(fixed)==p
    assert all(len(f)==p for f in fixed)
    wanted={tuple(sorted((i,(i+a)%p) for i in range(p))) for a in range(p)}
    assert set(fixed)==wanted
    assert total==sum(expected)
    # A cyclic p-cycle on the vertices of each invariant (p-1)-simplex:
    # local tangent is the reduced real permutation module, with complex
    # weights 1,...,(p-1)/2, all coprime to p.
    weights=tuple(range(1,(p+1)//2))
    assert len(weights)*2 ==p-1 and all(0<w<p for w in weights)
    euler=sum((-1)**k*sizes[k] for k in range(p))
    quotient_euler=(euler+(p-1)*p)//p
    assert (euler+(p-1)*p)%p==0
    return {"p":p,"face_counts_by_dimension":sizes,"total_nonempty_faces":total,
            "fixed_face_count":len(fixed),"fixed_face_size":p,
            "normal_weights":list(weights),"euler_original":euler,
            "euler_quotient":quotient_euler}

if __name__=='__main__':
    for p in (5,7):
        print(check(p))
    print('DIAGONAL_CHESSBOARD_PRIME_FIXED_FACETS_PASS')
