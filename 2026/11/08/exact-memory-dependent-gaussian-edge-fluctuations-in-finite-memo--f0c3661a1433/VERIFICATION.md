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

# Verification evidence and limits

Execute `python3 check.py` with Python 3 standard library. The script recomputes the finite-memory history-chain transition probabilities, known stationary Pólya block law, short-lag covariances, the centered Poisson-equation resolvent, and the exact long-run variance coefficient. The checker reports 402 passed exact rational assertions, using all states for memories 1–4 and three rational parameter pairs at each memory. Its finite Poisson-equation calculation is algebraically independent of the martingale-innovation derivation used in `RESULT.md`.

The critical mathematical verification of the *infinite* theorem is a proof check: irreducible finite-state ergodicity; bounded martingale differences; convergence of predictable quadratic variation; the martingale functional central limit theorem; the deterministic uniform \(O_M(N)\) transfer error; and Itô isometry. The test program cannot establish tightness, convergence for all memory lengths, or an infinite-dimensional theorem by enumeration.

Known prior results used (not claimed as new) are the Pólya-block distribution and ergodicity from Alajaji and Fuja (1993/1994), and general martingale/finite-state Markov limit tools. The original finite-memory graph construction is Yu, Alajaji and Gharesifard (2026). Mathematical-priority assessment is necessarily provisional; no independent audit was performed.
