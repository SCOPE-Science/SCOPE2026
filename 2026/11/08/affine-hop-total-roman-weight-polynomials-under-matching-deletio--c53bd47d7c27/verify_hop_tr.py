"""Reproduce the hop-total-Roman weight enumerator from the original graph definition.
Only uses the Python standard library. Vertices are 0..a-1 on left,
a..a+b-1 on right. Deleted matching comprises (i,a+i), 0<=i<t.
"""
from itertools import product
from math import comb
from collections import deque

def add(*ps):
    out=[0]*max(map(len,ps))
    for p in ps:
        for i,c in enumerate(p):out[i]+=c
    return out

def mul(p,q):
    ans=[0]*(len(p)+len(q)-1)
    for i,c in enumerate(p):
        for j,d in enumerate(q):ans[i+j]+=c*d
    return ans

def scale(p,c):return [c*x for x in p]
def power(p,n):
    r=[1]
    for _ in range(n):r=mul(r,p)
    return r

def single_polys(s):
    F=add(power([1,1,1],s),scale(power([1,1],s),-1),[0]*s+[1])
    H=add(mul([0,1,1],power([1,1,1],s-1)),scale(mul([0,1],power([1,1],s-1)),-1),[0]*s+[1])
    return F,H

def predicted(a,b,t):
    fa,ha=single_polys(a); fb,hb=single_polys(b)
    loss=add(mul([0,0,1],ha),mul([0,0,1],hb),[0,0,0,0,-1])
    return add(mul(fa,fb),scale(loss,-t))

def checked(a,b,t):
    n=a+b
    adj=[set() for _ in range(n)]
    for i in range(a):
        for j in range(b):
            if i==j and i<t:continue
            adj[i].add(a+j);adj[a+j].add(i)
    dist=[]
    for x in range(n):
        d=[-1]*n;d[x]=0;qu=deque([x])
        while qu:
            u=qu.popleft()
            for v in adj[u]:
                if d[v]<0:d[v]=d[u]+1;qu.append(v)
        assert all(v>=0 for v in d)
        dist.append(d)
    near2=[tuple(j for j in range(n) if dist[i][j]==2) for i in range(n)]
    observed=[0]*(2*n+1);accepted=0
    for labels in product((0,1,2),repeat=n):
        if any(labels[u]==0 and not any(labels[v]==2 for v in near2[u]) for u in range(n)):continue
        if any(labels[u]>0 and not any(labels[v]>0 for v in adj[u]) for u in range(n)):continue
        observed[sum(labels)]+=1;accepted+=1
    assert observed==predicted(a,b,t), (a,b,t,observed,predicted(a,b,t))
    assert observed[4]==a*b-t
    assert not any(observed[:4])
    return accepted

def main():
    profiles=0; labels=0;valid=0
    for a in range(3,6):
        for b in range(a,6):
            for t in range(a+1):
                c=checked(a,b,t)
                profiles+=1;labels+=3**(a+b);valid+=c
                print('CHECKED',a,b,t,c)
    assert profiles==28
    print('VERIFY_OK profiles=%d labels=%d valid=%d independent_shortest_paths=PASS full_integer_polynomials=PASS linear_matching_defect=PASS minimum_placements=PASS'%(profiles,labels,valid))
if __name__=='__main__':main()
