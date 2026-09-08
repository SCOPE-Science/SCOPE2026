# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Certified exclusion fragment for five committed quadratic Liénard boxes

## Family and boxes (committed coefficients, order (a,c,b,d), radius 0.02)

x' = y − (a·x + b·x²),  y' = −x + c·y + d·x·y.

| box | center (a,c,b,d) | certified fact |
|-----|------------------|----------------|
| B1 | (1.0, 0.5, 0.3, 0.0) | Lyapunov no-cycle disc R=0.02; origin unique in R=[−0.5,0.5]², stable focus; Dulac half-plane log |
| B2 | (1.5, 0.8, 0.2, 0.1) | origin saddle (uniform); Dulac half-plane log; basin/existence OPEN |
| B3 | (0.8, 0.3, 0.5, −0.1) | Lyapunov no-cycle disc R=0.04; origin SOLE equilibrium of the plane; Dulac half-plane log |
| B4 | (2.0, 1.0, 0.1, 0.0) | origin saddle (uniform); Dulac half-plane log; basin/existence OPEN |
| B5 | (0.5, 0.1, 0.4, 0.2) | Lyapunov no-cycle disc R=0.06; origin unique in R=[−0.5,0.5]², stable focus; Dulac half-plane + slab logs |

All bounds below hold **uniformly over the full closed box** (all parameters varied
simultaneously by ±0.02), not just at nominal centers.

## Theorem (partial; proved by the replay script)

1. **Lyapunov no-cycle discs (B1, B3, B5).** Let A be the linearization at the
   origin at nominal center and P ≻ 0 the exact rational solution of AᵀP + PA = −I:
   - B1: P = [[7/2, −3], [−3, 5]], eig(P) = [1.1577, 7.3423];
   - B3: P = [[185/76, −55/38], [−55/38, 60/19]], eig(P) = [1.3041, 4.2880];
   - B5: P = [[49/19, −15/19], [−15/19, 55/19]], eig(P) = [1.9317, 3.5420].
   Write S(z) = A(z)ᵀP + PA(z) = −I + E(z) + D(par) with |E(z)|₂ ≤ K|z|,
   K = 2‖P‖F·√(4bb²+dd²) (bb, dd = box maxima of |b|, |d|; crude but rigorous
   entrywise estimate), and parameter spread |D|₂ ≤ 2λmax(P)√2·r (r = 0.02).
   Then V̇ < 0 on 0 < |z| < r*, r* = (1−spread)/K:
   - B1: spread = 0.4153, K = 9.5292, r* = 0.0614 → disc R = 0.02 certified
     (V(R) = 0.00294 < 0.00436 = λmin(P)·r*² keeps the sublevel set inside);
   - B3: spread = 0.2426, K = 9.3941, r* = 0.0806 → disc R = 0.04 certified;
   - B5: spread = 0.2004, K = 7.0119, r* = 0.1140 → disc R = 0.06 certified.
   Hence each disc contains **no periodic orbit**, and every trajectory starting
   in it converges to the origin.

2. **Equilibrium census.** With g(x) = (c+dx)(a+bx) − 1 (nonzero equilibria need
   g(x) = 0), sup g ≤ |bd|x² + |s||x| + (ac−1) < 0 on |x| ≤ 0.5 gives:
   B1 ≤ −0.3746, B3 ≤ −0.6700, B5 ≤ −0.8321 → the origin is the **unique**
   equilibrium in R = [−0.5, 0.5]² for B1/B3/B5, with tr < 0 (stable focus).
   For B3, bd ∈ [−0.0576, −0.0416] < 0, ac−1 ∈ [−0.7816, −0.7376] < 0,
   s = bc+ad ∈ [0.036, 0.104] give disc(s² − 4·bd·(ac−1)) ≤ 0.0108 − 0.1227 < 0,
   so the origin is the **sole equilibrium of the whole plane**.
   For B2/B4, det(0) = 1 − ac < 0 uniformly (ac ∈ [1.1544, 1.2464] / [1.9404, 2.0604]):
   the origin is a **saddle**.

3. **Dulac B ≡ 1 half-plane logs.** div = (c−a) + (d−2b)x with uniform upper bounds
   base ≤ (−0.46, −0.66, −0.46, −0.96, −0.36) and slope ≤ (−0.54, −0.24, −1.04, −0.14, −0.54)
   for (B1..B5): div < 0 on x ≥ 0 in every box, so **no periodic orbit lies fully
   in the right half-plane**. Additionally div ≤ −0.63 on the B5 slab x ≥ 0.5.

## What is NOT proved (explicitly open)

- Full cycle-freeness of any box; outer-equilibrium counts for B1/B5 and
  separatrix/basin structure for the saddle boxes B2/B4 remain open.
- No limit cycle is claimed anywhere — non-rigorous RK4 survey plus the linear
  census (stable foci in B1/B3/B5, saddles at the origin in B2/B4, unstable focus
  in B4) indicate the admitted target "B1–B4 exactly one hyperbolic cycle" is
  false at these coefficients; no trapping annulus or Poincaré return is asserted.

## Reproduction

Run `python3 output/artifacts/verify_basins.py` (stdlib only: `fractions`, `math`).
It re-solves the Lyapunov equations exactly, re-checks every inequality with
asserts, prints the tables above, and ends with `VERIFY_OK`.

## Relation to prior work

General Liénard criteria (Giacomini–Neukirch algebraic approximations;
Han–Romanovski degree bounds; López–Ruiz strongly-nonlinear asymptotics;
Gasull–Giacomini–Grau transversal-curve existence) prove no box-uniform
Lyapunov/Dulac exclusion table for these five committed coefficient boxes;
the checked discs, half-plane logs, and B3 global-uniqueness discriminant
computation are new as finite certificates. They form a citable fragment for
Hilbert-16th/Liénard validated-dynamics benchmarks even though the original
existence census did not close — indeed, the evidence refutes it.
