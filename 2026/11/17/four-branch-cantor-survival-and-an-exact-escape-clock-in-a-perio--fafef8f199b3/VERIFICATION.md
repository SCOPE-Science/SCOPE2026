---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

PASS: Direct substitution gives the four affine two-step branches of slope Λ=ab and translations b+1,b−1,1−b,−b−1. The strict inequalities are exactly T<1 and T<b−1 with T=(b+1)/(Λ−1); these put all four compact inverse images strictly in the correct switching intervals, including endpoint behavior. Hence K=intersection_n F^{−n}(I) is a strongly separated four-similarity attractor, full one-sided four-shift, dim_H K=log4/logΛ; S_n consists of 4^n disjoint intervals of length 2T Λ^{−n}, giving uniform survival (4/Λ)^n. F is linearly repelling outside ±T and every switching-point image exits, so there are no additional bounded forward orbits. Separate rational arithmetic verified 3 admissible (a,b) pairs and all inverse cylinders through depth four; the general statements follow from the branch proof, not finite tests.

## originality

PASS

PASS (best of knowledge): The identical 2023 neuron study gives exterior escape and low-expansion attraction, but its hypotheses exclude the strictly expanding cone; the four-full-branch Cantor set and geometric return-time law are not stated or implied. General IFS dimension theory is known; originality lies in its exact application and complete survivor proof for this recurrence.

## value

PASS

PASS: The exact four-branch repeller and return-time law resolve a genuine high-expansion complementary regime of an established periodically switched neuron model, distinguishing a null Cantor bounded set from the known attracting interval and giving a precise escape observable. Model-specific branch feasibility and exhaustive orbit characterization, rather than generic Moran arithmetic alone, are essential.

The dated certificate retains the supplied scientific assessment, sources and limitations.
