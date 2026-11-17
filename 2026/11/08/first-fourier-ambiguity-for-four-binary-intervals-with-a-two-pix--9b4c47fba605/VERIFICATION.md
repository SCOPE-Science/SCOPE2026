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

For binary pixel mask w, Fourier transform of the real-line union equals one-pixel factor K(xi) times P_w(e^(−2pi i xi)); K nonzero on a dense set, hence full continuous intensity equality iff all aperiodic integer correlation coefficients agree. Exactly four occupied runs with all 7 alternating occupied/gap widths >=2 bijectively correspond to seven-part integer compositions. Exhaustively compared all 6,435 compositions of spans N=14..22, reduced to 3,270 reflection classes using Burnside count; independent support-pair autocorrelation enumeration shows no collisions for N<=21 and exactly one two-class collision at 22, represented by A=1110011000111110000011 and B=1110000011111001100011. Algebraically P_A=(1−z³+z⁵)G(z), P_B=(1−z³+z⁵)z^16 G(1/z), with G=Σ_(j=0)^6z^j+Σ_(j=12)^16z^j, verifying equality directly. This is a fully finite exact cutoff, not extrapolated to larger spans.

## originality

PASS

General four-interval continuous Fourier nonuniqueness and reciprocal factor reversal were known (Xia–Xu 2026), as were run-autocorrelation formulas (Willms 2012). Neither accessible statement supplies exact smallest span 22 and unique first pair under simultaneous two-pixel minimum for all seven features. Earlier published three-block first-collision results use different objects and cannot imply four-run cutoff. Full Xia–Xu article was inaccessible in this run; priority explicitly conditional.

## value

PASS

The simultaneous minimum two-pixel widths of solid and transparent aperture features are a natural fabrication resolution constraint. The first loss of uniqueness and its entire double fiber are meaningful finite extremal information for a standard inverse diffraction model, beyond mere exhibition of some ambiguity. Exact cutoff and uniqueness provide a useful reproducibility benchmark without claiming robust noisy inversion or unbounded classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
