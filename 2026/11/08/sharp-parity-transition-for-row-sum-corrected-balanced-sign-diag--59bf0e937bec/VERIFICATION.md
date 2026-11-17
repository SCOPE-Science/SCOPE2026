---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For coordinate-exchangeable signs, pair correlation ρ=(E S²−n)/(n(n−1)) is bounded below by −1/(n−1) in even n and −1/n in odd n, with equality for the corresponding minimum-imbalance sign layers. Directly, E[z_i(Az)_i]=(1−ρ)A_ii+ρ(A1)_i gives the uniquely universally unbiased affine row-sum correction. For row i, variance of the corrected single probe equals (sum_{j≠i}A_ij²+ρ(sum_{j≠i}A_ij)^2)/(1−ρ). Independent probes divide variance by m, yielding total risk (||B||_F²+ρ||B1||²)/(m(1−ρ)). The derivative with respect to ρ is (||B||_F²+||B1||²)/(m(1−ρ)^2)>0 for nondiagonal A, hence minimum correlation is globally optimal in stated class. Cauchy–Schwarz gives even zero-risk rows precisely row-constant off diagonal; odd risk zero only B=0. Comparing with m+1 iid signs gives strict universal advantage for even n≥4 m≥n, odd n≥3 m≥n+1 and n=2 any m; B1=0 witnesses make boundaries exact. Independently enumerated all optimal fixed-count sign vectors for n=2..7 with rational matrix entries, checking unbiasedness and row variance; the dimension-general proof is algebraic.

## originality

PASS

Classical Hutchinson and Diag++ work studies iid-coordinate signs, Gaussian vectors and low-rank corrections. The inspected Dharangutte–Musco paper explicitly defines independent iid-entry Rademacher probes and derives its iid baseline; this does not imply the minimum-correlation fixed-Hamming-weight within-probe design with one deterministic row-sum matvec, parity-dependent zero-error subspaces and exact cost thresholds. XDiag has a leave-one-out cross-probe construction, not this universal affine row correction. Novelty qualified for uninspected finite-population/control-variate specialist literature.

## value

PASS

The diagonal of a matrix accessed only by matrix–vector products is a natural computational invariant. Exact dimension/parity-sensitive risk and zero-error subspaces supply actionable sampling and budget decisions beyond generic concentration bounds. A deterministic row-sum query plus fixed-sum signs can exactly recover a dense row-constant-off-diagonal matrix for even dimensions; matched-budget crossover is sharp. Its restricted-class optimality is clear and mathematically motivated, not a claim of arbitrary estimator minimax.

The dated certificate retains the supplied scientific assessment, sources and limitations.
