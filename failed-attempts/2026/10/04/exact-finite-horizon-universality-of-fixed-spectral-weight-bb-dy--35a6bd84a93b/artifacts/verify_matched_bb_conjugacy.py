import math

def dot(x,y):
    return sum(a*b for a,b in zip(x,y))

def had(a,b):
    return [x*y for x,y in zip(a,b)]

def sub(a,b):
    return [x-y for x,y in zip(a,b)]

def mul(c,x):
    return [c*a for a in x]

def alpha_w(u,H,W):
    Wu=had(W,u)
    WHu=had(W,had(H,u))
    return dot(u,Wu)/dot(u,WHu)

def step(state,H,W):
    u,v=state
    if max(abs(x) for x in u+v) == 0.0:
        return ([0.0]*len(u),[0.0]*len(u))
    a=alpha_w(u,H,W)
    nxt=sub(v,mul(a,had(H,v)))
    return (v,nxt)

def transform(state,W):
    s=[math.sqrt(w) for w in W]
    return (had(s,state[0]),had(s,state[1]))

def norm_e(state):
    return math.sqrt(dot(state[0],state[0])+dot(state[1],state[1]))

def norm_w(state,W):
    z=transform(state,W)
    return norm_e(z)

def maxdiff(a,b):
    return max(abs(x-y) for p,q in zip(a,b) for x,y in zip(p,q))

models=[
    ([1.0,3.0,7.0],[1.0,2.0,5.0]),
    ([0.5,2.0,9.0,13.0],[4.0,1.0,7.0,2.0]),
    ([1.0,4.0],[1.0,4.0]),
]
for H,W in models:
    for alpha0 in [1.0/max(H),0.5*(1.0/max(H)+1.0/min(H)),1.0/min(H)]:
        for u in [
            [1.0+0.2*i for i in range(len(H))],
            [(-1.0)**i*(0.7+0.1*i) for i in range(len(H))],
        ]:
            v=sub(u,mul(alpha0,had(H,u)))
            z=(u,v)
            zI=transform(z,W)
            assert abs(norm_w(z,W)-norm_e(zI)) < 1e-12
            cur=z
            curI=zI
            for k in range(9):
                if k>0:
                    cur=step(cur,H,W)
                    curI=step(curI,H,[1.0]*len(H))
                assert maxdiff(transform(cur,W),curI) < 2e-10
                rw=norm_w(cur,W)/norm_w(z,W)
                ri=norm_e(curI)/norm_e(zI)
                assert abs(rw-ri) < 2e-11
print('VERIFY_OK')
