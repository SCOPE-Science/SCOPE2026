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

# Reproducibility and limits

Execute `python3 check.py` in a folder containing the accompanying files. The program uses only the Python standard library and constructs the truncated Witt bracket exactly as \([x^h\partial_x,x^j\partial_x]=(j-h)x^{h+j-1}\partial_x\), with all exponents outside the truncated algebra discarded.

The checker exhausts \(125\) elements over \(\mathbb F_5\), \(16{,}807\) elements over \(\mathbb F_7\), and \(15{,}625\) elements over \(\mathbb F_{25}\). The quadratic extension is implemented with the irreducible relation \(\alpha^2=2\) over \(\mathbb F_5\). For each nonzero element it compares the actual ranks of *all positive powers* of its adjoint matrix with the proposed formula. It also performs 500 fixed-seed random checks over each of \(\mathbb F_{11}\) and \(\mathbb F_{13}\), and it independently checks both ambient-Witt example partitions at \(p=5,7,11,13\). The recorded result ends with `WITT_NILRADICAL_JORDAN_DIRECT_BRACKET_OK`.

The finite calculations are complete only in the three stated exhaustive cases; the arbitrary-field theorem is mathematical, not a finite-experiment extrapolation. The example illustrates non-rigidity of the full Witt adjoint representation but is not a census of all full-Witt Jordan partitions. This document records no independent audit or external certification.
