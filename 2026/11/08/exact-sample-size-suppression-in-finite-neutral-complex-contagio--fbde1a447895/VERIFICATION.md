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

Execute `python verify.py` with Python 3.10 or newer and no external dependencies. The checker separately enumerates binomial contact-composition probabilities, checks all interior absorption harmonic identities for populations up to 23 and encounter counts up to 11, solves exact-rational tridiagonal absorption systems for independent confirmation, checks symmetry/strict inequalities, and evaluates the asymptotic saddlepoint formula using log-Gamma sums at odd and even populations. The program reports `VERIFY_OK 2863 exact transitions, systems, asymptotic instances`.

The proof in `RESULT.md`, not the finite checker, establishes all-population claims. The asymptotic comparison is a numerical consistency check only; the asymptotic proof uses Stirling's formula and a unique strictly concave saddlepoint. Exact finite-source sampling, self-play permission and neutral Fermi probability \(1/2\) are assumptions, not consequences of the experiments. No independent external audit has been performed.
