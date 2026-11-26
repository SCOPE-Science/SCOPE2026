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

Every image point is fixed and every component is a fiber with one root. The five rank-two formulas detect precisely the stated properties: the doubleton test selects a leaf that is the only leaf of its fiber, and the large test selects two distinct leaves at the same root. For a first point, reduce all terms to x,y,f(x),f(y). For a singleton root the availability of another root follows from another point, and another leaf exists iff there is a nonsingleton component. For a nonsingleton root or any leaf, an outside root is available iff there is a singleton or a second nonsingleton component, and an outside leaf iff there is a second nonsingleton component. For a first-point leaf, a distinct sibling is available precisely in a large component. These exhaust the atomic possibilities, so the two-round strategy works for finite and infinite universes. The admissible patterns are 2+4+6; the exhibited multisets realize them, and the pattern with a singleton and at least two large components first occurs at 7. A size-j rooted component contributes j z^j/j!, yielding A=z, B=z², C=z(e^z−1−z). Labelled SET over component types gives the exact formulas in RESULT.md:39–45. I inspected checker.py without executing it; the written back-and-forth is the proof for infinite models. I independently reconstructed the earlier coloured-equivalence census restricted to one marked root per class: run component multiplicities (a,b,c) over {0,1,2}³ minus zero, build components with one red and respectively 0, 1 or 2 blue elements, and group by the set of first colours paired with their sets of second-colour/equality/same-component triples. Taking the minimum of a+2b+3c in each group gives 12 groups with minima 1,2,2,3,3,4,4,5,5,6,6,7, confirming the finite count and cutoff independently.

## originality

FAIL

The core classification and cutoff are a direct subcensus of the earlier exact coloured-equivalence profile computation in Resultary e2acfc789698. The functions are a rank-preserving presentation of equivalence classes with precisely one marked point per class, and that restriction itself is rank two. In the earlier complete enumeration, keep only three of its eight capped class types and read off the rank-two profiles and their minima. This gives exactly the frozen census, including which patterns coalesce; for infinite models the same capped-profile proof works without alteration of its witness conditions. The earlier record does not state labelled EGFs, but the frozen series are the direct exponential-formula weights of those same profile cells, with no change of classification or further enumeration problem. This verdict rests on the actual earlier proof and enumeration, not on ambiguous overlap with the model-counting literature.

## value

FAIL

A small-model cutoff for this natural unary theory can be useful, and the five tests are a readable presentation. Here the numerical cutoff and the classes are already recoverable by selecting precisely the root-coloured rows from a stronger exact census. The explicit series are standard labelled-component weights on those rows and add no independent nonroutine invariant. There is no surviving supported contribution in the frozen finding that warrants a repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
