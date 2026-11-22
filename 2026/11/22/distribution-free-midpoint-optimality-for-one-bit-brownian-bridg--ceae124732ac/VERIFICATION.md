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

# Reproducibility and boundaries

Run `python verify.py` after installing the dependency in `requirements.txt` with `python -m pip install -r requirements.txt`. The script checks the exact noiseless covariance formula against integration for nine observation times, a closed Gaussian midpoint risk coefficient against integration at seven distinct correlations, midpoint dominance at 56 off-center constant-relative-noise settings, 24 off-center fixed-absolute-noise settings, and 18 off-center discrete symmetric-noise settings. It additionally checks two exact limiting constants. It passed all 116 assertions.

The universal theorem is not certified by these finite tests. Its noncomputational proof needs (i) the previously established uniform occupation law, (ii) the elementary conditional bivariate normal sign identity for any independent symmetric noise, (iii) the Brownian-bridge log-odds correlation transform and (iv) the strict monotonicity of interval averages of the logistic density. The critical boundaries are finite almost-sure noise, an interior observation time, symmetry of noise, and a standardized scale that attains its global minimum at time \(1/2\). Full-value observations, asymmetric channels and unrestricted time-dependent noise amplitudes are unproved.

No independent audit has been performed. Numerical tests do not establish historical novelty or all-parameter mathematical validity.
