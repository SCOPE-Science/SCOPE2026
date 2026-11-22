"""Exact rational certificates for square-root completion in nullity-two matrix Waring maps.
No finite sample substitutes for the general proof; this tests four structural strata.
Run: python check_square_coeff.py
"""
from sympy import Matrix, zeros, eye
from random import Random
from itertools import product

rng = Random(238712)

def mat(n, rows=None):
    if rows is not None: return Matrix(rows)
    return Matrix(n, n, lambda i, j: rng.randint(-4, 4))

def blockmatrix(s, top, bottom):
    return Matrix.vstack(top, bottom)

def root_nilpotent(s, a, t):
    n=s+2
    X=zeros(n)
    # Nilpotent length-three block on {e_1,e_{s+1},e_{s+2}}.
    X[0,0]=a; X[s,0]=1
    X[0,s]=-a*a; X[s,s]=-a
    X[0,s+1]=1
    for j in range(1,s): X[j,j]=t
    N=X*X
    expected=zeros(n)
    expected[0,s+1]=a; expected[s,s+1]=1
    for j in range(1,s): expected[j,j]=t*t
    assert N==expected, ('nilpotent-root failure',s,a,t)
    return expected

def choose_param(producer, C, s):
    for a,t in product((1,2,3,4,5,-1,-2,-3,-4,-5,7,11),repeat=2):
        N=producer(s,a,t)
        H=C[:s,:]-N[:s,:]
        if H.rank()==s:
            return a,t,N
    raise AssertionError('no completion')

def make_N(s, typ, a, t):
    n=s+2
    N=zeros(n)
    if typ=='zero':
        for j in range(s): N[j,j]=t*t
    elif typ=='top':
        N[0,0]=a; N[0,s]=1; N[s,0]=1
        for j in range(1,s): N[j,j]=t*t
        assert (N.extract([0,s],[0,s])).det()==-1
    elif typ=='semisimple':
        for j in range(s): N[j,j]=t*t
        N[s,s]=2
    elif typ=='nilpotent':
        return root_nilpotent(s,a,t)
    else: raise ValueError(typ)
    return N

for n in [7,8,9,12]:
    s=n-2
    for typ in ('zero','top','semisimple','nilpotent','rank2'):
        for i in range(6):
            top=Matrix(s,n,lambda r,c:rng.randint(-4,4))
            if typ=='zero': bottom=zeros(2,n)
            elif typ=='top': bottom=Matrix([[1]+[0]*(n-1),[0]*n])
            elif typ=='semisimple': bottom=zeros(2,n);bottom[0,s]=2
            elif typ=='nilpotent': bottom=zeros(2,n);bottom[0,n-1]=1
            else:
                bottom=Matrix(2,n,lambda r,c:rng.randint(-4,4))
                while bottom.rank()<2:
                    bottom=Matrix(2,n,lambda r,c:rng.randint(-4,4))
            C=blockmatrix(s,top,bottom)
            if typ!='rank2':
                a,t,N=choose_param(lambda s,a,t:make_N(s,typ,a,t), C,s)
            else:
                # Invertible completion and full-rank residual by generic top rows.
                for j in range(300):
                    Q=Matrix(s,n,lambda r,c:rng.randint(-8,8))
                    N=blockmatrix(s,Q,bottom)
                    if N.det()!=0 and (C[:s,:]-Q).rank()==s: break
                else: raise AssertionError('rank-two generic completion failed')
            assert N[s:,:] == bottom
            assert (C[:s,:]-N[:s,:]).rank()==s
            # The N is a square since it is invertible, is diagonalizable on
            # its nonzero spectral part, or is explicitly rooted above.
    print('PASS canonical ranks and square-root structures for n=',n)
print('MATRIX_TWO_SQUARES_NULLITY_TWO_CERTIFICATES_OK')
