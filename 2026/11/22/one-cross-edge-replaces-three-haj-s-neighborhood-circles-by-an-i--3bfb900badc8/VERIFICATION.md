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

For a,b≥5 the two shore complexes are simply connected spheres up to homotopy: each is a contractible join glued to a simplex along that simplex's boundary. Their union meets at w. The other three old neighborhood simplices attach along two contractible components apiece and supply the free U,P,Q connectors. The only changed neighborhoods are those of α and β, and their enlarged simplices share only w, an old vertex. Each old intersection consists of two simplices glued along a nonempty simplex, together with two extra edges, giving a connected wedge of two circles. Relative chains split across the two attachments, hence the sole relative group is Z^4 in degree two. Orient the three connectors from the A-shore to the B-shore. For p∈A−{α}, q∈B−{β}, the loops (w,p,β), (y,p,β), (w,α,q), (z,α,q) map, after joining their basepoints within the shores, to U, UQ⁻¹, U, P⁻¹U. The first, second and fourth images contain a unit minor after abelianization and normally generate the free connector group before abelianization. Van Kampen gives simple connectivity; the integral exact sequence gives the split primitive inclusion and exactly one new degree-two generator, also when one or both old sphere degrees are two. Fresh check: from reconstructed graph neighborhoods and all old triangles, independently computed signed loop coordinates and the integral unit minor in four cases, including (5,5). Replay: cd /workspace && python3 review-evidence/reproduce.py 3; output review-evidence/3.txt. Frozen finite mod-two checks and their hard-coded matrix minor do not establish the integral map or π₁; the attaching argument does. Frozen scripts were inspected, not executed.

## originality

PASS

The distinct supported claim is the integral and fundamental-group response of the open-neighborhood complex to one ordinary cross-edge after the complete-graph Hajós merge, not the existence of a circle in the unedited merge or of two-classes in a disjoint-clique edge filtration.

## value

PASS

A natural one-edge perturbation of the standard Hajós construction changes three independent loops simultaneously, creates exactly one extra primitive two-class and preserves the old higher classes. The relative and induced integral maps make this a useful exact edge-sensitivity benchmark; the contribution is not a small graph count or simple connectivity in isolation. No general classification of arbitrary edge insertions is warranted.

The dated certificate retains the supplied scientific assessment, sources and limitations.
