"""Exact rational checks for RK2 Markov-generator positivity and edge thresholds.

Standard-library-only supplemental calculations. Infinite cases require the proof.
"""
from fractions import Fraction as F
from itertools import product
from random import Random

def mm(a,b):
    n=len(a)
    return [[sum((a[i][k]*b[k][j] for k in range(n)),F(0)) for j in range(n)] for i in range(n)]

def generator(a):
    n=len(a)
    return [[-sum(a[i]) if i==j else a[i][j] for j in range(n)] for i in range(n)]

def step(q,h):
    n=len(q); q2=mm(q,q)
    return [[int(i==j)+h*q[i][j]+h*h*q2[i][j]/2 for j in range(n)] for i in range(n)]

def limit(a):
    n=len(a); lam=[sum(row) for row in a]
    out=[]
    for i in range(n):
        for j in range(n):
            if i==j or not a[i][j]: continue
            s=sum((a[i][k]*a[k][j] for k in range(n) if k!=i and k!=j),F(0))
            delta=(lam[i]+lam[j])*a[i][j]-s
            if delta>0:out.append((2*a[i][j]/delta,i,j))
    if not out:return None
    return min(out)[0]

def allpos(p):return all(x>=0 for row in p for x in row)

checks=0
for n in (2,3,4):
    # zero, directed and heterogeneous rational edges
    arrays=([rng.randrange(3) for _ in range(n*(n-1))] for rng in [Random(1500+j) for j in range(1000)]) if n==4 else product((0,1,2),repeat=n*(n-1))
    # sample enough while keeping replay bounded
    from itertools import islice
    for seq in islice(arrays,0,1000 if n==4 else 2000):
        a=[[F(0) for _ in range(n)] for _ in range(n)]; it=iter(seq)
        for i in range(n):
            for j in range(n):
                if i!=j:a[i][j]=F(next(it))
        q=generator(a)
        for row in q:
            assert sum(row)==0; checks+=1
        M=max(sum(row) for row in a)
        hstar=limit(a)
        assert (hstar is None)==(M==0);checks+=1
        if M==0:continue
        assert F(1,M)<=hstar<=F(2,M);checks+=1
        eq=any(a[i][j] and sum(a[i])==M and sum(a[j])==M and not any(a[i][k]*a[k][j] for k in range(n) if k not in (i,j)) for i in range(n) for j in range(n) if i!=j)
        assert (hstar==F(1,M))==eq;checks+=1
        for h,expect in [(F(0),True),(F(1,M),True),(hstar,True),(hstar+F(1,100),False)]:
            p=step(q,h)
            assert allpos(p)==expect,(n,seq,h,hstar)
            assert all(sum(row)==1 for row in p)
            assert all(p[i][i]>=F(1,2) for i in range(n))
            # polynomial equals 1/2(I+(I+hQ)^2)
            e=[[int(i==j)+h*q[i][j] for j in range(n)] for i in range(n)]
            e2=mm(e,e)
            assert p==[[(int(i==j)+e2[i][j])/2 for j in range(n)] for i in range(n)]
            checks+=4
# sharp examples
for m in range(2,51):
 n=m+1; a=[[F(0) for _ in range(n)] for _ in range(n)]
 for j in range(1,n): a[0][j]=a[j][0]=F(1)
 assert limit(a)==F(2,m+1)
 checks+=1
print('VERIFY_OK exact_assertion_groups=',checks)
