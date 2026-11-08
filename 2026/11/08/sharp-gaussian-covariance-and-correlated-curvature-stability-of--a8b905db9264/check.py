"""Exact-arithmetic tests for the randomized-coordinate Langevin covariance theorem.

Run with Python 3 standard library: python3 check.py
Finite checks are supplemental; the universal claims require the analytic proof.
"""
from fractions import Fraction as Q
from math import sqrt

checks = 0

def ok(value, label):
    global checks
    if not value:
        raise AssertionError(label)
    checks += 1

def matrix(a):
    return [[Q(v) for v in row] for row in a]

def eye(d):
    return [[Q(i == j) for j in range(d)] for i in range(d)]

def mm(a,b):
    return [[sum(a[i][k]*b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]

def tr(a):
    return sum(a[i][i] for i in range(len(a)))

def trans(a):
    return list(map(list,zip(*a)))

def add(a,b):
    return [[a[i][j]+b[i][j] for j in range(len(a[0]))] for i in range(len(a))]

def mul(a,q):
    return [[q*v for v in row] for row in a]

def inv(a):
    d=len(a)
    z=[row[:]+eye(d)[i] for i,row in enumerate(a)]
    for k in range(d):
        pivot=next(i for i in range(k,d) if z[i][k] != 0)
        z[k],z[pivot]=z[pivot],z[k]
        v=z[k][k]
        z[k]=[x/v for x in z[k]]
        for i in range(d):
            if i!=k:
                v=z[i][k]
                z[i]=[z[i][j]-v*z[k][j] for j in range(2*d)]
    return [row[d:] for row in z]

def transfer(h,H,S):
    d=len(H)
    out=mul(S,Q(0))
    for j in range(d):
        M=eye(d)
        for k in range(d):
            M[j][k]-=d*h*H[j][k]
        out=add(out,mul(mm(mm(M,S),trans(M)),Q(1,d)))
    return out

def cov_2d(h,a,b,c):
    # Exact stationary covariance from the three moment equations.
    A=matrix([[a-h*a*a, c*(1-2*h*a), -h*c*c],
              [c, a+b, c],
              [-h*c*c,c*(1-2*h*b),b-h*b*b]])
    R=matrix([[1],[0],[1]])
    V=mm(inv(A),R)
    return matrix([[V[0][0],V[1][0]],[V[1][0],V[2][0]]])

# Uniform-diagonal universality, including nontrivial correlations and dimensions.
for H0 in [
    [[3]],
    [[3,1],[1,3]],
    [[4,1,-1],[1,4,1],[-1,1,4]],
    [[5,1,0,0],[1,5,1,0],[0,1,5,1],[0,0,1,5]],
    [[8,2,-1],[2,8,2],[-1,2,8]],
]:
    H=matrix(H0);d=len(H);a=H[0][0];iH=inv(H)
    for ratio in [Q(1,17),Q(1,4),Q(3,5),Q(9,10)]:
        h=ratio*Q(2)/(d*a)
        Sigma=mul(iH,Q(1)/(1-Q(d)*a*h/2))
        lhs=add(transfer(h,H,Sigma),mul(eye(d),2*h))
        for i in range(d):
            for j in range(d):
                ok(lhs[i][j]==Sigma[i][j],"uniform diagonal covariance identity")
        term=add(transfer(h,H,iH),mul(iH,-1))
        for i in range(d):
            for j in range(d):
                ok(term[i][j]==(-2*h+d*h*h*a)*Q(i==j),"target covariance drift")

# The exact three-moment recurrences, with random affine coordinate directions.
for a,b,c in [(Q(1),Q(4),Q(1)), (Q(5),Q(2),Q(1)), (Q(3),Q(3),Q(2)),
              (Q(9),Q(5),Q(-3)), (Q(3,2),Q(7,2),Q(1,2))]:
    H=matrix([[a,c],[c,b]])
    for h in [Q(1,100)/max(a,b),Q(1,20)/max(a,b),Q(1,4)/max(a,b)]:
        S=cov_2d(h,a,b,c)
        actual=add(transfer(h,H,S),mul(eye(2),2*h))
        for i in range(2):
            for j in range(2):
                ok(actual[i][j]==S[i][j],"exact anisotropic covariance fixed point")
        ok(S[0][0]>0 and S[1][1]>0 and S[0][0]*S[1][1]-S[0][1]**2>0,
           "stationary positive-definite covariance")
        ok((a+b)*S[0][1]+c*(S[0][0]+S[1][1])==0,
           "off-diagonal covariance constraint")

# Exact symmetric 2x2 gain matrix and threshold numerics.
for a,b,c in [(1,4,1),(4,1,1),(3,3,2),(10,3,5),(7,2,3)]:
    a,b,c=Q(a),Q(b),Q(c)
    ok(a*b>c*c,"SPD hypothesis")
    t=a+b;delta=c*c/t
    K=matrix([[a-delta,delta],[delta,b-delta]])
    trace=tr(K); discriminant=(K[0][0]-K[1][1])**2+4*K[0][1]**2
    lam=(float(trace)+sqrt(float(discriminant)))/2
    hstar=1/lam
    ok(hstar>=1/float(max(a,b))-1e-12,"sharp gain vs diagonal constraint")
    ok(hstar<((1+sqrt(2))/2)/float(max(a,b))+1e-12,"universal gain ceiling")
    if a!=b and c!=0:
        ok(hstar>1/float(max(a,b))+1e-12,"strict correlation gain")
    if a==b:
        ok(abs(hstar-1/float(a))<1e-12,"equal diagonal exact threshold")

# Supremal gain from nearly singular SPD targets.
r=sqrt(2)-1
ok(abs((1+r)/(1+r*r)-(1+sqrt(2))/2)<1e-14,"sharp bound profile")
# Check covariance variance blowup while approaching the sharp threshold from below.
a,b,c=Q(1),Q(4),Q(1)
trace=Q(5)-Q(2,5)
D=Q(9)+Q(4,25)
hstar=1/((float(trace)+sqrt(float(D)))/2)
for h1,h2 in [(Q(1,4),Q(13,50)), (Q(13,50),Q(131,500))]:
    ok(float(h2)<hstar,"below exact threshold")
    v1=tr(cov_2d(h1,a,b,c));v2=tr(cov_2d(h2,a,b,c))
    ok(v2>v1,"variance diverges near mean square instability")

print("PASS",checks,"exact-rational and independent floating threshold assertions")
print("witness H=[[1,1],[1,4]]: hstar",format(hstar,'.16f'),"diagonal baseline",.25)
print("unattained universal maximal multiplicative gain",format((1+sqrt(2))/2,'.16f'))
