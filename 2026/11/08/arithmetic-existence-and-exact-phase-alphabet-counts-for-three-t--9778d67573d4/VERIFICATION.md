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

Run `python3 CHECK.py` with Python 3.10 or newer; the standard library suffices. The program constructs all \(3p\) actual Gabor columns for each tested \((N,s)\) and checks every matrix entry against the predicted antipodal blocks. It also verifies root-of-unity constructions for various odd step orders divisible by three, and exact finite enumerations for two phase-alphabet sizes. The number of assertions is printed when execution succeeds.

The unbounded statements for all even \(N\), all nondegenerate \(s\), and all integer \(q\ge2\) are justified by the explicit group-orbit proof in `RESULT.md`; a finite checker is not a substitute for that proof. No external validation or independent mathematical audit has been performed. The complete classification does not cover nonflat amplitudes, more than three translations, or nonlinear phase retrieval.
