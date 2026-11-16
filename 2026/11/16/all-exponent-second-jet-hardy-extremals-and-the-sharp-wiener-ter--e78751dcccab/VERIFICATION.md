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

# Verification and reproducibility

The proof derives the complete infinite-dimensional norm reduction from the published outer-extremal theorem, then differentiates the explicit scalar optimization on the unit root-coefficient sphere. Its nontrivial analytic checks are: existence and positivity of the Hardy extremal's root, the exact first three Taylor coefficients of an analytic noninteger power, the unique radial critical point on each feasible region, zero-freeness of the quadratic root, and support-plane recovery of the fixed-origin frontier. The relationship with the known first-coefficient optimum uses the high-origin branch of [2, Theorem 12(ii)].

Run `python3 CHECK.py` using standard-library Python 3. The checker validates coefficient normalization and the two-branch formula over deterministic grids of \(q>2\) and positive \(\tau\), compares all sampled real/complex coefficient triples with the predicted global bound, tests boundary and cutoff matching, and confirms the positive-square formula for the frontier gap. It passed 94,010 assertions when executed from this package.

The checker is finite and does not certify the continuum theorem, outer-extremal reduction, global sign analysis, or historical originality. These are assessed by the displayed proof and cited primary results. No independent audit has been performed.
