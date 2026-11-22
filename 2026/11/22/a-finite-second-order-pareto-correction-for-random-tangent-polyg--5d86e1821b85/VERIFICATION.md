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

The analytic proof establishes the normal-gap density, the exact tangent-area identity, a finite residual mean for every fixed \(n\ge4\), and a quantitative \(o(t^{-2})\) bound for all excluded double-near-semicircle configurations. The numerical checker is ancillary.

Install the dependencies listed in `requirements.txt` and execute `python verify.py` with Python 3. The checker integrates the explicit residual law for \(n=4,5,6\), verifies the exact quadrilateral \(\log2\) identity, reconstructs 600 polygon areas independently by intersecting adjacent tangent lines and applying the shoelace formula, and uses deterministic-seeded Sobol quadrature for the nonoverlapping extreme-gap contribution at thresholds 10,000 and 100,000. It reports the amount of discarded high-residual mass as an explicit upper bound.

The packaged run printed `ALL_CHECKS_PASSED`. In particular, the calculated \(n=4\) coefficient \(D_4=6.272449683341\ldots\) was compared against the finite-threshold rescaled values \(6.12198400\ldots\) at 10,000 and \(6.26940037\ldots\) at 100,000. A rigorous (though conservative) union-bound cap for the omitted sector, multiplied by the squared threshold, was approximately 3.881 at 10,000 and 1.801 at 100,000. A separate diagnostic omits that sector from quadrature; no claim is made that the finite quadrature itself is exact. Sampling and floating-point tests cannot prove a limiting expansion or exclude an undiscovered prior theorem.

The full source, proof and checker are self-contained within their respective files. No separate certificate or independent audit is supplied.
