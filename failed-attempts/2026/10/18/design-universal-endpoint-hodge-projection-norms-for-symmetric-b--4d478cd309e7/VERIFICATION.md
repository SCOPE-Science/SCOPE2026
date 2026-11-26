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

For a current injection at p and extraction at B, the point–block mean drop is 1/(kv). The block equations invert on the separately centered subspaces with scalar denominator k^2-k+lambda=lambda v. The point correction is (k e_p-N e_B)/(lambda v), the block correction (N^T e_p-k e_B)/(lambda v), verifying the transfer-current formula. The negative entries are precisely the disjoint-endpoint cases with one or both cross incidences. Each one-cross class has (k-1)(k-lambda) edges and the two-cross class has (k-1)(lambda-1), by the pair-count identities. Signed column sum one gives the cut norm; the cycle norm changes only the absolute diagonal contribution R=(2v-1)/(kv) to 1-R. The difference of the norms is ((4-k)v-2)/(kv), with the stated strict sign. For a separate upper-bound check, the negative-mass bracket simplifies to 2k-2-2lambda+lambda(lambda+1)/k, less than 2k because lambda+1<=k. Since lambda v>k(k-1), the cut norm is strictly below 5, hence the cycle norm below 6. Substitution of projective-plane parameters gives the displayed expansions and shows sharpness along prime-power orders.

## originality

FAIL

A distinct Resultary record contains the same exact canonical norms for the identical class, the block-size reversal, and the same projective-plane specialization and limits; the strict upper bounds and the first asymptotic corrections follow directly from its formulas. This is demonstrable current coverage, not a finding of earlier priority. The same-day Steiner and crown records additionally cover the two boundary slices.

## value

FAIL

The invariant is well motivated and the absence of a transitivity hypothesis is useful. As a distinct contribution the record does not survive the exact all-design match: the sharp bounds, crossover and plane expansions are already stated or elementary consequences of its formulas. No separate valuable remainder is established.

The dated certificate retains the supplied scientific assessment, sources and limitations.
