#!/usr/bin/env python3
"""Standalone exact checks of idempotent generation counts over finite fields."""
from itertools import product, permutations
from collections import defaultdict
from math import prod
import random


def add(a,b,q):
    return (a+b)%q if q!=4 else a^b

def neg(a,q):
    return (-a)%q if q!=4 else a

def mul_f(a,b,q):
    if q!=4:
        return (a*b)%q
    z=0
    for i in range(2):
        if (b>>i)&1: z^=a<<i
    for i in (2,):
        if (z>>i)&1: z^=0b111<<(i-2)
    return z

def inv_f(a,q):
    assert a
    return next(z for z in range(1,q) if mul_f(a,z,q)==1)


def arena(n,q):
    positions=[(i,j) for i in range(n) for j in range(i,n)]
    loc={ij:t for t,ij in enumerate(positions)}
    degree=len(positions)
    identity=tuple(int(i==j) for i,j in positions)
    def matmul(x,y):
        out=[]
        for i,j in positions:
            z=0
            for k in range(i,j+1):
                z=add(z,mul_f(x[loc[i,k]],y[loc[k,j]],q),q)
            out.append(z)
        return tuple(out)
    def span_rank(vectors):
        basis={}
        for src in vectors:
            a=list(src)
            for pivot,b in sorted(basis.items()):
                scalar=a[pivot]
                if scalar:
                    a=[add(a[k],neg(mul_f(scalar,b[k],q),q),q) for k in range(degree)]
            if any(a):
                pivot=next(k for k,v in enumerate(a) if v)
                inv=inv_f(a[pivot],q)
                basis[pivot]=[mul_f(inv,v,q) for v in a]
        return len(basis)
    def generates(gens):
        basis=[identity]
        frontier=[identity]
        while frontier:
            new=[]
            for word in frontier:
                for x in gens:
                    product_word=matmul(word,x)
                    if span_rank(basis+[product_word])>len(basis):
                        basis.append(product_word)
                        new.append(product_word)
                        if len(basis)==degree:
                            return True
            frontier=new
        return False
    def criterion(gens):
        words=[tuple(g[loc[i,i]] for g in gens) for i in range(n)]
        if len(set(words))<n:return False
        for i in range(n-1):
            delta=[add(words[i][a],neg(words[i+1][a],q),q) for a in range(len(gens))]
            off=[g[loc[i,i+1]] for g in gens]
            if all(add(mul_f(delta[a],off[b],q),neg(mul_f(delta[b],off[a],q),q),q)==0
                   for a in range(len(gens)) for b in range(len(gens))):
                return False
        return True
    return degree,matmul,generates,criterion


def weighted_count(n,m,q):
    vertices=range(1<<m)
    count=0
    for bits in permutations(vertices,n):
        h=[(bits[i]^bits[i+1]).bit_count() for i in range(n-1)]
        if any(z<2 for z in h):continue
        far=sum((bits[i]^bits[j]).bit_count() for i in range(n) for j in range(i+2,n))
        count+=q**far*prod(q**z-q for z in h)
    return count



def poly_mul(a,b):
    out=defaultdict(int)
    for i,v in a.items():
        for j,w in b.items():out[i+j]+=v*w
    return {i:v for i,v in out.items() if v}

def poly_pow(a,e):
    out={0:1}
    for _ in range(e):out=poly_mul(out,a)
    return out

def weighted_polynomial(n,m):
    out=defaultdict(int)
    for bits in permutations(range(1<<m),n):
        h=[(bits[i]^bits[i+1]).bit_count() for i in range(n-1)]
        if any(v<2 for v in h):continue
        far=sum((bits[i]^bits[j]).bit_count() for i in range(n) for j in range(i+2,n))
        poly={far:1}
        for v in h:poly=poly_mul(poly,{v:1,1:-1})
        for k,c in poly.items():out[k]+=c
    return {k:v for k,v in out.items() if v}

def expected_polynomial(n):
    q={1:1}
    qm1={1:1,0:-1}
    if n==3:return poly_mul({0:48},poly_mul(poly_pow(q,3),poly_mul(poly_pow(qm1,2),{1:2,0:1})))
    if n==4:return poly_mul({0:24},poly_mul(poly_pow(q,6),poly_mul(poly_pow(qm1,3),{3:4,2:7,1:7,0:2})))
    if n==5:return poly_mul({0:48},poly_mul(poly_pow(q,11),poly_mul(poly_pow(qm1,4),poly_mul({1:1,0:1},{2:9,1:3,0:2}))))
    raise ValueError(n)

def direct(n,q,m):
    degree,matmul,generates,criterion=arena(n,q)
    idempotents=[v for v in product(range(q),repeat=degree) if matmul(v,v)==v]
    actual=0
    for gens in product(idempotents,repeat=m):
        p=criterion(gens)
        g=generates(gens)
        if p!=g:raise AssertionError(('wrong generation test',n,q,m,gens,p,g))
        actual+=g
    expected=weighted_count(n,m,q)
    assert actual==expected,(n,q,m,actual,expected)
    print('EXHAUSTIVE_PASS',n,q,m,'idempotents',len(idempotents),'generator_tuples',actual)


def sample(n,q,m,count,seed):
    degree,matmul,generates,criterion=arena(n,q)
    idempotents=[v for v in product(range(q),repeat=degree) if matmul(v,v)==v]
    rng=random.Random(seed)
    for _ in range(count):
        gens=[rng.choice(idempotents) for _ in range(m)]
        assert generates(gens)==criterion(gens)
    print('SAMPLE_PASS',n,q,m,count,seed)


def main():
    for n,q,m in [(2,2,2),(2,3,2),(2,4,2),(3,2,3)]: direct(n,q,m)
    sample(4,2,3,320,250)
    for n,poly in [(3,lambda q:48*q**3*(q-1)**2*(2*q+1)),
                   (4,lambda q:24*q**6*(q-1)**3*(4*q**3+7*q**2+7*q+2)),
                   (5,lambda q:48*q**11*(q-1)**4*(q+1)*(9*q**2+3*q+2))]:
        for q in (2,3,4,5): assert weighted_count(n,3,q)==poly(q)
        assert weighted_polynomial(n,3)==expected_polynomial(n),('polynomial mismatch',n,weighted_polynomial(n,3),expected_polynomial(n))
        print('SYMBOLIC_POLYNOMIAL_PASS',n,'q=2,3,4,5')
    assert weighted_count(2,2,2)==8
    assert weighted_count(3,2,2)==0
    print('ALL_IDEMPOTENT_GENERATOR_CHECKS_PASS')

if __name__=='__main__':main()
