"""Standalone finite-dimensional checks of the peer-epoch spectral criterion.
The analytic theorem in RESULT.md is not replaced by these finite tests.
Run: python3 VERIFY.py (requires numpy, networkx).
"""
import itertools
import numpy as np
import networkx as nx


def filter_matrix(W, alpha, K):
    n=W.shape[0]
    power=np.eye(n)
    out=np.zeros((n,n))
    for j in range(K):
        out+=(1-alpha)*alpha**j*power
        power=power@W
    out+=alpha**K*power
    return out


def factor(mu,alpha,K):
    return (1-alpha + alpha**(K+1)*(mu**K)*(1-mu))/(1-alpha*mu)


def check_all_small_regular():
    # Exhaustively inspect the 1253 nonisomorphic undirected graphs on 2..7 vertices,
    # retaining connected regular graphs; compare the spectral obstruction and formula.
    graph_count=0
    cases=0
    atlas=nx.graph_atlas_g()
    for G in atlas:
        n=G.number_of_nodes()
        if n < 2 or n > 7 or not nx.is_connected(G):
            continue
        deg=[d for _,d in G.degree()]
        if not deg or min(deg)!=max(deg): continue
        graph_count+=1
        W=nx.to_numpy_array(G)/deg[0]
        spectrum=np.linalg.eigvalsh(W)[::-1]
        if nx.is_connected(G) and nx.density(G)<1-1e-12:
            assert spectrum[1]>-1e-10, (n,spectrum)
        else:
            assert spectrum[1]<0
        for K in range(1,7):
            for alpha in (0.13, 0.41, 0.73, 0.93):
                M=filter_matrix(W,alpha,K)
                lambdas=np.linalg.eigvalsh(M)[::-1]
                formula=sorted([factor(float(mu),alpha,K) for mu in spectrum],reverse=True)
                assert np.allclose(lambdas,formula,atol=1e-12)
                assert np.allclose(M@np.ones(n),np.ones(n),atol=2e-12)
                assert np.min(M)>-1e-12
                cases+=1
    return graph_count,cases


def check_weighted_example():
    # Positive symmetric weighted complete network with two distinct negative modes.
    from fractions import Fraction as F
    Wq=[[F(1,20),F(11,20),F(2,5)],
        [F(11,20),F(1,10),F(7,20)],
        [F(2,5),F(7,20),F(1,4)]]
    assert all(sum(row)==1 for row in Wq)
    W=np.array(Wq,dtype=float)
    eigs=np.linalg.eigvalsh(W)
    assert eigs[1]<-1e-8 and eigs[0]<eigs[1]-1e-8, eigs
    alphas=[1/(1-float(mu)) for mu in eigs[:-1]]
    assert all(0<a<1 for a in alphas)
    M=np.eye(3)
    for a in alphas: M=filter_matrix(W,a,1)@M
    assert np.allclose(M,np.ones((3,3))/3,atol=5e-14),M
    for mu in eigs[:-1]:
        for K in (1,3,5,7):
            lo,hi=0.,1.
            for _ in range(100):
                a=(lo+hi)/2
                if factor(mu,a,K)>0:lo=a
                else:hi=a
            a=(lo+hi)/2
            assert abs(factor(mu,a,K))<2e-13
        for K in (2,4,6):
            for a in (0.1,0.4,0.8,0.99):assert factor(mu,a,K)>0
    return eigs.tolist(), alphas


def check_exact_three_node():
    # Rational exact construction for an infinitely near-complete lazy-free example.
    # W=(J/3) - (1/12)*projection_1 - (1/6)*projection_2, where
    # P1=vvT/2, v=(1,-1,0); P2=wwT/6, w=(1,1,-2).
    from fractions import Fraction as F
    v=[1,-1,0]; w=[1,1,-2]
    W=[[F(1,3)-F(1,12)*F(v[i]*v[j],2)-F(1,6)*F(w[i]*w[j],6)
        for j in range(3)] for i in range(3)]
    assert all(sum(r)==1 and all(z>0 for z in r) for r in W)
    roots=[F(-1,12),F(-1,6)]
    P=[[F(int(i==j)) for j in range(3)] for i in range(3)]
    for mu in roots:
        alpha=1/(1-mu)
        Q=[[((1-alpha) if i==j else F(0))+alpha*W[i][j] for j in range(3)] for i in range(3)]
        P=[[sum(Q[i][k]*P[k][j] for k in range(3)) for j in range(3)] for i in range(3)]
    assert P==[[F(1,3) for _ in range(3)] for _ in range(3)]
    return str(roots),str([1/(1-m) for m in roots])

if __name__=='__main__':
    graphs,cases=check_all_small_regular()
    eigs,alphas=check_weighted_example()
    rat=check_exact_three_node()
    print(f'PASS: {graphs} connected regular graph types, {cases} spectral/filter comparisons')
    print('PASS: weighted complete three-node example has two distinct negative eigenvalues',eigs)
    print('PASS: two FJ one-inner-step epochs yield exact rank-one averaging (floating)',alphas)
    print('PASS: exact rational three-node rank-one product',rat)
