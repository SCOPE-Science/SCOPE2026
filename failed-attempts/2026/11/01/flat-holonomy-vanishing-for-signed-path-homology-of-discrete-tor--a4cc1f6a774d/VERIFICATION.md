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

The signed convention and all-degree result are correct. In the frozen descent argument an allowed path lifts from a chosen start; endpoint deletions and backtracks pose no obstruction. Every regular forbidden face of an allowed path boundary has exactly one nonedge. All two-edge bridges for that nonedge lift with the same endpoint because the base product has no competing distinct two-edge bridges other than elementary squares. This remains true for the intermediate quotient: a square projects into the base product and the lift to the longer product closes. Consequently the same signed coefficient sums must vanish for the forbidden faces, both downstairs and upstairs. The orbit sum is therefore an isomorphism onto invariants on GLMY chains, and real averaging commutes with homology. The seam normal form and quotient map realize the cover and its residual deck flip; factor rotations act trivially by naturality of the shuffle product. For a bidirected cycle of length at least five, its higher homology vanishes, and in degree one the two-step backtracks give the symmetric edge-sum boundaries while distinct-endpoint two-step shortcuts are unique and forbidden. This gives exactly one H1 generator, the oriented cycle, and ordinary H0 is one-dimensional. Cartesian Künneth gives the balanced binomial formula. Independently of descent, square-flatness makes the lifted positive shifts T_i commute (two orders traverse a flat square); their inverses are the negative shifts. Each T_i is therefore a digraph automorphism moving every vertex along an edge, so it is one-step digraph-homotopic to the identity. If chi_i = −1 then T_i^(m_i) is the deck flip, hence its action on all ordinary path homology is the identity. The real anti-invariant groups are zero. This also covers d=1. The supplied field examples are corroboration only and were not run; the all-degree proof does not use a general cubical-to-GLMY comparison. The frozen long-cycle citation is imprecise in proposition numbering in the consulted Asao version.

## originality

FAIL

No earlier verbatim statement for all the sign patterns was identified, but the all-degree vanishing is directly implied by the published canonical double-cover formula together with the established one-step GLMY homotopy theorem. Lift the positive coordinate shifts; flatness says they commute, so they are graph automorphisms along edges. Iterating one of them around any negative coordinate circle is exactly the deck involution, hence homologically the identity. This takes no new cover-descent or torus homology computation. The balanced case is already the standard product calculation. This is an implication decision about the frozen dimension theorem, not a claim that the longer chain-descent argument appears in the literature.

## value

FAIL

The stated real rank formula for the flat torus is a routine application of ordinary digraph homotopy to the canonical deck action. Its arbitrary dimension gives no additional obstruction or separate computation once the coordinate lift is observed. The longer chain-descent lemma could be considered on its own with an independent use case and coverage review, but neither that independent contribution nor an integral refinement is the frozen finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
