---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

In the (1,x) basis over k[y]/(y^m), the t-th power has both diagonal entries f^t and its sole off-diagonal entry t f^(t-1) g. Lift f and g to k[[y]], using y^m for a zero element; reduction recovers the actual multiplication matrix, also for t=1 and f=0. If t vanishes in k the two Smith exponents are t alpha. Otherwise the smaller is min(t alpha,(t-1)alpha+beta) and their sum is 2t alpha. This follows either by eliminating the other entries using a pivot of least valuation, or by the entry ideal and determinant. Reduction turns each exponent d into rank max(m-d,0); this gives exactly both branches of (1), without needing any roots of units. Taking second differences of the ranks gives the block counts; independent counting of f and g in their valuation layers proves (3) and yields q^(2m-1) in total. The bound at m+1 follows from the radical powers, while a^m=m x f^(m-1)g. The witnesses x+y if m is nonzero in k and y otherwise attain the respective bounds. At m=3, (alpha,beta)=(1,0) gives (4,2) unless characteristic 3; (2,0) gives (3,2,1) unless characteristic 2, with the stated weights.

## originality

FAIL

The complete finite-field partition census and its valuation mechanism are demonstrably covered by a distinct indexed result, Complete Jordan-type distribution on k[x,y]/(x^2,y^n) over finite fields. Its nilpotent parts are exactly the elements in the frozen theorem. Its ranks agree after capping exponents, and removing the free scalar factor q gives the identical partition generating polynomial for the radical. It also yields the sharp index in positive characteristic. The characteristic-zero case adds no distinct census or rank phenomenon: the common expression for all relevant powers is the case p>m+1, in which none of the relevant integer multipliers vanishes, and the same Smith reduction works unchanged. This is an existing-coverage finding, not an attribution of earlier publication: the distinct indexed record is dated November 2, after the October 18 frozen record, and the evidence does not establish derivation or historical priority. The earlier Lefschetz and Jordan-type sources inspected do not provide the general valuation census.

## value

PASS

As a mathematical result, an all-element valuation-stratified census of this standard family is useful: it separates nonlinear partitions from the classical linear-form cases, exposes where prime divisibility changes the top block size, and permits exact enumeration without traversing the whole field-sized algebra. The result's intrinsic classification value does not resolve the duplicate-coverage issue or give this version distinct content.

The dated certificate retains the supplied scientific assessment, sources and limitations.
