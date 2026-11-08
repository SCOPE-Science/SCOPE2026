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

The standalone `verify.py` uses Python 3 standard-library `fractions.Fraction` and deterministic `random.Random`, with no numerical precision tolerance and no external data or packages. Execute `python3 verify.py` in the directory containing this file. The reviewed output was exactly `VERIFY_OK 42875 rational matrix identities and signs; 90 weight configurations`.

It checks the explicit fourth-degree matrix polynomial against its claimed hub-to-leaf cubic and leaf-to-leaf quadratic formulas, exact row sums, strict diagonal positivity, positive quadratic certificates, negative cubic-derivative discriminants, and rational root brackets across 90 positive-weight configurations with 2–7 leaves. The test is **finite** and is not being passed off as a proof of a theorem quantified over all real positive weights and every dimension. The human-readable analytic proof in `RESULT.md` establishes the global claims, including the strict spectral stability separation and equal-conductance equality case. Numeric examples in that proof are illustrations, not certificates. Independent audit has not been performed.
