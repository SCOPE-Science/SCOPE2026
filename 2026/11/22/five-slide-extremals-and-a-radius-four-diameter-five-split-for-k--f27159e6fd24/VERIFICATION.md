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

Final repaired claim, n≥8. The unobserved vertices initially are unselected pairs that hit all selections. For up to three selected spokes there are at least four unobserved spokes; a noncentral observed pair sees at least two, and every observed central pair is selected and sees no unobserved vertex. Two disjoint selected pairs leave the four cross pairs, each observed pair being adjacent to zero or at least two of them. Triangles and three disjoint pairs leave no unobserved vertex; the other two nonstar triples leave the displayed two, one forced by a pair using a fresh label and then the last forced. Thus the slide states are precisely nonstar triples. Orbit sizes use the counts of labelled ground graphs on their supports. For each selected pair there are binom(n−2,2) disjoint candidates: total invalid replacements over the three deletions are 3(n−3), 2+2(n−4), 2+(n−3), and 6 in the four respective classes, accounting for overlaps of occupancy and the forbidden star only once. This gives the degree and enumerator formulas. The obstruction is symbolic: with disjoint endpoint configurations and at most four slides, each tracked token must move, so two move once, giving a direct matching of size at least two. For the converse and all upper bounds, permutation orbits permit four roots for each n=8…12; any larger-order endpoints occupy at most 12 labels, and paths on those 12 labels remain admissible in the larger graph. The custom adjacency construction groups triples by their two retained pairs and links exactly the disjoint legal extensions, so it tests the full induced graph (not unrestricted jumping). Complete independent distance layers from all four roots at each of five orders reach every state and identify the depth-five layer with precisely the stated matching deficit; all 20 histograms and all five size/edge counts agree with both recorded outputs where applicable. Replay: python3 /workspace/branches/independent_slides.py 8, then 9 10 and 11 12; outputs /workspace/branches/independent_slides_n8.txt, independent_slides_n9_10.txt and independent_slides_n11_12.txt. Frozen scripts were inspected, not executed. For sharp lower bounds in every order, the triangle witness requires at least four by lack of a direct perfect matching, while the two original path-type witnesses and the corrected matching witness have ν=1. In the corrected case every target meets both 01 and 23 and avoids 45. These witnesses persist in all larger orders. Together with the upper layers this gives all four eccentricities, radius four and diameter five with no extrapolation assumption.

## originality

PASS

The repaired final finding is the same precise adjacent-slide theorem, not the known nonstar classification, the orbit enumeration of that classification, or the general finite-support method. The inspected literature and related records do not imply the radius/diameter split with its exact all-order criterion. In particular the nearest same-graph comparison changes both feasibility and moves, and the distinct same-day records change the base graph. This is an evidence-bounded pass, not proof of priority.

## value

PASS

The feasible set is a known natural optimal-sensor family, but requiring legal adjacent motion poses a distinct constrained-geodesic problem. In this unbounded highly symmetric graph family, the theorem reconstructs all maximally distant configurations from a direct-move matching obstruction and identifies the central orbit, with a nontrivial radius–diameter gap. This is useful beyond numerical diameter per order; the complete twelve-label certificate and matching obstruction connect a finite exact computation to the all-order classification. It makes no claim for higher-subset Kneser graphs, general token counts, or the complete distance law below five.

The dated certificate retains the supplied scientific assessment, sources and limitations.
