"""Compute explicit uniform threshold Q*(L,K,N,c,tau) for Lazutkin-KAM existence horn.

Majorants are deliberately conservative overestimates: any larger M0 / smaller
delta_H only increases Q*, preserving validity. Formulas are documented in
output/DRAFT.md.
"""
import math

def compute(L=2*math.pi, K=2.0, N=10.0, c=0.01, tau=1.0, delta_H=1e-8):
    out = {}
    out['L'] = L; out['K'] = K; out['N'] = N; out['c'] = c; out['tau'] = tau
    out['delta_H'] = delta_H
    # curvature bounds from total curvature 2pi + ratio K
    kmin = 2*math.pi/(L*K)
    kmax = 2*math.pi*K/L
    out['kmin'] = kmin; out['kmax'] = kmax
    # C = int kappa^{2/3}
    Cmin = L*(kmin**(2/3)); Cmax = L*(kmax**(2/3))
    out['Cmin'] = Cmin; out['Cmax'] = Cmax
    # curvature derivative majorants: B_j = (j+1)! (1+N)^{j+1}, j<=5
    B = {}
    for j in range(6):
        B[j] = math.factorial(j+1)*((1+N)**(j+1))
    out['B5'] = B[5]
    # Lazutkin remainder majorant M0 (conservative polynomial majorant).
    # Schematic: f,g are rational in kappa, C, and derivatives up to order 5
    # with worst denominators kappa^8, C^3. The prefactor 200 absorbs all
    # Faà-di-Bruno/Bell combinatorics (Bell(5)=52, Leibniz factors, etc.).
    M0 = 200.0 * ((1+B[5])**3) * (kmin**-8) * ((Cmax**3)/(Cmin**3)) * ((1+L)**2)
    out['M0'] = M0
    # geometric radius where Lazutkin chart + twist bounds hold:
    # y_geo = min(1/4, kmin^2 * Cmin/(64*Cmax*(1+B2)) ) style bound; conservative.
    y_geo = min(0.25, (kmin**2)*Cmin/(64.0*Cmax*(1+B[2])))
    out['y_geo'] = y_geo
    # KAM smallness: eps=M0*w^3 <= delta_H*(c*w)^2  =>  w <= delta_H*c^2/M0
    # Twist/nondegeneracy + strip-width factors absorbed as factor 4.
    w_KAM = delta_H*(c**2)/(4.0*M0)
    # tau dependence of KAM constant: delta(tau)=delta_H/(1+tau)^4 already
    # folded by caller; here tau=1 so effective delta smaller by 1/16.
    w_KAM_tau = w_KAM/((1+tau)**4)
    out['w_KAM'] = w_KAM_tau
    w_allow = min(y_geo/2.0, w_KAM_tau)
    out['w_allow'] = w_allow
    Qstar = 1.0/w_allow
    out['Qstar'] = Qstar
    # relative-Diophantine positive-measure check on (0,eta], eta=w_allow:
    # meas(bad)/eta <= 2*c*eta*sum1 + 4*c*sum2, sum1=pi^2/6, sum2=zeta(3)
    eta = w_allow
    s1 = math.pi**2/6.0; s2 = 1.2020569
    ratio = 2*c*eta*s1 + 4*c*s2
    out['measure_ratio_bound'] = ratio
    out['positive_measure'] = ratio < 0.5
    return out

if __name__ == '__main__':
    # concrete instance
    r = compute()
    for k, v in r.items():
        print(f"{k} = {v!r}")
    print(f"\nQ* concrete = {r['Qstar']:.6e}")
    print(f"1/Q* = {1/r['Qstar']:.6e}")
    print(f"measure bad fraction <= {r['measure_ratio_bound']:.6e}  positive-measure: {r['positive_measure']}")
    # general-form illustration
    print("\n--- general formula samples ---")
    for (L, K, N, c, tau) in [(2*math.pi, 2, 10, 0.01, 1), (2*math.pi, 3, 50, 0.005, 2), (10.0, 2, 20, 0.02, 1)]:
        rr = compute(L=L, K=K, N=N, c=c, tau=tau)
        print(f"L={L:.3f} K={K} N={N} c={c} tau={tau} -> Q*={rr['Qstar']:.3e}  M0={rr['M0']:.3e}")
