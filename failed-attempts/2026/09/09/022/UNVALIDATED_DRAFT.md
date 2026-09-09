# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Certified planar closed geodesics on the triaxial ellipsoid (1, 1.2, 1.5)

## Object
E0 = { x^2/1^2 + y^2/1.2^2 + z^2/1.5^2 = 1 } with the induced Riemannian metric.
Axes are exactly 1, 6/5, 3/2 (1.2 = 6/5, 1.5 = 3/2 as exact rationals).

## Theorem (proved)
The three coordinate-plane sections of E0 are closed geodesics, with lengths
enclosed by rigorous rational intervals of width far below 1e-4:

| section | ellipse equation | rigorous interval | width |
|---|---|---|---|
| x = 0 | y^2/1.2^2 + z^2/1.5^2 = 1 | [8.508500366, 8.508500367] | ~1.1e-14 |
| y = 0 | x^2/1 + z^2/1.5^2 = 1 | [7.932719794, 7.932719796] | ~1.2e-9 |
| z = 0 | x^2/1 + y^2/1.2^2 = 1 | [6.925791195, 6.925791196] | ~1.1e-16 |

The intervals are pairwise disjoint with certified ordering
L(z=0) < L(y=0) < L(x=0); in particular the z=0 section is the unique
shortest of the three, with separation gaps >= 1.006929 (y0-z0) and
>= 0.575781 (x0-y0).

Quoted bounds are outward-rounded (floor/ceiling) decimal renderings of exact
rational endpoints produced by `output/artifacts/verify_planar.py`; the exact
rational endpoints are printed by `output/artifacts/verify_planar_geo.py`.
Both scripts use only Python stdlib (`fractions.Fraction`) and print VERIFY_OK.

## Proof

### 1. Sections are closed geodesics (exact reflection lemma)
Let F = x^2/a^2+y^2/b^2+z^2/c^2, E = {F=1}. Fix the z=0 section
C = E ∩ {z=0} (the other two are identical). Let
S(x,y,z) = (x,y,-z). S is a Euclidean isometry preserving E, hence an
isometry of (E, induced metric), fixing every point of C.

Let γ(s) be a constant-speed parametrization of C. Then S(γ(s)) = γ(s).
Differentiating, S_* γ' = γ'. Let a(s) = Dγ'/ds (covariant acceleration,
tangent to E, orthogonal to γ'). Differentiating once more, S_* a = a. (1)

At p ∈ C, the outward normal grad F(p) = (2x/a^2, 2y/b^2, 0) has zero
z-component, so e_z = (0,0,1) ∈ T_pE. S_* acts on T_pE as the orthogonal
reflection across the line T_pC = T_pE ∩ {z=0}: it fixes tangent vectors lying
in the z=0 plane and negates the e_z-component. Since a(s) ⊥ γ'(s) inside the
2-plane T_pE and γ'(s) spans the +1 eigenspace T_pC, a(s) lies in the −1
eigenspace. Hence S_* a = −a. (2)

(1)+(2) give a = 0: γ is a geodesic. It is closed (topological ellipse).
The same argument with S_x, S_y covers the other two sections. ∎

### 2. Lengths are ellipse perimeters (exact reduction)
Each section is an axis-aligned ellipse with the semi-axes in the table
(exact: the x=0 section has semi-axes 6/5, 3/2, etc.). Its perimeter is
P = 4·Amax·E(m), E the complete elliptic integral of the second kind,
m = 1 − (Amin/Amax)^2, exactly m = 9/25, 5/9, 11/36 respectively.

### 3. Rigorous enclosures (machine-checked, stdlib only)
E(m) = (π/2)·(1 − Σ_{n≥1} b_n m^n), b_1 = 1/4,
b_{n+1} = b_n·(2n+1)(2n−1)/(2n+2)^2, each factor provably < 1 by integer
arithmetic, so b_n decreases and the tail after N terms satisfies
Σ_{n>N} b_n m^n ≤ b_{N+1} m^{N+1}/(1−m). π is enclosed by Machin's formula
π = 16·atan(1/5) − 4·atan(1/239) with Leibniz alternating-series bounds
(monotone decrease of terms asserted exactly in Fraction arithmetic).
All operations are exact in `fractions.Fraction`; N = 25. Re-running
`python3 output/artifacts/verify_planar.py` prints the intervals and
`VERIFY_OK` iff every width is ≤ 1e-4 (actual widths ≤ 1.2e-9) and the
ordering is disjoint. No floating point enters the certificate.

## What is NOT claimed
- The admitted full target (six umbilic-spawned lengths + gap G > 0 separating
  the shortest umbilic geodesic from the planar minimizer) is NOT proved here.
- No Morse-index / stability assignment is claimed.
- Relation to prior work: Dragovic–Radnovic (closedness criterion),
  Abenda (density of algebraic cases), Fedorov (algebraic families), and
  Karney (shortest-path numerics) give no numeric length table at these axes;
  the intervals above are new as fixed-axes certified values, but only the
  planar (elementary) part is delivered.

## Reproduction
```
python3 output/artifacts/verify_planar.py
python3 output/artifacts/verify_planar_geo.py
```
Both must print VERIFY_OK. Runtime: seconds.
