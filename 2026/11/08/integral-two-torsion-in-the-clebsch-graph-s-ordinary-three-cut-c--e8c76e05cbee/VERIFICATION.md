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
# Reproduction of the integral homotopy computation

Run `python3 verify_clebsch_cut.py` from the directory containing that file, using Python 3.10 or later. Only the standard library is needed. The program terminates with `ALL CHECKS PASSED` if and only if every assertion and the full acyclicity, signed boundary and independent dual-field checks succeed. `verification_output.txt` is the complete recorded execution output.

The exact domain is the sixteen even-weight five-bit words, with edges at Hamming distance four, and ordinary disconnected-triple complements. The program reconstructs all 400 facets and 65,198 nonempty faces, verifies a fixed 32,590-pair matching and examines all 519,776 nonempty Hasse incidences. A complete topological sort certifies acyclicity. An explicit recursion over directed gradient paths, with signs induced from increasing vertex order, computes the sole nonzero possible Morse differential, whose entries have gcd two. In high dimensions the Hurewicz isomorphism identifies this differential with the homotopy attaching degree, proving the stated sphere-plus-Moore wedge.

The independent Alexander-dual code does not reuse the cut-complex face enumeration: it tests all candidate subsets against the condition that every induced triple be connected. It builds finite-field boundary matrices from the resulting 337 dual faces and confirms the characteristic-two rank drop. Field calculations alone cannot establish the integral attaching degree; the separate exact signed Morse computation does so. The program does not constitute independent human review, does not verify unexamined external claims and does not extend this finite graph result to other graphs.
