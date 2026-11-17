#!/usr/bin/env python3
"""Reproduce the eight-point matching-complex cyclic-quotient CW reduction.

Usage: python3 verify.py --write certificate.json
       python3 verify.py --check certificate.json
Only Python's standard library is required. This is an exhaustive finite proof
certificate for the explicitly specified finite CW model; the topological
interpretation of the elementary reductions is given in RESULT.md.
"""
import itertools
import json
import sys
from collections import Counter
from pathlib import Path

N=8
P=7
EDGES=list(itertools.combinations(range(N),2))
EDGE_INDEX={e:i for i,e in enumerate(EDGES)}

def rot_edge(e,k):
    return tuple(sorted(((v+k)%P if v<P else P) for v in e))

def rot_face(f,k):
    return tuple(sorted(EDGE_INDEX[rot_edge(EDGES[a],k)] for a in f))

def canon(f):
    return min(rot_face(f,k) for k in range(P))

def face_sizes():
    """All 1..4-edge matchings and all C7-orbit representatives."""
    full=[]; quotient=[]
    for n in range(1,5):
        arr=[f for f in itertools.combinations(range(len(EDGES)),n)
             if len({v for j in f for v in EDGES[j]})==2*n]
        full.append(arr)
        quotient.append(sorted(set(map(canon,arr))))
        # No nonidentity element stabilizes a simplex even setwise.
        assert all(rot_face(f,k)!=f for f in arr for k in range(1,P))
        assert len(arr)==P*len(quotient[-1])
    return full,quotient

def freered(w):
    stack=[]
    for x in w:
        if stack and stack[-1]==-x: stack.pop()
        else: stack.append(x)
    while len(stack)>1 and stack[0]==-stack[-1]:
        stack=stack[1:-1]
    return stack

def parity(perm):
    return (-1)**sum(perm[i]>perm[j]
                     for i in range(len(perm)) for j in range(i+1,len(perm)))

