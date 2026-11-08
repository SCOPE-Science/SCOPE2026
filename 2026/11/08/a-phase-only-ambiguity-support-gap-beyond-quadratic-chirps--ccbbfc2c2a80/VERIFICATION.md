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

# Reproducible analytical and arithmetic checks

The argument in `RESULT.md` is independent of computation. The critical lemma is an ordered-difference uniqueness claim for two or three distinct Fourier frequencies on an odd prime cyclic group. It forces a nonzero nonconstant character coefficient of the squared modulus, contradicting unimodularity. The singleton-delay recurrence is solved on the entire prime orbit to obtain exactly quadratic chirps. All remaining rows have at least four frequencies, yielding the claimed total lower bound.

Run `python3 verify_support.py` using Python 3 and no external packages. The program enumerates all 625 five-phase sequences normalized to phase zero at their first entry, classifies the exact zero/nonzero ambiguity support using the minimal polynomial of a prime root of unity, and checks cyclic differences for frequency supports of sizes two and three. It checks additional prime-alphabet examples at primes 7 and 11. Expected output:

```
PHASE_AMBIGUITY_EXACT_CHECKS_PASS 3443 p5_histogram [(5, 25), (17, 500), (21, 100)]
```

The enumeration establishes a finite statement for p-ary root-of-unity phase codes and is only a sanity test for the general result, whose proof handles arbitrary complex unit phases. Zero decisions in the checker use integer exponent-count vectors; no floating-point tolerance is involved. Every p5 phase-code check is exhaustive within the stated alphabet, while the p7 and p11 phase-code checks are selected subsets. The explicit five-point attaining example is also checked algebraically in the proof.

No external independent audit or independent validation has been performed.
