#!/usr/bin/env python3
"""Exact-integer reproducibility tests for digit-sum recurrence-gap theorem.
No external dependencies. Finite checks corroborate the separate unrestricted proof.
"""
def digit_sum(x, q):
    assert x >= 0 and q >= 2
    out = 0
    while x:
        out += x % q
        x //= q
    return out

def value(n, q):
    return digit_sum(2*n, q) % q

def gap_bound(q):
    return (2*q-1) if q % 2 == 0 else (3*q*q-1)//2

def even_witness(q, j):
    assert q % 2 == 0
    M = (q-2) + sum((q-1)*q**i for i in range(1,q-1))
    M += j*q**q
    assert M % 2 == 0
    k = M//2
    return q*k, q*k+2*q-1

def odd_witness(q, j):
    assert q % 2 == 1
    r = j if j % 2 == 0 else j+q
    low = min(r,q-1)
    high = r-low
    H = low + high*q
    assert digit_sum(H,q)==r and H % 2 == 0
    left = H*q**3//2
    right = (H*q**3+3*q*q-1)//2
    return left,right

def main():
    n_witness=0; n_block=0; n_scan=0
    for q in range(2,32):
        for j in range(q):
            lo,hi=(even_witness(q,j) if q%2==0 else odd_witness(q,j))
            assert hi-lo == gap_bound(q), (q,j,'bad length')
            assert value(lo,q)==j and value(hi,q)==j, (q,j,'bad endpoints')
            if q%2:
                for n in range(lo+1,hi):
                    assert value(n,q)!=j, (q,j,'odd intervening hit',n)
                    n_witness += 1
            else:
                k=lo//q
                assert value(k+1,q)==(value(k,q)+1)%q
                assert sorted(value(q*k+t,q) for t in range(q)) == list(range(q))
                assert sorted(value(q*(k+1)+t,q) for t in range(q)) == list(range(q))
                for n in range(lo+1,hi):
                    assert value(n,q)!=j, (q,j,'even intervening hit',n)
                    n_witness += 1
        if q%2 == 0:
            for k in range(180):
                v=[value(q*k+t,q) for t in range(q)]
                assert sorted(v)==list(range(q))
                n_block+=1
        else:
            B=q*q
            for k in range(180):
                sums={digit_sum(k*B+t,q)%(2*q) for t in range(B)}
                assert len(sums)>=2*q-1
                if k:
                    previous={digit_sum((k-1)*B+t,q)%(2*q) for t in range(B)}
                    assert sums|previous==set(range(2*q))
                n_block+=1
    for q in range(2,18):
        prev=[None]*q
        bounds=[gap_bound(q)]*q
        for n in range(120000):
            j=value(n,q)
            if prev[j] is not None:
                assert n-prev[j] <= bounds[j], (q,j,n,prev[j])
                n_scan+=1
            prev[j]=n
    print('VERIFY_OK bases=2..31 residues=all witness_interiors=%d block_cases=%d direct_consecutive_gap_checks=%d' % (n_witness,n_block,n_scan))

if __name__=='__main__': main()
