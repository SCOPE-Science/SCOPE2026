#!/usr/bin/env python3
"""Exact integral chain certificate for the second forest-filtration complexes
of the Shrikhande and 4x4 rook graphs. Requires SymPy >= 1.11.

Run: python verify.py [--certificate path-to-json]
Face sets are reconstructed exhaustively; the second face test, two pivot
orders, complete acyclicity checks, and full mod-two boundary ranks check
separate aspects of the computation.
"""
import json
import sys
from collections import Counter, defaultdict
from functools import lru_cache
from sympy import Matrix, ZZ
from sympy.matrices.normalforms import smith_normal_form

N = 16
STEPS = {(1,0),(3,0),(0,1),(0,3),(1,1),(3,3)}

def graph(name):
    adjacency = [0]*N
    edges = []
    for i in range(N):
        a,b = divmod(i,4)
        for j in range(i+1,N):
            c,d = divmod(j,4)
            linked = (a==c or b==d) if name=='rook' else (((c-a)%4,(d-b)%4) in STEPS)
            if linked:
                edges.append((i,j))
                adjacency[i] |= 1<<j
                adjacency[j] |= 1<<i
    assert len(edges)==48
    assert all(z.bit_count()==6 for z in adjacency)
    for i in range(N):
        for j in range(i+1,N):
            common = (adjacency[i]&adjacency[j]).bit_count()
            assert common == 2 # (16,6,2,2), whether adjacent or not.
    return adjacency,edges

def face_dsu(mask,edges):
    """Direct cycle detection with union-find and degree count."""
    parent=list(range(N));degree=[0]*N
    def root(x):
        while parent[x]!=x:x=parent[x]
        return x
    for u,v in edges:
        if mask&(1<<u) and mask&(1<<v):
            degree[u]+=1;degree[v]+=1
            if degree[u]>2 or degree[v]>2:return False
            x,y=root(u),root(v)
            if x==y:return False
            parent[x]=y
    return True

def face_dfs(mask,adjacency):
    """Independent predicate: component count + edge count = vertex count."""
    seen=0;components=0;double_edges=0
    for v in range(N):
        if mask&(1<<v):
            neighbors=mask&adjacency[v]
            if neighbors.bit_count()>2:return False
            double_edges+=neighbors.bit_count()
            if not seen&(1<<v):
                components+=1; stack=[v];seen|=1<<v
                while stack:
                    u=stack.pop()
                    new=adjacency[u]&mask&~seen
                    while new:
                        bit=new&-new;w=bit.bit_length()-1
                        seen|=bit;stack.append(w);new-=bit
    assert double_edges%2==0
    return double_edges//2+components==mask.bit_count()

def all_faces(adjacency,edges):
    fs=[]
    for mask in range(1<<N):
        a=face_dsu(mask,edges)
        b=face_dfs(mask,adjacency)
        assert a==b,(mask,a,b)
        if a:fs.append(mask)
    return fs

def boundary(cell):
    bits=[v for v in range(N) if cell & (1<<v)]
    return [(cell^(1<<v),-1 if i%2 else 1) for i,v in enumerate(bits)]

def lex_matching(faces,order):
    unmatched=set(faces)
    lower_to_upper={}
    for v in order:
        bit=1<<v
        for low in list(unmatched):
            high=low|bit
            if not(low&bit) and high in unmatched:
                lower_to_upper[low]=high
                unmatched.remove(low);unmatched.remove(high)
    assert len(lower_to_upper)*2+len(unmatched)==len(faces)
    assert len(set(lower_to_upper.values()))==len(lower_to_upper)
    return lower_to_upper,unmatched

def acyclicity(faces,pairs):
    """Orient each face-cover arrow downward, except matched arrows upward."""
    domain=set(faces)
    assert len(domain)==len(faces)
    indeg={f:0 for f in faces};nexts=defaultdict(list);arrows=0
    for high in faces:
        if not high:continue
        for low,_ in boundary(high):
            assert low in domain
            if pairs.get(low)==high:src,dst=low,high
            else:src,dst=high,low
            nexts[src].append(dst);indeg[dst]+=1;arrows+=1
    stack=[c for c in faces if indeg[c]==0];seen=0
    while stack:
        c=stack.pop();seen+=1
        for dst in nexts[c]:
            indeg[dst]-=1
            if indeg[dst]==0:stack.append(dst)
    assert seen==len(faces),('directed gradient cycle',seen,len(faces))
    return arrows

def morse_matrices(pairs,critical):
    # The projection follows alternating gradient paths of fixed dimension.
    # All matched incidence numbers are +-1, hence each reduction is integral.
    rev={high:low for low,high in pairs.items()}
    cells=defaultdict(list)
    for c in critical:cells[c.bit_count()-1].append(c)
    for dim in cells:cells[dim].sort()
    @lru_cache(None)
    def projection(low):
        if low in critical:return {low:1}
        if low in rev:return {}
        high=pairs[low]
        pivot=next(a for face,a in boundary(high) if face==low)
        assert abs(pivot)==1
        out=defaultdict(int)
        for face,coef in boundary(high):
            if face==low:continue
            for target,m in projection(face).items():
                out[target]-=pivot*coef*m
        return {target:m for target,m in out.items() if m}
    matrices={}
    for dim in sorted(cells):
        if dim<0:continue
        rows=cells[dim-1];columns=cells[dim]
        lookup={t:i for i,t in enumerate(rows)}
        matrix=[[0]*len(columns) for _ in rows]
        for j,cell in enumerate(columns):
            accum=defaultdict(int)
            for face,sign in boundary(cell):
                for target,m in projection(face).items():accum[target]+=sign*m
            for target,m in accum.items():
                assert target in lookup
                matrix[lookup[target]][j]=m
        matrices[dim]=matrix
    for d in matrices:
        if d-1 not in matrices:continue
        A=matrices[d-1];B=matrices[d]
        if A and B:
            assert all(sum(A[i][j]*B[j][k] for j in range(len(B)))==0
                       for i in range(len(A)) for k in range(len(B[0])))
    return cells,matrices

