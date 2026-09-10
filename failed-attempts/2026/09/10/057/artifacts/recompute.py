d=0.9; D=2.0
alpha=min(1+d,D)
num=alpha*D - d*(D+alpha-d)
den=(d+1)*(alpha*D - d**2) - d**2*(alpha+D-2*d)
FS=d*(1-num/den)
SW=d/2+d**2/(2*(2+(d**2+4)**0.5))
DORZ=5/3*d-1
KS=2*d/3
print(f"FS Cor3 at 0.9,2: {FS:.6f} (num={num:.4f}, den={den:.4f})")
print(f"SW low-dim: {SW:.6f}, DORZ: {DORZ:.6f}, KS: {KS:.6f}")
print(f"target 0.70 gap: {0.70-FS:.6f}, 2/3 gap: {2/3-FS:.6f}")
# required energy coefficient c
c_cur=d**2*(D+alpha-2*d)/(alpha*D-d**2)
print(f"current c: {c_cur:.6f}")
c_req=(0.70-0.9*0.2)/0.8  # from 0.18+0.8c=0.70
print(f"required c for 0.70 at L=0.2r: {c_req:.6f}, deficit {c_req-c_cur:.6f} ({100*(c_req-c_cur)/c_cur:.1f}%)")
# D threshold for 0.70 via FS formula
def B(sig,D):
    a=min(1+sig,D)
    n=a*D-sig*(D+a-sig)
    de=(sig+1)*(a*D-sig**2)-sig**2*(a+D-2*sig)
    return sig*(1-n/de) if abs(de)>1e-12 else None
for D in [1.3,1.4,1.5,1.55,1.58,1.6,1.7,1.8,1.9,2.0]:
    print(f"D={D}: B={B(0.9,D):.6f}")
