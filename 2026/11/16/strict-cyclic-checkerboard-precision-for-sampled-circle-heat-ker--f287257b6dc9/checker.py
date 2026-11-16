"""Checks for a cyclic Fourier precision sign theorem.
This is verification, not an infinite-parameter proof.
"""
import sympy as sp
import mpmath as mp


def product_spectrum_coeffs(n, params):
    # z^n = 1; each factor (1+a*z)(1+a*z^-1).
    coeff = [sp.Integer(0)] * n
    coeff[0] = sp.Integer(1)
    for a in params:
        fac = [sp.Integer(0)] * n
        fac[0] += 1+a*a
        fac[1 % n] += a
        fac[(-1) % n] += a
        coeff = [sum(coeff[k]*fac[(j-k) % n] for k in range(n))
                 for j in range(n)]
    return coeff


def exact_tests():
    tests = 0
    for n in range(2, 16):
        for params in [(sp.Rational(1, 2),),
                       (sp.Rational(1, 3), sp.Rational(3, 5)),
                       (sp.Rational(1, 2), sp.Rational(2, 3), sp.Rational(1, 7))]:
            c=product_spectrum_coeffs(n, params)
            K=sp.Matrix(n,n,lambda i,j:c[(i-j)%n])
            Q=K.inv()
            for i in range(n):
                for j in range(n):
                    d=min((i-j)%n,(j-i)%n)
                    assert (-1)**d*Q[i,j]>0, (n,params,i,j,Q[i,j])
                    tests+=1
            assert K*Q==sp.eye(n)
            tests+=1
    return tests


def heat_tests():
    mp.mp.dps=105
    tests=0
    for n in range(2,21):
        for t in ['0.04','0.07','0.12','0.3','0.7','1.5','4','10','20']:
            t=mp.mpf(t)
            # λ_r = n sum_{k∈Z} exp(-t(r+kn)^2)
            M=int(mp.ceil(mp.sqrt(mp.mpf(265)/t)/n))+3
            lam=[n*sum(mp.exp(-t*(r+n*k)**2) for k in range(-M,M+1))
                 for r in range(n)]
            for d in range(n):
                q=mp.re(sum(mp.exp(2j*mp.pi*r*d/n)/lam[r] for r in range(n))/n)
                dist=min(d,n-d)
                # avoid false near-cancellation when n tiny and t very small
                if abs(q)>mp.mpf('1e-75'):
                    assert (-1)**dist*q>0,(n,str(t),d,str(q))
                    tests+=1
            # Compare direct matrix inverse at moderate t where stable
            if mp.mpf('0.3')<=t<=mp.mpf('4') and n<=12:
                K=mp.matrix([[sum(mp.exp(-t*k*k)*mp.exp(2j*mp.pi*k*(i-j)/n) for k in range(-90,91)).real for j in range(n)] for i in range(n)])
                Q=mp.inverse(K)
                for d in range(n):
                    q=mp.re(sum(mp.exp(2j*mp.pi*r*d/n)/lam[r] for r in range(n))/n)
                    assert abs(Q[0,d]-q)<mp.mpf('1e-23')*max(1,abs(q)), (n,str(t),d)
                    tests+=1
    return tests


def unimodality_tests():
    tests=0
    for half in range(2,19):
        N=2*half
        for r in range(half+1):
            for s in range(half+1):
                X={j for j in range(N) if min(j,N-j)<=r}
                Y={j for j in range(N) if min(j,N-j)<=s}
                counts=[len(X.intersection({(k+d)%N for k in Y})) for d in range(half+1)]
                assert all(counts[d]>=counts[d+1] for d in range(half)),(N,r,s)
                tests+=half
    return tests

if __name__=='__main__':
    a=exact_tests(); print('exact product-spectrum rational matrix checks:',a,flush=True)
    b=unimodality_tests(); print('exact circular-arc convolution checks:',b,flush=True)
    c=heat_tests(); print('high-precision heat covariance tests:',c,flush=True)
    print('PASS total assertions:',a+b+c)
