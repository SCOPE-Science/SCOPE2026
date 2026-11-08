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

Execute `python3 CHECK.py` using standard Python 3. The checker works in finite fields containing primitive \(p\)-th roots of unity and uses exact Gaussian elimination. Tested primes are \(p\in\{5,7,11,13,17\}\). For each it verifies that every exact Fourier eigenspace has full column rank when restricted to the eight stated sites and that block sizes sum to \(p^2\), with largest block size eight. For \(p=5,7,11\) it also verifies the exact rank of the complete temporal-spatial observation matrix.

The executable is supplementary. It neither proves the infinitely many prime instances nor establishes novelty. The complete unrestricted proof, including the prime-cyclotomic noncollision lemma, appears in `RESULT.md`. For composite side length and for noisy reconstruction no general optimality claim is made.
