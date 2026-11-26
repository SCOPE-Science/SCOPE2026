---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Each outgoing binary carry lowers the digit-sum increment by one, so the increment is h-K_t. If K_t<=h, no carry can travel the h+1 or more positions to another 1-bit of the shift. Conversely, for a tuple of runs starting at the shift's 1-bits with total j<=h, the tested windows (ones followed by a terminating zero) are disjoint and no carry interacts. The joint weight of any such tuple is 2^(-h-j); stars and bars gives the claimed low-carry profile. For fixed t and j the event is determined by the bits through e_h+j: any carry surviving this position must have already used at least j+1 carries. Fair independent bits on that finite prefix give the natural density by uniform residues. The negative-binomial sum is the fair-coin probability of at least h successes among 2h tosses; symmetry and Stirling give the two stated bias formulas.

## originality

FAIL

Verified Resultary coverage: the finite-gap shielding theorem in 2fd2f492b4f5 proves the entire profile under a weaker gap condition and gives an explicit first-contact correction. Setting its gap-count correction to zero yields the frozen statement exactly, not merely a similar bias or general computability. This is a finding of mathematical coverage by a distinct record, not an inference of authorship or priority from path dates.

## value

FAIL

The low-carry tail is a motivated exact invariant and would be useful as an exact benchmark. This particular gap restriction and the asymptotic bias, however, add no new case or mechanism beyond finite-gap shielding: they discard the contact correction and sum an already determined table. The frozen result supplies no independent valuable remainder.

The dated certificate retains the supplied scientific assessment, sources and limitations.
