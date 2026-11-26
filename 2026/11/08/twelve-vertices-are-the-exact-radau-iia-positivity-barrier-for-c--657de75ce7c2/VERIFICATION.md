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

The endpoint scalar filter has no poles for nonnegative arguments. The Laplacian acts by 0 on the constants, by q=N−p on mean-zero vectors supported in a part of size p, and by N on the part-constant centered space. The projectors give diagonals 1/N+(1−1/p)R(qh)+(1/p−1/N)R(Nh). Writing f(z)=(1−R(z))/z=(z+6)/(z²+4z+6), the between-part off-diagonal equals h f(Nh)>0 and the within-part off-diagonal equals (qh/p)[f(qh)−f(Nh)]>0 for h>0, since f′ is strictly negative on nonnegative arguments. The global scalar minimum is (5−3√3)/2 at z=3+3√3. The resulting lower bound on a diagonal has numerator at least 26−15√3>0 through order 11. For h=8/q and t=p/N, direct substitution uses R(8)=−5/51 and R(8/(1−t))=−(1−t)(5+3t)/(51−22t+3t²). The negative of the resulting diagonal has positive denominator and numerator N(255−110t+15t²)−2848+1056t. For N≥12 this numerator is bounded below by 4(45t²−66t+53)>0, since the quadratic has negative discriminant. The bound holds for every part, with no inference of a common negative timestep. At zero the endpoint is the identity, so the diagonals stay positive for small positive steps; at large steps the endpoint tends to J/N, so strict positivity returns. The uniform algebra rather than the supplied finite tests establishes the theorem.

## originality

PASS

Earlier balanced multipartite work already proves the same order cutoff, even with common positive edge weights, and classifies reentry more finely in its domain. This is substantial prior coverage, alongside overlapping star and K₂,q statements. The supported distinct contribution is the sharp result for arbitrary part profiles and a uniform explicit witness for each individual part at all orders N≥12. The inspected general time-discretization criteria do not imply that extension.

## value

PASS

An all-step positivity bound for this endpoint update controls whether nonnegative data can acquire negative entries. The exact graph-order barrier for every part profile is stronger than a positive range from an unrestricted method criterion or isolated balanced examples. The simple explicit witness and all-time off-diagonal sign give usable information even though graph-specific positivity windows are not all classified.

The dated certificate retains the supplied scientific assessment, sources and limitations.
