#!/usr/bin/env python3
"""Independent finite checks for the last nontrivial Rips scale of equal-arm theta graphs.

Standard Python library only. No external files or network access.
"""
from collections import deque
from math import comb

def graph(m, ell):
    assert m >= 2 and ell >= 2
    n = 2 + m*(ell-1)
    adj = [set() for _ in range(n)]
    for i in range(m):
        path = [0] + [2+i*(ell-1)+j for j in range(ell-1)] + [1]
        for u,v in zip(path,path[1:]):
            adj[u].add(v); adj[v].add(u)
    return adj

def distances(adj):
    out=[]
    for root in range(len(adj)):
        d=[None]*len(adj); d[root]=0; todo=deque([root])
        while todo:
            u=todo.popleft()
            for v in adj[u]:
                if d[v] is None:
                    d[v]=d[u]+1;todo.append(v)
        assert all(x is not None for x in d)
        out.append(d)
    return out

def groups(m, ell):
    blocks=[(0,1)]
    for a in range(1,ell//2+1):
        b=ell-a
        if a<b:
            blocks.append(([2+i*(ell-1)+a-1 for i in range(m)],
                           [2+i*(ell-1)+b-1 for i in range(m)]))
        elif a==b:
            blocks.append(tuple(2+i*(ell-1)+a-1 for i in range(m)))
    return blocks

def predicted_far_pairs(m,ell):
    out={frozenset((0,1))}
    for a in range(1,ell//2+1):
        b=ell-a
        if a<b:
            for i in range(m):
                for j in range(m):
                    if i!=j:
                        out.add(frozenset((2+i*(ell-1)+a-1,
                                           2+j*(ell-1)+b-1)))
        else:
            for i in range(m):
                for j in range(i+1,m):
                    out.add(frozenset((2+i*(ell-1)+a-1,
                                       2+j*(ell-1)+a-1)))
    return out

def full_face_count(m,ell):
    # Independent-set enumerator of the distance-ell graph,
    # whose connected components are K2, crown graphs, and maybe Km.
    # Evaluate at t=1; each pair of complementary arm levels contributes
    # 2^(m+1)-1 + m independent sets.
    k=ell//2
    crowns=k if ell%2 else k-1
    return 3*(2**(m+1)-1+m)**crowns * ((m+1) if ell%2==0 else 1)

def exact_face_count(adj, ell):
    n=len(adj)
    d=distances(adj)
    # Enumerate faces by independent-set dynamic programming on incompatibilities.
    bad=[sum(1<<j for j in range(n) if d[i][j]==ell) for i in range(n)]
    def recur(mask):
        if not mask:return 1
        x=mask&-mask
        v=x.bit_length()-1
        other=mask^x
        return recur(other)+recur(other & ~bad[v])
    return recur((1<<n)-1)

def main():
    total=0; checked=0
    for m in range(2,6):
      for ell in range(2,10):
        adj=graph(m,ell);d=distances(adj)
        n=len(adj)
        far={frozenset((i,j)) for i in range(n) for j in range(i+1,n) if d[i][j]>ell-1}
        assert max(max(row) for row in d)==ell,(m,ell)
        assert far==predicted_far_pairs(m,ell),(m,ell,'far pairs')
        blocks=groups(m,ell)
        assert len({x for z in blocks for part in z for x in (part if isinstance(part,list) else [part])})==n,(m,ell)
        # The far-distance graph has no edges between distinct canonical blocks.
        block_sets=[set([z[0],z[1]]) if isinstance(z[0],int) and len(z)==2 else
                    set(z[0])|set(z[1]) if len(z)==2 else set(z) for z in blocks]
        assert all(any(pair<=s for s in block_sets) for pair in far)
        k=ell//2
        expected=(-1)**(ell-1)*(m-1)**k
        Fm1=(-1)*(m-1)**(k if ell%2 else k-1)* (-(m-1) if ell%2==0 else 1)
        assert -Fm1==expected
        if n<=23:
            got=exact_face_count(adj,ell)
            assert got==full_face_count(m,ell),(m,ell,got,full_face_count(m,ell))
            checked+=1;total+=got
    print('ALL_CHECKS_PASS', 'distance_cases=32','full_face_counts_checked=',checked,
          'total_faces_in_checked_examples=',total,
          'sample_m3_L5_faces=',full_face_count(3,5),
          'sample_m4_L5_faces=',full_face_count(4,5))

if __name__=='__main__':main()

# Second, orientation-sensitive finite cross-check by signed chain traces.
def vertex_map(m,ell,arm_perm,pole_swap):
    f=list(range(2+m*(ell-1)))
    f[0]=1 if pole_swap else 0
    f[1]=0 if pole_swap else 1
    for i in range(m):
        for a in range(1,ell):
            f[2+i*(ell-1)+a-1]=2+arm_perm[i]*(ell-1)+(ell-a if pole_swap else a)-1
    assert sorted(f)==list(range(len(f)))
    return f

def chain_reduced_lefschetz(m,ell,g):
    n=len(g); seen=set();orbits=[]
    for v in range(n):
        if v not in seen:
            o=[];w=v
            while w not in seen:
                seen.add(w);o.append(w);w=g[w]
            assert w==v
            orbits.append(o)
    far=predicted_far_pairs(m,ell)
    eligible=[]
    for orbit in orbits:
        if any(frozenset((x,y)) in far for x in orbit for y in orbit if x<y):continue
        eligible.append(orbit)
    if len(eligible)>24:raise ValueError('too many orbit blocks')
    total=0
    for mask in range(1<<len(eligible)):
        selected=[v for i,O in enumerate(eligible) if mask>>i&1 for v in O]
        s=set(selected)
        if any(pair<=s for pair in far):continue
        total+=(-1)**mask.bit_count()
    return -total

def test_symmetry():
    cases=0
    for m in range(2,5):
      perms=[list(range(m))]
      t=list(range(m));t[0],t[1]=t[1],t[0];perms.append(t)
      if m>=3:perms.append(list(range(1,m))+[0])
      for ell in range(2,8):
        if 2+m*(ell-1)>23:continue
        k=ell//2
        for p in perms:
          f=sum(int(p[i]==i) for i in range(m))
          for swap in (False,True):
            g=vertex_map(m,ell,p,swap)
            actual=chain_reduced_lefschetz(m,ell,g)
            sign=(-1)**(k if ell%2==0 else k+1)
            trace=(f-1)**k * (sign if swap else 1)
            predicted=(-1)**(ell-1)*trace
            assert actual==predicted,(m,ell,p,swap,actual,predicted)
            cases+=1
    print('SIGNED_LEFSCHETZ_CHECKS_PASS',cases)

if __name__=='__main__':test_symmetry()
