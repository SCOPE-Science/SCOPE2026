"""Supplementary checks for a sharp orthoscheme solid-angle/fullness bound.

The universal theorem is proved analytically in RESULT.md; these checks are
independent numerical corroboration, not a replacement for the proof.
"""
import math
import random


def dot(u, v):
    return sum(x*y for x,y in zip(u,v))


def norm(u):
    return math.sqrt(dot(u,u))


def det(u,v,w):
    return (u[0]*(v[1]*w[2]-v[2]*w[1])
           -u[1]*(v[0]*w[2]-v[2]*w[0])
           +u[2]*(v[0]*w[1]-v[1]*w[0]))


def omega(p, others):
    u,v,w=([x-y for x,y in zip(q,p)] for q in others)
    d=(norm(u)*norm(v)*norm(w)+dot(u,v)*norm(w)
       +dot(v,w)*norm(u)+dot(w,u)*norm(v))
    return 2*math.atan2(abs(det(u,v,w)), d)


def trial(a,b,c):
    v=((0.,0.,0.),(a,0.,0.),(a,b,0.),(a,b,c))
    o=[omega(v[i],[v[j] for j in range(4) if i!=j]) for i in range(4)]
    s=math.hypot(a,b);t=math.hypot(b,c); L=math.sqrt(a*a+b*b+c*c)
    explicit=(2*math.atan2(b*c,(s+a)*(L+s)),
              math.atan2(c,b),math.atan2(a,b),
              2*math.atan2(a*b,(t+c)*(L+t)))
    for u,w in zip(o,explicit):
        assert abs(u-w)<3e-11*max(1,u,w),(a,b,c,o,explicit)
    mu=a*b*c/(6*L**3)
    assert 6*mu > min(o)**2*(1-1e-11),(a,b,c,mu,o)
    if a>=c:
        # Independent algebraic certificate of the key proof chain.
        assert 4*b*c*L**3 <= a*(s+a)**2*(L+s)**2*(1+1e-12)
        assert b*L**2 <= s*(s+a)**2*(1+1e-12)
    else:
        assert 4*b*a*L**3 <= c*(t+c)**2*(L+t)**2*(1+1e-12)
    return mu,min(o)


def main():
    rng=random.Random(261005883)
    N=12000
    for _ in range(N):
        a,b,c=(10**rng.uniform(-2.5,2.5) for k in range(3))
        trial(a,b,c)
    r=[]
    for eps in [1e-2,1e-3,1e-4,1e-5]:
        mu,Om=trial(eps,1.,eps)
        ratio=mu/Om**2
        r.append((eps,ratio))
    assert abs(r[-1][1]-1/6)<1e-5
    print('PASS: 12,000 deterministic independent solid-angle and bound comparisons')
    print('Sharpness ratios:',r)
    print('Analytic argument is required for the universal claim.')

if __name__=='__main__':
    main()