def smith_diagonal(matrix):
    if not matrix or not matrix[0]:return []
    S=smith_normal_form(Matrix(matrix),domain=ZZ)
    return sorted(abs(int(S[i,i])) for i in range(min(S.shape)) if S[i,i]!=0)

def gf2_rank(columns):
    basis={}
    for x in columns:
        while x:
            p=x.bit_length()-1
            if p in basis:x^=basis[p]
            else:basis[p]=x;break
    return len(basis)

def full_gf2_homology(faces):
    bydim=defaultdict(list)
    for f in faces:
        if f:bydim[f.bit_count()-1].append(f)
    boundary_rank={}
    for d in range(1,max(bydim)+1):
        lower={f:i for i,f in enumerate(bydim[d-1])}
        cols=[]
        for f in bydim[d]:
            x=0
            for g,_ in boundary(f):x^=1<<lower[g]
            cols.append(x)
        boundary_rank[d]=gf2_rank(cols)
    betti={d:len(bydim[d])-boundary_rank.get(d,0)-boundary_rank.get(d+1,0)
           for d in bydim}
    betti[0]-=1
    return boundary_rank,betti

def theorem_betti(name):
    if name=='rook':return {5:33,6:72}
    return {4:9,5:6,6:36}

def main():
    certificate={}
    for name in ('rook','shrikhande'):
        adjacency,edges=graph(name)
        fs=all_faces(adjacency,edges)
        assert len(fs)==(6521 if name=='rook' else 5945)
        counts=Counter(f.bit_count()-1 for f in fs)
        expected=([-1,0,1,2,3,4,5,6],[1,16,120,528,1392,2160,1728,576]) if name=='rook' else ([-1,0,1,2,3,4,5,6],[1,16,120,528,1408,2064,1424,384])
        assert [counts[d] for d in expected[0]]==expected[1]
        reduced_chi=sum((-1 if d % 2 else 1)*v for d,v in counts.items())
        assert reduced_chi==39
        ranks,mod2=full_gf2_homology(fs)
        print(name,'f_vector',[counts[d] for d in expected[0]],'reduced_euler',reduced_chi)
        print(name,'full_boundary_ranks_mod2',ranks)
        print(name,'reduced_betti_mod2',mod2)
        cert=[]
        for tag,order in (('forward',list(range(N))),('reverse',list(range(N-1,-1,-1)))):
            pairs,critical=lex_matching(fs,order)
            incidences=acyclicity(fs,pairs)
            cells,mats=morse_matrices(pairs,critical)
            sm={d:smith_diagonal(M) for d,M in mats.items()}
            critical_counts={d:len(v) for d,v in cells.items() if v}
            assert incidences==(32608 if name=='rook' else 29024)
            assert len(pairs)==(3204 if name=='rook' else 2934)
            assert critical_counts==({4:4,5:37,6:72} if name=='rook' else {4:22,5:19,6:36})
            assert sm[5]==([1]*4 if name=='rook' else [1]*12+[2])
            assert sm[6]==[]
            free={}
            for d,crit in critical_counts.items():
                lower_rank=len(sm.get(d,[]))
                higher_rank=len(sm.get(d+1,[]))
                free[d]=crit-lower_rank-higher_rank
            assert {d:k for d,k in free.items() if k}==theorem_betti(name)
            torsion={d-1:[x for x in inv if x!=1] for d,inv in sm.items() if any(x!=1 for x in inv)}
            assert torsion==({} if name=='rook' else {4:[2]})
            predicted={d:free.get(d,0)+len(torsion.get(d,[]))+len(torsion.get(d-1,[])) for d in range(7)}
            assert all(predicted.get(d,0)==mod2.get(d,0) for d in mod2)
            print(name,tag,'matching_pairs',len(pairs),'hasse_arrows',incidences,
                  'critical',critical_counts,'smith',sm,'free_ranks',free,'torsion',torsion)
            cert.append({'order':tag,'matched_pairs':len(pairs),'hasse_incidences':incidences,
                         'critical_cells':critical_counts,'smith_diagonals':sm,
                         'morse_boundaries':mats})
        certificate[name]={'f_vector':{str(k):counts[k] for k in expected[0]},
                            'mod2_boundary_ranks':ranks,'mod2_betti':mod2,
                            'morse_certificates':cert}
    if len(sys.argv)>1:
        assert len(sys.argv)==3 and sys.argv[1] in ('--write-certificate','--check-certificate')
        filename=sys.argv[2]
        if sys.argv[1]=='--write-certificate':
            with open(filename,'w',encoding='utf8') as fh:
                json.dump(certificate,fh,sort_keys=True,separators=(',',':'),ensure_ascii=False)
                fh.write('\n')
        else:
            with open(filename,encoding='utf8') as fh:prior=json.load(fh)
            assert prior==json.loads(json.dumps(certificate))
    print('FOREST_LEVEL_TWO_SHRIKHANDE_ROOK_INTEGRAL_CERTIFICATE_PASS')

if __name__=='__main__':main()
