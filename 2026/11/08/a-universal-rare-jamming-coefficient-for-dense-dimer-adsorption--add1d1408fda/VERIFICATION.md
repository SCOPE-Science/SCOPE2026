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

# Reproducibility and evidence

Run `python verify.py` from the directory containing `verify.py`. No external packages or network are needed. It reports 62 exact-rational assertions, including the identity \(3/(N^2-1)\) for a single forbidden pair, benchmark exact probabilities for even excluded cycles through fourteen vertices, and selected small forbidden-graph and matching-deletion cases. The finite checker computes the dimer process through a fresh memoized Markov recursion over currently vacant vertex sets.

The analytic proof is self-contained in RESULT.md: uniform marked-set survival bounds, conditional extra-edge estimates and an exact telescoping probability. It is an asymptotic proof for every fixed forbidden-degree bound, not a claim of exhaustive finite numerical verification or external formal certification. Limitations and historical-priority caveats are recorded in RESULT.md and REVIEW.md. No independent scientific audit has been performed.
