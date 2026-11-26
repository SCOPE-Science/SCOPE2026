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

For each feasible rank of the modified bond, the exchangeability of the other labels makes their relative permutation uniform conditional on rank. In the homogeneous experiment the rank-r edge is uniform, its conditional count law is independent of its identity by rotation, and the mixture is the unconditioned law. This proves the full-law invariance, not only its mean. Conditional on the first bond, or on the two disjoint forced first bonds, delete their occupied vertices: the remaining path lengths are n-2, or d-2 and n-d-2, with zero lengths allowed. First-edge splitting of a path yields (m-1)F_m=(m-1)+2 sum_{j=0}^{m-2}F_j. For H(z)=G(z)/z this gives H'-2zH/(1-z)=1/(1-z)^2, H(0)=0, verifying the generating function and coefficient normalization. Subtracting the two path formulas, the affine terms cancel exactly by 1-2a=e^(-2). The truncated exponential series remainder is the stated integral, with absolute beta integral 1/[m(m+1)] before the e^(-2x) weight. The sign is strictly (-1)^m; the normalized factor is E[e^(-2X)] for X~Beta(2,m), with 0 <= 1-E[e^(-2X)] <= 4/(m+2). This gives the leading equivalent and both strict displayed bounds. The word 'sharp' should refer to the leading asymptotic, not optimality of the lower constant: Jensen already gives E[e^(-2X)] >= exp(-4/3) for all m>=1. Parity applies after the fixed-d infinite-cycle limit, not at arbitrary finite n. Read verification_pair_impurities.py and the recorded bounded checks in VERIFICATION.md; did not run the frozen script. Its floating quadrature is only a sanity check; the exact series proof establishes the tail.

## originality

FAIL

The principal contribution, the controlled two-seed signed profile and its factorial equivalent, is mathematically covered by a distinct indexed record on parity-optimal spacing with exactly the same intervention and scope. The displayed date of that comparison record is later than the frozen record; this is a finding of current equivalent coverage, not a finding that it was discovered first or that it is the same record. The unmatched single-bond statement is an elementary rank-exchangeability lemma for any edge-transitive graph and does not supply a substantive independent remainder for this claim.

## value

PASS

The principal two-seed response addresses a natural intervention, gives an exact finite-size formula, and explains the strict sign reversal and a quantified spatial decay that an unconditioned occupancy correlation cannot supply. This is meaningful mathematically but is not a surviving new claim after the comparison. The elementary one-bond symmetry observation alone does not warrant a repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
