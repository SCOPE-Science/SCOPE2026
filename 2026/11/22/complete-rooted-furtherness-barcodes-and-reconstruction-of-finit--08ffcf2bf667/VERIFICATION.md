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

The symbolic proof explicitly computes the principal downsets, the entire filtration sequence, the augmentation-tensor chain homology of each join, and the cone factorization killing every reduced inclusion map. It is valid for all layer vectors and roots stated in RESULT.md. The pointwise root-weight stability comparison is proved from the definitions.

Run `python3 verify.py` in the same directory to reproduce an independent finite-checking implementation. It enumerates all strict chains and computes literal downset differences, then reduces filtered boundary matrices with signed face incidence modulo the distinct primes 2, 3 and 101. It checks eleven layered posets, all root levels with two representatives when possible, for 204 root-prime runs. The expected output contains `PASS: 11 layer-size patterns; 204 root-by-prime calculations`. The program is standalone Python 3 without third-party packages.

Finite tests cannot certify statements quantified over all layer sizes, cannot prove integral torsion-freeness by themselves, and do not provide independent human or machine-checked mathematical certification. The all-parameter claims rest on the symbolic proof.
