---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

The equations in primary Tables 1 and 2 match the eight displayed cases, including the additive exponential term in Model 6 (unlike the general template in Eq. (8)). The second output fixes q=v−x. The distinct phase levels have density κ/π, and each strictly monotone piece contributes that density times its phase range up to O(1), with at most one duplicate at each shared endpoint. The four quadratic-charge phases decrease on both tails because −3ωbx² dominates O(|x|) derivative terms. Likewise the absolute-only and literal mixed Model 6 have derivative −2ωb|x|+O(1); their difference is bounded with bounded derivative. These six maps have O(1) pieces: at the possible kink each analytic branch extends locally to its endpoint and the derivative is not identically zero. Subtracting the two cubic endpoints cancels the v-dependent x² term, and for R>|v| the absolute term contributes exactly 2ωbR² before its linear constant adjustment; the x-scaled bounded exponential contributes only O(R). For the two periodic-only memories, the variation equals ωb∫|x||M′(v−x)|dx+O(R). Subtract the mean of |M′| and integrate with a bounded periodic primitive to obtain the stated R² coefficients. Simple zeros of M′ give at most one stationary point in each distant zero neighborhood because h″ has constant sign there, and none away from those neighborhoods on distant tails, so the counting error is O(R). The zero-coupling formula follows directly from its phase lattice. The phase expressions are nonconstant analytic on each side, with analytic continuation up to a kink, so fibers are finite on compact windows and hence countable. The determinant on smooth branches is a cos(h)h′; this gives infinitely many regular predecessors at interior outputs. At an extremal output even an absolute-value kink poses no boundary exception: H is locally Lipschitz and the sine has zero derivative at that phase, so the first output is differentiable with zero derivative there. The claim that all extremal-output predecessors are critical follows.

## originality

PASS

No novelty is assigned to the Model 1 law, to phase-variation counting, or to the zero-linear-tilt specialization of Model 3. The last is exactly equivalent to an existing cosine-memristor result under an affine coordinate change. The surviving claim is the full fixed-parameter architecture comparison, especially the target-independent R² difference within the cubic-growth class and the quantitative distinctions between the periodic and absolute/exponential choices. The source paper defines these maps but its inspected analysis and conclusions report forward diagnostics, not these inverse asymptotics. The compared statements do not supply the mixed-memory term or full comparison.

## value

PASS

The original comparison varies memory type and number; bounded-window inverse multiplicity is a natural reconstruction observable for these real maps. Within the four cubic-growth models the leading count cannot distinguish the mixtures, but the second-order coefficient detects absolute-charge memory regardless of the fixed target and the exponential component. This compares a complete published architecture family at a precision where the distinguishing effect is visible, rather than offering another fixed-parameter computation or claiming value from the already-known special cases.

The dated certificate retains the supplied scientific assessment, sources and limitations.
