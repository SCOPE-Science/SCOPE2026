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

There are h=2r+s followers with r complete pairs and s singletons, and pair permutations and swaps identify exactly the configurations at each r. Moving one singleton follower to the grounded mate of another replaces two singleton pairs with a double and an empty pair, changing only the edge between the two affected follower coordinates. The grounded diagonal remains D=2m−2+μ. Independently of the derivative proof, write the trace as exp(−tD) times the exponential trace of the nonnegative follower adjacency. Each power trace counts closed walks and weakly decreases upon the edge deletion, with a strict decrease of two at power two. This proves strictness for every t>0, including when only a single edge is removed from a two-follower graph. All feasible r below floor(h/2) have two singletons, so the exchanges order all the orbits and yield precisely the stated leader compositions and counts. Positive definiteness follows from grounding a nonempty set in a connected graph. Both weighted heat integrals therefore yield the claimed optimizers. On pair antisymmetric, pair difference, and singleton difference modes the eigenvalues are a−1, a+1 and a; on the remaining two constants the displayed quotient matrix gives, for s=1, trace 2a−2r and radicand r²+1. The s=0 and h=1 spectra follow from their single remaining constant mode; equal entries in the eigenvalue list contribute their multiplicities additively. The finite checker was inspected without execution.

## originality

PASS

The supported distinct result is the pointwise-in-time strict hierarchy of every placement orbit for the family beyond the four-cycle, with its simultaneous screened, inverse-power and finite-horizon consequences. The full unscreened first-inverse hierarchy, not only the minimizer, overlaps the older balanced multipartite result for m≥3; the full m=2 heat-order boundary case overlaps two other cycle records. Neither overlap covers the all-time family theorem for m≥3, and no novelty is assigned to those overlapping pieces separately.

## value

PASS

The useful result is a single strict ranking for every transient horizon, not merely a recomputation of the optimal steady-state placement. The family has a natural one-edge exchange at fixed grounded degree and the theorem yields schedule-independent optimizer classes and exact values. The mechanism and the quantified all-time comparison are informative even when the p=1, μ=0 result and the C4 boundary case are set aside.

The dated certificate retains the supplied scientific assessment, sources and limitations.
