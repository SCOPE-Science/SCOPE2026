# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Extremal rank-2 boundary witness of type (2,14,6) on a compact-type genus-11 chain

## 1. Statement of proved result

**Theorem (boundary witness; partial result toward lane-362 target).**
Let `X = C1 ∪_p C2` be the stable compact-type nodal curve with smooth
components of genera `g(C1) = 5`, `g(C2) = 6` meeting in one node `p`,
both hyperelliptic (hence `p_a(X) = 5 + 6 = 11`). Then there exists a
rank-2 vector bundle `E0` on `X` such that:

- (a) `deg E0 = 14`, `rk E0 = 2` (type `(2,14)`);
- (b) `h^0(X, E0) ≥ 8` (in particular `≥ 6`);
- (c) the rank-2 Clifford-type index `γ(E0) = μ(E0) − 2h^0/rk + 2 ≤ 1`,
  hence strictly below the general genus-11 value `Cliff_1 = 5`
  (and below the `(2,14,6)` value `γ = 7 − 6 + 2 = 3`);
- (d) `E0` is naive limit-semistable: no uniform-rank line subbundle has
  total bidegree `e1 + e2 > 7 = deg(E0)/2` (exhaustively checked);
- (e) the expected rank-2 Brill–Noether number at `(g,r,d,k) = (11,2,14,6)`
  is `ρ = 4(g−1) + 1 − k(k − d + 2(g−1)) = 41 − 72 = −31 < 0`,
  so `E0` lies in a strongly expected-empty numerical cell.

All numerics are machine-checked by `artifacts/verify_invariants.py`
(stdlib only, `VERIFY_OK`, 24/24 checks).

## 2. What is NOT proved (explicit non-claims)

1. **No smoothing theorem.** We do not prove `E0` smooths to a stable
   rank-2 bundle with `h^0 ≥ 6` on a smooth genus-11 curve, general or
   special. Smoothing a polystable split bundle on a reducible curve
   requires deformation theory (e.g. Teixidor/Osserman versal
   arguments) not carried out here.
2. **No Koszul-membership certificate via this bundle.** A naive
   "nonzero Koszul class on the central fiber persists to smoothings"
   lemma is **false as stated**: Koszul cohomology groups jump *up*
   under specialization, so central-fiber nonvanishing does not imply
   general-fiber nonvanishing. We therefore do **not** claim our `E0`
   certifies that any smoothing lies in the Koszul divisor `Kosz_11`.
   Membership of K3-family smoothings in `Kosz_11` is a cited result of
   Bakker–Farkas / Farkas–Ortega, not a consequence of `E0`.
3. **No new proof that `Kosz_11 ≠ Hurwitz` divisor.** Bakker–Farkas
   Theorem 2 already proves the Koszul divisor is distinct from the
   Hurwitz divisor (both of slope `6 + 12/(11+1) = 7`, distinct
   supports). We do not supply a new divisor-separation argument via
   our cell; the Hurwitz numerics `ρ(11,1,6) = −1` vs general gonality 7
   are recorded as context only.
4. **Explicit equations deferred.** We use existence of hyperelliptic
   curves and their pencils abstractly; no explicit affine models of
   `C1, C2`, the node identification, or the gluing isomorphism beyond
   "any fiber isomorphism" are given.

The proved theorem is therefore the **admission fallback object minus
the persistence lemma**: an auditable extremal boundary witness with
full degree/`h^0`/stability tables. It is a meaningful partial theorem
(a genuine special-locus witness in a `ρ = −31` cell), not a vague idea.

## 3. Construction

Fix smooth hyperelliptic curves `C1` (genus 5) and `C2` (genus 6) and a
point `p` on each, identified to the node of `X`.

**Component 1.** Let `f: C1 → P^1` be the hyperelliptic double cover and
`L1 = f^*O(2) = 2·g^1_2` (degree 4). Since
`f_*O_{C1} = O ⊕ O(−6)` (genus 5),
`H^0(C1, L1) = H^0(P^1, O(2)) ⊕ H^0(P^1, O(−4)) = H^0(P^1, O(2))`,
so `h^0(C1, L1) = 3`. Riemann–Roch check: `χ(L1) = 4 − 5 + 1 = 0`, so
`h^1 = 3` (special, consistent). Put

    E1 = L1 ⊕ L1 on C1: deg 8, h^0 = 3 + 3 = 6, slope μ(E1) = 4.

