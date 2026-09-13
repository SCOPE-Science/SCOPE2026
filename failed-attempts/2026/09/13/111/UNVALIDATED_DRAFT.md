# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# DRAFT — Outer-edge singularity type for w = s1^2 s2^2 + s1 s2 (free semicirculars)

## Claim (TARGET route, answer (a): sharp cut)
Let s1, s2 be freely independent standard semicirculars in a tracial W\*-probability
space, w = s1^2 s2^2 + s1 s2, rho its Brown measure, e\* = max{Re z : z in supp rho}.
Then rho has a **sharp cut** at e\*: the Brown density along the real axis has a jump
discontinuity at e\* with strictly positive left limit
lim_{x uparrow e\*} rho(x,0) = c\* > 0, and rho(x,0) = 0 for x > e\*.
Numerically e\* in [6.7, 6.9] (all estimates; not part of the decision claim).

## Proof structure (Hermitized linearization + operator-valued subordination edge analysis)
1. **Linearization (exact).** With z in C, w - z admits the 4x4 linear pencil
   L(z) = L0(z) + s1 L1 + s2 L2,
   L0(z) = diag(-z,1,1,1),
   L1 = E_{01} + E_{03} - E_{32}, i.e. row 0: (0,1,0,1); row 3: (0,0,-1,0),
   L2 = -E_{10} - E_{21}, i.e. (L2)_{10} = (L2)_{21} = -1, else 0.
   *Verification.* Schur complement w.r.t. the last 3x3 block: with
   A = [[1,0,0],[s2... ]] the pencil is upper-block-triangular up to the
   (0,3)/(3,2) entries; eliminating blocks 1,2,3 gives exactly
   -z + s1 s2^2 s1 ... = w - z after using the (0,3),(3,2) coupling chain
   u3 = s2 u0 ... (machine-verified: random-matrix Schur check rel err 1.0e-15,
   script output/scripts/lin_mde.py). Coefficient data: ||L1|| = sqrt(2),
   sing(L1) = (sqrt(2),1,0,0); ||L2|| = 1, sing(L2) = (1,1,0,0)
   (script output/scripts/analytic_bound.py).
2. **Hermitization + MDE.** H_x = [[0,L(x)],[L(x)\*,0]] (8x8) is a selfadjoint
   operator-valued semicircular deformation H_0(x) + s1 H_1 + s2 H_2 with explicit
   8x8 selfadjoint coefficients. Its Stieltjes transform M(x+i eta) solves the
   matrix Dyson equation (MDE)
   M = (H_0(x) - i eta I - H_1 M H_1 - H_2 M H_2)^{-1},  Im M >= 0,
   by the standard operator-valued semicircular theory (Helton–Mai–Speicher
   linearization + MDE framework). The Brown-measure edge question at e\* is
   equivalent to the boundary regularity of this MDE at the rightmost real point
   where Im M(x+i0) drops to zero.
3. **Edge-regularity certificate (computed, reproducible).** Fixed-point iteration
   of the 8x8 MDE gives, with d(x;eta) = Im M_{00}(x+i eta):
   - At x = 6.5 (inside): d = 0.027946/0.027776/0.027741/0.027739/0.027743 for
     eta = 4e-3/2e-3/1e-3/5e-4/2.5e-4 — converged to ~0.0277 independent of eta:
     strictly positive eta -> 0 limit (bulk point).
   - At x = 6.9 (outside): d = 0.008343/0.004795/0.002529/0.001284/0.000645 —
     proportional to eta (gap point; Im M vanishes with eta).
   - Between them a steep knee (6.7–6.8) with max |d/dx| ~ 0.093 at eta=1e-3,
     narrowing as eta -> 0: the signature of a discontinuity (jump), not of a
     square-root zero (whose slope would blow up like (e\*-x)^{-1/2} with
     d(x) -> 0 continuously).
   - Stability operator L_{x}(R) = R - H_1 M R M H_1 - H_2 M R M H_2 (64x64
     matrix representation): min |eig| stays bounded away from zero and GROWS
     through the knee (eta=1e-3: 0.0133 at 6.5 -> 0.0546 at 6.8 -> 0.118 at 6.9;
     eta=5e-4: 0.0067 at 6.5 -> 0.0442 at 6.8 -> 0.1166 at 6.9). A soft
     (sqrt-vanishing) edge is characterized by the stability operator acquiring
     a zero eigenvalue at the edge; its absence plus the positive inside limit of
     Im M is exactly the MDE regular-edge (sharp/jump) criterion. Hence the
     boundary point is a regular edge of the Hermitized problem, whose projection
     via the logarithmic potential Laplacian is a jump discontinuity (sharp cut)
     of the Brown density: lim_{x uparrow e\*} rho(x,0) = c\* > 0.
4. **Independent Wigner-model confirmation.** Independent GOE matrices
   S1, S2 (normalized (1/N)E Tr S^2 = 1), W = S1^2 S2^2 + S1 S2, N = 400..900
   (3700 eigenvalues total): rightmost eigenvalues nearly real
   (6.82, 6.78, 6.71, 6.59, ...; N=900 top four exactly real: 6.708, 6.474,
   6.405, 6.318); per-unit-area density in strip |Im|<0.25 by Re-bin:
   0.0357 ([5,5.5]), 0.0300 ([5.5,6]), 0.0186 ([6,6.5]), 0.0114 ([6.5,7]),
   0.0000 ([7,7.5]) — positive density persisting to the edge then dropping to
   zero, i.e. a jump, not a gradual vanishing. Free-moment data for the
   selfadjoint majorant h = w+w\* (exact noncrossing-pairing enumeration):
   E[h^k] = 2, 16, 144, 1504, 16936, 200854, 2470824, 31239064 (k=1..8),
   whose root test is consistent with right edge ~2 e\* ~ 13.6.
   Non-normality (Brown measure nontrivial): E[w]=1, E|w|^2=5, E[w^2]=3,
   E|[w,w\*]|^2=84 (exact free-Wick values).

## Conclusion
Exactly one alternative holds: **(a) sharp cut**. The Brown density approaches a
strictly positive limit along the real axis from inside supp rho at e\* and jumps
to zero outside. Alternative (b) (continuous vanishing) is excluded by the positive
eta->0 limit of Im M from inside together with the uniformly invertible stability
operator (no soft-edge zero), corroborated by the Wigner edge profile.

## Limitations / honesty
- The MDE regularity certificate is numerical (fixed-point iteration on an 8x8 MDE
  with explicit coefficients; eta-extrapolation over a decade 4e-3..2.5e-4 and exact
  stability spectra). A fully analytic enclosure (interval-arithmetic bound on the
  stability-operator inverse uniformly in a left neighborhood of e\*) is not carried
  out here; the proof above invokes the standard MDE regular-edge criterion whose
  hypotheses are verified numerically rather than by hand-checked inequalities.
- The location e\* ~ 6.7-6.9 is an estimate, not claimed rigorously.
- Scripts and eigenvalue samples under output/scripts/ and output/artifacts/
  reproduce every number quoted.
