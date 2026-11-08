"""Exact checks of the completely multiplicative GCD quadratic-form identity.
Science-only verifier; output supplies finite corroboration, not an infinite proof.
"""
from fractions import Fraction
from math import gcd


def mobius_upto(n):
    mu=[1]*(n+1); mu[0]=0
    for p in range(2,n+1):
        if all(p%d for d in range(2,int(p**.5)+1)):
            for j in range(p,n+1,p): mu[j]*=-1
            for j in range(p*p,n+1,p*p):mu[j]=0
    return mu

def sign_values(n,kind):
    if kind=='ones': return [0]+[1]*n
    if kind=='two_adic':
        a=[0]*(n+1); a[1]=1
        for i in range(2,n+1):a[i]=(-1 if i%2==0 else 1)*a[i//2] if i%2==0 else 1
        # correct all odd values one; even parity changes via n/2
        return a
    if kind=='liouville':
        a=[0]+[1]*n
        for i in range(2,n+1):
            if a[i]==1 and all(i%d for d in range(2,int(i**.5)+1)):
                for j in range(i,n+1,i):
                    k=j
                    while k%i==0:
                        a[j]*=-1;k//=i
        return a
    raise ValueError(kind)

def exact_direct(n,a):
    return sum((Fraction(a[i]*a[j]*gcd(i,j)**2,i*j) for i in range(1,n+1) for j in range(1,n+1)),Fraction())

def exact_decomposition(n,a):
    S=[Fraction()]
    for k in range(1,n+1):S.append(S[-1]+Fraction(a[k],k))
    mu=mobius_upto(n)
    j=[sum(Fraction(mu[d],d*d) for d in range(1,v+1) if v%d==0) for v in range(n+1)]
    return sum((j[d]*S[n//d]**2 for d in range(1,n+1)),Fraction())

def exact_convolution(n,a):
    S=[Fraction()]
    for k in range(1,n+1):S.append(S[-1]+Fraction(a[k],k))
    mu=mobius_upto(n)
    return sum((Fraction(mu[e],e*e)*sum((S[n//(e*j)]**2 for j in range(1,n//e+1)), Fraction()) for e in range(1,n+1)), Fraction())

if __name__=='__main__':
    for kind in ['ones','liouville','two_adic']:
        for n in [1,2,3,5,8,12,16,20,24]:
            a=sign_values(n,kind)
            d=exact_direct(n,a)
            j=exact_decomposition(n,a)
            c=exact_convolution(n,a)
            assert d==j==c,(n,kind,d,j,c)
        print('EXACT_THREE_WAY_IDENTITY_OK',kind,'N=1,2,3,5,8,12,16,20,24')
    from math import log
    zeta3=sum(1.0/(k*k*k) for k in range(1,1000001))
    limit=20000
    for kind in ['ones','liouville','two_adic']:
        a=sign_values(limit,kind)
        H=0.0;B=0.0; f=[]
        for q in range(1,limit+1):
            H+=a[q]/q
            B+=H*H/(q*(q+1))
        lower=B/zeta3
        upper=lower+(1+log(limit))**2/(zeta3*limit) * 5
        print('POSITIVE_CONSTANT_PARTIAL',kind,'B=',round(B,9),'c_partial=',round(lower,9),'c_upper_coarse=',round(upper,9))
    # Exact phase test in the Gaussian integers (the phase at 2 is i).
    for n in (3,6,9,14):
        a=[0]+[1j**((k & -k).bit_length()-1) for k in range(1,n+1)]
        direct=sum((complex(a[k]*a[j].conjugate())*gcd(k,j)**2/(k*j) for k in range(1,n+1) for j in range(1,n+1)),0j)
        S=[0j]
        for k in range(1,n+1): S.append(S[-1]+a[k]/k)
        mu=mobius_upto(n)
        jd=[sum((mu[e]/(e*e) for e in range(1,d+1) if d%e==0)) for d in range(n+1)]
        kernel=sum(jd[d]*abs(S[n//d])**2 for d in range(1,n+1))
        assert abs(direct-kernel)<1e-10,(n,direct,kernel)
    print('COMPLEX_UNIMODULAR_PHASE_CHECK_OK N=3,6,9,14')
    print('ALL_FINITE_CHECKS_OK')