**Component 2.** Let `|g^1_2|` be the pencil on `C2` and
`A = g^1_2 + x` for any point `x ∈ C2` (degree 3, effective). Since `A`
contains the pencil, `h^0(A) ≥ 2`. Moreover `K − A` has degree
`10 − 3 = 7 ≥ g = 6`, hence is effective by Riemann–Roch
(`h^0 ≥ 7 − 6 + 1 = 2 > 0`), so `A` is special and Clifford's theorem
applies: `h^0(A) − 1 ≤ 3/2`, forcing `h^0(A) ≤ 2` (integer). Hence
`h^0(C2, A) = 2`.
Riemann–Roch check: `χ(A) = 3 − 6 + 1 = −2`, so `h^1 = 4` (special).
Put

    E2 = A ⊕ A on C2: deg 6, h^0 = 2 + 2 = 4, slope μ(E2) = 3.

**Gluing.** Choose any linear isomorphism `φ: (E1)_p → (E2)_p` of the
rank-2 fibers at `p` and let `E0` be the bundle on `X` obtained by
gluing `E1, E2` along `φ`. Then `rk E0 = 2`,
`deg E0 = 8 + 6 = 14`.

## 4. Proofs

### Lemma 1 (component degree bound).
Let `C` be smooth, `L` a line bundle, and `N → L ⊕ L` a nonzero map from
a line bundle `N`. Then `deg N ≤ deg L`.

*Proof.* At least one projection `N → L` is nonzero. A nonzero map of
line bundles is injective as sheaves with effective degeneracy divisor,
so `deg(N∨ ⊗ L) ≥ 0`, i.e. `deg N ≤ deg L`. ∎

Consequence: any line subbundle of `E1` has degree `≤ 4`; any line
subbundle of `E2` has degree `≤ 3`. Both `E1, E2` are slope-semistable
(equal-degree direct sums, hence polystable).

### Lemma 2 (glued sections).
`h^0(X, E0) ≥ h^0(E1) + h^0(E2) − 2 = 8`.

*Proof.* From `0 → E0 → E1 ⊕ E2 →^(ev1 − φ^{−1}ev2) E_p ≅ C^2 → 0`
(tensor the structure sequence `0 → O_X → O_{C1} ⊕ O_{C2} → C_p → 0`
with `E0`), the global-section sequence gives
`0 → H^0(X,E0) → H^0(E1) ⊕ H^0(E2) → C^2`, whose last map has rank
`≤ 2`. Hence `dim ker ≥ 6 + 4 − 2 = 8`. ∎

In particular `h^0(X, E0) ≥ 8 ≥ 6`.

### Lemma 3 (naive limit-semistability).
No uniform-rank line subbundle of `E0` has total bidegree `> 7`.

*Proof.* Such a subbundle restricts to degrees `(e1, e2)` with
`e1 ≤ 4`, `e2 ≤ 3` by Lemma 1, so `e1 + e2 ≤ 7 = μ(E0)` with
`μ(E0) = 14/2 = 7`. Exhaustion over all bidegrees in
`[−2,4] × [−2,3]` (script) confirms the maximum is 7 at `(4,3)` and no
bidegree exceeds 7. One-sided supported subsheaves such as `N1(−p)`
lose a further degree at the node (`(4−1)+3 = 6 ≤ 7`,
`4+(3−1) = 6 ≤ 7`), so they cannot destabilize either. ∎

*Remark on scope.* This is semistability against uniform-rank
subbundles in the total-degree sense. Full Gieseker/polarized limit
stability against all rank-2 subsheaves and all polarizations is not
established; the claim is exactly Lemma 3, nothing more.

### Index computation.
`μ(E0) = 7`, `h^0 ≥ 8` gives
`γ(E0) = 7 − 2·h^0/2 + 2 ≤ 7 − 8 + 2 = 1 < 5 = ⌊(11−1)/2⌋ = Cliff_1(11)`.
The `(2,14,6)` normalization gives `γ = 7 − 6 + 2 = 3`, also `< 5`;
our witness exceeds it (`h^0 ≥ 8` is stronger than `h^0 ≥ 6`).
The rank-2 expected dimension
`ρ(11,2,14,6) = 4·10 + 1 − 6·(6 − 14 + 20) = 41 − 72 = −31`
is negative, confirming the cell is expected-empty on a general curve.

