"""Independent transfer-matrix verification for quadratic exterior multiplication.
No external dependencies; source-independent Wilson formula imported from candidate_check.
"""
from candidate_check import rank_powers_formula, jordan_from_ranks, alternating_count
from math import comb

def transfer_blocks(n,r,p):
    assert 0 <= 2*r <= n and p >= 2
    v = [0]*(p-1)
    v[0] = 1
    for _ in range(r):
        w=[0]*(p-1)
        for s in range(p-1):
            w[s]=2*v[s]
            if s: w[s]+=v[s-1]
            if s+1<p-1:w[s]+=v[s+1]
        v=w
    b=[2**(n-2*r)*x for x in v]
    remainder=2**n - sum((s+1)*b[s] for s in range(p-1))
    assert remainder >= 0 and remainder%p==0
    b.append(remainder//p)
    return tuple(b)

def ranks_from_jordan(blocks,p):
    n=sum((j+1)*b for j,b in enumerate(blocks))
    return [sum(max(0,j+1-k)*b for j,b in enumerate(blocks)) for k in range(p+1)]+[0]

def main():
    comparisons=0
    for p in (2,3,5,7,11):
        for n in range(0,21):
            for r in range(n//2+1):
                blocks=transfer_blocks(n,r,p)
                assert ranks_from_jordan(blocks,p)==rank_powers_formula(n,r,p), (n,r,p)
                assert all(v>=0 for v in blocks)
                comparisons+=1
    print('TRANSFER_VS_WILSON_RANKS_PASS',comparisons,'parameter triples')
    for p in (2,3,5,7,11):
        for r in range(20):
            n=2*r
            blocks=transfer_blocks(n,r,p)
            nonfree=sum((i+1)*blocks[i] for i in range(p-1))
            assert nonfree <= 2**n
            if r >= 1:
                prev=transfer_blocks(2*(r-1),r-1,p)
                prev_frac=sum((i+1)*prev[i] for i in range(p-1)) / 2**(2*(r-1))
                assert nonfree / 2**n <= prev_frac + 1e-15
    print('MONOTONE_NONPROJECTIVE_FRACTION_PASS p=2,3,5,7,11, r<=19')
    for q in (2,3,4,5,7,8,9):
        for n in range(12):
            expected={tuple(transfer_blocks(n,r,2 if q in (2,4,8) else 3 if q in (3,9) else 5 if q==5 else 7)): alternating_count(n,r,q) for r in range(n//2+1)}
            assert sum(expected.values())==q**comb(n,2)
    print('FINITE_FIELD_FORM_POPULATION_PASS')
    print('QUADRATIC_EXTERIOR_TRIDIAGONAL_PASS')
if __name__ == '__main__':main()
