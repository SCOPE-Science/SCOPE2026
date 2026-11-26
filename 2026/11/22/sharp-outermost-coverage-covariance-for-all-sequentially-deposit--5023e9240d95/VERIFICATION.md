---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

A site is first covered at the earliest first-attempt time among its k incident starts, because that attempt must be accepted. A start can be accepted only once, and at its first attempt, exactly when it attains such a minimum for some site. This verifies the local-clock representation on the infinite lattice and the clock window [x-2k+2,x+k-1]. Sets separated by at least 3k-2 use disjoint independent coordinates. At 3k-3 the sole shared clock is U_{k-1}, fixed by reflection, so the covariance is the variance of the common conditional mean. Only start 0 on the left can see the shared clock. Given U_0=s≤t, switching the shared clock from earlier than s to later changes acceptance precisely when starts 1,…,k-2 are all later and start -1 is earlier: the latter covers all sites before k-1, whereas if it is later, site k-2 already certifies acceptance. Integration against e^{-s} yields g_k(min(u,t)) plus a constant. The derivative g'_k=e^{-(k-1)s}(1-e^{-s}) gives strict positivity even for arbitrarily small positive times. Multiplying g'_k and 2g_k g'_k by the exponential survival factor and integrating reproduces the two finite-time moments. Independent symbolic integration in the uniform variable e^{-U} (python /workspace/independent_checks.py 5) verifies the jammed simplification and k=2,3,4 values; the leading k^{-5} term follows from degrees. The conclusion on decay is about covariance, not a computed Pearson correlation coefficient. No uploaded verifier was executed.

## originality

PASS

The supported distinct claim is the all-k≥3 full-multiplicity last-lag covariance, including its finite-time strict positivity and jammed asymptotic. First-arrival locality, dimer results, trimer-indicator results and one-site laws are credited separately. The access limits below do not establish priority or absence.

## value

PASS

Locating the last possible dependence by clock windows is cheap; showing that this boundary is attained for every positive time and quantifying how weak that farthest coupling becomes is more informative. The explicit all-length covariance and fifth-power saturation scale distinguish an expanding interaction range from the fast falloff of its edge strength, and give an exact benchmark for two-point calculations beyond available one-site laws.

The dated certificate retains the supplied scientific assessment, sources and limitations.
