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

# Verification procedure and boundaries

Run `python3 acyclohedron_verify.py` with a standard Python 3 interpreter. It requires no third-party packages and uses exact integer arithmetic.

The script independently constructs the oriented triangle-to-edge matrix and tetrahedron-to-triangle matrix from sorted vertex tuples. It asserts every entry of the Hodge identity for \(3\le n\le8\), tests all \((n-1)!\) distinguished circular orders for those sizes, and checks the one-flip second-shell prediction for each order from \(4\) through \(8\). It exhaustively enumerates all sign vectors only for \(n=3,4,5,6\): respectively \(2\), \(16\), \(1024\), and \(1,048,576\), altogether \(1,049,618\) candidate endpoints. Every exhaustive test verifies outer radius, count of outer signings, and the second-largest squared radius where defined.

Expected successful final line:

`PASS: 22618 exact analytical-identity/order checks plus 1,049,618 exhaustive endpoint signs (n=3..6)`

The finite tests do **not** establish the theorem for unrestricted \(n\); the Hodge identity, defect-support argument, and exposing witnesses in `RESULT.md` are the infinite proof. The \(n=5\) radius/contact special case overlaps a known near-top acyclohedron result. Independent audit has not been performed.
