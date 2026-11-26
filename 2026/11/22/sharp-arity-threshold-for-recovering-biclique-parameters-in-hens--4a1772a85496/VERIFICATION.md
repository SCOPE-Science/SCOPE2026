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

Every admissible finite graph diagram embeds in H_m by universality; homogeneity moves the embedded named base back onto A. An isomorphism fixing each named vertex and each corresponding tuple coordinate extends to an automorphism, so the full ordered injective types are exactly the labelled admissible diagrams, with no quotient by shore or tuple permutations. Since the old clique number is two, all diagrams are admissible with s<m−2, including the empty tuple. At r=m−2 a forbidden clique must use all r new vertices and an old adjacent pair, one from each part. It exists iff the new vertices form a clique and each old part contains a vertex with all-one incidence to the new clique. Counting incidence assignments on the two parts independently gives (q^a−h^a)(q^b−h^b); this counts a whole forbidden diagram once, regardless of how many old adjacent pairs witness it. Fix n from t_1=2^n (r>=2). Subtracting the corrections at (a+1,b−1) and (a,b) by expanding the cross terms gives (q−h)(qh)^a(q^(b−a−1)−h^(b−a−1)), strictly positive for b−a>=2 because q−h=1. Thus t_r strictly decreases along distinct steps toward balance. No shorter prefix separates K_{1,n−1} from K_{2,n−2} for n>=4; n=2,3 have unique positive unordered splits. The ambient is fixed throughout. Homogeneity makes every higher numerical count invariant under base isomorphism, with no canonical renaming required.

## originality

PASS

The supported distinct claim is numerical recovery of the two positive part sizes at their first detecting tuple arity m−2, uniformly in fixed H_m, with exact spacing under balancing. Finite-extension admissibility, unary counts, and (for m>=5) the two-type invisibility of these bases have documented coverage. Same-day coverage of pieces does not order the records or give the later-arity correction and inverse result.

## value

PASS

Numerical tuple-type totals are natural invariants of pointwise named finite bases, and a biclique is the first family here with fixed clique number two but varying internal geometry at a fixed size. The theorem determines precisely when that geometry first becomes detectable from totals alone, gives quantitative separation between successive unordered sizes, and proves uniform impossibility below the threshold. The benign low-arity formula itself is routine; the value is the exact inverse boundary and spacing, potentially useful when comparing or calibrating reconstruction from finite extension counts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
