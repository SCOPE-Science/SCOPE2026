---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Conditioning that t specified labels are origins forces all n images into the other n−t labels and leaves a uniform restricted map with exactly the same cycles. Summing over ordered labels proves deletion for every h and t≤n−1. Given the k roots and their cyclic permutation, the attached directed forest is uniform among k n^(n−k−1) forests. Deleting t prescribed nonroot leaves and allowing their parents to be any remaining label gives ratio (1−t/n)^(n−k−1), including the empty forest when every nonroot is deleted. This yields the factorial moments and PGF, with L_n=0 for k=n. The displayed adjacent decrement is positive including k=n−1, where it is one. Pairing two independent copies of the full-support K_n yields the covariance sign for increasing g; taking t=1 in deletion yields the exact covariance identity. The product law for K_n gives Rayleigh convergence and Gaussian tail control of all fixed scaled moments. Expanding log(1−1/n) uniformly for k≤C√n gives m_n(k)=n/e+1/(2e)−k²/(2en)+o(1), and subtracting n(1−1/n)^n yields the stated shift. The quadratic bound on the centered mean controls the covariance integrand by a constant times 1+(K_n/√n)^3. For its endpoint k=n, use n(1−1/n)^n≤n/e≤(n−1)/2 for n≥4, and direct evaluation for n=2,3, rather than bounding the last decrement by (n−1)/n. Fourth-moment control gives uniform integrability, and E X³=3 E X for the Rayleigh limit gives the coefficient −√(π/2)/(2e). Empty-box indicator covariances give Var(L_n)/n→e^−1−2e^−2 while Rayleigh moments give Var(K_n)/n→2−π/2. The frozen verification notes and finite-check script were inspected, not executed.

## originality

FAIL

Two preceding Resultary records give exact coverage. Record e4cf3e3e51f2 proves a deletion identity for all functions of the full cycle-count vector, which specializes to arbitrary functions of cyclic-core size. Record 007c2a04bfe9 gives the same full conditional origin law, strict decrease of the mean, identical covariance coefficient, and stronger correlation asymptotic. The finite PGF, monotone-function sign and Rayleigh-scale mean shift follow routinely from these verified formulas; there is no distinct substantive remainder.

## value

FAIL

The conditional law and sharp covariance are natural statistics, but their exact content and the general pruning mechanism are already covered. The remaining re-expression as a PGF, monotone-test covariance sign and Taylor expansion of the known mean do not establish a separately motivated unknown fact or new technique.

The dated certificate retains the supplied scientific assessment, sources and limitations.
