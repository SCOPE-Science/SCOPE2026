import numpy as np

def C1(a,b,eps):
    s=np.sqrt(a*b); D=np.sqrt(eps*eps+4*a*b)
    t=(D-eps)/(2*s); t=min(t,1-1e-15)
    return (a+b-(D-eps))/2 - (eps/2)*np.log1p(-t*t)

def OT1(a,b): return (np.sqrt(a)-np.sqrt(b))**2/2

def r1(a,b,eps): return C1(a,b,eps)-0.5*(C1(a,a,eps)+C1(b,b,eps))-OT1(a,b)

# sanity: sign of r1 over grid
xs=np.concatenate([np.logspace(-5,0,40)])
mx=0
for a in [1e-4,1e-3,1e-2,0.1,0.5,1.0]:
    for b in [0.5,1.0]:
        for eps in [1e-4,1e-3,1e-2,0.05,0.1]:
            v=r1(a,b,eps)
            assert v<=1e-12, (a,b,eps,v)
print("sign check: all r1<=0 OK")

# worst-case two-level search: B_i=1; A: fraction alpha at delta, rest at 1
# constraints: mean(A)<=M=1, mean(1/A)<=F=2, A<=1/kap=1
def ratio_twolevel(n,alpha,delta,eps,b=1.0):
    m=int(round(alpha*n))
    A=np.ones(n); A[:m]=delta
    tot=sum(r1(a,b,eps) for a in A)
    return abs(tot)/n/eps

best={}
for n in [4,16,64,256]:
    b=1.0
    mx=0; arg=None
    for alpha in [0.05,0.1,0.2,0.3,0.5]:
        for delta in [1/(n*2),1/n,2/n,5/n,0.01,0.05,0.1,0.5]:
            if alpha/delta+(1-alpha)>2.0+1e-9: continue  # Fisher
            if alpha*delta+(1-alpha)>1.0+1e-9: continue  # moment
            for eps in [0.1,0.05,0.02,0.01,0.005,0.002,0.001,5e-4]:
                v=ratio_twolevel(n,alpha,delta,eps)
                if v>mx: mx=v; arg=(alpha,delta,eps)
    print(f"n={n} worst R1={mx:.5f} at {arg}")
    best[n]=(mx,arg)

# also: uniform profiles a=b=1/F? and a=1/F,b=1
print("--- uniform ---")
for a in [0.5,1.0]:
    for b in [0.5,1.0]:
        for eps in [0.1,0.05,0.01,0.005,0.001]:
            print(f"a={a} b={b} eps={eps} R1={abs(r1(a,b,eps))/eps:.5f} R1b={abs(r1(a,b,eps))/eps:.5f}")
        print()
