#!/usr/bin/env python3
"""Exact checks for the integral multipath homology of both six-vertex cubic graphs.

Standard-library only. Run: python3 verify_six_cubic.py [certificate.json]
"""
import sys, json, collections, itertools, fractions
from pathlib import Path

EXPECTED = {
    'triangular_prism': {'faces': 687, 'f_vector': [18,108,260,240,60], 'pairs': 323,
                         'hasse': 2274, 'critical': {'2': 9, '3': 26, '4': 6},
                         'ranks': {'3': 4, '4': 0}, 'homology': {'2': 5, '3': 22, '4': 6},
                         'unit_minor': {'rows': [0,1,4,5], 'cols':[4,9,10,13], 'det':-1}},
    'K33': {'faces':715,'f_vector':[18,108,264,252,72],'pairs':336,'hasse':2394,
            'critical':{'2':6,'3':25,'4':12},'ranks':{'3':6,'4':0},
            'homology':{'3':19,'4':12},
            'unit_minor':{'rows':[0,1,2,3,4,5],'cols':[0,1,5,9,14,19],'det':-1}},
}


def base_graph(name):
    if name == 'triangular_prism':
        E = [(i,j) for t in [0,3] for i in range(t,t+3) for j in range(i+1,t+3)]
        E += [(i,i+3) for i in range(3)]
    elif name == 'K33':
        E = [(i,j) for i in range(3) for j in range(3,6)]
    else:
        raise ValueError(name)
    assert len(E)==9
    assert sorted(sum((v in edge) for edge in E) for v in range(6))==[3]*6
    return E


def directed_arcs(E):
    return [(u,v) for a,b in E for u,v in ((a,b),(b,a))]


def is_multipath_by_successor(mask,arcs):
    succ=[-1]*6; indeg=[0]*6
    for j,(u,v) in enumerate(arcs):
        if mask>>j&1:
            if succ[u]!=-1 or indeg[v]: return False
            succ[u]=v; indeg[v]=1
    for u in range(6):
        v=succ[u]
        while v>=0:
            if v==u:return False
            v=succ[v]
    return True


def is_multipath_by_union_find(mask,arcs):
    parent=list(range(6)); inc=[0]*6; out=[0]*6
    def root(i):
        while parent[i]!=i:
            i=parent[i]
        return i
    for j,(u,v) in enumerate(arcs):
        if not mask>>j&1:continue
        inc[v]+=1;out[u]+=1
        if inc[v]>1 or out[u]>1:return False
        a,b=root(u),root(v)
        if a==b:return False
        parent[a]=b
    return True


def all_faces(arcs):
    # Independent direct enumeration plus monotone-first enumeration.
    F={0}
    for mask in range(1,1<<len(arcs)):
        first=mask&-mask
        if (mask^first) in F and is_multipath_by_successor(mask,arcs):
            F.add(mask)
    F2={mask for mask in range(1<<len(arcs)) if is_multipath_by_union_find(mask,arcs)}
    assert F==F2
    return F


def greedy_matching(F,m,reverse=False):
    remaining=set(F);pairs=[]
    for j in (range(m-1,-1,-1) if reverse else range(m)):
        bit=1<<j
        uppers=sorted((mask|bit) for mask in remaining
                      if not(mask&bit) and (mask|bit) in remaining)
        for upper in uppers:
            lower=upper^bit
            if lower in remaining and upper in remaining:
                remaining.remove(lower);remaining.remove(upper)
                pairs.append((lower,upper))
    return remaining,pairs


def check_acyclic(F,pairs):
    paired=set(pairs)
    out=collections.defaultdict(list)
    indeg={u:0 for u in F}
    edges=0
    for upper in F:
        t=upper
        while t:
            bit=t&-t; t-=bit
            lower=upper^bit
            a,b=(lower,upper) if (lower,upper) in paired else (upper,lower)
            out[a].append(b);indeg[b]+=1;edges+=1
    q=collections.deque(u for u,d in indeg.items() if d==0)
    visited=0
    while q:
        u=q.popleft();visited+=1
        for v in out[u]:
            indeg[v]-=1
            if indeg[v]==0:q.append(v)
    assert visited==len(F), (visited,len(F))
    return edges


