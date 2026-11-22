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

The local reference implementation `verify.py` is standalone Python 3, requiring no third-party packages. From the directory containing it, run `python3 verify.py`; the observed result was `VERIFY_OK 3473`.

The implementation enumerates graph orientations with optional absent edges on up to four vertices, compares exact homomorphism counts into three-level transitive targets with the polynomial reduction, and checks fixed-seed finite random configurations on up to eight vertices. It additionally compares full middle-fibre polynomial coefficient vectors for small graphs and checks Fibonacci admissible-orientation counts through fourteen vertices. The tree family is checked against its two closed-form counts. These are finite computations, not a proof for unbounded graphs; the all-size argument is in `RESULT.md`.

No independent audit or external validation has been performed. Historical-priority uncertainty about earlier counting-CSP formulations remains.
