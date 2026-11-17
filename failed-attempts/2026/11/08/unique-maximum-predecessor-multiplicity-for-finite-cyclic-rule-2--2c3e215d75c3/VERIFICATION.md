---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-14.md",
      "INDEPENDENT_AUDIT_2026-11-14.json"
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

The one-step indexed cyclic Rule-22 inverse fiber equals tr(M_y0...M_y(n-1)), including repeated positions at n=1,2. The homogeneous count 1+T_n follows from block charpoly t^3-t²-1. I checked actual integer certificate/proof scripts: simultaneous singular-value bounds exclude outputs containing >=4 ones; Perron residual powers 3,4,5 have Frobenius norms below 1 and hence bound long sparse words; exactly 15,250 sparse outputs at n<=24 are checked by integer transfer matrices. Independent direct evaluation of all 2^n inputs for n=1..12 corroborates maximum uniqueness and recurrence. This proves correctness; the decisive issue is earlier identical theorem, not mathematics. Nonzero targets can have zero preimages; that is included in comparison.

## originality

FAIL

A fully inspected earlier published theorem (2026-11-02) proves literally the same unique all-zero modal output for Rule22 cyclic indexed binary rings for every n>=3, with identical 1+T_n recurrence and a *stronger* global upper bound on every nonzero fiber. The submission extends only to trivial sizes n=1,2, which follow by checking at most four input words; it therefore offers no mathematically distinct global theorem.

## value

FAIL

The naturally meaningful maximal inverse-fiber count and unique target of Rule22 were already fully classified for all nondegenerate indexed rings n>=3 in a stronger published theorem. The only addition n=1,2 is a tiny direct calculation with at most four inputs, offering no substantively distinct invariant or motivated boundary theorem. Correctness and alternative spectral proof do not make covered science valuable as a new finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
