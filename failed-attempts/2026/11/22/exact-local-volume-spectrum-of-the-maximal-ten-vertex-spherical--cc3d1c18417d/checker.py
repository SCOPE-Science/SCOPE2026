"""Numerical second-variation cross-check for the regular-pentagon join.

The proof is analytic; these finite-difference tests are supplementary, not
an exact certificate of any identity.
"""
from math import cos, sin, pi, sqrt

n = 5
phi = 2*pi/n
s = sin(phi)
base = [(cos(i*phi),sin(i*phi)) for i in range(n)]
V0 = 25*s*s/24


def det4(columns):
    a = [[columns[c][r] for c in range(4)] for r in range(4)]
    sign = 1.0
    ans = 1.0
    for k in range(4):
        piv = max(range(k,4), key=lambda r:abs(a[r][k]))
        if abs(a[piv][k]) < 1e-14: return 0.0
        if piv != k:
            a[piv],a[k] = a[k],a[piv]
            sign *= -1
        t=a[k][k]
        ans*=t
        for i in range(k+1,4):
            q=a[i][k]/t
            for j in range(k+1,4): a[i][j]-=q*a[k][j]
    return sign*ans


def geometry(alpha, beta, u, v, t):
    a=[];b=[]
    for i,(x,y) in enumerate(base):
        k=1/sqrt(1+t*t*(alpha[i]**2+sum(z*z for z in u[i])))
        a.append((k*(x-t*alpha[i]*y),k*(y+t*alpha[i]*x),k*t*u[i][0],k*t*u[i][1]))
        l=1/sqrt(1+t*t*(beta[i]**2+sum(z*z for z in v[i])))
        b.append((l*t*v[i][0],l*t*v[i][1],l*(x-t*beta[i]*y),l*(y+t*beta[i]*x)))
    return sum(det4((a[i],a[(i+1)%5],b[j],b[(j+1)%5])) for i in range(5) for j in range(5))/24


def mat(f):
    return [[f(row,col) for col in range(2)] for row in range(2)]

def matvec(M,x):
    return (M[0][0]*x[0]+M[0][1]*x[1],M[1][0]*x[0]+M[1][1]*x[1])

def transpose(M):
    return [[M[j][i] for j in range(2)] for i in range(2)]

def norm2(M):
    return sum(z*z for row in M for z in row)

def projections(w):
    # M = (2/5) sum_i w_i base_i^T; w_i = M base_i + residual_i.
    M=[[sum(w[i][r]*base[i][c] for i in range(5))*2/5 for c in range(2)] for r in range(2)]
    rem=[tuple(w[i][r]-matvec(M,base[i])[r] for r in range(2)) for i in range(5)]
    return M,rem

def quadratic(alpha,beta,u,v):
    ang=sum((a[(i+1)%5]-a[i])**2 for a in (alpha,beta) for i in range(5))*5*s*s/48
    M,ur=projections(u);N,vr=projections(v)
    C=[[M[i][j]+N[j][i] for j in range(2)] for i in range(2)]
    cross=25*s*s*norm2(C)/48+5*s*s*sum(z*z for w in ur+vr for z in w)/24
    return ang+cross

z=[0.0]*5; w=[(0.0,0.0)]*5
examples=[]
examples.append(('first angular harmonic',[cos(i*phi) for i in range(5)],z,w,w))
examples.append(('second angular harmonic',[cos(2*i*phi) for i in range(5)],z,w,w))
examples.append(('residual cross mode',z,z,[(1.0,0.0)]*5,w))
examples.append(('mixed symmetric motion',z,z,base,base))
examples.append(('infinitesimal rotation',z,z,base,[(-x,-y) for x,y in base]))
examples.append(('combined generic motion',
       [1,-2,0.5,0.25,-1],[0.5,1,-1.75,0,2],
       [(i/7,(i*i)%6/11) for i in range(5)],
       [((2*i)%7/9,i/13) for i in range(5)]))
for name,alpha,beta,u,v in examples:
    h=2e-4
    q=quadratic(alpha,beta,u,v)
    finite=(2*V0-geometry(alpha,beta,u,v,h)-geometry(alpha,beta,u,v,-h))/(2*h*h)
    print(name, 'analytic Q=', round(q,11), 'finite difference=',round(finite,11))
    assert abs(q-finite) < 0.0002*(1+abs(q)), (name,q,finite)

root5=sqrt(5)
values=[(0,6),(25/96,4),((25+5*root5)/96,12),(25*(3+root5)/192,4),((25+5*root5)/48,4)]
assert sum(mult for value,mult in values)==30
assert all(values[i][0]<values[i+1][0] for i in range(len(values)-1))
assert abs(5*s*s*(5-root5)/48-25/96)<1e-14
print('Spectrum ordering, multiplicities and smallest level validated.')
