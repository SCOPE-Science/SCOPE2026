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

For the two transfer eigenvalues alpha and -t alpha, the occupied diagonal projector weights are t/(1+t) and 1/(1+t). Inserting one, two, or three projectors in the trace gives the products of occupied matrix elements at the corresponding cyclic gaps, divided by the same ring partition function. Expanding the centered moment with these probabilities reproduces its exact numerator factorization. In the open interval (0,1) its sign is the opposite of H_m. H_m starts at -1 and ends at 0 with slope 4-6m for even m and 2-2m for odd m; this gives a positive-to-negative crossing in fugacity. At one half, with a=2^-m, even m gives H_m/a at least 1/4-1/8-1/32-3/512>0; for odd m, the negative constant and negative quadratic-in-a contribution to H_m dominate its positive cubic term. Uniform C^1 convergence to 2t-1 on [2/5,3/5] gives eventual uniqueness and simplicity on that interval. The midpoint residual first bounds the root displacement by O(2^-m); there |((-t)^m)'|=O(m 2^-m), so the mean-value formula gives t_m=1/2-(-1)^m 2^-m/8+O(m 4^-m). The fugacity map has derivative 12 there, yielding the stated amplitude, sign and error.

## originality

PASS

The independent-set/matching correspondence and cycle transfer framework are known. The distinct supported claim is the connected three-site sign crossing and the exact parity-dependent displacement for the specified nearly equispaced marked cycle. The closest distinct inspected corpus work concerns open paths, whose conditional structure at the middle site does not carry over to a cycle. None of the inspected available statements supplies or implies this finite-ring sign and root asymptotic.

## value

PASS

The triple has the closest possible evenly spaced gaps for these ring sizes, a natural finite-size comparison. Its low-to-high fugacity reversal, alternating correction at fixed fugacity, and explicit opposite-side root law quantify a genuine cyclic effect of a third connected statistic beyond the partition or pair functions. Knowing the coefficient and error resolves which side of two the boundary lies on, rather than just exhibiting a decaying correlation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
