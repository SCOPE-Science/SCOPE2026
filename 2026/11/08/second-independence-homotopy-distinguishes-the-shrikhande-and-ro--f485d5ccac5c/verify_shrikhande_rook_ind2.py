#!/usr/bin/env python3
"""Exhaustive integer Morse verification for second-independence complexes."""
from collections import Counter, defaultdict, deque
from functools import lru_cache
from itertools import combinations

N = 16
DIRECTIONS = {(1,0),(3,0),(0,1),(0,3),(1,1),(3,3)}

def neighbors(kind):
    adj = [0] * N
    for a in range(N):
        i,j = divmod(a,4)
        for b in range(a+1,N):
            k,l = divmod(b,4)
            linked = ((i-k)%4,(j-l)%4) in DIRECTIONS if kind == 'Shrikhande' else i == k or j == l
            if linked:
                adj[a] |= 1 << b
                adj[b] |= 1 << a
    assert all(t.bit_count() == 6 for t in adj)
    assert all((adj[a] & adj[b]).bit_count() == 2 for a in range(N) for b in range(a+1,N))
    local = {v for v in range(N) if adj[0] >> v & 1}
    connected_sizes = []
    while local:
        seed = min(local)
        seen = {seed}
        frontier = [seed]
        while frontier:
            v = frontier.pop()
            for w in list(local - seen):
                if adj[v] >> w & 1:
                    seen.add(w)
                    frontier.append(w)
        connected_sizes.append(len(seen))
        local.difference_update(seen)
    assert sorted(connected_sizes) == ([6] if kind == 'Shrikhande' else [3,3])
    return adj

def enumerate_faces(adj):
    bad = []
    for a in range(N):
        nbr = [b for b in range(N) if adj[a] >> b & 1]
        for b,c in combinations(nbr,2):
            bad.append((1<<a)|(1<<b)|(1<<c))
    valid = bytearray(1 << N)
    valid[0] = 1
    for m in range(1,1<<N):
        bit = m & -m
        valid[m] = valid[m^bit] and not any(m & t == t for t in bad)
    # Independent test: the induced maximum degree is at most one.
    for m in range(1<<N):
        ok = all((adj[v] & m).bit_count() <= 1 for v in range(N) if m >> v & 1)
        assert bool(valid[m]) == ok, (m,ok)
    return valid

def build_matching(valid, order):
    unmatched = bytearray(valid)
    pair = {}
    for v in order:
        bit = 1 << v
        for m in range(1 << N):
            if not unmatched[m] or (m & bit) or not unmatched[m|bit]:
                continue
            unmatched[m] = unmatched[m|bit] = 0
            pair[m] = m|bit
            pair[m|bit] = m
    assert pair.get(0) is not None
    vertex = pair.pop(0)
    assert pair.pop(vertex) == 0
    assert not unmatched[vertex]
    unmatched[vertex] = 1
    return unmatched,pair,vertex

def acyclic_hasse(valid,pair):
    indeg = [0] * (1<<N)
    outgoing = [[] for _ in range(1<<N)]
    arrows = 0
    for upper in range(1,1<<N):
        if not valid[upper]:continue
        for b in iterbits(upper):
            lower=upper^b
            if not lower:continue
            if pair.get(lower) == upper:
                src,dst=lower,upper
            else:
                src,dst=upper,lower
            outgoing[src].append(dst)
            indeg[dst]+=1
            arrows+=1
    q=deque(m for m in range(1,1<<N) if valid[m] and indeg[m] == 0)
    seen=0
    while q:
        m=q.popleft();seen+=1
        for y in outgoing[m]:
            indeg[y]-=1
            if indeg[y] == 0:q.append(y)
    assert seen == sum(valid)-1,(seen,sum(valid)-1)
    return arrows,seen

def iterbits(m):
    while m:
        b=m&-m
        yield b
        m-=b

def sign(mask,bit):
    return -1 if (mask & (bit-1)).bit_count() & 1 else 1

def integer_morse_boundary(pair,lowcrit,topcrit):
    @lru_cache(None)
    def expansion(face):
        if face in lowcrit:
            return {face:1}
        other=pair.get(face)
        if other is None or other.bit_count()<face.bit_count():
            return {}
        bit=other^face
        leading=sign(other,bit)
        out=defaultdict(int)
        for b in iterbits(other):
            if b == bit:continue
            for x,k in expansion(other^b).items():
                out[x]-=leading*sign(other,b)*k
        return {k:v for k,v in out.items() if v}
    boundary={}
    for upper in sorted(topcrit):
        row=defaultdict(int)
        for b in iterbits(upper):
            for low,k in expansion(upper^b).items():
                row[low]+=sign(upper,b)*k
        boundary[upper]={k:v for k,v in row.items() if v}
    return boundary

for kind,order in [('Shrikhande',list(range(N))),('Rook',[i*5%16 for i in range(16)])]:
    adj=neighbors(kind)
    valid=enumerate_faces(adj)
    counts=Counter(m.bit_count()-1 for m in range(1,1<<N) if valid[m])
    unmatched,pair,base=build_matching(valid,order)
    critical=Counter(m.bit_count()-1 for m in range(1,1<<N) if unmatched[m])
    arrows,seen=acyclic_hasse(valid,pair)
    low={m for m in range(1,1<<N) if unmatched[m] and m.bit_count() == 3}
    top={m for m in range(1,1<<N) if unmatched[m] and m.bit_count() == 4}
    bd=integer_morse_boundary(pair,low,top)
    vals=Counter(value for row in bd.values() for value in row.values())
    print(kind,'f_vector',dict(sorted(counts.items())))
    print(kind,'faces',sum(valid)-1,'matched_pairs',len(pair)//2,'critical',dict(sorted(critical.items())),'base',base,'hasse_arrows',arrows,'sorted_vertices',seen)
    print(kind,'boundary_nonzero',sum(map(bool,bd.values())),'coefficients',dict(vals),'critical_2',list(low),'first_unit_witness',next(((a,b,c) for a,row in bd.items() for b,c in row.items() if abs(c)==1),None))
    if kind=='Shrikhande':
        assert counts == {0:16,1:120,2:384,3:544,4:240,5:32}
        assert critical == {0:1,2:1,3:58}
        assert any(abs(v)==1 for row in bd.values() for v in row.values())
        assert arrows == 4976 - 16  # remove 16 vertex-to-empty arrows
    else:
        assert counts == {0:16,1:120,2:384,3:528,4:144}
        assert critical == {0:1,3:105}
        assert not any(bd.values())
        assert arrows == 4240 - 16
print('INTEGRAL_MORSE_CERTIFICATE_PASS')
