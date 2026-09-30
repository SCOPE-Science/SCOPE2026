# Sticky R3 Kakeya maximal exponent 0.49 at p=2 is false: the sticky bush attains 1/2

## Context
The 3D Kakeya dimension conjecture closed in 2025 (Wang–Zahl: every sticky Kakeya
set in R^3 has Hausdorff dimension 3). The Kakeya maximal conjecture in R^3
remains open. The admitted target sought a sticky-case maximal-operator
improvement at n=3, p=2: with gamma_HRZ the Hickman–Rogers–Zhang sticky-case
exponent, prove ||K_delta|| <= C_eps delta^{-(gamma_HRZ-0.01)-eps}.

## Definitions
- delta in (0,delta_0], Omega subset S^2 delta-separated, |Omega| >= c_0 delta^{-2}.
- T = {T_omega}: delta-tubes (unit height, radius delta) in B^3.
- Sticky in the Wang–Zahl sense (Definition 1.1): coaxial lines form a set of
  packing dimension n-1 = 2; quantitatively M = O(1) (fat/thin ratio bounded).
- HRZ tube-sum normalization (Conjecture 1.1, Kp):
  ||sum chi_T||_{L^p} <= C delta^{-(n-1-n/p)-eps} (sum|T|)^{1/p}.

## Result
Instantiated baseline: HRZ Theorem 1.2 + Figure 1 gives no improvement at n=3,
so at n=3, p=2 the proved exponent is n-1-n/p = 1/2; gamma_HRZ = 1/2 and the
target demands 0.49.

Theorem (target disproved). The claimed bound
  ||sum_{T in T} chi_T||_2 <= C_eps delta^{-0.49-eps} (sum|T|)^{1/2}
for all sticky families with M <= delta^{-eta} (eta <= 0.01) is FALSE.
The sticky bush through the origin (M = O(1) <= min(10, delta^{-eta}))
satisfies ||sum chi_T||_2 >= c delta^{-1/2} while (sum|T|)^{1/2} = O(1),
so gamma_HRZ = 1/2 is sharp on sticky families. Equivalently
||K_delta|| >= c delta^{-1/2} on f = chi_{B(0,delta)}.

## Proof / evidence
1. Baseline: HRZ Thm 1.2/Fig.1; n=3 maximal range stays Katz–Zahl p >= 5/3-eps.
2. Extremizer: maximal delta-separated Omega, N in [c_0 delta^{-2}, C_2 delta^{-2}]
   (c_0=1/2, C_2=20); T_e = delta-tube through origin in direction e.
   Lines {axes} = Lipschitz graph p=0 over S^2, packing dim 2: Wang–Zahl sticky.
   At scale rho, covered by ≲ rho^{-2} rho-tubes each holding ≲ (rho/delta)^2
   thin tubes: M = O(1).
3. Lower bound: each T_e contains B(0,delta/4), so sum chi >= N >= c_0 delta^{-2}
   there; ||sum chi||_2 >= sqrt(pi/48) c_0 delta^{-1/2}. sum|T| <= N pi delta^2 = O(1).
4. Contradiction: at eps_0=0.005, target RHS = C delta^{-0.495} sqrt(C_2 pi).
   Ratio R = K C^{-1} delta^{-0.005} -> infinity, K ≈ 0.016.
   C=1: violated for k > 1190.7 at delta=2^{-k} (k=1200 R≈1.03, k=2000 R≈16.5).
   General C: finite k*(C)=ln(C/K)/(0.005 ln2) (C=10^100 -> k*≈67629).
   Maximal form: K_delta chi_{B(0,delta)}(e) >= c delta for all e, ratio ≳ delta^{-1/2}.

## Limitations
Disproof addresses the L^2/operator exponent (the 0.01-gain content). The
"equivalently" union-volume form |∪T| >= c_eps delta^eps delta^{2 gamma}(#T delta^2)
with gamma=0.49 is strictly weaker (bush has |∪T| ≳ 1, #T delta^2 ≍ 1, satisfies
it with gamma=0) and is not disproved. Constants c_0, C_2 generous absolute;
radius conventions affect only prefactors, not the exponent.

## Reproducibility
python3 output/artifacts/verify_bush.py -> explicit k violations, k*(C)
thresholds, packing/sticky checks, VERIFY_OK (replayed by auditor).

## References
- Wang–Zahl, Sticky Kakeya sets and the sticky Kakeya conjecture, JAMS 2026, arXiv:2210.09581.
- Hickman–Rogers–Zhang, Improved bounds for the Kakeya maximal conjecture in higher dimensions, arXiv:1908.05589.
- Wolff, An improved bound for Kakeya type maximal functions, RMI 1995.
- Choudhuri, Sticky Kakeya sets in R^4, RMI 2026.
