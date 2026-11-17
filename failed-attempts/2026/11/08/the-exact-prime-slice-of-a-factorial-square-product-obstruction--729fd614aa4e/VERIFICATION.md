---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

The actual RESULT.md proves s(c!)>27c^3/125>c^2 for c>=51 by three pairwise disjoint Nagura intervals contained in (c/2,c); each selected prime has exponent exactly one in c!. Independently trial-factored c=12..50 and confirmed strict s(c!)>c^2 and s(11!)=77. For p>=13, c<p preserves s(pc!)=p s(c!); for c>=p, squarefree prime toggling gives p s(c!) or s(c!)/p>=c^2/p>=p. Directly verified all five counterexamples (p,c,s(pc!))=(2,2,1),(3,3,2),(5,6,1),(7,7,5),(11,11,7). The infinite range genuinely depends on the published Nagura theorem, not finite tests.

## originality

FAIL

An October 13 published result proves exactly the identical prime slice in exactly Yudin’s set and a strictly stronger s(c!)>c^2 bound beginning at 12, with the same 11! endpoint. Thus the candidate theorem is already an exact corollary (indeed same conclusion) and has no surviving novel claim.

## value

FAIL

The prime-stratum obstruction and sharp cut-off are mathematically motivated, but both were already published, and the new proof merely changes the Nagura interval decomposition/finite endpoint. No new unknown invariant, classification, or independently valuable exact boundary survives.

The dated certificate retains the supplied scientific assessment, sources and limitations.
