"""Exact, standalone checks for the four-node degree-two characteristic-imset polytope.

Python 3 standard library only. No floating-point acceptance conditions.
"""
from fractions import Fraction as F
from itertools import combinations, product
from math import isqrt

V = tuple(range(4))
PAIRS = tuple(combinations(V,2))
TRIPLES = tuple(combinations(V,3))
KEYS = PAIRS + TRIPLES
IX = {s:i for i,s in enumerate(KEYS)}


def connected(nodes, edges):
    reached={nodes[0]}
    while True:
        updated=reached|{v for e in edges if any(t in reached for t in e) for v in e}
        if updated==reached:
            return len(updated)==len(nodes)
        reached=updated


def coeff(edge_sign, edges, triple_coeff):
    a=[0]*10
    for e in edges:
        a[IX[tuple(sorted(e))]]=edge_sign
    for t,c in triple_coeff.items():
        a[IX[tuple(sorted(t))]]=c
    return tuple(a)


def facets():
    out={}
    def add(a,b,kind):
        out.setdefault((tuple(a),b),set()).add(kind)
    # Connected-graph path inequalities, source Theorem 4.6.
    for m in range(2,5):
        for nodes in combinations(V,m):
            edges=list(combinations(nodes,2))
            for bits in product((0,1),repeat=len(edges)):
                chosen={e for e,bit in zip(edges,bits) if bit}
                if not connected(nodes,chosen):
                    continue
                tc={}
                for t in combinations(nodes,3):
                    count=sum(e in chosen for e in combinations(t,2))
                    if count>=2:
                        tc[t]=2 if count==3 else 1
                add(coeff(-1,chosen,tc),0,'path')
    # Outer inequalities for degree-two-free trees, Theorem 5.2.
    for m in range(2,5):
        for nodes in combinations(V,m):
            edges=list(combinations(nodes,2))
            for chosen in combinations(edges,m-1):
                if not connected(nodes,chosen):
                    continue
                if any(sum(v in e for e in chosen)==2 for v in nodes):
                    continue
                tc={}
                for v in nodes:
                    neigh=sorted(w for e in chosen if v in e for w in e if w!=v)
                    for t in combinations(neigh,3):
                        tc[t]=1
                add(coeff(1,chosen,tc),m-1,'outer')
    # Clique inequalities, Theorem 6.3.
    for m in range(2,5):
        for nodes in combinations(V,m):
            add(coeff(1,combinations(nodes,2),{t:-1 for t in combinations(nodes,3)}),m-1,'clique')
    # Augmented triangle inequalities, Proposition 6.5.
    for nodes in combinations(V,3):
        p=next(v for v in V if v not in nodes)
        edges=list(combinations(nodes,2))
        a=list(coeff(-1,edges,{nodes:2}))
        for e in edges:
            a[IX[tuple(sorted((*e,p)))]]+=1
        add(a,1,'triangle_plus')
    # Disconnected two-plus-two clique inequalities, Theorem 6.6.
    for nodes in combinations(V,2):
        remain=tuple(v for v in V if v not in nodes)
        a=[0]*10
        a[IX[nodes]]=1
        for v in nodes:
            a[IX[tuple(sorted((v,*remain)))]]+=1
        add(a,2,'disconnected')
    # Triple-coordinate nonnegativity and rank inequalities.
    for t in TRIPLES:
        a=[0]*10;a[IX[t]]=-1
        add(a,0,'nonnegative_triple')
    for m in (3,4):
        for nodes in combinations(V,m):
            a=[0]*10
            for t in combinations(nodes,3):
                a[IX[t]]=1
            add(a,m-2,'triple_rank')
    return out


