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

Let U and V be the images, T=U∩V and W=U+V. The four relations are equivalent to both operators killing W. Once U,V are prescribed, the maps are uniquely determined by two independent surjections E/W→U,V, counted by S_q(d,r)S_q(d,s). Count the images by choosing W, then U≤W, then T≤U; the eligible V/T are complements of U/T in W/T. The complements are graphs of maps from an (s−u)-space to an (r−u)-space, giving q^((r−u)(s−u)). The flag identity [n choose t]_q[t choose r]_q=[n choose r]_q[n−r choose s−u]_q turns this into the stated formula. Choices exist precisely for the stated intersection and quotient-dimension constraints, including rank zero. For n=2m and r=s=m, d=u≥m forces u=m and the two surjections are isomorphisms. The proof has no characteristic restriction. The frozen verify.py was inspected, not executed; it computes image overlap by the rank of horizontal concatenation and uses polynomial F₄ arithmetic. Its six finite test cases do not establish the general count. As a boundary check, at n=2 the formula sums to 1+(q+1)(q²−1), giving 10, 33 and 76 at q=2,3,4.

## originality

FAIL

Resultary 2db661bafe6d gives the exact same joint distribution under transpose, with k=n−r−s+u. A separate indexed record, 6deaf49eec33, gives the identical image-overlap count in factorized form by choosing the sum of the images first, with the same feasibility conditions and additional geometry. This is demonstrated statement-level coverage; the displayed dates, including the same date for the dual record, do not establish priority or provenance. The difference between a Gaussian–Möbius sum and a positive product does not make the underlying joint census a distinct finding.

## value

FAIL

Individual ranks and the common image span are natural representation invariants, and the positive product is convenient compared with a Möbius sum. The exact information, including feasibility and the maximal-rank boundary, is already recovered by duality from the same-day joint census. The product itself is the standard complement and surjection count in the known radical chart and also appears in the indexed overlap census. The record gives no independently useful new exact invariant beyond those equivalent results.

The dated certificate retains the supplied scientific assessment, sources and limitations.
