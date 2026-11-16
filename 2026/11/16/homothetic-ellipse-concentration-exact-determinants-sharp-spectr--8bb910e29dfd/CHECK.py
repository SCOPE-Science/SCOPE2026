"""Exact and high-precision checks for homothetic ellipse polynomial concentration.
Requires sympy and mpmath. No network access is used.
"""
from fractions import Fraction
from math import comb
import sympy as sp
import mpmath as mp


def moments(a,b,n):
    a,b=sp.Rational(a),sp.Rational(b)
    u,v=(a+b)/2,(a-b)/2
    G=sp.zeros(n+1)
    for i in range(n+1):
        for j in range(n+1):
            if (i+j)%2: continue
            m=(i+j)//2
            G[i,j]=sum(sp.binomial(i,k)*sp.binomial(j,m-k)
                *u**k*v**(i-k)*v**(m-k)*u**(j-(m-k))
                for k in range(i+1) if 0<=m-k<=j)/(m+1)
    return G


def monic_ellipse_chebyshev(n,a,b):
    z=sp.Symbol('z'); q=sp.Rational(a)**2-sp.Rational(b)**2
    f0,f1=sp.S(1),z
    if n==0:return f0
    for k in range(2,n+1):f0,f1=f1,sp.expand(z*f1-q*sp.Rational(1,4)*f0)
    return f1


def main():
    for a,b in [(3,2),(5,1)]:
        for n in range(1,7):
            G=moments(a,b,n); assert G.det()>0
            z=sp.Symbol('z'); p=monic_ellipse_chebyshev(n,a,b)
            co=sp.Matrix([sp.expand(p).coeff(z,k) for k in range(n+1)])
            H=sp.simplify((co.T*G*co)[0]);
            assert all(sp.simplify((co.T*G[:,j])[0])==0 for j in range(n))
            c2=sp.Rational(a)**2-sp.Rational(b)**2
            U=sp.chebyshevu(n,(sp.Rational(a)**2+sp.Rational(b)**2)/c2)
            H_formula=(c2/4)**n*U/(n+1)
            assert sp.simplify(H-H_formula)==0
            diag=G[n,n]
            assert sp.simplify(diag-sum(sp.binomial(n,k)**2*((sp.Rational(a)+b)/2)**(2*k)*((sp.Rational(a)-b)/2)**(2*(n-k)) for k in range(n+1))/(n+1))==0
            for t in [sp.Rational(1,3),sp.Rational(2,3)]:
                D=sp.diag(*[t**i for i in range(n+1)])
                Gt=t*t*D*G*D
                assert sp.simplify(Gt.det()/G.det()-t**((n+1)*(n+2)))==0
            mp.mp.dps=90
            A=mp.matrix([[mp.mpf(int(G[i,j].p))/int(G[i,j].q) for j in range(n+1)] for i in range(n+1)])
            L=mp.cholesky(A); Li=L**-1
            for tf in [mp.mpf('0.04'),mp.mpf('0.02')]:
                Dt=mp.diag([tf**i for i in range(n+1)])
                At=tf**2*Dt*A*Dt
                T=Li*At*Li.T
                lambdas,Vec=mp.eigsy(T)
                lam_min=lambdas[0];lam_max=lambdas[n]
                Cmin=mp.mpf(int(H.p))/int(H.q)/(mp.mpf(int(diag.p))/int(diag.q))
                Ginv=A**-1
                Cmax=A[0,0]*Ginv[0,0]
                # All spectral exponents and exterior-power constants.
                minors=[mp.mpf(1)]
                for kk in range(1,n+2):
                    det_g=mp.det(mp.matrix([[A[i,j] for j in range(kk)] for i in range(kk)]))
                    det_inv=mp.det(mp.matrix([[Ginv[i,j] for j in range(kk)] for i in range(kk)]))
                    minors.append(det_g*det_inv)
                for jj in range(n+1):
                    coefficient=minors[jj+1]/minors[jj]
                    actual=lambdas[n-jj]/tf**(2*jj+2)
                    assert abs(actual/coefficient-1)<mp.mpf('0.05'),(a,b,n,tf,jj,'spectrum')
                # Small t errors are O(t^2), with nonzero constants.
                assert abs(lam_min/tf**(2*n+2)/Cmin-1)<mp.mpf('0.05'),(a,b,n,tf,'min')
                assert abs(lam_max/tf**2/Cmax-1)<mp.mpf('0.05'),(a,b,n,tf,'max')
                eigvec=Li.T*Vec[:,0]
                qcoeff=[eigvec[k]/eigvec[n]*tf**(k-n) for k in range(n+1)]
                pcoeff=[mp.mpf(str(co[k])) for k in range(n+1)]
                for k in range(n+1):
                    assert abs(qcoeff[k]-pcoeff[k])<mp.mpf('0.09')*max(1,abs(pcoeff[k])),(a,b,n,tf,k,qcoeff[k],pcoeff[k])
            print('ELLIPSE_EXACT_AND_ASYMPTOTIC_PASS',a,b,n)
    print('HOMOTHETIC_ELLIPSE_CONCENTRATION_PASS')

if __name__=='__main__': main()
