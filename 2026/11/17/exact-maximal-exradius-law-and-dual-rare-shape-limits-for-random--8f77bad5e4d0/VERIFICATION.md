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

# Verification performed

The analytical verification checked normalization of the anchored angle-simplex measure, the exradius half-angle identity, the three-to-one sorted-angle Jacobian, and the exact circular-section integral. At the lower endpoint, the derivative of the exradius at the equilateral point and the area of the limiting angular triangle were reconstructed. At the upper endpoint, the quadratic form \(B^2+BC+C^2\), the linear sector transform, its Jacobian and the three-corner multiplicity were checked independently. Bounded convergence of normalized sublevel-domain densities establishes the reported total-variation limits.

Run `python exradius_check.py` after `python -m pip install -r requirements.txt`. A completed run using NumPy and SciPy printed `MAXIMAL_EXRADIUS_EXACT_CDF_AND_MARKED_TAILS_OK`. The checker sampled 650,000 independent triples of polar angles. It calculated excircle radii independently from Cartesian side lengths, determinant area, and semiperimeter and compared these with the half-angle identities. Maximum discrepancy across non-extremely-degenerate tested triangles was \(4.77\times10^{-11}\). It integrated the exact CDF at six thresholds and compared each with the Cartesian Monte Carlo sample. It independently drew 1,200,000 uniform-simplex angle triples and inspected the marked shape near the upper endpoint. Finite-threshold ratios of the exact CDF approached the two predicted coefficients: for \(\varepsilon=0.005\), the lower ratio was approximately \(0.30421908\), versus \(3/\pi^2\approx0.30396355\); at \(\varepsilon=0.002\), the upper ratio was approximately \(0.36761385\), versus \(2/(\pi\sqrt3)\approx0.36755260\). The upper-tail conditional sample count was 8,926 for \(\varepsilon=0.02\), and its scaled squared-radius and angular means were approximately \(0.5028\) and \(0.5236\), versus predicted \(1/2\) and \(\pi/6\).

# Verification limits

A simulation cannot certify an asymptotic theorem or guarantee that an unsearched prior paper does not already contain it. The proofs of those claims are the exact geometric integral and the localized sublevel-domain arguments in `RESULT.md`; historical priority is provisional. In particular, no independent mathematical audit or external proof certification is claimed.
