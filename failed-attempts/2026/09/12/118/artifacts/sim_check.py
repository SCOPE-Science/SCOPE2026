"""ASEP Euler scaling check: E||rho^N - rho||_L1 vs N (TASEP, parallel sublattice).
Vectorized; approximate continuous-time ASEP. Burgers exact via characteristics.
"""
import numpy as np, json, math

def burgers_solution_TASEP(y, tau, rho0_fn, nchar=4000, iters=40):
    # TASEP: J=rho(1-rho), speed a=1-2rho. rho(y,tau)=rho0(z), y=z+(1-2rho0(z))tau.
    z = np.linspace(0,1,nchar,endpoint=False)
    r = rho0_fn(z); a = 1-2*r
    # invert map z -> y for each query y by Newton/bisection on monotone? map may fold;
    # use fixed-point via fine grid + interpolation (smooth regime: monotone).
    xmap = (z + a*tau) % 1.0
    order = np.argsort(xmap)
    xs, rs = xmap[order], r[order]
    # monotone in smooth regime; periodic interp
    xe = np.concatenate([xs-1, xs, xs+1]); re = np.concatenate([rs, rs, rs])
    return np.interp(y, xe, re)

def simulate(N, tau, rho0_fn, dt=0.25, trials=12, seed=0, p=1.0):
    q = 1-p
    rng = np.random.default_rng(seed)
    l = int(round(math.sqrt(N))); M = N//l
    Nb = M*l
    yc = (np.arange(Nb)+0.5)/N
    rho_exact = burgers_solution_TASEP((np.arange(M)+0.5)/M % 1.0, tau, rho0_fn)
    errs = []
    steps = int(round(N*tau/dt))
    for t in range(trials):
        eta = (rng.random(Nb) < rho0_fn(yc)).astype(np.int8)
        for s in range(steps):
            for parity in (0,1):
                xs = np.arange(parity, Nb-1, 2)
                # right jumps on bonds (x,x+1) with (1,0)
                mv = (eta[xs]==1)&(eta[xs+1]==0)&(rng.random(xs.size)<p*dt)
                eta[xs[mv]]=0; eta[xs[mv]+1]=1
                # left jumps: (0,1) particle moves left
                mv2 = (eta[xs]==0)&(eta[xs+1]==1)&(rng.random(xs.size)<q*dt)
                eta[xs[mv2]]=1; eta[xs[mv2]+1]=0
            # periodic bond (Nb-1,0)
            if rng.random()<1.0:  # handle once per sweep pair approx with prob dt
                if eta[Nb-1]==1 and eta[0]==0 and rng.random()<p*dt: eta[Nb-1]=0; eta[0]=1
                elif eta[Nb-1]==0 and eta[0]==1 and rng.random()<q*dt: eta[Nb-1]=1; eta[0]=0
        A = eta.reshape(M,l).mean(axis=1)
        errs.append(np.abs(A-rho_exact).mean())
    return float(np.mean(errs)), float(np.std(errs))

def rho0(y): return 0.5+0.25*np.sin(2*np.pi*y)

out=[]
for N in [64,144,256,576,1024]:
    for tau in [0.0, 0.2]:
        m,s = simulate(N,tau,rho0)
        out.append({"N":N,"tau":tau,"mean":m,"std":s})
        print({"N":N,"tau":tau,"mean":round(m,5),"std":round(s,5)}, flush=True)
# fit exponent at tau=0.2
import math
xs=[math.log(r["N"]) for r in out if r["tau"]==0.2]; ys=[math.log(r["mean"]) for r in out if r["tau"]==0.2]
n=len(xs); sx=sum(xs); sy=sum(ys); sxx=sum(x*x for x in xs); sxy=sum(x*y for x,y in zip(xs,ys))
slope=(n*sxy-sx*sy)/(n*sxx-sx*sx)
print("fitted exponent:", slope)
with open("output/artifacts/sim_scaling.json","w") as f: json.dump({"rows":out,"fitted_exponent_tau02":slope},f,indent=1)
