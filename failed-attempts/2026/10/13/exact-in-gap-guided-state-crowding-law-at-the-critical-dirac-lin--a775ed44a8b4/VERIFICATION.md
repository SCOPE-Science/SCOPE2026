---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

The primary fiber result supplies exactly one signed guided eigenvalue for each k; the record takes its magnitude and counts both signs of momentum, not two eigenvalues. Write M=|m| and a=a_eta in (0,1). Above the edge aM the momentum condition is |k|<=sqrt(E^2-a^2M^2)/a, so the length divided by 2pi gives the stated N. At the edge the allowed singleton has measure zero; below it the set is empty. At E=M the boundary points have measure zero and 1-a^2=16eta^2/(eta^2+4)^2 gives 4M|eta|/(pi|eta^2-4|). For each eta_c=+/-2 and delta=eta-eta_c, factor eta^2-4=delta(eta+eta_c) to get a=|delta|/2+O(delta^2) and |eta|/|eta+eta_c|=1/2+O(|delta|). This proves the two-sided total estimate with O(1) remainder. Differentiation gives the stated density, and (aM+epsilon)^2-a^2M^2=epsilon(2aM+epsilon) proves the edge asymptotic at fixed noncritical eta; it is not uniform in coupling. At fixed positive E the factor (1-(aM/E)^2)^(-1/2) tends to one. The count excludes the bulk, eta=0, and the flat critical band; the latter endpoint is supported by the original spectral theorem. The frozen Markdown has LaTeX control-character damage, but the mathematical statement is unambiguous from its context and support. The inspected frozen script was not run: verify_density.py lines 19–29 use the same +2+h expression in both total-limit tests and test the fixed-energy limit at +2+h only. The two-sided analytic argument, not those tests, establishes both critical couplings.

## originality

FAIL

No explicit earlier statement of the normalized count was established. The exact count and all coefficients are nevertheless mechanically implied by the published exact one-branch dispersion once the specified Fourier normalization is used; no new spectral or asymptotic input is required.

## value

FAIL

The guided density per unit length is a motivated quantity, and the formulas are usable. But the proposed contribution is the elementary one-dimensional change of variables for the known scaled square-root band, with a derivative and endpoint substitutions. It supplies no independent exact fact beyond that mechanical computation under the stipulated normalization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
