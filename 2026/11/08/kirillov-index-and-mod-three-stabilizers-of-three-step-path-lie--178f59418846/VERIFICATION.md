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

# Verification of the path-Lie-algebra index formula

Run `python3 verify.py` using Python 3. The script depends only on the Python standard library and constructs the brackets of the band-truncated strictly upper triangular Lie algebra directly from matrix-unit multiplication. Gallo and Videla identify this as the graph Lie algebra for a path. The code computes Kirillov matrices and exact ranks modulo prime fields without importing the proof's mixed-block rank formula.

For each \(n=2,\ldots,18\), and each prime field \(\mathbb F_2,\mathbb F_3,\mathbb F_5,\mathbb F_7\), the script checks the explicit functional has rank \(2n-2\), the predicted mixed-block rank, and the given radical vector. These are \(68\) witness checks. It separately exhausts all noncentral functional coordinates for \(n=2,\ldots,8\) over \(\mathbb F_2\) and \(n=2,\ldots,5\) over \(\mathbb F_3\), totaling \(13{,}382\) forms, each satisfying the proposed upper bound and alternating even-rank property.

`verification_output.txt` contains the replay output. The general proof is a symbolic recurrence and alternating-form argument; the finite tests do not establish validity beyond their enumerated parameters or represent an independent audit.
