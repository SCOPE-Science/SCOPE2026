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

For a vertex pair the two arc totals are A and R-A, giving A(R-A)/R. Each edge pair at distance d contributes its product once for each vertex pair separated by deleting those two edges, giving d(n-d) occurrences. Expanding r_i=1+delta I_i gives the frozen expression with strictly positive placement coefficient delta^2/(n+k delta). In the spacing simplex each directed block length L contributes L(n-L), with an overall factor 1/2; the length-one terms ensure strict concavity, so only the simplex vertices minimize and they are all rotations of the clustered block. For maxima, each fixed block length has fixed sum and smoothing two differing integer lengths by one improves the quadratic unless all lengths differ by at most one. Floor placements attain every block bound simultaneously. The residues ell*n mod k repeat g times across the multiples of g, giving the claimed gcd correction. The contrast is positive since n-k>=2 and g>=1, giving a bracket at least 3(k^2-1)>0. Symmetric jump rates give uniform stationary weights and the Laplacian pseudoinverse gives K/n for stationary-target hitting time (zero for the starting target). Independent replay python3 -B /workspace/reproductions/5.py checks 16028 exact resistance cases with two different contrasts and 12 cases with all-target rational hitting-time systems; universal results follow from the algebra.

## originality

FAIL

A distinct earlier Resultary theorem proves the exact same binary placement energy and both equality classes, with the identical gcd term and in a broader count range. The weighted-cycle and continuous-time interpretation is distinct as wording but transfers that theorem using the arc identity, a quadratic expansion and the usual Kemeny identity. This is demonstrable coverage, not an inference from an inaccessible paper or a same-day listing.

## value

FAIL

A transport interpretation is useful exposition, but once the exact binary rearrangement and gcd values already exist, the residual is the direct expansion of the parallel-arc law and standard stationary-target identity. The quadratic contrast and both signs of the ordering are forced by that expansion; there is no independent unknown structural or transport invariant here. No surviving nonroutine repair was established.

The dated certificate retains the supplied scientific assessment, sources and limitations.
