#!/usr/bin/env python3
"""Exact polynomial certificate for temporal orbit populations of the binary prism XOR map."""

def mul(a,b):
    p=0
    while b:
        if b&1:p^=a
        a<<=1;b>>=1
    return p

def pow_poly(a,t):
    z=1
    while t:
        if t&1:z=mul(z,a)
        a=mul(a,a);t>>=1
    return z

def gcd(a,b):
    while b:
        r=a
        while r and r.bit_length()>=b.bit_length():r^=b<<(r.bit_length()-b.bit_length())
        a,b=b,r
    return a

def fixed(n,t):
    p=pow_poly(0b111,t)^pow_poly(0b10,t)
    g=gcd((1<<n)|1,mul(p,p) if t&1 else p)
    return 1<<((g.bit_length()-1)*(1 if t&1 else 2))

def main():
    checks=0
    for k in range(9):
        v=1<<k
        for n in (v,3*v):
            if n<3:continue
            A0=1<<min(v,4)
            assert fixed(n,1)==A0,(n,1,fixed(n,1),A0)
            checks+=1
            old=A0
            for j in range(1,k+4):
                t=1<<j
                expected=1<<(2*min(v,1<<(j+1)))
                got=fixed(n,t)
                assert got==expected,(n,t,got,expected)
                assert (got-old)%t==0,(n,t)
                assert got>=old
                old=got
                checks+=1
            assert old==(1<<(2*v)),(n,v)
            if k<=4:print('rim',n,'power2',v,'fixed',A0,'periodic',old,'maximal_period',max(2,v//2))
    print('exact_polynomial_gcd_power_two_family_PASS',checks)
if __name__=='__main__':main()
