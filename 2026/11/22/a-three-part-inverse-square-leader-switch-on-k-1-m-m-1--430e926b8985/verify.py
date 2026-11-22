#!/usr/bin/env python3
"""Exact checks for two-leader inverse-square optimization on K_{1,m,m+1}."""
import itertools
import sympy as sp

m,z,N,d,e = sp.symbols('m z N d e', positive=True)


def e_same(D, NN):
    return NN**2/(4*D**2)-1/D-2/D**2-1/NN**2


def e_cross(D, E, NN):
    return (1/(NN-1)**2-2/(D+E)+(NN+1)**2/(D+E)**2
            -2/NN**2-1/D**2-1/E**2)


def extras(k):
    nn=2*k+2
    da,db,dc=nn-1,k+2,k+1
    return {'AB': e_cross(da,db,nn), 'AC': e_cross(da,dc,nn),
            'BB':e_same(db,nn), 'BC': e_cross(db,dc,nn),
            'CC':e_same(dc,nn)}


def base(k):
    nn=2*k+2
    return sp.Rational(2,nn**2)+sp.Rational(k-1,(k+2)**2)+sp.Rational(k,(k+1)**2)


def laplacian(k):
    parts=[1,k,k+1]
    labels=sum(([i]*c for i,c in enumerate(parts)),[])
    mat=sp.zeros(len(labels))
    for i in range(len(labels)):
        for j in range(i+1,len(labels)):
            if labels[i]!=labels[j]:
                mat[i,i]+=1;mat[j,j]+=1;mat[i,j]=-1;mat[j,i]=-1
    return mat,labels


def pair_type(i,j):
    return ''.join(sorted('ABC'[i]+'ABC'[j]))


def matrix_cost(mat, pair):
    I=[i for i in range(mat.rows) if i not in pair]
    Q=mat.extract(I,I)
    W=Q.inv()
    return sp.trace(W*W)


def check():
    # First prove the rational resolvent identities symbolically.
    a=1/(z+d); b=1/(z+e); c=1/(z*(z+N))
    offd=c-1/((z+N)*(z+d)); offe=c-1/((z+N)*(z+e))
    same=(a+offd)**2-offd**2
    cross=(a+offd)*(b+offe)-c*c
    stated_same=(z*z+N*z+2*d)/(z*(z+N)*(z+d)**2)
    stated_cross=((z+N-1)*(z*z+(N+1)*z+d+e)
                  /(z*(z+N)**2*(z+d)*(z+e)))
    assert sp.cancel(same-stated_same)==0
    assert sp.cancel(cross-stated_cross)==0
    # Differentiating determinants gives exactly the inverse-square extras.
    log_same=sp.log(z*z+N*z+2*d)-sp.log(z+N)-2*sp.log(z+d)
    log_cross=(sp.log(z+N-1)+sp.log(z*z+(N+1)*z+d+e)
               -2*sp.log(z+N)-sp.log(z+d)-sp.log(z+e))
    assert sp.simplify(-sp.limit(sp.diff(log_same,z,2),z,0)-e_same(d,N))==0
    assert sp.simplify(-sp.limit(sp.diff(log_cross,z,2),z,0)-e_cross(d,e,N))==0

    f=extras(m)
    expected={
      'AC': 2*(12*m**5+85*m**4+157*m**3+103*m**2+36*m+12)/(9*(m+1)**2*(m+2)**2*(3*m+2)**2),
      'BB': (20*m**3-20*m**2-87*m-42)/(36*(m+1)**2*(m+2)),
      'BC': 2*m*(20*m**4+62*m**3+44*m**2-24*m-21)/(9*(m+1)**2*(2*m+1)**2*(2*m+3)),
      'CC': (20*m**4+92*m**3+89*m**2-180*m-264)/(36*(m+1)**2*(m+2)**2)
    }
    for typ,gap in expected.items():
        assert sp.factor(f[typ]-f['AB']-gap)==0, typ
    # Every numerator after m=3+u has strictly positive coefficients.
    u=sp.symbols('u', nonnegative=True)
    numerators={
      'AC':12*m**5+85*m**4+157*m**3+103*m**2+36*m+12,
      'BB':20*m**3-20*m**2-87*m-42,
      'BC':20*m**4+62*m**3+44*m**2-24*m-21,
      'CC':20*m**4+92*m**3+89*m**2-180*m-264,
    }
    for typ,p in numerators.items():
        coeffs=sp.Poly(sp.expand(p.subs(m,3+u)),u).all_coeffs()
        assert all(t>0 for t in coeffs),typ
    # For m=2 check all four competing orbit gaps exactly.
    f2={k:sp.factor(v.subs(m,2)) for k,v in f.items()}
    assert {k:sp.factor(v-f2['BB']) for k,v in f2.items() if k!='BB'}=={
        'AB':sp.Rational(17,162), 'AC':sp.Rational(109,576),
        'BC':sp.Rational(1151,3150), 'CC':sp.Rational(37,144)}
    assert sp.factor((base(2)+f2['BB'])-sp.Rational(1,2))==0
    assert sp.factor((base(3)+f['AB'].subs(m,3))-sp.Rational(187,300))==0

    # Direct exact grounded-matrix inversions, all pairs of small instances.
    comparisons=0
    for k in range(2,6):
        L,labels=laplacian(k)
        possible=[]
        for pair in itertools.combinations(range(len(labels)),2):
            typ=pair_type(*(labels[i] for i in pair))
            actual=matrix_cost(L,pair)
            expected_value=base(k)+extras(sp.Integer(k))[typ]
            assert sp.factor(actual-expected_value)==0,(k,typ,pair)
            possible.append((actual,typ))
            comparisons+=1
        minval=min(val for val,typ in possible)
        expected_kind='BB' if k==2 else 'AB'
        assert {typ for val,typ in possible if val==minval}=={expected_kind}
    # Additional representative matrices for larger sizes.
    representative=0
    for k in range(6,11):
        L,labels=laplacian(k)
        for pair_type_str in ('AB','AC','BB','BC','CC'):
            i,j=('ABC'.index(ch) for ch in pair_type_str)
            first=labels.index(i)
            second=labels.index(j)+(i==j)
            assert pair_type(*(labels[t] for t in (first,second)))==pair_type_str
            actual=matrix_cost(L,(first,second))
            assert sp.factor(actual-(base(k)+extras(sp.Integer(k))[pair_type_str]))==0
            representative+=1
    print('VERIFY_OK rational_gap_identities=4 symbolic_resolvent=4'
          f' all_pair_exact_checks={comparisons} larger_representative_checks={representative}'
          ' polynomial_positive_certificates=4')

if __name__=='__main__':
    check()
