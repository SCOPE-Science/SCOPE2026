---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

At least one vertex of color a and one of each b_i are necessary for the boxed subformulas to be defined and false, giving k+1. With only k+1 total, every p_bi has one fixed value and every Box_a p_bi being false forces it to be false; any accessible face defining the full disjunction then falsifies it, contradicting a true antecedent. For k+2, root r plus false states f_i and one true t_k, with maximal faces {r,f_1,...,f_(k-1),t_k} and {r,f_k}, all faces at root accessible and singleton directions elsewhere, are upward; weak-Kleene disjunction is defined only on top face where t_k is true; every consequent box has a defined false witness. Independently constructed/checked k=2..12, but general argument works without finite cutoff.

## originality

PASS

A primary preprint Unbelievably Complex (2026) introduces upward directed simplicial models and displays a larger illustrative binary independence failure, as stated in submitted work; the paper itself could not be read in full from attempted OA/arXiv or authorized institutional access. Search of published Resultary returned no prior theorem of a sharp k+2 local-vertex threshold. This supports only qualified best-of-knowledge originality, not a negative whole-paper priority assertion.

## value

PASS

The smallest concrete Kripke-like simplicial countermodel for a standard distributivity/independence axiom is a natural semantic model-size threshold, with a uniform arity-dependent exact law and a specific one-agent-state duplication mechanism. Distinguishes falsity from undefinedness, an essential subtlety of the semantics.

The dated certificate retains the supplied scientific assessment, sources and limitations.
