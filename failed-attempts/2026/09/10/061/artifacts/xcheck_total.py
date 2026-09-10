"""Independent cross-check: total finite persistence via local-extrema pairing (no union-find).
For 1D alternating extrema, finite-bar total = Smax - Smin - (globalmax - globalmin),
where Smax/Smin sum interior strict local max/min. Also tabulate full-ray HF_conn."""
from verify_fallback import delta_tau, compress
import math

def local_sums(v):
    smax=smin=0; nmax=nmin=0
    for i in range(1,len(v)-1):
        if v[i]>v[i-1] and v[i]>v[i+1]: smax+=v[i]; nmax+=1
        elif v[i]<v[i-1] and v[i]<v[i+1]: smin+=v[i]; nmin+=1
    return smax,nmax,smin,nmin

for r in [5,7,11,13,17,19,23,25,29,31,37]:
    if math.gcd(r,18)!=1: continue
    N0,S,Delta,tau=delta_tau(2,9,r)
    v=compress(tau)
    smax,nmax,smin,nmin=local_sums(v)
    total=smax-smin-(max(v)-min(v))
    print(f"r={r} N0={N0} kappa={len(S)} tauMin={min(tau)} nmax={nmax} nmin={nmin} totalPers={total}")
