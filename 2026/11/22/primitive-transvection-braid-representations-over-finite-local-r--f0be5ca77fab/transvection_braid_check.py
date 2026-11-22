"""Finite-ring checks for primitive-transvection braid fibers.
Run with Python 3; no nonstandard packages required.
"""
from itertools import product

def ring(p, dual):
    if not dual:
        els=list(range(p))
        add=lambda a,b:(a+b)%p
        mul=lambda a,b:(a*b)%p
        red=lambda a:a
    else:
        els=list(range(p*p))
        add=lambda a,b:((a%p+b%p)%p)+p*((a//p+b//p)%p)
        mul=lambda a,b:((a%p)*(b%p)%p)+p*((a%p*(b//p)+(a//p)*(b%p))%p)
        red=lambda a:a%p
    return els,add,mul,red

def matmul(A,B,n,add,mul):
    return tuple(sumlike((mul(A[i*n+k],B[k*n+j]) for k in range(n)),add) for i in range(n) for j in range(n))

def sumlike(vals,add):
    s=0
    for x in vals: s=add(s,x)
    return s

def rank1_primitive(p,dual,n):
    els,add,mul,red=ring(p,dual)
    neg=lambda a:next(e for e in els if add(a,e)==0)
    sols=set()
    for u in product(els,repeat=n):
        if not any(red(x) for x in u): continue
        for v in product(els,repeat=n):
            if not any(red(x) for x in v):continue
            if sumlike((mul(u[i],v[i]) for i in range(n)),add):continue
            A=tuple(mul(u[i],v[j]) for i in range(n) for j in range(n))
            sols.add(A)
    return sorted(sols), (els,add,mul,red)

def run(p,dual,n):
    S,(els,add,mul,red)=rank1_primitive(p,dual,n)
    T=len(els); h=T//p
    predicted=len(S)*(1+T**(2*n-3))
    expected=h**(2*n-2)*(p**n-1)*(p**(n-1)-1)//(p-1)
    assert len(S)==expected,(p,dual,n,len(S),expected)
    I=tuple(int(i==j) for i in range(n) for j in range(n))
    roots=[tuple(add(I[k],A[k]) for k in range(n*n)) for A in S]
    actual=0; nontriv=0
    for i,X in enumerate(roots):
      for j,Y in enumerate(roots):
        lhs=matmul(matmul(X,Y,n,add,mul),X,n,add,mul)
        rhs=matmul(matmul(Y,X,n,add,mul),Y,n,add,mul)
        if lhs==rhs:
            actual+=1
            nontriv+=i!=j
    assert actual==predicted,(p,dual,n,actual,predicted)
    assert nontriv==len(S)*T**(2*n-3)
    print('PASS',dict(q=p,dual=dual,n=n,ring_size=T,transvections=len(S),nontrivial_braid_pairs=nontriv,all_braid_pairs=actual))

if __name__=='__main__':
    for cfg in [(2,False,2),(3,False,2),(5,False,2),(2,True,2),(3,True,2),(2,False,3),(2,True,3)]:
        run(*cfg)

# Independent finite-ring comparisons with identical residue-field size and ring order.
def run_same_order_ring(model):
    p=2; n=2; els=list(range(8))
    if model=='Z8':
        add=lambda a,b:(a+b)%8
        mul=lambda a,b:(a*b)%8
    elif model=='cubic':
        add=lambda a,b:a^b
        mul=lambda a,b: (((a&1)*(b&1)) & 1) | (((((a&1)*((b>>1)&1))+(((a>>1)&1)*(b&1)))&1)<<1) | (((((a&1)*((b>>2)&1))+(((a>>1)&1)*((b>>1)&1))+(((a>>2)&1)*(b&1)))&1)<<2)
    elif model=='plane':
        add=lambda a,b:a^b
        mul=lambda a,b: (((a&1)*(b&1)) & 1) | (((((a&1)*((b>>1)&1))+(((a>>1)&1)*(b&1)))&1)<<1) | (((((a&1)*((b>>2)&1))+(((a>>2)&1)*(b&1)))&1)<<2)
    else: raise ValueError(model)
    red=lambda a:a&1
    S=set()
    for u in product(els,repeat=n):
      if not any(red(x) for x in u):continue
      for v in product(els,repeat=n):
        if not any(red(x) for x in v):continue
        if sumlike((mul(u[i],v[i]) for i in range(n)),add):continue
        S.add(tuple(mul(u[i],v[j]) for i in range(n) for j in range(n)))
    I=(1,0,0,1)
    roots=[tuple(add(I[i],A[i]) for i in range(4)) for A in S]
    actual=sum(matmul(matmul(X,Y,2,add,mul),X,2,add,mul)==matmul(matmul(Y,X,2,add,mul),Y,2,add,mul) for X in roots for Y in roots)
    assert len(S)==48 and actual==432,(model,len(S),actual)
    print('PASS',dict(model=model,q=2,ring_size=8,n=2,transvections=len(S),braid_pairs=actual))

if __name__=='__main__':
    for model in ('Z8','cubic','plane'):run_same_order_ring(model)
