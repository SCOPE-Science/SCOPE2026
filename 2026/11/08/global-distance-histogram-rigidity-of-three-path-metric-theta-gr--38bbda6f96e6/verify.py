"""Standalone exact-rational and independent simulation checks for the theta distance law.
Run: python verify.py (Python 3 standard library only)."""
from fractions import Fraction as Q
from random import Random
from bisect import bisect_right


def clip(poly, A, B, C):
    if not poly: return []
    out = []
    for p, q in zip(poly, poly[1:] + poly[:1]):
        vp, vq = A*p[0] + B*p[1]-C, A*q[0]+B*q[1]-C
        if vp <= 0: out.append(p)
        if (vp<0<vq) or (vq<0<vp):
            t=vp/(vp-vq)
            out.append((p[0]+t*(q[0]-p[0]), p[1]+t*(q[1]-p[1])))
    return out


def area(poly):
    if len(poly)<3:return Q(0)
    return abs(sum((p[0]*q[1]-p[1]*q[0] for p,q in zip(poly,poly[1:]+poly[:1])),Q(0)))/2


def cross_tail(a,b,c,r):
    P=[(Q(0),Q(0)),(a,Q(0)),(a,b),(Q(0),b)]
    for A,B,C in ((-1,-1,-r),(1,1,a+b-r),(-1,1,b+c-r),(1,-1,a+c-r)):
        P=clip(P,Q(A),Q(B),C)
    return area(P)


def same_tail(a,m,r):
    lo=max(Q(0),r); hi=min(a,a+m-r)
    if hi<=lo:return Q(0)
    return 2*a*(hi-lo)-(hi**2-lo**2)


def cdf(a,b,c,r):
    L=a+b+c
    T=sum((same_tail(x,min(y,z),r) for x,y,z in ((a,b,c),(b,a,c),(c,a,b))),Q(0))
    T+=2*(cross_tail(a,b,c,r)+cross_tail(a,c,b,r)+cross_tail(b,c,a,r))
    return 1-T/L**2


def expected_jumps(a,b,c):
    a,b,c=sorted((a,b,c)); L=a+b+c
    jumps={}
    for r,v in (((a+b)/2,-2*(a+b)/L**2),((a+c)/2,-2*(a+c)/L**2),((b+c)/2,-4*a/L**2)):
        jumps[r]=jumps.get(r,Q(0))+v
    return jumps


def measured_jump(a,b,c,r):
    L=a+b+c
    distinct=sorted(set([Q(0),(a+b)/2,(a+c)/2,(b+c)/2, L]))
    gaps=[abs(t-r) for t in distinct if t!=r]
    h=min(gaps)/Q(1000)
    F=lambda s:cdf(a,b,c,s)
    f_left=(3*F(r)-4*F(r-h)+F(r-2*h))/(2*h)
    f_right=(-3*F(r)+4*F(r+h)-F(r+2*h))/(2*h)
    return f_right-f_left


def distance(a,b,c,i,x,j,y):
    ls=(a,b,c)
    if i==j:
        delta=abs(x-y)
        return min(delta,ls[i]+min(ls[t] for t in range(3) if t!=i)-delta)
    z=3-i-j
    return min(x+y,(ls[i]-x)+(ls[j]-y),x+ls[z]+ls[j]-y,ls[i]-x+ls[z]+y)


def main():
    cases=((1,2,3),(1,1,1),(1,1,4),(1,4,4),(1,3,6),(2,3,5),
           (Q(1,2),Q(7,3),Q(13,3)),(Q(3,4),Q(3,4),Q(13,4)),(Q(2,5),Q(13,10),Q(13,10)),
           (Q(17,13),Q(19,11),Q(17,4)))
    exact=0; thresholds=0; recovered=0
    for raw in cases:
        a,b,c=sorted(map(Q,raw)); L=a+b+c
        J=expected_jumps(a,b,c)
        assert cdf(a,b,c,Q(0))==0
        assert cdf(a,b,c,L)==1
        h=Q(1,10000)
        assert (4*cdf(a,b,c,h)-cdf(a,b,c,2*h))/(2*h) == 2/L  # quadratic near origin
        for r,j in J.items():
            assert measured_jump(a,b,c,r)==j, (raw,r,measured_jump(a,b,c,r),j)
            assert j<0
            thresholds+=1
        rr=sorted(J)
        if len(rr)==3:
            aa=rr[0]+rr[1]-rr[2];bb=rr[0]+rr[2]-rr[1];cc=rr[1]+rr[2]-rr[0]
            assert (aa,bb,cc)==(a,b,c)
        elif len(rr)==2:
            s,t=rr
            if L==s+2*t:
                assert (a,b,c)==(s,s,2*t-s)
            else:
                assert L==2*s+t and (a,b,c)==(2*s-t,t,t)
        else:
            assert len(rr)==1 and a==b==c==rr[0]
        recovered+=1
        exact+=1
    rng=Random(20261103)
    samples=0; worst=0.; comparisons=0
    for raw in ((1,2,3),(1,1,1),(1,1,4),(Q(1,2),Q(7,3),Q(13,3))):
        a,b,c=map(float,raw);L=a+b+c
        obs=[]
        for t in range(80000):
            i=bisect_right((a,a+b,L),rng.random()*L)
            j=bisect_right((a,a+b,L),rng.random()*L)
            x=rng.random()*(a,b,c)[i]; y=rng.random()*(a,b,c)[j]
            obs.append(distance(a,b,c,i,x,j,y))
        obs.sort(); samples+=len(obs)
        for r in (L/10,L/5,L*3/10,L*2/5,L/2):
            observed=bisect_right(obs,r)/len(obs)
            exact_val=float(cdf(*map(Q,raw),Q(str(r))))
            err=abs(observed-exact_val)
            worst=max(worst,err)
            assert err<0.009, (raw,r,err)
            comparisons+=1
    print(f'THETA_VERIFY_OK exact_rational_cases={exact} jump_groups={thresholds} recovered={recovered} independent_pair_samples={samples} cdf_comparisons={comparisons} max_abs_cdf_error={worst:.7f}')

if __name__=='__main__': main()
