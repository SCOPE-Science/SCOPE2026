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

The coefficient identities and bounds have a complete analytic proof in `RESULT.md`, conditional only on the precisely identified published Godbersen inequality and type-B Narayana Hankel-total positivity theorem. The provided standard-library Python script `check.py` reproduces 1,048,469 integer coefficient comparisons across all ordered decompositions of dimensions two through sixteen, plus three planar model profiles.

Independent exact polygon geometry gave area \(2\), difference-body area \(10\), and reflected mixed polynomial \(1+3t+t^2\) for the trapezoid with vertices \((0,0),(3,0),(1,1),(0,1)\). This checks a nonsimplex factor case without relying on a floating-point result. The finite checks support the algebra; they do not certify all dimensions, and no independent mathematical audit has been conducted.
