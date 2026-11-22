"""Reproducible finite checks for a two-boundary diffusion allocation theorem.

Standard-library only. The assertions check equations and numerical examples;
they do not substitute for the analytic uniqueness and crossing proofs.
"""
import math
import random

rng = random.Random(731291)
checks = 0

def near(a, b, tol=2e-9):
    global checks
    assert abs(a-b) <= tol * (1+abs(a)+abs(b)), (a,b)
    checks += 1

def coeff(k, positions, weights, K):
    A = sum(w*math.cosh(k*(1-y)) for y,w in zip(positions,weights))
    B = sum(w*math.cosh(k*y) for y,w in zip(positions,weights))
    C = sum(w*(math.sinh(k*(1-y))+math.sinh(k*y))/k for y,w in zip(positions,weights))
    E = math.sinh(k)/k
    Q0 = k*math.sinh(k)+K*math.cosh(k)
    return A,B,C,E,Q0

def laplace_point(k,a,b,y):
    q=k*math.sinh(k)+(a+b)*math.cosh(k)+a*b*math.sinh(k)/k
    n=a*math.cosh(k*(1-y))+b*math.cosh(k*y)+a*b*(math.sinh(k*(1-y))+math.sinh(k*y))/k
    nprime=-a*k*math.sinh(k*(1-y))+b*k*math.sinh(k*y)+a*b*(-math.cosh(k*(1-y))+math.cosh(k*y))
    return n/q, nprime/q

def objective(k,a,K,positions,weights):
    A,B,C,E,Q0 = coeff(k,positions,weights,K)
    return (a*A+(K-a)*B+a*(K-a)*C)/(Q0+a*(K-a)*E)

def H(k,a,K,positions,weights):
    A,B,C,E,Q0 = coeff(k,positions,weights,K)
    delta=A-B
    Z=C*Q0-E*K*B
    return delta*Q0+(K-2*a)*Z+E*delta*a*a

def optimum(k,K,positions,weights):
    lo,hi=0.0,K
    if H(k,lo,K,positions,weights)<=0: return lo
    if H(k,hi,K,positions,weights)>=0: return hi
    for _ in range(75):
        mid=(lo+hi)/2
        if H(k,mid,K,positions,weights)>0: lo=mid
        else: hi=mid
    return (lo+hi)/2

for _ in range(300):
    k=rng.uniform(0.15,4.0)
    K=rng.uniform(.15,6.)
    a=rng.uniform(0,K)
    b=K-a
    y=rng.random()
    f,fp=laplace_point(k,a,b,y)
    f0,fp0=laplace_point(k,a,b,0)
    f1,fp1=laplace_point(k,a,b,1)
    near(fp0,a*(f0-1))
    near(fp1,b*(1-f1))
    near(0.0, k*k*f-(a*k*k*math.cosh(k*(1-y)) + b*k*k*math.cosh(k*y) +a*b*k*(math.sinh(k*(1-y))+math.sinh(k*y)))/(k*math.sinh(k)+K*math.cosh(k)+a*b*math.sinh(k)/k))
    near(1, f+ (1-f))
    w=rng.random(); z=rng.random()
    pos=[y,z]; wei=[w,1-w]
    fmu=objective(k,a,K,pos,wei)
    fpoint=w*f+(1-w)*laplace_point(k,a,b,z)[0]
    near(fmu,fpoint)
    A,B,C,E,Q0=coeff(k,pos,wei,K)
    den=Q0+E*a*(K-a)
    # Check symbolic quotient-rule numerator via centered numerical differences.
    h=1e-5*min(K,1)
    if h<a<K-h:
        fd=(objective(k,a+h,K,pos,wei)-objective(k,a-h,K,pos,wei))/(2*h)
        near(fd,H(k,a,K,pos,wei)/(den*den),2e-7)
    astar=optimum(k,K,pos,wei)
    delta=A-B
    if delta>1e-9: assert astar>K/2
    elif delta< -1e-9: assert astar<K/2
    else: near(astar,K/2)
    checks+=1
    # Verify global optimality against all sampled allocations, not just stationarity.
    optimum_value=objective(k,astar,K,pos,wei)
    for j in range(31):
        assert optimum_value>=objective(k,j*K/30,K,pos,wei)-1e-11
        checks+=1

kc=5*math.acosh(1.5)
for K in [0.1,1.,10.,100.]:
    for mult,expected in [(0.4,-1),(0.7,-1),(1.,0),(1.3,1),(1.8,1)]:
        k=kc*mult
        a=optimum(k,K,[0.1,0.7],[0.25,0.75])
        if expected==0:
            near(a,K/2,1e-9)
        else:
            assert expected*(a-K/2)>0,(K,k,a)
            checks+=1
    # Any positive reactivity budget crosses at exactly the same frequency.
    near(H(kc,K/2,K,[0.1,0.7],[0.25,0.75]),0,2e-7)

# Direct mathematical relation for the two-site hyperbolic sign.
for k in [.1,.5,1.,kc,8.,12.]:
    A,B,*_=coeff(k,[.1,.7],[.25,.75],1.)
    near(A-B,2*math.sinh(k/2)*(.25*math.sinh(.4*k)-.75*math.sinh(.2*k)))

print(f"PASS {checks} deterministic finite checks; critical k={kc:.12f}; rL^2/D={kc**2:.12f}")
