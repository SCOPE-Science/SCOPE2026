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

A symmetric probability rule on at most three points has outer radius d and common outer weight b, with possible centre mass 1−2b. The centred second moment forces b=1/(24d²), and the odd moments vanish. For pointwise Jordan BV, Jordan decomposition followed by layer cake on the increasing parts proves the exact error norm is the maximum over both initial-segment discrepancies, including at atoms. Open and closed upper-step witnesses give the reverse bound; at the endpoints use the endpoint spike or its complement as needed. The candidate discrepancies are 1/2−d, |b+d−1/2|, and 1/2−b. The first is dominated because 24d²(1−2d)≤8/9. The two remaining branches cross once at 12d²(1−d)=1. The crossing is below 2/5, with the first branch strictly decreasing up to the crossing and the second strictly increasing thereafter. This proves uniqueness including the two-node and endpoint cases. The witnesses give errors +d/2 and −d/2, respectively. Substitution gives 2/9 for three-point Gauss and 1/3 for Simpson; independent scalar bisection yielded d=0.361175862232188 and an 18.7354% reduction from Gauss. The packaged finite grid and random tests were inspected, not used as the universal proof.

## originality

PASS

Credit the known rule family and discrepancy norm. The supported distinct claim is the exact unique constrained at-most-three-node minimizer of this norm, including sharpness and benchmarks. The inspected broader-node result and the moving-node 3-convex result do not furnish that minimizer. This is not a priority certification.

## value

PASS

This is a sharp complete within-class design rather than a pointwise bound for an arbitrary fixed formula. It quantifies the robustness tradeoff between Jordan-BV inputs and higher polynomial exactness, with attained worst cases and a material improvement over standard rules. It asserts neither optimality without symmetry nor optimality with larger support.

The dated certificate retains the supplied scientific assessment, sources and limitations.
