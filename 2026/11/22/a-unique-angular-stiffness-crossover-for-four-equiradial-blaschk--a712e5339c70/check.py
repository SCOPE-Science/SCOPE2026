"""Exact-rational and finite-difference diagnostics for a Blaschke variance Hessian."""
from fractions import Fraction as F
from math import cos, pi, sqrt


def p(u):
    return u**6 - 4*u**5 - 13*u**4 - 24*u**3 - 13*u**2 - 4*u + 1


def pos_poly(u):
    return 1 + 4*u + 19*u*u + 24*u**3 + 19*u**4 + 4*u**5 + u**6


def stiffness(u):
    l1 = 4*u*(1-u)*pos_poly(u)/((1+u)**3*(1+u*u)**3)
    l2 = 32*u*u*(1-u)*(1+u)/(1+u*u)**3
    return l1,l2


def residue_sum(k,u):
    v = u**4
    return u**k*(k*k/(1-v)+8*k*v/(1-v)**2+16*v*(1+v)/(1-v)**3)


def pair_energy(u, angles):
    # Poisson convolution: integral of P_r(t-a) P_r(t-b) is P_{r^2}(a-b).
    return sum((1-u*u)/(1-2*u*cos(a-b)+u*u)
               for a in angles for b in angles)-16


def main():
    count=0
    # The two rational formulae are recovered independently from the Fourier residues.
    for i in range(1,20):
        u=F(i,20)
        a=[residue_sum(j,u) for j in range(4)]
        h1=a[1]+a[3]-2*a[0]
        h2=2*(a[2]-a[0])
        l1,l2=stiffness(u)
        assert l1==4*h1 and l2==4*h2
        assert l1-l2==4*u*(1-u)*p(u)/((1+u)**3*(1+u*u)**3)
        assert l1>0 and l2>0
        count+=5
    assert p(F(152,1000))>0 and p(F(153,1000))<0
    count+=2
    left,right=0.0,1.0
    for _ in range(70):
        mid=(left+right)/2
        if p(mid)>0:left=mid
        else:right=mid
    transition=(left+right)/2
    assert abs(transition-0.1520115267277273)<1e-13
    count+=1
    for u in (0.03,0.10,0.152,0.30,0.50,0.80):
        l1,l2=stiffness(u)
        base=[j*pi/2 for j in range(4)]
        val0=pair_energy(u,base)
        # A real first-Fourier perturbation, and the alternating mode.
        for direction,expected in (
            ([1,0,-1,0],2*l1),([0,1,0,-1],2*l1),
            ([1,-1,1,-1],4*l2)):
            eps=0.0003
            a=[base[j]+eps*direction[j] for j in range(4)]
            b=[base[j]-eps*direction[j] for j in range(4)]
            numerical=(pair_energy(u,a)+pair_energy(u,b)-2*val0)/(2*eps*eps)
            assert abs(numerical-expected)<3e-5*max(1,abs(expected)),(u,direction,numerical,expected)
            count+=1
    # Distinct weak directions on opposite sides of the transition.
    assert stiffness(0.1)[1] < stiffness(0.1)[0]
    assert stiffness(0.5)[0] < stiffness(0.5)[1]
    count+=2
    print('PASS: %d exact and finite-difference diagnostic assertions; u*=%.15f; r*=%.15f' %
          (count,transition,sqrt(transition)))


if __name__=='__main__':
    main()
