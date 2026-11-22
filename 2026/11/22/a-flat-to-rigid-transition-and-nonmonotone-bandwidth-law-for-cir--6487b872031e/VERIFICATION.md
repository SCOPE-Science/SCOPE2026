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

The standalone `check.py` runs with Python 3 and SymPy. It makes exact rational calculations of the forward moving-average integral on many rational window/arc pairs, checks closed-form and derivative identities symbolically, confirms rational-grid comparisons, and independently evaluates truncated Fourier series at selected parameters. On the reviewed package the checker passed **7,354 assertions**; numerical Fourier comparisons have explicitly bounded finite truncation, while exact integration checks use `fractions.Fraction`.

The full quantified result does not rely on the tested grids: the proof separately establishes the Jordan BV measure reduction, the exact integral formula, global monotonicity/plateau inequalities, and equality rigidity from strict Fourier multiplier separation. The formal scope is real circular BV, standard \(L^2\), and forward boxcar \(0<a\le1\).

Unperformed: independent audit and full-text comparison with one historically related 2009 approximation-error article. This record does not assert validation by an external mathematical authority.
