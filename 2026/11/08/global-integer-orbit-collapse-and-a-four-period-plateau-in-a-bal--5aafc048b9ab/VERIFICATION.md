---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

For all integer x,y, x’<=1; in the invariant x<=1 half-plane the exhaustive cases x<=-1/y>0, x<=-1/y<=0, x=0, x=1 force descent then finite entry at (1,2), except (0,1). Direct preimage case analysis proves the fixed state has no other predecessor. Four explicit certificates for c=1,2,3,4+ give distinct full cycles and exact closure; c>=4 universality follows because every listed first coordinate >=-4 so max(0,c+x)-c=x along the orbit. Independently reconstructed all four complete cycle sequences and checked every transition and distinctness at c=1,2,3,4,5,9,100, periods 18,19,22,24; independently checked exact first-hit N²+2N+2 for N=2..20. Finite checks supplement exhaustive all-Z² branch reasoning and symbolic parameter argument.

## originality

PASS

Best-of-knowledge: Willox 2026 defines this ultradiscrete predator–prey family and describes unbalanced periodic examples, but no verified broader statement provides the all-integer balanced family global basin and four exact period values. Ohmori–Yamazaki max-plus equations are different (second coordinate resets rather than carries old y), so published period tables do not directly cover this recurrence. The inaccessible 2007 paper and unindexed related results remain explicit priority risks, not automatic failure.

## value

PASS

The balanced equality line of the published ultradiscrete predator–prey family is mathematically natural, and a global finite-time attracting-cycle classification for all Z² is a nontrivial infinite-state result. The exact transition periods and c>=4 plateau, together with quadratic unbounded transient times, distinguish attractor rigidity from slow capture in a way useful for future analysis.

The dated certificate retains the supplied scientific assessment, sources and limitations.
