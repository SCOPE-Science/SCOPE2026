"""Fallback scan F1+F2: model-operator second-variation quotients for tanh((r1-r2)/sqrt2).
O(4)xO(4) reduction, full gradient incl. cutoff + cross terms, R=1,2,4.
Reproduces WORKLOG fallback numbers. Stdlib+numpy only."""
import numpy as np, math
volS3 = 2*math.pi**2

def Q_scan(R=2.0, width=0.5, center=0.0, n=400, mode=(0,0)):
    rhos = np.linspace(1e-9, R, n); ts = np.linspace(0, math.pi/2, n)
    dr = rhos[1]-rhos[0]; dt = ts[1]-ts[0]
    Rho, T = np.meshgrid(rhos, ts, indexing='ij')
    R1 = Rho*np.cos(T); R2 = Rho*np.sin(T)
    s = (R1-R2)/math.sqrt(2)
    U = np.tanh(np.clip(s, -20, 20))
    Vpot = 3*U**2-1.0
    l1, l2 = mode
    chi = np.sin(math.pi*Rho/R)**2
    dchi = 2*math.pi/R*np.sin(math.pi*Rho/R)*np.cos(math.pi*Rho/R)
    g = np.exp(-((s-center)/width)**2)
    dg = g*(-2*(s-center)/width**2)
    phi = g*chi
    ds_phi = dg*chi; drho_phi = g*dchi
    cross = 2*(s/np.maximum(Rho, 1e-12))*ds_phi*drho_phi
    grad2 = ds_phi**2 + drho_phi**2 + cross
    centrif = (l1*(l1+2)/np.maximum(R1,1e-9)**2 + l2*(l2+2)/np.maximum(R2,1e-9)**2)*phi**2
    w = volS3**2*(R1**3)*(R2**3)*Rho
    num = np.sum((grad2+centrif+Vpot*phi**2)*w)*dr*dt
    den = np.sum(phi**2*w)*dr*dt
    return float(num/den)

if __name__ == "__main__":
    best = 1e9; bestp = None
    for R in [1.0, 2.0, 4.0]:
        for w in [0.3, 0.6, 1.2, 2.0]:
            for c in [0.0, 0.5, 1.0]:
                q = Q_scan(R=R, width=w, center=c)
                if q < best:
                    best, bestp = q, (R, w, c)
                print(f"R={R} w={w} c={c}: Q={q:+.3f}")
    print("best:", round(best, 4), bestp)
    assert best > 0, "destabilizer found (unexpected)"
    print("VERIFY_OK: no model destabilizer in scanned class; minimum +%.3f" % best)
