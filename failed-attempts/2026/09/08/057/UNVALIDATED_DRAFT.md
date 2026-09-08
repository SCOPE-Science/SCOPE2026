# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Certified forward-invariant annulus for the Van der Pol limit cycle at μ=1

## Theorem (fallback lemma; proved)
For `x' = y − x³/3 + x`, `y' = −x` (Van der Pol at μ=1), let `O` be the
convex CCW octagon with vertices (exact rationals)

- (2.87, 0.20), (2.86, 3.47), (−0.18, 3.09), (−1.25, 2.17),
- (−2.87, −0.20), (−2.86, −3.47), (0.18, −3.09), (1.25, −2.17),

and `I` the CCW octagon with vertices

- (0.45, −0.02), (0.25, 0.25), (−0.02, 0.41), (−0.40, 0.40),
- (−0.45, 0.02), (−0.25, −0.25), (0.02, −0.41), (0.40, −0.40).

Then:
1. `F·n_out < 0` strictly on every edge of `O` (field points strictly inside `O`);
2. `F·n_out-of-hole > 0` strictly on every edge of `I` (field points strictly
   out of `I`, i.e. into the annulus `A = interior(O) ∖ closure(I)`);
3. `0 ∈ interior(I)`, all vertices of `I` lie strictly inside `O`;
   hence `A` is a compact forward-invariant annulus containing no equilibrium;
4. `A` contains **exactly one** periodic orbit (the Van der Pol cycle);
5. every closed trajectory in `A` has period `T ≤ 530779/5000 < 106.16`.

## Certificates (replay: `python3 output/artifacts/verify_annulus.py`, stdlib only, exact `Fraction` arithmetic)
- Outer edge `sup(F·n_out)` upper bounds (unnormalized normals, Lipschitz grid N=40):
  `−4.6919, −0.1611, −0.0522, −0.2620` (×2 by centrosymmetry), all `< 0`.
- Inner edge `inf(F·n_out-of-hole)` lower bounds (N=60):
  `0.01722, 0.01111, 0.00246, 0.01053` (×2), all `> 0`.
  On each edge `h(t) = F·n` is an exact cubic in the edge parameter;
  `sup ≤ max_grid + L/2N`, `L = 3|h₃|+2|h₂|+|h₁|`, all in exact rationals.
- Nesting: `O` convex CCW (all 8 cross products `> 0`), origin strictly left of
  each `I` edge, each `I` vertex strictly left of each `O` edge — exact sign checks.
- Speed: `|F|² = x² + g²`, `g = y − x³/3 + x`. Hole `|x| ≤ 9/20`, so outside the
  hole either `|x| ≥ 9/20` (gives `|F|² ≥ 0.2025`) or `|x| ≤ 9/20` with
  `|F|² ≥ max(x², gap(x)²)`, `gap(x)` = distance from cubic nullcline to hole boundary.
  Exact grid `1/10000`: `min = 2601/62500 = 0.041616`; hole-edge slopes `≤ 38/5`,
  Lipschitz slack `0.00086` ⇒ `|F|² ≥ 1/25` on the strip ⇒ `|F| ≥ 1/5` on `A`.
- Perimeter: exact rational majorants give `P(O) ≤ 530779/25000 = 21.23116`.
  A closed curve in a convex body is no longer than its perimeter, so
  `T = ∮ ds/|F| ≤ P(O)/(1/5) = 530779/5000 ≈ 106.156`.

## Proof notes
- Equilibria: `−x = 0`, `y − x³/3 + x = 0` ⇒ unique equilibrium `(0,0) ∈ I`, so `A`
  is equilibrium-free. Forward invariance follows from strict transversality on
  both boundaries. Poincaré–Bendixson ⇒ `A` contains a periodic orbit.
- Uniqueness: the system is Liénard with `F(x) = x³/3 − x` odd, `F'(x) = x²−1`
  (single positive zero `a = 1`, `F < 0` on `(0,1)`, `F > 0` increasing for
  `x > 1`), `g(x) = x` odd with `xg(x) > 0`. Classical Liénard theorem ⇒ at most
  one closed orbit in the plane ⇒ the orbit in `A` is the unique limit cycle.
- Origin is an unstable focus (Jacobian `[[1,1],[−1,0]]`, eigenvalues
  `(1±i√3)/2`), consistent with outward crossing of `I`.

## What is NOT claimed
- No two-sided period/amplitude enclosure (`U−L ≤ 0.05` target) and no
  harmonic-separation witness: the validated-integrator leg was not completed;
  the transit bound `T < 106.16` is one-sided and weak (orbit-length/perimeter
  argument with the coarse global speed bound `|F| ≥ 1/5`).
- No contraction/return-map argument; uniqueness comes from analytic Liénard
  theory, not from validated numerics.

## Reproducibility
- `output/artifacts/verify_annulus.py` — single stdlib-only exact verifier, exit 0 (ALL PASS).
- Intermediate scripts: `s1_scan.py`, `s2a_verify_outer.py`, `s2b_hill.py`, `s4_minspeed.py`
  (search/scout only; not needed for the certificate).
- Python version used: 3.x stdlib only (`fractions`, `math`, `sys`).
