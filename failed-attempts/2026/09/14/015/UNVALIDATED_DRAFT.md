# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Second-order joint flattener for rotation numbers 1/4 and 1/6 in centrally symmetric near-circular billiards

## Claim
Let the billiard table be given by the support function
h(t) = 1 + e*cos(10t) + e^2*(a*cos(20t) + c*cos(40t)), small e > 0.
Let R_q(e) be the range over the rotation parameter s of the perimeter of the
frozen equal-spaced q-gon with vertices at support angles s + 2*pi*j/q
(a necessary-condition diagnostic: an exact smooth rational caustic of rotation
number 1/q requires the true pinned-minimal q-gon perimeter to be s-independent;
the frozen diagnostic captures its leading resonances). Then:

1. (First-order selection rule.) A pure mode h = 1 + e*cos(kt) breaks the
   frozen 1/q diagnostic at first order iff q divides k: measured log-log slope
   of R_q(e) is 1.000 when q|k and >= 2 otherwise (2.000 for q=4, 3.000 for
   q=6 in the non-resonant cases). Under central symmetry (k even), the joint
   1/4+1/6 first-order survivors are k = 2 (ellipse direction) and
   k = 10, 14, 22, 26, ... — so linearized theory alone cannot prove rigidity.
2. (Explicit second-order joint rescue.) For the lowest non-elliptic joint
   survivor k=10, the uncorrected residual is R_4 = 2.83*e^2 + O(e^3)
   (slope 2.000). The choice (a,c) = (-1/4, 0), i.e.
   h*(t) = 1 + e*cos(10t) - (e^2/4)*cos(20t),
   suppresses R_4 to O(e^3) (measured slope ~3.9 over e in [5e-4, 4e-3];
   R_4(2e-3) drops from 1.13e-5 to 2.8e-12), while the 6-gon diagnostic stays
   at O(e^3) (slope ~3.0), because q=6 first-order resonances involve only
   modes divisible by 6. A third-order scan finds no joint obstruction either.
3. (Mechanism.) Corrections decouple by divisor class: q=4 killers are modes
   divisible by 4 (20, 40); q=6 killers are modes divisible by 6 (30, 60).
   The sets are disjoint, so the two resonant constraints do not interfere at
   orders 1-3. Any rigidity proof for coexisting exact 1/4 and 1/6 caustics must
   therefore use global or infinite-order mechanisms.

## Proof / evidence
- First variation: d/ds of the q-gon length at first order in the deformation
  mu(t) = sum c_k e^{ikt} is proportional to sum_{j=0}^{q-1} mu(s+2*pi*j/q),
  which equals q*c_k*e^{iks} if q|k and 0 otherwise. This is analytic.
- Numerical verification: `output/artifacts/recovery_test_v2.py` produces
  `output/artifacts/results_v2.json` (slopes 1.000/2.000/3.000 as above).
- Rescue: `output/artifacts/rescue_v3.py` grid-finds (a,c)=(-0.25,0.0);
  `output/artifacts/rescue_v4.py` produces `output/artifacts/results_v4.json`
  confirming the jointly corrected scalings and the failed third-order
  obstruction search. All shapes satisfy convexity (h+h''>0) at tested e.

## Limitations (what is NOT claimed)
- The frozen equal-spaced diagnostic is necessary but not sufficient for an
  exact rational caustic: true caustics require constancy of the pinned
  minimal-perimeter functional m_q(s) = min over q-gons pinned at x(s), plus
  smoothness and genuine billiard reflection at each vertex. Only the frozen
  diagnostic was flattened here.
- The result is finite-order (through O(e^2) with O(e^3) residual) and
  near-circle; it is neither a rigidity proof nor a certified exact coexistence
  table, and convergence of the correction ladder is not established.
- An early attempt with pinned-minimizer numerics was discarded after it
  returned nonzero ranges even for circles/ellipses (optimizer/pinning
  misformulation), so no claims rest on it.

## Reproduction
Run with numpy only:
  python3 output/artifacts/recovery_test_v2.py
  python3 output/artifacts/rescue_v3.py
  python3 output/artifacts/rescue_v4.py
and compare against `output/artifacts/results_v2.json`, `results_v4.json`.
