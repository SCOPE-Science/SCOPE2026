"""Independent exact coordinate-model construction and quantum-transfer check.
Run: python verify_coordinates.py (requires sympy, numpy).
No graph-library graph constructors or stored adjacency matrices are used.
"""
import itertools
import sympy as S
import numpy as np

phi=(1+S.sqrt(5))/2
ip=1/phi
signs=(-1,1)
C={}
C['tetrahedron']=[(S.Integer(a),S.Integer(b),S.Integer(c)) for a,b,c in itertools.product(signs,repeat=3) if a*b*c==1]
C['cube']=[tuple(map(S.Integer,p)) for p in itertools.product(signs,repeat=3)]
C['octahedron']=[tuple(S.Integer(s if k==i else 0) for k in range(3)) for i in range(3) for s in signs]
C['icosahedron']=[]
for p,q in itertools.product(signs,repeat=2):
    C['icosahedron'] += [(0,S.Integer(p),q*phi),(S.Integer(p),q*phi,0),(p*phi,0,S.Integer(q))]
C['dodecahedron']=[tuple(map(S.Integer,p)) for p in itertools.product(signs,repeat=3)]
for p,q in itertools.product(signs,repeat=2):
    C['dodecahedron'] += [(0,p*ip,q*phi),(p*ip,q*phi,0),(p*phi,0,q*ip)]
D2={'tetrahedron':S.Integer(8),'cube':S.Integer(4),'octahedron':S.Integer(2),'icosahedron':S.Integer(4),'dodecahedron':4*ip**2}
NE={'tetrahedron':(4,6),'cube':(8,12),'octahedron':(6,12),'icosahedron':(12,30),'dodecahedron':(20,30)}
SP={'tetrahedron':{S.Integer(3):1,S.Integer(-1):3},
'cube':{S.Integer(3):1,S.Integer(-3):1,S.Integer(1):3,S.Integer(-1):3},
'octahedron':{S.Integer(4):1,S.Integer(-2):2,S.Integer(0):3},
'icosahedron':{S.Integer(5):1,S.Integer(-1):5,S.sqrt(5):3,-S.sqrt(5):3},
'dodecahedron':{S.Integer(3):1,S.Integer(-2):4,S.Integer(1):5,S.Integer(0):4,S.sqrt(5):3,-S.sqrt(5):3}}

for name,coord in C.items():
    n=len(coord);A=S.zeros(n)
    for i in range(n):
        for j in range(i+1,n):
            d=S.simplify(sum((S.sympify(x)-S.sympify(y))**2 for x,y in zip(coord[i],coord[j])))
            if S.simplify(d-D2[name])==0:A[i,j]=A[j,i]=1
            else: assert float(d-D2[name])>0.0001, (name,i,j,d)
    assert (n,sum(A)/2)==NE[name]
    assert A.eigenvals()==SP[name],(name,A.eigenvals())
    # Breadth-first distances independently of graph packages.
    distance=[]
    for v in range(n):
        ds=[-1]*n;ds[v]=0;queue=[v]
        for cur in queue:
            for j in range(n):
                if A[cur,j] and ds[j]<0:
                    ds[j]=ds[cur]+1;queue.append(j)
        assert len(queue)==n
        distance.append(ds)
    dia=max(max(ds) for ds in distance)
    antip=[[j for j in range(n) if distance[i][j]==dia] for i in range(n)]
    # Compare spectral projection weights with antipodal signs using polynomial formula.
    eig=SP[name]
    for lam,m in eig.items():
        E=S.eye(n)
        for mu in eig:
            if mu!=lam:E=E*(A-mu*S.eye(n))/(lam-mu)
        assert S.simplify(E[0,0]-S.Rational(m,n))==0
        if len(antip[0])==1:
            ratio=S.simplify(E[0,antip[0][0]]/E[0,0])
            assert ratio in [-1,1],(name,lam,ratio)
    # One independently numerical diagonalization check on all n(n-1)/2 pairs at selected times.
    a=np.asarray(A,dtype=float);w,V=np.linalg.eigh(a)
    for t in (0.31,1.49,2.61):
        H=(V*np.exp(-1j*w*t))@V.T
        assert np.max(np.abs(H@H.conj().T-np.eye(n)))<1e-11
        if len(antip[0])==1:
            val=0j
            for lam,m in eig.items():
                E=S.eye(n)
                for mu in eig:
                    if mu!=lam:E=E*(A-mu*S.eye(n))/(lam-mu)
                sign=float(E[0,antip[0][0]]/E[0,0])
                val+=m*sign*complex(np.exp(-1j*float(lam)*t))/n
            assert abs(H[0,antip[0][0]]-val)<1e-10,(name,t,H[0,antip[0][0]],val)
    print(name,'coordinate edges',int(sum(A)/2),'diameter',dia,'spectral/numerical agreement PASS')
