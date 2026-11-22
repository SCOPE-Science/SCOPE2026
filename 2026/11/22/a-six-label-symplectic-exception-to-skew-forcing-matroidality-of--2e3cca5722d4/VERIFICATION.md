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

Run `python3 verify.py` in this directory. It uses only the standard library and independently constructs skew forcing neighborhoods.

For \(n=3,4,6\), it checks the closure on all \(8+64+32768=32840\) initial subsets against, respectively, the uniform, dual partition, and binary-rank dual projective matroid closures. In particular, the rank of every subset of the projective geometry is computed by binary Gaussian elimination modulo the all-one vector, separately from graph forcing. Exchange failures at \(n=5,7\) and the uniform double-star witness at \(8\le n\le14\) are checked directly. These calculations verify the cited finite instances, not the unrestricted induction-free proof for every \(n\ge8\).

The replayed output is in `verify_output.txt`; the final line is `VERIFY_OK`.
