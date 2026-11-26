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

Expanding (D-A)^2 gives d_v(d_v+1) on the diagonal, c_uv-d_u-d_v on an edge, and c_uv on a nonedge. Intersecting the associated nonnegative conditions gives the exact union-complement with closed edge cutoff. The diagonal discriminant is d(d-2)/3: degrees zero and one do not obstruct; degree two gives the double zero (1-h)^2. For d>=3 the first root decreases with d, and h_-(Delta)<3/(Delta+1)<3/Delta<=h_E. A direct stable negative witness on every branching graph is h=3/(Delta+1): the maximum-degree diagonal is -(Delta-2)/(2(Delta+1)), and h lambda_max<=6Delta/(Delta+1)<6. The norm claim follows since the multiplier P_2(1-y/3) has absolute value at most one exactly for y in [0,6] when y>=0. For stars lambda_max=m+1 and the spoke cutoff is 6/(m+1); only the hub may be negative, and h_+(m)<6/(m+1). The four-vertex witness, two smaller positive stars and the 1/sqrt(3) fraction follow. No graph of at most three vertices has a negative diagonal or reentry after an edge first fails. Row sums remain one, including isolated vertices. The independent python /workspace/reproduce_frozen.py checks 64 labeled four-vertex graphs at six rational steps and the exact maximum-degree witness formula. The frozen checker was inspected, not executed; its graph comparisons and computed star signs use rational arithmetic, but its star reference root comparisons at sampled steps contain floating square roots. These finite checks are supplemental to the exact proof and not evidence of continuum coverage by enumeration.

## originality

PASS

Best of current knowledge, the supported distinct result is the exact unmodified RKL1 degree-only first endpoint barrier with stable negativity on every branching simple graph, and the smallest-star reentry and full star windows. The polynomial, graph entry algebra, and regular-graph specialization are credited, not treated as new.

## value

PASS

A sharp maximum-degree rule usable without triangle or spectral data, a guaranteed spectral-versus-positivity gap for every branching graph, and explicit reentry at the smallest possible number of vertices answer natural endpoint maximum-principle questions for an existing integrator. The importance is in those exact obstructions and thresholds, not in expanding L² alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
