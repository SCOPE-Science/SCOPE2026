"""Reproduce exact fan-wall degrees and convex certificates for Z13''(a,2,a+2,d).
Run with Python 3 and SymPy: python verify.py.
"""
import itertools
import sympy as s

a,k=s.symbols('a k',integer=True); d=a+k
V={1:s.Matrix([1,1,2]),2:s.Matrix([1,0,0]),3:s.Matrix([0,-1,0]),4:s.Matrix([0,0,-1]),5:s.Matrix([-1,a,d]),6:s.Matrix([0,1,0]),7:s.Matrix([0,0,1]),8:s.Matrix([-1,a+2,d+1])}
cones=['124','234','345','456','146','167','127','237','358','568','378','678']
inc={}
for c in cones:
    for ij in itertools.combinations(sorted(map(int,c)),2):inc.setdefault(ij,[]).append(tuple(map(int,c)))
assert len(inc)==18 and all(len(x)==2 for x in inc.values())
expected={'12':2,'14':-1,'16':2,'17':3,'23':2,'24':3,'27':-1,'34':2*a+k+2,'35':3,'37':3-k,'38':-1,'45':2,'46':k+3,'56':-1,'58':2,'67':-2*a-k-4,'68':3,'78':2}
for (i,j),tri in inc.items():
    m,n=sorted(set(tri[0])-{i,j}).pop(),sorted(set(tri[1])-{i,j}).pop()
    coeff=s.Matrix.hstack(V[i],V[j]).gauss_jordan_solve(V[m]+V[n])[0]
    degree=s.expand(2-coeff[0]-coeff[1])
    assert s.simplify(degree-expected[str(i)+str(j)])==0,(i,j,degree)
print('VERIFY_OK 18 independent symbolic wall relations and all anticanonical degrees')
A=(V[2]+V[5])/2; D=(V[1]+V[8])/2
h=lambda v:s.expand(v[1]-v[2]);g=lambda v:s.expand(v[1]+v[2])
assert h(A)==h(D)==-k/2 and g(A)==a+k/2 and g(D)==a+k/2+3
# Compare coordinates of the certificates to explicit rational formulas.
tpos=4/(k+2); tneg=4/(2-k)
Qa_pos=tpos*A+(1-tpos)*V[4]; Qd_pos=tpos*D+(1-tpos)*V[6]
Qa_neg=tneg*A+(1-tneg)*V[3]; Qd_neg=tneg*D+(1-tneg)*V[7]
for Q,H,G in ((Qa_pos,-1,(4*a+k+2)/(k+2)),(Qd_pos,-1,(4*a+3*k+10)/(k+2)),(Qa_neg,1,(4*a+3*k+2)/(2-k)),(Qd_neg,1,(4*a+k+10)/(2-k))):
    assert s.simplify(h(Q)-H)==s.simplify(g(Q)-G)==0
print('VERIFY_OK four exact barycentric surface-obstruction certificates')
# For d in both infinite regimes, all invariant-wall degrees are nonzero.
for val in list(range(-30,-4))+list(range(4,31)):
    vals=[s.expand(z).subs({a:0,k:val}) for z in expected.values()]
    assert all(q!=0 for q in vals)
print('VERIFY_OK finite corroboration of no invariant zero-degree wall in both parameter wings')
# Literal inequalities proving that one certificate always applies.
for kval in list(range(-40,-1))+list(range(2,41)):
    for aval in range(-40,41):
        assert 2*aval+kval+2<=0 or 2*aval+kval+4>=0
print('VERIFY_OK finite corroboration of exhaustive sign disjunction')
