#!/usr/bin/env python3
"""Independent finite certificates for the induced-forest filtration of the Wagner graph.

Run: python3 verify.py
Uses only the Python standard library and the four bundled JSON certificates.
"""
from collections import Counter, defaultdict, deque
from itertools import combinations
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent
N = 8
EDGES = sorted({tuple(sorted((i,j))) for i in range(N)
                for j in ((i+1)%N, (i+4)%N)})
assert len(EDGES) == 12
EXPECTED_F = [
    [1, 8, 16, 8],
    [1, 8, 28, 32, 10],
    [1, 8, 28, 56, 58, 16],
    [1, 8, 28, 56, 66, 32],
]
EXPECTED_CRIT = [
    {0: 1, 1: 1},
    {0: 1, 2: 1},
    {0: 1, 3: 7},
    {0: 1, 4: 1},
]

def is_forest_and_degree(mask, limit):
    parent = list(range(N))
    degrees = [0]*N
    def find(v):
        while parent[v] != v:
            v = parent[v]
        return v
    for a,b in EDGES:
        if (mask>>a)&1 and (mask>>b)&1:
            degrees[a] += 1
            degrees[b] += 1
            if max(degrees[a],degrees[b]) > limit:
                return False
            pa,pb = find(a),find(b)
            if pa == pb:
                return False
            parent[pa] = pb
    return True

def faces(limit):
    return {mask for mask in range(1,1<<N)
            if is_forest_and_degree(mask,limit)}

def face_vector(fs):
    c=Counter(mask.bit_count()-1 for mask in fs)
    return [1]+[c[i] for i in range(max(c)+1)]

def check_collapse_certificate(limit, fs):
    cert=json.loads((ROOT/'certificates'/f'stage_{limit}.json').read_text('utf-8'))
    assert cert['stage'] == limit
    active=set(fs)
    matched=[]
    critical=[]
    for step in cert['operations']:
        kind=step[0]
        if kind=='collapse':
            assert len(step)==3
            s,t=step[1:]
            assert s in active and t in active
            assert s.bit_count()+1 == t.bit_count() and s&t == s
            assert not any(t != v and (t&v)==t for v in active), ('nonmaximal upper face',t)
            assert not any(t != v and (s&v)==s for v in active if v!=s), ('not free',s)
            active.remove(s)
            active.remove(t)
            matched.append((s,t))
        elif kind=='critical':
            assert len(step)==2
            t=step[1]
            assert t in active
            assert not any(t!=v and (t&v)==t for v in active), ('nonmaximal critical',t)
            active.remove(t)
            critical.append(t)
        else:
            raise AssertionError(('invalid action',step))
    assert not active
    assert len(matched)*2+len(critical)==len(fs)
    assert Counter(t.bit_count()-1 for t in critical)==EXPECTED_CRIT[limit]
    # Independent acyclicity test for the entire matching on the original face poset:
    matched_set={(s,t) for s,t in matched}
    indeg={s:0 for s in fs}
    directed={s:[] for s in fs}
    for t in fs:
        for i in range(N):
            if t>>i&1:
                s=t^(1<<i)
                if s not in fs:continue
                if (s,t) in matched_set:
                    u,v=s,t
                else:
                    u,v=t,s
                directed[u].append(v)
                indeg[v]+=1
    queue=deque(x for x in fs if indeg[x]==0)
    seen=0
    while queue:
        x=queue.popleft()
        seen+=1
        for y in directed[x]:
            indeg[y]-=1
            if indeg[y]==0:
                queue.append(y)
    assert seen==len(fs), 'cyclic discrete-Morse matching'
    return len(matched), dict(sorted(EXPECTED_CRIT[limit].items()))

def permutation_sign(vs, g):
    new=[g(v) for v in vs]
    if set(new)!=set(vs): return 0
    pos={v:i for i,v in enumerate(vs)}
    q=[pos[x] for x in new]
    inv=sum(q[i]>q[j] for i in range(len(q)) for j in range(i+1,len(q)))
    return -1 if inv%2 else 1

def lefschetz(fs,g):
    total=0
    for mask in fs:
        vs=[j for j in range(N) if mask>>j&1]
        total+=(-1)**(len(vs)-1)*permutation_sign(vs,g)
    return total

def check_symmetry(f2,f3):
    edge_set=set(EDGES)
    for k in range(8):
        for g in (lambda x,k=k:(x+k)%8,lambda x,k=k:(k-x)%8):
            assert {tuple(sorted((g(a),g(b)))) for a,b in EDGES}==edge_set
    rot2=[];ref2=[];rot3=[];ref3=[]
    for k in range(8):
        rot=lambda x,k=k:(x+k)%8
        ref=lambda x,k=k:(k-x)%8
        # L(g)=1+(-1)^j tr(g|H_j); j=3 in stage 2 and j=4 in stage 3.
        rot2.append(1-lefschetz(f2,rot))
        ref2.append(1-lefschetz(f2,ref))
        rot3.append(lefschetz(f3,rot)-1)
        ref3.append(lefschetz(f3,ref)-1)
    assert rot2 == [7,1,-1,1,-1,1,-1,1]
    assert ref2 == [1]*8
    assert rot3 == [1,-1,1,-1,1,-1,1,-1]
    assert ref3 == [1,-1,1,-1,1,-1,1,-1]
    # Character orthogonality for D8: one trivial plus each 2D irrep.
    # Only the classes of rotations are needed for the 2D multiplicities.
    assert sum(rot2)+sum(ref2)==16  # exactly one trivial constituent
    for m in (1,2,3):
        import math
        c=sum(rot2[k]*2*math.cos(2*math.pi*m*k/8) for k in range(8))/16
        assert abs(c-1)<1e-9
    return rot2,ref2,rot3,ref3

def main():
    allfaces=[]
    for d in range(4):
        fs=faces(d)
        assert face_vector(fs)==EXPECTED_F[d]
        assert not allfaces or allfaces[-1] <= fs
        allfaces.append(fs)
        npairs,crit=check_collapse_certificate(d,fs)
        print(f'stage {d}: f={EXPECTED_F[d]} pairs={npairs} critical={crit} PASS')
    traces=check_symmetry(allfaces[2],allfaces[3])
    print('D8 stage-2 rotation traces:',traces[0])
    print('D8 stage-2 reflection traces:',traces[1])
    print('D8 stage-3 rotation traces:',traces[2])
    print('D8 stage-3 reflection traces:',traces[3])
    print('All enumeration, elementary-collapse, acyclicity, filtration and symmetry checks PASS')

if __name__=='__main__':main()
