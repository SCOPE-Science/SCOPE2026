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

Fresh audit of the repaired theorem: the shore inequalities exclude sizes below five and force the two five-set patterns. In the two-point case the three forced lines cover exactly the seven unselected points and concur at the unselected third point of the omitted direction, which violates restraint; duality handles the other shore. Independent Python enumerated all 262144 subsets; all stated polynomial coefficients agree, with 207 optima at six. It considered both shores and all 9! point-image bijections on each; connected bipartiteness and distinct line-neighborhood triples make this an exhaustive automorphism check, not an inference from finding 216 permutations. The five orbits have the reported sizes. The two three-edge types have induced degrees (1,1,1,1,1,1) at mask 3682 and (0,0,1,1,1,3) at mask 3591. Comparing the actual isolated-state sets for both rules gives precisely their union. Pairwise exchange checks and BFS from every main-component state verify edge totals 432/324 and eccentricities 6/8. The full corrected checker was run successfully.

## originality

PASS

The distinct supported claim is the full 207-state restrained classification, its polynomial and both mobility censuses. The ordinary five-set classification has a separate exact overlap; the nine matching states and their immobility were already implied by the efficient-open-domination result; and the 18 claw configurations can be reconstructed from the ordinary minima. This narrower novelty statement applies to the repaired finding, not to the rejected structural assertion.

## value

PASS

The Pappus graph is a natural symmetric cubic incidence graph. The repaired result distinguishes actual immobility from connectivity under two different exact move rules and gives a complete usable optimizer and restrained polynomial census; its contribution is not the known ordinary count or merely that the nine efficient open dominating sets are frozen.

The dated certificate retains the supplied scientific assessment, sources and limitations.
