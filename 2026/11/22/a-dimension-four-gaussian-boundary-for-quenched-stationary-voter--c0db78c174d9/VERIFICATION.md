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

# Reproducibility and analytical scope

Run `python3 check_voter_memory.py` with Python 3; no external dependencies are required. The checker constructs full continuous-time finite-spin Markov generators for three- and four-site cycles, solves the stationary linear equations with exact rational arithmetic, and compares each original-spin-conditioned stationary mean against a separately solved copy/reset resolvent. For every original opinion configuration in those finite cases, it verifies exact agreement, including the Rademacher second and fourth-moment identities. It also checks Fourier resolvent normalization, the explicit one-dimensional infinite-line variance identity, and the low-reset one-dimensional scaling constant. The run returned `PASS: 231 deterministic checks (full finite Markov generators, exact fourth cumulant, Fourier and one-dimensional identities)`.

The actual infinite-lattice Gaussian/non-Gaussian transition rests on the analytically stated heat-kernel estimates, square summability of the Green function in dimensions at least five, the Lindeberg triangular-array argument, and the fourth-cumulant identity. Neither a finite checker nor a plot is an infinite proof. The special four-dimensional logarithmic constant is an analytical limit; the checker is not represented as exhaustive evidence. No independent verification or publication-priority certification has been performed.
