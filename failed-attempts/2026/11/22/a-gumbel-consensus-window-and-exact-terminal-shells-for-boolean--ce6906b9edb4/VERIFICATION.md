---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

Exact-length walks reach precisely the positions at compatible parity and distance at most t. The two target-parity distance-to-support maxima differ by one because distance changes by at most one across an edge and has opposite parities on the two classes. First saturation is therefore R−1; full and empty target classes stay full and empty while the classes swap. This yields the four recurrent states and the maximum of the two support clocks. An antipodal singleton is the only way to have R=d; a nonsingleton with R=d−1 lies in a Hamming-1 star. Each qualifying pair lies in two stars and a larger support lies in just one, giving U and both max-clock counts. A fresh cycle census on all 256 d=3 states gave (4,140,112); exhaustive parity censuses gave (N,U)=(4,10),(8,64),(16,336) for d=3,4,5. For the random claim, ordered k-tuples with an overlapping neighborhood number O_k(2^{d(k−1)}d²), and the union of their neighborhoods loses at most 2 binom(k,2) from kd. Their contribution is o(1); the disjoint tuples give the Poisson factorial moments. At two steps each predecessor set has size 1+binom(d,2); a union bound suffices. Empty seed parity classes and initial periodicity are negligible. For fixed p below or above 1/2, the second-moment or first-moment bound respectively gives the stated law. Inspected the three frozen checkers without executing them.

## originality

FAIL

Different one-step dynamics do not establish independence from the exact prior results. An iterate reduction and the prior Hamming-star census cover the main deterministic calculation. A first-image complement gives exact overlap with a stronger public same-date result for the stochastic centerpiece. The remaining steps to separate shells or obtain the two-update law are direct parity, subtraction and a predecessor union bound. No strict publication order is asserted within the common date.

## value

FAIL

Typical versus worst-case dynamics is a useful question and the combined record is a convenient exposition. As a distinct result the shell formulas reuse previously enumerated terminal obstructions, and the critical law uses an identical previously analyzed public observable. Relabeling, subtracting cumulative counts and a two-step union bound leave no substantive independently useful unknown invariant or boundary in this package.

The dated certificate retains the supplied scientific assessment, sources and limitations.
