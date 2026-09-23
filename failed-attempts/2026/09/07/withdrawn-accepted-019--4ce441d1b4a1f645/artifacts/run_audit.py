#!/usr/bin/env python3
"""Fixed-seed finite-N GOE edge audit at N=10,20,50.
Sampler: Dumitriu-Edelman beta=1 tridiagonal with diag N(0,2), offdiag chi_k.
Classical edge: mu_N=2*sqrt(N), sigma_N=N^{-1/6}.
TW1 CDF: Painleve-II Hastings-McLeod via RK4 from Airy init (vendored).
Only deps: numpy, mpmath, stdlib.
"""
import numpy as np
import mpmath
import time, json, csv, hashlib, platform, sys, os, math

OUT = os.path.dirname(os.path.abspath(__file__))
print("OUT dir:", OUT)
print("numpy", np.__version__, "mpmath", mpmath.__version__, "python", sys.version)

MASTER_SEED = 500020
BOOTSTRAP_SEED = 500021
CONFIG = {"N10": 5000, "N20": 20000, "N50": 5000}

# ---------- TW1 CDF via Painleve II ----------
def build_tw1(s_max=8.0, s_min=-8.0, h=0.001):
    mpmath.mp.dps = 50
    q_init = float(mpmath.airyai(s_max))
    qp_init = float(mpmath.diff(mpmath.airyai, s_max))
    N = int(round((s_max - s_min) / h))
    xs_desc = np.empty(N+1, dtype=np.float64)
    qs_desc = np.empty(N+1, dtype=np.float64)
    s = s_max
    y = np.array([q_init, qp_init], dtype=np.float64)
    def f(s, y):
        q, p = y
        return np.array([p, s*q + 2*q**3], dtype=np.float64)
    hh = -h
    for i in range(N+1):
        xs_desc[i] = s
        qs_desc[i] = y[0]
        k1 = f(s, y)
        k2 = f(s+hh/2, y+hh/2*k1)
        k3 = f(s+hh/2, y+hh/2*k2)
        k4 = f(s+hh, y+hh*k3)
        y = y + hh/6*(k1+2*k2+2*k3+k4)
        s += hh
    xs = xs_desc[::-1]
    qs = qs_desc[::-1]
    d = h
    r = qs**2
    trap_r = (r[:-1]+r[1:])/2*d
    K = np.empty_like(xs); K[-1]=0; K[:-1]=np.cumsum(trap_r[::-1])[::-1]
    xr = xs*r
    trap_xr = (xr[:-1]+xr[1:])/2*d
    J = np.empty_like(xs); J[-1]=0; J[:-1]=np.cumsum(trap_xr[::-1])[::-1]
    I2 = J - xs*K
    trap_q = (qs[:-1]+qs[1:])/2*d
    I1 = np.empty_like(xs); I1[-1]=0; I1[:-1]=np.cumsum(trap_q[::-1])[::-1]
    F1 = np.exp(-0.5*I1 - 0.5*I2)
    return xs, F1, qs

