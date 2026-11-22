"""Reproducible spectral checks for fractional heat on strongly regular graphs.

Requires Python 3 and NumPy. Finite tests corroborate, not replace, the proof.
"""
import math
import itertools
import numpy as np

def graph(kind):
    if kind == 'pentagon':
        n=5; edges={(i,(i+1)%n) for i in range(n)}
    elif kind == 'petersen':
        verts=list(itertools.combinations(range(5),2)); n=len(verts)
        edges={(i,j) for i in range(n) for j in range(i+1,n) if set(verts[i]).isdisjoint(verts[j])}
    elif kind == 'rook4':
        verts=list(itertools.product(range(4),repeat=2));n=len(verts)
        edges={(i,j) for i in range(n) for j in range(i+1,n) if verts[i][0]==verts[j][0] or verts[i][1]==verts[j][1]}
    elif kind == 'triangular5':
        verts=list(itertools.combinations(range(5),2));n=len(verts)
        edges={(i,j) for i in range(n) for j in range(i+1,n) if set(verts[i])&set(verts[j])}
    elif kind == 'bipartite33':
        n=6;edges={(i,j) for i in range(3) for j in range(3,6)}
    else:raise ValueError(kind)
    A=np.zeros((n,n));
    for i,j in edges:A[i,j]=A[j,i]=1
    return A

def check():
    cases=0
    for kind in ('pentagon','petersen','rook4','triangular5','bipartite33'):
        G=graph(kind); n=G.shape[0];k=int(G.sum(axis=1)[0]);assert np.all(G.sum(axis=1)==k)
        GA=G@G; e=[int(GA[i,j]) for i in range(n) for j in range(i+1,n) if G[i,j]==1]
        z=[int(GA[i,j]) for i in range(n) for j in range(i+1,n) if G[i,j]==0]
        assert len(set(e))==len(set(z))==1
        lam=e[0];mu=z[0]
        delta=math.sqrt((lam-mu)**2+4*(k-mu));r=(lam-mu+delta)/2;s=(lam-mu-delta)/2
        a=k-r;b=k-s;C=(k-s)/(r-s);U=(n-k+s)/(r-s)
        assert a>0 and b>a and C>1 and U>-1e-12
        xvals, Q=np.linalg.eigh(k*np.eye(n)-G)
        xvals[np.abs(xvals)<1e-10]=0
        assert np.allclose(np.sort(xvals), np.sort([0]+[a]*int(round(((-k-s*(n-1))/(r-s)))) + [b]*int(round((k+r*(n-1))/(r-s)))),atol=1e-10)
        h=n-k-1
        for alpha in (0.45,1,1.01,1.1,1.5,2,3.5,7):
            aa=a**alpha; bb=b**alpha
            for t in (0.001/aa,0.1/aa,0.5/aa,2/aa,5/aa):
                K=(Q*np.exp(-t*np.maximum(xvals,0)**alpha))@Q.T
                qn=(1-C*math.exp(-aa*t)+(C-1)*math.exp(-bb*t))/n
                qe=(1+U*math.exp(-aa*t)-(1+U)*math.exp(-bb*t))/n
                assert np.allclose(K[np.where((G==0)&(~np.eye(n,dtype=bool)))], qn,atol=5e-12)
                assert np.allclose(K[np.where(G==1)],qe,atol=5e-12)
                assert qe>0
                assert (qn>0) if alpha<=1 else (qn <0 if t<1e-3/aa else True)
                bound=1+2*h*max(0,-qn)
                assert abs(np.max(np.sum(abs(K),axis=1))-bound)<1e-10, (kind,alpha,t,qn,np.max(np.sum(abs(K),axis=1)),bound)
                cases+=1
        for deltaalpha in (.0001,.00003):
            alpha=1+deltaalpha; aa=a**alpha;bb=b**alpha
            def fn(t):return -C*math.expm1(-aa*t)+(C-1)*math.expm1(-bb*t)
            peak=(alpha-1)*math.log(b/a)/(bb-aa)
            lo=peak;hi=10/aa
            for _ in range(90):
                mid=(lo+hi)/2
                if fn(mid)>0:hi=mid
                else:lo=mid
            troot=(lo+hi)/2
            target=2*math.log(b/a)/(b-a)*deltaalpha
            assert abs(troot/target-1)<0.002
        print(kind,'v,k,lambda,mu=',n,k,lam,mu,'r,s=',r,s,'C=',C,'U=',U)
    print('PASS', cases, 'independent kernel and norm comparisons')
if __name__=='__main__':check()
