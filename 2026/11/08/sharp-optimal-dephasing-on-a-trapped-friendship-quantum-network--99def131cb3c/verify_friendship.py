#!/usr/bin/env python3
"""Reproducible symbolic certificate and independent finite-Liouvillian checks.
Requires Python 3, numpy, scipy, sympy. All assertions are self-contained.
"""
import numpy as np
import sympy as sp
from scipy.linalg import solve

# Coordinates for operators fixed by permutations of the m-1 undistinguished
# triangles and swapping the two vertices within each such triangle.
COORDS = ['tt','pp','hh','bb',
          'Re(tp)','Im(tp)','Re(th)','Im(th)','Re(ph)','Im(ph)',
          'Re(tb)','Im(tb)','Re(pb)','Im(pb)','Re(hb)','Im(hb)',
          'Re(b,b_partner)','Re(b,b_other)']

def graph(m):
    n=2*m+1
    a=np.zeros((n,n),dtype=float)
    for j in range(m):
        x,y=(0,1) if j==0 else (3+2*(j-1),4+2*(j-1))
        for u,v in [(x,y),(x,2),(y,2)]:
            a[u,v]=a[v,u]=1.
    return a

def orbit_bases(m):
    n=2*m+1
    bulk=list(range(3,n))
    paired=[(3+2*j,4+2*j) for j in range(m-1)]
    paired_set=set(paired)
    cross=[(u,v) for i,u in enumerate(bulk) for v in bulk[i+1:]
           if (u,v) not in paired_set]
    blocks=[]
    def push_diag(vertices):
        x=np.zeros((n,n),dtype=complex)
        for v in vertices:x[v,v]=1
        blocks.append(x)
    for vertices in [[0],[1],[2],bulk]:push_diag(vertices)
    edges=[[(0,1)],[(0,2)],[(1,2)]]+[
        [(v,b) for b in bulk] for v in [0,1,2]]
    for edge_set in edges:
        for imaginary in [False,True]:
            x=np.zeros((n,n),dtype=complex)
            for u,v in edge_set:
                x[u,v]=1j if imaginary else 1
                x[v,u]=-1j if imaginary else 1
            blocks.append(x)
    for edge_set in [paired,cross]:
        x=np.zeros((n,n),dtype=complex)
        for u,v in edge_set:x[u,v]=x[v,u]=1
        blocks.append(x)
    assert len(blocks)==18
    return blocks

def coordinates(x):
    out=[x[q,q].real for q in range(4)]
    # Note coordinates[3] is the first generic peripheral site (index 3).
    out[3]=x[3,3].real
    for a,b in [(0,1),(0,2),(1,2),(0,3),(1,3),(2,3)]:
        out.extend([x[a,b].real,x[a,b].imag])
    out.extend([x[3,4].real,x[3,5].real])
    return np.asarray(out,dtype=float)

def reduced(m, gamma, kappa=2, J=1):
    a=graph(m);n=a.shape[0]
    sink=np.zeros_like(a);sink[0,0]=1
    def generator(x):
        return (-1j*J*(a@x-x@a)
                -gamma*(x-np.diag(np.diag(x)))
                -kappa/2*(sink@x+x@sink))
    return np.column_stack([coordinates(generator(v)) for v in orbit_bases(m)])

def integer_matrix(x):
    for y in x.flat:assert abs(y-round(y))<1e-10, y
    return sp.Matrix([[int(round(x[i,j])) for j in range(18)]
                      for i in range(18)])