t0=time.time()
xs_fine, F1_fine, qs_fine = build_tw1(h=0.001)
xs_coarse, F1_coarse, _ = build_tw1(h=0.002)
Fcoarse_on_fine = np.interp(xs_fine, xs_coarse, F1_coarse)
maxdiff = float(np.max(np.abs(F1_fine - Fcoarse_on_fine)))
print(f"TW1 table built: {len(xs_fine)} points, h=0.001 vs 0.002 maxdiff={maxdiff:.3e}, time={time.time()-t0:.1f}s")
# moments check via pdf gradient
d = xs_fine[1]-xs_fine[0]
pdf = np.gradient(F1_fine, d)
TW_EX = float(np.trapz(xs_fine*pdf, xs_fine))
TW_EX2 = float(np.trapz(xs_fine**2*pdf, xs_fine))
TW_EX3 = float(np.trapz(xs_fine**3*pdf, xs_fine))
TW_EX4 = float(np.trapz(xs_fine**4*pdf, xs_fine))
TW_var = TW_EX2-TW_EX**2
TW_skew = (TW_EX3-3*TW_EX*TW_EX2+2*TW_EX**3)/TW_var**1.5
TW_kurt = (TW_EX4-4*TW_EX*TW_EX3+6*TW_EX**2*TW_EX2-3*TW_EX**4)/TW_var**2-3
EX, var, skew, kurt = TW_EX, TW_var, TW_skew, TW_kurt
print(f"TW1 moments: mean={EX:.8f} var={var:.8f} skew={skew:.6f} kurt={kurt:.6f}")
print("TW1 reference: mean=-1.20653357 var=1.60778103 skew=0.29346 kurt~0.16524")
# save TW table
with open(os.path.join(OUT,"tw1_cdf.csv"),"w",newline="") as f:
    w=csv.writer(f)
    w.writerow(["# TW1 CDF vendored via Painleve-II Hastings-McLeod RK4"])
    w.writerow([f"# s_max=8.0 s_min=-8.0 h=0.001 init Ai/Ai' via mpmath {mpmath.__version__} dps=50, numpy {np.__version__}"])
    w.writerow([f"# convergence h=0.001 vs h=0.002 maxdiff={maxdiff:.3e}"])
    w.writerow([f"# moments mean={EX:.8f} var={var:.8f} skew={skew:.6f} kurt={kurt:.6f}"])
    w.writerow(["s","F1"])
    for a,b in zip(xs_fine, F1_fine):
        w.writerow([f"{a:.6f}", f"{b:.12f}"])

def tw_cdf(s):
    return np.interp(s, xs_fine, F1_fine, left=0.0, right=1.0)

def ks_distance_sorted(v_sorted, mu, sig):
    n=len(v_sorted)
    s=(v_sorted-mu)/sig
    Ft=np.interp(s, xs_fine, F1_fine, left=0.0, right=1.0)
    i_over_n=(np.arange(1,n+1))/n
    im1_over_n=(np.arange(0,n))/n
    return float(max(np.max(np.abs(i_over_n-Ft)), np.max(np.abs(im1_over_n-Ft))))

# ---------- GOE sampler ----------
master = np.random.SeedSequence(MASTER_SEED)
children = master.spawn(3)
# map: 0->N10, 1->N20, 2->N50
plan = [(10, CONFIG["N10"], children[0]), (20, CONFIG["N20"], children[1]), (50, CONFIG["N50"], children[2])]

def sample_lmax_array(N, n, seedseq):
    rng = np.random.default_rng(seedseq)
    out = np.empty(n, dtype=np.float64)
    dfs = np.arange(N-1, 0, -1)
    for i in range(n):
        dd = np.sqrt(2.0)*rng.standard_normal(N)
        chisq = rng.chisquare(dfs)
        off = np.sqrt(chisq)
        A = np.diag(dd) + np.diag(off,1) + np.diag(off,-1)
        out[i] = np.linalg.eigvalsh(A)[-1]
        if (i+1)%5000==0:
            print(f"  N={N} {i+1}/{n}", flush=True)
    return out

results={}
for N,n,child in plan:
    print(f"Sampling N={N} n={n} ...", flush=True)
    t1=time.time()
    vals=sample_lmax_array(N,n,child)
    print(f" done N={N} time={time.time()-t1:.1f}s mean={vals.mean():.5f}", flush=True)
    # save CSV
    with open(os.path.join(OUT,f"lmax_N{N}.csv"),"w",newline="") as f:
        w=csv.writer(f)
        w.writerow(["idx","lambda_max"])
        for i,v in enumerate(vals):
            w.writerow([i, f"{v:.12f}"])
    results[N]=(vals,n)

