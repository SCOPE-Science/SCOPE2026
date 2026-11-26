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

A queried consecutive triple can be labelled with the forbidden factor. For 000 any other queried support extends by filling unqueried positions with ones. For 010, consider gaps between successive prescribed zeros. Fill unused positions with ones except for a single unused slot between neighboring prescribed zeros at distance two, which is filled with zero. A one-slot gap already prescribed to be one would give a queried consecutive triple. Thus every positive run of ones between zeros has length at least two and no 010 occurs. Complement gives the other Class A factors. For 100, the label 1 at a queried i preceding a queried zero pair at j,j+1 forces 100, by taking the last one before j. Conversely after the first prescribed one fill unused positions with one, and before it fill unused positions with zero. A forbidden occurrence would require two adjacent prescribed zeros after that first one. Reversal and complement provide all four Class B factors. Class A support masks avoid runs of three ones, giving the stated recurrence and the extremizer (110) repeated and truncated. For Class B, after fixing the least selected coordinate the later coordinates form an independent set on a path. Summing size-k counts over the least coordinate gives binom(n−k+2,k) for k≥2 and the stated dimension, with n=0 separate. Word counts equal support counts for 000/111 by complement of a support mask, and for Class B by counting the suffix after the first one versus independent later positions in a support. Independently, the longest-prefix-suffix three-state automaton for 010, with transitions 0->states (1,0), 1->(1,2), and 2->(forbidden,0) under the two input bits, gives (1+t²)/(1−2t+t²−t³). Subtracting from the Class A face series at z=1 yields the claimed defect. Each reciprocal denominator has positive coefficients at every degree (for the second use the geometric expansion in t³/(1−t)²), so strictness starts exactly at n=4. An independently written automaton enumerates extendibility of all partial assignments at n=0..9, verifies all support predicates and coefficients and reproduces defect values 0,0,0,0,1,3,7,16,35,74. This is a check, not the basis of the all-length proof.

## originality

PASS

The distinct supported contribution is the complete comparison of the eight factors, especially the nontrivial alternating-factor support characterization and the resulting same-support/different-extremality theorem. Class B's predicates, polynomials and VC dimensions are covered by the distinct same-day 001 result and reversal/complement, and its extremality is implied using the already-known word count. Do not give separate originality credit to those claims, ordinary avoidance counts or the immediate downward-closed constant-pattern cases. No shared-date order or unrestricted priority is inferred.

## value

PASS

The classification addresses a natural interaction between finite-word avoidance and coordinate VC shattering. It gives every admissible query support, not just global size or VC dimension, and shows that two factor-avoidance languages with identical full shattered-support complexes can behave differently in the equality case of Sauer–Shelah at every length from four onward. That structural comparison is useful independently of the already-known avoidance counts or Class B census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
