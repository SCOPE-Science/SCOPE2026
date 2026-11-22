---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

An exact star-edge parity reduction maps all 21 edge frequencies onto 15 internal-edge frequencies with 64 lifts, while matching 2640 degree-three regular orientations. The independent 2^21 orientation-cube integer transform was recomputed from the actual edge definition and agreed at every listed histogram bin: 1,543,168 zeros, 553,984 nonzero, min |W|16, max2640. Independent Walsh transform of the nonzero-support mask yielded full kernel absolute sum 91,381,760, divided by 2^21 =11155/256; the 15D quotient form is 1,427,840/32768. Translation conjugacy averaging proves optimality of this Fourier projection among all projections, not just translation-equivariant ones. Both source checker scripts and its finite certificate inspected. The computation exhausts the entire specified finite domain.

## originality

FAIL

A separate published Resultary record gives literally the same 2640 regular K7 tournament object, absolute full Walsh histogram (shown divided by the same factor 64), rank553984, min multiplier16, and sharp endpoint norm11155/256. It is equivalent under globally complemented orientation-bit conventions; the current record presents no distinct stronger claim. Both copies appear in the same published snapshot (2026-11-17T02:18:15Z), so priority between contemporaneous copies is not asserted, but uniqueness/originality of this exact finding cannot be accepted.

## value

FAIL

The exact regular-seven tournament Fourier and optimal-projection invariants are intrinsically mathematically motivated; however, this package reproduces an already published complete evaluated spectrum and endpoint constant without a new mathematical distinction, so its claimed additional scientific value fails the bar against known-table recomputation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
