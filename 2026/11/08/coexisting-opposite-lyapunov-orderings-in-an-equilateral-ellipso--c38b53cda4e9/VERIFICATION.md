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

# Verification of the periodic spectral comparison

Run `python check_billiard.py` using Python 3 and NumPy. It constructs the equilateral obstacle centers, the two- and three-collision orbits, exact ellipsoid line intersections, and geometric normal-reflection maps. Perturbations of postcollision position are projected back to the exact ellipsoid surface before each numerical return. It computes centered finite differences for the two invariant variational directions and checks four per-collision exponents against \(\operatorname{arcosh}(1+aL/2)\) at \(\beta=11/10\). On execution it prints:

`VERIFY_OK ray_cycles=2 normal_and_planar_blocks=4 geometric_return_checks=2 thresholds_exact=1 sample_beta=1.1`

The inequality \(1<\beta^2<4/3\) and strict monotonicity of \(\operatorname{arcosh}\) give the claimed open interval analytically. The Gibbs approximation is proved by the variational principle and continuous invariant unstable line bundles; it is not verified by finitely many simulated trajectories. The program only corroborates differential geometry and monodromy normalizations. No independent scientific audit has been performed.
