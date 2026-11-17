"""Exact transfer and spectral checks for majority fixed points on GP(n,k).
Run: python check_transfer.py  (Python 3.11+, sympy and networkx)
"""
import sympy as sp
import networkx as nx

P32 = [1,0,-1,-2,-2,0,1,1,0,1,4,7,0,0,0,0,6,3,-7,-7,-8,-8,0,-1,-2,-3,-6,-2,0,-1,0,-1,-1]
P33 = [1,-1,1,-3,4,-4,5,-6,5,-1,-1,-1,1,-2,-4,4,-4,1,4,0,1,2,0,-1,-3,1,-3,-2,0,1,-1,1,0,1]
x = sp.Symbol('x')


def graph_for(k):
    """Overlap on words of 2*k columns; each column has two binary spins."""
    width = 2*k
    g = nx.DiGraph()
    g.add_nodes_from(range(1 << (2*width)))
    for state in range(1 << (2*width)):
        for new_column in range(4):
            w = state | (new_column << (2*width))
            a = lambda j: (w >> (2*j)) & 1
            b = lambda j: (w >> (2*j+1)) & 1
            ou = (a(k-1)+a(k+1)+b(k) >= 2) == bool(a(k))
            inn = (b(0)+b(2*k)+a(k) >= 2) == bool(b(k))
            if ou and inn:
                target = (state >> 2) | (new_column << (2*(width-1)))
                g.add_edge(state, target)
    return g


def cyclic_components(g):
    c = []
    for S in nx.strongly_connected_components(g):
        if len(S)>1 or g.has_edge(next(iter(S)),next(iter(S))):
            c.append(sorted(S))
    return sorted(c, key=len, reverse=True)


def adjacency(g,component):
    ix = {s:i for i,s in enumerate(component)}
    M = sp.zeros(len(ix))
    for s in component:
        for t in g[s]:
            if t in ix:
                M[ix[s],ix[t]] += 1
    return M


def sums(co,nmax):
    """Newton sums of all complex roots, with algebraic multiplicity."""
    d=len(co)-1
    s=[d]
    for n in range(1,nmax+1):
        val=sum(co[j]*s[n-j] for j in range(1,min(n-1,d)+1))
        if n<=d:val+=n*co[n]
        s.append(-val)
    return s


def pf_bracket(g,component,lower_num,upper_num,denom,power):
    ix={s:i for i,s in enumerate(component)}
    adj=[[ix[t] for t in g[s] if t in ix] for s in component]
    v=[1]*len(component)
    for _ in range(power):
        v=[sum(v[j] for j in neighbors) for neighbors in adj]
    assert min(v)>0
    w=[sum(v[j] for j in neighbors) for neighbors in adj]
    assert all(lower_num*v[i] < denom*w[i] < upper_num*v[i]
               for i in range(len(v)))
    return (min(sp.Rational(w[i],v[i]) for i in range(len(v))),
            max(sp.Rational(w[i],v[i]) for i in range(len(v))))


def main():
    details={}
    for k in (1,2,3):
        G=graph_for(k)
        comps=cyclic_components(G)
        assert [len(c) for c in comps] == {1:[4,1,1],2:[24,1,1],3:[124,1,1]}[k]
        assert G.number_of_edges()=={1:20,2:320,3:5120}[k]
        mats=[adjacency(G,c) for c in comps]
        charpolys=[m.charpoly(x).as_expr() for m in mats]
        full=sp.prod(charpolys)
        P=sp.Poly(full,x)
        if k==1:
            target=(x-1)**2*(x*x-x-1)*(x*x-x+1)
        elif k==2:
            pplus=x**9-x**8-x**7-x**4+2*x**3+1
            pminus=x**9-x**8-x**7+2*x**6-x**4-1
            target=(x-1)**2*x**6*pplus*pminus
        else:
            q32=sp.Poly.from_list(P32,gens=x).as_expr()
            q33=sp.Poly.from_list(P33,gens=x).as_expr()
            target=(x-1)**3*x**58*q32*q33
            assert sp.Poly(q32,x).count_roots(sp.Rational(15965,10000),sp.Rational(15966,10000))==1
            assert sp.Poly(q33,x).count_roots(sp.Rational(15965,10000),sp.Rational(15966,10000))==0
        assert sp.expand(full-target)==0
        trace_n=sums(list(map(int,P.all_coeffs())),24)
        details[k]=trace_n
        print(f'k={k} size={G.number_of_nodes()} edges={G.number_of_edges()} cyclic_SCC_sizes={[len(c) for c in comps]}')
        print(f'k={k} counts n={2*k+1}..12: {[trace_n[n] for n in range(2*k+1,13)]}')
        if k==2:
            lo,hi=pf_bracket(G,comps[0],156485,156486,100000,38)
            print('k=2 Perron strict bracket 1.56485..1.56486; ratio bounds:',lo,hi)
        if k==3:
            lo,hi=pf_bracket(G,comps[0],15965,15966,10000,37)
            print('k=3 Perron strict bracket 1.5965..1.5966; ratio bounds:',lo,hi)
        assert len(comps[0])>1
        assert any(G.has_edge(u,u) for u in comps[0]) # irreducible and aperiodic
    assert [details[3][n] for n in range(7,13)]==[32,72,52,124,224,236]
    assert [details[2][n] for n in range(7,13)]==[32,48,76,118,158,242]
    assert [details[1][n] for n in range(7,13)]==[32,48,76,124,202,326]
    print('All exact symbolic, graph and Perron checks passed.')

if __name__=='__main__':main()