# ---------- KS audit + grid search ----------
ks_rows=[]
calibrated={}
for N in [10,20,50]:
    vals,n = results[N]
    mu_cl=2*math.sqrt(N); sig_cl=N**(-1/6)
    v_sorted=np.sort(vals)
    ks_cl=ks_distance_sorted(v_sorted, mu_cl, sig_cl)
    eps=math.sqrt(math.log(2/0.05)/(2*n))
    # coarse grid
    dmus=np.linspace(-1.0,0.6,33)
    fs=np.linspace(0.85,1.20,15)
    best=(1e9,None,None)
    for dmu in dmus:
        for ff in fs:
            ks=ks_distance_sorted(v_sorted, mu_cl+dmu, sig_cl*ff)
            if ks<best[0]:
                best=(ks,mu_cl+dmu,sig_cl*ff)
    # refine
    bks,bmu,bsig=best
    dmus2=np.linspace(bmu-0.06,bmu+0.06,13)
    # sigma refine in factor space
    fbest=bsig/sig_cl
    fs2=np.linspace(max(0.8,fbest-0.03),fbest+0.03,13)*sig_cl
    for mu2 in dmus2:
        for sig2 in fs2:
            ks=ks_distance_sorted(v_sorted, mu2, sig2)
            if ks<best[0]:
                best=(ks,mu2,sig2)
    ks_cal,mu_star,sig_star=best
    calibrated[N]=(mu_star,sig_star,ks_cal)
    print(f"N={N} classical mu={mu_cl:.6f} sig={sig_cl:.6f} KS={ks_cl:.5f} | calibrated mu*={mu_star:.6f} sig*={sig_star:.6f} KS*={ks_cal:.5f} DKW_eps={eps:.5f}")
    ks_rows.append((N,n,mu_cl,sig_cl,ks_cl,mu_star,sig_star,ks_cal,eps))

with open(os.path.join(OUT,"ks_table.csv"),"w",newline="") as f:
    w=csv.writer(f)
    w.writerow(["N","n","mu_classical","sigma_classical","KS_classical","mu_star","sigma_star","KS_calibrated","DKW95_eps"])
    for r in ks_rows:
        w.writerow([r[0],r[1],f"{r[2]:.8f}",f"{r[3]:.8f}",f"{r[4]:.6f}",f"{r[5]:.8f}",f"{r[6]:.8f}",f"{r[7]:.6f}",f"{r[8]:.6f}"])

# ---------- Moments + bootstrap ----------
TW_MEAN, TW_VAR, TW_SKEW = -1.2065335747, 1.607781034, 0.293464524
brng=np.random.default_rng(np.random.SeedSequence(BOOTSTRAP_SEED))
B=1000
moment_rows=[]
for N in [10,20,50]:
    vals,n=results[N]
    mu_cl=2*math.sqrt(N); sig_cl=N**(-1/6)
    s=(vals-mu_cl)/sig_cl
    mean=float(s.mean())
    var=float(((s-mean)**2).mean())
    skew=float((((s-mean)**3).mean())/var**1.5)
    # bootstrap percentile CIs
    idx=np.arange(n)
    bmeans=np.empty(B); bvars=np.empty(B); bskews=np.empty(B)
    for b in range(B):
        samp=brng.choice(s, size=n, replace=True)
        m=float(samp.mean())
        v=float(((samp-m)**2).mean())
        sk=float((((samp-m)**3).mean())/v**1.5)
        bmeans[b]=m; bvars[b]=v; bskews[b]=sk
    def pci(x):
        return float(np.quantile(x,0.025)), float(np.quantile(x,0.975))
    mlo,mhi=pci(bmeans); vlo,vhi=pci(bvars); slo,shi=pci(bskews)
    print(f"N={N} scaled mean={mean:.5f} [{mlo:.5f},{mhi:.5f}] var={var:.5f} [{vlo:.5f},{vhi:.5f}] skew={skew:.5f} [{slo:.5f},{shi:.5f}]")
    moment_rows.append((N,n,mean,mlo,mhi,var,vlo,vhi,skew,slo,shi))
    # also calibrated-scaled moments for reference
    mu_star,sig_star,_=calibrated[N]
    sc=(vals-mu_star)/sig_star
    print(f"  calibrated-scaled mean={sc.mean():.5f} var={sc.var():.5f} skew={(((sc-sc.mean())**3).mean())/(sc.var()**1.5):.5f}")

