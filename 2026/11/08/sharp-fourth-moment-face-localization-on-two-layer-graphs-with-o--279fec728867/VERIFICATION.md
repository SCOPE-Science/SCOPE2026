---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

Let G have maximum degree at most two, no triangles or four-cycles and at least one edge; on H=K₂□G use real edge coefficients and independent fair vertex signs. The all-graph moment formula is E F⁴=3S²−2∑a_e⁴+24∑_{base edges uv}r_ur_vp_eq_e because all four-cycles are vertical squares. The exact nonnegative deficit decomposition (4) uses the base-graph positive-part energy lemma 2∑_{uv}[3(z_u+z_v)/2−Z]_+² ≤ ∑z_v². Its active edges cannot be disjoint and, by degree≤2/triangle-free, either one edge is active or two adjacent are; the two-edge case has a strictly positive quadratic gap. Equality forces exactly two adjacent equal nonzero rung masses and one matching square with four equal magnitudes and positive sign product. An independent 4-sign full enumeration gives the stated fourth moment 912 for an illustrative coefficient vector, and sign/mass restrictions were checked. Finite tests are not the proof for all admissible G.

## originality

PASS

The sharp 4S² bound and one-square equality persist for an infinite family of prisms with vertically overlapping adjacent squares. The published edge-disjoint-four-cycle theorem explicitly excludes their shared rung edges, and the older Q₃ cube proof treats only one finite graph via a 12-edge copositivity certificate. Neither entails the all-length open/closed ladder theorem or the positive-part structural lemma. Fourth-moment graph-Walsh expansion is acknowledged as known.

## value

PASS

Exact L²→L⁴ norms and optimizer supports on graph-structured Walsh spaces are natural operator-space invariants. Overlapping four-cycles invalidate simple disjoint-square additivity; the new positive-part lemma proves a substantive global localization mechanism on paths and long cycles, and a nonnegative deficit sharpens the result. No generic-hypercontractivity constant is misrepresented as new.

The dated certificate retains the supplied scientific assessment, sources and limitations.
