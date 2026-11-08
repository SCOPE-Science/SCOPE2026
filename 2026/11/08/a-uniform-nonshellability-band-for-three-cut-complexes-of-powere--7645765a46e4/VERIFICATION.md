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

# Verification and scope

The attached `VERIFY.py` is self-contained Python 3 with no nonstandard packages. It independently builds the seed complex and its Alexander dual, computes mod-two boundary ranks using exact integer bit operations, checks the claimed induced adjacency for all parameter pairs in the finite test window, and checks the graph-link identity for the indicated small powers. `VERIFY_OUTPUT.txt` contains the actual standard output of one execution of the embedded script.

The seed has reduced mod-two Betti number one in degree three, whereas its facets are four-dimensional. Its non-shellability, the graph-link identity, and the all-parameter embedding inequalities are explained by a mathematical proof in `RESULT.md`. Verification of finitely many cases alone would not prove a universal theorem. The upper/lower bounds are optimal only for cyclic-order-preserving copies, as stated.

Scientific checks are self-review only; no independent audit, certification, or external validation was performed.
