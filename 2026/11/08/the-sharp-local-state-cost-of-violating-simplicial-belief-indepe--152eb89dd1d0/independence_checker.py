"""Independent three-valued semantics check for finite upward DSMs.
Standard library only. Uses face-level paper semantics, not a modal shortcut.
"""
from itertools import combinations, product

T,F,U=1,0,-1

def downcomplex(facets):
    return set(frozenset(x) for f in facets for n in range(1,len(f)+1)
               for x in combinations(f,n))

def upward(rho, C, vertex):
    assert frozenset((vertex,)) in rho
    assert all(vertex in X and X in C for X in rho)
    assert all(Y in rho for X in rho for Y in C if vertex in Y and Y<=X)
    return all(X|Y in rho for X in rho for Y in rho if X|Y in C)

def getval(face, i, color, trues):
    x=[v for v in face if color[v]==i]
    assert len(x)<=1
    return U if not x else (T if x[0] in trues else F)

def v_or(vals):
    return U if U in vals else int(any(v==T for v in vals))

def box(face,a,subs,rho,color,trues):
    v=next((x for x in face if color[x]==a),None)
    if v is None:return U
    vals=[v_or([getval(Y,i,color,trues) for i in subs]) for Y in rho[v]]
    defined=[w for w in vals if w!=U]
    return U if not defined else int(all(w==T for w in defined))

def witness(k):
    # v=0 is the root of color 0, v=i (1<=i<=k) false local state of color i,
    # v=k+1 is the only true local state of color k.
    a=0; color={i:i for i in range(k+1)}; color[k+1]=k
    high=frozenset([0,*range(1,k),k+1])
    low=frozenset((0,k))
    C=downcomplex((high,low))
    rho={v:{frozenset((v,))} for v in color}
    rho[0]={X for X in C if 0 in X}
    assert all(upward(rho[v],C,v) for v in color)
    trues={k+1}
    face=frozenset((0,))
    ante=box(face,0,tuple(range(1,k+1)),rho,color,trues)
    cons=[box(face,0,(i,),rho,color,trues) for i in range(1,k+1)]
    assert ante==T and cons==[F]*k,(k,ante,cons)
    return len(color), len(C)

# Exhaustively enumerate all chromatic complexes with one vertex of each of 3 colors.
# For each, all downward-closed directions, all valuations, every face containing a.
visited=0; counterexamples=0
color={0:0,1:1,2:2}; edges=((0,1),(0,2),(1,2))
for mask in range(8):
    used=[frozenset(e) for j,e in enumerate(edges) if mask&(1<<j)]
    triangles=[False,True] if len(used)==3 else [False]
    for triangle in triangles:
        C={frozenset((i,)) for i in range(3)}|set(used)
        if triangle: C.add(frozenset((0,1,2)))
        families=[]
        for v in range(3):
            others=sorted([X for X in C if v in X and len(X)>1],key=lambda s:(len(s),tuple(sorted(s))))
            choices=[]
            for bits in product((False,True),repeat=len(others)):
                rho={frozenset((v,))}|{s for s,bit in zip(others,bits) if bit}
                if all(not (Y<=X) or Y in rho for X in rho for Y in C if v in Y): choices.append(rho)
            families.append(choices)
        for ra,rb,rc in product(*families):
            rho={0:ra,1:rb,2:rc}
            for val in range(8):
                trues={i for i in range(3) if val&(1<<i)}
                for face in C:
                    if 0 not in face: continue
                    ante=box(face,0,(1,2),rho,color,trues)
                    v1=box(face,0,(1,),rho,color,trues)
                    v2=box(face,0,(2,),rho,color,trues)
                    if ante==T and v1==F and v2==F: counterexamples+=1
                    visited+=1
assert counterexamples==0
for k in range(2,9):witness(k)
print('ALL_CHECKS_OK', 'three_vertex_cases',visited, 'counterexamples',counterexamples,
      'sharp_witness_sizes', list(range(4,11)))
