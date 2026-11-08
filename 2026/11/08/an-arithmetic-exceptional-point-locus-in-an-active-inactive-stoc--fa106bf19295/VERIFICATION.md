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

The supplied `verify.py` assembles the full Markov generator separately from its Fourier-space analytical blocks, calculates full matrix exponentials, and verifies the exact Fourier inactive-mode formula. Replaying `python verify.py` produced the result in `checks.txt`.

The numerical work covers finite sizes and does not independently certify an infinite-size mathematical statement. The all-size classification, Jordan structure, parabolic locus, and density assertion follow from the explicit algebraic proof in `RESULT.md`. This verification describes the direct checks only; no independent audit has been performed.
