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

The general scheme isomorphism follows from the derivative-zero property of the marked Gauss map, the unique scaling of projectively fixed points, and the simple-root trace polynomial. These are mathematical arguments valid for all \(n\ge3\).

The standalone script `verify.py` can be run with standard Python 3 and no external dependencies. It verifies polynomial identities for \(3\le n\le10\), arithmetic over the degree-five extension, and all fixed points and Frobenius orbits for \(n=5\). The exact recorded output is in `verification_output.txt`. Finite test ranges are corroboration and do not prove the general case. Literature priority is qualified by the precise comparisons in `REVIEW.md` and `AUDIT.json`.
