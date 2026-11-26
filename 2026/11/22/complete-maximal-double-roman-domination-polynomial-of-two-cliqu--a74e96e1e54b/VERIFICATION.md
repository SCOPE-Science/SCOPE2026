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

Zeros in both cliques dominate; with zeros only in B the maximality witness exists exactly when B also has a positive label, whose mate in A has no zero neighbor. With neither clique containing zeros, one can choose a high (2 or 3) in each (E_n²), or have one all-1 clique forced to match only high labels in the other (the second term). With zeros in B, A must have a high label because the mate of a zero could not be a defended 1 if A were all ones. The three B regimes are disjoint: (i) some 3 or at least two 2s gives internal defense, counted by E_n B_n after excluding no-zero and deficient B assignments; (ii) exactly one 2 and no 3 gives its column z²a, then other columns either b_i=1 with factor za, or b_i=0 requiring a_i≥2 with factor z²+z³, and the all-positive B choice is subtracted; (iii) only 0s and 1s in B requires a_i=3 at each zero and a_i≥2 at each one, with both constant B choices forbidden. Orientations supply the stated factors of two. The first one-sided regime starts at n+4 only with a single 2 among the positive clique's ones and a single 3 among the other clique's zeros. The independent choice of two positions gives 2n². Competing regimes start at 2n+2, 2n+1 or 3n, all strictly above n+4 for n≥4. The two intervals [n+4,3n+3] (hold the lone 3 in B) and [2n+2,6n] (positive and high in each clique) overlap and realize the entire spectrum. At z=1 the zero-free terms and no-high term combine to 9^n−1, and the remaining terms give the displayed total. Independent replay: python3 /workspace/reviews/check_mathematics.py 3 tests the dominance witness and defender conditions directly on graph neighborhoods for n=3,4,5, with coefficientwise matches and exact listed optimizer sets at n=4,5. At n=3 there are 36 minima rather than 18, confirming the need for the scope restriction.

## originality

PASS

The exact maximal double Roman weight enumerator for two matched cliques is distinct from the scalar clique result, ordinary Roman-variant product results and the same-graph calculations for other defender rules. No earlier equivalent was located in the bounded comparisons.

## value

PASS

The full weight distribution for the natural matched-clique family isolates which configurations need defenders across the matching and which are internally self-sufficient. The non-domination witness removes entire extreme configurations, not just weights. The polynomial gives a uniform benchmark for weighted enumeration, recovering the exact minimum multiplicity and full contiguous spectrum rather than only a scalar optimum.

The dated certificate retains the supplied scientific assessment, sources and limitations.
