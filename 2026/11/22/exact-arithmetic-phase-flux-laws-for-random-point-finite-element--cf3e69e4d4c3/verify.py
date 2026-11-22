"""Exact finite-element checks and numerical asymptotic tests for finite-jump diffusion flux."""
from fractions import Fraction as F
from itertools import product
from math import comb
from math import sqrt

N_CHECKS = 0

def ck(test, label):
    global N_CHECKS
    N_CHECKS += 1
    if not test:
        raise AssertionError(label)

def solve(A,b):
    M=[row[:] + [v] for row,v in zip(A,b)]
    n=len(b)
    for i in range(n):
        pivot=next(k for k in range(i,n) if M[k][i])
        M[i],M[pivot]=M[pivot],M[i]
        z=M[i][i]
        M[i]=[v/z for v in M[i]]
        for k in range(n):
            if k==i: continue
            t=M[k][i]
            M[k]=[u-t*v for u,v in zip(M[k],M[i])]
    return [row[-1] for row in M]

def direct_flux(ks):
    n=len(ks)
    A=[[F(0) for _ in range(n-1)] for __ in range(n-1)]
    b=[F(0)]*(n-1)
    for i in range(n-1):
        A[i][i]=n*(ks[i]+ks[i+1])
        if i: A[i][i-1]=-n*ks[i]
        if i+1<n-1: A[i][i+1]=-n*ks[i+1]
    b[-1]=n*ks[-1]
    u=solve(A,b)
    return n*ks[0]*u[0]

# Exact matrix inversion under 2 rationally positioned jumps.
thetas=[F(1,3),F(2,3)]
ks_orig=[F(1),F(3),F(5)]
rs=[1/k for k in ks_orig]
T=sum((end-beg)*r for beg,end,r in zip([F(0)]+thetas,thetas+[F(1)],rs))
deltas=[rs[j-1]-rs[j] for j in range(1,3)]
for n in (5,7,8,10,11,13,16,19):
    positions=[n*t for t in thetas]
    cells=[int(x) for x in positions]
    ps=[x-int(x) for x in positions]
    for bits in product((0,1),repeat=2):
        # A bit selects whether a cut cell uses the material on the left.
        klist=[]
        for i in range(n):
            if i in cells and ps[cells.index(i)] > 0:
                j=cells.index(i)
                klist.append(ks_orig[j+1-bits[j]])
            else:
                mid=F(2*i+1,2*n)
                region=sum(mid>=t for t in thetas)
                klist.append(ks_orig[region])
        S=sum(d*(bit-p) for d,bit,p in zip(deltas,bits,ps))
        if any(p==0 and bit for p,bit in zip(ps,bits)):
            continue
        q_spectrum=1/(T+S/n)
        q_stiffness=direct_flux(klist)
        ck(q_spectrum==q_stiffness,('stiffness-vs-resistance',n,bits))
        ck(q_stiffness==1/(sum(1/k for k in klist)/n),('direct-flux',n,bits))

# For finite n the sampled resistance is exactly unbiased. For one jump,
# exact upward inverse bias is an algebraic identity.
for n in (3,5,7,10,16,23,31):
    for p in (F(1,5),F(1,2),F(4,5)):
        T=F(7,10); delta=F(3,5)
        vp=delta/n
        q1=1/(T+vp*(1-p))
        q0=1/(T-vp*p)
        qmean=p*q1+(1-p)*q0
        exact_bias=vp*vp*p*(1-p)/(T*(T+vp*(1-p))*(T-vp*p))
        ck(qmean-1/T==exact_bias,('exact-bias',n,p))
        ck(qmean>=1/T,('jensen-positive',n,p))

# Verify the triangular mixture moments directly as polynomial integrals:
# integral_0^1 p*(1-p)^k + (1-p)*(-p)^k dp.
def uniform_bernoulli_moment(k):
    # Integrate p*(1-p)^k+(1-p)*(-p)^k term-by-term.
    left=sum(((-1)**i)*comb(k,i)*F(1,i+2) for i in range(k+1))
    right=(-1)**k*(F(1,k+1)-F(1,k+2))
    return left+right
for k in range(0,12):
    if k%2==0:
        ck(uniform_bernoulli_moment(k)==F(2,(k+1)*(k+2)),('triangular-moment',k))
    else:
        ck(uniform_bernoulli_moment(k)==0,('odd-moment',k))

# Generic, explicitly irrational two-interface example:
theta1=sqrt(2)/5; theta2=sqrt(3)/3
r=[1.,0.5,0.2]
T=theta1*r[0]+(theta2-theta1)*r[1]+(1-theta2)*r[2]
q=1/T; ds=[r[0]-r[1],r[1]-r[2]]
csq=q**4*(ds[0]**2+ds[1]**2)/6
cbias=q**3*(ds[0]**2+ds[1]**2)/6
ave_sq=0.; ave_bias=0.
for n in range(25,30025):
    p1=n*theta1%1;p2=n*theta2%1
    pred_sq=0.;pred_bias=0.
    for b1,b2 in product((0,1),repeat=2):
        prob=(p1 if b1 else 1-p1)*(p2 if b2 else 1-p2)
        S=ds[0]*(b1-p1)+ds[1]*(b2-p2)
        qn=1/(T+S/n)
        pred_sq+=prob*(n*(qn-q))**2
        pred_bias+=prob*n*n*(qn-q)
    ave_sq+=pred_sq;ave_bias+=pred_bias
ave_sq/=30000;ave_bias/=30000
ck(abs(ave_sq/csq-1)<0.015,('cesaro-risk',ave_sq,csq))
ck(abs(ave_bias/cbias-1)<0.025,('cesaro-bias',ave_bias,cbias))

# Deterministic (exact-integrated) P1 element stiffness has arithmetic
# conductivity in each cut cell; its resistance differs from the exact
# physical resistance by the explicit positive cut-interface defect.
for n in (5,7,8,10,11,13,16,19):
    pos=[n*t for t in thetas]
    cells=[int(x) for x in pos]
    p=[x-int(x) for x in pos]
    elem=[]
    for i in range(n):
        mid=F(2*i+1,2*n)
        j=sum(mid>=t for t in thetas)
        k=ks_orig[j]
        if i in cells and p[cells.index(i)]>0:
            j=cells.index(i)
            k=p[j]*ks_orig[j]+(1-p[j])*ks_orig[j+1]
        elem.append(k)
    gammas=[pp*(1-pp)*(ks_orig[j]-ks_orig[j+1])**2/(ks_orig[j]*ks_orig[j+1]*(pp*ks_orig[j]+(1-pp)*ks_orig[j+1])) for j,pp in enumerate(p)]
    g=sum(gammas)
    q_fe=direct_flux(elem)
    global_T=sum((end-beg)*r for beg,end,r in zip([F(0)]+thetas,thetas+[F(1)],rs))
    ck(q_fe==1/(global_T-g/n),('FE-bias-identity',n))
    ck(q_fe>=1/global_T,('FE-upward-bias',n))

print('VERIFY_OK',N_CHECKS)
print('CESARO_MSE',ave_sq,csq)
print('CESARO_BIAS',ave_bias,cbias)
