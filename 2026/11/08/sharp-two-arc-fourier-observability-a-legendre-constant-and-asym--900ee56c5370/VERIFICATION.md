---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

For the repaired claim, a unit trial polynomial with m-fold zeros at both distinct centers bounds the cost by O(α^{2m+1}). On each arc the rescaled Taylor polynomial of any unit minimizer has bounded coefficients, because its L² norm is bounded and the Taylor remainder is uniformly O(α). Thus the first m unscaled jets vanish in the limit, selecting the two-root polynomial with leading angular Taylor modulus (2 sin θ)^m/√S_m. The monic Legendre norm is 2·4^m/[(2m+1)B_m²]; prescribing the lower jets independently with a bounded Hermite right inverse attains that cost on both arcs, including the Haar factor 1/π. The right inverse is bounded on compact interior angle sets and the lower bound works along convergent interior angle sequences, giving compact-uniform convergence. Parseval expresses S_m as the even-power integral of 2 cos t−2c and its positive even coefficients imply S_m(c)>S_m(0)=B_m for c≠0. On a trial arc one root distance is at most α, the other at most 2 sin θ+α. The resulting uniform bound excludes endpoint limits of maximizing placements, proving the optimized limit and convergence of all maximizers. At antipodal centers the rank-two leading Gram term has evaluation-vector squared norms 2m+1 and cross inner product of modulus 1; its top eigenvalue gives the stated condition-number coefficient. The three-mode formula is correct as a benchmark: the Gram eigenvalue a+c/2−sqrt(c²/4+2b²) is strictly below a−B when cos θ≠0, since c/2+B>0 and 2b²>B²+Bc with B=sin(2α)/π; at the antipodal point a−B is the minimum. The frozen high-precision script was inspected, not rerun; its checks are corroborative only. The continuous two-arc result fixes m before α tends to zero.

## originality

PASS

The original finding included the exact all-width three-mode design as a contribution, but that statement and value are exactly covered by the 2026-11-01 record 1c5e863c7cba. The distinct same-date theorem e95b9bae48f1 also already gives equivalent coverage of the fixed antipodal coefficient, without a priority inference. The repaired RESULT and SLOGAN remove the three-mode design as a contribution, credit both precise overlaps and restrict the claim to the arbitrary-angle coefficient and the sharp all-degree moving-placement optimization. That remainder survives all inspected comparisons; this is not an originality pass for the old three-mode assertion.

## value

PASS

At fixed observation length the angle can change the leading least observable energy by a macroscopic factor, and collapsing centers suppress it even on the rescaled scale. The solved placement problem supplies an explicit worst-case reconstruction penalty and proves asymptotic optimizer convergence at every fixed degree, beyond the known exact degree-one special case and the known periodic-placement value. Finite-width optimality for larger m and optimal full condition number are not claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
