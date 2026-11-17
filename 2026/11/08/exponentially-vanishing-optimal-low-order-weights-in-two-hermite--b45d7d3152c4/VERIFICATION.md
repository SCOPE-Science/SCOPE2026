---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

For fixed m<n without common Laguerre zeros, the high-radius tails P=e^-t L_n^2, Q=e^-t L_m^2 are both decreasing. The compact minimum near simple n-th Laguerre roots has G(w)=c w+O(w^2), c>0, strictly increasing for small w; the outer endpoint H_T=b_n-(b_n-a_m)w strictly decreases. Their unique crossing is the global optimum because H decreases beyond it. Thus w=b_n/c+O(b_n^2) and floor b_n-b_n^2/c+o(b_n^2). For h1,h2 independently evaluated c_inner=0.0955091130 and c_outer=0.1917684953. The Laguerre recurrence excludes shared adjacent zeros; the argument covers all fixed pairs satisfying the hypothesis.

## originality

PASS

The full October 25 three-Hermite result is a different, strictly larger three-channel optimization and does not solve the restricted h_m/h_n pair. The published all-plane Gaussian-relative h1/h2 theorem divides out e^-t and has a constant weight; its conclusion cannot imply the unweighted expanding-disk boundary/root balance and exponentially shrinking weight. Primary multi-window STFT text could not be inspected beyond abstracts; residual historical overlap noted.

## value

PASS

Optimal allocation of two fixed Hermite ambiguity measurements under a fixed exposure budget is a motivated and quantitatively sharp stability-design invariant. The unique weight, nontrivial limiting zero circle, and second-order deficit add more than a routine Laguerre identity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