def reduced_morse_boundary(F,pairs):
    # Signed simplicial boundaries with the empty face in degree minus one.
    bd={u:{u^(1<<j):(-1 if (u&((1<<j)-1)).bit_count()%2 else 1)
            for j in range(u.bit_length()) if u>>j&1} for u in F}
    alive=set(F)
    row=collections.defaultdict(set)
    for upper,lower_list in bd.items():
        for lower in lower_list:row[lower].add(upper)
    for lower,upper in pairs:
        assert lower in alive and upper in alive
        pivot=bd[upper].get(lower)
        assert pivot in (-1,1), (lower,upper,pivot)
        for other in list(row[lower]):
            if other==upper:continue
            q=bd[other].get(lower,0)
            if not q:continue
            mult=q*pivot
            for a,c in bd[upper].items():
                val=bd[other].get(a,0)-mult*c
                if val:
                    bd[other][a]=val;row[a].add(other)
                else:
                    bd[other].pop(a,None);row[a].discard(other)
        for other in list(row[upper]):
            bd[other].pop(upper,None)
        for c in bd[upper]:row[c].discard(upper)
        for c in bd[lower]:row[c].discard(lower)
        del bd[upper];del bd[lower]
        alive.remove(lower);alive.remove(upper)
        row.pop(lower,None);row.pop(upper,None)
    groups=collections.defaultdict(list)
    for u in alive:groups[u.bit_count()-1].append(u)
    for arr in groups.values():arr.sort()
    matrices={}
    for degree in range(max(groups)+1):
        col=groups.get(degree,[]); row_cells=groups.get(degree-1,[])
        ri={r:i for i,r in enumerate(row_cells)}
        matrix=[[0]*len(col) for _ in row_cells]
        for j,cell in enumerate(col):
            for lower,v in bd[cell].items():
                assert lower in ri
                matrix[ri[lower]][j]=v
        matrices[degree]=matrix
    for d in matrices:
        if not d or d-1 not in matrices:continue
        A=matrices[d-1]; B=matrices[d]
        if not A or not B:continue
        assert len(A[0])==len(B)
        for r in range(len(A)):
            for c in range(len(B[0])):
                assert sum(A[r][j]*B[j][c] for j in range(len(B)))==0
    return {str(k):len(v) for k,v in sorted(groups.items()) if v}, matrices


def integer_rank(M):
    if not M:return 0
    A=[[fractions.Fraction(v) for v in row] for row in M]
    rows=len(A); cols=len(A[0]); rank=0
    for c in range(cols):
        found=next((i for i in range(rank,rows) if A[i][c]!=0),None)
        if found is None:continue
        A[rank],A[found]=A[found],A[rank]
        pivot=A[rank][c]
        for i in range(rank+1,rows):
            if A[i][c]:
                f=A[i][c]/pivot
                for j in range(c,cols):A[i][j]-=f*A[rank][j]
        rank+=1
        if rank==rows:break
    return rank


