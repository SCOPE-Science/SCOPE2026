---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

Trace of alpha^n in the etale cubic Z[t]/(t^3-t-1) has perfect pairing modulo 3. Direct alpha^13=7+12alpha+9alpha^2=1+3beta with beta a 3-adic unit proves exact unit and sequence period. The branch derivatives mod3 distinguish nine 3-adic isometries: three reducing to 0, two to 1, four to 2. Four remaining branches are fixed modulo 9 at 3,2,5,7; hence residues 0,1,8 mod9 have no singular contribution and sharp minima follow. Independent recurrence enumeration for k=1..5 reproduced (4,3,6) at k=1 and (3,2,4) thereafter, not a substitute for all-k proof.

## originality

PASS

Earlier Perrin valuation theorem of 2026-11-02 gives all 3-adic valuation levels but only distinguishes zero from unit values, not the unit residue images or exact per-residue fiber minima. Published OEIS A104217 periods 13,39,117 do not determine the multiplicities. No inspected source implies the full minimum-frequency theorem.

## value

PASS

A sharp residue-by-residue coverage theorem for a classical cubic recurrence is a natural local-distribution invariant beyond known periods and valuation densities, with explicit exceptional vs regular 3-adic branches; independently useful for modular recurrence questions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
