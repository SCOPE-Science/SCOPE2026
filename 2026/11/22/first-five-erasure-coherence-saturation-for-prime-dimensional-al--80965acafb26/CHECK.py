"""Exact finite certificates for the onset of five-erasure Alltop coherence.

Run `python CHECK.py` with Python 3.10+ and NumPy.
The program exhausts the small excluded prime-field cases, verifies explicit
witnesses for all smaller primes needed by the general analytic argument,
and checks the actual finite Gabor Gram matrices.
"""
from itertools import combinations
from math import sqrt, pi
import cmath
import numpy as np

EXCLUDED = (5, 13, 17)
# Every admissible prime below the analytic threshold 109 except exclusions.
WITNESSES = {
 29: (0, 1, 3, 5, 19),
 37: (0, 1, 4, 6, 18),
 41: (0, 1, 2, 10, 33),
 53: (0, 1, 3, 32, 37),
 61: (0, 1, 4, 32, 33),
 73: (0, 1, 2, 3, 4),
 89: (0, 1, 2, 10, 11),
 97: (0, 1, 2, 3, 96),
101: (0, 1, 3, 5, 97),
}

def chi(x, p):
    x %= p
    if x == 0:
        return 0
    return 1 if pow(x, (p-1)//2, p)==1 else -1

def triangle_positive(q, p):
    for a,b,c in combinations(q,3):
        if chi((b-a)*(c-b)*(c-a),p)!=1:
            return False
    return True

def vector(p,a,b):
    return np.array([cmath.exp((2j*pi/p)*(((x-a)**3+b*x)%p))
                     for x in range(p)], dtype=complex)/sqrt(p)

def check_actual_matrix(p,slopes):
    # In the quadratic-chirp parametrization, choose the line B=0.
    V=[]
    for A in slopes:
        a=(-A*pow(3,-1,p))%p
        b=(-3*a*a)%p
        V.append(vector(p,a,b))
    G=np.stack(V).conj()@np.stack(V).T
    e=np.linalg.eigvalsh(G)
    expected=np.array([1-1/sqrt(p)]*4+[1+4/sqrt(p)])
    assert max(abs(e-expected))<3e-10,(p,slopes,e)
    # Complete frame is exactly p-tight; the complement norm follows.
    full=np.column_stack([vector(p,a,b) for a in range(p) for b in range(p)])
    assert max(abs((full@full.conj().T-p*np.eye(p)).ravel())) < 4e-11
    return float(e[-1])

def main():
    exhausted = 0
    for p in EXCLUDED:
        for five in combinations(range(p),5):
            assert not triangle_positive(five,p),('unexpected coherent set',p,five)
            exhausted+=1
    gram_count=0
    for p, A in WITNESSES.items():
        assert len(set(A))==5 and all(0<=x<p for x in A)
        assert triangle_positive(A,p),(p,A)
        check_actual_matrix(p,A)
        gram_count+=1
        print('witness',p,tuple(A))
    # The list exhausts every eligible prime below the large-prime
    # character-sum plus Hoffman threshold 109.
    def is_prime(n):
        return n>=2 and all(n%d for d in range(2,int(n**.5)+1))
    expected=[p for p in range(5,109) if is_prime(p) and p%4==1]
    assert sorted(EXCLUDED+tuple(WITNESSES))==expected
    print(f'CHECK_OK excluded_five_sets={exhausted} explicit_witnesses={gram_count}')

if __name__=='__main__':
    main()
