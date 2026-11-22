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

# Verification and evidence limits

The mathematical proof in `RESULT.md` derives the pulse response by integrating the first-order differential equations, then proves both constructive inverse maps and the method-specific lower bounds. Strict monotonicity of the logarithmic mean follows from its elementary integral representation. The common-rate branch is handled by its continuous limit, not by division by a vanishing difference of rates.

## Reproducibility

From the artifact directory, run `python3 verify.py` using the Python standard library. The fixed-seed verifier generates 10,000 positive parameter tuples (including exactly coincident and nearly coincident rates), checks both inverse formulas, passive pole-sum/product identities and exact interchange symmetry, and conducts additional tests of the one-active-measurement ambiguity and quadratic collision behavior. The recorded execution returned `SUPPLEMENTARY_ASSERTIONS_PASSED 128008`.

## Limits of checking

Finite floating-point checks are supplementary and do not establish universal theorems. The decisive proof steps are symbolic. All inference statements are noiseless and specific to the initial-value model with constant rates, an initially empty, nondepleting passive sampler and exact same-deployment observations. No field data were used to estimate the model parameters; no independent external audit or empirical validation was performed. Sensitivity can become poor away from fixed positive interior parameters, for example at vanishing signals.
