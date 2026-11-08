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

The accompanying `verify.py` is an ordinary reproducibility checker and requires Python 3 and NumPy. It constructs full Fourier sampling matrices for 36 finite configurations using cyclic and noncyclic finite abelian alphabets, checks their complete Gram spectra against independent moment formulas, and tests representative numerical large-dimension asymptotics. Successful output: `HAMMING_BALL_FIRST_BAND_CHECKS_PASS finite_cases=36`.

The exact finite checks validate arithmetic, Fourier normalization, and eigenvalue multiplicities. The asymptotic checks are illustrative numerical tests only. The derivation of the subcritical geometric tail, the truncated Gaussian second-moment limit, and the supercritical spectral convergence is contained in the proof; these infinitely quantified steps cannot be certified by finitely many numerical cases. No independent scientific audit or external validation is claimed.
