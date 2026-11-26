---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

Increasing paths of length three give exactly (abc,bcd,abg+adf+ecd) in positions (14,25,15); the higher three input entries contribute q³ freely. For (A,B)≠(0,0) one chooses b,c nonzero and solves uniquely for a,d; the last output is a nonzero linear functional with q² lifts. At A=B=0, there are H=q⁴−(q−1)²(q²−1) eligible quadruples. A nonzero last functional occurs in three disjoint cases: ad≠0 and bc=0, or ad=0 with ab≠0 (forcing d=c=0), or ad=0 with cd≠0 (forcing a=b=0). They give L=(q−1)²(2q+1) quadruples. A nonzero C has q⁵L lifts; at zero the count is q⁵[L+q(H−L)], as claimed. The counts are positive and strictly increasing in the stated order for q≥2, and with target multiplicities q(q²−1), q−1, 1 their sum is q¹⁰. In characteristic three the binomial identity holds since I commutes with X. The filtration 1+N₅^i bounds the lower central series in one direction by commutator degree, and elementary matrix commutators generate each permitted superdiagonal in the other; thus γ₃=1+N₅³.

## originality

FAIL

There is verified, exact coverage in the distinct indexed Near-top matrix-power fibers theorem. At exponent m=3 its domain, all three prescribed-target cases, positivity, support and characteristic-three group scope are identical. This is a coverage decision, not an assertion that the broader record was first or that either proof was copied. Both have the same publication date; the broader text describes m=3 as recovery of an existing calculation and does not claim it as new, but this does not establish publication order or independently identify that calculation's provenance.

## value

FAIL

The root census is mathematically meaningful at this natural cube-image boundary, and the proof is a convenient small worked case. As a standalone exact finding against the available corpus, however, it supplies no independent invariant or refinement beyond a direct parameter specialization of the broader census. The enhanced central fibers, zero probability and cube-word interpretation are all already obtained from it.

The dated certificate retains the supplied scientific assessment, sources and limitations.
