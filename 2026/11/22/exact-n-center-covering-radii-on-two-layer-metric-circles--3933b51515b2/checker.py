"""Independent exact-fraction checks for the two-layer metric-circle covering theorem.

The proof of the continuum lower bound is in RESULT.md. This program checks
finite rational constructions and their sharp lower-bound inequalities; it
is not a proof by enumeration of all real parameters.
"""
from fractions import Fraction as F
from math import ceil


def radius(L, s, N):
    L, s = F(L), F(s)
    assert L > 0 and s > 0 and isinstance(N, int) and N >= 1
    sep = L / (2 * (N // 2)) if N >= 2 else None
    mixed = (L + 2 * s * ((N + 1) // 2)) / (2 * N)
    return mixed if sep is None else min(sep, mixed)


def centers(L, s, N):
    L, s = F(L), F(s)
    r = radius(L, s, N)
    sep = L / (2 * (N // 2)) if N >= 2 else None
    if sep is not None and sep <= (L + 2*s*((N+1)//2))/(2*N):
        k = N//2
        v = [(F(i)*L/k, layer) for layer in (0, 1) for i in range(k)]
        return r, v  # An unused extra center may be added for odd N.
    assert r >= s
    v=[]
    p=F(0)
    for i in range(N):
        v.append((p, i%2))
        if i == N-1 and N%2:
            g = 2*(r-s)  # two short arcs meet in the minority layer
        else:
            g = 2*r-s  # one short and one long arc
        assert g >= 0
        p += g
    assert p == L, (p,L,N,s,r)
    return r,v


def circle_covered(L, cent, rad):
    L=F(L)
    if rad>=L/2:
        return True
    if rad<0:
        return False
    arcs=[]
    for shift in (-1,0,1):
        a=cent+shift*L-rad; b=cent+shift*L+rad
        if b>=0 and a<=L:
            arcs.append((max(F(0),a),min(L,b)))
    return arcs


def cover_fiber(L, centers, s, r, sheet):
    arcs=[]
    for p,lab in centers:
        R=r if lab==sheet else r-s
        x=circle_covered(L,p,R)
        if x is True: return True
        if x is False: continue
        arcs.extend(x)
    arcs.sort()
    end=F(0)
    for a,b in arcs:
        if a>end: return False
        if b>end:end=b
        if end>=L:return True
    return False


def lower_bound(L,s,N,r):
    """Proves no N balls at radius r using two disjoint fibers or lengths."""
    if r<s:
        return N < 2*((L+2*r- F(1,10**12))//(2*r)) if False else N<2*ceil(L/(2*r))
    return L>2*r*N-2*s*((N+1)//2)


def main():
    tests=0
    for Ln in range(1,13):
      for den in (1,2,3,5):
       L=F(Ln,den)
       for sn in range(1,11):
        s=F(sn,den*3)
        for N in range(1,16):
         r,cent=centers(L,s,N)
         assert len(cent)<=N
         assert cover_fiber(L,cent,s,r,0)
         assert cover_fiber(L,cent,s,r,1)
         for eps in (F(1,100),F(1,1000)):
          rr=r*(1-eps)
          assert lower_bound(L,s,N,rr), (L,s,N,r,rr)
         tests+=1
    print(f'PASS: {tests} exact-rational parameter sets: constructive two-fiber coverage and strict suboptimal-radius certificates')
    for N in range(1,12):
      for s in (F(1,5), F(2), F(100)):
        L=F(6)
        print(f'N={N} L=6 s={s} R={radius(L,s,N)}')

if __name__=='__main__':
    main()
