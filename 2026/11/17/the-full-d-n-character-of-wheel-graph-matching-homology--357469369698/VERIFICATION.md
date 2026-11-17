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

The attached `verify_wheel.py` uses only the Python standard library. Running `python3 verify_wheel.py` exhaustively enumerates all matchings for \(3\le n\le16\), computes signed traces of all \(2n\) dihedral elements, compares them with the general formula, and independently checks mod-two simplicial boundary ranks for \(3\le n\le11\). It also checks the cycle and reversed-path independent-set formulas for lengths through \(18\), plus cyclic and dihedral invariant congruences for \(3\le n\le300\).

The supplied `verification_output.txt` is the actual output of a successful execution of that same script. The result is finite computational corroboration; it does not substitute for the all-parameter proof in RESULT.md. No independent audit has been performed.
