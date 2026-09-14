# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Dyadic 4-arm quasi-multiplicativity at 1–2–4 with constant 2⁻¹⁰: proof

## Setting
Critical Bernoulli bond percolation on ℤ² at p = 1/2 (primal open with prob. 1/2;
closed otherwise; the dual model is likewise critical). For 0 < r < R let
Ann(r,R) = [−R,R]² ∖ interior([−r,r]²), and let A(r,R) be the alternating 4-arm
event: four pairwise-disjoint crossings of the annulus from its inner square
boundary to its outer square boundary, in cyclic order open (primal), closed-dual,
open, closed-dual. (Closed-dual = dual-open = primal-closed bonds; at p = 1/2 each
forced primal bond has probability 1/2 either way.)

## Theorem (target)
P(A(1,4)) ≥ 2⁻¹⁰ · P(A(1,2)) · P(A(2,4)).

## Proof
It suffices to prove the absolute bound P(A(1,4)) ≥ 2⁻¹⁰, since
0 ≤ P(A(1,2)), P(A(2,4)) ≤ 1 gives 2⁻¹⁰·P(A(1,2))·P(A(2,4)) ≤ 2⁻¹⁰.

Exhibit an explicit 10-bond forcing sub-event F ⊂ A(1,4):

- Open arm N: primal bonds (0,1)–(0,2), (0,2)–(0,3), (0,3)–(0,4), all open.
  Vertex path (0,1) → (0,4): starts on the inner boundary (max|·| = 1),
  ends on the outer boundary (max|·| = 4).
- Open arm S: primal bonds (0,−1)–(0,−2), (0,−2)–(0,−3), (0,−3)–(0,−4), all open.
  Vertex path (0,−1) → (0,−4), inner → outer.
- Closed-dual arm W: dual-vertex path (−1.5,0.5) → (−2.5,0.5) → (−3.5,0.5),
  i.e. require primal bonds (−2,0)–(−2,1) and (−3,0)–(−3,1) closed.
  Each dual step is a unit horizontal step crossing exactly the stated primal
  bond (horizontal dual bond at height 0.5 with midpoint (x,0.5) crosses the
  vertical primal bond (x,0)–(x,1)). Endpoints are dual sites 0.5 outside the
  inner square and 0.5 inside the outer square — a dual crossing of the annulus.
- Closed-dual arm E: dual-vertex path (1.5,0.5) → (2.5,0.5) → (3.5,0.5),
  i.e. primal bonds (2,0)–(2,1) and (3,0)–(3,1) closed. Same crossing property.

Verification (machine-checked in `output/artifacts/verify_forcing.py`):
1. The 10 forced primal bonds are pairwise distinct (6 open + 4 closed).
2. Each arm connects inner boundary to outer boundary (primal tracing;
   dual end-adjacency ±0.5 with unit-step continuity, plus the standard
   dual/primal crossing correspondence checked bond-by-bond).
3. Arms are pairwise bond-disjoint and land on distinct faces (N/E/S/W), so
   they are separated and non-touching; cyclic colour order O,C,O,C alternates.
Hence on F all four alternating arms exist disjointly: F ⊂ A(1,4).

Probability via RSW-separation/FKG-gluing decomposition. The four corridor
events involve disjoint bond sets, and group into same-monotonicity pairs:
{top-open} ∩ {bottom-open} (both increasing, FKG-glued, P = 2⁻³·2⁻³ = 2⁻⁶)
and {left-closed} ∩ {right-closed} (both decreasing, FKG-glued, P = 2⁻²·2⁻² = 2⁻⁴);
the two groups have disjoint supports, glued by independence. Thus
P(F) = 2⁻⁶ · 2⁻⁴ = 2⁻¹⁰ (each of the 10 bonds forced independently with
probability 1/2). Therefore P(A(1,4)) ≥ P(F) = 2⁻¹⁰, and the target inequality
follows from the product factors being at most 1. ∎

## Remarks
- The argument gives the absolute bound P(A(1,4)) ≥ 2⁻¹⁰ ≈ 0.00098, stronger
  than the stated relative inequality whenever the product factor is < 1.
- The corridors land on the middle of each face (x = 0 column; y = 0.5 rows),
  the standard RSW separation geometry; only straight corridors are needed at
  this small scale, so no RSW crossing-probability input beyond the p = 1/2
  symmetry is required.
- A bounded Monte Carlo gauge of straight-corridor sufficient sub-events
  (20k samples: S(1,2) ≈ 0.062 vs 2⁻⁴ exact; S(2,4) ≈ 0.0042 vs 2⁻⁸;
  S(1,4) ≈ 0.0003 vs 2⁻¹²) confirmed the forcing probabilities before the
  tighter 10-bond construction was adopted; it is diagnostic only and not part
  of the proof.
