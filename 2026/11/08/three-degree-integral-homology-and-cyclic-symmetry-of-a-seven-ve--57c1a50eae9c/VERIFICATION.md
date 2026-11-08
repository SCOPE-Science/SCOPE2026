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

# Verification evidence

The standalone `verify.py` reconstructs all faces of the consecutive-difference tournament by two independent enumerators, tests the directed acyclicity of both lexicographic face matchings against the complete Hasse graph, computes signed integral Morse boundaries by substitution along gradient paths, and performs exact integer Smith calculations with SymPy. The ascending Morse boundary has an explicit determinant-one maximal-rank minor. An independent mod-two simplicial chain calculation checks the resulting Betti ranks. Signed orbit-sum boundary matrices supply the exact rational invariants under the natural cyclic rotation, and the chain identity is checked.

Run `python verify.py`; compare stdout byte-for-byte with `verification_output.json`. No outside data, downloaded certificate, or external executable is required beyond Python and SymPy. The program does not establish a full homotopy type, and this work has not undergone an independent audit.
