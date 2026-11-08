"""Reproducible finite checks for the Gaussian sketched Rayleigh--Ritz bound.

Requires Python 3.9+ standard library. All assertions test finite consequences;
the analytic argument in RESULT.md establishes the universal statement.
"""
from fractions import Fraction as F
from random import Random
from math import sqrt, pi, sin, cos


def determinant3(K):
    a,b,c=K[0]; d,e,f=K[1]; g,h,i=K[2]
    return a*(e*i-f*h)-b*(d*i-f*g)+c*(d*h-e*g)


def matrix_K(d,t1,t2):
    return ((t1*t1,t1*t2,-2*d*t1),
            (t1*t2,t2*t2,2*d*t2),
            (-2*d*t1,2*d*t2,4*d*d))


def disc_via_q(d,t1,t2,q1,q2):
    return 4*d*d-4*d*(t1*q1-t2*q2)+(t1*q1+t2*q2)**2


def disc_via_matrix(alpha,beta,t1,t2,q1,q2):
    m11=alpha+t1*q1; m12=t2*q1
    m21=t1*q2; m22=beta+t2*q2
    return (m11+m22)**2-4*(m11*m22-m12*m21)


def quad_probability_equal(t,d=1.0,n=4096):
    # Independent angular evaluation derived from the eigenvalue cone law.
    r=t/d
    eta=sqrt(1+2*r*r)
    aa=(eta+1)/2
    bb=(eta+1)/(eta-1)
    dt=2*pi/n
    val=0.0
    for j in range(n):
        a=(j+0.5)*dt
        c=aa*cos(a)**2+bb*sin(a)**2
        val+=1-sqrt(c/(1+c))
    return val/n


def eigs_symmetric3(M):
    # Jacobi diagonalization with orthogonal rotations, finite-dimensional test.
    a=[list(map(float,row)) for row in M]
    for _ in range(45):
        p,q=max(((0,1),(0,2),(1,2)),key=lambda ij:abs(a[ij[0]][ij[1]]))
        if abs(a[p][q])<1e-13:
            break
        tau=(a[q][q]-a[p][p])/(2*a[p][q])
        t=(1 if tau>=0 else -1)/(abs(tau)+sqrt(1+tau*tau))
        c=1/sqrt(1+t*t); sn=t*c
        app,aqq,apq=a[p][p],a[q][q],a[p][q]
        a[p][p]=app-t*apq; a[q][q]=aqq+t*apq
        a[p][q]=a[q][p]=0.0
        for j in range(3):
            if j!=p and j!=q:
                x,y=a[j][p],a[j][q]
                a[j][p]=a[p][j]=c*x-sn*y
                a[j][q]=a[q][j]=sn*x+c*y
    return sorted((a[i][i] for i in range(3)),reverse=True)


def cone_probability(d,t1,t2,n=8192):
    if d==0 or t1*t2==0:
        return 0.0
    l1,l2,l3=eigs_symmetric3(matrix_K(d,t1,t2))
    assert l1>0 and l2>0 and l3<0
    assert abs(-l3/l1-l3/l2-1)<3e-11
    aa=l1/(-l3);bb=l2/(-l3)
    total=0.0
    for k in range(n):
        phi=(k+.5)*2*pi/n
        c=aa*cos(phi)**2+bb*sin(phi)**2
        total+=1-sqrt(c/(1+c))
    return total/n


def main():
    rng=Random(26022261)
    exact_checks=0
    for j in range(2400):
        d=F(1+(j%9),1+(j%4))
        t1=F((j%13)-6,1+(j%5))
        t2=F((j%11)-5,1+(j%7))
        q1=F((j%17)-8,1+(j%6))
        q2=F((j%19)-9,1+(j%8))
        K=matrix_K(d,t1,t2)
        assert K[0][0]*K[1][1]-K[0][1]**2==0
        assert K[0][0]*K[2][2]-K[0][2]**2==0
        assert K[1][1]*K[2][2]-K[1][2]**2==0
        assert determinant3(K)==-16*d*d*t1*t1*t2*t2
        assert disc_via_q(d,t1,t2,q1,q2)==disc_via_matrix(F(7)-d,F(7)+d,t1,t2,q1,q2)
        T=t1*t1+t2*t2+4*d*d
        assert T**3>=108*d*d*t1*t1*t2*t2
        exact_checks+=6
    psharp=1-sqrt(2/3)
    assert abs(quad_probability_equal(2)-psharp)<2e-14
    for r in (0.05,0.1,0.3,0.5,0.8,1,1.5,1.9,2.1,2.5,3,4,8,20):
        assert quad_probability_equal(r)<psharp-1e-6
    # Check the full unequal-coupling Gaussian cone law as well.
    for t1,t2 in ((0.4,1.2),(1.,2.),(2.,1.),(4.,4.),(-2.,2.)):
        p=cone_probability(1.,t1,t2)
        assert 0<p<=psharp+1e-12
        if abs(t1)==abs(t2)==2.:
            assert abs(p-psharp)<1e-12
    # Draw the actual three-column Gaussian sketch, not only a Cauchy proxy.
    N=180000
    count=0
    for _ in range(N):
        a,b,c,d,z0,z1=(rng.gauss(0,1) for j in range(6))
        det=a*d-b*c
        if det==0:
            continue
        q1=(d*z0-b*z1)/det
        q2=(-c*z0+a*z1)/det
        if disc_via_q(1.,2.,2.,q1,q2)<0:
            count+=1
    empirical=count/N
    tolerance=7*sqrt(psharp*(1-psharp)/N)
    assert abs(empirical-psharp)<tolerance,(empirical,psharp,tolerance)
    # Validity of the sharpness example: Schur complement = 14/3 > 0.
    assert F(10)-F(4)*(F(1)+F(1,3))==F(14,3)
    print(f'VERIFY_OK exact_rational_identities={exact_checks} angular_checks=20 '
          f'gaussian_trials={N} empirical={empirical:.7f} '
          f'predicted={psharp:.7f} tolerance={tolerance:.7f}')


if __name__ == '__main__':
    main()
