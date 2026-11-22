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

# Verification and reproducibility

Run `python3 verify.py` using Python 3 and its standard library. The program directly enumerates all filled consecutive triangles and every tolerance-one face in dimensions two and three, then performs the three stated sequences of ordinary elementary collapses. Each proposed free face is checked against the **entire current set** of remaining tetrahedra before deletion. Counts, final absence of tetrahedra and the formula for the second Betti rank are checked for all integers \(9\le n\le30\). Eight additional exact bit-vector \(\mathbb F_2\)-rank computations, at lengths \(9\le n\le16\), independently verify that the original degree-three boundary has full column rank.

`verification_output.txt` records the executed output. The infinite assertion relies on the written proof of freeness and exhausting all tetrahedra at arbitrary \(n\ge9\), the spanning-tree argument for the fundamental group, and Hurewicz/Whitehead. The program tests finitely many inputs and does not by itself establish an unrestricted theorem. No independent audit has been carried out.
