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

Independently reproduced every size stratum and all five universality tests with /workspace/branches/replay_order16.py; read the submitted checkers but did not execute them. In the replay a pair of subsets of reciprocal sizes tiles iff its nonzero difference masks are disjoint: precisely such an intersection would give a repeated sum, and there are 16 sums. I grouped every zero-containing set of each divisor size by that difference mask, and intersected the exact Fourier-zero masks within each permissible complement bucket and then across permissible buckets. Evaluating in the basis 1,ζ,…,ζ^(E/2−1) with ζ^(E/2)=−1 gives the exact zero criterion (E=2 works too). Each possible spectrum translates to one containing 0; test its entire nonzero difference mask against the common Fourier-zero mask, checking all subgroups separately by difference closure. Translating complements changes each Fourier coefficient only by a phase, so no nonnormalized complement can change the mask. Uniformly over labeled tiles of size k, anchoring accounts for a fraction k/16, by double-counting a tile and a chosen element, also for periodic tiles. Replay produced totals (795,1611,2155,3147,4747) and obstruction totals (764,1056,1168,896,0), with all size columns as in RESULT.md. The cyclic example also checks: the alternating parity complements have all nonzero restricted character differences of {0,…,7} orthogonal, but difference 8 in the only order-eight dual subgroup restricts trivially. This proves the bounded order-16 classification; no extrapolation or formal proof claim.

## originality

PASS

The full size-resolved ordinary tile baseline in all five groups is already available under anchoring, and every universal/subgroup count in the Z4² row exactly overlaps record 5. These are not credited as new. The supported distinct result is the joint census outside that row: exact obstruction size profiles for Z16, Z8×Z2 and Z4×Z2² and the subgroup-versus-arbitrary comparison across types, including the elementary abelian zero row. Cyclic universal existence is credited to the prior cyclic framework, not identified as an addition.

## value

PASS

A complete first comparably small multi-type cutoff for common Fourier bases tests a natural restriction: are simultaneous spectra still possible when the frequencies must form a subgroup coset? The exact profiles distinguish a common basis from a common quotient transversal, quantify how severely they diverge, and expose the elementary-abelian contrast, including abundant obstructions even in the cyclic group with prior existence. The value lies in the exact obstruction data across types, not in recomputing known tile counts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
