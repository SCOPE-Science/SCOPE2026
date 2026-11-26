"""Exhaustive self-contained circular universal-cycle enumeration for ternary four-mers with three distinct symbols."""
from itertools import product
A = tuple(range(3))
target = {s for s in product(A, repeat=4) if len(set(s)) == 3}
assert len(target) == 36
V = tuple(s for s in product(A, repeat=3) if len(set(s)) == 3)
assert len(V) == 6
# Suppress every one-in/one-out state in the four-mer overlap graph.
def expand_path(u, v):
    for letter in A:
        initial = u + (letter,)
        if initial not in target:
            continue
        state = initial[1:]
        words = [initial]
        while len(set(state)) != 3:
            possible = [b for b in A if state + (b,) in target]
            assert len(possible) == 1
            b = possible[0]
            words.append(state + (b,))
            state = state[1:] + (b,)
        if state == v:
            return words
    raise AssertionError((u, v))
E = sorted((u,v) for u in V for v in V if u!=v and expand_path(u,v)) if False else []
for u in V:
    for b in A:
        start=u+(b,)
        if start not in target: continue
        state=start[1:]
        path=[start]
        while len(set(state))!=3:
            cand=[c for c in A if state+(c,) in target]
            assert len(cand)==1
            c=cand[0]
            path.append(state+(c,))
            state=state[1:]+(c,)
        E.append((u,state,tuple(path)))
assert len(E)==18
assert {x for _,_,p in E for x in p} == target
assert sorted(len(p) for _,_,p in E)==[1]*6+[2]*6+[3]*6
start_edge=next(i for i,e in enumerate(E) if e[0]==(0,1,2) and e[1]==(1,2,0))
start=E[start_edge][0]; used=1<<start_edge
out={u:[i for i,(x,_,_) in enumerate(E) if x==u] for u in V}
counts=0
example=None

def dfs(v,mask,seq):
    global counts,example
    if mask.bit_count()==len(E):
        if v!=start: return
        words=[w for i in seq for w in E[i][2]]
        assert len(words)==36
        assert all(words[j][1:]==words[(j+1)%36][:3] for j in range(36))
        word=tuple(w[0] for w in words)
        assert {tuple(word[(j+k)%36] for k in range(4)) for j in range(36)}==target
        counts+=1
        if example is None:example=''.join(map(str,word))
        return
    for i in out[v]:
        if not (mask>>i)&1:
            dfs(E[i][1],mask|1<<i,seq+[i])

dfs(E[start_edge][1],used,[start_edge])
assert counts==4800,counts
print('count=',counts)
print('witness=',example)
print('target four-mers=',len(target),'overlap states=',len(V),'contracted arcs=',len(E))
