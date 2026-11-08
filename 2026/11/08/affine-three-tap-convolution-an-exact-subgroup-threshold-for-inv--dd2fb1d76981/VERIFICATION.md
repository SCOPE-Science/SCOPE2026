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
The bundled `check_affine.py` is a dependency-free Python 3 script. Execute `python3 check_affine.py` and expect `AFFINE_THREE_TAP_CHECKS_PASS cyclotomic_orbits=281 modular_rank_cases=72`. This run independently checked the actual packaged script after extraction.

For each listed small prime, every multiplier of order at least two was examined. Exact cyclic integer coefficient reduction checked each multiplicative-orbit cyclotomic block identity, totaling 281 orbits. For groups with at most 120 elements, two nonzero translation/shift parameter pairs were checked using rank elimination over the prime field with 65537 elements, totaling 72 matrices. The statement of the theorem itself requires complement order at least three. The exact finite tests rule out a range of sign/index errors but do not prove the general result, which rests on the written Fourier/cyclotomic argument.

The full text of a closely related historical affine-graph paper by Bell and Minei (2006) was not accessible, leaving a bounded-priority risk. Independent mathematical validation has not been performed.
