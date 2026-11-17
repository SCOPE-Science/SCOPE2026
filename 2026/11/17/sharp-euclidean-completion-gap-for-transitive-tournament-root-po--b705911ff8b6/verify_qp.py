import numpy as np
from scipy.optimize import minimize
checks=0
for n in range(2,12):
    E=[(i,j) for i in range(n) for j in range(i+1,n)]
    A=np.zeros((n,len(E)))
    for t,(i,j) in enumerate(E):A[i,t]=1;A[j,t]=-1
    distances=[]
    for i,j in E:
        x=-A[:,E.index((i,j))]
        def f(z):return np.dot(A@z-x,A@z-x)/2
        def g(z):return A.T@(A@z-x)
        sol=minimize(f,np.full(len(E),1/len(E)),jac=g,method='SLSQP',
            bounds=[(0,None)]*len(E),constraints=[{'type':'eq','fun':lambda z:np.sum(z)-1,'jac':lambda z:np.ones(len(E))}],
            options={'ftol':1e-13,'maxiter':2000})
        assert sol.success,(n,i,j,sol.message)
        distances.append((2*sol.fun,i,j))
        checks+=1
    winner=max(distances)
    expected=8 if n==2 else (4.5 if n==3 else (3.2 if n==4 else 2+12/((n-3)*(n-2)*(n-1))))
    assert abs(winner[0]-expected)<1e-8,(n,winner,expected)
    assert (winner[1],winner[2])==(0,n-1),(n,winner)
    if n>=5:
        m=n-2
        c=6/(m*(m*m-1))
        p=np.zeros(n)
        p[1:-1]=[c*(m-1-2*h) for h in range(m)]
        assert abs(np.dot(p-(-A[:,E.index((0,n-1))]),p-(-A[:,E.index((0,n-1))]))-expected)<1e-9
print(f'INDEPENDENT_QP_PASS negative_roots={checks} dimensions=2..11')
