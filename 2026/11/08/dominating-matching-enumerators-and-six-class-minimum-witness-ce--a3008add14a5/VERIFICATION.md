---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-14.md",
      "INDEPENDENT_AUDIT_2026-11-14.json"
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

One matching edge dominates at most six graph vertices: gamma_pr=2ceil(n/3), attained by every-third rungs. Column symbols 0,L,R,V encode each matching uniquely and ensure exact domination via length-three windows. Independently reconstructed 34 compatible pair states and 101 transitions, including cost potential yielding 44 zero, 24 unit, 29 double, 4 quadruple transitions. Zero-cost strongly connected components are only 3- and 6-cycles, hence D=(1-x^3)(1-x^6). Trace coefficients of defects 0,1,2 matched all displayed rational forms through n=103 using independent exact transfer/rational-recurrence computation. Since rational numerator after D^j clearing has respective degree <=33,67,101, coefficient agreement through 103 is exhaustive finite polynomial identity verification for all n, not mere extrapolation. A separate brute matching enumeration for n=3..8 corroborated Q_n and min counts. Formula counts matchings and not necessarily distinct vertex sets.

## originality

PASS

Earlier 2026-10-26 paper provides the n=2 mod 3 minimum paired-dominating vertex set count and proves unique matching there, hence that residue-class formula is old. It does not supply the n=0 or n=1 mod 3 matching-witness counts, the four-degree quasi-polynomial or full all-cardinality transfer enumerator. Ordinary matching, maximal matching and dominating-vertex polynomials are different invariants. Best-of-knowledge new full classification.

## value

PASS

Full cardinality enumerator of dominating matching witnesses is a natural graph-counting invariant, and the exact minimum-count six-residue family includes nontrivial quartic classes. The witness-versus-set distinction is mathematically important; the remaining congruence classes beyond n=2 mod3 are not mechanically determined by the older result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
