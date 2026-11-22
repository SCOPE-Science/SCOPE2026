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

Run `python3 verify.py` in a directory containing the supplied verifier, using Python 3 with only its standard library.

The verifier regenerates the two-sided no-triple window set, checks the degree classification and balanced graph, constructs the two-arc forced-corridor contraction, and confirms all contracted branch states are reachable from the prescribed root. It computes the exact principal cofactor by a fraction-free integer determinant for orders \(4\le n\le11\). As a separate arithmetic check it computes the complete, uncontracted Laplacian cofactor for \(4\le n\le9\). It independently enumerates every labeled-edge Euler circuit, canonically rooted at one fixed starting edge, for \(4\le n\le7\). All three agree wherever their ranges overlap.

Exact results: \(C_4=1\), \(C_5=5\), \(C_6=12\), \(C_7=44\), \(C_8=6720\), \(C_9=1832544\), \(C_{10}=48681971200\), \(C_{11}=4431338775673113600\).

These enumerations do not prove an all-length statement on their own. The all-length argument depends on the cited unique optimal-window-support theorem, the forced-corridor in-arborescence bijection, BEST, and the directed matrix-tree theorem. The code does not independently reprove the cited maximum-length and rigid-support theorem.
