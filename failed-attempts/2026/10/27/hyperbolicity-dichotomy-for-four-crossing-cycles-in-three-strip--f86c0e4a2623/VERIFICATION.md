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

For an already realized primitive R,C,L,C orbit, each same-line outer flight preserves a boundary quadratic at distinct ordinates with nonzero normal velocities. A zero quadratic coefficient would force zero normal velocity, so the two outer maps are local reflections with derivative −1 and fixed midpoint. In the center, write t_R,t_L for the midpoint normal velocities and v_R,v_L for the signed half-differences in the given forward labeling. The crossings force b v_R,b v_L>0 and the four stated strict normal signs. Adding and subtracting the two central conserved-energy conditions gives t_R v_R=t_L v_L and Δ+(b/2)(v_R²−v_L²)=0. Each center map differentiates to the ratio of inlet to outlet normal velocity; composing with both reflections gives the genuine crossing-return multiplier. Its positive value differs from one by 2b(t_R v_L−t_L v_R) divided by the strictly negative denominator (t_L−bv_L)(t_R+bv_R). The energy identity rewrites the numerator as 2b(t_R−t_L)(v_R+v_L), proving the claimed opposite sign with Θ=t_R−t_L. If t_R=t_L≠0, the matching equations give v_R=v_L and Δ=0, so common amplitude varies freely. If both vanish, the remaining matching equation has nonzero derivatives in both amplitudes. In each case the transverse local hit maps are smooth and persist with the same itinerary (the interiors of the reference arcs stay off the boundaries); the energy level at each exit has a unique nearby ordinate because its normal derivative is nonzero. Thus the matching family follows actual flight branches and the return map is the identity on an open section interval, giving a local period annulus. No global existence or annulus statement follows. Independently checked three affine examples via exact flight times and ordinates: attracting multiplier 7/25 and its reversal 25/7, plus nearby exact cycles in the zero-midpoint and nonzero-midpoint neutral regimes, all allowing degenerate linear parts. Direct high-precision evaluation of the frozen motivating ordinates gives 7.1636898251743157934. Replay: python3 /workspace/branches/reproduce_frozen.py strips; log /workspace/branches/reproduction-strips.txt. These checks are illustrative and finite.

## originality

FAIL

A distinct indexed record states the same coefficient sign on the motivating nondegenerate domain and proves the same two-case neutral annulus using the same equations. Its determinant hypothesis is absent from every decisive argument, so deleting that hypothesis here does not yield an independent stability or neutral-family mechanism. The scope distinction is real, but the extension is mechanically implied by the inspected argument. This is a coverage finding, not an attribution of priority from catalogue dates.

## value

FAIL

The dichotomy and directly computable stability sign are mathematically useful in themselves. Relative to the independent matching finding, however, the determinant-free version makes no further structural or quantitative gain: the determinant never enters the local proof, and the record neither classifies realizability in degenerate fields nor gives a distinct degeneracy result. The signed labeling and alternate verification examples check the same mechanism rather than advancing it.

The dated certificate retains the supplied scientific assessment, sources and limitations.
