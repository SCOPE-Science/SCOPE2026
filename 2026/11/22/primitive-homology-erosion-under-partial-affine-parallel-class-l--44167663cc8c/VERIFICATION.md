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

# Verification protocol

From the package directory execute `python3 verify_affine_line_fault.py`. No external modules are required. Successful execution terminates with `VERIFY_OK`, matching `verification_output.txt`.

The verifier constructs \(\mathbb F_2\), \(\mathbb F_3\), and \(\mathbb F_4\) affine incidence graphs, deletes the first \(s\) parallel line vertices, and recomputes all shortest-path distances at every stage. Over \(\mathbb F_3\), every radius-two simplex is enumerated, independent exact mod-two boundary ranks are computed, and inclusion-induced ranks are computed directly from chain maps. The four stage pairs of positive-degree homology ranks (degree two, degree three) are \((16,16)\), \((14,8)\), \((12,0)\), and \((26,0)\). Degree-two inclusion image ranks are \(14,12,10\), and degree-three image ranks are \(8,0,0\). For \(\mathbb F_4\), only graph metrics and structural clique conditions are checked; predicted homology ranks are *not* independently calculated from boundary matrices. The order-two case is a regression check outside the claimed range.

Finite calculations cannot establish the theorem for all existing affine planes, integral primitivity or absence of torsion; these depend on the written all-order graph, homotopy-pushout and integral lattice arguments. No independent validation was performed.
