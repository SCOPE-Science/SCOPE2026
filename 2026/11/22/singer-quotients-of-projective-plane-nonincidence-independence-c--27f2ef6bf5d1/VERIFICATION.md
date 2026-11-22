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

# Reproducibility

Execute `python3 verify.py` with Python 3, using no external packages. The program must finish with `SINGER_NONINCIDENCE_QUOTIENT_CHECKS_OK`.

The verification explicitly enumerates cyclic plane difference sets for orders two, three, and four; all incident pairs and equivariant star-tree edges; and the order-two quotient cellular chain after stellar subdivision at the two fixed-shore barycenters. It verifies chain identities, exact elementary integer pivot cancellations, and the remaining two free degree-two generators. This is a finite consistency check, not a proof for arbitrary prime powers.

The infinite proof rests on the equivariant nerve lemma for invariant finite subcomplex covers, explicit linewise relative simplicial collapses, and a group-ring chain basis change. These mathematical steps must be evaluated separately from the executable finite checks. No independent audit has been performed.
