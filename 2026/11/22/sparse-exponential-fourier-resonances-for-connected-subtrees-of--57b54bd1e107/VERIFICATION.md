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

# Exact computation and proof boundaries

Run `python3 verify_spider.py` with Python 3.9 or later, without external dependencies. It builds each subdivided-star graph directly from its adjacency masks and enumerates **all** vertex subsets for each arm count from one through eight; the connected-subset indicator is transformed with an integer fast Walsh–Hadamard transform. The resulting signed histogram is compared term by term to the independent closed-form formula. The program verifies the total frequency count, Parseval's identity, and the empty-subset Fourier-sum identity.

The program also checks the arithmetic resonance equivalence for every arm count from two through 499, and checks the exact claimed spectral gap at the first seven exceptional indices. These are finite checks. The all-orders results rest on the elementary symbolic factorization and inequalities proved in `RESULT.md`, **not** on extrapolating the computed cases. No independent external certification or audit has been performed.

The saved `verification_output.txt` is the actual stdout of the standalone script, including the final `PASS` indication. The user may reproduce it from source on a clean Python installation. Numerical tolerance and random sampling play no role.
