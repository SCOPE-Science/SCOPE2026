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

Run `python check.py` with Python 3, NumPy and SciPy in the same directory as the accompanying mathematical report. The provided checker was executed on the actual included file with `OPENBLAS_NUM_THREADS=1 python check.py` and returned: `PASS: 2182 finite exact and numerical checks; not an infinite-dimensional proof`.

The checker evaluates all \(k\le3\) minors of the seven-site lower-triangular step matrix exactly using rational elimination, compares singular-value products for several finite matrix sizes and ordered parameter values, and independently compares the elliptic coefficient with angular quadrature and selected high-index singular values. Floating-point tolerances are stated in source.

The proof in RESULT.md, rather than these finite diagnostics, establishes every infinite-dimensional assertion: the compound-matrix formula, the Poisson integral, the weighted Toeplitz counting lemma with truncation control, and the elliptic integral consequence. No independent verification of the general proof is claimed. The singular limit is only for each fixed parameter strictly below one; the order theorem does not entail monotonicity of each individual singular number.
