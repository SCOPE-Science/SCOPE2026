#!/usr/bin/env python3
"""Direct numerical consistency tests for a mixed graph heat theorem.
Requires numpy, scipy, networkx; runs without external files or network access.
Float tests illustrate the theorem and are not a substitute for its proof.
"""
import math
import numpy as np
import networkx as nx
from scipy.linalg import expm
from scipy.optimize import brentq


def graph_suite():
    q=13
    residues={i*i%q for i in range(1,q)}
    p=nx.Graph()
    p.add_nodes_from(range(q))
    p.add_edges_from((i,j) for i in range(q) for j in range(i+1,q) if ((i-j)%q) in residues)
    return [
        ('pentagon',nx.cycle_graph(5)),
        ('Petersen',nx.petersen_graph()),
        ('rook4',nx.cartesian_product(nx.complete_graph(4),nx.complete_graph(4))),
        ('triangular5',nx.line_graph(nx.complete_graph(5))),
        ('balanced_biclique',nx.complete_bipartite_graph(3,3)),
        ('tripartite',nx.complete_multipartite_graph(2,2,2)),
        ('Paley13',p),
    ]

def spectrum(A):
    N=len(A)
    d=A.sum(axis=0)
    assert np.max(np.abs(d-d[0])) < 1e-10
    k=int(round(d[0]))
    adj=np.argwhere(np.triu(A,k=1)>0)
    non=np.argwhere(np.triu(1-np.eye(N)-A,k=1)>0)
    assert len(adj)>0 and len(non)>0
    A2=A@A
    lmbd=int(round(A2[tuple(adj[0])]))
    mu=int(round(A2[tuple(non[0])]))
    assert np.max(np.abs(A2[tuple(adj.T)]-lmbd))<1e-9
    assert np.max(np.abs(A2[tuple(non.T)]-mu))<1e-9
    delta=math.sqrt((lmbd-mu)**2 + 4*(k-mu))
    a=(2*k-lmbd+mu-delta)/2
    b=(2*k-lmbd+mu+delta)/2
    assert 0<a<b<=N+1e-10
    L=k*np.eye(N)-A
    z=np.linalg.eigvalsh(L)
    assert min(abs(z-a))<1e-8 and min(abs(z-b))<1e-8
    return L,a,b,adj,non,(N,k,lmbd,mu)

def threshold(a,b,eta):
    alpha=a+eta*a*a
    beta=b+eta*b*b
    tmin=math.log((1+eta*b)/(1+eta*a))/(beta-alpha)
    f=lambda t:b*math.exp(-alpha*t)-a*math.exp(-beta*t)-(b-a)
    assert f(tmin)>0
    Tmax=math.log(b/(b-a))/alpha
    return brentq(f,tmin,Tmax+1e-9,xtol=1e-14)

def peak(a,b):
    A=math.log1p(a/b)
    B=math.log1p(b/a)
    denominator=b*b*A-a*a*B
    numerator=a*B-b*A
    eta=numerator/denominator
    tmax=denominator/(a*b*(b-a))
    assert eta>0 and tmax>0
    return eta,tmax

def main():
    records=0
    for name,G in graph_suite():
        A=nx.to_numpy_array(G)
        L,a,b,adj,non,params=spectrum(A)
        eta_star,t_star=peak(a,b)
        assert abs(threshold(a,b,eta_star)-t_star)<1e-10
        for eta in [eta_star/8,eta_star/2,eta_star,eta_star*2,eta_star*8,0.05,0.5,5]:
            T=threshold(a,b,eta)
            assert T <= t_star*(1+2e-11)
            for scale in [0.01,0.2,0.75,1.,1.3,2.,5.]:
                t=scale*T
                K=expm(-t*(L+eta*(L@L)))
                off_non=K[tuple(non.T)]
                off_adj=K[tuple(adj.T)]
                assert np.max(off_non)-np.min(off_non)<2e-12
                assert np.min(off_adj)>-2e-12
                assert np.min(np.diag(K))>0
                pred=(1-(b/(b-a))*math.exp(-(a+eta*a*a)*t)+(a/(b-a))*math.exp(-(b+eta*b*b)*t))/len(A)
                assert np.max(np.abs(off_non-pred))<3e-12
                if scale<0.99:assert np.max(off_non)<1e-10, (name,eta,scale,off_non)
                if scale>1.01:assert np.min(off_non)>-1e-10,(name,eta,scale,off_non)
                records+=1
        print(f'{name:20s} params={params} a={a:.8f} b={b:.8f} eta*={eta_star:.9f} maxT={t_star:.9f}')
    print('PASS:',records,'matrix exponential / entrywise / optimality checks')
if __name__=='__main__':main()
