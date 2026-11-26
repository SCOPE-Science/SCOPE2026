---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Rook distance is two between cells in distinct rows and columns, so the forbidden triple is an induced two-edge path, equivalently a selected incidence edge whose endpoints both have selected degree >=2. Requiring a degree-one endpoint on every selected edge forces each nontrivial incidence component to be a star. A spanning star forest is maximal because any newly added edge would join two already used vertices. With an unused row, all columns must be used, and any column center or singleton-edge endpoint would permit a legal addition. Hence every column is a leaf at a row center of degree >=2, and conversely any addition to this configuration destroys the star-forest property. The transposed case is disjoint. The exponential generating terms are exactly those for labeled isolated selected edges and the two orientations of stars with >=2 edges. The nonspanning terms choose the used centers and assign all opposite-side labels with each fiber of size >=2, matching the T counts with no symmetry multiplier missing. For m<=n the spanning forests have c in [2,m] components and m+n-c edges. Every such c is realized by c-2 isolated selected edges and a pair of oppositely centered stars on the remaining at-least-2 by at-least-2 board. The nonspanning classes have sizes m or n; a full column supplies m. The proof covers m=n and m=2, including coincident exponents in the sum. Independent replay checked forbidden triples, one-cell maximality, and an alternative labeled-component recursion on seven boards; e.g. M_2,5=5z^2+32z^5, M_3,5=5z^3+213z^5+15z^6, M_4,4=104z^4+144z^5+16z^6.

## originality

FAIL

Two distinct earlier-dated Resultary records each give the same complete labeled maximal-set polynomial and exact support; a third exact indexed match uses the name maximal induced cluster sets. The correction terms differ in notation only. Prior primary endpoint and game results alone would not give the full census. The catalog dates establish displayed order, not discovery priority or dependence.

## value

FAIL

A maximal-set spectrum and labeled multiplicity polynomial are natural refinements of the earlier minimum and maximum parameters. But this frozen finding adds no independently useful new invariant or structural classification to the complete indexed enumeration. Its potentially long gap is precisely the complement of the already stated support, not a separate surviving claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
