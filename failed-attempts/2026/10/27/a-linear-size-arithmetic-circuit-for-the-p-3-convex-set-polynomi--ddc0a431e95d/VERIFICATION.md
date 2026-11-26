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

The states track omitted with zero descendant-block selected neighbors, omitted with one, and selected, weighting a vertex only in its selected state. An omitted parent with no selected clique child allows either omitted state for every child; if it has one selected child, other children see that sibling and must have zero selected descendant neighbors. A selected parent allows either all children omitted in their zero states or all children selected; any mixed choice would give an omitted child two selected neighbors. At a vertex the descendant blocks contribute disjoint neighbor sets, so the zero/one calculation and the selected-state product are necessary and sufficient. Induction on the incidence tree gives the root sum, and independent components multiply; bridges, isolates and the empty graph obey the same conventions. The two-accumulator formula evaluates the one-exception sums in linear operations; there are O(|V|) incidence edges after decomposition, hence the claimed O(|V|+|E|) gate bound holds, without claiming linear coefficient-expansion bit-time. In a bouquet an omitted center admits only empty and singleton choices; a selected center permits independent all-or-none choices of each petal, giving exactly the stated polynomial. Independent finite code and output in branches/ebabd826-770f-4a0f-b8d5-5312a62f3776/record5_independent_check.py and record5_independent_check.txt corroborated every coefficient on 123 generated graphs up to 10 vertices and a heterogeneous bouquet; finite checks are not the unrestricted induction. The frozen output counts 8367 nonempty labeled block graphs through order six, with the empty graph outside that tested histogram.

## originality

FAIL

Demonstrated stronger coverage, not a search miss or an inaccessible-source judgment. Two distinct indexed records give the same three-state positive recurrence with arbitrary individual vertex weights. Substituting one common weight z gives the frozen circuit coefficient by coefficient; the earlier general theorem has an O(|V|) gate bound and explicitly covers disconnected graphs, isolates and the empty graph. The heterogeneous bouquet expression is the direct evaluation of the same covered recurrence on leaf petals, not a distinct structural result. The equal-petal derivation was already explicitly given. No historical authorship or precedence inference beyond the demonstrated mathematical duplication is needed for this assessment.

## value

FAIL

An explicit multivariate block-graph recurrence with small boundary states is useful in itself, but that work is already present in the compared records. The only apparent separate addition, nonidentical petal sizes in the bouquet display, is a product of independent all-or-none petal terms obtained directly from that known recurrence; it resolves no remaining structural or counting gap. A fresh finite certificate or a narrower restatement of this substitution would not produce a substantive surviving claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
