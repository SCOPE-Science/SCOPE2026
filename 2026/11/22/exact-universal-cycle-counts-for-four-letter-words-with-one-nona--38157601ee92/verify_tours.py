"""Independent exhaustive small-alphabet overlap-tour verification."""
from itertools import product
from collections import Counter,defaultdict

def allowed(w):
    return len(set(w)) == 3 and (w[0] == w[2] or w[1] == w[3] or w[0] == w[3])

def edges(q):
    return [w for w in product(range(q),repeat=4) if allowed(w)]

def cycle_from_edges(seq):
    s=''.join(str(e[0]) for e in seq)
    return s

def verify(seq, expect):
    s=cycle_from_edges(seq)
    n=len(s)
    windows=Counter(tuple(map(int, ''.join(s[(i+j)%n] for j in range(4)))) for i in range(n))
    assert len(windows)==len(expect)
    assert windows==Counter({w:1 for w in expect})
    return s
E=edges(3)
idx={w:i for i,w in enumerate(E)}
out=defaultdict(list)
for w in E:out[w[:3]].append(w)
start=min(E)
used={start}
seq=[start]
words=[]
def dfs(v):
    if len(seq)==len(E):
        if v==start[:3]: words.append(verify(seq,E))
        return
    for w in out[v]:
        if w in used:continue
        used.add(w);seq.append(w)
        dfs(w[1:])
        seq.pop();used.remove(w)
dfs(start[1:])
assert len(words)==len(set(words))==12
print('q=3 Euler tours modulo rotation:',len(words))
print('q=3 lexicographic witness:',min(words))
# Hierholzer, completely separate existence check on q=4.
q=4;E=edges(q);out=defaultdict(list)
for w in E:out[w[:3]].append(w)
for v in out:out[v].sort(reverse=True)
stack=[min(out)]; walk=[]
while stack:
    v=stack[-1]
    if out[v]:stack.append(out[v].pop()[1:])
    else:walk.append(stack.pop())
walk=walk[::-1]
assert len(walk)==len(E)+1 and walk[0]==walk[-1]
seq=[(walk[i][0],walk[i][1],walk[i][2],walk[i+1][2]) for i in range(len(E))]
assert Counter(seq)==Counter(E)
print('q=4 witness:',verify(seq,E))
print('TOUR_VERIFY_OK')
