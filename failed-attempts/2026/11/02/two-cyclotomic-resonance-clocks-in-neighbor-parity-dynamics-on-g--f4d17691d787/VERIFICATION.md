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

The loopless three-neighbor rule gives the displayed Laurent matrix B and det(B)=z^(−3)Φ₃Φ₅, with present factors of multiplicity e by the odd part of z^n−1. Locally at Φ₃, B²=(y+1)U with U invertible, and the unit off-diagonal entry and valuation-one determinant give local Smith form diag(1,Φ₃). Hence the nilpotent part has one length-2e chain per root. At Φ₅, B modulo Φ₅ is rank-one idempotent, so every positive power still has a unit entry and its determinant has valuation t in the DVR. Thus its nullity on the module of length e is min(t,e) per root; the nonzero-eigenvalue branch is invertible and this gives one size-e block per root. The kernel dimensions yield the stated preimage census by the Fitting decomposition and imply the attained strict stabilization time. The unit entry of B+I and det(B+I)=z^(−3)(z+1)²Φ₅ give the fixed-point exponent. For each t>0, clearing a monomial unit gives H_t, whose two polynomial Smith invariants yield both gcd dimensions. Its determinant is nonzero because the generic characteristic polynomial has nonzero cubic term in y for any constant candidate eigenvalue, so it has no constant root of unity. Return counts give primitive cycles by Möbius inversion; the examples use t=1,2, whose returning counts exhaust the recurrent sets there. An independent direct-column binary rank calculation matched 605 power cases and 1087 return cases, including even n, both resonances and the examples.

## originality

FAIL

The main theorem is directly covered by a distinct earlier indexed finding for the same open-neighbor parity map: the two zero-primary chain families, all entry populations, maximal transient time and reversibility are exact matches. Its source passage does not state the extra fixed-point or all-return formula. These extras are different outputs of the known explicit Laurent symbol, but applying the usual scalar Smith/gcd kernel rule to B+I or B^t+I is a direct standard deduction; the fixed-point factorization is one determinant, and the all-return procedure leaves the general invariant-factor computation unevaluated. This does not support the submitted claim of a distinct structural theorem.

## value

FAIL

The repeated-root transient partition is structurally useful but already covered, including all its stated population consequences. As an independent remainder the fixed-point count is a single determinant/gcd specialization of the known symbol, and the return census is the generic Smith calculation for each power rather than an additional structural result about periods. The two small examples do not make that routine remainder a substantive repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
