"""Exact modular checks for the Stirling difference stabilization theorem.

No external dependencies.  Exponentiation is modular and the inclusion/exclusion
numerator is divided by the exact power of two in the factorial.
"""
from math import comb, factorial

def v2(x):
    return (x & -x).bit_length() - 1 if x else None

def modular_difference(a, b, n, k, extra=5):
    """Return exact v2 of difference if < n+1+v2(a-b)+extra.

    The factorial's odd part is a unit, so valuations can be calculated
    from the inclusion/exclusion numerator modulo a known power of 2.
    """
    assert a > b >= 1 and n >= 1 and k >= 1
    w = v2(a-b)
    h = v2(factorial(k))
    bound = n+1+w+extra
    modulus = 1 << (bound+h)
    A = a << n
    B = b << n
    total = sum(((-1)**(k-j))*comb(k, j)*(pow(j,A,modulus)-pow(j,B,modulus))
                for j in range(1,k+1)) % modulus
    assert total
    valuation = v2(total)-h
    assert valuation < bound
    return valuation

def direct_stirling(n,k):
    row=[1]
    for t in range(1,n+1):
        nxt=[0]*(min(k,t)+1)
        for j in range(1,len(nxt)):
            nxt[j]=(row[j-1] if j-1<len(row) else 0) + (j*row[j] if j<len(row) else 0)
        row=nxt
    return row[k] if k < len(row) else 0

def check():
    direct=0
    for k in (3,7,15):
        for n in range(3,6):
            for a,b in ((2,1),(3,1),(5,2)):
                if b*(1<<n) < k or a*(1<<n)>250:
                    continue
                exact=direct_stirling(a<<n,k)-direct_stirling(b<<n,k)
                assert v2(exact)==modular_difference(a,b,n,k,extra=30)
                direct+=1
    assert direct>=18
    stabilized=0
    for m in (4,5,6,7):
        k=(1<<m)-1
        h=v2(factorial(k))
        for n in (max(h+1,m),max(h+2,m)):
            for a,b in ((2,1),(3,1),(9,3),(257,1),(513,1),((1<<25)+1,1)):
                w=v2(a-b)
                assert 1<<n>=n+2+h+w
                got=modular_difference(a,b,n,k)
                assert got==n+1+w,(m,n,a,b,got,n+1+w)
                stabilized+=1
    # Confirm that the distinction between eventual and all-level claims is real.
    counter = modular_difference(257,1,4,15)
    assert counter != 4+1+v2(256)
    print('VERIFY_OK direct_independent_cases=%d eventual_cases=%d m_range=4..7 big_gap_bits=25 counterexample_at_small_n=%d' %(direct,stabilized,counter))

if __name__ == '__main__':
    check()
