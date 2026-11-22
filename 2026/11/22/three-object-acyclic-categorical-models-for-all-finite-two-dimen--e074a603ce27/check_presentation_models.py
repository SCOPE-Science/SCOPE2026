"""Exact finite checks for three-object categorical presentation models.

Input relators are lists of signed integers, e.g. [[1,2,-1,-2]].
No external input or network access is used. Optional SymPy supplies Smith normal form
for the finite sample invariants, not for the general topological proof.
"""
from collections import Counter, defaultdict


def model(k, words):
    assert k >= 1 and words
    words = [w if w else [1, -1] for w in words]
    assert all(0 < abs(x) <= k for w in words for x in w)
    L=sum(map(len,words)); s=len(words)
    f={}; cyc={'c*'}; b_ids=[]; witnesses=[]
    for ri, word in enumerate(words):
        mid=[f'c{ri}.{p}' for p in range(1,len(word))]
        cc=['c*']+mid+['c*']
        for j, signed in enumerate(word):
            b=f'b{ri}.{j}'; b_ids.append(b)
            a=abs(signed)
            if signed>0:
                f[a,b]=cc[j]; f[0,b]=cc[j+1]
                witnesses.append((cc[j],b,cc[j+1],a,0,signed))
            else:
                f[0,b]=cc[j]; f[a,b]=cc[j+1]
                witnesses.append((cc[j],b,cc[j+1],0,a,signed))
            cyc.update((cc[j],cc[j+1]))
            for m in range(1,k+1):
                if m!=a:
                    leaf=f'leaf{ri}.{j}.{m}'
                    f[m,b]=leaf; cyc.add(leaf)
    c_ids=sorted(cyc)
    assert len(f)==(k+1)*L
    assert len(c_ids)==k*L-s+1
    E=(k+1)+len(b_ids)+len(c_ids)
    assert 3-E+len(f)==1-k+s
    edges=[('a',i) for i in range(k+1)]+[('b',b) for b in b_ids]+[('c',c) for c in c_ids]
    edge_index={e:i for i,e in enumerate(edges)}
    E2=sorted(f)
    # Cellular differential of [a,b] = [b]-[f(a,b)]+[a].
    d2=[]
    for a,b in E2:
        col=[0]*E
        col[edge_index['a',a]]+=1
        col[edge_index['b',b]]+=1
        col[edge_index['c',f[a,b]]]-=1
        d2.append(col)
        # ∂1∂2=0, orientations a:0->1, b:1->2, c:0->2.
        assert all(sum(col[i] * ({'a':(-1,1,0),'b':(0,-1,1),'c':(-1,0,1)}[edges[i][0]][v]) for i in range(E))==0 for v in range(3))
    # The incidence graph Γ has c and b vertices, and one edge (a,b) for each table entry.
    V=set(('c',c) for c in c_ids)|set(('b',b) for b in b_ids)
    nbr=defaultdict(set)
    for (a,b),c in f.items():
        nbr['b',b].add(('c',c)); nbr['c',c].add(('b',b))
    seen={next(iter(V))}; frontier=list(seen)
    while frontier:
        z=frontier.pop()
        for y in nbr[z]:
            if y not in seen:seen.add(y);frontier.append(y)
    assert seen==V, 'Γ is disconnected'
    beta=len(f)-len(V)+1
    assert beta==s,(beta,s)
    decoded=[]
    for v,b,w,a1,a2,signed in witnesses:
        # Collapse a_0 to tree; path cprev->b->cnext becomes a1 * a2^-1.
        pair=([a1] if a1 else [])+([-a2] if a2 else [])
        assert pair==[signed]
        decoded+=pair
    assert decoded==[x for w in words for x in w]
    # Present H1 from non-tree edges, where tree edges are a0 and the first b.
    tree={edge_index['a',0],edge_index['b',b_ids[0]]}
    P=[[col[i] for col in d2] for i in range(E) if i not in tree]
    return {'k':k,'s':s,'L':L,'E1':E,'E2':len(E2),'C':len(c_ids),'chi':3-E+len(E2),
            'gamma_vertices':len(V),'gamma_edges':len(f),'gamma_cycle_rank':beta,
            'map':f,'boundary_presentation':P, 'words':words}


def snf_invariants(M):
    from sympy import Matrix,ZZ
    from sympy.matrices.normalforms import smith_normal_form
    S=smith_normal_form(Matrix(M),domain=ZZ)
    nonzero=[abs(int(S[i,i])) for i in range(min(S.rows,S.cols)) if S[i,i]]
    return len(nonzero),[i for i in nonzero if i!=1]


def check_examples():
    examples=[('projective_plane',1,[[1,1]],0,[2],0),
              ('klein_bottle',2,[[1,2,1,-2]],1,[2],0),
              ('torus',2,[[1,2,-1,-2]],2,[],1),
              ('moore_3',1,[[1,1,1]],0,[3],0),
              ('sphere_with_canceling_pair',1,[[1],[]],0,[],1),
              ('pair_of_relators',2,[[1,1],[2,2]],0,[2,2],0),
              ('free_circle_plus_sphere',2,[[]],2,[],1),
              ('nonorientable_genus_3',3,[[1,1,2,2,3,3]],2,[2],0)]
    for title,k,words,free,torsion,betti2 in examples:
        d=model(k,words)
        rank,tor=snf_invariants(d['boundary_presentation'])
        assert len(d['boundary_presentation'])-rank==free,(title,'b1',len(d['boundary_presentation'])-rank,free)
        assert sorted(tor)==sorted(torsion),(title,'torsion',tor,torsion)
        assert d['E2']-rank==betti2,(title,'b2',d['E2']-rank,betti2)
        print(title, 'shape:',(d['E1'],d['E2']), 'Γb1:',d['gamma_cycle_rank'], 'H1:',(free,tor),'H2:',betti2)
    print('PASS all explicit composition/graph/chain/Smith sample checks')

if __name__=='__main__':check_examples()
