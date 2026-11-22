"""Finite mod-two boundary checks for bridge-connected cycle matching complexes.
Standard-library-only. Output is deterministic; tests do not prove the infinite theorem.
"""
from itertools import combinations

def matching_faces(p,q):
    edges = ([(i,(i+1)%p) for i in range(p)]
             + [(p+i,p+(i+1)%q) for i in range(q)] + [(0,p)])
    by_dim = {}
    def rec(i,used,chosen):
        if i == len(edges):
            if chosen:
                by_dim.setdefault(chosen.bit_count()-1,[]).append(chosen)
            return
        rec(i+1,used,chosen)
        u,v=edges[i]
        if not (used & (1<<u) or used & (1<<v)):
            rec(i+1,used|(1<<u)|(1<<v),chosen|(1<<i))
    rec(0,0,0)
    return {d:sorted(set(v)) for d,v in by_dim.items()}

def rank_binary(columns):
    pivots={}
    for col in columns:
        while col:
            high=col.bit_length()-1
            if high not in pivots:
                pivots[high]=col
                break
            col^=pivots[high]
    return len(pivots)

def reduced_betti(p,q):
    faces=matching_faces(p,q)
    ranks={0:1}  # augmented boundary C_0 -> Z/2, reduced homology
    for d in sorted(faces):
        if d == 0:
            continue
        rows={f:i for i,f in enumerate(faces[d-1])}
        columns=[]
        for face in faces[d]:
            vec=0
            for i in range(p+q+1):
                if face & (1<<i):
                    vec^=1<<rows[face^(1<<i)]
            columns.append(vec)
        ranks[d]=rank_binary(columns)
    result={}
    for d,fs in faces.items():
        b=len(fs)-ranks.get(d,0)-ranks.get(d+1,0)
        assert b>=0
        if b:
            result[d]=b
    return result,sum(map(len,faces.values()))

def prediction(p,q):
    k,r=divmod(p,3); ell,s=divmod(q,3)
    r,s=sorted((r,s))
    d=k+ell
    if (r,s)==(0,0): return {d-1:4}
    if (r,s)==(0,1): return {d-1:2}
    if (r,s)==(0,2): return {d:2}
    if (r,s)==(1,1): return {}
    if (r,s)==(1,2): return {d:2}
    if (r,s)==(2,2): return {d:1,d+1:1}
    raise AssertionError('unexpected residue')

if __name__=='__main__':
    count=0; checked_faces=0
    for p in range(3,10):
        for q in range(p,10):
            actual,face_count=reduced_betti(p,q)
            expected=prediction(p,q)
            assert actual==expected,(p,q,actual,expected)
            checked_faces+=face_count; count+=1
            print(f'C_{p}--edge--C_{q}: {actual}; faces={face_count}; PASS')
    assert count==28
    print(f'PASS: {count} lengths pairs, {checked_faces} nonempty faces; all predicted reduced F_2 Betti ranks matched.')
