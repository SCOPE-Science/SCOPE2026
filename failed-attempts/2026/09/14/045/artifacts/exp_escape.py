"""Finite-time escape morphology for transcendental Henon F(z,w)=(exp(z)-d*w, z).
Saves ASCII summaries + raw escape-time arrays (npy) for audit.
"""
import numpy as np, os
os.makedirs("output/artifacts", exist_ok=True)

def escape_time(Z0, W0, delta, R=20.0, N=80, cap=1e6):
    Z = Z0.copy(); W = W0.copy()
    ET = np.full(Z0.shape, -1, dtype=np.int32)
    alive = np.ones(Z0.shape, bool)
    for n in range(1, N+1):
        Zn = np.empty_like(Z)
        # only update alive points; guard overflow of exp
        Za = Z[alive]; Wa = W[alive]
        # cap real part to avoid overflow: exp overflows at Re~709
        with np.errstate(over='ignore', invalid='ignore'):
            F = np.exp(Za)
        F[~np.isfinite(F)] = np.inf
        Zn_a = F - delta*Wa
        Wn_a = Za
        Z[alive] = Zn_a; W[alive] = Wn_a
        norm = np.abs(Z) + np.abs(W)
        esc = alive & (norm > R)
        ET[esc] = n
        alive[esc] = False
        # kill non-finite as escaped
        bad = alive & (~np.isfinite(norm))
        ET[bad] = n; alive[bad] = False
        if not alive.any(): break
    return ET  # -1 = not escaped within N

def components_bounded(mask):
    """4-connected components of True mask; return list of (size, touches_border)."""
    H, Wd = mask.shape
    seen = np.zeros_like(mask, bool)
    out = []
    for i in range(H):
        for j in range(Wd):
            if mask[i,j] and not seen[i,j]:
                stack=[(i,j)]; seen[i,j]=True; sz=0; tb=False
                while stack:
                    a,b = stack.pop(); sz+=1
                    if a==0 or b==0 or a==H-1 or b==Wd-1: tb=True
                    for da,db in ((1,0),(-1,0),(0,1),(0,-1)):
                        na,nb=a+da,b+db
                        if 0<=na<H and 0<=nb<Wd and mask[na,nb] and not seen[na,nb]:
                            seen[na,nb]=True; stack.append((na,nb))
                out.append((sz,tb))
    return out

def report(name, ET):
    esc = ET>=0
    comp = components_bounded(esc)
    bounded_islands = [s for s,tb in comp if not tb]
    print(f"[{name}] shape={ET.shape} esc_frac={esc.mean():.3f} "
          f"ncomp={len(comp)} bounded_esc_components={len(bounded_islands)} "
          f"sizes={sorted(bounded_islands, reverse=True)[:10]}")
    return comp

# Exp 1: w=0 slice, z in [-3,3] x [-3pi,3pi], delta=0.3
xr = np.linspace(-3,3,481); yi = np.linspace(-3*np.pi,3*np.pi,481)
XX, YY = np.meshgrid(xr, yi); Z0 = XX+1j*YY; W0=np.zeros_like(Z0)
for delta in [0.3, 1.0, 0.05]:
    ET = escape_time(Z0, W0, delta, R=20.0, N=80)
    np.save(f"output/artifacts/ET_slice_w0_d{delta}.npy", ET)
    report(f"slice w=0 d={delta} R=20 N=80", ET)

# Exp 2: persistence under larger N,R for d=0.3
ET2 = escape_time(Z0, W0, 0.3, R=100.0, N=200)
np.save("output/artifacts/ET_slice_w0_d0.3_R100_N200.npy", ET2)
report("slice w=0 d=0.3 R=100 N=200", ET2)

# Exp 3: w-direction scan at candidate z centers (slice statistics): fix z on real axis grid, w vary
zr = np.linspace(-3,3,241); wr = np.linspace(-10,10,241); wi = np.linspace(-10,10,241)
WX, WY = np.meshgrid(wr, wi)
for zc in [-2.0, -1.0, 0.0, 1.0, 2.0]:
    Z0b = np.full(WX.shape, zc+0j, dtype=complex); W0b = WX+1j*WY
    ETb = escape_time(Z0b, W0b, 0.3, R=20.0, N=80)
    np.save(f"output/artifacts/ET_wplane_z{zc}.npy", ETb)
    esc = ETb>=0
    comp = components_bounded(~esc)  # non-escaped components in w-plane
    print(f"[w-plane z={zc}] esc_frac={esc.mean():.3f} nonesc_comp={len(comp)} "
          f"nonecbounded={(sum(1 for s,tb in comp if not tb))}")
print("done")
