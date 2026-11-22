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

# Verification details

The calculation is analytic. The proof uses the exact integer-redundancy Zak identity, finite-dimensional projection and equality analysis on the one-sided Zak strip; no computer search stands in for the universal quantifiers.

Run `python3 check_uniform_two_decay.py` beside the mathematical document. The completed standard-library-only diagnostic printed:

```
TWO_DECAY_GABOR_CHECKS_PASS 950 grid samples; 5 edge and coalescence parameter cases
```

It checks five distinct parameter triples, 950 sampled complex-mixture fibers, independent geometric-series reconstruction, exact boundary-fiber equality, the local coalescence expansion and a zero at critical density. Every finite numerical check is a reproducibility diagnostic, not a rigorous infinite-domain certificate.

The source-priority comparison explicitly excludes already known qualitative two-pole frame existence and standard Zak diagonalization; full historical priority remains subject to independent specialist verification.
