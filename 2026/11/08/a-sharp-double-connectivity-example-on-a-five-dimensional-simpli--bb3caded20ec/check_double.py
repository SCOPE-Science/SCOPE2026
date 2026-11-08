#!/usr/bin/env python3
"""Independent finite checks for the double of a join of two tetrahedral boundaries."""
from itertools import combinations

A=set(range(4)); B=set(range(4,8)); U=A|B
V=list(combinations(range(8),2))
AA={e for e in V if set(e)<=A}; BB={e for e in V if set(e)<=B}
AB=set(V)-AA-BB

def allowed(F):
    used=[]
    for e in F: used.extend(e)
    return len(used)==len(set(used)) and not A<=set(used) and not B<=set(used)

def make_faces(vertices,rule):
    out={0:[(v,) for v in vertices]}
    for k in (2,3):
        out[k-1]=[F for F in combinations(vertices,k) if allowed(F) and rule(F)]
    return out

allf=make_faces(V,lambda F:True)
cf=make_faces(sorted(AB),lambda F:True)
yf=make_faces(V,lambda F:len(F)<3 or (sum(e in AB for e in F)==1))
# Y has no AB--AB edges; include only edges between distinct types, and AA--BB.
yf[1]=[F for F in yf[1] if not all(e in AB for e in F)]
yf[2]=[F for F in yf[2] if sum(e in AB for e in F)==1]
for k in range(3):
    assert set(allf[k])==set(cf[k])|set(yf[k])
    assert len(set(cf[k])&set(yf[k]))== (16 if k==0 else 0)
assert [len(allf[k]) for k in range(3)]==[28,204,240]
assert [len(cf[k]) for k in range(3)]==[16,72,96]
assert [len(yf[k]) for k in range(3)]==[28,132,144]

# Directly reconstruct cone construction of Y, including 16 K_{3,3} links.
base={F for F in yf[1] if all(e not in AB for e in F)}
assert len(base)==36
for e in AB:
    triples={F for F in yf[2] if (e,) == (tuple(x for x in F if x in AB))}
    left=[p for p in AA if set(p).isdisjoint(e)]
    right=[q for q in BB if set(q).isdisjoint(e)]
    assert len(left)==len(right)==3
    assert triples=={tuple(sorted((e,p,q))) for p in left for q in right}

# A calculation from oriented boundary maps over finite fields, independent
# of the homotopy proof. Matrices are generated from simplicial incidences.
def rank_mod(faces,p):
    ranks=[]
    for dim in (1,2):
        lo={f:i for i,f in enumerate(faces[dim-1])}
        pivots={}
        for col in faces[dim]:
            vec={lo[col[:j]+col[j+1:]]:(1 if j%2==0 else p-1) for j in range(dim+1)}
            while vec:
                lead=min(vec)
                if lead not in pivots:
                    inv=pow(vec[lead],-1,p)
                    pivots[lead]={i:(v*inv)%p for i,v in vec.items()}
                    break
                coeff=vec[lead]
                for i,v in pivots[lead].items():
                    new=(vec.get(i,0)-coeff*v)%p
                    if new: vec[i]=new
                    else: vec.pop(i,None)
        ranks.append(len(pivots))
    return ranks

for p in (2,101,103):
    result=[]
    for F in (allf,cf,yf):
        r1,r2=rank_mod(F,p)
        b=(len(F[0])-r1-1,len(F[1])-r1-r2,len(F[2])-r2)
        result.append(b)
    assert result==[(0,15,78),(0,0,39),(0,0,39)],(p,result)
    print('prime',p,'reduced_betti (double,chessboard_skeleton,cone_union):',result)
print('f_vectors:',*[tuple(len(F[k]) for k in range(3)) for F in (allf,cf,yf)])
print('DOUBLE_JOIN_BOUNDARIES_CHECKS_OK')
