"""Independent finite-sum and high-temperature checks for a balanced bipartite occupation gas.
Finite calculations corroborate but do not prove the limit theorem.
"""
from math import comb, exp, log, factorial
import numpy as np
from scipy.special import gammaln


def z_one_side(beta, mu, J, k, t=0.0, cutoff=36):
    """Sum over A totals, analytically sum B totals; t tilts beta*J*M*N."""
    nmax = int(cutoff/(beta*mu))
    ans = 0.0
    for start in range(0, nmax+1, 200000):
        m = np.arange(start, min(nmax+1,start+200000),dtype=float)
        logmultip = gammaln(m+k) - gammaln(m+1) - gammaln(k)
        x = beta*(mu+(1+t)*J*m)
        terms = np.exp(logmultip-beta*mu*m-k*np.log(-np.expm1(-x)))
        ans += float(terms.sum())
    return ans


def check():
    c=0
    for k in range(1,5):
        for n in range(13):
            # Independent recursive composition count.
            def compositions(total, slots):
                if slots==1:return 1
                return sum(compositions(total-i,slots-1) for i in range(total+1))
            assert compositions(n,k)==comb(n+k-1,k-1)
            c+=1
    for beta,mu,J,k in [(0.8,1.3,2.1,1),(0.5,1.4,2.0,2),(0.6,1.1,1.2,3)]:
        nmax=45
        direct=sum(comb(m+k-1,k-1)*comb(n+k-1,k-1)*exp(-beta*(mu*(m+n)+J*m*n)) for m in range(nmax+1) for n in range(nmax+1))
        summed=z_one_side(beta,mu,J,k,cutoff=40)
        assert abs(direct-summed)/summed<1e-8,(direct,summed)
        c+=1
        # Exact independent double-sum test for the interaction-energy Laplace tilt.
        tilted=sum(comb(m+k-1,k-1)*comb(n+k-1,k-1)*exp(-beta*(mu*(m+n)+1.7*J*m*n)) for m in range(nmax+1) for n in range(nmax+1))
        z_t=z_one_side(beta,mu,J,k,t=0.7,cutoff=40)
        assert abs(tilted-z_t)/z_t<1e-8,(tilted,z_t)
        c+=1
    # Exactly solvable benchmark J=0: (1-e^{-beta*mu})^{-2k}.
    for k in range(1,5):
        for beta in [.3,.9,1.7]:
            z=z_one_side(beta,1.2,0.0,k,cutoff=40)
            z0=(1-exp(-beta*1.2))**(-2*k)
            assert abs(z-z0)/z0<2e-13,(beta,k,z,z0)
            c+=1
    # Check the (slow) characteristic logarithm through its one-decade increment.
    for k in [1,2,3]:
        mu=1.0;J=2.0
        vals=[]
        for beta in [1e-3,1e-4,1e-5]:
            z=z_one_side(beta,mu,J,k,cutoff=26)
            vals.append(z*(beta**k)*(J**k)*factorial(k-1))
        # Differences tend to log 10; finite-beta effects can remain.
        assert vals[2]>vals[1]>vals[0] and abs((vals[2]-vals[1])-log(10))<0.25,(k,vals)
        c+=1
        print('k=',k,'scaled partition values', vals,'last decade increment',vals[2]-vals[1], 'target',log(10))
    # Under a uniform weak composition, the normalized quadratic share moment
    # is exactly 2/(k+1)+(k-1)/((k+1)*m), approaching the Dirichlet limit.
    def compositions_list(m,k):
        if k==1:
            yield (m,)
        else:
            for j in range(m+1):
                for other in compositions_list(m-j,k-1):
                    yield (j,)+other
    for k in [2,3,4]:
        for m in [8,15,25]:
            allc=list(compositions_list(m,k))
            val=sum(sum((x/m)**2 for x in z) for z in allc)/len(allc)
            expected=2/(k+1)+(k-1)/((k+1)*m)
            assert abs(val-expected)<1e-10,(k,m,val,expected)
            c+=1
    # Laplace identity: changing J to (1+t)J exactly tilts beta*J*M*N.
    for k in [1,2,3]:
        for b in [0.05,0.1]:
            for t in [0.0,0.5,1.0]:
                a=z_one_side(b,1.0,2.0,k,t=t,cutoff=38)
                ratio=a/z_one_side(b,1.0,2.0,k,cutoff=38)
                assert 0<ratio<=1+1e-10
                assert ratio>=1/(1+t)**k - 0.5
                c+=1
    print('PASSED',c,'checks')

if __name__=='__main__':check()
