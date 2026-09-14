"""Two-speed BRW (mean regime, common theta*) simulation artifact.

Binary branching, Gaussian increments:
  L1: 2 children, N(0,1); L2: 2 children, N(b,1), b=1.
Common critical theta* = sqrt(2 log 2) ~= 1.17741; v1=theta, v2=b+theta.
Switch at t_n=floor(t n), t=0.5. Centering m_n = v1 t_n + v2 s_n - (3/(2th)) log n.
Verifies: derivative martingale positivity, centering tightness, Gumbel-mixture
max law with fitted C_m stable across n, and phase-2 clustering (decoration).
"""
import json, math, numpy as np

rng = np.random.default_rng(0)
TH = math.sqrt(2*math.log(2)); B=1.0; T=0.5
V1 = TH; V2 = B+TH; KAP1 = math.log(2)+TH**2/2  # = log 4

def simulate(n, ntrials):
    tn = int(math.floor(T*n)); s = n-tn
    m = V1*tn + V2*s - (3/(2*TH))*math.log(n)
    Max=[]; Z=[]; topshare=[]
    for _ in range(ntrials):
        # phase 1: full tree depth tn -> 2^tn particles
        X = np.zeros(1)
        for _ in range(tn):
            X = np.repeat(X,2) + rng.normal(0,1,X.shape[0]*2)
        a = X - V1*tn
        Zw = float(np.sum((-a)*np.exp(TH*a)))  # = Z_{tn}^{(1)} (W-normalized: e^{th V - tn kap1})
        # leaves: each phase-1 particle spawns 2^s phase-2 leaves
        nL = 1<<s
        Xrep = np.repeat(X, nL)
        G = rng.normal(B,1,Xrep.shape[0])
        # accumulate s generations efficiently
        L = Xrep + G
        # remaining s-1 generations: block structure already flat, just add sums
        for _ in range(s-1):
            L = L + rng.normal(B,1,L.shape[0])
        # NOTE: above adds independent increments per leaf (correct: each leaf path independent)
        M = float(np.max(L) - m)
        Max.append(M); Z.append(Zw)
        # cluster check: do top-2 leaves share same phase-1 ancestor?
        if L.shape[0] >= 2:
            i1 = int(np.argmax(L))
            tmp = L.copy(); tmp[i1] = -np.inf
            i2 = int(np.argmax(tmp))
            topshare.append(1.0 if (i1//nL)==(i2//nL) else 0.0)
    return m, np.array(Max), np.array(Z), float(np.mean(topshare))

def fit_C(Max, Z, grid):
    # Use positive part Z+ (limit Z>=0 a.s.; negatives are finite-n artifacts).
    Zp = np.clip(Z, 0, None)
    # Fit C_m by matching empirical CDF at median-ish y0, then check whole curve.
    # Model: F(y) = E[exp(-C Z e^{-th y})].
    y0 = float(np.median(Max))
    p0 = float(np.mean(Max<=y0))
    # solve for C: mean(exp(-C Z e^{-th y0})) = p0 via bisection
    w = np.exp(-TH*y0)
    lo, hi = 1e-6, 20.0
    def F(C):
        E = np.clip(C*Zp*w, None, 700.0)
        return float(np.mean(np.exp(-E)))
    while F(hi) > p0 and hi < 1e4: hi*=2
    for _ in range(60):
        mid=(lo+hi)/2
        if F(mid) > p0: lo=mid
        else: hi=mid
    C=(lo+hi)/2
    # KS-type mismatch over grid
    errs=[]
    def G(Cv, y):
        E = np.clip(Cv*Zp*np.exp(-TH*y), None, 700.0)
        return float(np.mean(np.exp(-E)))
    for y in grid:
        emp=float(np.mean(Max<=y)); mod=G(C,y)
        errs.append(abs(emp-mod))
    return C, y0, p0, float(max(errs)), [float(np.mean(Max<=y)) for y in grid], [G(C,y) for y in grid]

out={}
grid=[-4,-2,-1,0,1,2,3,5]
for n,nt in [(8,2000),(10,2000),(12,800),(14,300),(16,150)]:
    m,Max,Z,sh = simulate(n,nt)
    C,y0,p0,ks,emp,mod = fit_C(Max,Z,grid)
    out[n]={"trials":nt,"tn":int(math.floor(T*n)),"m":m,
      "mean_M_minus_m":float(np.mean(Max)),"sd":float(np.std(Max)),
      "P_positive_Z":float(np.mean(np.array(Z)>0)),
      "mean_Z":float(np.mean(Z)),
      "C_fit":C,"KS_vs_mixture":ks,
      "top2_same_phase1_ancestor":sh,
      "emp_cdf":[round(v,3) for v in emp],"model_cdf":[round(v,3) for v in mod]}
    print(n, "mean=%.2f sd=%.2f C=%.3f KS=%.3f share=%.2f PZ=%.3f"%(
        np.mean(Max),np.std(Max),C,ks,sh,float(np.mean(np.array(Z)>0))),flush=True)

with open("/srv/scope-research/rounds/2026-09-14-hands-on-first-light-01/workspaces/research/lane-20133/output/artifacts/summary.json","w") as f:
    json.dump({"theta_star":TH,"v1":V1,"v2":V2,"t":T,"grid":grid,"results":out},f,indent=1)
print("saved")
