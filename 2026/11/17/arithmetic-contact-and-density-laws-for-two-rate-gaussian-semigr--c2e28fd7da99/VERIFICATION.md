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

The mathematical statement is proved in `RESULT.md` and rests on the established closed Epperson region, which is covered in Janson's complex second-quantization criterion and the related account of van Neerven and Portal. The arithmetic deductions are independently reconstructed there: zero-site geometry, torus equidistribution, Taylor estimates, and best rational approximations.

Run `python CHECK.py` with a Python 3 standard-library interpreter. This checks 1,616 rational-period samples, 12 rational small-real-time densities, nine irrational density coefficients, 11 golden-ratio near-contacts, and 597 direct comparisons with the two boundedness inequalities. All 2,245 checks passed when executed from the prepared package.

For \(p=4\), \(\alpha=1\), \(\beta=(1+\sqrt5)/2\), the predicted coefficient \(\pi^2/(2k_p\alpha\beta\sqrt5)\) evaluates to `0.787474464789772`.

Computational checks are finite. They are not a proof of the Gaussian hypercontractivity criterion, the irrational equidistribution law, the full period-group classification, or the infinite liminf; these depend on the stated analytical argument. Literature overlap and residual access risks are described in `REVIEW.md` and `AUDIT.json`. No independent mathematical audit was conducted.
