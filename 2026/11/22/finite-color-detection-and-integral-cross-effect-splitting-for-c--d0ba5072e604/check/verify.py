"""Small independent finite-chain checks for categorical-product color cross-effects.
Run: python3 verify.py
This is a finite stress test, not a proof of the general theorem.
"""
from itertools import combinations
from collections import defaultdict


def faces(edges, n, max_size):
    nG=max(max(e) for e in edges)+1
    adj={tuple(sorted(e)) for e in edges}
    vertices=tuple((v,c) for v in range(nG) for c in range(1,n+1))
    result={k:[] for k in range(max_size+1)}
    result[0]=[()]
    for k in range(1,max_size+1):
        for face in combinations(vertices,k):
            if all(not (a!=b and tuple(sorted((v,w))) in adj) for (v,a),(w,b) in combinations(face,2)):
                result[k].append(face)
    return result

def p_face(face, i):
    return tuple(sorted(set((v,1 if c==i else c) for (v,c) in face)))

def m_map(face,i):
    original=tuple(sorted(face)); result={original:1}
    image=p_face(face,i)
    # orientation determined by mapping order; duplicates give zero in normalized simplicial chains
    mapped=[(v,1 if c==i else c) for v,c in face]
    if len(set(mapped))!=len(mapped):
        return result
    parity=sum(mapped[t]>mapped[u] for t in range(len(mapped)) for u in range(t+1,len(mapped)))%2
    result[tuple(sorted(mapped))]=result.get(tuple(sorted(mapped)),0)+(-1 if parity else 1)*(-1)
    return {k:v for k,v in result.items() if v}

def merge_map(chain,i):
    out=defaultdict(int)
    for face,c in chain.items():
        mapped=[(v,1 if col==i else col) for v,col in face]
        if len(set(mapped))!=len(mapped):continue
        parity=sum(mapped[t]>mapped[u] for t in range(len(mapped)) for u in range(t+1,len(mapped)))%2
        out[tuple(sorted(mapped))]+=c*(-1 if parity else 1)
    return {k:v for k,v in out.items() if v}

def E(chain, S, n):
    # All p commute: p outside S then (1-p) inside S.
    for j in range(2,n+1):
        if j not in S:
            chain=merge_map(chain,j)
    for i in sorted(S):
        m=merge_map(chain,i)
        out=defaultdict(int,chain)
        for f,c in m.items():out[f]-=c
        chain={f:c for f,c in out.items() if c}
    return chain

def boundary(chain):
    out=defaultdict(int)
    for f,c in chain.items():
        for i in range(len(f)):
            out[f[:i]+f[i+1:]]+=c*(-1 if i%2 else 1)
    return {k:v for k,v in out.items() if v}

def gf2_rank(rows):
    basis={}
    for r in rows:
        while r:
            p=r.bit_length()-1
            if p not in basis: basis[p]=r;break
            r^=basis[p]
    return len(basis)

def bettis(edges,n,max_degree=2):
    F=faces(edges,n,max_degree+2)
    B={}
    for k in range(1,max_degree+3):
        ids={face:i for i,face in enumerate(F[k-1])}
        cols=[]
        for f in F[k]:
            col=0
            for i in range(len(f)):
                col^=1<<ids[f[:i]+f[i+1:]]
            cols.append(col)
        B[k]=gf2_rank(cols)
    return [len(F[d+1])-B[d+1]-B[d+2] for d in range(max_degree+1)]

def main():
    graphs={
        'edge': [(0,1)],
        'triangle':[(0,1),(1,2),(0,2)],
        'path3':[(0,1),(1,2)],
        'pentagon':[(i,(i+1)%5) for i in range(5)],
    }
    tested_faces=0; tested_cones=0; reports=[]
    for name,edges in graphs.items():
        for n in range(2,5):
            F=faces(edges,n,4)
            # Verify simplicial property of every merge for faces up to dimension 3.
            FF={size:set(v) for size,v in F.items()}
            for k in range(1,5):
                for f in F[k]:
                    tested_faces+=1
                    for i in range(2,n+1):
                        img=p_face(f,i)
                        assert img in FF[len(img)],(name,n,f,i,img)
                    # Boundary commutes with projection on normalized chains.
                    for i in range(2,n+1):
                        assert boundary(merge_map({f:1},i))==merge_map(boundary({f:1}),i)
                    # E_S decomposition and orthogonality on basis chains.
                    if k<=3:
                        total=defaultdict(int)
                        for r in range(n):
                            for T in combinations(range(2,n+1),r):
                                for face,v in E({f:1},set(T),n).items():total[face]+=v
                        assert {x:c for x,c in total.items() if c}=={f:1}
                    # Top cross effect with s=k is null in H_(k-1) via explicit cone.
                    if k<=3:
                        S=set(range(2,n+1))
                        if len(S)==k and all(col in S for v,col in f) and len(set(col for v,col in f))==k:
                            assert all(tuple(sorted((v,w))) not in {tuple(sorted(e)) for e in edges} for (v,_),(w,_) in combinations(f,2))
                            v=f[0][0]
                            cone=tuple(sorted(f+((v,1),)))
                            assert cone in FF[len(cone)]
                            assert E(boundary({cone:1}),S,n)==E({f:1},S,n)
                            tested_cones+=1
            if name in ['edge','triangle','path3'] or n<=3:
                bb=bettis(edges,n)
                reports.append((name,n,bb))
    for name in ['edge','triangle','path3']:
        seq=[b for nm,n,b in reports if nm==name]
        # For H_1 the differences are linear, for H_2 quadratic in n-1.
        for d in range(1,3):
            b2,b3,b4=[b[d] for b in seq]
            alpha=b2
            gamma=b3-2*alpha
            assert b4==3*alpha+3*gamma,(name,d,seq)
            assert alpha>=0 and gamma>=0,(name,d,alpha,gamma)
            if d==1:assert gamma==0
    print('PASS face_merge_and_chain_naturality',tested_faces)
    print('PASS projected_idempotent_decomposition all low-degree test faces')
    print('PASS top_cross_effect_chain_cones',tested_cones)
    print('PASS finite_field_betti_coefficients degree_1_2',reports)

if __name__=='__main__':main()
