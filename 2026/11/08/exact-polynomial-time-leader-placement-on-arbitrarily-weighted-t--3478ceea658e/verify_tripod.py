"""Exact-arithmetic verifier for polynomial tripod leader placement.
The direct checker compares the dynamic program with exhaustive grounded-Laplacian inverses.
Python standard library only.
"""
from fractions import Fraction as F
from itertools import product, combinations
from math import prod


def inv_trace(matrix):
    n=len(matrix)
    if n==0:return F(0)
    a=[[F(v) for v in row]+[F(i==j) for j in range(n)] for i,row in enumerate(matrix)]
    for i in range(n):
        pivot=next((j for j in range(i,n) if a[j][i]),None)
        assert pivot is not None
        a[i],a[pivot]=a[pivot],a[i]
        z=a[i][i];a[i]=[v/z for v in a[i]]
        for j in range(n):
            if j!=i:
                z=a[j][i]
                if z:a[j]=[x-z*y for x,y in zip(a[j],a[i])]
    return sum(a[i][n+i] for i in range(n))


def brute(arms,k):
    edges=[];ids=[];v=1
    for ar in arms:
        prev=0;arr=[]
        for w in ar:
            edges.append((prev,v,F(w)));arr.append(v);prev=v;v+=1
        ids.append(arr)
    L=[[F(0) for _ in range(v)] for _ in range(v)]
    for i,j,w in edges:
        L[i][i]+=w;L[j][j]+=w;L[i][j]-=w;L[j][i]-=w
    best=None;sets=[]
    for S in combinations(range(v),k):
        followers=[i for i in range(v) if i not in S]
        cost=inv_trace([[L[i][j] for j in followers] for i in followers])
        if best is None or cost<best:best=cost;sets=[S]
        elif cost==best:sets.append(S)
    return best,sets


def solver(arms,k):
    assert len(arms)==3 and all(arms) and all(w>0 for arm in arms for w in arm)
    pref=[];table=[]
    for arm in arms:
        r=[F(0)]
        for w in arm:r.append(r[-1]+F(1)/F(w))
        pref.append(r)
        L=len(arm)
        def between(a,b):
            d=r[b]-r[a]
            return sum((r[z]-r[a])*(r[b]-r[z])/d for z in range(a+1,b))
        def after(a):return sum(r[z]-r[a] for z in range(a+1,L+1))
        gaps={(a,b):between(a,b) for a in range(L+1) for b in range(a+1,L+1)}
        costs={}
        for first in range(L+1):
            states={first:F(0)}
            values=[after(first)]
            for s in range(1,L-first+1):
                nxt={}
                for last,c in states.items():
                    for j in range(last+1,L+1):
                        val=c+gaps[last,j]
                        if j not in nxt or val<nxt[j]:nxt[j]=val
                states=nxt
                values.append(min(val+after(last) for last,val in states.items()))
            costs[first]=values
        table.append(costs)

    def budget(t, num):
        # t entries are None if arm has no first leader and center is follower,
        # else fixed leader position at 0 or later.
        dp={0:F(0)}
        for i in range(3):
            vals=([F(0)] if t[i] is None else table[i][t[i]])
            nd={}
            for a,old in dp.items():
                for s,v in enumerate(vals):
                    if a+s<=num:
                        z=old+v
                        if a+s not in nd or z<nd[a+s]:nd[a+s]=z
            dp=nd
        return dp.get(num)

    best=None;type_witness=None
    if k>=1:
        c=budget([0,0,0],k-1)
        if c is not None: best=c;type_witness=('center',)
    for t in product(*[([None]+list(range(1,len(ar)+1))) for ar in arms]):
        anchored=[i for i in range(3) if t[i] is not None]
        r=len(anchored)
        if r==0 or r>k:continue
        g=sum(1/pref[i][t[i]] for i in anchored)
        h=1/g
        for i,ar in enumerate(arms):
            R=pref[i]
            if t[i] is None:
                h+=sum(R[j]+1/g for j in range(1,len(ar)+1))
            else:
                other=g-1/R[t[i]]
                if other==0:h+=sum(R[t[i]]-R[j] for j in range(1,t[i]))
                else:
                    rr=1/other
                    h+=sum((R[t[i]]-R[j])*(R[j]+rr)/(R[t[i]]+rr) for j in range(1,t[i]))
        rest=budget(t,k-r)
        if rest is not None and (best is None or h+rest<best):
            best=h+rest;type_witness=('center-follower',t)
    return best,type_witness


def run():
    tests=0;types=set()
    # Exhaustive all positive weight-1 or weight-2 tripods up to six noncentral vertices.
    for lengths in product((1,2,3),repeat=3):
        if sum(lengths)>6:continue
        for weights in product((1,2),repeat=sum(lengths)):
            off=0;arms=[]
            for n in lengths:
                arms.append(weights[off:off+n]);off+=n
            for k in range(1,2+sum(lengths)):
                got,wit=solver(arms,k)
                expected,_=brute(arms,k)
                assert got==expected,(arms,k,got,expected,wit)
                types.add(wit[0]);tests+=1
    print('EXACT_TRIPOD_MATCH',tests,'cases; root modes',sorted(types))
    # Nontrivial tripods beyond all-equal edges.
    for arms in (((2,1,4,3),(3,1),(2,)),((1,3),(2,5),(3,4,1)),((1,),(2,2,3),(4,)),((3,2),(4,1),(5,2))):
        for k in range(1,min(4,1+sum(map(len,arms)))+1):
            got,wit=solver(arms,k); exp,_=brute(arms,k)
            assert got==exp,(arms,k,got,exp)
            tests+=1
    c1,s1=brute(((1,),(1,),(1,1,1,1)),1)
    c2,s2=brute(((1,),(1,),(1,1,1,1)),2)
    assert c1==F(11) and s1==[(3,)] and c2==F(13,3) and s2==[(0,5)]
    assert solver(((F(3,2),F(5,4)),(F(2),),(F(4),)),2)[0]==brute(((F(3,2),F(5,4)),(F(2),),(F(4),)),2)[0]
    tests+=1
    print('NON_NESTED_WITNESS',str(c1),str(c2),s1,s2)
    print('VERIFICATION_OK',tests,'total exact comparisons')

if __name__=='__main__':run()
