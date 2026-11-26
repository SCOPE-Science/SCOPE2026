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

The frozen formulas are correct; in the repaired claim the auxiliary law is credited and the support-to-moment argument is made explicit. Each shifted polynomial has two simple lifted roots, and corresponding centers are equal modulo p^s but pairwise distinct modulo p^(s+1), since p is odd. The common clipped variable Y and disjoint excesses U_i give pair and triple raw moments E[Y^2]+2s E[U_i] and E[Y^3]+3s^2 E[U_i]. Summing geometric power tails gives the repaired rational formula. At s=1 it is negative for p=3 and positive for p>=5; the successive difference is positive for every admissible p,s, and kappa(3,2)=2/9. The finite-block claim for any clipping depth follows from residue periodicity, including k<=s; in the unbounded integer average a residue-tail count and the O(log N) maximum make the cubic tails vanish uniformly in the required double limit. That estimate covers mixed monomials by the cube of the maximum coordinate. The independently written modular check agrees with the exact clipped census at tested depths and the rational moments at tested scales. The proof, not these finite tests, handles all p,c,s and N tending to infinity.

## originality

PASS

PASS only for the repaired focus on the evaluated connected third cumulant, its unique ternary negative case and its scale dependence. The frozen text's claim of a distinct trivariate law not entailed by the bivariate laws fails as written: the indexed pairwise theorem forces the joint support and all its cell probabilities for these special shifts. The repair credits the indexed result and uses the trivariate census only as an auxiliary consequence. No distinct inspected statement gave the third-cumulant sign theorem. The demonstrable implication is not a claim about which same-day record came first.

## value

PASS

Even after removing independent novelty credit for the law and both pairwise and marginal calculations, the surviving result supplies a motivated higher-order dependence witness. The first possible odd-prime scale produces strictly positive covariances in all three pairs but a negative connected third cumulant, and the theorem locates exactly where that discrepancy disappears in a natural equally spaced family. It concerns a precise third-order statistic rather than evidence against independence in general.

The dated certificate retains the supplied scientific assessment, sources and limitations.
