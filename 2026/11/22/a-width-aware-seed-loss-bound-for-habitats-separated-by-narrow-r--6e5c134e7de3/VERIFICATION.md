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

# Verification record

The proof in `RESULT.md` establishes the universal outflow bound, the Jensen step, and the exact order-two correction symbolically. No numerical experiment is used as an infinite proof.

Run `python verify_gap.py` using Python 3 and SciPy. The script checks 600 randomly generated Gaussian two-dimensional geometries against the kernel-aware and mean-only bounds; 600 more Gaussian cases against the Jensen improvement; 100 two-radius Jensen instances; nine small-road Gaussian scalings; six direct Gaussian capped-displacement integrals; and nine direct fixed-radius angular integrations against the exact analytic correction. All these checks passed on the included source code.

Reproducible Gaussian example: reserve width \(1\), height \(4\); one roadway from \(0.5\) to \(0.505\); isotropic Gaussian coordinate standard deviation \(0.02\). Exact loss (quadrature/formula): approximately \(0.024471799238\). Mean-only upper bound: approximately \(0.024732294769\). Perimeter upper bound: approximately \(0.036065184042\). These printed approximations should not be mistaken for exact symbolic certificates.

No external independent validation has been performed. The result does not establish ecological parameter accuracy or exhaust all historical mathematical literature.
