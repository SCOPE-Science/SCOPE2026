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

Run `python verify.py` with Python 3 and no third-party packages. The program independently computes digit-sum parity by repeated Euclidean division and by a recursively tabulated formula. It compares both on 149 reduced rational radices (denominators smaller than numerators at most 22), tests the all-odd alternating case and the exact scale identity on several block lengths, and computes larger prefix-change counts for six rational bases.

Observed output: `PASS 149 coprime bases; 15377 independent identities and checks`.

The proof in RESULT.md, not the finite execution, establishes correctness for arbitrary coprime parameters and all natural indices. The computation does not establish novelty, cover higher-order factors or replace external mathematical validation.
