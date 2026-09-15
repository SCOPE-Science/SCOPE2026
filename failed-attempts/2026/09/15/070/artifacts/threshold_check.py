"""Threshold check for Elekes + Stevens-de Zeeuw (SDZ) direct route.

Model bound: I(P,L) <= C*( m^{3/4} n^{3/4} + m + n + m*n/p )
with Elekes config m = S*Pprod, n = N^2, I >= N^3, N=|A|.
Solves implied lower bound on m in each regime and checks
exponent vs target m >> N^{5/2} (i.e. max >> N^{5/4}).

Also scans alpha = log_p(N) in {0.5, 0.5625, 0.625} to compare
main term vs Vinh term in refined configs with |P| ~ N^3.
"""
import math

def direct_bounds(N, p):
    out = {}
    # Regime A: main term dominates: N^3 << m^{3/4} N^{3/2} => m >> N^2
    out['main_implied_m'] = N**2
    out['main_implied_max_exponent'] = 1.0  # m>>N^2 => max>>N^1
    # Regime D: Vinh dominates: N^3 << m N^2 / p => m >> p*N
    out['vinh_implied_m'] = p * N
    return out

def scan():
    print("=== Direct Elekes + SDZ(3/4) ===")
    print("Main-term regime: N^3 <= m^{3/4} n^{3/4}, n=N^2 => m >= N^2.")
    print("Target needs m >= N^{2.5}. Hence main term alone gives exponent 1.0, NOT 1.25.")
    print()
    for alpha in [0.5, 0.5625, 0.625]:
        # p symbolic: take p = 10^12-ish scale via logs; use log_p arithmetic
        # Compare main-implied m (N^2) vs target (N^2.5) vs Vinh-implied (p*N = N^{1/alpha?} ...)
        # In log_p units: log_p(N)=alpha; log_p(N^2)=2a; log_p(N^2.5)=2.5a; log_p(pN)=1+a
        m_main = 2*alpha
        m_target = 2.5*alpha
        m_vinh = 1+alpha
        print(f"alpha={alpha}: log_p: main-implied={m_main:.4f} target={m_target:.4f} vinh-implied={m_vinh:.4f} "
              f"main_gap_to_target={m_target-m_main:.4f} (need 0 to close)")
    print()
    print("=== Refined config (|P|~N^3) Vinh check ===")
    print("SDZ/Vinh non-triviality needs |P|<<p^2 i.e. 3a<2, and mn/p subdominant needs |P||L|/p << main.")
    for alpha in [0.5, 0.5625, 0.625]:
        cond_p2 = 3*alpha - 2.0  # >0 means |P|>>p^2, hypothesis fails
        print(f"alpha={alpha}: 3a-2={cond_p2:+.4f} {'FAIL p^2 hypothesis' if cond_p2>0 else 'p^2 ok'}")
    print()
    print("=== Conclusion ===")
    print("Direct route caps at exponent 1 (trivial). Refined E4 route with |P|~N^3 hits p^2 hypothesis")
    print("at alpha=2/3; at alpha=5/8=0.625, margin is only 0.125 in log_p, and balancing the dyadic/E4")
    print("constants to keep exponent 5/4 forces the auxiliary product back under p^{1/2} regime.")
    print("No tuning of (m,n) split recovers N^{2.5} from m^{3/4}n^{3/4} main term.")

if __name__ == "__main__":
    scan()
