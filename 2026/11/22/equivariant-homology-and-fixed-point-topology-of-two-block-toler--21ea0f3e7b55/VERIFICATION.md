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

# Verification

The standalone program `check_tolerance.py` was run from the accompanying bytes. It enumerated all simplicial faces, formed mod-two boundary matrices and independently compared the reduced Betti groups against the claim in 46 cases with two block sizes between 2 and 5 (including all admissible tolerance cutoffs). It also checked the signed simplicial Lefschetz trace under 10 equal-block exchanges, and verified that this equals the Euler characteristic of the asserted fixed-orbit skeleton. All checks passed.

The infinite-family proof is mathematical, not exhaustive computation: it uses a two-piece homotopy pushout, simplex-skeleton homology, equivariant Mayer–Vietoris signs and an explicit orthogonal sphere-action model. It proves the integral module and projective quotient without inferring infinite statements from finite rank tests.

The published minimal-size boundary-sphere example is acknowledged as prior. The full text of one recent plausible preprint was inaccessible, leaving residual priority uncertainty. This package has not been independently audited or validated.
