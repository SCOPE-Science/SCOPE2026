---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Checked the reduction and certificate in RESULT.md, VERIFICATION.md, verify.py and verification_output.txt without executing the uploaded code. The one-bit condition permits normalization to words starting in 0 and ending in 1. At n≥14 the seven-bit endpoint blocks are disjoint, so the maximum is the largest compatible rectangle size times 2^(n−14); this includes the boundary n=14 and self-pairs. In the submitted search the product of the largest possible prefix count and current compatible suffix count is a valid upper bound. At equal depth and suffix mask the greater chosen count dominates every continuation, so memoization is valid. Independently, `python3 /workspace/replay/restricted_overlap_closed_sets.py 1 2 3 4 5 6 7` constructed the graph by literal string comparisons and enumerated mutual closures without objective pruning. Any positive rectangle can be enlarged to a mutually closed one; each nonroot closed prefix set is reachable by adding its least not-yet-included element and closing, with the canonical test rejecting additions inducing lower new indices. This traversed 1,944 closed sets with nonempty suffix side at cutoff seven, found maximum 744 with a 24×31 witness, and returned the sequence 1,2,6,20,64,216,744 across all seven cutoffs. A separate intersection-state dynamic program confirmed 744 and checked the frozen witness directly. These exact finite computations establish the endpoint coefficient only; the disjoint-block argument extends it to all stated n.

## originality

PASS

Best of current evidence, the claimed distinct contribution is solely the unrestricted binary matching upper bound at cutoff seven. The witness, the compatibility-graph viewpoint and the middle-word scaling already occur in the literature. The strongest available same-parameter sources leave the coefficient gap open; an inaccessible plausible source remains a named risk, not negative evidence.

## value

PASS

This is the next natural binary cutoff after the previously exact smaller cutoffs and a case explicitly treated as computationally difficult in the construction paper. Closing the real gap between its witness and upper bound fixes the capacity for every n≥14, rather than reporting one experiment or recomputing a known table entry. The exact endpoint calculation is reproducible and avoids assuming that a specially constructed family contains an unrestricted optimum.

The dated certificate retains the supplied scientific assessment, sources and limitations.
