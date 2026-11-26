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

In Z[x]/(x³−x²−1), x⁷=1+2(1+x+2x²), so B mod 2 is 1+x and (B+B²) mod 2 is x+x². Applied to the cyclic parity word (1,1,1,0,1,0,0), their two scalar parity rows are (0,0,1,1,1,0,1) and (0,1,1,1,0,1,0). Writing M^(7·2^r)=I+2^(r+1)D_r, successive squaring gives D_r≡B+B² mod 2 for r≥1; odd multiples preserve the leading term, including r=0. Only classes 2 and 3 pass both rows. Each failing row supplies the counterexample t−s=1 or 2 at s=0. The exact valuation gives finite bijections from t mod 2^(k−1) onto the appropriate parity class mod 2^k, also at k=1. The seven-letter nonconstant parity period forces any period to be a multiple of seven, and the difference law at j=2 forces the stated dyadic factor. Completing the compatible quotient bijections gives the asserted 2-adic isometries.

## originality

FAIL

A distinct indexed record establishes the same two exact isometries, sections and sharp period after an index shift, independently of reliance on the assigned statement in the inspected passages. Even the assigned exclusivity addendum follows immediately from its complete modulo-eight slice table. The matched records bear the same calendar date, so this is verified scientific coverage, not a conclusion about priority or who proved it first. No distinct valuable remainder was found to repair.

## value

FAIL

Exact two-adic coordinate charts would be useful structural information by themselves, but this record adds no independently useful exact fact to the covered theorem: the only apparent further assertion, exclusivity, is a direct four-entry row comparison in the overlapping result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
