---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

In the apex deletion each shadow neighborhood is contained in its corresponding old neighborhood. Thus adjoining to an independent face the shadows of its old vertices preserves independence. The projection is contiguous to the identity, equivariantly retracts to the shadow simplex, and straight-line contraction reaches the invariant barycenter. The apex link is the old independence complex. Its cone meets the deletion along exactly that link, so collapsing the deletion gives the unreduced suspension with both poles fixed. For each subgroup the fixed-pair inclusion is a cofibration after barycentric subdivision, the deletion fixed space is nonempty and contractible, and collapsing it commutes with fixed points since all other fibers are singletons. Equivariant Whitehead therefore applies. This also handles empty fixed links, and naturality under graph isomorphisms, the module isomorphism, and iteration follow from the quotient map.

## originality

FAIL

No explicit earlier universal statement was located, but the result is a direct combination of published ingredients that already supply the equivariant maps, not just an inference from an ordinary homotopy type or character table. The October 11 result, Proof §1, proves the labeled simultaneous equivariant fold by exactly the map and contiguity homotopy used here; its group written as S_n can be replaced verbatim by any group acting simultaneously on the labels, since the proof uses nothing else about S_n. For ordinary Mycielski apex deletion the two required labeled families are precisely all shadows and all old vertices and N(v') ⊆ N(v). This gives the invariant contraction used in the published apex-link/suspension argument; collapsing the deletion via standard equivariant cofibration or Whitehead then gives the stated result, with fixed points, modules, and iteration formal. The exact November indexed match is later and is not the basis for failure.

## value

FAIL

Fixed-space and integral representation information is genuinely useful and stronger than ordinary homotopy type, but the claimed advance uses the exact already available orbitwise fold on the already analyzed apex decomposition. Once this is recognized there is no independently needed unknown invariant or obstruction: the fixed-space, representation and iteration claims are formal, and the C5 illustration does not supply a separate substantive result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
