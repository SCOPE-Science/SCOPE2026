# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Refutation of the extremal Salem braid-word target (lane-763)

## 1. Statement

Let `w* = σ1^3 σ2^{−1} σ1 σ2^{−2} ∈ B3`.
The target claims, as a conjunction:

- (a) `w*` is pseudo-Anosov;
- (b) its dilatation `λ(w*)` equals the largest root `≈ 1.401` of a degree-6 Salem polynomial;
- (c) that root is a Salem number;
- (d) `w*` is the minimal-entropy monodromy in a named punctured-torus-bundle face, forcing sharpness of a neighboring face gap.

Inputs specify no polynomial, no face name, and no tolerance, so only the
word-to-dilatation core (a)–(c) is literally auditable. We refute that core
exactly; hence the conjunction is false as stated.

**Theorem.** For `w* = σ1^3 σ2^{−1} σ1 σ2^{−2}`, the reduced action
`ρ(w*) ∈ SL(2,Z)` has trace `20`, characteristic polynomial `x^2 − 20x + 1`,
and dilatation `λ(w*) = 10 + 3√11 ∈ (19.948, 19.951)`, with Galois conjugate
`10 − 3√11 ∈ (0.049, 0.052)`. In particular `λ(w*) ≠ 1.401…`; it is a
quadratic Pisot number, not a degree-6 Salem number. Moreover every
pseudo-Anosov 3-braid has `λ ≥ (3+√5)/2 > 2.618 > 1.401`, so no convention
change or word-reading rescue can reach `1.401` under the D3 meaning; and no
D3 train-track matrix for `w*` can have spectral radius `1.401`.

## 2. Method

Standard faithful (up to center) representation `ρ : B3 → SL(2,Z)` with

```
ρ(σ1) = [[1,1],[0,1]],   ρ(σ2) = [[1,0],[−1,1]],
```

the once-punctured-torus / thrice-punctured-disk action. Nielsen–Thurston
type of a 3-braid is read from `t = |tr ρ(w)|`: `t > 2` pseudo-Anosov,
`t = 2` reducible, `t < 2` periodic; for `t > 2` the dilatation is the
spectral radius (larger eigenvalue). The same route is calibrated on the
known D3-minimum word `σ1σ2^{−1}`.

## 3. Computation (exact integers; replay `output/artifacts/verify_target_refutation.py`)

1. **Homomorphism check.** `ρ(σ1)ρ(σ2)ρ(σ1) = ρ(σ2)ρ(σ1)ρ(σ2) = [[0,1],[−1,0]]`,
   and all generators have determinant 1.
2. **Image of `w*`.** `ρ(σ1)^3 = [[1,3],[0,1]]`, `ρ(σ2)^{−2} = [[1,0],[2,1]]`,
   and (left-to-right convention)
   `ρ(w*) = [[18,7],[5,2]]`, trace `20`, determinant `1`.
   Right-to-left convention gives the transpose `[[2,7],[5,18]]`, same trace
   `20` and determinant `1`. Trace is invariant under transpose, inverse, and
   cyclic permutation, so the type and dilatation are convention-independent.
3. **Type.** `|tr| = 20 > 2`, so `w*` is pseudo-Anosov; clause (a) is TRUE.
4. **Dilatation.** Characteristic polynomial `x^2 − 20x + 1`, discriminant
   `396 = 20^2 − 4`. Roots `10 ± 3√11`. Integer bounds
   `3316^2 = 10995856 < 11·1000^2 = 11000000 < 3317^2 = 11002489` give
   `3.316 < √11 < 3.317`, hence `λ(w*) ∈ (19.948, 19.951)` and its conjugate
   lies in `(0.049, 0.052)`. The value `1.401` differs from the large root by
   more than `17` and from the small root by more than `1.3`; exactly,
   `f(1401/1000) = −25057199/1000000 ≠ 0`.
5. **Number type.** `361 = 19^2 < 396 < 20^2 = 400`, so the discriminant is
   not a square: the polynomial is irreducible over `Q`, degree 2, not
   degree 6. Both roots are real, positive, reciprocal (`λ·λ^{−1} = 1` with
   one `> 1`, one `< 1`); there is no conjugate on the unit circle. Hence
   `λ(w*)` is a quadratic Pisot number, NOT a Salem number (Salem requires
   degree ≥ 4 with all but two reciprocal conjugates on the unit circle).
   Clauses (b)–(c) are FALSE.
6. **Calibration.** `ρ(σ1σ2^{−1}) = [[2,1],[1,1]]`, trace `3`,
   `λ = (3+√5)/2 ≈ 2.618`, the known D3 minimum — confirming the conventions.
7. **General obstruction.** Any pseudo-Anosov 3-braid has integer
   `|tr| ≥ 3`, so `λ ≥ (3+√5)/2 ≥ 2.618 > 1.401`, and every such dilatation
   is quadratic. Thus no re-reading of the word order, inverse, or conjugate
   can produce `≈ 1.401` or a degree-6 Salem value for a D3 braid. Any
   invariant D3 train-track transition matrix for `w*` has spectral radius
   equal to the dilatation `≈ 19.95` (Perron–Frobenius), so no `1.401`
   track certificate for `w*` exists either.

## 4. Conclusion

`w*` IS pseudo-Anosov, but with dilatation `10 + 3√11 ≈ 19.95` (quadratic
Pisot), not `≈ 1.401` (degree-6 Salem). The target conjunction is therefore
FALSE as stated. Per the audit plan ("a proved obstruction … is itself a
recordable exact-type determination"), this rigorous disproof is the complete
TARGET resolution: it fixes the exact type and dilatation of the named word.

## 5. Limitations and scope notes

- The refutation concerns the literal word-to-dilatation core. Inputs name no
  fibered face, log no degree-6 polynomial, and state no sharpness tolerance,
  so clause (d) (face minimality / gap sharpness) is unauditable as stated and
  is not independently evaluated.
- No higher-genus surface `M_s`, marking, or lift data is specified; the word
  alone does not determine a higher-genus monodromy, so a higher-genus
  re-reading cannot be tested against the given inputs.
- Proof uses only exact integer arithmetic plus the standard
  `B3 → SL(2,Z)` trace classification; no floating-point step is load-bearing
  (decimals shown are display only; enclosures are rational).
- 23/23 checks in `verify_target_refutation.py` pass (stdlib only).
