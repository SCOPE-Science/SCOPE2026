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

The log Laplace functional of the Poisson trajectories makes each mixed cumulant the intensity integral of a same-mark product of indicators. Bounded windows ensure integrability of that functional (each translated indicator integrates to the window area), and rectangle values determine the displacements' count measures. In one lag uniform headings and isotropic translational noise give a radial displacement law, and reflection interchanges ω and −ω, so even pairs of unequal windows cannot distinguish the sign. From the triple measure the transformation to two adjacent increments gives ρ dx times their joint law. With one bounded anchor of nonzero area, normalization recovers their mean wedge; spatial truncation is valid by E|U||V|<∞. This is an ensemble statistic, not a recovered individual trajectory. Independent translational increments leave only v² times the integral of e^(−D_r(b−a)) sin(ω(b−a)) over a∈[0,t], b∈[t,t+s]. With x=t−a, y=b−t it factorizes. For equal lags the integrals of x+y and (x+y)² are h³ and (7/6)h⁴, giving the stated sign and coefficients directly. D_r=ω=0 gives zero without dividing by zero. The radial law gives M(t); its right derivatives through order four are 4D_t, 2v², −2v²D_r and 2v²(D_r²−ω²). The second is strictly positive, and H(h,h)/(v²h³) tends to ω including zero. If intensity is unspecified it is obtained by total mass of the lagged measure per unit anchor area. Ran python3 /workspace/reproductions/1.py (18 integrated-series comparisons, 3 circle-geometry comparisons and exact short-lag coefficient checks). Separate bounded high-precision quadrature also agreed, but the proof, not finite samples, establishes identifiability. This is for all ideal bounded-window observables in a fixed oriented coordinate plane, not a finite-field or finite-sample estimator. Frozen status fields mark Lean/expert/independent evidence not performed; uploaded code was inspected, not run.

## originality

PASS

The supported distinction is a tracking-free, signed adjacent-increment observable from three-time counts, proving where the chirality-sign ambiguity of pair-count data ends in the stated Poisson gas. The independent-particle cumulant formula, ordinary MSD and its derivative information, circle-swimmer scattering law, and general principle of using higher-order observables to break a symmetry are not claimed as novel. The strongest inspected statements supply pieces, but do not supply this count-only separation and recovery.

## value

PASS

The comparison of measurement orders answers a practical inverse question at the theorem's own idealized level: arbitrary spatial resolution of pair counts cannot remove the sign ambiguity, while one specific third-order ensemble moment can. The calibrated short-lag limit and separate identification of transport and turning parameters make the distinction operationally precise within that model. No practical signal-to-noise, finite field-of-view or tracking claim is needed for this value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
