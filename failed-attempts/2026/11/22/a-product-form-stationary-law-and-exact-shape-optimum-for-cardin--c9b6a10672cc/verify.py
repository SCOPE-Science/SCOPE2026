"""Reproduce exact generator identities and stationary samples for a cardinal-heading active particle.
Scientific reproduction: only Python 3 standard library is required.
"""
from fractions import Fraction as Q
import math
import random


def one_moment(kind, k, length, ell):
    """Exact moment of a one-coordinate measure (kind=0 symmetric, +/- oriented)."""
    mass = length**(k+1)/Q(k+1)
    if kind == 0:
        mass += ell*length**k/Q(2)
        if k == 0: mass += ell/Q(2)
    elif kind == +1:
        mass += ell*length**k
    elif kind == -1 and k == 0:
        mass += ell
    return mass/(length+ell)


def generator_residual(dim, lengths, speeds, weights, gamma, powers, coeffs):
    """Exact weak generator integral of all heading-dependent monomials.

    coeffs holds rational coefficients for f(x, heading), one per +i and -i.
    """
    ell=[2*v/gamma for v in speeds]
    result=Q(0)
    for axis in range(dim):
        other=math.prod([one_moment(0,powers[j],lengths[j],ell[j])
                         for j in range(dim) if j != axis])
        for sign in (-1,+1):
            c=coeffs[2*axis+(sign+1)//2]
            exponent=powers[axis]
            # Constrained drift on interior only, outward endpoints clipped.
            if exponent==0:
                transport=Q(0)
            else:
                transport=sign*speeds[axis] * lengths[axis]**exponent/(lengths[axis]+ell[axis])
            incoming=one_moment(0,exponent,lengths[axis],ell[axis])
            outgoing=one_moment(sign,exponent,lengths[axis],ell[axis])
            resetting=gamma*(incoming-outgoing)
            result += c*weights[axis]/2*other*(transport+resetting)
    return result


def exact_checks():
    sets=[
        (2,[Q(3,2),Q(5,3)],[Q(5,4),Q(7,3)],[Q(2,5),Q(3,5)],Q(7,3)),
        (3,[Q(3,2),Q(2),Q(7,5)],[Q(2),Q(5,4),Q(11,6)],[Q(1,5),Q(1,2),Q(3,10)],Q(8,5)),
    ]
    count=0
    for d,L,v,w,g in sets:
        for u in range(4**d):
            exps=[]; n=u
            for i in range(d):
                exps.append(n%4); n//=4
            coeffs=[Q((i+1)**2+u%5,2*i+3) for i in range(2*d)]
            assert generator_residual(d,L,v,w,g,exps,coeffs)==0, (d,exps)
            count+=1
        lam=sum(w)
        assert lam==1
        for i in range(d):
            e=2*v[i]/g
            wall=e/(2*(L[i]+e))
            assert wall>0
            # The fraction on the outward heading at a wall is derived exactly.
            pi_out=w[i]*e/(2*(L[i]+e))
            friction=Q(7,3)
            area=math.prod(L)/L[i]
            pres=friction*v[i]*pi_out/area
            expected=friction*(w[i]*v[i]**2/g)*L[i]/(math.prod(L)*(L[i]+e))
            assert pres==expected
    print(f'PASS: {count} exact rational generator identities, pressure and corner measures')


def monte_carlo():
    seed=194807
    for w in (0.2,0.8):
        rng=random.Random(seed+int(w*100))
        L=(1.5,2.25)
        speeds=(1.2,2.1)
        gamma=1.4
        ell=[2*v/gamma for v in speeds]
        pos=[0.8,1.1]
        heading=0
        sign=1
        sumw=Q(0) if False else 0.0
        sumx=[0.0,0.0]
        cross=0.0
        joint_upper=0.0
        for i in range(320000):
            dt=rng.expovariate(gamma)
            u=rng.random()*dt
            x=pos.copy()
            x[heading]=min(L[heading],max(0.,x[heading]+sign*speeds[heading]*u))
            if i>=1000:
                sumw+=dt
                sumx[0]+=dt*x[0]
                sumx[1]+=dt*x[1]
                cross+=dt*x[0]*x[1]
                joint_upper+=dt*(x[0]>=L[0]-1e-12 and x[1]>=L[1]-1e-12)
            pos[heading]=min(L[heading],max(0.,pos[heading]+sign*speeds[heading]*dt))
            heading=0 if rng.random()<w else 1
            sign=1 if rng.random()<.5 else -1
        means=[s/sumw for s in sumx]
        covariance=cross/sumw-means[0]*means[1]
        corner=joint_upper/sumw
        theory=(ell[0]/(2*(L[0]+ell[0])))*(ell[1]/(2*(L[1]+ell[1])))
        assert abs(means[0]-L[0]/2)<.035, (w,means)
        assert abs(means[1]-L[1]/2)<.035, (w,means)
        assert abs(covariance)<.035,(w,covariance)
        assert abs(corner-theory)<.035,(w,corner,theory)
        print('PASS Monte Carlo weights %.1f: means=(%.5f, %.5f), covariance=%.5f, corner=%.5f vs %.5f' %
              (w,means[0],means[1],covariance,corner,theory))


def shape_check():
    # KKT solution in 3D, exact proof in text uses strict positive Hessian.
    import math
    D=[0.3,0.6,0.9]
    ell=[2.0,1.0,1.5]
    volume=8.0
    lo,hi=0.0,min(D)
    for _ in range(120):
        mid=(lo+hi)/2
        sides=[e*mid/(d-mid) for d,e in zip(D,ell)]
        if math.prod(sides)>volume:hi=mid
        else:lo=mid
    lagrange=(lo+hi)/2
    sides=[e*lagrange/(d-lagrange) for d,e in zip(D,ell)]
    assert abs(math.prod(sides)-volume)<1e-11
    assert max(abs(d*l/(l+e)-lagrange) for d,l,e in zip(D,sides,ell))<1e-12
    print('PASS fixed-volume scalar root and stationarity; sides:',*[round(x,7) for x in sides])


if __name__=='__main__':
    exact_checks()
    monte_carlo()
    shape_check()
