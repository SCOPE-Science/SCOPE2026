#!/usr/bin/env python3
"""Lane-486 TARGET: exact threshold arithmetic for pure-pair+Turan obstructions.
Stdlib only. Prints values logged into increment_table analysis.
"""
import math
LOG=[]
def log(s): LOG.append(s); print(s)
c=1/8
log("=== A. Type-controlled pure-pair threshold: need 2*g^c>=1, i.e. c<=ln2/ln(1/g) ===")
for g in [1/4, 1/7, 1/50, 1/100]:
    cmax=math.log(2)/math.log(1/g)
    log(f"gamma={g:.4f}: c_max={cmax:.6f} {'TARGET 1/8 FOLLOWS (if type-controlled)' if cmax>=c else 'insufficient'}")
log("=== B. Type-uncontrolled (max only): factor g^c<1 always; deficit 1-g^c ===")
for g in [1/4, 1/7, 1/50]:
    log(f"gamma={g:.4f}: g^c={(g**c):.6f} deficit={1-g**c:.6f}")
log("=== C. Turan in window W=[1/4,3/4]: alpha>=n/(d(n-1)+1); solve n where >=n^c ===")
for d in [1/4, 1/2, 3/4]:
    # find largest n with bound >= n^c by scan
    ok=0
    n=2
    while True:
        if n/(d*(n-1)+1) >= n**c: ok=n
        n+=1
        if n>10**7: break
        if n>100 and n/(d*(n-1)+1) < n**c and ok>0 and n>ok*4: break
    log(f"d={d}: Turan closes n^c only for n<={ok} (beyond: constant vs growing)")
log("=== D. Domination-partition degraded exponent c(1-c) fixed point ===")
cc=c
log(f"c=1/8 -> c(1-c)=7/64={cc*(1-cc):.6f}<1/8; iterate c_{{k+1}}=c_k(1-c_k)->0")
log(f"needed split factor f with f^c>=1/2 (to keep 2 f^c>=1 at c=1/8): f>={(1/2)**(1/c):.6f}=2^-8=1/256")
log("i.e. type-controlled pair with gamma>=1/256 each side suffices for 1/8; gamma=1/50 qualifies WITH type control")
log("=== E. Additive +1 compensation windows ===")
def holds(n, num, den):
    return 1+(num*n/den)**c >= n**c
for num,den in [(3,4),(1,2),(1,4)]:
    lo=0
    for e in range(1,13):
        if holds(10**e,num,den): lo=10**e
    log(f"1+({num}n/{den})^c>=n^c holds up to ~1e{len(str(lo))-1} (lo={lo})")
log("THRESHOLD_OK")
with open("output/artifacts/thresholds.log","w") as f: f.write("\n".join(LOG)+"\n")
