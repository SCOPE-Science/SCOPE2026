#!/usr/bin/env python3
"""Finite certificate for the perfect-matching complex of the Fano incidence graph.
Uses only Python standard library; reconstructs all faces and all Morse pairs.
"""
from collections import Counter, defaultdict, deque
from itertools import permutations

LINES = [frozenset(((i)%7, (i+1)%7, (i+3)%7)) for i in range(7)]
EDGES = [(i,j) for i in range(7) for j in sorted(LINES[i])]
assert len(EDGES)==21 and len(set(EDGES))==21
EDGE_ID = {a:k for k,a in enumerate(EDGES)}

def matchings():
    match=[]
    def extend(p, used, chosen):
        if p==7:
            match.append(tuple(sorted(chosen)));return
        for i in range(7):
            if p in LINES[i] and not (used>>i)&1:
                extend(p+1,used|(1<<i),chosen+(EDGE_ID[i,p],))
    extend(0,0,())
    return match

def faces_of(facets):
    faces=set()
    for F in facets:
        for sel in range(1,1<<len(F)):
            mask=0
            for j,i in enumerate(F):
                if sel & (1<<j):mask|=1<<i
            faces.add(mask)
    return faces

def morse(faces):
    """Face-poset pairing by a deterministic sequence of vertex toggles."""
    free=set(faces)
    pairs=[]
    for i in range(21):
        for f in sorted(free):
            if f not in free or f & (1<<i): continue
            F=f | (1<<i)
            if F in free:
                free.remove(f);free.remove(F);pairs.append((f,F))
    assert len(free)+2*len(pairs)==len(faces)
    return free,pairs

def check(faces,critical,pairs):
    """Check every codimension-one incidence, gradient direction and acyclicity."""
    face_set=set(faces);used=set()
    pair_set=set(pairs)
    assert len(pair_set)==len(pairs)
    for low,high in pairs:
        assert low in face_set and high in face_set
        assert high.bit_count()==low.bit_count()+1
        assert ((high ^ low).bit_count()==1) and (low & high)==low
        assert low not in used and high not in used
        used.update((low,high))
    assert face_set-used==set(critical)
    outs=defaultdict(list);indeg={f:0 for f in faces};incident=0
    for high in faces:
        for b in range(21):
            if not high&(1<<b):continue
            low=high^(1<<b)
            if low not in face_set:continue
            incident+=1
            src,dst=(low,high) if (low,high) in pair_set else (high,low)
            outs[src].append(dst);indeg[dst]+=1
    Q=deque(f for f in faces if indeg[f]==0)
    seen=0
    while Q:
        f=Q.popleft();seen+=1
        for other in outs[f]:
            indeg[other]-=1
            if indeg[other]==0:Q.append(other)
    assert seen==len(faces),('directed gradient cycle',len(faces)-seen)
    return incident

def dimensions(faces):
    return dict(sorted(Counter(f.bit_count()-1 for f in faces).items()))

def mod2_betti(faces, relative=False):
    """Independent raw relative simplicial boundary check over F2."""
    bysize={k:sorted(f for f in faces if f.bit_count()==k) for k in range(1,8)}
    count={k:len(bysize[k]) for k in range(1,8)}
    ranks={}
    for k in range(2,8):
        row={f:j for j,f in enumerate(bysize[k-1])}
        pivots={}
        for F in bysize[k]:
            col=0
            for e in range(21):
                if F & (1<<e):
                    j=row.get(F^(1<<e))
                    if j is not None:col ^= 1<<j
            while col:
                leading=col.bit_length()-1
                if leading in pivots:col ^= pivots[leading]
                else:
                    pivots[leading]=col
                    break
        ranks[k-1]=len(pivots)
    result={}
    for k in range(1,8):
        b=count[k]-ranks.get(k-1,0)-ranks.get(k,0)
        if b:result[k-1]=b
    return result

def run():
    # Verify the Fano plane point-pair axiom independently of matching enumeration.
    for p in range(7):
        for q in range(p+1,7):
            assert sum(p in L and q in L for L in LINES)==1
    facets=matchings()
    assert len(facets)==len(set(facets))==24
    X=faces_of(facets)
    assert len(X)==2201
    xcrit,xpairs=morse(X)
    xinc=check(X,xcrit,xpairs)
    assert dimensions(xcrit)=={0:1,2:16}
    assert mod2_betti(X)=={0:1,2:16}
    print('X faces',len(X),'f_vector',dimensions(X),'morse_pairs',len(xpairs),'critical',dimensions(xcrit),'hasse',xinc)
    all_rows=[]
    for e in range(21):
        M=[F for F in facets if e not in F]
        A=faces_of(M)
        R=X-A
        acrit,apairs=morse(A)
        rcrit,rpairs=morse(R)
        ai=check(A,acrit,apairs)
        ri=check(R,rcrit,rpairs)
        if dimensions(acrit)!={0:1,2:7} or dimensions(rcrit)!={2:9}:
            raise AssertionError(('unexpected critical',e,dimensions(acrit),dimensions(rcrit)))
        assert len(A)==1552 and len(R)==649 and len(M)==16
        assert mod2_betti(A)=={0:1,2:7}
        assert mod2_betti(R)=={2:9}
        all_rows.append((e,len(M),len(A),len(apairs),ai,len(R),len(rpairs),ri))
    assert len(all_rows)==21
    print('Each of 21 edge deletions: 16 surviving perfect matchings; A has 1552 faces, 772 Morse pairs, critical (one 0-cell, seven 2-cells).')
    print('Each relative pair (X,A): 649 relative faces, 320 Morse pairs, nine critical 2-cells.')
    print('First three edge rows',all_rows[:3])
    print('Independent raw mod-two boundary reductions agree with all three Morse critical-cell profiles for every edge.')
    print('All 21 deletion and relative gradient digraphs checked exhaustively acyclic; INTEGRAL_RESULT_OK')

if __name__=='__main__':run()
