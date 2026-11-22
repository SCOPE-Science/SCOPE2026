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

Run `python3 verify.py` with Python 3 and its standard library. The program independently enumerates transformations for \(3\le n\le6\), checks the rooted-fiber involution weights, and directly checks every pairwise composition of all the displayed rank-one, rank-two and rank-three endomorphisms for \(n=5\).

The resulting small-case counts are \(I_5=196\), \(B_5=180\), \(H_5=81\), \(571\) vertices and \(930\) edges. These checks are finite corroboration only. The proof of the full result is mathematical and is given in RESULT.md. No independent audit or external certification has been performed.
