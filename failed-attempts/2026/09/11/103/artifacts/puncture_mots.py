"""Single-spin Bowen-York puncture solver + axisymmetric MOTS shooter (numpy only).

Family: psi = 1 + 1/(2r) + u,  Δu + beta*psi^-7 = 0,
  beta = (9/4) S^2 sin^2θ / r^6   (from A~^2 = 18 S^2 sin^2θ/r^6, /8)
Grid: r_i=(i+.5)*dr (Neumann at r=0 via mirror), theta cell-centered,
  Robin u+r u_r=0 at Rmax. Red-black SOR, Picard on nonlinearity.
MOTS: minimal-surface-in-psi^4δ ODE for h(θ) (K_ss=0 for BY spin on
  axisymmetric surfaces), pole shooting, equatorial symmetry condition.
Outputs: output/artifacts/census.json + stdout table.
"""
import numpy as np, json, math, sys, time

RMAX = 20.0
NR = 260
NT = 60
OMEGA = 1.9
PICARD_SWEeps = 400
PICARD_ROUNDS = 22

dr = RMAX / NR
dth = math.pi / NT
r1d = (np.arange(NR) + 0.5) * dr          # (NR,)
th1d = (np.arange(NT) + 0.5) * dth        # (NT,)
R = r1d[:, None] * np.ones((1, NT))       # (NR,NT)
TH = np.ones((NR, 1)) * th1d[None, :]
SN = np.sin(TH); CS = np.cos(TH); COT = CS / SN

# stencil coefficients
aE = 1/dr**2 + 1/(R*dr)
aW = 1/dr**2 - 1/(R*dr)
aN = (1/R**2)*(1/dth**2 + COT/(2*dth))
aS = (1/R**2)*(1/dth**2 - COT/(2*dth))
DG = -(aE + aW + aN + aS)                 # >0 ; equation: -DG*u + nbr = f
c_out = (2*RMAX - dr)/(2*RMAX + dr)       # outer ghost factor

MASK = ((np.arange(NR)[:, None] + np.arange(NT)[None, :]) % 2 == 0)  # red

def solve_u(S, verbose=False):
    U = np.zeros((NR+2, NT+2))            # padded; interior [1:-1,1:-1]
    beta = (9.0/4.0)*S*S*(SN**2)/(R**6)
    base = 1.0 + 1.0/(2.0*R)
    t0=time.time()
    for rnd in range(PICARD_ROUNDS):
        Uc = U[1:-1, 1:-1]
        psi = base + Uc
        f = -beta * psi**-7
        maxch = 0.0
        for sw in range(PICARD_SWEeps):
            # ghosts
            U[0, :] = U[1, :]                       # inner Neumann
            U[NR+1, :] = c_out * U[NR, :]           # Robin outer
            U[:, 0] = U[:, 1]; U[:, NT+1] = U[:, NT]  # poles
            for red in (True, False):
                Cc = U[1:-1, 1:-1]
                E = U[2:, 1:-1]; W = U[:-2, 1:-1]
                N = U[1:-1, 2:]; Sm = U[1:-1, :-2]
                newstar = (f - (aE*E + aW*W + aN*N + aS*Sm)) / DG
                upd = np.where((MASK == red), (1-OMEGA)*Cc + OMEGA*newstar, Cc)
                ch = np.max(np.abs(upd - Cc))
                if ch > maxch: maxch = ch
                U[1:-1, 1:-1] = upd
        # residual of PDE on interior
        U[0, :] = U[1, :]; U[NR+1, :] = c_out*U[NR, :]; U[:,0]=U[:,1]; U[:,NT+1]=U[:,NT]
        Cc = U[1:-1,1:-1]
        E=U[2:,1:-1]; W=U[:-2,1:-1]; N=U[1:-1,2:]; Sm=U[1:-1,:-2]
        psi = base + Cc; f = -beta*psi**-7
        res = DG*Cc + (aE*E+aW*W+aN*N+aS*Sm) - f
        # note: DG here = -(aE+..) so DG*u - nbrsum - f = -(aE*(E-u)...) - f ; residual of Δu - f
        rmax = float(np.max(np.abs(res)))
        if verbose: print(f"  S={S} rnd={rnd} maxch={maxch:.2e} res={rmax:.2e}", flush=True)
        if rmax < 2e-7 and maxch < 1e-10:
            break
    Uc = U[1:-1,1:-1]
    psi = base + Uc
    # ADM mass from outer falloff: M = 1 + 2 R u(R) averaged
    M_est = float(1.0 + 2*RMAX*np.mean(Uc[-1, :]))
    # min principle check
    return Uc, psi, M_est, rmax

def make_interp(psi, Uc):
    # centered derivatives on interior grid, then bilinear interp w/ clamping
    psr = np.zeros_like(psi); pst = np.zeros_like(psi)
    psr[1:-1,:] = (psi[2:,:]-psi[:-2,:])/(2*dr)
    psr[0,:] = (psi[1,:]-psi[0,:])/dr; psr[-1,:] = (psi[-1,:]-psi[-2,:])/dr
    pst[:,1:-1] = (psi[:,2:]-psi[:,:-2])/(2*dth)
    pst[:,0]=0.0; pst[:,-1]=0.0
    def interp(F, r, t):
        fi = np.clip((r/dr - 0.5), 0, NR-1.001)
        tj = np.clip((t/dth - 0.5), 0, NT-1.001)
        i0 = int(np.floor(fi)); j0 = int(np.floor(tj))
        i1=min(i0+1,NR-1); j1=min(j0+1,NT-1)
        a=fi-i0; b=tj-j0
        return (1-a)*(1-b)*F[i0,j0]+a*(1-b)*F[i1,j0]+(1-a)*b*F[i0,j1]+a*b*F[i1,j1]
    return (lambda r,t: float(interp(psi,r,t)),
            lambda r,t: float(interp(psr,r,t)),
            lambda r,t: float(interp(pst,r,t)))

