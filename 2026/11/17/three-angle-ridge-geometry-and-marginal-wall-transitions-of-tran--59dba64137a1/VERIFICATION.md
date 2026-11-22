---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

Full dimension is (m−1)(n−1) because X_ij=a_i b_j/T is positive. The Hall positive-flow criterion after deleting at most two cells proves single facet condition a_i+b_j<T and the pairwise same-row/same-column/disjoint conditions. Without strict support an extra coordinate is forced zero; connectedness of K_{m,n} after deleting at most three cells except impossible isolated-margin cases gives codimension at least three. The Frobenius tangent projector is P_m Z P_n, with pair-normal cosine -1/(n−1), -1/(m−1), +1/((m−1)(n−1)). The central inequalities 1/m+2/n<1 and 2/m+1/n<1 fail only for 3x3. In the mean-angle formula A=m−1,B=n−1, AB asin(1/AB)−A asin(1/A)−B asin(1/B) -> -1, whereas the disjoint-class scaled angle approaches +1. Independently solved 1,440 strict positive common-slack LPs across dimensions 3x3–4x4 and checked all predicted facet pairs; finite LPs corroborate only, the Hall/projector proof supplies universal and equality cases.

## originality

PASS

Best-of-knowledge original as a full pairwise strict-margin incidence and Frobenius dihedral-angle classification, with an unusual rare-angle/mean reversal in central transportation polytopes. Classical Hall criteria and the coordinate-facet criterion are explicitly credited. No inspected accessible full primary source was found to imply simultaneously the all-pair wall conditions and metric angle/mean theorem; Klee–Witzgall report is plausible and not accessible, so a material historical-priority risk remains but alone is not disqualifying.

## value

PASS

The exact pairwise margin walls characterize a natural face-adjacency invariant without generic margins, including sharp equality boundaries and the central 3x3 exception. The metric normal-product classification makes a mathematically motivated distinction between a typical asymptotically obtuse scaled angle (+1) and a negative scaled mean (−1), a rare-event phenomenon meaningful beyond a routine Hall restatement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
