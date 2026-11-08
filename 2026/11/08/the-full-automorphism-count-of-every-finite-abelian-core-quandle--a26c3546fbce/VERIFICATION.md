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

# Reproducible verification

Run `python3 verify.py` in the same directory. The Python standard library is sufficient. The file `verification_output.txt` contains the recorded output.

The checker constructs direct core-quandle multiplication \(x*y=2y-x\) on finite direct products of cyclic groups. It exhaustively evaluates every permutation for eight groups of order at most eight: \(C_2\), \(C_4\), \(C_8\), \(C_3\), \(C_2^2\), \(C_2\oplus C_4\), and \(C_2\oplus C_3\) and \(C_2^3\). It independently enumerates additive automorphisms of \(2G\) and compares the exact formula on twelve groups.

For the four configurations \(C_2\oplus C_4\), \(C_2\oplus C_8\), \(C_4^2\), and \(C_2\oplus C_4\oplus C_3\), it constructs every normalized map from the coset criterion and verifies both bijectivity and the quandle identity on all ordered pairs; their normalized counts are respectively \(16\), \(32\), \(384\), and \(32\). Multiplying by their group orders gives \(128\), \(512\), \(6144\), and \(768\) unrestricted automorphisms.

No computation establishes an all-groups result; that follows from the proof in `RESULT.md`. The test program is not a formal proof assistant or an independent expert certificate.
