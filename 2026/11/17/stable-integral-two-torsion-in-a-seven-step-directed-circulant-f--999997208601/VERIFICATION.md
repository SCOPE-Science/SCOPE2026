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

# Verification

Run `python3 verify.py` and compare with `verification_output.txt`. The code uses only Python's standard library. It independently reconstructs the complete short-addition relation lattice, verifies its maximal-minor gcd two and the explicit twice-a-torsion-generator relation. It computes the GLMY degree-two boundary presentation in full for the cyclic moduli 41 and 43, over two fields with different characteristics. This supports but does not replace the infinite integral proof in `RESULT.md`.

Finite arithmetic checks: all passed. Exact rank/minor tests are not a homotopy classification or an all-degree integral computation. The scientific claim covers first integral path homology for moduli at least 41. Independent audit: not performed.
