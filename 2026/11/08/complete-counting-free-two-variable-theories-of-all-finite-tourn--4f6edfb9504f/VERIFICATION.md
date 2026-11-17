---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

At most one source and one sink can exist. Repeatedly removing sources yields a canonical initial linear chain. Subsequent sink peeling from source-free residue cannot create a source because each remaining vertex already beat that sink; the nonempty terminal core has no global source or sink and at least three vertices. Two-variable formulas σ_i(x) and reversed θ_i(x) recursively define the ith head/tail positions via scoped variable reuse; fixed finite i needs only x,y, so different peeling counts and transitive lengths are distinguishable. For equal (h,t), Duplicator maps matching chain positions; inside a core, each vertex has both in- and out-neighbor, so a permanent two-pebble response preserves equality and either arc orientation for arbitrary moves and depth. No counting quantifier is used. A 3-cycle core gives minimal nontransitive representative, and any core size r>=3 exists (e.g. lexicographic blow-up of a 3-cycle), giving 1+C(n−1,2) classes. Independent enumeration of all labelled tournaments of orders 1..5 found invariant class counts [1,1,2,4,7], matching formula; finite checks cannot replace infinite-depth Duplicator argument.

## originality

PASS

PASS to best of knowledge: full earlier FO² cyclic triangle substitution result proves precisely the h=t=0 special case, while unrestricted tournament peeling counts and all-core equivalence are not implied by it; structural tournament decomposition and model-theory survey give tools, not the full quotient/spectrum.

## value

PASS

An unrestricted-quantifier-depth classification of all finite tournament FO² elementary theories with explicit canonical minima and exact spectrum is a natural full model-theoretic classification, showing dramatic blindness to arbitrarily complex source/sink-free cores. This is stronger than the special directed-triangle transitive-block family and supplies a reusable normal form for finite-variable logic.

The dated certificate retains the supplied scientific assessment, sources and limitations.