def symbolic_certificate():
    m,g=sp.symbols('m g',positive=True)
    def affine(m3,m4):
        return m3+(m-3)*(m4-m3)
    A3=integer_matrix(reduced(3,0,0)); A4=integer_matrix(reduced(4,0,0))
    B3=integer_matrix(reduced(3,1,0))-A3
    B4=integer_matrix(reduced(4,1,0))-A4
    C3=integer_matrix(reduced(3,0,2))-A3
    C4=integer_matrix(reduced(4,0,2))-A4
    M=affine(A3,A4)+g*affine(B3,B4)+affine(C3,C4)
    # The generator changes only one matrix index at a time; each entry is
    # affine in m, so the two-size interpolation is exact for all m>=3.
    for t in [5,6,7,9]:
        for r in [0,1,3]:
            exact=integer_matrix(reduced(t,r,2))
            assert M.subs({m:t,g:r})==exact
    rhs=sp.zeros(18,1)
    rhs[3]=-1/(2*(m-1))
    integrated=M.inv()*rhs
    T=sp.factor(integrated[0]+integrated[1]+integrated[2]
                +2*(m-1)*integrated[3])
    N,D=sp.fraction(T)
    assert sp.simplify(T-sp.factor(N/D))==0
    y=sp.symbols('y',nonnegative=True)
    for label,p in [('numerator',N),('denominator',D)]:
        pp=sp.Poly(sp.expand(p.subs(m,y+2)),g,y)
        assert all(c>=0 for _,c in pp.terms()),label
    assert sp.factor(sp.limit(g*T,g,0))==2*m-3
    assert sp.simplify(sp.limit(T/g,g,sp.oo)-(2*m+1)/3)==0
    assert sp.simplify(sp.limit(T/m**2,m,sp.oo)-2/(2*g+1))==0
    z,u=sp.symbols('z u',positive=True)
    F=sp.factor(sp.limit(T.subs({m:1/u**2,g:z/u})*u**3,u,0,dir='+'))
    expected=2*(z*z+1)*(z*z+2)/(z*(3*z*z+4))
    assert sp.simplify(F-expected)==0
    assert sp.simplify(sp.diff(F,z)-2*(3*z**6+3*z**4-6*z*z-8)/(z*z*(3*z*z+4)**2))==0
    # Coefficientwise nonnegative-polynomial certificates, using y=m-2>=1.
    y=sp.symbols('y',nonnegative=True)
    certificates={
        'T>=m^2/[4(g+1)]':sp.expand(((g+1)*N-sp.Rational(1,4)*m*m*D).subs(m,y+2)),
        'T>=mg/4':sp.expand((N-sp.Rational(1,4)*m*g*D).subs(m,y+2)),
    }
    for label,expression in certificates.items():
        polynomial=sp.Poly(expression,g,y)
        assert polynomial.terms() and all(coef>=0 for _,coef in polynomial.terms()),label
        print(label,'PASS, nonnegative coefficients:',len(polynomial.terms()))
    for t in [3,4,5,6,8,12,20,50]:
        for h in [sp.Rational(1,5),sp.Rational(1,2),sp.Integer(1),sp.Integer(3),sp.Integer(7)]:
            actual=sp.simplify(T.subs({m:t,g:h}))
            mat=M.subs({m:t,g:h}); b=rhs.subs(m,t)
            vv=mat.inv()*b
            check=sp.factor(vv[0]+vv[1]+vv[2]+2*(t-1)*vv[3])
            assert actual==check
    print('symbolic exact identity PASS; rational T has',len(sp.Poly(N,m,g).terms()),'numerator monomials and',len(sp.Poly(D,m,g).terms()),'denominator monomials')
    print('scaling F(z)=',F)
    return T

def finite_independent_checks(T):
    m,g=sp.symbols('m g',positive=True)
    for count in range(3,8):
        A=graph(count); n=A.shape[0]; eye=np.eye(n)
        trap=np.zeros_like(A);trap[0,0]=1
        for rate in [0.25,1.0,3.0]:
            # Full N^2-dimensional complex Liouvillian in column-major order.
            L=(-1j*(np.kron(eye,A)-np.kron(A.T,eye))
               -np.kron(eye,trap)-np.kron(trap,eye))
            for i in range(n):
                for j in range(n):
                    if i!=j:L[i+n*j,i+n*j]-=rate
            initial=np.zeros(n*n);initial[3+n*3]=1
            x=solve(-L,initial)
            truth=np.trace(x.reshape((n,n),order='F')).real
            predicted=float(T.subs({m:count,g:sp.Rational(str(rate))}))
            assert abs(truth-predicted)<1e-7,(count,rate,truth,predicted)
    print('full Liouvillian check PASS: 15 comparisons, m=3..7, gamma=1/4,1,3')

if __name__=='__main__':
    value=symbolic_certificate()
    finite_independent_checks(value)
    print('CERTIFICATE PASS')
