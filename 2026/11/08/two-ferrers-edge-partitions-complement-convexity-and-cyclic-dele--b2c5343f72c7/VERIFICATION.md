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

The mathematical proof is given in `RESULT.md`. Run `python3 artifacts/verify.py` from this package root.

The program checks the theorem's equivalence for all antichain-row matrices on \(3\times3\), \(3\times4\), and \(4\times4\) labelled bipartite boards: 12, 384, and 600 instances. It independently enumerates Ferrers two-colour assignments and row orderings of the complement, rather than simply replaying the construction. It additionally verifies the proposed three-part decomposition for cyclic-deletion graphs of sizes \(3\) through \(100\).

Expected final line: `VERIFY_OK`.

The finite checks cannot certify the infinite statements; those are proved by the chain-order argument and the explicit edge partition. The embedded tests do not independently establish historical priority. Independent audit has not been performed.