with open(os.path.join(OUT,"moments_table.csv"),"w",newline="") as f:
    w=csv.writer(f)
    w.writerow(["N","n","mean","mean_lo","mean_hi","var","var_lo","var_hi","skew","skew_lo","skew_hi","TW1_mean","TW1_var","TW1_skew"])
    for r in moment_rows:
        w.writerow([r[0],r[1],f"{r[2]:.6f}",f"{r[3]:.6f}",f"{r[4]:.6f}",f"{r[5]:.6f}",f"{r[6]:.6f}",f"{r[7]:.6f}",f"{r[8]:.6f}",f"{r[9]:.6f}",f"{r[10]:.6f}",TW_MEAN,TW_VAR,TW_SKEW])

# ---------- Histogram (50 bins on [-6,4]) ----------
binedges=np.linspace(-6,4,51)
binwidth=binedges[1]-binedges[0]
with open(os.path.join(OUT,"histogram_all.csv"),"w",newline="") as f:
    w=csv.writer(f)
    w.writerow(["N","bin_left","bin_right","observed_count","expected_TW1_count","observed_density","expected_TW1_density"])
    for N in [10,20,50]:
        vals,n=results[N]
        mu_cl=2*math.sqrt(N); sig_cl=N**(-1/6)
        s=(vals-mu_cl)/sig_cl
        counts,_=np.histogram(s,bins=binedges)
        for i in range(50):
            l=binedges[i]; rr=binedges[i+1]
            exp_c=n*(tw_cdf(rr)-tw_cdf(l))
            w.writerow([N,f"{l:.4f}",f"{rr:.4f}",int(counts[i]),f"{exp_c:.3f}",f"{counts[i]/(n*binwidth):.6f}",f"{(tw_cdf(rr)-tw_cdf(l))/binwidth:.6f}"])

# SVG for N=20
N=20
vals,n=results[N]
mu_cl=2*math.sqrt(N); sig_cl=N**(-1/6)
s=(vals-mu_cl)/sig_cl
counts,_=np.histogram(s,bins=binedges)
# TW pdf via gradient
tw_pdf=np.gradient(F1_fine, xs_fine[1]-xs_fine[0])
# SVG params
W,H=640,400; ml,mr,mt,mb=60,20,20,50
pw,ph=W-ml-mr,H-mt-mb
ymax=max(counts.max()/(n*binwidth), float(np.max(tw_pdf[(xs_fine>-6)&(xs_fine<4)])))*1.15
def X(v): return ml+(v-(-6))/(4-(-6))*pw
def Y(v): return mt+ph-(v/ymax)*ph
svg=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}">']
svg.append(f'<rect x="0" y="0" width="{W}" height="{H}" fill="white"/>')
svg.append(f'<rect x="{ml}" y="{mt}" width="{pw}" height="{ph}" fill="none" stroke="black"/>')
# bars
for i in range(50):
    l=binedges[i]; rr=binedges[i+1]
    dens=counts[i]/(n*binwidth)
    x0=X(l)+1; x1=X(rr)-1; y0=Y(dens); y1=Y(0)
    svg.append(f'<rect x="{x0:.1f}" y="{y0:.1f}" width="{max(1,x1-x0):.1f}" height="{y1-y0:.1f}" fill="#7aa7d9" stroke="none"/>')
# TW pdf line
pts=[]
for a,b in zip(xs_fine[::20], tw_pdf[::20]):
    if -6<=a<=4:
        pts.append(f"{X(a):.1f},{Y(b):.1f}")
svg.append(f'<polyline points="{" ".join(pts)}" fill="none" stroke="red" stroke-width="2"/>')
# axes ticks
for v in [-6,-4,-2,0,2,4]:
    svg.append(f'<line x1="{X(v):.1f}" y1="{Y(0):.1f}" x2="{X(v):.1f}" y2="{Y(0)+5:.1f}" stroke="black"/>')
    svg.append(f'<text x="{X(v):.1f}" y="{Y(0)+18:.1f}" font-size="12" text-anchor="middle">{v}</text>')
