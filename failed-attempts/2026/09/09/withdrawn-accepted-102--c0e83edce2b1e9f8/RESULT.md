# Fixed-cone excess decay fails at the Lawlor-critical Lagrangian pair: explicit calibrated neutral family

## Context
The admitted target asked for explicit fixed-cone rigidity-with-decay at the
Lawlor-critical symmetric Lagrangian plane pair Q in C^2 = R^4 (characteristic
angles (pi/2,pi/2), angle sum pi, density 2): some eps0>0, alpha0>0 such that
every 2D area-minimizing integral current T near Q has unique tangent a unitary
rotation of Q with E(T,Q,B_r) <= r^{2 alpha0} E(T,Q,B_1).
Qualitative 2D uniqueness (De Lellis-Spadaro-Spolaor) holds; no explicit
per-cone decay or non-decay certificate at Q was known.
The target's own failure clause requests an explicit excess-non-decay datum at
stated scales on failure. This record is that datum, proved at full strength.

## Definitions
- Identify C^2 = R^4 with (x1,y1,x2,y2), zj = xj + i yj.
- P0 = R^2 x {0} = {y1=y2=0}; P1 = {0} x iR^2 = {x1=x2=0}.
- Q = [[P0]] + [[P1]], oriented so the Lawlor form calibrates each sheet.
- phi = Re(dz1 ^ dz2) = dx1 ^ dx2 - dy1 ^ dy2 (constant, hence closed).
  This is the Lawlor special-Lagrangian form (beta=0), NOT the Kahler form
  omega0 = dx1 ^ dy1 + dx2 ^ dy2.
- U_delta = diag(e^{i(pi/2+delta)}, e^{i(pi/2-delta)}),
  P_delta = U_delta R^2, Q_delta = [[P0]] + [[P_delta]].
  (P0,P_delta) has characteristic angles (pi/2+delta, pi/2-delta), sum pi.
- Scale-invariant L^2 height excess vs fixed Q (m=2):
  E(T,Q,B_r) = r^{-4} int_{T cap B_r} dist(x,Q)^2 d||T||(x).
  Cones have constant E under this normalization.

## Result
**Theorem.** At the Lawlor-critical Q (M(Q cap B1) = 2 pi, Theta(Q,0) = 2),
fixed-cone decay as stated is false. For every eps0>0 and every alpha0>0 there
exists a 2D area-minimizing integral current T with 0 in spt T,
Theta(T,0)=2, E(T,Q,B1)<eps0, whose unique tangent cone at 0 is not a unitary
(indeed not an orthogonal) rotation of Q and which satisfies
E(T,Q,B_r) = E(T,Q,B1) > r^{2 alpha0} E(T,Q,B1) for every r<1.
In particular:
- Every Q_delta is calibrated by the SAME phi, hence area-minimizing,
  density 2, homogeneous, with unique tangent itself.
- E(Q_delta,Q,B_r) = (pi/2) sin^2 delta for every r>0 (scale-constant),
  -> 0 as delta -> 0.
- For 0<|delta|<=1/4, Q_delta is not in the SO(4)-orbit (hence not in the
  U(2)-orbit) of Q: principal angles (pi/2,pi/2) vs
  (pi/2-|delta|, pi/2-|delta|), gap |delta|.
- Explicit witness: eps0=0.01, delta=sqrt(0.01/pi)~0.0564,
  E(B1)=(pi/2)sin^2 delta~0.00500<eps0, E(B_{1/4})/E(B1)=1.

## Proof / Evidence
Analytic proofs (see DRAFT):
1. Comass: for real orthonormal a,b with complex vectors A,B,
   (dz1^dz2)(a,b)=det[A B], |det|^2 = 1-|<A,B>|^2 <= 1, so |phi|<=1;
   equality +1 on P0. Pullback on diag(e^{i theta1},e^{i theta2})R^2 is
   cos(theta1+theta2); here theta1+theta2=pi for P1 and every P_delta
   (-1 natural, +1 after flipping one orientation vector). Each sheet is
   Lagrangian (omega0 pullback 0). Hence phi calibrates Q and all Q_delta.
2. Q_delta minimizing, density 1+1=2, homogeneous; P_delta is a tan-delta
   graph over P1, so Hausdorff distance O(|delta|) and flat convergence
   Q_delta -> Q, E -> 0.
3. Excess: for |delta|<=pi/4, dist(p,Q)^2 = rho^2 sin^2 delta on P_delta
   (nearest sheet P1), integral sin^2 delta * int_0^r rho^2 2 pi rho drho
   = (pi/2) r^4 sin^2 delta; /r^4 gives (pi/2) sin^2 delta, r-independent.
4. Orbit exclusion: a subspace in a union of two subspaces lies in one of
   them, so an orthogonal map of pairs permutes sheets; inner-product
   matrices 0 vs diag(-sin delta, sin delta) give singular values
   (0,0) vs (|sin delta|,|sin delta|), i.e. angle gap |delta|>0.
5. Theorem follows: T=Q_delta homogeneous => blow-ups equal itself
   (unique tangent outside U(2).Q); constant positive excess vs
   r^{2 alpha0}<1 refutes decay at every scale (e.g. r=1/4).

Supporting computation (stdlib+numpy only, analytic proofs primary):
- verify_calibration_excess.py: pullbacks +1/-1, comass MC max ~0.99999<=1,
  excess table, mass 2pi -> VERIFY_OK.
- verify_angles_flat.py: angle pairs 87.14/84.27/78.54 deg vs 90 deg,
  gap |delta|, Hausdorff<=sin delta, scale law -> VERIFY2_OK.
- verify_target_obstruction.py: pullbacks, comass MC, scaling, witness
  formula for every eps0 -> VERIFY_OK.

## Limitations
- Rotation conclusion refuted for any excess notion; decay conclusion
  refuted for the standard scale-invariant L^2 height excess (r^{-4}) and
  normalized-flat variants.
- Does not prove a corrected decay-modulo-neutral-family statement; it
  diagnoses the kernel direction (angle-sum-pi family) such a statement
  must quotient by.
- Harvey-Lawson fundamental theorem and Lawlor angle threshold cited as
  background; comass bound proved analytically, Monte Carlo is a spot-check.
- Orbit exclusion at unoriented plane-pair level; orientation/multiplicity
  bookkeeping does not affect the tangent-cone statement.

## Reproducibility
Run from workspace root:
  python3 output/artifacts/verify_target_obstruction.py
  python3 output/artifacts/verify_calibration_excess.py
  python3 output/artifacts/verify_angles_flat.py
Expect VERIFY_OK / VERIFY2_OK lines and the numbers quoted above.

## References (background only)
- H. B. Lawson, R. Harvey, Calibrated geometries; M. Lawlor angle
  criterion; Lotay survey (minimality background, no per-cone decay).
- C. De Lellis, E. Spadaro, L. Spolaor, arXiv:1508.05266 (qualitative 2D
  uniqueness, consistent: each Q_delta has unique tangent itself).
- M. Engelstein, L. Spolaor, B. Velichkov, arXiv:1802.00418
  (integrability vs log-epiperimetric; interpretation only).
- A. Wood, arXiv:1910.06122; Y. Li, G. Szekelyhidi, arXiv:2410.22172
  (LMCF flow settings); S. Becker-Kahn, arXiv:1401.7660 (two-valued graphs).
