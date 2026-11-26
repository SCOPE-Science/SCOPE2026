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

For every odd q, let T be the union of the x-lines through (0,t²,t³), and V the surface 2z=3xy−x³. For two curve summands, their sum x and second power sum y give product (x²−y)/2 and discriminant Δ=2y−x²; the third power sum is forced by V. The ordered fiber is therefore 1+χ(Δ) on V, including characteristic 3. A curve-plus-line decomposition has one choice of curve parameter on T since t is recovered by t³/t² away from zero. Subtract the common origin before squaring the convolution: on L the only curve-curve point is zero, and the net count is q everywhere. On T away from L the two oriented mixed representations remain. The curve-curve candidate equation is (x−t)²(x+2t)=0. At x=t the two curve-curve pairs both involve the origin and are already among the mixed pairs. At x=−2t they are genuinely new exactly when this is a distinct root and Δ=−2t² is a square. Thus char 3 eliminates the separate root, not its square character. In tallying, subtract the supported intersections from the curve-curve histogram: its q discriminant-zero points lose only the origin; its q(q−1)/2 two-pair points lose (q−1)(1+ε_q). Add the counts on T and L to obtain the displayed histogram; summing counts and their squares gives the claimed sumset and energy. Additive-character orthogonality with the unnormalized transform yields exactly the factor q⁻³ in the fourth moment. The proof's line 79 literally says V∩T contains the distinct −2t point only in the square phase; that is true for T intersected with the supported curve-curve convolution, not for V∩T as a bare algebraic set (e.g. (3,1,1) over F₅). Steps (2)–(3) and the actual subtraction correctly use support, so this wording slip does not change the proof's count or frozen finding. Independently enumerated all ordered pairs for q=3,5,11,27, recovering the histograms including zeros; q=11 gives ten four-pair targets, q=27 none. Replay: python3 -I /tmp/opencode/review_frozen_repro.py 2; the calculation forms S as a set and tallies every coordinatewise sum, using F₃[X]/(X³−X−1) for q=27. The frozen checker was read, not executed; finite corroboration does not prove the general case. No claim about weighted extension norms or arbitrary lines is verified.

## originality

PASS

The strongest distinct indexed match is a same-day planar cubic-with-tangent result. It computes a genuinely analogous invariant, but projection dropping the second moment merges target fibers and does not determine the three-coordinate convolution, in particular the −2t discriminant phase. The two records' dates do not establish priority. The older twisted-cubic incidence work and the pure-curve extension results give related geometric and algebraic ingredients, not a known implication of the corrected mixed-support histogram and its arithmetic split. The pass is specific to that mixed three-dimensional statement, not to Newton identities, curve-only energy, the Fourier identity, or the broader cubic-plus-tangent problem.

## value

PASS

The line is the intrinsic tangent at the distinguished origin, not a parameter chosen to simplify a table. Its union with the curve is a natural mixed curved/flat test for additive-energy and indicator Fourier calculations. A researcher can use the exact collision law, including the multiplicities themselves rather than just a bound, to distinguish when sums coalesce into four-representation targets; this regime changes both the support size and exact fourth moment by order q and disappears in characteristic three despite −2 being a square. This is a useful complete invariant of the canonical object and not a claim of a new general extension theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
