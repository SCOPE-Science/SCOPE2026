"""Independent finite orbit-union and quotient-forest checks for regular free actions.
Run with Python 3 standard library; no network or external files.
"""
from itertools import permutations
from itertools import combinations
from math import factorial


def group_cyclic(n):
    return list(range(n)),lambda a,b:(a+b)%n,0

def group_v4():
    return list(range(4)),lambda a,b:a^b,0

def group_s3():
    el=list(permutations(range(3))); unit=(0,1,2)
    return el,lambda a,b:tuple(a[b[i]] for i in range(3)),unit

def acyclic(edges, size):
    parent=list(range(size)); rank=[0]*size
    def root(x):
        while parent[x]!=x:
            parent[x]=parent[parent[x]]; x=parent[x]
        return x
    for a,b in edges:
        a=root(a);b=root(b)
        if a==b:return False
        if rank[a]<rank[b]:a,b=b,a
        parent[b]=a
        if rank[a]==rank[b]:rank[a]+=1
    return True

def check_case(label,group,m,limit=None):
    elements,mul,e=group
    k=len(elements);ix={h:i for i,h in enumerate(elements)}
    verts=[(i,h) for i in range(m) for h in elements]
    vi={v:j for j,v in enumerate(verts)}
    edges=list(combinations(range(m*k),2))
    seen=set(); orbit=[]
    for edge in edges:
        if edge in seen:continue
        one=set()
        for h in elements:
            a,b=(verts[edge[0]],verts[edge[1]])
            na=vi[(a[0],mul(h,a[1]))];nb=vi[(b[0],mul(h,b[1]))]
            one.add(tuple(sorted((na,nb))))
        seen|=one
        orbit.append(sorted(one))
    assert seen==set(edges)
    eligible=[o for o in orbit if acyclic(o,len(verts))]
    inv=sum(1 for x in elements if x!=e and mul(x,x)==e)
    expect=inv*m+k*m*(m-1)//2
    assert len(eligible)==expect,(label,m,len(eligible),expect)
    base_edges=[]
    for o in eligible:
        a,b=o[0];i=verts[a][0];j=verts[b][0]
        if i==j:base_edges.append((i,m))
        else:base_edges.append((i,j))
    assert sum(1 for a,b in base_edges if b==m)==inv*m
    assert len(base_edges)<=22, (label,m,len(base_edges))
    cases=1<<len(base_edges)
    assert limit is None or cases<=limit
    for mask in range(cases):
        orbit_edges=[];small=[]
        for j,o in enumerate(eligible):
            if (mask>>j)&1:
                orbit_edges.extend(o)
                small.append(base_edges[j])
        is_forest=acyclic(orbit_edges,len(verts))
        quotient_forest=acyclic(small,m+1)
        assert is_forest==quotient_forest,(label,m,mask,orbit_edges,small)
    print('CASE',label,'m',m,'order',k,'involutions',inv,
          'edge_orbits',len(orbit),'admissible',len(eligible),'subsets',cases,'PASS')
    return len(eligible),cases

def tree_count(t):
    return 1 if t==1 else t**(t-2)

def weighted_forest_sum(m,k,s):
    # count forests by partitions: each base component has a chosen tree and
    # optionally one marked apex edge, with k parallel cross-edge choices.
    total=0
    def partitions(arr):
        if not arr:
            yield []
        else:
            v=arr[0]
            for p in partitions(arr[1:]):
                yield [[v]]+[part[:] for part in p]
                for i in range(len(p)):
                    new=[part[:] for part in p]
                    new[i]=[v]+new[i]
                    yield new
    for p in partitions(list(range(m))):
        val=1
        for part in p:
            t=len(part)
            val*=tree_count(t)*(-k)**(t-1)*(1-s*t)
        total+=val
    rank=(m if s else m-1)
    return (-1)**rank*total

def direct_beta_multigraph(m,k,s):
    # Enumerate simple forests with multiplicity of each graph edge.
    edge_types=[(i,j,k) for i in range(m) for j in range(i+1,m)]
    edge_types += [(i,m,s) for i in range(m)]
    total=0
    for mask in range(1<<len(edge_types)):
        E=[];weight=1
        for j,(u,v,c) in enumerate(edge_types):
            if (mask>>j)&1:E.append((u,v));weight*=c
        if acyclic(E,m+1):total+=(-1)**len(E)*weight
    return (-1)**(m if s else m-1)*total

if __name__=='__main__':
    total=0
    for label,g,ms in [('C2',group_cyclic(2),[1,2,3,4]),
                       ('C3',group_cyclic(3),[1,2,3]),
                       ('C4',group_cyclic(4),[1,2,3]),
                       ('V4',group_v4(),[1,2]),
                       ('S3',group_s3(),[1,2])]:
        for m in ms:
            admissible,cases=check_case(label,g,m,limit=2**21)
            total+=cases
            invol=sum(x!=g[2] and g[1](x,x)==g[2] for x in g[0])
            beta=weighted_forest_sum(m,len(g[0]),invol)
            assert beta==direct_beta_multigraph(m,len(g[0]),invol)
            assert beta>=0
            print('BETTI',label,m,'sphere_dimension',m-1 if invol else m-2,'rank',beta)
    for m in range(1,8):
        for k,s in [(2,1),(3,0),(4,1),(4,3),(6,3)]:
            a=weighted_forest_sum(m,k,s)
            assert a>=0
            if m<=4:assert a==direct_beta_multigraph(m,k,s)
    print('TOTAL_CHECKED_ORBIT_SUBSETS',total)
    print('FREE_GROUP_FOREST_CONE_EQUIVALENCE_PASS')
