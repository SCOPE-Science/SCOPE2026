import numpy as np,itertools,math

def construct(mods):
    G=list(itertools.product(*(range(q) for q in mods))); n=len(G)
    ix={t:i for i,t in enumerate(G)}
    add=lambda a,b: tuple((x+y)%q for x,y,q in zip(a,b,mods))
    neg=lambda a: tuple((-x)%q for x,q in zip(a,mods))
    Q=np.zeros((n*n,n)); D=np.zeros((n,n));
    for i,x in enumerate(G):
      for j,y in enumerate(G):
        Q[i*n+j,ix[add(x,y)]]+=1
        Q[i*n+j,ix[add(x,neg(y))]]+=1
        Q[i*n+j,i]-=2
        Q[i*n+j,j]-=2
      D[i]=Q[i*n+i]
    return G,Q,D

def predicted(mods):
    G=list(itertools.product(*(range(q) for q in mods))); n=len(G); ix={t:i for i,t in enumerate(G)}
    double=lambda a: tuple((2*x)%q for x,q in zip(a,mods))
    visited={G[0]}; cycles=[]
    for x in G[1:]:
      if x not in visited:
        c=[];y=x
        while y not in visited:
           c.append(y);visited.add(y);y=double(y)
        assert y==x
        cycles.append(c)
    lam_minus=(n+12-math.sqrt(n*(n+24)))/2
    lam_plus=(n+12+math.sqrt(n*(n+24)))/2
    ev=[lam_minus,lam_plus]+[9]*(len(cycles)-1)
    for c in cycles:
      for k in range(1,len(c)):
        ev.append(17-8*math.cos(2*math.pi*k/len(c)))
    assert len(ev)==n
    return sorted(ev), cycles

count=0
for mods in [(3,),(5,),(7,),(9,),(11,),(13,),(15,),(17,),(19,),(21,),(3,3),(3,5),(3,3,3)]:
    G,Q,D=construct(mods);n=len(G)
    eig=np.linalg.eigvalsh(D.T@D)
    expected,cycles=predicted(mods)
    if not np.allclose(eig,expected,atol=1e-10):
       print(mods,'MISMATCH',eig,expected);raise SystemExit(1)
    raw=np.linalg.eigvalsh(Q.T@Q/n)
    expectedQ=sorted([4]+[10]*(n-1))
    if not np.allclose(raw,expectedQ,atol=1e-10):
       print(mods,'Q MISMATCH',raw,expectedQ);raise SystemExit(1)
    print(mods,'N',n,'cycle lengths',list(map(len,cycles)),'min D²',round(eig[0],9),'max D²',round(eig[-1],9))
    count+=n*n+n
print('DIAGNOSTIC_OK',count)
