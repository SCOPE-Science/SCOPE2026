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

The source file `rank_resolution_check.py` is self-contained apart from SymPy. Running `python rank_resolution_check.py` completed 10,485 exact rational assertions. It checks the interval-moment matrix, its rank at several nonuniform masses, alternating blind alternatives through their first visible rank response, the precise Pearson departure, bounded exhaustive sign-change tests, and cofactor constructions for unequal null probabilities. It outputs a JSON success record only if all assertions pass. This is supplementary evidence, not exhaustive verification over all alphabets or parameters.

The infinite-parameter theorem is established by the integrated Vandermonde determinant (strictly positive maximal minors), the polynomial sign obstruction, the cofactor identity, and the binomial finite-difference identity in `RESULT.md`. All checks were performed against the current bundled checker source; no external certification, independent replication, or formal verification has been performed. The applicability and literature-priority limitations stated in `RESULT.md` remain in force.
