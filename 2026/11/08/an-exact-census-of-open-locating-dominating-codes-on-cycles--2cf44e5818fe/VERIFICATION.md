---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

PASS. For OLD codes on ordinary labelled C_n, the definition demands all open neighborhoods have nonempty distinct traces, including code vertices. In C_n except n=4 these conditions are equivalent to omitting no pair at cyclic differences 2 or 4: distance 2 forbidden by domination; equal singleton traces from centers distance 2 iff their two nonshared neighbors distance 4 are omitted. C_3 is directly valid, C_4 has equal open twin neighborhoods regardless of set. The forbidden-pair auxiliary graph is C_n^2 when n odd (multiplication by 2 invertible) or two disjoint C_{n/2}^2 for even n≥6. For m-cycle squares every k-set has gaps at least 3 and count (m/k)*binom(m-2k-1,k-1), so polynomial A_m and P_n(z)=z^n A_n(z^-1) or z^n A_{n/2}(z^-1)^2 follows; all size supports follow by subsets of independent sets and the minimum is n-floor(n/3) for odd and n-2floor(n/6) for even. The example C13 complement of {0,5,6,12} is a valid nine-code and corrects the overly broad congruence-1-mod-3 conjecture. Independent direct neighborhood-code enumeration of every subset of C_3..C_14 (32760 masks) matched the polynomial. Proof, not finite testing, establishes all n.

## originality

PASS

PASS, with residual risk of a conventional independence-polynomial specialization in graph-coding literature. Raza 2021 gives the cycle minimum conjectural extra unit for all lengths 1 mod 3, while the submitted complete labelled code-size polynomial refines and corrects it. Argiroffo et al. 2019 present a scalar OLD optimum assertion, not an all-coefficients polynomial. Standard cycle-square independence counting is preexisting but the all-vertex OLD trace equivalence and consequent parity factorization/nonexistence at C4 are specific, not identical to the locating-total or error-detecting variants returned in search.

## value

PASS

PASS. OLD sensor-code placement on basic cycle graphs is a natural invariant. The complete cardinality distribution, multiplicities of minima and the parity-dependent correction to a published conjecture provide an exact reusable classification, beyond merely copying the standard cyclic gap count. No general-graph classification is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
