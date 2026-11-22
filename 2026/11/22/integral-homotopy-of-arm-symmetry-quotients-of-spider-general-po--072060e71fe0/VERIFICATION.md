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

# Verification instructions and limits

Run `python3 verify.py` with an ordinary Python 3 interpreter and no third-party dependencies. The expected output is in `verification_output.txt`. The program checks all vertex subsets directly against graph-geodesic collinearity for \(r\in\{3,4\}\), \(1\le L\le5\), then independently constructs the quotient of the barycentric subdivision by all arm permutations. Since simplex-flag vertices have distinct face cardinalities, stabilizers fix each flag pointwise, making its orbit-chain complex a valid integral cellular complex of the genuine quotient. The script verifies consecutive signed boundaries compose to zero over integers and compares exact ranks over \(2,3,5,7\) with the predicted full Betti vectors.

An ordinary finite enumeration does not prove the unrestricted homotopy theorem, exclude torsion at other primes or guarantee bibliographic priority. The unrestricted proof is in `RESULT.md`: a topological strong deformation retraction of the quotient join to a simplex skeleton, an acyclic matching on that skeleton, and an exact count of the remaining attached orbit edges. No separate independent review has occurred.
