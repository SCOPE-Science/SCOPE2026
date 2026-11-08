"""Exact finite checks of odd strongly unimodal residues modulo four."""
from math import isqrt, pi, log


def coefficients(limit):
    # q^{2j+1} prod_{h=0}^{j-1}(1+q^{2h+1})^2 (all arithmetic modulo 4).
    coefficients = [0] * (limit+1)
    product = [0] * (limit+1)
    product[0] = 1
    for j in range((limit-1)//2 + 1):
        shift = 2*j+1
        for i in range(limit+1-shift):
            coefficients[i+shift] = (coefficients[i+shift]+product[i])%4
        # Multiply by (1+q^{shift})^2
        new_product = product[:]
        for i in range(limit+1-shift):
            new_product[i+shift] = (new_product[i+shift]+2*product[i])%4
        for i in range(limit+1-2*shift):
            new_product[i+2*shift] = (new_product[i+2*shift]+product[i])%4
        product = new_product
    return coefficients


def odd_coefficient_predicates(n):
    assert n>=1 and n%2
    t=3*n-1
    odd = t%2==0 and isqrt(t//2)**2 == t//2
    if odd: return True,False
    factors=[]
    v=0
    while t%2==0:
        t//=2;v+=1
    d=3
    while d*d<=t:
        if t%d==0:
            e=0
            while t%d==0:
                t//=d;e+=1
            factors.append((d,e))
        d+=2
    if t>1: factors.append((t,1))
    oddexps = [(p,e) for p,e in factors if e%2]
    two = (len(oddexps)==1 and oddexps[0][1]%4==1
           and oddexps[0][0]%8 in (5,7))
    return False,two


def primality_sieve(limit):
    data=bytearray(b'\x01')*(limit+1)
    data[0:2]=b'\x00\x00'
    for p in range(2,isqrt(limit)+1):
        if data[p]:
            data[p*p:limit+1:p]=b'\x00'*(((limit-p*p)//p)+1)
    return data


def exact_count(limit, prime_flag):
    # Enumerate the *classification* independent of the generating function.
    bound=3*limit-1
    out=0
    vals=[]
    for eps in (1,2):
        mmax=isqrt(bound//eps)
        for m in range(1,mmax+1):
            if m%3==0 or (eps==1 and m%2): continue
            pmax=bound//(eps*m*m)
            for p in range(5,pmax+1):
                if prime_flag[p] and p%8 in (5,7) and p%3==(2 if eps==1 else 1) and m%p:
                    # p^1 family, distinct per pair; p^(4k+1), k>=1 are below checked separately.
                    vals.append((eps,m,p,1))
                    for ex in range(5,100,4):
                        if eps*m*m*(p**ex)>bound:break
                        vals.append((eps,m,p,ex))
    indices=set()
    for eps,m,p,ex in vals:
        t=eps*m*m*(p**ex)
        assert t%6==2
        n=(t+1)//3
        assert n%2==1 and n<=limit
        assert n not in indices, (n,eps,m,p,ex)
        indices.add(n)
        out+=1
    return out


if __name__=='__main__':
    bound=5000
    coefficients_mod4=coefficients(bound)
    counts={"odd":0,"two":0,"zero":0}
    for n in range(1,bound+1,2):
        odd,two=odd_coefficient_predicates(n)
        assert not (odd and two)
        v=coefficients_mod4[n]
        assert (v%2==1)==odd,(n,v,odd,two)
        assert (v==2)==two,(n,v,odd,two)
        counts['odd' if odd else 'two' if two else 'zero']+=1
    print('GF_EXACT_OK odd_n<=',bound,'residues=',counts,'p_fifth_power_case=',coefficients_mod4[4167])
    for limit in (10000,100000,1000000):
        flags=primality_sieve(3*limit)
        exact=exact_count(limit,flags)
        approx=(pi*pi/12)*limit/log(limit)
        print('SIEVE_EXACT X=',limit,'count_two=',exact,'main_term=',round(approx,2),'ratio=',round(exact/approx,6))
    print('VERIFY_OK separate_computational_routes=yes modular_arithmetic=exact')
