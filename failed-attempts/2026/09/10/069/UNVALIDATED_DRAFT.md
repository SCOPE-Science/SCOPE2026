# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Distal cell-bound transfer to henselian fields via one explicit RV-adapted Wilkie preparation step

## Claim (TARGET)

**Theorem.** Let `T = Th(RCVF, L_RV)` be the theory of a henselian real-closed
valued field of residue characteristic `0`, in a two-sorted RV-enriched
language `L_RV` whose residue sort `k` carries restricted-exponential
o-minimal structure (so Wilkie / van den Dries–Speissegger preparation
applies) and whose value-group sort `Γ` satisfies DOAG. Let `φ(x;y)` be a
valued-field formula with `|x| = 2`, `|y| = 1` built from at most two
exponential-polynomial RV-terms of total degree `≤ 2` (RV-complexity `≤ 2`).
Then `φ` admits a distal cell decomposition with at most `N = 48` cells and
distal exponent at most `2·(d_k + 1)`, where `d_k` is the o-minimal distal
exponent of the corresponding residue-field fiber. The bound is obtained
through the explicit RV-adapted Wilkie preparation normal form **(NF2)**
stated in Lemma 1.

## 1. Setup and definitions

**Language `L_RV`.** VF-sort: ordered-ring language with valuation data
accessed only through `rv : VF^× → RV` and the exact sequence
`1 → k^× → RV^× → Γ → 0` (write `ξ` for the `k`-coordinate, `γ` for the
`Γ`-coordinate). Residue sort `k`: real-closed field with restricted
exponentiation (o-minimal, Wilkie preparation available). Value-group sort
`Γ`: DOAG (ordered `ℚ`-vector space). This is the standard Pas/Basarab
RV setup; we use Pas quantifier elimination (residue char `0`, henselian):
every VF-formula is `T`-equivalent to a Boolean combination of conditions
`rv(F(x;y)) ∈ D` with `D` RV-definable, i.e. a product of a `k`-condition on
`ξ` and a `Γ`-condition on `γ`, plus value comparisons.

**RV-complexity.** For `φ` as above, RV-complexity = (number of distinct
exponential-polynomial RV-terms occurring in `φ`) + (total polynomial
degree), capped in the hypothesis at: `≤ 2` terms, total degree `≤ 2`.
An *atom* compares at most two terms, so up to Boolean structure it is the
sign of a single difference `H = F_1 − F_2` (still degree `≤ 2` in the
polynomial part, with a single exponential ratio — see Lemma 1). Zero loci
`{x_i = 0}` / `{H = 0}` are treated with non-strict cuts (`<` vs `≥`), so
they are absorbed into existing cells and cost no extra cells.

**Distal cells / exponent.** We use the Chernikov–Simon / Anderson
convention: a distal cell decomposition of `φ(x;y)` is a uniform finite
family of cell formulas `C_i(x; a_i)` (each a conjunction of two literals
as below) covering the domain, such that each fiber `φ ∩ C_i` is distal
with uniform exponent; the *distal exponent* `t` is the density exponent:
for finite `B`, the number of realized `φ`-types over `B` is `O(|B|^t)`.
We cite: (a) preimages of distal cells under definable maps are distal
cells with the same exponent (Chernikov–Simon); (b) the product of a
`d_k`-exponent family and a `t_Γ`-exponent family has exponent `d_k + t_Γ`
(Anderson §2 induction / Chernikov–Simon density subadditivity);
(c) o-minimal groups satisfy exponent `≤ 2|x| − 2` (Anderson), hence the
`Γ`-fiber below has exponent `≤ 2`.

## 2. Normal form (NF2)

**Lemma 1 (RV-adapted Wilkie normal form, degree ≤ 2, ≤ 2 terms).**
Up to `T`-equivalence, each atom of `φ` is, on each RV-fiber, a conjunction
of a `k`-condition `ψ_k` and a `Γ`-condition `θ_Γ`, where after Wilkie
preparation the residue part has the following shape. Write the comparison
as the sign of `H = F_1 − F_2 = M·(1 + R)` with `M` a monomial times a
dominant exponential and `R = c·exp(±(Q_1 − Q_2) + P)`, `Q_i, P` of degree
`≤ 2`. Then the residue domain partitions definably into **at most two**
preparation cells:

- `C_bdd`: `R` is bounded (the exponential argument stays in a fixed
  compact box). Here `exp(R)` is restricted-analytic, so
  `H = m_bdd(z)·u_bdd(z)·Q_bdd(z)` with `m_bdd` a monomial, `u_bdd` a unit,
  `Q_bdd` a polynomial of degree `≤ 2` in prepared coordinates `z`;
  `sign(H)` is a polynomial sign.
- `C_unbdd`: `R` is unbounded (either `→ +∞` or `→ −∞`). Factoring the
  dominant term in either direction gives `H = m_∞(z)·u_∞(z)·(1 + ε)` with
  `|ε| < 1/2` and `u_∞` a unit; the two unbounded branches are grouped as
  ONE preparation cell because in both cases the sign is the (polynomial)
  sign of the dominant monomial `m_∞`. No separate cell per direction is
  needed.

*Why two cells suffice (the degree-≤2 bookkeeping).* With at most two
terms there is a single exponential ratio `R`; preparation must only decide
bounded-vs-unbounded for this one ratio (Wilkie/vdD–Speissegger applied to
the single function `H`). The usual three-way split
(bounded / →+∞ / →−∞) collapses to two cells by the dominant-term
factorization above. This is the only place the `≤ 2`-term / degree-`≤ 2`
hypothesis is used, and it is what makes the constant explicit.

