#!/usr/bin/env python3
"""Exact cyclotomic verification of the length-two hyperbolic-shell Fourier support."""
from itertools import product
import argparse


def operations(p, split):
    modulus = p * p
    def add(a,b):
        if not split:
            return (a+b) % modulus
        return ((a % p + b % p) % p) + p * (((a//p)+(b//p)) % p)
    def mul(a,b):
        if not split:
            return (a*b) % modulus
        a0,a1=a%p,a//p
        b0,b1=b%p,b//p
        return (a0*b0)%p + p*((a0*b1+a1*b0)%p)
    def negative(a):
        return (modulus-a)%modulus if not split else ((-a%p)+p*(-(a//p)%p))
    def residue(a):
        return a%p
    def char_exp(a):
        return a//p if split else a
    def socle(a):
        return a%p==0
    return modulus,add,mul,negative,residue,char_exp,socle


def dot(x,y,add,mul):
    v=0
    for a,b in zip(x,y): v=add(v,mul(a,b))
    return v


def cyclotomic_zero(counts,p,split):
    stride = 1 if split else p
    return all(len({counts[r+i*stride] for i in range(p)})==1 for r in range(stride))


def check(p,n,split):
    modulus,add,mul,neg,residue,phase,socle=operations(p,split)
    vec=list(product(range(modulus),repeat=n))
    origin=(0,)*n
    shell=[(x,y) for x in vec for y in vec if dot(x,y,add,mul)==1]
    assert len(shell)==p**(4*n-2)-p**(3*n-2)
    expected=p**(2*n)*(1+(p**n-1)*p**(n-1)*(p-1)//(2 if p%2 else 1))
    actual=0
    for a in vec:
        for b in vec:
            c=dot(a,b,add,mul)
            residue_c=residue(c)
            expected_nonzero=(all(socle(z) for z in a+b) or
              (residue_c!=0 and (p%2==0 or pow(residue_c,(p-1)//2,p)==1)))
            counts=[0]*(p if split else modulus)
            for x,y in shell:
                e=phase(add(dot(a,x,add,mul),dot(b,y,add,mul)))
                counts[e]+=1
            is_zero=cyclotomic_zero(counts,p,split)
            if is_zero==expected_nonzero:
                raise AssertionError((p,n,split,a,b,expected_nonzero,counts))
            actual+=not is_zero
    assert actual==expected,(p,n,split,actual,expected)
    print('EXACT_SHELL_OK',{'p':p,'n':n,'ring':'split' if split else 'cyclic',
                            'frequencies':len(vec)**2,'shell':len(shell),'Fourier_rank':actual})

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--fast',action='store_true');a=parser.parse_args()
    for p,n,split in [(2,1,False),(2,2,False),(2,1,True),(2,2,True),(3,1,False),(3,2,False),(3,1,True),(3,2,True),(5,1,False)]:
        check(p,n,split)
    print('ALL_EXACT_HYPERBOLIC_SHELL_TESTS_OK')

def check_split_f4():
    # GF(4)=GF(2)[a]/(a^2+a+1); R=GF(4)[t]/(t^2).
    def fm(a,b):
        v=0
        for i in range(2):
            if (b>>i)&1:v ^=a<<i
        if v&8:v^=0b1001 # a^3=1
        if v&4:v^=0b111 # a^2=a+1
        return v
    def add(a,b):return a^b
    def mul(a,b):return fm(a&3,b&3) | (fm(a&3,b>>2)^fm(a>>2,b&3))<<2
    def char(a):
        # tr(1)=0, tr(alpha)=tr(alpha+1)=1
        return ((a>>2)&3) in (2,3)
    q=4
    for n, samples in [(1,None),(2,400)]:
        vv=list(product(range(16),repeat=n))
        shell=[(x,y) for x in vv for y in vv if dot(x,y,add,mul)==1]
        assert len(shell)==q**(4*n-2)-q**(3*n-2)
        import random
        all_freq=[(a,b) for a in vv for b in vv]
        if samples is not None:
            rng=random.Random(20261101)
            all_freq=rng.sample(all_freq,samples)
        for a,b in all_freq:
            c=dot(a,b,add,mul)
            predicted=all((z&3)==0 for z in a+b) or (c&3)!=0
            total=sum(-1 if char(add(dot(a,x,add,mul),dot(b,y,add,mul))) else 1 for x,y in shell)
            assert (total!=0)==predicted,(n,a,b,total,predicted)
        print('F4_SPLIT_EXACT_OK',{'n':n,'frequencies_checked':len(all_freq),'shell':len(shell)})

if __name__ == '__main__':
    check_split_f4()
