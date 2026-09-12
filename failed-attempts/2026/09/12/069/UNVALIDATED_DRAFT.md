# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Primitive Bloch invariant for +1 figure-eight surgery: disproof of the target as stated

## Claim (TARGET refutation)

Let M be +1 Dehn surgery on the figure-eight knot. The target presupposition that M is
hyperbolic — carrying a hyperbolic invariant trace field K_M, hyperbolic complex volume
Vol(M) + i 2 pi^2 CS(M), and a hyperbolic Neumann–Yang Bloch invariant beta(M) — is
**false**. M is a closed small Seifert fibered space (hence non-hyperbolic), so the
hyperbolic Bloch invariant, trace field, and complex volume described in the target do
not exist for M. A fortiori there is no nontorsion primitive beta(M) generating a free
rank-one summand with a unified rational multiple q pinning volume and Chern–Simons
simultaneously. The target is disproved (refutation alternative), not merely unproven.

## What is proved exactly (machine-checked) vs cited classification vs heuristic

### 1. Exact machine-checked certificate (run: `python3 output/artifacts/cert1229b.py`)
- B3 Artin action on F(x0,x1,x2) with s1: x0 -> x0 x1 X0, x1 -> x0, x2 -> x2 and
  s2: x0 -> x0, x1 -> x1 x2 X1, x2 -> x1; stated inverses verified as two-sided
  identities in Aut(F3); braid relation s1 s2 s1 = s2 s1 s2 verified in Aut(F3).
- beta = s1 s2^-1 s1 s2^-1 has closure permutation (1,2,0), a 3-cycle, hence connected
  closure: a knot. Writhe = 0, word length 4, so crossing number <= 4.
- Closure relators: r0 = x0x2X0X2x1x2x0X2X0X0, r1 = x0x2X0X1, r2 = X2X1x2x0X2x1.
- Tietze elimination via r1 (x1 = x0x2X0, verified by reduction to empty word):
  s0 = abABabAbaBAA, s2 = BaBAbaBabA (a = x0, b = x2).
- Fox calculus with abelianization a,b -> t: d(s0)/da = 1-3t+t^2,
  d(s2)/da = -t^-2+3t^-1-1; exact Laurent gcd (Euclid over Q) is monic t^2-3t+1.
- Exact integer SNF (Bareiss minors): abelian relation matrix rows
  (-1,1,0),(0,-1,1),(1,0,-1) give H1(complement) = Z; adding the +1-filling row
  (meridian killed; longitude is null-homologous hence row (1,0,0) up to basis)
  gives H1 = 0: the +1 filling is an integral homology sphere.
- Knot identification: crossing number <= 4 plus Alexander polynomial t^2-3t+1
  identifies the knot as the figure-eight 4_1 (the only knot with <= 4 crossings
  with that polynomial; trefoil has t^2-t+1, unknot has 1). The figure-eight is
  achiral, so +1 and -1 surgeries agree up to orientation.

### 2. Cited classification step (not recomputed; standard theorem)
- By the Gordon / Thurston / Lackenby–Meyerhoff exceptional-surgery classification
  for the figure-eight knot, +1 surgery is one of the 10 exceptional slopes and is a
  small Seifert fibered space, hence by geometrization/Perelman not hyperbolic.
- A closed hyperbolic 3-manifold group is the fundamental group of a closed hyperbolic
  3-manifold; small Seifert fibered integral homology spheres in this class are not
  hyperbolic. Therefore M admits no hyperbolic structure, no hyperbolic invariant
  trace field K_M distinct from Q(sqrt(-3)), no hyperbolic complex volume, and no
  hyperbolic Neumann–Yang invariant beta(M) as postulated.

### 3. Numerical corroboration (heuristic only, not part of proof)
- Riley-type ansatz A = [[1,1],[0,1]], B = [[1,0],[w,1]] solves both certified
  relators at w = (1-i sqrt(3))/2 with residual norm ~1.8e-31 (Newton from grid best).
- Null-homologous word l = bABaaBAb (length 8) centralizes the meridian with
  commutator norm 0.0 and trace -2 in this cusp representation (peripheral curve).
- 12-start Newton search for a representation of the filled group found no solution
  (all residuals large), consistent with absence of a closed hyperbolic structure.
  This is corroboration only; the refutation rests on (1) + (2).

## Conclusion
The target's hyperbolic presupposition fails for +1 surgery on the figure-eight knot.
The complete answer required by the target is therefore the certified refutation:
torsion/divisibility-collapse alternative in the strong sense — the postulated
hyperbolic beta(M), K_M, and complex volume do not exist, so no primitive generator
with a unified rational multiple q exists either. QED (refutation).

## Reproduction
- `python3 output/artifacts/cert1229b.py` (stdlib only) reproduces checks A1–E3;
  expected output is stored in `output/artifacts/cert1229.log`.
- Heuristic scripts `riley_heuristic.py`, `longitude_heuristic.py` reproduce the
  numerical corroboration and are labeled as such.
