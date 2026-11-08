#!/usr/bin/env python3
"""Reproducible tests of a signed-matching criterion for finite tournaments.
Only the Python standard library is required. No external data are used.
"""
from collections import defaultdict, Counter
from itertools import permutations, product

PERMS = tuple(permutations(range(3)))
OPTIONS = ((0, None), (3, None)) + tuple((k, p) for k in (1, 2) for p in PERMS)

def empty(n):
    return [[False] * n for _ in range(n)]

def orient(a, u, v):
    assert u != v and not a[u][v] and not a[v][u]
    a[u][v] = True

def triangle_family(choices):
    m = 3
    n = 3*m
    a = empty(n)
    for g in range(m):
        for i in range(3):
            orient(a, 3*g+i, 3*g+(i+1)%3)
    for (g,h), (k, p) in zip(((0,1),(1,2),(0,2)), choices):
        for i in range(3):
            for j in range(3):
                u, v = 3*g+i, 3*h+j
                if k == 3 or (k == 1 and p[i] == j) or (k == 2 and p[i] != j):
                    orient(a,u,v)
                else:
                    orient(a,v,u)
    assert all((a[i][j] != a[j][i]) for i in range(n) for j in range(i+1,n))
    return a

def stable_classes(a):
    n=len(a); colors=[0]*n
    for t in range(n+1):
        sig=[]
        for i in range(n):
            out=Counter(colors[j] for j in range(n) if a[i][j])
            inc=Counter(colors[j] for j in range(n) if a[j][i])
            sig.append((colors[i], tuple(sorted(out.items())),tuple(sorted(inc.items()))))
        lookup={v:k for k,v in enumerate(sorted(set(sig)))}
        new=[lookup[s] for s in sig]
        old_blocks={frozenset(i for i in range(n) if colors[i]==c) for c in colors}
        new_blocks={frozenset(i for i in range(n) if new[i]==c) for c in new}
        if new_blocks==old_blocks:
            return tuple(sorted((tuple(sorted(b)) for b in new_blocks)))
        colors=new
    raise AssertionError('refinement unexpectedly exceeded n rounds')

def parity(p):
    return (-1)**sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))

def cycle_order(a, block):
    x=min(block)
    assert len(block)==3
    y=next(j for j in block if a[x][j])
    z=next(j for j in block if j not in (x,y))
    assert a[y][z] and a[z][x]
    return (x,y,z)

def signed_prediction(a, blocks):
    assert all(len(b) in (1,3) for b in blocks)
    triples=[cycle_order(a,b) for b in blocks if len(b)==3]
    r=len(triples); adj=[[] for _ in range(r)]
    for i in range(r):
        for j in range(i+1,r):
            A,B=triples[i],triples[j]
            rows=[sum(a[x][y] for y in B) for x in A]
            cols=[sum(a[x][y] for x in A) for y in B]
            assert len(set(rows))==len(set(cols))==1 and rows[0]==cols[0]
            k=rows[0]
            if k in (0,3):continue
            assert k in (1,2)
            p=tuple(next(t for t in range(3) if a[x][B[t]]==(k==1)) for x in A)
            assert sorted(p)==[0,1,2]
            sign=parity(p)
            adj[i].append((j,sign));adj[j].append((i,sign))
    sign_state={}; unbalanced=set(); parts=[]; balanced_components=0
    for start in range(r):
        if start in sign_state:continue
        stack=[start];sign_state[start]=1;component=[];bad=False
        while stack:
            v=stack.pop();component.append(v)
            for w,s in adj[v]:
                if w not in sign_state:
                    sign_state[w]=s*sign_state[v];stack.append(w)
                elif sign_state[w]!=s*sign_state[v]:bad=True
        if bad:unbalanced.update(component)
        else:balanced_components+=1
    for i,trip in enumerate(triples):
        if i in unbalanced:parts.extend(frozenset([x]) for x in trip)
        else:parts.append(frozenset(trip))
    parts.extend(frozenset(b) for b in blocks if len(b)==1)
    return frozenset(parts),len(unbalanced),len(triples),balanced_components,3**balanced_components

