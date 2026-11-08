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

# Verification record

The standalone Python 3 checker `verify.py` enumerates every approval matrix for \((m,k,n)=(3,2,1),(3,2,2),(3,2,3),(3,2,4),(4,2,2),(4,2,3),(4,2,4),(4,3,3)\), totaling 78,664 profiles. For each profile it compares literal all-cohesive-group SJR and SSJR definitions to candidate-supporter reductions, verifies the exact set-cardinality prediction when all candidates have private supporters, and computes exact rational binomial proxy probabilities at \(q=1/2\). All assertions passed and the terminal marker was `ALL_EXHAUSTIVE_CHECKS_PASS`.

The infinite assertions instead follow from the proof: deterministic private-supporter reduction, an elementary union bound, independence of popularity counts, and a central limit theorem with fixed \(m,k\). Neither finite enumeration nor numerical tests are asserted to certify the infinite claims. No independent audit has been performed.
