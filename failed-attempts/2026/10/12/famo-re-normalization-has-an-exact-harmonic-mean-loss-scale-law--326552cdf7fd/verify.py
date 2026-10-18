import math
import random

def softmax(x):
    m=max(x)
    e=[math.exp(v-m) for v in x]
    s=sum(e)
    return [v/s for v in e]

def add(a,b):
    return [x+y for x,y in zip(a,b)]

def mul(s,a):
    return [s*x for x in a]

def norm(a):
    return math.sqrt(sum(x*x for x in a))

def famo_direction(losses, grads, logits):
    z=softmax(logits)
    inv=sum(zi/li for zi,li in zip(z,losses))
    c=1.0/inv
    raw=[0.0]*len(grads[0])
    for zi,li,gi in zip(z,losses,grads):
        raw=add(raw,mul(zi/li,gi))
    d=mul(c,raw)
    w=[c*zi/li for zi,li in zip(z,losses)]
    return d,w,c,z

random.seed(350074)

# Pointwise independent-scale law.
for _ in range(4000):
    T=random.randint(2,8)
    d=random.randint(1,7)
    losses=[10**random.uniform(-2,2) for _ in range(T)]
    grads=[[random.uniform(-4,4) for _ in range(d)] for _ in range(T)]
    logits=[random.uniform(-3,3) for _ in range(T)]
    scales=[10**random.uniform(-2,2) for _ in range(T)]
    base,w,c,z=famo_direction(losses,grads,logits)
    losses2=[s*l for s,l in zip(scales,losses)]
    grads2=[mul(s,g) for s,g in zip(scales,grads)]
    scaled,w2,c2,z2=famo_direction(losses2,grads2,logits)
    H=1.0/sum(wi/si for wi,si in zip(w,scales))
    err=norm(add(scaled,mul(-H,base)))
    assert err < 2e-10*max(1.0,norm(base),norm(scaled))
    assert min(scales)-1e-12 <= H <= max(scales)+1e-12

# Two equal practical weights gives the closed harmonic formula.
for s in (1e-6,0.1,1.0,7.0,1e6):
    H=1.0/(0.5/s+0.5)
    assert abs(H-2*s/(1+s)) < 1e-12*max(1.0,H)

# Full common-scale trajectory equivalence on positive quadratic-plus-offset losses.
# Loss_i(theta)=0.5*a_i*(theta-b_i)^2 + q_i with q_i>0.
def losses_grads(theta, params):
    L=[]; G=[]
    for a,b,q in params:
        L.append(0.5*a*(theta-b)**2+q)
        G.append([a*(theta-b)])
    return L,G

def logit_update(logits, oldL, newL, beta, gamma):
    z=softmax(logits)
    delta=[math.log(a)-math.log(b) for a,b in zip(oldL,newL)]
    mean=sum(zi*di for zi,di in zip(z,delta))
    # Jacobian(softmax)^T delta = z_i*(delta_i - weighted mean).
    jd=[zi*(di-mean) for zi,di in zip(z,delta)]
    return [x-beta*(g+gamma*x) for x,g in zip(logits,jd)]

params=[(1.2,-1.0,2.0),(0.7,2.0,1.5),(2.1,0.5,3.0)]
for scale in (0.2,3.0,50.0):
    theta1=0.3
    theta2=0.3
    xi1=[0.2,-0.4,0.1]
    xi2=xi1[:]
    alpha=0.03
    beta=0.025
    gamma=0.001
    for _ in range(80):
        L1,G1=losses_grads(theta1,params)
        d1,_,_,_=famo_direction(L1,G1,xi1)
        nxt1=theta1-alpha*d1[0]
        NL1,_=losses_grads(nxt1,params)
        nxi1=logit_update(xi1,L1,NL1,beta,gamma)

        L2=[scale*x for x in L1]
        G2=[[scale*g[0]] for g in G1]
        d2,_,_,_=famo_direction(L2,G2,xi2)
        nxt2=theta2-(alpha/scale)*d2[0]
        # The same theta is expected; construct scaled next losses there.
        rawNL2,_=losses_grads(nxt2,params)
        NL2=[scale*x for x in rawNL2]
        nxi2=logit_update(xi2,L2,NL2,beta,gamma)

        assert abs(nxt1-nxt2)<2e-12
        assert max(abs(a-b) for a,b in zip(nxi1,nxi2))<2e-12
        theta1,theta2=nxt1,nxt2
        xi1,xi2=nxi1,nxi2

print("verification passed")