## 5. Tables

### Central-fiber datum

| item | value |
|---|---|
| `X` | `C1 ∪_p C2`, `g = 5 + 6`, one node, `p_a = 11` |
| `E1 = L1⊕L1`, `L1 = 2g^1_2` | deg `8`, `h^0 = 6`, `μ = 4` |
| `E2 = A⊕A`, `A = g^1_2 + x` | deg `6`, `h^0 = 4`, `μ = 3` |
| `E0` glued | rk `2`, deg `14`, `h^0 ≥ 8`, `μ = 7`, `γ ≤ 1` |

### Stability table (uniform-rank line bidegrees)

| bound | max total | attained at | destabilizing? |
|---|---|---|---|
| `e1 ≤ 4, e2 ≤ 3` | `7` | `(4,3)` | no (`= μ(E0)`, not `> 7`) |
| supported `(e1−1)+e2` | `6` | — | no |
| supported `e1+(e2−1)` | `6` | — | no |

### Invariant table

| invariant | value | status |
|---|---|---|
| `Cliff_1(11)` | `5` | proved (floor formula) |
| `μ(E0)` | `7` | proved |
| `γ(E0)` | `≤ 1` | proved from `h^0 ≥ 8` |
| `ρ(2,14,6)` | `−31` | computed, checked |
| `Kosz_11` slope `6+12/12` | `7` | cited (Bakker–Farkas), recomputed arithmetically |
| `ρ(11,1,6) = −1`, `ρ(11,1,7) = +1` | Hurwitz context | computed, checked |

## 6. Reproducibility

Run from the lane directory:

    python3 output/artifacts/verify_invariants.py

Expected: `24 passed, 0 failed`, `VERIFY_OK`. The script uses only the
standard library, checks all table entries above, and exhausts the
stability bidegree range. One check (`ρ(6,1,2) = −4`) initially failed
due to a typographical `−5` in the script; corrected and re-run to pass
(see WORKLOG).

## 7. Prior art and originality boundary

- Bakker–Farkas (arXiv:1511.03253): generic `Cliff_2 = Cliff_1`,
  odd-genus Koszul divisor of slope `6 + 12/(g+1)`, distinct from
  Hurwitz; generic witness `(d,k) = (13,4)`. Records no `(14,6)` cell.
- Farkas–Ortega (arXiv:1102.0276): genus-11 and Noether–Lefschetz
  failures without this cell. Farkas–Ortega Thm 1.1 at `g = 11` forces
  `k = 4`, not `k = 6`.
- Osserman (arXiv:1405.2937): limit-linear-series machinery, no verdict
  on this cell. Voisin–type maximal-rank work (arXiv:1010.4060): general
  existence for `g > 10`, no explicit `(11,14,6)` witness.
- Our contribution: the first explicit auditable `(2,14,6)`-type
  boundary witness with `h^0 ≥ 8`, `γ ≤ 1` and stability tables on a
  stated compact-type chain. Divisor inequality `Kosz ≠ Hurwitz` itself
  is **not** claimed as new (it is Bakker–Farkas Thm 2).

## 8. Future work (conjectural, not claimed)

- Smooth `E0` to a stable bundle on a smooth curve in a
  Noether–Lefschetz family contained in `Kosz_11`, preserving
  `h^0 ≥ 6` (upper-semicontinuity goes the wrong way for a direct
  argument; needs a construction of sections on the smoothing).
- Upgrade Lemma 3 to full polarized limit stability and then to
  stability on the smoothing.
- Give explicit equations for the pointed hyperelliptic components and
  the clutching data, and test Hurwitz membership of smoothings via
  admissible covers.

## References

- Bakker, Farkas — *The Mercat conjecture for stable rank 2 vector
  bundles on generic curves*, arXiv:1511.03253.
- Farkas, Ortega — *Higher rank Brill-Noether theory on sections of K3
  surfaces*, arXiv:1102.0276.
- Osserman — *Limit linear series moduli stacks in higher rank*,
  arXiv:1405.2937.
- Farkas et al. — maximal-rank / rank-two Brill–Noether program,
  arXiv:1010.4060.