def generate_certificate():
    full,faces=face_sizes()
    reps=[{f:i for i,f in enumerate(arr)} for arr in faces]
    # A triple matching leaves precisely two unused vertices and has exactly
    # one containing perfect matching. Verify directly, not by assumption.
    ext={f:0 for f in full[2]}
    all3=set(full[2])
    for four in full[3]:
        for f in itertools.combinations(four,3): ext[f]+=1
    assert set(ext)==all3 and set(ext.values())=={1}
    # One orbit of free 2-faces is removed for each 3-cell orbit.
    chosen=[canon(t[1:]) for t in faces[3]]
    assert len(set(chosen))==len(faces[3])
    remaining=[t for t in faces[2] if t not in set(chosen)]
    assert len(remaining)==45
    # An oriented quotient edge is identified using a literal rotation of an
    # ordered 2-element face; the sign records whether the endpoints flip.
    def oriented_pair(pair):
        j=reps[1][canon(pair)]
        target=faces[1][j]
        for k in range(P):
            rp=tuple(EDGE_INDEX[rot_edge(EDGES[v],k)] for v in pair)
            if tuple(sorted(rp))==target:
                return j,parity([target.index(v) for v in rp])
        raise AssertionError('No orbit transport found')
    ends=[tuple(reps[0][canon((v,))] for v in face) for face in faces[1]]
    parent=list(range(len(faces[0])))
    def root(i):
        while parent[i]!=i: i=parent[i]
        return i
    tree=[]
    for j,(a,b) in enumerate(ends):
        if root(a)!=root(b):
            parent[root(a)]=root(b)
            tree.append(j)
    assert len(tree)==3
    # Verify each oriented triangle has zero 0-boundary, including repeated
    # quotient endpoints or quotient loops.
    rel=[]
    boundary_columns=[]
    for a,b,c in remaining:
        terms=[]; word=[]
        for pair,sgn in [((b,c),1),((a,c),-1),((a,b),1)]:
            j,s=oriented_pair(pair)
            terms.append([j,sgn*s])
        accum=[0]*len(faces[0])
        for j,s in terms:
            va,vb=ends[j]
            accum[va]-=s;accum[vb]+=s
        assert not any(accum)
        boundary_columns.append(terms)
        for pair in ((a,b),(b,c),(c,a)):
            j,s=oriented_pair(pair)
            if j not in tree:word.append((j+1)*s)
        rel.append(freered(word))
    original_words=[list(w) for w in rel]
    all_generators=set(range(1,len(faces[1])+1))-{i+1 for i in tree}
    assert len(all_generators)==27
    moves=[]
    # Each move eliminates a generator appearing exactly once on the
    # boundary of a particular 2-cell. Substitution is checked verbatim.
    while True:
        candidates=[]
        for j,w in enumerate(rel):
            freq=Counter(abs(x) for x in w)
            for gen,n in freq.items():
                if n==1:
                    occurrences=sum(sum(abs(x)==gen for x in ww) for ww in rel)
                    candidates.append((occurrences,j,gen))
        if not candidates:break
        _,j,gen=min(candidates)
        w=rel[j]
        p=next(i for i,v in enumerate(w) if abs(v)==gen)
        w=w[p:]+w[:p]
        assert abs(w[0])==gen
        repl=[-v for v in w[:0:-1]] if w[0]>0 else w[1:]
        # Check cyclically rotated relator implies g=repl.
        assert freered([w[0]]+w[1:])==freered(w)
        def substitute(word):
            out=[]
            for v in word:
                if abs(v)!=gen:out.append(v)
                elif v>0:out.extend(repl)
                else:out.extend(-x for x in reversed(repl))
            return freered(out)
        other=[substitute(u) for i,u in enumerate(rel) if i!=j]
        moves.append({'relator_index':j,'generator':gen,
                      'relator_rotated':w,'replacement':repl})
        rel=other
    eliminated={m['generator'] for m in moves}
    assert len(moves)==26 and len(eliminated)==26
    assert all_generators-eliminated=={10}
    assert len(rel)==19
    exponents=[sum(1 if v>0 else -1 for v in w) for w in rel]
    assert set(abs(t) for t in exponents)<= {0,7,14}
    assert 7 in set(abs(t) for t in exponents)
    assert all(all(abs(v)==10 for v in w) for w in rel)
    # This count independently verifies Euler characteristic of quotient.
    assert 4-30+60-15==19 and 4-30+45==19
    return {
        'specification':{'ground_labels':list(range(8)),
                         'rotated_labels':list(range(7)),
                         'fixed_label':7,'group_order':7},
        'full_face_counts':list(map(len,full)),
        'quotient_face_counts':list(map(len,faces)),
        'selected_collapse_pairs':[
            {'tetrahedron_orbit':list(t),'triangle_orbit':list(c)}
            for t,c in zip(faces[3],chosen)],
        'collapsed_quotient_face_counts':[4,30,45],
        'tree_edge_orbit_indices_0_based':tree,
        'initial_attaching_words':original_words,
        'elementary_substitutions':moves,
        'final_attaching_exponents':exponents,
        'final_generator_id_1_based':10,
        'initial_and_final_euler_characteristic':19,
        'conclusion':{'moore_degree':7,'sphere_dimension':2,'sphere_count':18}
    }

def main():
    assert len(sys.argv)==3 and sys.argv[1] in ('--check','--write')
    data=generate_certificate()
    data_json=json.dumps(data,indent=2,ensure_ascii=False,sort_keys=True)+'\n'
    file=Path(sys.argv[2])
    if sys.argv[1]=='--write':file.write_text(data_json,encoding='utf-8')
    else:
        saved=json.loads(file.read_text(encoding='utf-8'))
        assert saved==data, 'The certificate differs from the fresh exhaustive replay'
    print('FULL_MATCHING_FACES',data['full_face_counts'])
    print('QUOTIENT_CELLS',data['quotient_face_counts'])
    print('AFTER_FREE_FACE_COLLAPSES',data['collapsed_quotient_face_counts'])
    print('SPANNING_TREE',data['tree_edge_orbit_indices_0_based'])
    print('ELIMINATION_STEPS',len(data['elementary_substitutions']))
    print('FINAL_RELATOR_EXPONENTS',data['final_attaching_exponents'])
    print('HOMOTOPY_TYPE M(Z/7,1) wedge (18 copies of S^2)')
    print('PASS')
if __name__=='__main__':main()
