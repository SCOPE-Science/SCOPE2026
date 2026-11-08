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

The analytical derivation, not a finite experiment, proves the all-site, all-time theorem. The included `verify.py` independently multiplies two-state Markov transition matrices to check the four-time connected kernel, tests a one-body exact beta-law cumulant, compares a positive matrix-exponential transfer to a closed form, checks disconnected ancestry, and evaluates one mixed-lag integral with deterministic quasi-Monte-Carlo quadrature.

Replay from the extracted package root:

```sh
python verify.py
```

Observed result: `PASS: 895 deterministic checks`. The sample negative mixed-lag connected cumulant is approximately `-0.0007348809245`. Exact integration of the one-site case appears in the proof and is not inferred from quadrature. The code was replayed with Python 3.13.5, NumPy 2.3.5 and SciPy 1.17.0; `requirements.txt` declares the tested dependencies. It requires no private datasets or external services.

Limitations: the numerical tests concern finitely many graphs, lags and rates. They do not certify novelty, all possible models, statistical detectability from finite samples, or any independent audit.
