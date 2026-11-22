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

# Reproducibility and checks

The source-independent enumeration routine in `verify.py` applies every adjacent swap of each proper coloring and directly checks all adjacent inequalities of each candidate. Distinct resulting words are collected as a set. This is compared with a separate two-state dynamic enumerator, as well as a direct implementation of the local indicator identity.

Command: `python3 verify.py`

Observed success output: `VERIFY_OK exact_strata=31 randomized_long_words=2000`.

The check covers thirty-one manageable exhaustive alphabet-length parameter strata and 2,000 independently generated longer random proper words. It also verifies the exact frozen count, extremal degree count, and finite exact rational moments in every applicable exhaustive stratum. A finite sweep is not proof of a universal formula; the published argument derives the formulas from first principles, transfer algebra, and a bounded one-dependent central limit argument. A direct independent mathematical audit has not been performed.
