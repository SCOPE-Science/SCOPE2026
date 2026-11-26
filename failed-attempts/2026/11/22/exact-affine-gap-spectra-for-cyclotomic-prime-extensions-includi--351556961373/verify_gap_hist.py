"""Exact, self-contained coefficient-support gap certificate for Phi_(15p).
Run with: python3 verify_gap_hist.py
No third-party packages are required. All arithmetic is integral.
"""
from collections import Counter
from math import gcd

M = 15
A = (1, -1, 0, 1, -1, 1, 0, -1, 1)
U = (1, 1, 1, 0, 0, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0)
# Gap histogram entries are indexed by length 1,...,8.
TABLE = {
 1: ((10,4,10,2,4,0,4,2), (10,4,10,2,4,0,4,2)),
 2: ((42,16,2,0,0,4,0,2), (46,18,2,0,0,4,0,2)),
 4: ((58,12,2,4,0,0,0,2), (74,16,2,4,0,0,0,2)),
 7: ((50,6,14,0,0,0,0,2), (72,10,20,0,0,0,0,2)),
 8: ((50,6,14,0,0,0,0,2), (78,8,22,0,0,0,0,2)),
11: ((58,12,2,4,0,0,0,2), (100,20,4,8,0,0,0,2)),
13: ((42,16,2,0,0,4,0,2), (80,30,4,0,0,8,0,2)),
14: ((10,4,10,2,4,0,4,2), (20,8,20,4,8,0,8,2)),
}

def verify_u_identity():
    product = [0] * (M + 1 + len(A))
    for i, ai in enumerate(A):
        for j, uj in enumerate(U):
            product[i+j] += ai * uj
    assert product[:M+1] == [1]+[0]*(M-1)+[-1]
    assert not any(product[M+1:])

def quotient_by_long_division(t):
    """F_t = Phi_15(x**t)/Phi_15(x), no factorization package."""
    d = len(A)-1
    D = d*(t-1)
    q = [0]*(D+1)
    for k in range(D+1):
        b = A[k//t] if k % t == 0 and k//t <= d else 0
        q[k] = b - sum(A[i]*q[k-i] for i in range(1,min(d,k)+1))
    # Check all coefficients including tail after degree D.
    for k in range(d*t+1):
        lhs = sum(A[i]*q[k-i] for i in range(d+1) if 0<=k-i<=D)
        rhs = A[k//t] if k % t == 0 and k//t <= d else 0
        assert lhs == rhs,(t,k)
    return q

def block_formula(t):
    d = len(A)-1
    D = d*(t-1)
    return [sum(A[i]*U[(k-i*t)%M] for i in range(min(d,k//t)+1)) for k in range(D+1)]

def histogram(coeffs):
    s = [i for i,c in enumerate(coeffs) if c]
    assert s[0]==0 and s[-1]==len(coeffs)-1
    return Counter(y-x for x,y in zip(s,s[1:]))

def cyclic_slope(r):
    ans = Counter()
    for j in range(len(A)-1):
        word = [sum(A[i]*U[(s-i*r)%M] for i in range(j+1)) for s in range(M)]
        supp = [s for s,v in enumerate(word) if v]
        assert supp,(j,r)
        ans.update((supp[(i+1)%len(supp)]-supp[i])%M or M for i in range(len(supp)))
    assert not (set(ans) - set(range(1,len(A))))
    return tuple(ans[i] for i in range(1,len(A)))

def main():
    verify_u_identity()
    count = 0
    for r, (alpha, base) in TABLE.items():
        assert gcd(r,M)==1
        assert cyclic_slope(r)==alpha,(r,'slope')
        for Q in range(1,16):
            t=M*Q+r
            first = quotient_by_long_division(t)
            assert first == block_formula(t),(r,Q,'independent formulas')
            h=histogram(first)
            want=tuple(base[k]+(Q-1)*alpha[k] for k in range(8))
            got=tuple(h[k+1] for k in range(8))
            assert got==want,(r,Q,got,want)
            assert sum((k+1)*got[k] for k in range(8))==8*(t-1)
            assert not (set(h)-set(range(1,9)))
            assert got[7]==2*Q
            count+=1
    print('PASS: 1 symbolic polynomial identity, 8 cyclic slopes,',count,
          'exact polynomial divisions, complete gap histograms and degree sums.')

if __name__=='__main__':
    main()
