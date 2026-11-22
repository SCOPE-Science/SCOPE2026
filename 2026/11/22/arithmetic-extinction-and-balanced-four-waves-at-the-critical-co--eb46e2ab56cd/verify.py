"""Exact checks for a critical-contact graph excitable-media theorem.
Python 3 standard library only; the characteristic-polynomial check is exact integer arithmetic.
"""
from itertools import combinations, product
from collections import deque
from math import comb


def graph_odd(m):
    vertices = list(combinations(range(2*m-1), m-1))
    adj = [set() for _ in vertices]
    sets=[set(s) for s in vertices]
    for i in range(len(vertices)):
        for j in range(i+1, len(vertices)):
            if sets[i].isdisjoint(sets[j]):
                adj[i].add(j); adj[j].add(i)
    return vertices, adj


def gh_step(s, adj, threshold):
    return tuple(2 if s[v]==1 else 0 if s[v]==2 else
        1 if sum(s[u]==1 for u in adj[v])>=threshold else 0 for v in range(len(s)))


def check_o4():
    vertices, adj=graph_odd(4)
    assert len(vertices)==35 and all(len(x)==4 for x in adj)
    seen={0}; todo=deque([0]);
    while todo:
        v=todo.popleft()
        for w in adj[v]:
            if w not in seen:seen.add(w);todo.append(w)
    assert len(seen)==35
    assert all(not(adj[u] & adj[v]) for u in range(35) for v in adj[u])
    # Explicit odd cycle on a cyclic ground set (7 vertices)
    ix={s:i for i,s in enumerate(vertices)}
    cyc=[ix[tuple(sorted(((i+2*j)%7 for j in range(3))))] for i in range(7)]
    assert len(set(cyc))==7 and all(cyc[(i+1)%7] in adj[cyc[i]] for i in range(7))
    # A has four distinct candidate eigenvalues. Verify the exact monic
    # annihilating polynomial and its first four power traces using integers;
    # Vandermonde uniqueness then forces their asserted multiplicities.
    vals=(4,-3,2,-1)
    mult=(1,6,14,14)
    coeff=[1]
    for root in vals:
        nxt=[0]*(len(coeff)+1)
        for j,c in enumerate(coeff):
            nxt[j]-=root*c; nxt[j+1]+=c
        coeff=nxt
    def apply(vec):
        return [sum(vec[u] for u in adj[v]) for v in range(35)]
    traces=[0]*4
    for i in range(35):
        v=[int(j==i) for j in range(35)]
        powers=[v]
        for j in range(4): powers.append(apply(powers[-1]))
        assert all(sum(coeff[j]*powers[j][u] for j in range(5))==0 for u in range(35))
        for j in range(4): traces[j]+=powers[j][i]
    assert traces==[sum(mult[i]*vals[i]**j for i in range(4)) for j in range(4)]
    # A concrete +2 eigenvector demonstrates that the critical eigenvalue
    # is present and that zero-mode exclusion alone is insufficient.
    h=[(int(0 in S)-int(1 in S))*(int(2 in S)-int(3 in S)) for S in vertices]
    assert any(h) and apply(h)==[2*x for x in h]
    return len(vertices), sorted([4,-3,2,-1]), len(cyc)


def balanced_signs(adj):
    d=len(adj[0]); assert all(len(x)==d for x in adj) and not d%2
    out=[]
    for bits in range(1<<len(adj)):
        if all(sum((bits>>u)&1 for u in adj[v])==d//2 for v in range(len(adj))):out.append(bits)
    return out


def check_four_wave(adj, parts, signs):
    left=set(parts)
    seen=set()
    for orientation in range(2):
        for bits in signs:
            phase=[(orientation+(0 if v in left else 1)+2*((bits>>v)&1))%4 for v in range(len(adj))]
            xs=[]
            for t in range(4):
                xs.append(tuple(1 if z==t else 2 if z==(t-1)%4 else 0 for z in phase))
            for t in range(4):assert gh_step(xs[t],adj,len(adj[0])//2)==xs[(t+1)%4]
            assert len(set(xs))==4
            seen.add(xs[0])
    assert len(seen)==2*len(signs)
    return len(signs),len(seen)//4


def check_q4():
    adj=[{v^(1<<k) for k in range(4)} for v in range(16)]
    signs=balanced_signs(adj)
    assert len(signs)==36
    return check_four_wave(adj,[v for v in range(16) if v.bit_count()%2==0],signs)


def check_k44():
    adj=[set(range(4,8)) for _ in range(4)]+[set(range(4)) for _ in range(4)]
    signs=balanced_signs(adj)
    assert len(signs)==comb(4,2)**2
    return check_four_wave(adj,list(range(4)),signs)


def check_k5():
    adj=[set(range(5))-{v} for v in range(5)]
    count=0
    for s in product(range(3),repeat=5):
        cur=s
        for t in range(20):
            if all(x==0 for x in cur):break
            cur=gh_step(cur,adj,2)
        assert all(x==0 for x in cur)
        count+=1
    return count


def lucas():
    residues=[]
    for a in range(7):
        m=4*(3**a)
        n=comb(2*m-1,m-1)
        assert n%3==2
        residues.append((a,m,n%3))
    return residues

if __name__=='__main__':
    print('O4',check_o4())
    print('Q4 signed null vectors / period-four orbits:',check_q4())
    print('K44 signed null vectors / period-four orbits:',check_k44())
    print('K5 configurations extinct:',check_k5())
    print('Lucas family:',lucas())
    print('All verification assertions passed.')
