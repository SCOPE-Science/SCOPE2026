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

Exact Bernstein beta moments give the shifted Legendre modes of degrees 0, 1, 2 with eigenvalues 1, 1/2, 1/10; these exhaust the degree-two range. With u=2x−1 and v=2y−1 the power kernel is 1+3·2^(-t)uv+(5/4)10^(-t)(3u²−1)(3v²−1). A negative value anywhere, including the boundary, gives negative output on a positive-measure interval for a nonnegative input supported in a nearby interval, so continuity really makes the pointwise minimum decisive. At fixed w=|uv|, opposite signs and u²+v²≤1+w² give the exact lower envelope 1−3·2^(-t)w+(5/2)10^(-t)(3w²−1), attained at u=1,v=−w. Its vertex is w=5^(t−1), yielding the first formula for t≤1 and the endpoint formula for t≥1. The first branch is strictly concave, negative at 0, zero at 1 with negative derivative there, so it has precisely one internal root. The second is zero at 1, has negative derivative there, and its derivative changes sign once from negative to positive; its limit is 1, yielding exactly one later root. Degree one has eigenvalues 1 and 1/3, so its kernel minimum is 1−3^(1−t), with no reentry. Zero eigenvalues do not contribute at any t>0.

## originality

PASS

The positive original kernel, the low-degree eigensystem and generic spectral calculus are existing background. On the comparisons inspected, the supported distinct claim is the exact real-time order-positivity set for this unweighted quadratic operator, including the loss just after the positive Markov iterate at t=1 and subsequent recovery. No historical priority is certified.

## value

PASS

The natural quadratic Markov averaging kernel gives a sharp counterexample to monotone persistence of order positivity along its canonical real spectral powers after t=1. Exact witnesses and thresholds locate both failure and recovery, and the degree-one comparison shows the low-degree boundary within the family. This distinction between order positivity and positive semidefiniteness is directly relevant to positive interpolation of a Markov iterate.

The dated certificate retains the supplied scientific assessment, sources and limitations.