svg.append(f'<text x="{ml+pw/2:.1f}" y="{H-8:.1f}" font-size="13" text-anchor="middle">edge-scaled s = (lambda_max - mu_N)/sigma_N, N=20, 50 bins on [-6,4]</text>')
svg.append(f'<text x="18" y="{mt+ph/2:.1f}" font-size="13" text-anchor="middle" transform="rotate(-90 18,{mt+ph/2:.1f})">density</text>')
svg.append(f'<text x="{ml+pw-5:.1f}" y="{mt+15:.1f}" font-size="12" text-anchor="end" fill="red">TW1 pdf</text>')
svg.append(f'<text x="{ml+pw-5:.1f}" y="{mt+30:.1f}" font-size="12" text-anchor="end" fill="#2a5a9a">empirical (n=20000)</text>')
svg.append('</svg>')
with open(os.path.join(OUT,"histogram_N20.svg"),"w") as f:
    f.write("\n".join(svg))
print("histograms written")

# ---------- Replay 500-sample subsample (N=20 prefix) ----------
print("Replay test: regenerating first 500 of N=20 ...")
child20 = np.random.SeedSequence(MASTER_SEED).spawn(3)[1]
vals_orig,_ = results[20]
vals_replay = sample_lmax_array(20, 500, child20)
diff = np.abs(vals_replay - vals_orig[:500])
maxdiff_replay=float(diff.max())
print(f"replay max abs diff = {maxdiff_replay:.3e}")
assert maxdiff_replay < 1e-10, f"replay failed {maxdiff_replay}"
with open(os.path.join(OUT,"replay_log.json"),"w") as f:
    json.dump({
        "test": "500-sample exact-diagonalization replay, N=20 prefix indices 0..499",
        "master_seed": MASTER_SEED,
        "child_index_for_N20": 1,
        "eig_func": "numpy.linalg.eigvalsh on dense symmetric tridiagonal",
        "numpy_version": np.__version__,
        "python_version": platform.python_version(),
        "platform": platform.platform(),
        "max_abs_diff": maxdiff_replay,
        "threshold": 1e-10,
        "passed": bool(maxdiff_replay < 1e-10),
        "note": "Replay regenerates tridiagonals from same SeedSequence and re-diagonalizes; bit-identical expected."
    }, f, indent=2)

# ---------- Provenance ----------
prov={
    "master_seed": MASTER_SEED,
    "bootstrap_seed": BOOTSTRAP_SEED,
    "sampler": "Dumitriu-Edelman beta=1 tridiagonal: diag sqrt(2)*N(0,1) i.e. N(0,2), offdiag sqrt(chisquare_k) k=N-1..1; dense numpy.linalg.eigvalsh max",
    "classical_scaling": "mu_N=2*sqrt(N), sigma_N=N^{-1/6}",
    "calibrated_search": "two-stage grid minimizing KS vs vendored TW1 CDF; coarse dmu[-1,0.6] 33pts x f[0.85,1.20] 15pts, refine +-0.06/+-0.03",
    "tw1_vendor": f"Painleve-II HM RK4 s_max=8 s_min=-8 h=0.001 mpmath {mpmath.__version__} dps=50, convergence h0.001vs0.002 maxdiff={maxdiff:.3e}",
    "tw1_moments": {"mean": TW_EX, "var": TW_var, "skew": TW_skew, "kurt": TW_kurt},
    "ks_table": [{"N":r[0],"n":r[1],"mu_cl":r[2],"sig_cl":r[3],"ks_cl":r[4],"mu_star":r[5],"sig_star":r[6],"ks_cal":r[7],"dkw":r[8]} for r in ks_rows],
    "numpy_version": np.__version__,
    "python_version": platform.python_version(),
}
with open(os.path.join(OUT,"provenance.json"),"w") as f:
    json.dump(prov,f,indent=2)
print("ALL DONE")