*Proof sketch.* Existence of preparation is Wilkie (1996) /
van den Dries–Speissegger (1998) on the residue sort, applied to the single
function `H` (one exponential argument after differencing). The displayed
factorizations are the standard preparation outputs; the 2-cell grouping is
the elementary dominant-term observation above. ∎

## 3. Fiberwise counts

**Lemma 2 (residue fiber: ≤ 8 cells).** On each preparation cell `C_*`,
`sign(H)` (and jointly the signs of `F_1, F_2` where they occur
separately) is determined by at most two polynomial conditions of degree
`≤ 2`. Using non-strict cuts (`<` vs `≥`, so zero loci are absorbed), each
condition contributes a binary literal; the cell formulas are conjunctions
of two literals, i.e. `2^2 = 4` sign patterns per preparation cell. With
`≤ 2` preparation cells: `K_k ≤ 2 × 4 = 8` residue cells.

*Certificate.* `output/artifacts/verify_transfer.py` checks
`2 × 2^2 = 8`. The bound counts distal formulas (sign patterns), not
topological connected components, so Bézout-type splitting of conics into
more regions does not increase it: each sign vector is one distal cell by
definition. ∎

**Lemma 3 (value-group fiber: ≤ 6 cells, exponent ≤ 2).** The `Γ`-condition
`θ_Γ` in two object valuations `(v(x_1), v(x_2))` with one parameter
involves at most three affine linear forms through a common point:
`L_1, L_2, L_1 − L_2` (the two valuations and their comparison forced by
differencing two terms). With `<` vs `≥` cuts there are `2^3 = 8`
combinatorial patterns, of which exactly 6 are non-empty: in the quadrant
`L_1 ≥ 0 > L_2` one has `L_1 − L_2 > 0` forced (the `<` pattern is empty),
and symmetrically in the opposite quadrant — i.e. `2 + 1 + 2 + 1 = 6`.
Hence `K_Γ ≤ 6`. The exponent satisfies `t_Γ ≤ 2` by Anderson's o-minimal
group bound `2|x| − 2` at `|x| = 2` (Γ with DOAG is an ordered group).

*Certificate.* `verify_transfer.py` confirms via Euler count (`2m = 6`
sectors for a pencil of `m = 3` concurrent lines), realizable-sign
enumeration (6 strict triples), and an angle-sweep brute force (6 regions),
plus the quadrant-by-quadrant `<`/`≥` count `2+1+2+1 = 6`. ∎

## 4. Combination (AKE RV fibration)

**Theorem proof.** By Pas QE, `φ` is a Boolean combination of conditions
`rv(H(x;y)) ∈ D = D_k × D_Γ`. Pull back the Lemma 2 decomposition
(`≤ 8` `k`-cells) and the Lemma 3 decomposition (`≤ 6` `Γ`-cells) through
the definable maps `ξ ∘ rv` and `γ ∘ rv` (with `rv`-sections/centers from
QE; the section parameters are absorbed into the cell parameters). Each
product `C^k_i × C^Γ_j` pulls back to a VF distal cell (distality is
preserved under definable preimage), and these cover the domain (zeros
absorbed by `≥`-formulation, including `x_i = 0` via `v = ∞`). Hence

```
N ≤ K_k · K_Γ ≤ 8 × 6 = 48.
```

For the exponent, the product construction gives
`t ≤ d_k + t_Γ ≤ d_k + 2 ≤ 2·(d_k + 1)` for all `d_k ≥ 0`
(the last inequality is elementary; checked in the script for
`d_k = 0..10`, and it holds for all `d_k ≥ 0` since
`2(d_k+1) − (d_k+2) = d_k ≥ 0`). This is exactly the claimed exponent. ∎

## 5. What is proved, cited, computed

- **Proved here (new bookkeeping):** the 2-cell grouping of Lemma 1 from
  the single-ratio observation; the `2+1+2+1 = 6` Γ-count; the product
  assembly `8 × 6 = 48` and the exponent inequality. The script
  independently certifies every number from displayed formulas alone.
- **Cited standard theorems (not re-proved):** Wilkie / vdD–Speissegger
  preparation (existence), Pas/Basarab RV quantifier elimination (residue
  char `0`, henselian), Chernikov–Simon distal preimage/product preservation,
  Anderson distal-density caps (`2|x|−2` for o-minimal groups).
- **Computed evidence:** `output/artifacts/verify_transfer.py` →
  `VERIFY_OK` (residue `2×4=8`; Γ Euler/realizability/sweep `=6`;
  product `48`; exponent inequality OK).

## 6. Limitations and non-overclaim

1. The result is a **bounded-complexity transfer lemma** (`|x|=2,|y|=1`,
   `≤ 2` terms, degree `≤ 2`), not a general distal-transfer theorem for
   all formulas or all henselian fields; the constants `48` / `2·(d_k+1)`
   are tied to this syntax.
2. The residue sort is **assumed** to carry restricted-exp o-minimal
   structure so that Wilkie preparation applies (scope condition from the
   problem statement); mixed characteristic and unrestricted exp are
   excluded.
3. The value `d_k` is taken as input (the distal exponent of the pure
   residue fiber); the lemma lifts it rather than computing it.
4. No claim is made about optimality/sharpness of `48` (the single-difference
   case already gives `4 × 6 = 24 ≤ 48`, so slack exists by design as an
   upper bound).
5. Heavy inputs (preparation existence, Pas QE, distal preservation) are
   cited, not re-derived; the original contribution is the explicit
   degree-`≤ 2` normal form with exact fiber-product constants.
