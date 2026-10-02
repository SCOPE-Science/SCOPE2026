---
audit_date: 2026-10-01
status: failed
---

# Independent scientific audit

## Final claim

For Qin's explicit two-factor Fock-space Toeplitz zero-divisor pair in complex dimension at least two, both factors lie in every Schatten quasi-ideal; in particular each is trace class with norm at most \(4/9\), and their singular values satisfy the displayed stretched-exponential tail bound.

## Correctness — PASS

Qin's kernel formula identifies each Gaussian block with a scalar multiple of the adjoint of a linear Fock composition operator. Factoring the symbol's linear map into a unitary part and diag(1/4,1/4,1/2,...,1/2), the normalized monomial basis gives the exact singular values and hence the displayed S_p formula for every p>0. At p=1 the geometric products give block trace norm 1/9, so the four-term sums have norm at most 4/9. Truncation at total degree m has rank binom(n+m,n), while every higher homogeneous degree contracts by at most 2^{-(m+1)}; multiplying by the four block prefactors yields the stated 2^{-n-m-1} tail. The zero product and nonvanishing are Qin's theorem.

**Checked sources.** Assigned RESULT.md at tree 4caf665b4d00d49a6b45c255c69ba524179381bf; J. Qin, arXiv:2609.20555; Cordero--Grochenig, JFA 205 (2003)

**Residual risks.** No independent issue was found in the block-to-sum Schatten estimates; the scientific rejection is not a correctness rejection.

## Originality — FAIL

The all-Schatten and quantitative block estimates are mechanically implied by Qin's explicit kernel/composition-operator formula together with the standard monomial spectrum of a strict linear Fock composition operator. Classical localization-operator theory independently supplies broad Schatten criteria for rapidly decaying symbols. The exact number 4/9 and the displayed tail may not be printed in those sources, but they are direct corollaries of the already-given contraction data rather than a new uncovered theorem.

### Equivalent formulations

This is an equivalent operator-theoretic formulation of the load-bearing claim.

### Broader coverage

General operator-ideal theory already covers the qualitative regularity direction; the package adds only direct constants for this specific decomposition.

### Exact database or table

A table check is inapplicable because the exact values follow symbolically from the diagonal contraction.

### Claim versus prior implication

The prior/source formula and standard operator facts mechanically imply the final claim.

**Checked sources.** https://arxiv.org/abs/2609.20555; https://doi.org/10.1016/S0022-1236(03)00166-6; published stronger record dated 2026-09-19

**Residual risks.** The full Qin preprint was not retrievable through the available open-access route; the specific kernel identity was checked from the assigned package. The originality failure rests on mechanical implication, not on the postdated stronger record.

## Value — FAIL

Showing that Qin's already-explicit Gaussian composition blocks are trace class and in all Schatten ideals is a natural observation, but once the kernel formula is written down the result is a routine monomial/geometric-series deduction. The 4/9 bound and tail estimate do not create a separate motivated mathematical gap large enough to survive the required value bar.

**Residual risks.** The observation remains useful for exposition of the strength of Qin's counterexample, but usefulness alone does not make the covered corollary a new scientific finding.

## Limitations

- The result concerns Qin's explicit pair only.
- The constants are upper bounds and are not claimed optimal.
- The one-dimensional two-bounded-symbol zero-product problem is not addressed.

## Disposition

FAILED. Acceptance requires PASS on correctness, originality, and value.
