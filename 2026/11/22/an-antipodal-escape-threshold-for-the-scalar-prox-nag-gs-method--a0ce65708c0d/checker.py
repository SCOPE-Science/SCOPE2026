"""Exact-rational cross-checks for a scalar semi-implicit proximal iteration.

The accompanying proof, not this finite test, establishes the infinite claims.
Run: python checker.py
"""
from fractions import Fraction as Q


def soft(u, t):
    return u-t if u>t else u+t if u < -t else Q(0)


def step(a, k, theta, x, v):
    b = 1-a
    xp = b*x+a*v
    up = b*v+a*(1-k)*xp
    return xp, soft(up, theta)


def check():
    cases = 0
    for a in [Q(1,5), Q(1,3), Q(1,2), Q(3,4), Q(9,10)]:
        b=1-a
        c=(2-a)/a
        kc=1+c*c
        for theta in [Q(1,7),Q(3,5)]:
            for delta in [Q(1,10),Q(1,2),Q(2)]:
                k=kc+delta
                X=theta/(a*delta)
                assert step(a,k,theta,X,-c*X)==(-X,c*X)
                assert step(a,k,theta,-X,c*X)==(X,-c*X)
                gamma=a*a*(k-1)-(3-2*a)
                assert gamma >= b*b > 0
                for d,w in [(Q(1,5),Q(0)),(Q(0),Q(1,2)),(Q(2),Q(3))]:
                    x=X+d
                    v=-c*x-w
                    xp,vp=step(a,k,theta,x,v)
                    assert xp == -x-a*w
                    wp = a*delta*d+gamma*w
                    assert vp == c*(-xp)+wp
                    # The next point is on the opposite cone, with nonnegative slack.
                    assert wp >= 0
                    cases += 1
                R = max(X,theta/(a*k-2/a))+1
                xp,vp=step(a,k,theta,R,R)
                assert xp==R and vp < -c*R
                # Strictly positive cone displacement implies genuine expansion.
                x,v=xp,vp
                previous=abs(x)
                for j in range(8):
                    x,v=step(a,k,theta,x,v)
                    assert abs(x)>=previous
                    previous=abs(x)
                cases+=1
            for k in [Q(1,10),Q(1),kc/2, kc-Q(1,100)]:
                if not 0<k<kc:continue
                trace=2*b+a*a*(1-k)
                det=b*b
                assert 1-det>0 and 1-trace+det==a*a*k>0
                assert 1+trace+det==a*a*(kc-k)>0
                cases+=1
    print(f"PASS: {cases} exact rational cases (including antipodal cycles, cones, ")
    print("diagonal starts, and Schur inequalities).")


if __name__=='__main__':check()
