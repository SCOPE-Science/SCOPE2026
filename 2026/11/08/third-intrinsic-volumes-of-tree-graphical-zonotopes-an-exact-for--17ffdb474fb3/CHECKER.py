"""Independent finite arithmetic checks for third intrinsic volumes of tree graphical zonotopes.
Run: python checker.py; dependency: networkx>=3.0,<4.0.
No sampling claim is used in the mathematical proof.
"""
from collections import Counter
from itertools import combinations
from math import comb, sqrt, isclose
import networkx as nx

def count(T):
    E = [tuple(e) for e in T.edges()]
    n = T.number_of_nodes()
    m = len(E)
    M2 = sum(set(a).isdisjoint(b) for a, b in combinations(E, 2))
    M3 = 0
    P4 = 0
    triple_types = [0, 0, 0]  # connected, two-component, three-component
    det_checks = 0
    for triple in combinations(E, 3):
        H = nx.Graph()
        H.add_edges_from(triple)
        components = [len(c) for c in nx.connected_components(H)]
        triple_types[len(components)-1] += 1
        if len(components)==3:
            M3 += 1
        if len(components)==1 and max(dict(H.degree()).values())==2:
            P4 += 1
        A = []
        for x,y in triple:
            v=[0]*n; v[x]=1; v[y]=-1; A.append(v)
        g = [[sum(u[t]*v[t] for t in range(n)) for v in A] for u in A]
        det = (g[0][0]*(g[1][1]*g[2][2]-g[1][2]*g[2][1])
               -g[0][1]*(g[1][0]*g[2][2]-g[1][2]*g[2][0])
               +g[0][2]*(g[1][0]*g[2][1]-g[1][1]*g[2][0]))
        expected = {1:4,2:6,3:8}[len(components)]
        assert det == expected, (n,E,triple,det,expected)
        det_checks += 1
    p,c,q = triple_types
    D = (m-2)*M2-P4
    assert 2*c == D-3*M3
    assert 2*p == 2*comb(m,3)-D+M3
    assert M2 == comb(m,2)-sum(comb(deg,2) for _,deg in T.degree())
    assert p+c+q == comb(m,3)
    alpha=(sqrt(6)-2)/2
    beta=1+2*sqrt(2)-3*sqrt(6)/2
    direct=2*p+sqrt(6)*c+2*sqrt(2)*q
    reduced=2*comb(m,3)+alpha*D+beta*M3
    assert isclose(direct,reduced,rel_tol=1e-12,abs_tol=1e-10)
    return direct, det_checks, M2, M3, P4, triple_types

def spider(lengths):
    G=nx.Graph(); i=1
    for length in lengths:
        v=0
        for _ in range(length):
            G.add_edge(v,i);v=i;i+=1
    return G

def main():
    cnt=0; tr=0; strict=0
    for n in range(6,12):
        star=count(nx.star_graph(n-1))
        path=count(nx.path_graph(n))
        assert star[5] == [comb(n-1,3),0,0]
        assert path[5] == [n-3,(n-3)*(n-4),comb(n-3,3)]
        assert star[0] < path[0]
        for T in nx.generators.nonisomorphic_trees(n):
            val, tcount, M2, M3, P4, parts = count(T)
            cnt+=1;tr+=tcount
            assert star[0]-1e-10 <= val <= path[0]+1e-10, (n,T.edges(),val,star[0],path[0])
            if nx.is_isomorphic(T,nx.star_graph(n-1)) or nx.is_isomorphic(T,nx.path_graph(n)):
                continue
            strict += 1
            assert star[0]+1e-9 < val < path[0]-1e-9
    t0 = count(spider([3,1,1])); t1 = count(spider([2,2,1]))
    expected=2*sqrt(6)-2*sqrt(2)-2
    assert isclose(t0[0]-t1[0],expected,rel_tol=1e-12,abs_tol=1e-12)
    assert t0[2]==t1[2] and t0[3]!=t1[3] and t0[4]!=t1[4]
    print('THIRD_INTRINSIC_TREE_ZONOTOPE_CHECKS_PASSED',cnt,tr,strict)
    print('SPIDER_EXACT_DIFFERENCE',expected)

if __name__=='__main__':main()
