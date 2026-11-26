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

In the repaired proof, on each r=±1 input class the normalized expansion modulo 3 is t−(a/3)r with derivative 1 modulo 3, so Hensel gives each whole r+9 Z_3 cylinder. For a=3b the zero-input branch divided by 27 is t^3−bt with derivative −b modulo 3, taking precisely one residue when b=1 modulo 3 and every residue when b=−1. For a=9c direct rescaling gives 27 V_c. Iteration stops at v_3=0 or 1 as stated in the repair; for a=0 the residual nested sets have intersection {0}. For a unit ≡−1 the three normalized derivatives are units and give three disjoint cylinders mod 9. A unit ≡1 is a square and reduces by unit rescaling to F_1, whose positive class is −2+27t²(t+1); t=±1 mod 3 maps onto both attained classes of t²(t+1), giving the two mod-81 cylinders on this branch, their negatives on the other branch, and the distinct 9 Z_3 branch. Their reductions indeed give counts 3,3,5 and then 13·3^(k−4). Counting disjoint reductions and solving δ(9c)=2/9+δ(c)/27 gives the stated phase law with fixed point 3/13. The repaired decreasing-cylinder argument establishes the limiting density. Independent enumeration checked 72 complete finite image sets, at a=0,3,−3,9,18,27,54,81 and k=1…9, not all parameters or depths; the repaired stopping rule is in particular consistent with the checked odd valuations.

## originality

PASS

Credit is for the joint exact nonunit image classification, in particular the split at valuation one and its recursion across all nonunit parameters. The unit a=1 count is not new. A plausible earlier article directly treats Dickson polynomials over Galois rings; its coverage is unresolved, not negative evidence. No verified source here states this nonunit classification or supplies a stronger theorem from which it follows mechanically.

## value

PASS

The theorem completely decides local solvability for a natural low-degree Dickson family at its wild prime, not merely sizes at selected precisions. It distinguishes the two valuation-one unit parts and transmits the resulting measures to arbitrarily large valuations, supplying exact phase limits and congruence counts that the unit case and general upper bounds do not give. These nonunit statements survive the correction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
