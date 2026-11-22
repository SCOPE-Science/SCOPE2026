---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-19.md",
      "INDEPENDENT_AUDIT_2026-11-19.json"
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

The actual seven-entry frozen Git record was inspected, including RESULT.md, the complete assignment proof, the sharpness construction and verification source. The Git tree was reconstructed from its seven actual blob SHAs and matched 52bb0d57766296d68e41e7dd6debd7a737cececb. For q_(i,j)=max(-b_j(P)), take a maximum-sum perfect assignment sigma. The strict-improvement digraph i->sigma(j) is acyclic: a cycle would give a strictly improving reassignment among distinct columns; hence a sink r gives q_(r,j)<=q_(sigma(j),j). Choose attained coordinate witnesses from each assigned family; their intersection obeys all coordinate bounds of the complete r-th color intersection. Finiteness/nonemptiness, arbitrary nonzero normals, redundancy, ties and possibly empty polyhedral intersections are handled. For each essential facet choose an exterior point satisfying all others and relax remaining bounds by a common finite T; with m-1 selected distinct facet-index bodies some facet is omitted, so full universal containment fails. Independently reconstructed 3,096 small exhaustive/random matrix examples and all 2+64+7776 reduced-color axis-box assignments in dimensions 1-3; these are diagnostics only, not substitutes for the proof. The 2012 DAP theorem separately supplies an independent published proof of the critical matrix implication.

## originality

FAIL

The distinctive claim is directly covered by Calvillo & Romero (2012), The dominance assignment problem, Theorem 3 and its defining inequalities. For the common-normal severity matrix q, apply their general theorem to A=-q at h=m=n. Its guaranteed C_ii<=C_1i yields precisely q_(selected row,j)>=q_(winner,j) for every coordinate under matching permutations; taking input minimizers immediately gives the assigned rainbow-to-complete-color set inclusion. The claimed new assignment lemma is thus a weaker algebraic corollary of the published matrix theorem; the polyhedral translation is formal. The m-1 sharpness construction is an elementary omitted-facet pigeonhole argument, and 2d sharpness for boxes is already known. No independent valuable original remainder was identified; no revised claim is accepted.

## value

FAIL

Common-normal polyhedra and a single set-inclusion certificate are useful in geometry, and the result is correct. Nevertheless its entire proposed distinguishing structural content and polynomial matching algorithm are obtained by an immediate sign change of the published dominance-assignment theorem, with coordinatewise minima and the obvious omitted-facet example. Under the shared value bar, repackaging a known general theorem by routine substitution and a standard sharpness witness does not establish a new worthwhile mathematical gap. This is a lack of independent research value, not a claim that existing algorithms or geometric corollaries lack applications.

The dated certificate retains the supplied scientific assessment, sources and limitations.