def shoot(h0, P, Pr, Pt, nstp=2400):
    """integrate MOTS ODE pole->equator. Returns (h_eq, p_eq, area_integrand samples)."""
    th0 = 1e-5
    psi0 = P(h0, th0); pr0 = Pr(h0, th0)
    k = h0 + 2*h0*h0*pr0/max(psi0,1e-300)
    h = h0 + 0.5*k*th0*th0; p = k*th0; th = th0
    hpi = (math.pi/2 - th0)/nstp
    hs=[h]; ps=[p]; ts=[th]
    for _ in range(nstp):
        # RK4 on (h,p)
        def rhs(hh, pp, tt):
            rr = max(hh,1e-6); s=max(math.sin(tt),1e-12)
            psv=P(rr,tt); prv=Pr(rr,tt); ptv=Pt(rr,tt)
            W=math.sqrt(hh*hh+pp*pp)
            A=4*prv/psv+1/rr; B=4*ptv/psv+(math.cos(tt)/s)
            t1=W*(A+hh/(W*W)); t2=(pp*pp/W)*(A-hh/(W*W)); t3=(pp/W)*B
            dp=(t1-t2-t3)*(W**3)/(rr*rr)
            return pp, dp
        k1h,k1p=rhs(h,p,th); k2h,k2p=rhs(h+.5*hpi*k1h,p+.5*hpi*k1p,th+.5*hpi)
        k3h,k3p=rhs(h+.5*hpi*k2h,p+.5*hpi*k2p,th+.5*hpi)
        k4h,k4p=rhs(h+hpi*k3h,p+hpi*k3p,th+hpi)
        h+=hpi*(k1h+2*k2h+2*k3h+k4h)/6; p+=hpi*(k1p+2*k2p+2*k3p+k4p)/6; th+=hpi
        hs.append(h); ps.append(p); ts.append(th)
        if h<0.05 or h>4.0: break
    return h, p, np.array(ts), np.array(hs), np.array(ps)

def mots_area(ts, hs, ps, P):
    s=np.sin(ts); W=np.sqrt(hs*hs+ps*ps)
    pv=np.array([P(max(h,1e-6),max(min(t,math.pi-1e-9),1e-9)) for h,t in zip(hs,ts)])
    return float(2*math.pi*np.trapz(pv**4*hs*s*W, ts))

def find_mots(P, Pr, Pt):
    hs0 = np.linspace(0.25, 1.6, 28)
    peq = []
    for h0 in hs0:
        try:
            h,p,ts,hsa,psa = shoot(float(h0),P,Pr,Pt,nstp=1200)
            peq.append(p)
        except Exception:
            peq.append(float('nan'))
    peq=np.array(peq)
    roots=[]
    for i in range(len(hs0)-1):
        a0, b0 = hs0[i], hs0[i+1]
        fa, fb = peq[i], peq[i+1]
        if not (np.isfinite(fa) and np.isfinite(fb)):
            continue
        if abs(fa) < 1e-12:
            roots.append(a0); continue
        if abs(fb) < 1e-12:
            roots.append(b0); continue
        if fa*fb < 0:
            a, b = a0, b0
            for _ in range(40):
                m=.5*(a+b)
                _,pm,_,_,_ = shoot(m,P,Pr,Pt,nstp=1200)
                _,pa,_,_,_ = shoot(a,P,Pr,Pt,nstp=1200)
                if pa*pm<=0: b=m
                else: a=m
            roots.append(.5*(a+b))
    return hs0, peq, roots

def sphere_H(r, P, Pr):
    # physical mean curvature of coordinate sphere r (avg over theta)
    ts = np.linspace(0.01, math.pi-0.01, 9)
    Hs=[]
    for t in ts:
        psv=P(r,t); prv=Pr(r,t)
        Hs.append((2/r+4*prv/psv)/psv**2)
    return float(np.mean(Hs)), float(np.min(Hs))

if __name__ == "__main__":
    Ss = [float(x) for x in sys.argv[1:]] or [0.5, 1.0, 1.5, 2.0]
    out={}
    print("S      M_ADM    h0(outer)  Area      J      D        Hbar_min(R=2..11)", flush=True)
    for S in Ss:
        Uc, psi, M, res = solve_u(S)
        P,Pr,Pt = make_interp(psi, Uc)
        hs0, peq, roots = find_mots(P,Pr,Pt)
        h0 = max(roots) if roots else float('nan')
        if np.isfinite(h0):
            h,p,ts,hsa,psa = shoot(h0,P,Pr,Pt,nstp=4000)
            A = mots_area(ts,hsa,psa,P)
            J = S
            D = A/(8*math.pi*abs(S))-1 if S>0 else float('inf')
        else:
            A=float('nan'); D=float('nan'); p=float('nan')
        Hb=[sphere_H(r,P,Pr)[1] for r in [2.0,4.0,7.0,11.0]]
        print(f"{S:4.2f}  {M:7.4f}  {h0:7.4f}   {A:8.4f}  {S:5.2f}  {D:7.4f}  minH={min(Hb):.4f} res={res:.1e} roots={len(roots)}", flush=True)
        out[str(S)]={"M_ADM":M,"h0":h0,"Area":A,"J":S,"D":D,
                     "peq_equator":float(p) if np.isfinite(h0) else None,
                     "barrier_minH":min(Hb),"pde_res":res,"n_roots":len(roots),
                     "scan_h0":hs0.tolist(),"scan_peq":[float(x) for x in peq]}
    json.dump(out, open("output/artifacts/census.json","w"), indent=1)
    print("wrote output/artifacts/census.json", flush=True)
