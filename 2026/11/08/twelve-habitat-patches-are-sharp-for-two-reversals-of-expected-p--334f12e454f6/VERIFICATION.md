---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

For every tree, F_T(p)=sum_j a_j(T)p^(j+1) follows from survival of all j+1 vertices on each unique path. Equal-order tree differences have p³(1-p) factors. Under t=p/(1-p), exact integer transformed coefficients and Descartes variations bound interior zeros. Independently regenerated every unlabeled tree with NetworkX graph atlas generator through n=11; tree counts for n=4..11 equal 2,3,6,11,23,47,106,235 and distinct distance-vector counts 2,3,6,11,23,45,104,215. All profile pairs have <=1 sign variation except a single n=11 pair with two; its residual 3p³+p²-3p+1 has discriminant -76 and sole real root <0. Independent direct breadth-first distance calculation for both 12-node witnesses gives (11,14,14,12,8,5,2) and (11,15,11,13,10,6,0), yielding D=p³(p-1)(2p-1)(p³+p²-1), with exactly two simple roots in (0,1). These finite checks exhaust the bounded lower domain; no claim made for all n>=12.

## originality

PASS

The expectation is p times the classical Wiener/Hosoya distance polynomial, so polynomial definition is not new. The sharp first order n=12 for two crossing comparisons is an exact non-implied comparative invariant of tree distance distributions; inspected prior Wiener-root literature studies individual polynomial roots rather than positive roots of pairwise differences.

## value

PASS

Sharp first finite order for two reversals in a natural stochastic habitat-connectivity ranking is mathematically motivated and requires an exhaustive all-small-tree obstruction plus explicit witness, not a textbook identity or arbitrary slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
