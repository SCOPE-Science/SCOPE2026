"""Exact finite checks for the least ternary prime-power periods of A158690.

Reconstructs coefficients directly from the defining products and tests an
independent exponential-generating-function expansion.
"""
from math import comb


def g_coefficients(N):
    acc = [0]*N
    acc[0] = 1
    prod = [0]*N
    prod[0] = 1
    for m in range(1, N):
        a = 2*m-1
        f = [0]+[(-1)**(j+1)*comb(a+j-1,j) for j in range(1,N)]
        prod = [sum(prod[i]*f[j-i] for i in range(j+1)) for j in range(N)]
        acc = [acc[i]+prod[i] for i in range(N)]
    return acc


def original_egf_terms(N):
    # Exact integer coefficients of the exponential generating function.
    result = [0]*N
    result[0] = 1
    prod = [0]*N
    prod[0] = 1
    for m in range(1,N):
        odd = 2*m-1
        factor = [0]+[-(-odd)**j for j in range(1,N)]
        prod = [sum(comb(n,j)*prod[j]*factor[n-j] for j in range(n+1))
                for n in range(N)]
        result = [result[i]+prod[i] for i in range(N)]
    return result


def stirling_numbers(N):
    s=[[0]*N for _ in range(N)]
    s[0][0]=1
    for n in range(1,N):
        for k in range(1,n+1):
            s[n][k]=s[n-1][k-1]+k*s[n-1][k]
    return s


def a_mod(n,r,g):
    mod=3**r
    K=3*r
    c=[sum(g[k]*(-1)**(k-j)*comb(k,j) for k in range(j,K))%mod
       for j in range(K)]
    return sum(c[j]*pow(j,n,mod) for j in range(K))%mod


def run():
    g=g_coefficients(23)
    assert g[:6]==[1,1,2,7,33,197],g[:6]
    orig=original_egf_terms(16)
    s=stirling_numbers(16)
    from math import factorial
    for n in range(16):
        assert orig[n]==sum(g[k]*factorial(k)*s[n][k] for k in range(n+1)),n
    tests=0
    for r in range(1,8):
        mod=3**r
        period=2*3**(r-1)
        t=2*3**(r-2) if r>=2 else None
        n0=3*r
        for n in range(n0,n0+36):
            x=a_mod(n,r,g)
            assert a_mod(n+period,r,g)==x,(r,n,'period')
            if r>=2:
                delta=(a_mod(n+t,r,g)-x)%mod
                assert delta == (2*3**(r-1) if n%2==0 else 0),(r,n,delta)
            else:
                assert x== (2 if n%2==0 else 1),(r,n,x)
            tests+=1
    print('VERIFY_OK exact_g_prefix=6 independent_egf_coefficients=16 prime_power_levels=7 shifts='+str(tests))


if __name__=='__main__': run()
