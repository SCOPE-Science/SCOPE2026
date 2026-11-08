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

The proof reduces secure domination to the number of untouched peripheral pairs. The upper-bound argument uses two distinct edges of a quotient multigraph and includes parallel edges and loops. These are mathematical deductions, not a proof obtained from finite searches.

Reproduction: run `python verify.py` with Python 3 and only its standard library. It independently evaluates secure domination by testing every legal exchange and every resulting domination condition. It verifies all secure subsets for \(2\le m\le7\), exhausts all unordered partitions for \(2\le m\le5\), and cross-checks the quotient criterion against the exchange definition for \(2\le m\le4\). The observed maximum counts are \(1,81,1174,12290\). The successful run prints `VERIFY_OK`.

Limits: exhaustive finite verification does not establish an unrestricted infinite theorem, does not resolve historical priority, and is not independent mathematical audit.
