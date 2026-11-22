#!/usr/bin/env python3
"""Exact finite-state verifier for the four-sheet inverse law.
No external packages. Run: python3 check.py
"""
from collections import defaultdict, Counter, deque

N = 16
IDENT = tuple(range(N))

def T(b):
    arr=[]
    for s in range(N):
        a=(s>>3)&1; c=(s>>2)&1; d=(s>>1)&1; e=s&1
        v=b ^ c ^ (a & (d^1) & (c^e^1))
        arr.append((v<<3)|(a<<2)|(c<<1)|d)
    return tuple(arr)

T0,T1=T(0),T(1)
TR=(T0,T1)

def compose(f,g):
    return tuple(f[g[s]] for s in range(N))

def prod(w):
    f=IDENT
    for b in w:
        f=compose(TR[int(b)],f)
    return f

def fixed(f):
    return sum(f[i]==i for i in range(N))

def kernel(f):
    d=defaultdict(list)
    for i,x in enumerate(f):d[x].append(i)
    return tuple(sorted(tuple(v) for v in d.values()))

def image(f):
    return tuple(sorted(set(f)))

def reach(start,graph):
    have={start}; todo=[start]
    for s in todo:
        for t in graph[s]:
            if t not in have:
                have.add(t);todo.append(t)
    return have

# Exhaust all transformations in the two-letter transition monoid.
states=[IDENT]; ids={IDENT:0}; trans=[]
for f in states:
    successors=[]
    for t in TR:
        g=compose(t,f)
        if g not in ids:
            ids[g]=len(states); states.append(g)
        successors.append(ids[g])
    trans.append(tuple(successors))
assert len(states)==491, len(states)
assert len(trans)==len(states)
assert Counter(map(lambda f:len(image(f)),states)) == {4:480,6:6,8:2,10:2,16:1}

# After four symbols, every transformation has rank four.
words=[''.join(str((i>>j)&1) for j in range(4)) for i in range(16)]
assert all(len(image(prod(w)))==4 for w in words)
rank4={i for i,f in enumerate(states) if len(image(f))==4}
assert len(rank4)==480
assert all(all(t in rank4 for t in trans[i]) for i in rank4)
assert set(ids[prod(w)] for w in words) <= rank4

# Two kernel classes, each 10 images times 24 transformations.
by_kernel=defaultdict(lambda:defaultdict(list))
for i in rank4:
    f=states[i]; by_kernel[kernel(f)][image(f)].append(i)
assert len(by_kernel)==2
for K,imgs in by_kernel.items():
    idsK={i for seq in imgs.values() for i in seq}
    assert len(K)==4 and len(idsK)==240 and len(imgs)==10
    assert all(len(group)==24 for group in imgs.values())
    for I,idxs in imgs.items():
        assert all(sum(x in block for x in I)==1 for block in K)
        assert Counter(fixed(states[i]) for i in idxs)=={0:9,1:8,2:6,4:1}
        assert all(all(t in idsK for t in trans[i]) for i in idxs)
    # Forward/backward reachability verifies irreducibility of this closed class.
    start=min(idsK)
    forward={i:trans[i] for i in idsK}
    reverse=defaultdict(list)
    for i in idsK:
        for j in trans[i]: reverse[j].append(i)
    assert reach(start,forward)==idsK
    assert reach(start,reverse)==idsK
    # Closed walks of coprime lengths prove aperiodicity.
    assert ids[compose(T0,states[start])]==trans[start][0]
    def applyword(i,w):
        for c in w:i=trans[i][int(c)]
        return i
    assert applyword(start,'00')==start
    assert applyword(start,'01001001000')==start

# Enumerate each finite ring directly and compare exact fixed-point transfer.
def local(a,b,c,d,e):
    return a^c^(b&(d^1)&(c^e^1))

def binary_word(mask,n):
    return tuple((mask>>i)&1 for i in range(n))

def output(x):
    n=len(x)
    return tuple(local(*[x[(i+j)%n] for j in range(5)]) for i in range(n))

for n in range(1,13):
    fibers=Counter()
    for xmask in range(1<<n):fibers[output(binary_word(xmask,n))]+=1
    pop=Counter()
    for ymask in range(1<<n):
        y=binary_word(ymask,n)
        # Proper backward spatial ordering for transfer map.
        f=prod(reversed(y))
        k=fixed(f)
        assert k==fibers[y], (n,y,k,fibers[y])
        assert k in (0,1,2,4)
        pop[k]+=1
    print(f'n={n:2d} fiber histogram={dict(sorted(pop.items()))}')

print('PASS: exact 491-map closure; all length-four rank four; two 240-state primitive classes;')
print('      ten transversal images x 24 permutations; S4 fixed-point counts 9,8,6,1;')
print('      exhaustive independent cyclic checks through n=12.')
