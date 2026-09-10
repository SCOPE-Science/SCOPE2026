def B(sig,D):
    a=min(1+sig,D)
    n=a*D-sig*(D+a-sig)
    de=(sig+1)*(a*D-sig**2)-sig**2*(a+D-2*sig)
    return sig*(1-n/de) if abs(de)>1e-12 else None
# F1: direct fallback test
v=B(0.9,2.0)
print(f"F1 direct: B(0.9,2)={v:.6f} vs 2/3={2/3:.6f} deficit={2/3-v:.6f} -> {'PASS' if v>=2/3 else 'FAIL'}")
# F2: sigma sweep (can a smaller sigma give larger B? check monotonicity)
for s in [0.7,0.75,0.8,0.85,0.88,0.89,0.9]:
    print(f"  sigma={s}: B={B(s,2.0):.6f}")
# F3: D threshold for 2/3
import numpy as np
lo,hi=1.5,2.0
for _ in range(25):
    mid=(lo+hi)/2
    if B(0.9,mid)>=2/3: lo=mid
    else: hi=mid
print(f"F3: max D with B>=2/3: D*~{lo:.4f} (B={B(0.9,lo):.6f}); at D=2 FAIL by {2/3-B(0.9,2.0):.6f}")
# required c lift for 2/3
sig=0.9; D=2.0; a=min(1+sig,D)
c_cur=sig**2*(D+a-2*sig)/(a*D-sig**2)
# ledger value at optimum: solve sigma'(1 - G/((sig'+1)G - ...)) ; linearize: need c such that envelope >=2/3
# envelope = max_L min(sig'L + c(r-L)... ) -> at optimum L*: val = sig'(c+sig')/(c+sig'+?) -- easier: brute force L-scan
def envelope(sig,c):
    import numpy as np
    best=0
    for L in np.linspace(0,1,10001):
        v1=sig*L + c*(1-L)
        v2=sig - L  # sigma'r - L (per unit r), floored at 0
        v2=max(v2,0)
        # Kr >= max(v1,v2)-eps ; worst-case L minimizes the max
        m=max(v1,v2)
        if m<best or best==0: pass
    # find min over L of max
    ms=[max(sig*L+c*(1-L), max(sig-L,0)) for L in np.linspace(0,1,10001)]
    return min(ms)
print(f"c_cur={c_cur:.6f}, envelope={envelope(0.9,c_cur):.6f}")
for c in [0.5689,0.59,0.60,0.61,0.62]:
    print(f"  c={c}: envelope={envelope(0.9,c):.6f} {'>=2/3' if envelope(0.9,c)>=2/3 else '<2/3'}")
