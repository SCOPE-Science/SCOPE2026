#!/usr/bin/env python3
"""Independent finite checks of the rose-board sliding-puzzle component theorem."""
import itertools
import math
from collections import deque


def rose(ms):
    paths=[]; off=1
    for m in ms:
        assert m >= 3
        paths.append([0]+list(range(off,off+m-1))+[0])
        off += m-1
    return off,paths


def move(state,u,v):
    out=list(state)
    out[u],out[v]=out[v],out[u]
    return tuple(out)


def hub_configs(ms,paths):
    dims=[m-1 for m in ms]
    result={}
    for h in itertools.product(*(range(d) for d in dims)):
        state=tuple(range(1+sum(dims)))
        for i,steps in enumerate(h):
            for _ in range(steps):
                for u,v in zip(paths[i],paths[i][1:]):
                    state=move(state,u,v)
        assert state[0]==0
        result[h]=state
    assert len(set(result.values()))==len(result)
    return result


def explicit_core(ms):
    N,paths=rose(ms)
    dims=[m-1 for m in ms]
    hmap=hub_configs(ms,paths)
    label={}; edges=set()
    for h,init in hmap.items():
        label[('hub',h)]=init
        for i,m in enumerate(ms):
            current=init
            last=('hub',h)
            for k,(u,v) in enumerate(zip(paths[i],paths[i][1:]),1):
                current=move(current,u,v)
                if k < m:
                    key=('inner',h,i,k)
                    assert key not in label
                    label[key]=current
                else:
                    target=list(h);target[i]=(target[i]+1)%dims[i]
                    key=('hub',tuple(target))
                    assert current==hmap[tuple(target)]
                edges.add(frozenset((last,key)))
                last=key
    assert len(label)==N*math.prod(dims)
    assert len(set(label.values()))==len(label)
    return label,edges


def adjacency(p,board):
    at=p.index(0)
    for u in board[at]:
        yield move(p,at,u)


def enumerate_fs_component(ms):
    N,paths=rose(ms)
    board=[set() for _ in range(N)]
    for path in paths:
        for u,v in zip(path,path[1:]):
            board[u].add(v);board[v].add(u)
    start=tuple(range(N))
    seen={start};que=deque([start]);edges=set()
    while que:
        p=que.popleft()
        for q in adjacency(p,board):
            edges.add(frozenset((p,q)))
            if q not in seen:seen.add(q);que.append(q)
    label,coreedges=explicit_core(ms)
    assert set(label.values())==seen,(ms,len(seen),len(label))
    mapped={frozenset(label[v] for v in e) for e in coreedges}
    assert mapped==edges
    # With a fixed component size and vertex transitivity of label permutations,
    # every component has this size, hence gives the quotient of N!.
    dims=[m-1 for m in ms];L=math.prod(dims)
    assert len(seen)==N*L and len(edges)==L*sum(ms)
    assert math.factorial(N)%(N*L)==0
    assert len(edges)-len(seen)+1 == 1+(len(ms)-1)*L
    return label,coreedges


def det_bareiss(m):
    n=len(m)
    if n==0:return 1
    a=[list(row) for row in m]
    prev=1; sign=1
    for k in range(n-1):
        if a[k][k]==0:
            j=next((j for j in range(k+1,n) if a[j][k]!=0),None)
            if j is None:return 0
            a[k],a[j]=a[j],a[k];sign=-sign
        pivot=a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                numerator=a[i][j]*pivot-a[i][k]*a[k][j]
                assert numerator%prev==0
                a[i][j]=numerator//prev
        for i in range(k+1,n):a[i][k]=0
        prev=pivot
    return sign*a[n-1][n-1]


def count_trees(vertices,edges,weights=None):
    idx={v:i for i,v in enumerate(vertices)};n=len(vertices)
    a=[[0]*n for _ in range(n)]
    for e in edges:
        u,v=tuple(e);i,j=idx[u],idx[v]
        w=1 if weights is None else weights[e]
        a[i][i]+=w;a[j][j]+=w
        a[i][j]-=w;a[j][i]-=w
    return det_bareiss([row[:-1] for row in a[:-1]])


def weighted_core_tau(ms):
    dims=[m-1 for m in ms]
    L=math.prod(dims)
    hubs=list(itertools.product(*(range(d) for d in dims)))
    Q=math.lcm(*ms)
    # A directed edge from each h in each cyclic coordinate (distinct multiedges)
    # is recorded with a formal index, including the two parallel edges in C_2.
    edges=[]
    for h in hubs:
        for i,d in enumerate(dims):
            target=list(h);target[i]=(target[i]+1)%d
            edges.append((h,tuple(target),Q//ms[i]))
    index={h:i for i,h in enumerate(hubs)}
    mat=[[0]*L for _ in range(L)]
    for a,b,w in edges:
        u=index[a];v=index[b]
        mat[u][u]+=w;mat[v][v]+=w
        mat[u][v]-=w;mat[v][u]-=w
    num=math.prod(m**L for m in ms)*det_bareiss([row[:-1] for row in mat[:-1]])
    denom=Q**(L-1)
    assert num%denom==0
    return num//denom


def run():
    for ms in [(3,3),(3,4),(4,3),(4,4),(3,3,3)]:
        label,edges=enumerate_fs_component(ms)
        N=1+sum(m-1 for m in ms);L=math.prod(m-1 for m in ms)
        ts=count_trees(list(label),edges)
        tw=weighted_core_tau(ms)
        assert ts==tw,(ms,ts,tw)
        print('EXACT_COMPONENT_AND_MATRIX_TREE_PASS',ms,'components',math.factorial(N)//(N*L),'vertices',len(label),'edges',len(edges),'trees',ts)
    print('VERIFY_OK')

if __name__=='__main__':run()