def dag_vertices():
    out=set()
    # Every undirected pair is absent or has one of its two orientations.
    for states in product((0,1,2),repeat=6):
        arcs=[]
        for (i,j),s in zip(PAIRS,states):
            if s==1: arcs.append((i,j))
            if s==2: arcs.append((j,i))
        parents=[set() for _ in range(4)]
        for i,j in arcs:parents[j].add(i)
        if any(len(s)>2 for s in parents):continue
        topo={i:0 for i in V}
        for i,j in arcs:topo[j]+=1
        ready=[i for i in V if topo[i]==0]
        visited=0
        while ready:
            v=ready.pop();visited+=1
            for i,j in arcs:
                if i==v:
                    topo[j]-=1
                    if topo[j]==0:ready.append(j)
        if visited!=4:continue
        arr=[int(s!=0) for s in states]
        for t in TRIPLES:
            arr.append(int(any(set(t)-{v}<=parents[v] for v in t)))
        out.add(tuple(arr))
    return sorted(out)


def modular_rank(rows, prime=1000003):
    basis={}
    for row in rows:
        z=[int(t)%prime for t in row]
        for pivot, old in sorted(basis.items()):
            if z[pivot]:
                c=z[pivot]
                z=[(v-c*w)%prime for v,w in zip(z,old)]
        piv=next((i for i,t in enumerate(z) if t),None)
        if piv is None:continue
        inv=pow(z[piv],-1,prime)
        basis[piv]=[(v*inv)%prime for v in z]
    return len(basis)


def root_bracket(n, scale=10**10):
    j=isqrt(n*scale*scale)
    return F(j,scale),F(j+1,scale)


def exact_interval_certificates(facet_map):
    s22_l,s22_u=root_bracket(22)
    s10_l,s10_u=root_bracket(10)
    r_l=3/(4+s22_u+s10_u);r_u=3/(4+s22_l+s10_l)
    t_l=(8+s22_l)*r_l/6;t_u=(8+s22_u)*r_u/6
    active={(-6,8,22,0),(6,-4,10,3),(0,-1,1,0)}
    counts={};least=None
    for (a,b),names in facet_map.items():
        e=sum(a[:6]);u=sum(a[6:]);norm2=sum(x*x for x in a)
        sig=(e,u,norm2,b)
        counts[sig]=counts.get(sig,0)+1
        if sig in active:continue
        _,sq_u=root_bracket(norm2)
        # Exact, rational lower bound on b - e*t - u*r - r*||a||.
        lower=F(b)-F(e)*(t_u if e>0 else t_l)-F(u)*(r_u if u>0 else r_l)-(r_u+F(9,200))*sq_u
        assert lower>0,(sig,lower)
        if least is None or lower<least[0]:least=(lower,sig)
    assert sum(counts[x] for x in active)==6
    return r_l,r_u,t_l,t_u,least,counts


def main():
    fs=facets(); assert len(fs)==94
    vs=dag_vertices(); assert len(vs)==150
    assert modular_rank([(*v,1) for v in vs])==11
    for (a,b) in fs:
        tight=[(*v,1) for v in vs if sum(x*y for x,y in zip(a,v))==b]
        assert all(sum(x*y for x,y in zip(a,v))<=b for v in vs)
        assert modular_rank(tight)==10, (a,b,len(tight))
    rl,ru,tl,tu,least,counts=exact_interval_certificates(fs)
    assert len(counts)==18
    print('PASS 94 distinct complete-source inequalities; 150 distinct DAG imsets; ambient affine rank 11.')
    print('PASS every inequality valid on every vertex and facet-tight vertex affine rank 10.')
    print('PASS exact rational enclosures of radical center and positive gaps for 88 noncontact facets.')
    print('r bracket',float(rl),float(ru),'edge-center bracket',float(tl),float(tu))
    print('smallest exact clearance above 9/200 radii, unnormalized lower bound',str(least[0]),'facet orbit',least[1], 'decimal',float(least[0]))
    print('18 orbits (edge coefficient sum, triple coefficient sum, squared norm, right side):')
    for sig,n in sorted(counts.items()):print(sig,n)

if __name__=='__main__':main()
