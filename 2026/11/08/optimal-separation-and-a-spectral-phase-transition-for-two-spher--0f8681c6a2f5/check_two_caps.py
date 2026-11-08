"""Exact rational checks for the quadratic-harmonic two-cap Gram law.

Run: python3 check_two_caps.py
Uses only Python's standard library. Finite checks support but do not prove
all-parameter assertions in the accompanying mathematical argument.
"""
from fractions import Fraction as F
from itertools import combinations
from math import sqrt

def f(x): return F(x)
def dot(a,b): return sum(x*y for x,y in zip(a,b))
def mv(A,v): return tuple(dot(row,v) for row in A)
def inn(A,B): return sum(A[i][j]*B[i][j] for i in range(3) for j in range(3))
def bil(A,x,y): return dot(x,mv(A,y))
def mat(d): return tuple(tuple(F(d[i][j]) for j in range(3)) for i in range(3))

def basis():
    D=[]
    for d in [[[1,0,0],[0,-1,0],[0,0,0]],
              [[1,0,0],[0,1,0],[0,0,-2]]]: D.append(mat(d))
    for i,j in combinations(range(3),2):
        a=[[0]*3 for _ in range(3)];a[i][j]=a[j][i]=1;D.append(mat(a))
    return D
B=basis()

def coeff(t):
    mu2=F(1,2)-F(15,16)*t+F(5,8)*t**3-F(3,16)*t**5
    beta=F(15,8)*t*(1-t*t)**2
    gamma=F(15,32)*t*(1-t*t)*(7*t*t-3)
    return mu2,beta,gamma

def cap_integral(A,C,t,u,e,w):
    # Integrate the azimuthal fourth moment independently of the cap eigenspace law.
    I0=(1-t)/2; I2=(1-t**3)/6; I4=(1-t**5)/10
    au=bil(A,u,u); cu=bil(C,u,u)
    a11=bil(A,e,e); a22=bil(A,w,w); a12=bil(A,e,w)
    c11=bil(C,e,e); c22=bil(C,w,w); c12=bil(C,e,w)
    Q=(3*a11*c11+3*a22*c22+a11*c22+a22*c11+4*a12*c12)/8
    return I4*au*cu+(I2-I4)*(2*dot(mv(A,u),mv(C,u))-3*au*cu)+(I0-2*I2+I4)*Q

def model(A,C,t,u):
    mu2,beta,gamma=coeff(t)
    return mu2*inn(A,C)+beta*dot(mv(A,u),mv(C,u))+gamma*bil(A,u,u)*bil(C,u,u)

def cap_matrix(t,c,s,sign=1):
    u=(c,F(0),sign*s); e=(sign*s,F(0),-c); w=(F(0),F(1),F(0))
    M=[[F(15,2)*cap_integral(A,C,t,u,e,w) for C in B] for A in B]
    N=[[model(A,C,t,u) for C in B] for A in B]
    assert M==N, (t,c,s)
    return M

def test_pair(t,c,s):
    assert c*c+s*s==1
    q=c*c-s*s
    assert q<=2*t*t-1, ('caps not disjoint',t,q)
    P=cap_matrix(t,c,s)
    Q=cap_matrix(t,c,s,-1)
    M=[[P[i][j]+Q[i][j] for j in range(5)] for i in range(5)]
    mu2,beta,gamma=coeff(t)
    assert beta>0 and beta+gamma>0
    # Indices: D1, D2, xy, xz, yz. Their squared Frobenius norms are 2,6,2,2,2.
    for i in range(2):
        for j in range(2,5): assert M[i][j]==M[j][i]==0
    for i in range(2,5):
        for j in range(2,5):
            if i!=j: assert M[i][j]==0
    assert M[2][2]/2==2*mu2+beta*(1+q)/2
    assert M[4][4]/2==2*mu2+beta*(1-q)/2
    assert M[3][3]/2==2*mu2+beta+gamma*(1-q*q)
    a=M[0][0]/2-2*mu2
    d=M[1][1]/6-2*mu2
    b2=M[0][1]**2/12
    tau=(4*beta+gamma*(1+3*q*q))/3
    det=beta*(beta+gamma)*(1-q*q)/3
    assert a+d==tau
    assert a*d-b2==det
    # Exact determinant and trace, not numerical roots, certify the remaining block.
    return q,mu2,beta,gamma

cases=0
for t in map(F,['1/10','1/5','1/3','1/2','3/5','7/10','3/4','4/5','9/10','19/20']):
    for c,s in [(F(11,61),F(60,61)),(F(9,41),F(40,41)),
                (F(5,13),F(12,13)),(F(3,5),F(4,5)),(F(4,5),F(3,5))]:
        if c*c-s*s>2*t*t-1: continue
        test_pair(t,c,s);cases+=1
assert cases>=25
print('EXACT_CAP_MOMENT_TENSORS_AND_FIVE_EIGEN_SECTORS_OK',cases)

# Verify that our proposed optimum has a strictly higher least eigenvalue
# than all tested alternative feasible separations, across the phase boundary.
def least(t,q):
    mu2,b,g=coeff(t)
    T=(4*b+g*(1+3*q*q))/3
    D=b*(b+g)*(1-q*q)/3
    lo=(float(T)-sqrt(max(0,float(T*T-4*D))))/2
    return float(2*mu2)+min(float(b)*(1-abs(float(q)))/2,lo)
count=0
for ti in range(1,100):
    t=ti/100
    hi=2*t*t-1
    qstar=min(0.,hi)
    best=least(t,qstar)
    for j in range(201):
        q=-1+(hi+1)*j/200
        if abs(q-qstar)<1e-9:continue
        assert best>least(t,q)-1e-10, (t,qstar,q,best,least(t,q))
        count+=1
print('TWO_CAP_ANGLE_OPTIMALITY_GRID_OK',count)

# Sharp switched worst eigenspace at the optimal orthogonal geometry.
for ti in range(71,100):
    t=ti/100
    if t<sqrt(.5):continue
    q=0.
    mu2,b,g=coeff(F(ti,100))
    side=(b+g)/3-b/2
    if t<sqrt(5)/3: assert side<0
    elif t>sqrt(5)/3: assert side>0
    assert abs(least(F(ti,100),q)-(float(2*mu2)+min(float((b+g)/3),float(b/2))))<1e-12
print('ORTHOGONAL_THREE_MODE_TRANSITION_OK', 't_squared=5/9')
print('ALL_QUADRATIC_SPHERICAL_TWO_CAP_CHECKS_OK')
