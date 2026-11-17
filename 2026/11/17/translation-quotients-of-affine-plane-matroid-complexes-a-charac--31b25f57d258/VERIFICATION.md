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

# Reproducibility and verification

The full proof is in `RESULT.md`. Run `python affine_check.py` with Python 3 and SymPy installed; no network access or downloaded dataset is used. The program reconstructs finite-field addition and multiplication for \(\mathbb F_2\), \(\mathbb F_3\), and \(\mathbb F_4\), enumerates noncollinear affine triples and all proper-face chains, and constructs the geometric translation quotient after barycentric subdivision. The oriented flag boundary matrices satisfy \(\partial_1\partial_2=0\). A spanning-tree contraction converts first homology to an integral relation matrix; exact Smith forms determine the torsion and second-homology ranks.

The recorded output is in `finite_checks.txt`, with checksum held in the enclosing file manifest. In particular \(q=2\) gives \(H_1=0\), \(\operatorname{rank}H_2=1\); \(q=3\) gives \(H_1\cong(\mathbb Z/3)^2\), \(\operatorname{rank}H_2=4\); \(q=4\) gives \(H_1=0\), \(\operatorname{rank}H_2=30\). These finite exhaustive computations corroborate the proof at three distinct orders; they are not exhaustive over prime powers and do not establish the general theorem by themselves.

The infinite proof uses matroid shellability, the precise translation stabilizers, the orbit-space fundamental-group theorem, Burnside's Euler-characteristic identity for finite CW actions, and the elementary integral-homology and simply connected Whitehead arguments. No independent outside audit or computer formalization was performed.
