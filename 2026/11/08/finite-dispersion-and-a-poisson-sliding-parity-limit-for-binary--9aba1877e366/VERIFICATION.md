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
# Reproducibility and verification

Run `python3 checker.py` in the directory containing the files. The checker uses Python's standard library only, evaluates actual distinct deletion-output sets, compares the resulting counts with the deterministic identity for all binary words through length nine, then checks the exact finite Markov mean and variance using rational-weighted flip histories.

Expected successful output includes `PASS: exact distinct-output checks 8192` and `PASS: exact moment checks 132 parameter pairs`. These finite computations are corroboration and do not certify the point-process convergence for infinitely many block lengths. The latter relies on rare Bernoulli point-process convergence, Riemann approximation for moving parity windows, and exact Poisson interval parity identities as shown in the proof. No independent scientific audit was performed.
