#!/usr/bin/env python3
"""Exact finite verification for the cyclic seven-tournament multipath complex.

Requires Python >=3.10 and SymPy. All arithmetic for integral Morse
matrices and invariant-chain ranks is exact. No external inputs are used.
"""
import functools
import itertools
import json
from collections import Counter, defaultdict, deque
from sympy import Matrix, ZZ, zeros
from sympy.matrices.normalforms import smith_normal_form

N=7
EDGES=sorted((u,(u+d)%N) for u in range(N) for d in (1,2,3))
EDGE_INDEX={a:i for i,a in enumerate(EDGES)}

def generate_faces():
    by_size=[set() for _ in range(N)]
    def explore(start,face,used_out,used_in,next_vertex,card):
        by_size[card].add(face)
        for i in range(start,len(EDGES)):
            a,b=EDGES[i]
            if used_out & (1<<a) or used_in & (1<<b):continue
            v=b
            while v in next_vertex:
                v=next_vertex[v]
                if v==a:break
            if v==a:continue
            next_vertex[a]=b
            explore(i+1,face|(1<<i),used_out|(1<<a),used_in|(1<<b),next_vertex,card+1)
            del next_vertex[a]
    explore(0,0,0,0,{},0)
    return by_size

def is_multipath(combo):
    successor={};predecessor={}
    for i in combo:
        a,b=EDGES[i]
        if a in successor or b in predecessor:return False
        successor[a]=b;predecessor[b]=a
    for a in successor:
        visited=set();v=a
        while v in successor:
            if v in visited:return False
            visited.add(v);v=successor[v]
    return True

def exhaustive_independent_faces():
    faces=[set() for _ in range(N)]
    for length in range(N):
        for c in itertools.combinations(range(len(EDGES)),length):
            if is_multipath(c):
                faces[length].add(sum(1<<i for i in c))
    return faces

def facets(face):
    out=[];i=0;f=face
    while f:
        if f&1:out.append((face^(1<<i),(-1)**len(out)))
        i+=1;f>>=1
    return out

def greedy_matching(faces,order):
    remaining=set().union(*faces);pairs=[]
    for i in order:
        new_pairs=[]
        for f in remaining:
            if f&(1<<i):continue
            g=f|(1<<i)
            if g in remaining:new_pairs.append((f,g))
        for low,high in new_pairs:
            remaining.remove(low);remaining.remove(high)
        pairs.extend(new_pairs)
    return remaining,pairs

def verify_acyclic(faces,pairs):
    allfaces=set().union(*faces)
    pair_lookup=set(pairs)
    outgoing={f:[] for f in allfaces};indeg={f:0 for f in allfaces};count=0
    for f in allfaces:
        for low,_ in facets(f):
            src,dest=(low,f) if (low,f) in pair_lookup else (f,low)
            outgoing[src].append(dest);indeg[dest]+=1;count+=1
    q=deque(f for f in allfaces if indeg[f]==0);visited=0
    while q:
        f=q.popleft();visited+=1
        for g in outgoing[f]:
            indeg[g]-=1
            if not indeg[g]:q.append(g)
    assert visited==len(allfaces),(visited,len(allfaces))
    return count

def morse_matrices(remaining,pairs):
    low_to_high=dict(pairs);high_to_low={h:l for l,h in pairs}
    @functools.lru_cache(None)
    def reduce_face(f):
        if f in remaining:return {f:1}
        if f in high_to_low:return {}
        assert f in low_to_high
        high=low_to_high[f]
        boundary=dict(facets(high))
        pivot=boundary[f]
        result=defaultdict(int)
        for other,s in boundary.items():
            if other==f:continue
            for crit,coefficient in reduce_face(other).items():
                result[crit]-=pivot*s*coefficient
        return {k:v for k,v in result.items() if v}
    crit=defaultdict(list)
    for f in remaining:crit[f.bit_count()-1].append(f)
    for d in crit:crit[d].sort()
    mats={}
    for degree in sorted(crit):
        if degree<=0:continue
        higher=crit[degree];lower=crit[degree-1]
        m=zeros(len(lower),len(higher));ix={f:i for i,f in enumerate(lower)}
        for j,f in enumerate(higher):
            for facet,sgn in facets(f):
                for target,coeff in reduce_face(facet).items():
                    m[ix[target],j]+=sgn*coeff
        mats[degree]=m
    for degree in mats:
        if degree+1 in mats:
            assert mats[degree]*mats[degree+1]==zeros(mats[degree].rows,mats[degree+1].cols)
    return crit,mats

