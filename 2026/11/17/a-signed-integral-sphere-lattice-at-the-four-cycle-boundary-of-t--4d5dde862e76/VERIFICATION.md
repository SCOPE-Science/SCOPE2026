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

Run `python3 verify.py` with a standard Python 3 installation; there are no dependencies. The script independently constructs the graph and every allowed simplex directly from the connected-triple criterion, exhaustively rejects possible five-vertex faces, and validates all actual free-face/coface pairs in the \(14n\)-collapse. It reconstructs the survivor, counts long edges and independently computes mod-two boundary ranks from the original complex for \(n=5,6,7,8\).

The second part builds the signed integral cell-boundary model, checks \(\partial z_b=0\) for every \(b\), verifies the strip-coordinate basis is primitive, and computes all four generator actions as actual oriented square permutations. It also checks the exact signs, not only rational traces. Successful execution ends with `INTEGRAL_SYMMETRY_PASS` and includes `THIN_TORUS_THREE_CUT_PASS`.

The universal proof is the combinatorial collapse, integral two-chain boundary equations, and topological capping argument in RESULT.md. Finite checks are not an exhaustive proof of an infinite assertion. Independent audit is not performed.
