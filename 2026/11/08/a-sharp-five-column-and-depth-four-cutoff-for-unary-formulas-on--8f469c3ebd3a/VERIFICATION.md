---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
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

A 3-by-m Boolean one-letter bimodal frame maps surjectively by the 3-bit word of each column to a support quotient H_S, preserving and reflecting both row and column successor sets; hence every valuation is represented by one of 255 nonempty supports S subset {0,1}^3, with 3072 pointed states. Finite depth signature tau_(d+1)=(tau_d,sets of horizontal and vertical tau_d successor types) is exactly modal depth equivalence by characteristic-formula induction. I independently constructed and refined all 3072 states in a separate program: depth 3 counts by support-cap 1..8 are [4,28,88,136,140,140,140,140], depth 4 [4,28,88,146,164,164,164,164], and depth 5 identical. This fixed point proves no further depth distinctions. Every type admits finite-depth characteristic formula, so exactly 2^N_m formula-equivalence classes; strict depth3/4 and cap4/5 counts prove sharpness.

## originality

PASS

The standard bounded-morphism and bisimulation machinery is credited; the exact 164 pointed types, depth-four optimality, five-column realization bound, and all-width classification for a natural fixed-three-row S5 product family were not stated in the inspected qualitative product modal logic work or any non-self indexed table. Best-of-knowledge with possible specialist combinatorial tables.

## value

PASS

A natural one-variable quotient algebra of the product of equivalence frames is fully classified by a sharp finite semantic bound. Exact finite column/depth thresholds are useful model-theoretic information; support compression proves a genuine all-width result from finite computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
