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

# Reproduction and scope

For the exact proof, see `RESULT.md`, especially the weighted integral (5), its polynomial reduction, the nondegeneracy restriction \(A>0\), and the feasible-interval construction. Run `python verify.py` after installing `requirements.txt` using standard package tooling. The verifier is standalone and examines the exact symbolic identities in the half-perimeter \(s\), the side lengths \(a,b\), and edge inner product \(q\), with \(A^2=a^2b^2-q^2\).

Observed output:

`VERIFY_OK symbolic_moment_identities=3 rational_inverse_shapes=4 feasibility_cases=187 midpoint_quadratures=3`

The symbolic identities test general polynomial equalities. The finite rational and quadrature checks are supplementary; they do not certify all shapes by enumeration. Mathematical limits: positive area and exact population moments; no guarantee for noisy data or non-parallelograms. External independent audit has not been performed.
