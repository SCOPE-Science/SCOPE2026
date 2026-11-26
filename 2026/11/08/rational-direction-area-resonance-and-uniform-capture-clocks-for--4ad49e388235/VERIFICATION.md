---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

For local fractional horizontal position r, the next seam is reached at height y+alpha(1−r)=u+alpha mod 1. The remaining r units of horizontal motion restore the coordinate r, so the same phase formula applies to all slices, with area Jacobian one. At an arrival height in the barrier both sheet histories merge into the left sheet; otherwise they are exchanged. Each target phase has a unique base ancestor and loses exactly one sheet iff one of its preceding n arrival heights is in the barrier. A full q-cycle has either only swaps (so the period divides 2q) or a constant composition with exactly one fixed sheet (so the periodic label returns after q steps). Away from boundary lines the stable image is locally constant in the sheet coordinate; its complement has neighborhoods with no returns after q steps, and a short phase neighborhood excludes earlier returns when q>1. The translated intervals form a 1/q-grid, giving union length min(1,qb). In the disjoint case, the transient sheet over B−j alpha first agrees with the periodic sheet at step j, so the area of each such class is b and normalization by qb gives 1/q. The proof includes q=1; when qb=1 and B is open the grid endpoints can be missed, without changing area. The irrational-area comparison agrees with the originating paper's Theorem 1.

## originality

PASS

The single-barrier model and its merging mechanism, two-sheet symmetry and irrational equal areas are in Beck–Chen–Yang. The strongest verified predecessor studies the same surface for irrational slopes and uses a reverse-flow construction with guaranteed encounters; it does not give the finite-depth image formula or evaluate the rational paired-sheet and no-hit cases. These cases, including the exact conditioned first-capture masses, form the supported distinct claim. The related symmetric half-plane rotation and invertible two-circle gate have different sheet dynamics.

## value

PASS

The rational directions are a natural gap left by the same model's irrational theorem. This precisely identifies the denominators with excess recurrent area and gives a nontrivial capture law, not just an eventual-area bound. The area and time normalization allow direct comparisons with other barrier configurations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
