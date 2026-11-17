---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification

The proof is analytic for every integer \(n\ge6\) and every real mixture weight \(0\le\theta\le1\). It factors each local median selection derivative through cyclic differences, checks the four possible pairs of selector-edge indicators, bounds each column of the resulting matrix in \(\ell^1\), and constructs finite strict-rank extremizers.

The reproducibility script `checker.py` needs Python 3 with only its standard library. It validates the explicit attaining perturbations at dimensions 6–23 for six rational weights, and enumerates all strict rank-order chambers at dimensions 6, 7, 8 to recheck the difference factorization and column-sum inequality at seven rational weights. Expected final line: `ALL_MEAN_MEDIAN_VARIATION_CHECKS_PASS`.

These computations do not enumerate infinitely many dimensions or real mixture parameters and are not presented as proof of the full theorem. The separate case split and local-to-global Lipschitz integration in `RESULT.md` supply that proof. No independent mathematical audit has been performed.
