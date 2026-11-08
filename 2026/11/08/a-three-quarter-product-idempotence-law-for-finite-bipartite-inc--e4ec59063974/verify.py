"""Independent finite checks for products of idempotents in height-two incidence algebras.
All arithmetic is over prime fields in the direct matrix tests; symbolic counts hold
for every finite field. No third-party dependencies.
"""
from itertools import product
from math import comb

STATES=[(0,0),(0,1),(1,0),(1,1)]

def exponent(left,right):
    a,c=left; b,d=right
    fx=int(a!=b); fy=int(c!=d)
    rank=int(a*c==b*d and (a*fy or d*fx))
    return fx+fy-rank

W=[[exponent(s,t) for t in STATES] for s in STATES]
assert W==[[0,1,1,2],[1,0,2,1],[1,1,0,1],[2,1,1,0]]

def count_idem(a,b,q):
    return sum(comb(a,i)*comb(b,j)*q**(i*(b-j)+(a-i)*j)
               for i in range(a+1) for j in range(b+1))

def compositions(n,k):
    if k==1:
        yield (n,)
    else:
        for i in range(n+1):
            for t in compositions(n-i,k-1):yield (i,)+t

def multinom(n,ct):
    x=1; s=n
    for c in ct:
        x*=comb(s,c);s-=c
    return x

W_BOTH=[[0,1,1,2],[1,0,1,1],[1,1,0,1],[2,1,1,0]]

def count_both(a,b,q):
    tot=0
    for alpha in compositions(a,4):
        multiplier=multinom(a,alpha)
        vertex_sum=sum(q**sum(alpha[s]*W_BOTH[s][t] for s in range(4)) for t in range(4))
        tot+=multiplier*vertex_sum**b
    return tot

def count_product(a,b,q):
    tot=0
    for alpha in compositions(a,4):
        multiplier=multinom(a,alpha)
        vertex_sum=sum(q**sum(alpha[s]*W[s][t] for s in range(4)) for t in range(4))
        tot+=multiplier*vertex_sum**b
    return tot

def matrix_set(a,b,q):
    n=a+b
    edges=[(i,j) for i in range(a) for j in range(a,n)]
    items=[]
    def mul(A,B):
        return tuple(sum(A[i*n+k]*B[k*n+j] for k in range(n))%q for i in range(n) for j in range(n))
    for diag in product(range(q),repeat=n):
        if any(z not in (0,1) for z in diag):continue
        for upper in product(range(q),repeat=len(edges)):
            M=[0]*(n*n)
            for i,t in enumerate(diag):M[i*n+i]=t
            for (i,j),v in zip(edges,upper):M[i*n+j]=v
            M=tuple(M)
            if mul(M,M)==M:items.append(M)
    return items,mul

def direct(a,b,q):
    idem,mul=matrix_set(a,b,q)
    good=0; both=0
    for e in idem:
        for f in idem:
            z=mul(e,f)
            if mul(z,z)==z:
                good+=1
                w=mul(f,e)
                if mul(w,w)==w:both+=1
    return len(idem),good,both

def main():
    for q in [2,3]:
        for s in STATES:
            for t in STATES:
                a,c=s;b,d=t
                # Independent enumeration of all permitted off-diagonal entries.
                xs=range(q) if a!=b else (0,)
                ys=range(q) if c!=d else (0,)
                count=0
                for x in xs:
                    for y in ys:
                        v=(a*y+x*d)%q
                        if ((a*c+b*d-1)*v)%q==0:count+=1
                assert count==q**exponent(s,t),(q,s,t,count)
    print('LOCAL_SPIN_TABLE_OK',W)
    for q in (2,3):
        for ss,s in enumerate(STATES):
            for tt,t in enumerate(STATES):
                a,c=s;b,d=t
                cnt=0
                for x in (range(q) if a!=b else (0,)):
                    for y in (range(q) if c!=d else (0,)):
                        z=(a*y+x*d)%q
                        w=(c*x+y*b)%q
                        if ((a*c+b*d-1)*z)%q==0 and ((a*c+b*d-1)*w)%q==0:cnt+=1
                assert cnt==q**W_BOTH[ss][tt]
    print('LOCAL_BOTH_TABLE_OK',W_BOTH)
    cases=[(1,1,2),(1,1,3),(1,2,2),(1,2,3),(2,2,2),(2,2,3),(2,3,2)]
    for a,b,q in cases:
        predicted=(count_idem(a,b,q),count_product(a,b,q),count_both(a,b,q))
        actual=direct(a,b,q)
        assert predicted==actual,(a,b,q,predicted,actual)
        print('DIRECT_OK',a,b,q,actual)
    for q in (2,3,4,5):
        for n in (4,8,12,16,20,30):
            I=count_idem(n,n,q)
            S=count_product(n,n,q)
            assert S<=I*I
            B=count_both(n,n,q)
            assert B<=S
            from decimal import Decimal,getcontext
            getcontext().prec=23
            print('RATIO',q,n,Decimal(S)/Decimal(I*I))
    print('VERIFY_OK')
if __name__=='__main__':main()
