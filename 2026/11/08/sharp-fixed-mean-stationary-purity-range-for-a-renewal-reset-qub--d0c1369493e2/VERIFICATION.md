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

The mathematical proof of the complete sharp interval is in `RESULT.md`. The only auxiliary dependency is Python 3 with NumPy, for the finite diagnostic program `verify_qubit_purity.py`.

To reproduce the checks from the directory containing the two files:

```sh
python3 verify_qubit_purity.py
```

The program reports 7,115 successful finite diagnostic assertions in the tested environment. It recomputes the stationary-age Fourier integral using two algebraically distinct finite-support expressions, tests exact odd-/even-resonance constructions, verifies strict approach to the missing lower endpoint, and samples fixed-mean interarrival laws across both transition thresholds. Its assertions do not exhaust infinitely many renewal laws; global validity follows from the explicitly written concavity/Jensen proof and the nonnegative trigonometric equality argument. No independent external review or proof-assistant certification was performed.

A stationary renewal initialization is necessary for any conclusion about deterministic intervals: beginning the clock at a reset instant produces a periodic time-dependent ensemble, not generally a pointwise limiting mixed density matrix.
