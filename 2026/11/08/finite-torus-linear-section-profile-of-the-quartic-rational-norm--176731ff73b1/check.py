"""Finite-field witnesses and an exhaustive GF(5) support-rank check.

For prime p>=5, the six functions are 1,x,x^2,x^3,y,xy.
The general all-prime-power theorem rests on a separate algebraic proof.
"""
from itertools import combinations
from math import comb


def rank_mod(rows,p):
    a=[[int(v)%p for v in row] for row in rows]
    if not a:return 0
    n=len(a[0]); rr=0
    for c in range(n):
        piv=next((i for i in range(rr,len(a)) if a[i][c]),None)
        if piv is None:continue
        a[rr],a[piv]=a[piv],a[rr]
        v=pow(a[rr][c],-1,p)
        for j in range(c,n):a[rr][j]=a[rr][j]*v%p
        for i in range(rr+1,len(a)):
            h=a[i][c]
            if h:
                for j in range(c,n):a[i][j]=(a[i][j]-h*a[rr][j])%p
        rr+=1
        if rr==n:break
    return rr


def check(p):
    t=p-1
    pts=[(x,y) for x in range(1,p) for y in range(1,p)]
    coords=lambda x,y:(1,x,x*x%p,pow(x,3,p),y,x*y%p)
    rows=[coords(x,y) for x,y in pts]
    assert rank_mod(rows,p)==6
    r,s,b=1,2,2
    W={
      1:[lambda x,y:(x-1)*(x-2)*(x-3)],
      2:[lambda x,y:(x-1)*(x-2),lambda x,y:x*(x-1)*(x-2)],
      3:[lambda x,y:(x-r)*(x-s),lambda x,y:(x-r)*(x-s)**2,lambda x,y:(x-r)*(y-b)],
      4:[lambda x,y:x-r,lambda x,y:(x-r)*x,lambda x,y:(x-r)*x*x,lambda x,y:(x-r)*y],
      5:[lambda x,y,idx=i:coords(x,y)[idx]-coords(r,b)[idx] for i in range(1,6)],
      6:[lambda x,y,idx=i:coords(x,y)[idx] for i in range(6)]
    }
    max_common=[3*t,2*t,t+1,t,1,0]
    for dim,functions in W.items():
        values=[[f(x,y)%p for x,y in pts] for f in functions]
        assert rank_mod(values,p)==dim,(p,dim,'dependent witness')
        common=sum(all(v[i]==0 for v in values) for i in range(len(pts)))
        assert common==max_common[dim-1],(p,dim,common)
    print('prime',p,'n',t*t,'witness shared-zero maxima',max_common)
    if p==5:
        # Any support improvement would imply a subset of k points with
        # evaluation rank <=6-r. We check every such subset of the torus.
        thresholds={1:13,2:9,3:6,4:5,5:2}
        for dim,k in thresholds.items():
            for inds in combinations(range(len(pts)),k):
                if rank_mod([rows[i] for i in inds],p)<=6-dim:
                    raise AssertionError(('excessive torus intersection',dim,inds))
            print('GF(5) r=',dim,'all',comb(16,k),'sets of',k,'points excluded')

for p in (5,7,11):check(p)
print('ALL_CHECKS_PASSED')
