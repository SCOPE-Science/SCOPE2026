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

# Analytical and computational verification

The analytical proof covers all positive integer mode pairs and all real amplitudes \(0<\theta<1\). The exact density marginals, arcsine distributional identity, cosine-square and absolute-cosine integrals, and the conditional-CDF normalization are elementary continuous identities and are explicitly derived in `RESULT.md`.

The included standalone `verify.py` checker was executed with Python 3 using its standard library and passed six frequency configurations: \((1,1)\), \((2,2)\), \((2,4)\), \((4,2)\), \((4,6)\), and \((12,8)\), all at \(\theta=1/2\). It independently evaluated mutual information, total variation, chi-square divergence, and both directional population coefficients by midpoint quadrature; it also compared the two mutual-information series truncations and cross-frequency information values. These checks are finite numerical corroboration, **not** proofs of the universal claim.

Reproduce by placing `RESULT.md` and `verify.py` in one directory and executing `python3 verify.py`. No external dependencies, data, or network access are required. Independent mathematical audit has not been performed; priority assessments remain subject to the limitations stated in the scientific review.
