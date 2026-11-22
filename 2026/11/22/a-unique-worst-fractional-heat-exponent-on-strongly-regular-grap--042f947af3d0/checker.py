import numpy as np
from math import exp, log
from scipy.optimize import brentq
from scipy.linalg import expm
import networkx as nx


def matrix(g):
    return nx.to_numpy_array(g, dtype=float)

def graph_suite():
    yield 'pentagon',nx.cycle_graph(5)
    yield 'petersen',nx.petersen_graph()
    # Triangular graph T(5): vertices are two-subsets of {0..4}
    import itertools
    for m in (5,6):
        v=list(itertools.combinations(range(m),2)); g=nx.Graph();g.add_nodes_from(range(len(v)))
        for i in range(len(v)):
            for j in range(i+1,len(v)):
                if len(set(v[i]).intersection(v[j]))==1:g.add_edge(i,j)
        yield 'triangular_'+str(m),g
    # Rook (4x4) and (5x5)
    for m in (4,5):
        v=list(itertools.product(range(m),repeat=2));g=nx.Graph();g.add_nodes_from(range(len(v)))
        for i in range(len(v)):
            for j in range(i+1,len(v)):
                if v[i][0]==v[j][0] or v[i][1]==v[j][1]:g.add_edge(i,j)
        yield 'rook_'+str(m),g
    # equal-part complete multipartite (imprimitive)
    for p,r in ((2,3),(3,3)):
        yield 'multipartite_%d_%d'%(r,p), nx.complete_multipartite_graph(*([p]*r))

def stable_h(z,q):
    return -np.log(q*np.exp(-z)-(q-1))
def mininfo(a,b,n,k,alpha):
    q=b/a; A=a**alpha;B=b**alpha
    if alpha<=1:return (0.,0.,0.)
    tmin=(alpha-1)*log(q)/(B-A)
    h=(1-(b*exp(-A*tmin)-a*exp(-B*tmin))/(b-a))/n
    ampl=1+2*(n-k-1)*(-h)
    return tmin,h,ampl

def horizon(a,b,alpha):
    if alpha<=1:return 0.
    q=b/a
    c=log(b/(b-a)); BdivA=q**alpha
    def fun(z):return q*(-np.expm1(-z))-(-np.expm1(-BdivA*z))
    # near zero fun<0; use bracket with tiny lower z 
    lower=min(1e-10,c*1e-4)
    if fun(lower)>=0:
        lower=min(1e-14,c*1e-8)
    return brentq(fun,lower,c,xtol=1e-14)/(a**alpha)

def alphamax(a,b):
    q=b/a;delta=log(a)/log(q);c=log(q/(q-1))
    # h' expression
    def elast(z):
        h=stable_h(z,q)
        hp=q/(q-(q-1)*exp(z))
        return z*hp/h
    z=brentq(lambda z:elast(z)-(1+1/delta),1e-7,c-1e-9,xtol=1e-14)
    alpha=log(stable_h(z,q)/z)/log(q)
    return alpha, (z**(1+delta))/stable_h(z,q)**delta

nr=0
for name,g in graph_suite():
    Adj=matrix(g);n=Adj.shape[0];k=int(sum(Adj[0]));L=k*np.eye(n)-Adj
    e=np.argwhere(np.triu(Adj)>0)[0];u,v=e
    f=np.argwhere(np.triu(1-Adj-np.eye(n))>0)[0];p,q0=f
    lam=int(np.dot(Adj[u],Adj[v]));mu=int(np.dot(Adj[p],Adj[q0]))
    disc=((lam-mu)**2+4*(k-mu))**.5
    a=k-(lam-mu+disc)/2;b=k-(lam-mu-disc)/2
    eig=np.linalg.eigvalsh(L);assert np.max(np.minimum.reduce([abs(eig),abs(eig-a),abs(eig-b)]))<1e-9
    assert a>1
    alpha_star,tstar=alphamax(a,b)
    assert horizon(a,b,alpha_star-1e-3)<tstar and horizon(a,b,alpha_star+1e-3)<tstar
    for test_alpha in np.linspace(1.01,15,100):
        assert horizon(a,b,float(test_alpha))<=tstar+1e-9,(name,test_alpha)
    for alpha in [0.4,1,1.02,1.2,1.6,2,3,alpha_star,4]:
        T=horizon(a,b,alpha)
        tm,hm,ampl=mininfo(a,b,n,k,alpha)
        q=b/a;A=a**alpha;B=b**alpha
        P=(L-b*(np.eye(n)-np.ones((n,n))/n))/(a-b)
        Q=np.eye(n)-np.ones((n,n))/n-P
        for t in set([0.0001,0.25*T,0.5*T,T,1.0001*T,3*T,tm,0.1,1.0]):
            if t<0:continue
            K=np.ones((n,n))/n+np.exp(-A*t)*P+np.exp(-B*t)*Q
            evals,evecs=np.linalg.eigh(L)
            spectral_power=(evecs*np.where(evals>1e-9,evals,0.0)**alpha)@evecs.T
            F=expm(-t*spectral_power)
            assert np.max(abs(K-F))<1e-11,(name,alpha,t)
            if t>1e-8:
                for i in range(n):
                    for j in range(n):
                        v=K[i,j]
                        if i==j or Adj[i,j]==1:assert v>-1e-10,(name,alpha,i,j,v)
                        elif alpha>1 and t<T*(1-1e-7):assert v<1e-9,(name,alpha,t,T,v)
                        elif alpha>1 and t>T*(1+1e-7):assert v>-1e-9,(name,alpha,t,T,v)
                        elif alpha<=1:assert v>-1e-9,(name,alpha,t,T,v)
            nr+=1
    print(name,'N,k,a,b=',n,k,a,b,'optimal-alpha=',alpha_star,'maxdelay=',tstar,'sample T2=',horizon(a,b,2),'amp2=',mininfo(a,b,n,k,2)[2])

# Asymptotic scale checks, not a substitute for the analytical proof.
for name,g in graph_suite():
    Adj=matrix(g);n=len(Adj);k=int(sum(Adj[0]));L=k*np.eye(n)-Adj
    z=np.linalg.eigvalsh(L); v=np.unique(np.round(z[z>1e-9],11));a,b=v
    q=b/a;d=n-k-1
    for eps in [1e-2,2e-3]:
        T=horizon(a,b,1+eps)
        leading=2*log(q)/(b-a)*eps
        assert abs(T/leading-1)<0.03,(name,eps,T,leading)
        tm,hm,amp=mininfo(a,b,n,k,1+eps)
        assert abs((amp-1)/(d*a*b*(log(q))**2/(n*(b-a)**2)*eps*eps)-1)<0.04,(name,eps,amp)
    for alpha in [30,40]:
        T=horizon(a,b,alpha)
        target=log(b/(b-a))
        assert abs(T*a**alpha/target-1)<0.005,(name,alpha,T,target)
        _,hm,amp=mininfo(a,b,n,k,alpha)
        targetamp=1+2*d*a/(n*(b-a))
        assert abs(amp-targetamp)<0.03,(name,alpha,amp,targetamp)
print('PASSED matrices/times',nr,'and 32 scale checks, 800 global optimization samples')

