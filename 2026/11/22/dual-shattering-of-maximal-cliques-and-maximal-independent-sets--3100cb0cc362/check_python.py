"""Independent verification using maximal-clique enumeration and binary simplicial chains.
Run: python3 check_python.py ; requires networkx >=2.8.
All sets use 16-bit incidence masks; no external data or random choices.
"""
import itertools
import networkx as nx

def adjacency(kind):
    G=nx.Graph();G.add_nodes_from(range(16))
    for u,v in itertools.combinations(range(16),2):
        x,y=divmod(u,4);a,b=divmod(v,4)
        if kind=='rook': edge=(x==a or y==b)
        else:
            d=((x-a)%4,(y-b)%4)
            edge=d in {(1,0),(3,0),(0,1),(0,3),(1,1),(3,3)}
        if edge:G.add_edge(u,v)
    return G

def sets_as_masks(sets):
    return sorted(sum(1<<v for v in s) for s in sets)

def shattered(concepts):
    out=set()
    # No support above four can be all-positive for this instance.
    for k in range(5):
        for tup in itertools.combinations(range(16),k):
            s=sum(1<<v for v in tup)
            if len({s&c for c in concepts})==1<<k:out.add(s)
    return out

def f_vector(ss):
    return tuple(sum(s.bit_count()==k for s in ss) for k in range(5))

def gf2rank(cols):
    basis={}
    for v in cols:
        while v:
            b=v.bit_length()-1
            if b not in basis:
                basis[b]=v;break
            v^=basis[b]
    return len(basis)

def homology(ss):
    faces=[sorted(s for s in ss if s.bit_count()==k) for k in range(5)]
    ranks=[]
    for k in range(1,5):
        ind={s:i for i,s in enumerate(faces[k-1])}
        cols=[]
        for s in faces[k]:
            col=0
            for v in range(16):
                if s>>v&1:col^=1<<ind[s^(1<<v)]
            cols.append(col)
        ranks.append(gf2rank(cols))
    return {k-1:len(faces[k])-ranks[k-1]-(ranks[k] if k<4 else 0) for k in range(1,5)},ranks

def run():
    for label in ('rook','shrikhande'):
        G=adjacency('rook' if label=='rook' else 'shrikhande')
        assert sorted(dict(G.degree()).values())==[6]*16
        assert all(len(set(G.neighbors(i))&set(G.neighbors(j)))==2 for i,j in itertools.combinations(G.nodes,2))
        C=sets_as_masks(nx.find_cliques(G))
        I=sets_as_masks(nx.find_cliques(nx.complement(G)))
        CS=shattered(C);IS=shattered(I)
        triple_I={s for s in range(1<<16) if s.bit_count()==3 and all(not G.has_edge(u,v) for u,v in itertools.combinations([v for v in range(16) if s>>v&1],2))}
        assert IS=={s for s in range(1<<16) if s.bit_count()<=2 and all(not G.has_edge(u,v) for u,v in itertools.combinations([v for v in range(16) if s>>v&1],2))}|triple_I
        assert len(triple_I)==96
        hf,br=homology(IS)
        assert f_vector(IS)==(1,16,72,96,0)
        assert br[0]==1 and br[1]==15 and br[2]==57
        assert hf[1]==0 and hf[2]==39
        print(label, 'maximal_cliques',len(C),'maximal_independent_sets',len(I))
        print(label, 'clique_shattering_f',f_vector(CS),'independent_shattering_f',f_vector(IS))
        print(label, 'independent_mod2_betti',hf,'boundary_ranks',br)
        if label=='rook':
            assert f_vector(CS)==(1,16,48,0,0)
            assert CS=={0}|{1<<v for v in range(16)}|{(1<<u)|(1<<v) for u,v in G.edges}
            assert homology(CS)[0][1]==33
        else:
            assert f_vector(CS)==(1,16,48,32,0)
            triangles={s for s in range(1<<16) if s.bit_count()==3 and all(G.has_edge(u,v) for u,v in itertools.combinations([v for v in range(16) if s>>v&1],2))}
            assert len(triangles)==32 and CS=={0}|{1<<v for v in range(16)}|{(1<<u)|(1<<v) for u,v in G.edges}|triangles
            HC,brC=homology(CS)
            assert HC[1]==2 and HC[2]==1 and brC[2]==31
            print(label,'clique_mod2_betti',HC)
    print('INDEPENDENT_GRAPH_CLIQUE_SHATTER_PASS')
if __name__=='__main__':run()
