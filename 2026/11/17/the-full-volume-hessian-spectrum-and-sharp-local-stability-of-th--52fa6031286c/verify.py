"""Independent finite consistency checks for the nine-vertex volume-Hessian formula.

Standard Python library only. A finite check supplements but cannot replace the
analytical proof in RESULT.md. Run: python verify.py
"""
from math import cos, sin, pi, sqrt, hypot
from random import Random

M, N = 4, 5
A, B = sin(2*pi/M), sin(2*pi/N)
U = [(cos(2*pi*i/M), sin(2*pi*i/M)) for i in range(M)]
W = [(cos(2*pi*j/N), sin(2*pi*j/N)) for j in range(N)]
BASE = [(u[0],u[1],0.,0.) for u in U]+[(0.,0.,w[0],w[1]) for w in W]
V0 = M*N*A*B/24
checked=0

def dot(a,b): return sum(x*y for x,y in zip(a,b))
def norm2(a): return dot(a,a)
def cyc_diff_sq(z): return sum((z[(i+1)%len(z)]-z[i])**2 for i in range(len(z)))

def pts(alpha,beta,x,y,t):
    out=[]
    for i,(cx,sx) in enumerate(U):
        d=2*pi*i/M+t*alpha[i]
        scale=sqrt(1-t*t*norm2(x[i]))
        out.append((scale*cos(d),scale*sin(d),t*x[i][0],t*x[i][1]))
    for j,(cx,sx) in enumerate(W):
        d=2*pi*j/N+t*beta[j]
        scale=sqrt(1-t*t*norm2(y[j]))
        out.append((t*y[j][0],t*y[j][1],scale*cos(d),scale*sin(d)))
    return out