def determinant(M):
    n=len(M)
    assert all(len(row)==n for row in M)
    if not n:return 1
    # fraction-free Bareiss elimination
    A=[r[:] for r in M];sign=1;den=1
    for k in range(n-1):
        if A[k][k]==0:
            idx=next((i for i in range(k+1,n) if A[i][k]),None)
            if idx is None:return 0
            A[k],A[idx]=A[idx],A[k];sign=-sign
        p=A[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                value=A[i][j]*p-A[i][k]*A[k][j]
                assert value%den==0
                A[i][j]=value//den
            A[i][k]=0
        den=p
    return sign*A[-1][-1]


def modp_boundary_ranks(F,p):
    # Independent original signed simplicial boundary matrices.
    by_dim=collections.defaultdict(list)
    for f in F:by_dim[f.bit_count()-1].append(f)
    for L in by_dim.values():L.sort()
    ranks={}
    for dim in range(0,max(by_dim)+1):
        L=by_dim[dim]
        target={f:i for i,f in enumerate(by_dim[dim-1])}
        basis={}
        for f in L:
            coeffs={}
            for j in range(f.bit_length()):
                if not f>>j&1:continue
                s=f^(1<<j)
                k=target[s]; coeffs[k]=(-1 if (f&((1<<j)-1)).bit_count()%2 else 1)%p
            while coeffs:
                k=min(coeffs)
                if k not in basis:
                    inverse=pow(coeffs[k],-1,p)
                    basis[k]={i:(v*inverse)%p for i,v in coeffs.items()}
                    break
                v=coeffs[k]
                for i,a in basis[k].items():
                    value=(coeffs.get(i,0)-v*a)%p
                    if value:coeffs[i]=value
                    else:coeffs.pop(i,None)
        ranks[dim]=len(basis)
    hom={}
    for d in range(0,max(by_dim)+1):
        beta=len(by_dim[d])-ranks[d]-ranks.get(d+1,0)
        if beta:hom[str(d)]=beta
    return hom,ranks


def check(name,create_cert=False):
    exp=EXPECTED[name]
    arcs=directed_arcs(base_graph(name))
    F=all_faces(arcs)
    assert len(F)==exp['faces']
    fvec=[sum(f.bit_count()==d+1 for f in F) for d in range(5)]
    assert fvec==exp['f_vector']
    assert max(f.bit_count() for f in F)==5
    results=[]
    for rev in [False,True]:
        critical,pairs=greedy_matching(F,len(arcs),rev)
        assert len(pairs)==exp['pairs']
        incidences=check_acyclic(F,pairs)
        assert incidences==exp['hasse']
        cv,mats=reduced_morse_boundary(F,pairs)
        assert cv==exp['critical']
        ranks={str(d):integer_rank(M) for d,M in mats.items() if d>=3}
        assert ranks==exp['ranks'], (name,rev,ranks)
        assert all(not any(M[r][c] for r in range(len(M)) for c in range(len(M[0]) if M else 0))
                   for d,M in mats.items() if d==4)
        hom={}
        for d,count in cv.items():
            k=int(d)
            beta=count - integer_rank(mats.get(k,[])) - integer_rank(mats.get(k+1,[]))
            if beta:hom[d]=beta
        assert hom==exp['homology'],(hom,exp['homology'])
        if not rev:
            unit=exp['unit_minor']; B=mats[3]
            sub=[[B[i][j] for j in unit['cols']] for i in unit['rows']]
            assert determinant(sub)==unit['det']
        results.append({'order':'descending' if rev else 'ascending',
                        'critical':cv,'boundary_matrices':{str(d):M for d,M in mats.items() if d in [3,4]},
                        'ranks':ranks,'homology':hom})
    for p in [2,3]:
        hom,br=modp_boundary_ranks(F,p)
        assert hom==exp['homology'],(name,p,hom)
    return {'graph':name,'arcs':[list(a) for a in arcs],'f_vector':fvec,'faces_with_empty':len(F),
            'hasse_incidences':incidences,'matching_pairs':len(pairs),
            'morse':results,'unimodular_minor':exp['unit_minor'],
            'mod_2_and_mod_3_homology':exp['homology']}


def main():
    actual={name:check(name) for name in EXPECTED}
    if len(sys.argv)>1:
        cert=json.loads(Path(sys.argv[1]).read_text(encoding='utf-8'))
        assert cert==actual, 'Stored matrix certificate differs from reconstructed one'
    else:
        print(json.dumps(actual,separators=(',',':'),sort_keys=True))
    for name,r in actual.items():
        print('VERIFIED',name,'faces',r['faces_with_empty'],'incidences',r['hasse_incidences'],
              'pairs',r['matching_pairs'],'integral reduced homology',EXPECTED[name]['homology'])
    print('SIX_VERTEX_CUBIC_MULTIPATH_INTEGRAL_HOMOLOGY_VERIFIED')

if __name__=='__main__':main()
