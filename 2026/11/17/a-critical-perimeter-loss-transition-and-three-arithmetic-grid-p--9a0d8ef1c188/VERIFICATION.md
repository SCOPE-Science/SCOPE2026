---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

Original proof of the local normal form incorrectly asserted x=1−|t|^p/p+O(|t|^{min(2p,p+2)}), omitting the cos(t) contribution −t²/2; this stated estimate is false for 1<p<2. A complete corrected RESULT.md gives x=1−|t|^p/p+O_p(t²), y=t+O_p(|t|^{p+1}); since t²=o(|t|^p), the required tangent normal form and half-variance cell coefficient q_p remain valid. Independently reconstructed arc-minus-chord difference via tangent variation; away from axis it is bounded by C h³d^{2p−4}, and q_p tails behave as (p−1)²j^{2p−4}/24. These estimates yield the three residue-lattice phases below 3/2. At p=3/2 curvature density is (4d)^−1, eight axis sides giving h²ln n/12; for p>3/2 density is integrable and the smooth-cell Riemann sum yields (h²/24)∫ det²/|γʹ|³. Verified circle p=2 identity 2π−2n sin(π/n) and coefficient π/12. Reassessed C on the complete new final claim/proof, not the false original intermediate assertion.

## originality

PASS

Same-object prior Resultary polygon theorem rigorously treats max Hausdorff normal deviation and phase-dependent n^(−p) error. It does not determine the integral/sum of arc-length minus chords or critical p=3/2 integrability threshold. The Fodor–Minuță same-polygon primary source supplies construction and qualitative convergence, not this quantitative perimeter loss in accessible material. Full primary source retrieval remained blocked, a priority risk not an automatic scientific failure.

## value

PASS

The total chordal perimeter loss probes squared tangent variations and integrable curvature; the sharp critical exponent p=3/2 and three grid congruence classes (different from the two Hausdorff phases) are meaningful geometric approximation invariants. Correcting a local remainder restores a rigorous surviving self-contained theorem without changing any asserted principal scientific limit.

The dated certificate retains the supplied scientific assessment, sources and limitations.
