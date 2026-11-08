"""Exact-arithmetic checks for a scalar-bilinear partial-reuse extragradient law.

Run: python3 verify.py (standard library only).
The accompanying mathematical proof supplies the all-laws/all-horizons result.
"""
from fractions import Fraction as Q
from itertools import product


def step(z, a, b, eta):
    x, y = z
    return ((1-eta*eta*a*b)*x - eta*b*y,
            (1-eta*eta*a*b)*y + eta*b*x)


def outcomes(values, weights, reuse):
    for i, a in enumerate(values):
        for j, b in enumerate(values):
            w = (reuse*weights[i] if i == j else Q(0)) + (1-reuse)*weights[i]*weights[j]
            if w:
                yield w, a, b


def predicted(values, weights, reuse, eta):
    mu = sum((p*a for p,a in zip(weights, values)), Q(0))
    m2 = sum((p*a*a for p,a in zip(weights, values)), Q(0))
    m4 = sum((p*a**4 for p,a in zip(weights, values)), Q(0))
    A = (2*reuse-1)*m2+2*(1-reuse)*mu*mu
    B = reuse*m4+(1-reuse)*m2*m2
    M = 1-A*eta**2+B*eta**4
    C = reuse*m2+(1-reuse)*mu*mu
    mean2 = (1-eta*eta*C)**2 + eta*eta*mu*mu
    return M, mean2, A, B


def direct(values, weights, reuse, eta, steps):
    states = [(Q(1), (Q(1),Q(0)))]
    for _ in range(steps):
        states = [(w*p, step(z,a,b,eta)) for p,z in states
                  for w,a,b in outcomes(values,weights,reuse)]
    ms = sum((w*(z[0]*z[0]+z[1]*z[1]) for w,z in states),Q(0))
    mx = sum((w*z[0] for w,z in states),Q(0))
    my = sum((w*z[1] for w,z in states),Q(0))
    return ms, mx*mx+my*my


def run():
    count = 0
    examples=[((Q(0),Q(4)), (Q(3,4),Q(1,4))),
              ((Q(1),Q(4)), (Q(1,3),Q(2,3))),
              ((Q(-2),Q(4)),(Q(1,2),Q(1,2))),
              ((Q(3),Q(3)),(Q(1,2),Q(1,2)))]
    for values,weights in examples:
        for rho in (Q(0),Q(1,4),Q(1,3),Q(1,2),Q(3,4),Q(1)):
            for eta in (Q(1,10),Q(1,4),Q(1,2)):
                M,G,A,B=predicted(values,weights,rho,eta)
                ms,mean2=direct(values,weights,rho,eta,1)
                assert (M,G)==(ms,mean2)
                count+=1
    for rho in (Q(0),Q(1,3),Q(1,2),Q(1)):
        v=(Q(0),Q(4));w=(Q(3,4),Q(1,4));eta=Q(1,10)
        M,G,A,B=predicted(v,w,rho,eta)
        for k in (2,3):
            ms,me=direct(v,w,rho,eta,k)
            assert (ms,me)==(M**k,G**k)
            count+=1
    v=(Q(0),Q(4));w=(Q(3,4),Q(1,4));eta=Q(1,10)
    assert predicted(v,w,Q(0),eta)[:2] == (Q(1277,1250),Q(9901,10000))
    assert predicted(v,w,Q(1,2),eta)[0] == Q(497,500)
    assert predicted(v,w,Q(1,3),eta)[2] == 0
    # Strictly positive two-point laws with unit mean: sharpness near one-half.
    for rho,q in ((Q(1,3),Q(1,100)), (Q(49,100),Q(1,100)),
                  (Q(499,1000),Q(1,10000))):
        low=Q(1,100); high=(1-(1-q)*low)/q
        vv=(low,high);ww=(1-q,q)
        M,G,A,B=predicted(vv,ww,rho,Q(1,1000))
        assert A<0 and M>1
        half=predicted(vv,ww,Q(1,2),1/(10*(high+1)**2))
        assert half[2]==1 and half[0]<1
        count+=2
    print(f'PASS: {count} exact rational formula/horizon/universal-threshold checks')

if __name__ == '__main__':
    run()