def automorphism_partition(a,blocks):
    n=len(a)
    triples=[cycle_order(a,b) for b in blocks if len(b)==3]
    fixed=[b[0] for b in blocks if len(b)==1]
    parent=list(range(n));good=0
    def root(i):
        while parent[i]!=i:
            parent[i]=parent[parent[i]]
            i=parent[i]
        return i
    for choices in product(range(3),repeat=len(triples)):
        perm=list(range(n))
        for tri,shift in zip(triples,choices):
            for k,u in enumerate(tri):perm[u]=tri[(k+shift)%3]
        assert all(perm[x]==x for x in fixed)
        if all(a[i][j]==a[perm[i]][perm[j]] for i in range(n) for j in range(i+1,n)):
            good+=1
            for u in range(n):parent[root(u)]=root(perm[u])
    assert good>=1
    groups=defaultdict(set)
    for x in range(n):groups[root(x)].add(x)
    return frozenset(frozenset(g) for g in groups.values()),good

def add_dominating_triangle(a):
    a=[row[:] + [False]*3 for row in a]
    old=len(a)
    for i in range(3):
        a.append([True]*old+[False]*3)
    for i in range(3):
        orient(a,old+i,old+(i+1)%3)
    return a

def extend_dominators(a,count):
    a=[row[:] for row in a]
    for t in range(count):
        n=len(a)
        for row in a:row.append(False)
        a.append([True]*n+[False])
    return a

def matrix_code(a):
    return ''.join('1' if a[i][j] else '0' for i in range(len(a)) for j in range(i+1,len(a)))

def test():
    num=0;eligible=0;unbalanced=0;balanced=0
    for choices in product(OPTIONS,repeat=3):
        a=triangle_family(choices);num+=1
        blocks=stable_classes(a)
        if not all(len(b)<=3 for b in blocks):continue
        eligible+=1
        expected,bad,r,balanced_count,expected_aut=signed_prediction(a,blocks)
        actual,aut=automorphism_partition(a,blocks)
        assert expected==actual and aut==expected_aut,(choices,blocks,expected,actual,aut,expected_aut)
        if bad:unbalanced+=1
        else:balanced+=1
    print('FAMILY_CHECK',num,'eligible',eligible,'balanced',balanced,'unbalanced',unbalanced)
    witness=triangle_family(((1,(0,1,2)),(1,(0,1,2)),(1,(1,0,2))))
    block=stable_classes(witness)
    assert tuple(sorted(map(len,block)))==(3,3,3)
    assert tuple(sorted(set(sum(row) for row in witness)))==(3,4,5)
    predicted,bad,r,bc,oa=signed_prediction(witness,block)
    actual,aut=automorphism_partition(witness,block)
    assert bad==3 and aut==1 and predicted==actual and len(actual)==9
    print('WITNESS_9',matrix_code(witness),'stable_sizes',(3,3,3),'orbits',(1,)*9,'automorphisms',aut)
    mixed=add_dominating_triangle(witness)
    mixed_blocks=stable_classes(mixed)
    mixed_pred,unbal,r,b,group=signed_prediction(mixed,mixed_blocks)
    mixed_orbit,mixed_aut=automorphism_partition(mixed,mixed_blocks)
    assert sorted(map(len,mixed_blocks))==[3]*4
    assert mixed_pred==mixed_orbit and (unbal,r,b,group,mixed_aut)==(3,4,1,3,3)
    print('MIXED_COMPONENTS_12', 'unbalanced_triples',unbal,'balanced_components',b,'automorphisms',mixed_aut)
    for extra in range(1,5):
        a=extend_dominators(witness,extra)
        blocks=stable_classes(a)
        assert sorted(map(len,blocks))==[1]*extra+[3]*3
        prediction,_,_,_,oa=signed_prediction(a,blocks)
        orbits,numaut=automorphism_partition(a,blocks)
        assert prediction==orbits and numaut==oa==1
        print('WITNESS_EXTENDED',len(a),'aut',numaut)
    print('VERIFY_OK')
if __name__=='__main__':test()
