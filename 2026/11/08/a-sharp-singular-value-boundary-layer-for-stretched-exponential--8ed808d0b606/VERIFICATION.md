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

The analytical proof consists of six steps in `RESULT.md`: the known binomial Aluthge formula; the norm-scale law; the compressed regime's dominated-convergence argument; exact evaluation at the critical exponent; locally uniform binomial concentration for the stretched regime; and an explicit summable tail bound followed by a Riemann-sum limit. The last step is essential: convergence at each fixed singular-value rank does not justify convergence of the full Schatten mass.

The standalone file `check.py` uses only Python 3's standard library. Running `python check.py` produced `Passed 582 finite diagnostic assertions; not an asymptotic proof.` It verifies the binomial kernel's normalization, reproduces direct finite Aluthge iterations, tests the critical geometric identity, and compares finite normalized masses with the asymptotic formulas in several parameter regimes. Finite checks do not establish any infinite or asymptotic statement; those require the proof in `RESULT.md`.

The full source of `check.py` is included for reproduction. Independent verification has not been performed. The results do not include a uniform finite-iteration rate in varying parameters, nor do they address arbitrary compact unilateral weighted shifts.
