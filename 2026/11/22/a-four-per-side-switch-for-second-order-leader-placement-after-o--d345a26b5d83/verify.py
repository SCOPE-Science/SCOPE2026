"""Reproducibility checks for two pinned leaders in a one-edge-defective balanced biclique.
Run: python verify.py  (requires sympy and numpy)
Analytic identity and polynomial signs, not finite numerical tests, prove all n >= 3.
"""
import itertools
import math
import numpy as np
import sympy as sp

N = sp.symbols('n', integer=True, positive=True)
T = sp.symbols('t', nonnegative=True)

def class_cost(n, a, defect_A, defect_B):
    """Trace of square of Sherman-Morrison inverse after 2 leaders.
    a leaders on part A, 2-a on part B. Defect endpoint indicators on follower set.
    n may be symbolic or integer. Indicators are 0/1.
    """
    b=2-a
    r=n-a; s=n-b
    D=n*n-r*s
    u=sp.Integer(defect_A);v=-sp.Integer(defect_B)
    A=s*u/(n*D)+v/D
    B=r*v/(n*D)+u/D
    h_norm=r*A*A+2*A*u/n+(u/n)**2+s*B*B+2*B*v/n+(v/n)**2
    sumA=r*A+u/n
    sumB=s*B+v/n
    alpha=u*(A+u/n)+v*(B+v/n)
    cubic=h_norm/n+s*sumA**2/(n*D)+r*sumB**2/(n*D)+2*sumA*sumB/D
    base=(2*n-4)/n**2+(4*n*n-2*D)/D**2
    return sp.factor(base+2*cubic/(1-alpha)+h_norm*h_norm/(1-alpha)**2)

C={
    'DD':class_cost(N,1,0,0),
    'DS':class_cost(N,2,0,1),
    'DX':class_cost(N,1,0,1),
    'SS':class_cost(N,2,1,1),
    'SX':class_cost(N,1,1,1),
}

# Independent stated rational formulas: exact algebraic verification for symbolic N.
expected={
'DD':2*(N-1)*(2*N**3+4*N**2-7*N+2)/(N**2*(2*N-1)**2),
'DS':(4*N**6-4*N**5-22*N**4+76*N**3-105*N**2+68*N-20)/(N**2*(2*N**2-3*N+2)**2),
'DX':(4*N**6-4*N**5-28*N**4+108*N**3-147*N**2+88*N-20)/(4*N**2*(N-1)**4),
'SS':(N**6-3*N**5-2*N**4+23*N**3-35*N**2+22*N-5)/(N**2*(N-1)**4),
'SX':2*(2*N**6-6*N**5-7*N**4+67*N**3-134*N**2+116*N-40)/(N**2*(2*N**2-5*N+4)**2),
}
checks=0
for label in C:
    assert sp.cancel(C[label]-expected[label]) == 0, label
    checks+=1

# For N>=3 these three classes have strictly larger cost than DD.
positive_from_3={
'DS':[32,372,1718,3929,4432,1961],
'DX':[16,300,2460,11352,31648,53065,49394,19649],
'SX':[64,712,3156,6956,7604,3284],
}
for label,coeffs in positive_from_3.items():
    numerator=sp.together(C[label]-C['DD']).as_numer_denom()[0]
    got=sp.Poly(sp.expand(numerator.subs(N,T+3)),T).all_coeffs()
    assert got==list(map(sp.Integer,coeffs)),(label,got)
    assert all(x>0 for x in got)
    checks+=2

# Difference DD-SS has sign of degree 7 polynomial H.
H=4*N**7-19*N**6+17*N**5+14*N**4-35*N**3+25*N**2-8*N+1
assert sp.cancel(C['DD']-C['SS']-H/(N**2*(N-1)**4*(2*N-1)**2))==0
assert H.subs(N,3)==-581
assert sp.Poly(H.subs(N,T+4),T).all_coeffs()==[4,93,905,4754,14429,24885,21808,6833]
checks+=3

# Independent direct eigenspectrum of each grounded Laplacian for every leader pair.
for n in range(3,15):
    A=np.zeros((2*n,2*n),dtype=float)
    for i in range(n):
        for j in range(n,2*n):
            if (i,j)!=(0,n):
                A[i,j]=A[j,i]=1.
    L=np.diag(A.sum(axis=1))-A
    for leaders in itertools.combinations(range(2*n),2):
        remain=[i for i in range(2*n) if i not in leaders]
        vals=np.linalg.eigvalsh(L[np.ix_(remain,remain)])
        assert np.min(vals)>0
        actual=sum(float(1/x**2) for x in vals)
        selectedA=sum(i<n for i in leaders)
        c=sp.Rational(class_cost(n,selectedA,int(0 not in leaders),int(n not in leaders)))
        expected_value=float(c)
        assert math.isclose(actual,expected_value,rel_tol=5e-9,abs_tol=5e-9), (n,leaders,actual,expected_value)
        checks+=1
    costs={z:float(expr.subs(N,n)) for z,expr in C.items()}
    best=min(costs,key=costs.get)
    assert best==('DD' if n==3 else 'SS')
    checks+=1

# Separate first-order objective cross-check at the two disagreement sizes and the known switch.
for n in (4,5,6):
    A=np.ones((n,n),dtype=float)
    A[0,0]=0
    mat=np.block([[np.zeros((n,n)),A],[A.T,np.zeros((n,n))]])
    graph_L=np.diag(mat.sum(axis=1))-mat
    best=float('inf'); minimizers=[]
    for leaders in itertools.combinations(range(2*n),2):
        follower=[i for i in range(2*n) if i not in leaders]
        value=sum(1/x for x in np.linalg.eigvalsh(graph_L[np.ix_(follower,follower)]))
        if value<best-1e-9:
            best=float(value);minimizers=[leaders]
        elif abs(value-best)<1e-9:
            minimizers.append(leaders)
    if n in (4,5):
        assert minimizers==[(0,n)], (n,minimizers)
    else:
        expected_pairs=[pair for pair in itertools.combinations(range(2*n),2)
                        if pair[0]//n==pair[1]//n and pair[0]%n!=0 and pair[1]%n!=0]
        assert minimizers==expected_pairs,(n,minimizers,expected_pairs)
    checks+=1

print(f'PASS: {checks} symbolic and spectral checks, n=3,...,14; all-n proof by exact coefficient signs')
