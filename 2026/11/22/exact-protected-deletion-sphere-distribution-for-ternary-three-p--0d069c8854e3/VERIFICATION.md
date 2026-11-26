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

Any two deletions at i<j agree iff all symbols on i..j are equal, by comparing the shifted substrings. Thus the leftmost index of a run suffices, and a new forbidden triple can occur only across the resulting gap. The applicable tests are w_(i−2)≠w_(i+1) and w_(i−1)≠w_(i+2); test only when the indices exist. For n≥4 the initial and final marks handle the two left and right positions, and a shift of a four-letter state marks the third index of the previous window after the fifth symbol is known. Every legal state is one of the six displayed equality patterns with six concrete labelings, and appending a legal symbol implements the marked transition without extra multiplicity. Independent replay python /workspace/branches/independent_math_1_4.py 3 recomputes the transfer on labeled contexts by deletion and equality of actual strings, checks lumpability to six states, verifies the numerator identity coefficientwise, and matches direct exhaustive legal-source/output counts through n=13. The rational identity is exact: for a six-state transfer the true denominator has degree ≤6 in z and the true numerator has degree ≤9 (using its adjugate and the three short-length terms), so with the displayed denominator the cross difference has z-degree ≤13; the replay checks coefficients through 27. The displayed numerator has degree six, giving the recurrence from n=7. Top-degree comparison uses m_(3h)=2h+1, m_(3h+1)=2h+1 and m_(3h+2)=2h+2: only P_(n−3) with shift +2 contributes in class 0, in class 1 the contributions are +P_(n−1), +uP_(n−2), +u²P_(n−3), −u²P_(n−4), and in class 2 the contributions are +uP_(n−2), +u²P_(n−3). The six initial polynomials (including deletion to the empty word at n=1) give the three positive leading-coefficient laws and hence exactly the maxima. Frozen verify.py was read, not executed.

## originality

PASS

The complete marked distribution and sharp optimizer counts concern source and receiver under the same strict three-palindrome constraint, with duplicate outputs collapsed. Closest checked work either counts the source language, changes the allowed patterns or counts a different deletion image. None covers the exact marked law under the theorem's hypotheses.

## value

PASS

The finite-type constraint and the protected distinct deletion degree are natural before enumeration: the degree measures surviving received-word diversity while retaining the same language. The complete length-dependent spectrum and sharp period-three optimizer multiplicities supply a reusable benchmark that total word counts and unrestricted run counts do not determine. No coding-optimality or capacity result follows by itself.

The dated certificate retains the supplied scientific assessment, sources and limitations.
