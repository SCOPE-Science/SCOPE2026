#!/usr/bin/env python3
"""Independent exhaustive subspace/ideal enumerator for short quiver algebras."""
import itertools, collections, math

def gaussian(n,k,q):
    if k<0 or k>n:return 0
    v=1
    for i in range(k):v=v*(q**(n-i)-1)//1
    d=1
    for i in range(k):d*=q**(k-i)-1
    return v//d

def predicted(vertices,arrows,q):
    a=collections.Counter(arrows)
    out=collections.Counter()
    for n in range(len(vertices)+1):
        for subset in itertools.combinations(vertices,n):
            ranks={0:1}
            for s in subset:
                for t in subset:
                    m=a[s,t]
                    if not m:continue
                    nxt=collections.Counter()
                    for prev,w in ranks.items():
                        for d in range(m+1):nxt[prev+d]+=w*gaussian(m,d,q)
                    ranks=nxt
            for d,w in ranks.items():out[n+d]+=w
    return out

def rref_subspaces(dim,q):
    for r in range(dim+1):
        for pivots in itertools.combinations(range(dim),r):
            free=[(row,j) for row,p in enumerate(pivots) for j in range(p+1,dim) if j not in pivots]
            for vals in itertools.product(range(q),repeat=len(free)):
                B=[[0]*dim for _ in range(r)]
                for row,p in enumerate(pivots): B[row][p]=1
                for (i,j),v in zip(free,vals):B[i][j]=v
                yield tuple(tuple(row) for row in B),pivots

def reduce(v,B,piv,q):
    v=list(v)
    for row,p in zip(B,piv):
        a=v[p]
        if a:
            for j in range(len(v)):v[j]=(v[j]-a*row[j])%q
    return not any(v)

def brute(vertices,arrows,q):
    n=len(vertices); dim=n+len(arrows); vi={v:i for i,v in enumerate(vertices)}
    # b*c for vertex/arrow basis indices, nonzero output index or None
    mm={}
    for x in range(dim):
        for y in range(dim):
            if x<n and y<n:
                if x==y: mm[x,y]=x
            elif x<n and y>=n:
                s,t=arrows[y-n]
                if x==vi[s]:mm[x,y]=y
            elif x>=n and y<n:
                s,t=arrows[x-n]
                if y==vi[t]:mm[x,y]=x
    # multiplying any basis algebra element on right and left of ideal basis vector
    out=collections.Counter()
    for B,piv in rref_subspaces(dim,q):
        okay=True
        for x in range(dim):
            if not okay:break
            for row in B:
                for side in [0,1]:
                    v=[0]*dim
                    for i,coeff in enumerate(row):
                        if coeff:
                            k=mm.get((x,i) if side==0 else (i,x))
                            if k is not None:v[k]=(v[k]+coeff)%q
                    if not reduce(v,B,piv,q):okay=False;break
                if not okay:break
        if okay:out[dim-len(B)]+=1
    return out

def main():
    cases=[
      ([0],[],2),([0],[(0,0)],2),([0],[(0,0),(0,0)],2),
      ([0],[(0,0),(0,0)],3),([0,1],[(0,1)],2),([0,1],[(0,1),(0,1)],2),
      ([0,1],[(0,1),(1,0)],2),([0,1],[(0,0),(0,1)],2),
      ([0,1],[(0,0),(1,1)],2),([0,1,2],[(0,1),(1,2)],2),
      ([0,1,2],[(0,1),(1,2),(2,0)],2),([0,1],[(0,1)],3),
      ([0,1,2],[(0,1),(0,1),(1,2)],2),
    ]
    for vs,arr,q in cases:
        pred=predicted(vs,arr,q)
        actual=brute(vs,arr,q)
        assert actual==pred, (vs,arr,q,actual,pred)
        print('PASS',q,vs,arr,dict(sorted(actual.items())))
    print('VERIFY_OK cases=',len(cases))
if __name__=='__main__':main()