def bivector_area(points):
    a=[0.]*6
    coords=[(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]
    for i,p in enumerate(points):
        q=points[(i+1)%len(points)]
        for k,(h,j) in enumerate(coords):
            a[k]+=p[h]*q[j]-p[j]*q[h]
    return a

def volume(points):
    x=bivector_area(points[:M]);y=bivector_area(points[M:])
    return (x[0]*y[5]-x[1]*y[4]+x[2]*y[3]+x[3]*y[2]-x[4]*y[1]+x[5]*y[0])/24

def quadratic_raw(alpha,beta,x,y):
    cross=sum(dot(U[i],y[j])*dot(x[i],W[j]) for i in range(M) for j in range(N))
    return A*B/24*(N*sum(norm2(q) for q in x)+M*sum(norm2(q) for q in y)+4*cross+
                   N/2*cyc_diff_sq(alpha)+M/2*cyc_diff_sq(beta))

def quadratic_sos(alpha,beta,x,y):
    # K has rows in the second plane and columns in the first; L the reverse.
    K=[[sum(x[i][r]*U[i][c] for i in range(M))*2/M for c in range(2)] for r in range(2)]
    L=[[sum(y[j][r]*W[j][c] for j in range(N))*2/N for c in range(2)] for r in range(2)]
    R=[tuple(x[i][r]-sum(K[r][c]*U[i][c] for c in range(2)) for r in range(2)) for i in range(M)]
    S=[tuple(y[j][r]-sum(L[r][c]*W[j][c] for c in range(2)) for r in range(2)) for j in range(N)]
    return A*B/24*(M*N/2*sum((K[r][c]+L[c][r])**2 for r in range(2) for c in range(2))+
                   N*sum(norm2(q) for q in R)+M*sum(norm2(q) for q in S)+
                   N/2*cyc_diff_sq(alpha)+M/2*cyc_diff_sq(beta))

assert abs(volume(BASE)-V0)<1e-14
checked+=1
rng=Random(20261106)
for q in range(300):
    alpha=[rng.uniform(-1.,1.) for _ in range(M)]
    beta=[rng.uniform(-1.,1.) for _ in range(N)]
    x=[(rng.uniform(-1.,1.),rng.uniform(-1.,1.)) for _ in range(M)]
    y=[(rng.uniform(-1.,1.),rng.uniform(-1.,1.)) for _ in range(N)]
    Q=quadratic_raw(alpha,beta,x,y)
    assert Q>-2e-13
    assert abs(Q-quadratic_sos(alpha,beta,x,y))<3e-13
    checked+=2
    for t in (0.001,0.0005,0.00025):
        dv=V0-volume(pts(alpha,beta,x,y,t))
        assert abs(dv-Q*t*t)<8.0*t**3
        checked+=1

# Orthogonal group gives exact zero-volume-loss families.
for t in (0.01,0.02,0.1,0.3,0.5):
    ct,st=cos(t),sin(t)
    rotated=[]
    for z in BASE:
        w=list(z)
        w[0]=ct*z[0]-st*z[2]
        w[2]=st*z[0]+ct*z[2]
        rotated.append(tuple(w))
    assert abs(volume(rotated)-V0)<3e-14
    checked+=1

# Five-dimensional pentagon-angle Fourier spectrum has two twofold levels.
for k, expected in ((1,B*(5-sqrt(5))/24),(2,B*(5+sqrt(5))/24)):
    alpha=[0.]*M
    beta=[cos(2*pi*k*j/N) for j in range(N)]
    x=[(0.,0.)]*M;y=[(0.,0.)]*N
    tangent_norm=sum(p*p for p in beta)
    assert abs(quadratic_raw(alpha,beta,x,y)/tangent_norm-expected)<5e-14
    checked+=1

# Construct all 27 orthonormal tangent basis vectors.
E=[]
for i in range(M):
    E.append((i,(-U[i][1],U[i][0],0.,0.)))
    E.append((i,(0.,0.,1.,0.)))
    E.append((i,(0.,0.,0.,1.)))
for j in range(N):
    E.append((M+j,(1.,0.,0.,0.)))
    E.append((M+j,(0.,1.,0.,0.)))
    E.append((M+j,(0.,0.,-W[j][1],W[j][0])))
assert len(E)==27

def expchart(z):
    out=[]
    for i,p in enumerate(BASE):
        x=[0.,0.,0.,0.]
        for k,(idx,w) in enumerate(E):
            if idx==i:
                for q in range(4): x[q]+=w[q]*z[k]
        rho=sqrt(norm2(x))
        sinc=sin(rho)/rho if rho else 1.
        out.append(tuple(cos(rho)*p[q]+sinc*x[q] for q in range(4)))
    return out

def jacobi_eigenvalues(a):
    # Orthogonal similarity transformations of a real symmetric matrix.
    a=[row[:] for row in a]
    n=len(a)
    for sweep in range(70):
        maxoff=0.
        for i in range(n):
            for j in range(i+1,n):
                z=a[i][j];maxoff=max(maxoff,abs(z))
                if abs(z)<1e-12:continue
                theta=0.5*(a[j][j]-a[i][i])/z
                t=(1 if theta>=0 else -1)/(abs(theta)+sqrt(1+theta*theta))
                c=1/sqrt(1+t*t);s=t*c
                ai=a[i][i];aj=a[j][j]
                a[i][i]=ai-t*z;a[j][j]=aj+t*z
                a[i][j]=a[j][i]=0.
                for k in range(n):
                    if k==i or k==j:continue
                    ki,kj=a[k][i],a[k][j]
                    a[k][i]=a[i][k]=c*ki-s*kj
                    a[k][j]=a[j][k]=s*ki+c*kj
        if maxoff<2e-12:break
    return sorted(a[i][i] for i in range(n))

# Independent numerical Hessian of the signed-volume polynomial on the sphere.
h=2e-4
I=[[h*(i==j) for j in range(27)] for i in range(27)]
negH=[[0.]*27 for _ in range(27)]
for i in range(27):
    for j in range(i,27):
        if i==j:
            f=(volume(expchart(I[i]))-2*V0+volume(expchart([-v for v in I[i]])))/h**2
            checked+=2
        else:
            pp=[I[i][k]+I[j][k] for k in range(27)]
            pm=[I[i][k]-I[j][k] for k in range(27)]
            f=(volume(expchart(pp))-volume(expchart(pm))-
               volume(expchart([-v for v in pm]))+volume(expchart([-v for v in pp])))/(4*h*h)
            checked+=4
        negH[i][j]=negH[j][i]=-f/2
spec=jacobi_eigenvalues(negH)
expected=sorted([0.]*6+[B*(5-sqrt(5))/24]*2+[B/6]*6+[5*B/24]*6+
                [B*(5+sqrt(5))/24]*2+[3*B/8]*4+[5*B/12])
assert max(abs(x-y) for x,y in zip(spec,expected))<3e-7
checked+=27
print('PASS:',checked,'finite checks; maximal Hessian-spectrum error:',max(abs(x-y) for x,y in zip(spec,expected)))
print('Sharp local quadratic coefficient:',B*(5-sqrt(5))/24)
