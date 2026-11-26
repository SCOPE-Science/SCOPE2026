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

Expanding the product of fixed-label signs gives the binomial formula with I_(n-j). Equivalently, Wick pairings of factors Z-1 at selected labels and Z+1 elsewhere contribute one per paired transposition and the correct signs at singleton labels. Substituting -Z gives reflection symmetry by (-1)^n; subtracting consecutive weights factors a 2 and gives W_(n,k)-W_(n,k+1)=2 W_(n-1,k). Central values are a_m=E[(Z²-1)^m] or its negative by odd reflection. Gaussian integration by parts on Z(Z²-1)^m gives a_(m+1)=2m(a_m+a_(m-1)); from (1,0,2) all later a_m are positive. Starting at (10,2,2,2,10), positive even rows force strictly decreasing odd rows and the consecutive central values a_m,-a_m. The odd sign split then forces the next even row to decrease and then increase strictly, with positive center a_(m+1). This proves the sharp minimum with exactly the stated weight ties. The n=1,2,3 rows are (1,-1), (2,0,2), (4,0,0,-4); binomial multiplicities give ranks 2 at both exceptional n. The empty frequency attains the trivial upper bound I_n on absolute values, so the condition number follows with unnormalized counting convolution. Inspected verify.py and check_output.txt; their recorded finite checks are not independent reruns or the all-order proof. Replay: RESULT.md equations (1), (5)–(7) and Proof 4–5.

## originality

PASS

The supported distinct result is the all-order positionwise Walsh sign, invertibility and sharp gap theorem for multiplicity-weighted involutions. The enumeration backbone and central sequence are known. Closest indexed permutation analogues do not specialize to this kernel.

## value

PASS

The fixed-point incidence distribution is a natural marginal of involutions. The exact two exceptional orders, parity-dependent sign split, and complete location of the least multiplier determine when recovery works and its sharp l2 cost, uniformly in dimension. The result concerns an optimized invariant, not merely an evaluation of the known central sequence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
