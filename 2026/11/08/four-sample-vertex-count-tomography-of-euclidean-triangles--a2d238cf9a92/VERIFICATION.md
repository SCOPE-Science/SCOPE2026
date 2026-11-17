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

The supporting-side extreme-point identity V_4=sum_i min(2,K_i) is correct for iid boundary-arclength sampling. Multinomial occupancy gives h2=s4, h3=4(s3-s4), h4=6e2^2; Newton identities reconstruct e2>0 and e3, Vieta recovers unordered normalized sides. The cubic discriminant and signs e2,e3 plus f(1/2)>0 exactly enforce three positive real roots with all p_i<1/2, while Cauchy yields 3/8<h4<=2/3. The two distinct 61-denominator isosceles triples have equal s3, showing three samples insufficient. Independent rational occupancy checked three profiles and their exact h_j formulas.

## originality

PASS

Published general polygon-boundary hull vertex laws already give the occupancy generating function and reconstruction from the entire infinite sample-size sequence. They do NOT assert a single fixed N=4 suffices for triangles, the exact feasible image, or that N=4 is minimal; these precise finite-shot inverse conclusions survive without claiming the basic occupancy identity as novel. Best-of-knowledge, with significant risk because the derivation is elementary from known formulas.

## value

PASS

A minimum-sample inverse problem is a natural quantitative strengthening of general polygon side-length identifiability. Exact inversion and the full attainable-law inequality distinguish the 4-sample case from a mere table of one probability; the paired three-sample counterexample proves sharpness.

The dated certificate retains the supplied scientific assessment, sources and limitations.
