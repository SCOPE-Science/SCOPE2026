#!/usr/bin/env python3
"""Independent integer-reachability checks for fundamental-gap band theorem.
Run: python3 check_fundamental_gap_bands.py
"""

def iceil(x,y):
    return -((-x)//y)

def predicted(a,k):
    assert a>=2 and 1<=k<a
    A=iceil(a,2)
    B=iceil(2*a,3)
    out=[]
    for r in range(A,a):
        up=iceil(r,k)-1
        if r<B:
            low=max(0,iceil(3*r-a-k,3*k))
        else:
            low=max(0,iceil(2*r-a-k,2*k))
        out.extend(qa*a+r for qa in range(low,up+1))
    return sorted(out)

def independent_reachability(a,k):
    # Direct unbounded-coin DP; does not use the theorem's quotient test.
    conductor=a*iceil(a-1,k)
    high=3*(conductor+a)
    hit=bytearray(high+1)
    hit[0]=1
    for n in range(1,high+1):
        hit[n]=any(n>=c and hit[n-c] for c in range(a,a+k+1))
    return [n for n in range(1,conductor+a)
            if not hit[n] and hit[2*n] and hit[3*n]]

def exact_count(a,k):
    A=iceil(a,2)
    B=iceil(2*a,3)
    z=0
    for r in range(A,B):
        lo=max(0,iceil(3*r-a-k,3*k))
        z+=max(0,iceil(r,k)-lo)
    for r in range(B,a):
        lo=max(0,iceil(2*r-a-k,2*k))
        z+=max(0,iceil(r,k)-lo)
    return z

def genus(a,k):
    return sum(iceil(r,k) for r in range(1,a))

if __name__=='__main__':
    pairs=0;tested=0;fundamental=0
    for a in range(2,110):
        for k in range(1,a):
            explicit=predicted(a,k)
            direct=independent_reachability(a,k)
            assert explicit==direct,(a,k,explicit,direct)
            f=exact_count(a,k)
            g=genus(a,k)
            assert len(explicit)==f
            assert abs(9*k*f-2*a*a)<27*a*k
            assert abs(2*k*g-a*a)<2*a*k
            pairs+=1
            tested+=a*iceil(a-1,k)+a
            fundamental+=len(explicit)
    print(f'PASS: {pairs} parameter pairs, {tested} gap candidates, {fundamental} fundamental gaps')
    for k in [1,2,3,4,7,13]:
        a=720
        f=exact_count(a,k)
        g=genus(a,k)
        print(f'a={a}, k={k}: fundamental={f}, genus={g}, ratio={f/g:.8f}')