def exact_invariants(faces):
    rotations=[[EDGE_INDEX[((a+k)%N,(b+k)%N)] for a,b in EDGES] for k in range(N)]
    def rotate(face,k):
        inds=[rotations[k][i] for i in range(len(EDGES)) if face>>i&1]
        crossings=sum(inds[i]>inds[j] for i in range(len(inds)) for j in range(i+1,len(inds)))
        return sum(1<<i for i in inds), -1 if crossings%2 else 1
    orbit={};reps={}
    for degree,group in enumerate(faces):
        if degree==0:continue
        r=sorted({min(rotate(f,k)[0] for k in range(N)) for f in group})
        assert len(r)*N==len(group)
        for j,f in enumerate(r):
            for k in range(N):
                h,sgn=rotate(f,k)
                assert h not in orbit
                orbit[h]=(degree,j,sgn)
        reps[degree]=r
    matrices={}
    for degree in range(2,N):
        B=zeros(len(reps[degree-1]),len(reps[degree]))
        for col,f in enumerate(reps[degree]):
            for h,coeff in facets(f):
                d,row,sgn=orbit[h]
                assert d==degree-1
                B[row,col]+=coeff*sgn
        matrices[degree]=B
    for degree in range(3,N):
        assert matrices[degree-1]*matrices[degree]==zeros(matrices[degree-1].rows,matrices[degree].cols)
    ranks={degree:int(B.rank()) for degree,B in matrices.items()}
    # Degree-0 unaugmented boundary has rank zero; C_0/G has three generators.
    betti={degree-1:len(group)-ranks.get(degree,0)-ranks.get(degree+1,0)
           for degree,group in reps.items()}
    assert betti=={0:1,1:0,2:0,3:1,4:7,5:5},betti
    return dict(sorted((d,len(f)) for d,f in reps.items())),ranks,betti

def full_mod2_ranks(faces):
    result={}
    for degree in range(2,N):
        ix={f:i for i,f in enumerate(sorted(faces[degree-1]))}
        pivots={}
        for f in faces[degree]:
            col=0
            for h,_ in facets(f):col^=1<<ix[h]
            while col:
                k=col.bit_length()-1
                if k not in pivots:
                    pivots[k]=col
                    break
                col^=pivots[k]
        result[degree-1]=len(pivots)
    return result

def main():
    faces=generate_faces()
    independent=exhaustive_independent_faces()
    assert faces==independent
    assert len(EDGES)==21
    face_vector=[len(f) for f in faces]
    assert face_vector==[1,21,168,630,1113,819,175],face_vector
    Hasse=sum(i*len(group) for i,group in enumerate(faces))
    assert Hasse==11844
    summary={}
    for name,order in [('ascending',range(21)),('descending',reversed(range(21)))]:
        rem,pairs=greedy_matching(faces,order)
        assert len(pairs)*2+len(rem)==sum(face_vector)
        assert verify_acyclic(faces,pairs)==Hasse
        crit,mats=morse_matrices(rem,pairs)
        cr={degree:len(f) for degree,f in crit.items() if f}
        ranks={};smith={}
        for degree,B in mats.items():
            D=smith_normal_form(B,domain=ZZ)
            diagonal=[int(D[i,i]) for i in range(min(D.shape)) if D[i,i]]
            assert all(abs(x)==1 for x in diagonal)
            ranks[degree]=len(diagonal)
            smith[degree]={'rank':len(diagonal),'nonunit_factors':0}
        summary[name]={'pairs':len(pairs),'critical_cells':{str(k):v for k,v in sorted(cr.items())},
                       'boundary_ranks':{str(k):v for k,v in sorted(ranks.items())},
                       'smith_factors':{str(k):v for k,v in sorted(smith.items())}}
        if name=='ascending':
            assert cr=={3:24,4:54,5:17}
            assert ranks=={3:0,4:11,5:0}
            B=mats[4]
            rows=[1,2,3,4,5,10,11,12,13,14,20]
            columns=[5,9,14,15,17,23,25,27,32,46,47]
            assert B.extract(rows,columns).det()==1
        else:
            assert cr=={2:1,3:32,4:61,5:17}
            assert ranks=={2:0,3:1,4:18,5:0}
    mod2=full_mod2_ranks(faces)
    assert mod2=={1:20,2:148,3:482,4:618,5:158},mod2
    o,r,betti=exact_invariants(faces)
    group_ranks={3:13,4:43,5:17}
    # Rational C_7 representation is a copies of 1 plus b copies of Q(zeta_7).
    nonidentity_traces={str(d):(7*betti[d]-rank)//6 for d,rank in group_ranks.items()}
    assert nonidentity_traces=={'3':-1,'4':1,'5':3}
    result={
      'verification_marker':'CYCLIC_SEVEN_TOURNAMENT_MULTIPATH_HOMOLOGY_AND_C7_CHARACTER_VERIFIED',
      'arc_count':len(EDGES),
      'face_vector_including_empty':face_vector,
      'Hasse_incidences':Hasse,
      'morse_checks':summary,
      'independent_mod2_boundary_ranks':{str(k):v for k,v in mod2.items()},
      'reduced_integral_homology_ranks':{str(k):v for k,v in group_ranks.items()},
      'integral_torsion_factors':[],
      'cyclic_seven_face_orbits_by_cardinality':{str(k):v for k,v in o.items()},
      'cyclic_seven_invariant_chain_boundary_ranks':{str(k):v for k,v in r.items()},
      'cyclic_seven_fixed_homology_dimensions':{str(k):betti[k] for k in group_ranks},
      'cyclic_seven_nonidentity_homology_traces':nonidentity_traces,
      'independent_audit':'not_performed',
    }
    print(json.dumps(result,indent=2,sort_keys=True))
if __name__=='__main__':main()
