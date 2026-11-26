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

With the stated shift convention and gh(hg)^−1, the lamp coordinate is (I−σ^t)x+(σ^s−I)y and the top coordinate is zero. For fixed s,t its image is the subgroup of vectors summing to zero per coset of H=<s,t>: edge differences cancel there, and along a spanning tree of each coset they generate every zero-sum vector by moving each leaf value to the root. This does not divide in A. The image has m^(N−[B:H]) elements, so each nonempty fiber has m^(N+[B:H]) elements. This includes the trivial top group. For C_n, grouping by gcd(n,s,t) gives the Jordan count by inclusion–exclusion, and the generating pair (1,0) gives the entire augmentation kernel. For prime n only the d=1 summand survives on nonzero targets in that kernel. For composite n a difference at positions 0,d with 1<d<n and d|n has additional strictly positive summands that the difference at 0,1 cannot have. The n=10 contributions 147456, 98304 and 98304 agree with the two displayed fiber levels. The finite checker and its output were inspected, not rerun; they supplement, rather than prove, the group-uniform argument.

## originality

FAIL

Erovenko–Sury prove the fixed-top kernel size for every ordered top pair, not just the summed identity fiber. This already determines the size of the fixed-top image, and elementary coset cancellation places it in the coset-zero-sum subgroup of exactly that size. Equality and every nonempty fiber size follow immediately. The original supplies a self-contained direct image proof, but not a scientifically distinct target law under this comparison. This is an implication of inspected primary evidence, not a failure based on the inaccessible Riedl article.

## value

FAIL

The full word distribution is a natural invariant, but in this setting it is mechanically determined by the existing fixed-top kernel calculation and coset cancellation. The cyclic equal-fiber criterion follows by the divisor grouping and choosing two support positions, and the n=10 coincidence is an arithmetic illustration of that sum. Neither supplies a distinct surviving classification warranting repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
