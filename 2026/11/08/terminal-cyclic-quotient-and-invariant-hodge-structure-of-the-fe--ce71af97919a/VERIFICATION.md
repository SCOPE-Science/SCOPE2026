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

# Reproducible checks

Execute `python3 verify_fermat_quotient.py` with the Python 3 standard library. The saved script was run with its own source files and ended in `VERIFY_OK`.

The check enumerates all five Fourier eigendirections, detects four fixed points on the quartic, and reconstructs the three projective tangent characters at each one. It verifies all sixteen Reid–Tai inequalities for the four nonidentity group powers at the four points. It then enumerates the thirty cubic monomials in the quartic Jacobian ring and partitions them into exactly six orbits of length five. Finally it recomputes the quartic's Euler characteristic from Chern classes, the quotient's ordinary and orbifold Euler characteristics, and the anticanonical volume.

These finite computations are exact, not samples. The analytic linearization of a finite group at a fixed point, canonical divisor pullback under a quasi-étale map, Lefschetz and Hodge residue identifications, and rational cohomology transfer for finite quotients are the mathematical inputs proved or explained in the result, not capabilities implemented by the verifier. No independent mathematical audit has been performed.
