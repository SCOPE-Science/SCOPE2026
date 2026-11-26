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

The common coordinates on the two residual vertex cells, together with the two distinguished endpoints, describe the exact rank-four image: x0, x1, and the two shore sums are freely specifiable throughout the stated domain. Independently use image coordinates (s,w,t,p), where s is the sum of the two endpoint coordinates, w and t are the residual shore values, and p is the first endpoint. The update is (s, beta*t, s+alpha*w, p+s+beta*t). For beta=0 the image restriction has rank 2 or 3 as alpha=0 or 1, its square has rank 2, and the stable restriction swaps the two endpoint coordinates. For (alpha,beta)=(0,1) the rank drops from 3 to 2 and the stable restriction is the identity. For (1,1), the iterates of M+I on (1,0,0,0) are (0,0,1,1), (0,1,1,1), (0,0,0,1), then zero; the four chain vectors are independent. Translating the image ranks to whole-space powers gives the displayed zero blocks and sharp nilpotent entry times. The fixed-space dimensions of the unipotent blocks give all least-period counts, including 12 states on three four-cycles in the odd–odd case. The nilpotent kernels give H(t)=2^(N-rank(F^t)+r), and projection onto the invertible summand gives d*2^(N-r) states in each length-d orbit's basin, so the uniformity is for orbits of equal length. The smallest admissible sizes keep the four cells nonempty and all block counts nonnegative. The unedited map squares to zero on the part-constant image when either shore is even. The attached verification/verify.py and verification/verify_output.txt were inspected, not executed; the recorded finite check is consistent with 110 rank cases and 36 exhaustive cases and is not needed for the all-size proof.

## originality

PASS

The supported distinction is the complete parity-dependent Jordan and temporal census for one added internal edge in a biclique under synchronous open-neighbor XOR. Related defect records share the quotient strategy but have different operators and conclusions; common Fitting theory and the intact-graph census are antecedents, not new claims.

## value

PASS

An elementary local perturbation of a standard graph family turns nilpotent dynamics into recurrence, and in the odd–odd family creates period four absent in the intact graph. The full Jordan table separates phenomena that a period list or characteristic polynomial would not resolve and gives exact finite basins and transient populations uniformly at all admissible sizes. The four-cell method is simple, but the parity-sensitive defect classification is a natural exact benchmark rather than a selected small example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
