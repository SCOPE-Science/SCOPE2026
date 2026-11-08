#!/usr/bin/env python3
"""Independent incidence construction and binary wave fixed-space calculations."""
from itertools import product

def field(s):
    assert s in (2, 3, 4, 5, 8)
    if s in (2, 3, 5):
        add=lambda x,y:(x+y)%s
        mul=lambda x,y:(x*y)%s
    else:
        poly={4:0b111, 8:0b1011}[s]
        add=lambda x,y:x^y
        def mul(x,y):
            z=0
            while y:
                if y&1:z^=x
                y>>=1;x<<=1
                if x&s:x^=poly
            return z
    return add,mul

def projective(s):
    add,mul=field(s)
    inv={a:next(b for b in range(1,s) if mul(a,b)==1) for a in range(1,s)}
    normalized=set()
    for v in product(range(s),repeat=3):
        if not any(v):continue
        a=next(x for x in v if x)
        normalized.add(tuple(mul(x,inv[a]) for x in v))
    vs=sorted(normalized)
    assert len(vs)==s*s+s+1
    B=[]
    for p in vs:
        row=0
        for j,l in enumerate(vs):
            z=0
            for a,b in zip(p,l):z=add(z,mul(a,b))
            if z==0:row|=1<<j
        B.append(row)
    return B

def rank(rows):
    bas={}
    for v in rows:
        while v:
            k=v.bit_length()-1
            if k not in bas:
                bas[k]=v;break
            v^=bas[k]
    return len(bas)

def ident(n):return [1<<i for i in range(n)]

def matmul(L,R):
    out=[]
    for r in L:
        acc=0
        while r:
            b=r&-r
            acc^=R[b.bit_length()-1]
            r-=b
        out.append(acc)
    return out

def power(M,k):
    ans=ident(len(M));a=M
    while k:
        if k&1:ans=matmul(ans,a)
        a=matmul(a,a);k>>=1
    return ans

def matwave(B):
    v=len(B); m=2*v; d=2*m
    # Point and line adjacency; columns are line coordinates.
    adj=[B[i]<<v for i in range(v)]
    for j in range(v):
        adj.append(sum(1<<i for i in range(v) if B[i]>>j&1))
    return [adj[i]|(1<<(m+i)) for i in range(m)]+[1<<i for i in range(m)]

def pred_dim(s,rank_b,t):
    v=s*s+s+1
    b=t&-t
    if s&1:
        return 2*min(2,b)*(1+(v-1)*(t%3==0))
    r=rank_b-1
    return 2*min(2,b)*(t%3==0)+2*r*min(4,b)+(2*(v-1)-4*r)*min(2,b)

def main():
    for s in (2,3,4,5,8):
        B=projective(s);v=len(B);rho=rank(B)
        expected_rho=v-1 if s&1 else (3**(s.bit_length()-1)+1 if s&(s-1)==0 else None)
        assert rho==expected_rho,(s,rho,expected_rho)
        T=matwave(B)
        assert matmul(T,power(T,11 if s%2==0 else 5))==ident(4*v)
        obs={}
        for t in (1,2,3,4,6,12):
            Q=power(T,t)
            fixdim=4*v-rank([row^(1<<i) for i,row in enumerate(Q)])
            wanted=pred_dim(s,rho,t)
            assert fixdim==wanted,(s,t,fixdim,wanted)
            obs[t]=fixdim
        print(f'order={s} vertices={2*v} binary_incidence_rank={rho} wave_order={12 if s%2==0 else 6} fixed_dimensions={obs}')
    print('PASS: direct binary matrix powers agree with all predicted dimensions.')

if __name__=='__main__':main()
