#!/usr/bin/env python3
"""Hardy-Littlewood prediction for pattern (0,4,6,10,12,16).
C6 = prod_p (1-w(p)/p)/(1-1/p)^6, w(p)=distinct residues covered.
For p>16, w=6 (offsets distinct mod p). Compute product to 1e6 + analytic tail.
Prediction for interval [lo,hi]: C6 * integral_{lo}^{hi} dt/(log t)^6 ~= C6*(hi-lo+1)/(log xmid)^6.
Also compare to observed N.
"""
import math, json, sys

def compute_C(limit=200000):
    # sieve primes to limit
    bs = bytearray(b'\x01')*(limit+1)
    bs[0:2]=b'\x00\x00'
    for i in range(2,int(limit**0.5)+1):
        if bs[i]:
            bs[i*i:limit+1:i]=b'\x00'*(((limit-i*i)//i)+1)
    primes=[i for i in range(2,limit+1) if bs[i]]
    offs=[0,4,6,10,12,16]
    C=1.0
    for p in primes:
        w=len(set(o%p for o in offs))
        C*= (1-w/p)/((1-1/p)**6)
    # tail for p>limit with w=6: prod (1-6/p)/(1-1/p)^6 = prod (1 - 15/p^2 - ... ). Approx exp(sum log).
    # log term: log(1-6/p)-6*log(1-1/p) = [-6/p-18/p^2-72/p^3...] -6*[-1/p-1/(2p^2)-1/(3p^3)...]
    # = (-6/p+6/p) + (-18+3)/p^2 + ... = -15/p^2 - ... So tail = exp(-15*sum_{p>limit}1/p^2 + O(1/p^3)).
    # sum_{p>limit} 1/p^2 < integral ~ 1/(limit*log limit). Bound tiny.
    s=0.0
    for p in primes:
        if p>limit: break
    # compute tail sum from limit: approximate sum_{n>limit} 1/(n^2 log n) ~ small; just bound.
    # Use Mertens-like: sum_{p>limit}1/p^2 <= (1/limit)*sum 1/p ~ negligible <1e-6.
    # So report C with tail correction exp(-15*T) where T approx sum_{p>limit}1/p^2.
    # Estimate T by integral of prime density: sum_{p>limit}1/p^2 ~ 1/(limit*log limit).
    Test = 1.0/(limit*math.log(limit))
    tail = math.exp(-15*Test)
    return C, tail, primes

def main():
    lo=1000000000000; hi=1001000000000
    C, tail, primes = compute_C(200000)
    C_corr = C*tail
    xmid=(lo+hi)/2
    L=math.log(xmid)
    pred = C_corr*(hi-lo+1)/(L**6)
    # more accurate integral via Simpson with 5 points (log varies little)
    import numpy as np
    xs=np.linspace(lo,hi,9)
    integ=float(sum(1.0/(math.log(float(x))**6) for x in xs)/len(xs)*(hi-lo+1))
    pred2=C_corr*integ
    # observed
    with open("output/artifacts/census.json") as f:
        obs=json.load(f)["count"]
    out={"pattern":[0,4,6,10,12,16],"C_product_to_200k":C,"tail_factor":tail,
         "C6":C_corr,"lo":lo,"hi":hi,"log_xmid":L,
         "pred_simple":pred,"pred_integral":pred2,"observed":obs,
         "ratio_obs_pred":obs/pred2 if pred2 else None,
         "poisson_p_ge_obs":None,
         "note":"C6 product to 2e5; tail <1e-6 relative; integral via 9-pt mean"}
    # Poisson tail P(N>=obs | mean=pred2)
    lam=pred2
    # compute P(N>=obs)=1-sum_{k<obs} e^-lam lam^k/k!
    s=0.0; term=math.exp(-lam)
    for k in range(0,obs):
        s+=term
        term*=lam/(k+1)
    out["poisson_p_ge_obs"]=1-s
    with open("output/artifacts/hl_compare.json","w") as f:
        json.dump(out,f,indent=1)
    print(json.dumps(out,indent=1))

if __name__=="__main__":
    main()
