#!/usr/bin/env python3
"""Direct GF(2) wave matrix rank checks on Cartesian products of cliques."""
import itertools, math

def rank(rows,n):
    basis={}
    for x in rows:
        while x:
            p=x.bit_length()-1
            if p in basis:x^=basis[p]
            else:basis[p]=x;break
    return len(basis)

def prod(xs):return math.prod(xs)

def formula(qs):
    d=len(qs);odd=[q for q in qs if q&1];even=[q for q in qs if not q&1]
    W=prod(odd);P=prod(q-2 for q in odd);B=prod(even);C=prod(q-2 for q in even)
    assert (B-C)%2==0
    R=(B-C)//2
    h=[(W+(1 if ((a-d)%2)==0 else -1)*P)//2 for a in (0,1)]
    z0,z1=(h[0]*(B+C)//2,h[1]*(B+C)//2)
    D=[z0,2*z0,z0+2*z1,2*h[0]*B,2*z0+2*h[1]*B,2*B*W]
    return {k:2**x for k,x in zip((1,2,3,4,6,12),D)}

def mat(qs):
    vs=list(itertools.product(*(range(q) for q in qs)))
    n=len(vs); A=[]
    for u in vs:A.append(sum(1<<j for j,v in enumerate(vs) if sum(x!=y for x,y in zip(u,v))==1))
    rows=[A[i]|(1<<(n+i)) for i in range(n)] + [1<<i for i in range(n)]
    return rows

def compose(A,B):
    out=[]
    for x in A:
        r=0
        while x:
            l=x&-x;j=l.bit_length()-1;r^=B[j];x-=l
        out.append(r)
    return out

def fixed(A,t):
    n=len(A)
    I=[1<<i for i in range(n)]
    power=I
    for _ in range(t):power=compose(power,A)
    return 2**(n-rank([power[i]^I[i] for i in range(n)],n))

def run():
    families=[(2,), (3,), (4,), (5,), (2,2), (2,3), (3,3), (2,4), (3,4), (2,2,2), (2,2,3), (2,3,3), (2,2,4), (3,3,3), (2,2,2,2), (2,2,2,3), (2,2,3,3), (2,3,4), (2,2,2,2,2)]
    for qs in families:
        T=mat(qs);F=formula(qs)
        assert all(fixed(T,t)==F[t] for t in F),(qs,F)
        assert fixed(T,12)==(1<<(2*prod(qs)))
    print('MATRIX_RANK_CHECK_OK',len(families),'families', 'max_vertices',max(prod(q) for q in families))
    for qs in [(2,3),(2,2,3),(2,3,3)]:
        F=formula(qs)
        p12=(F[12]-F[6]-F[4]+F[2])//12
        assert p12>0
        print('EXAMPLE',qs,'F',[F[k] for k in (1,2,3,4,6,12)],'period12_orbits',p12)

if __name__=='__main__':run()
