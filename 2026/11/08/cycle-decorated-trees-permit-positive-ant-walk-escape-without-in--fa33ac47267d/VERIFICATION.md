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

# Reproducible verification

Run `python3 verify.py` with Python 3 and only its standard library. The standalone program constructs finite rooted trees with a private cycle attached to each node, including cycles of varying lengths. It computes directed crossing numbers and the resulting exact rational transition probabilities for every strictly outward path across the selected finite depths, then sums those probabilities and compares against the claimed finite product.

The checker reports 10,942 exact-rational finite probability comparisons (including conditional transition-weight and path-enumeration tests), plus 117 high-precision numerical inequalities checking finite approximants against the explicit analytic lower bound. The tested cycle lengths include lengths three through nine; the main proof permits every finite cycle length at least three. The bound is derived analytically from \(\log(1+x)\le x\) and the geometric reciprocal-degree sum; the checker cannot replace that proof.

Reproducibility is self-contained; no library downloads, network queries, external datasets, random seeds or hidden certificates are required. The main theorem and assumptions are in `RESULT.md`. A finite test does not certify all infinite graphs, all branch sequences, or the asymptotic positivity criterion.
