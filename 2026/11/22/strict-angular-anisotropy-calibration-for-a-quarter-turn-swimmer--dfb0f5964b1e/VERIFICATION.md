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

The original RESULT.md line 68 incorrectly asserts continuous log-ratio density for all a. Since h_a(w)^2 is asymptotic to w^(2a-2)/B(1/2,a)^2 near zero, the convolution at zero diverges for a<=1/2 (and Fatou's lemma shows the same limit as the argument tends to zero). The strict interval-mass argument also used strict density decrease where the a>1 step only established nonincrease. The full corrected RESULT.md under /workspace/repairs/3/ preserves the theorem: take layer cake in the symmetric unimodal density, not in the test. Each nontrivial finite centered superlevel interval contributes integral_{s-r}^{s+r} F(v) dv, strictly decreasing for s>0 because F(s+r)<F(s-r). Finite positive-length levels have positive measure even for an unbounded density. Convolution with the independent log difference of the nondegenerate beta factors strictly decreases the expectation. The repaired proof needs no strict density or continuity assertion. I rechecked the telegraph signs (one flips at each permitted turn, each at rate gamma), the rotation sign of cos(4theta), beta parameter and factor multiplication, the dominated continuity and endpoint beta limits, and the square-law integral giving pi-3. At high a the joint Gaussian correction in polar coordinates is r^2 - r^4(3+cos(4phi))/8 - 1/4; Gaussian radial averages of r² and r⁴ are 1 and 2, respectively, giving exactly -cos(4phi)/4 in the rotated angular density at first order. Gaussian domination outside r<=a^(1/8) and polynomial-weighted Taylor errors inside yield the stated integrated O(a^-2) error uniformly in angle. Independent bounded reproduction: python /workspace/branches/replay_frozen.py 3; direct polar integration gives aQ=0.125389077, 0.125156004, 0.125078064 at a=80,200,400. The original script and recorded numbers are unaffected by the proof repair and were not executed.

## originality

PASS

Best-knowledge pass after repair for strict all-positive-rate ordering of one scale-free stationary position-angle harmonic and the resulting inverse. The proof correction does not change the observable or parameter range. The exact position/angle law is prior input, and the unit-ratio anchor is a calculable consequence of its uniform square case, not an originality basis. Independent primary access to the decisive angular-law passage was limited. Two different calibration observables in the same model were compared by their actual statements, not discarded as same-date results.

## value

PASS

The full attainable range and strict ordering make a single angular harmonic sufficient to identify a rate ratio independently of spatial scale, including across the change in stationary density shape. This resolves ambiguity of a natural observable rather than supplying pointwise forward evaluations. The sharp high-rate law also quantifies fading of the signal. This is not a finite-sample estimation result, separate identification of both rates, or a theorem for noisy or differently turning swimmers.

The dated certificate retains the supplied scientific assessment, sources and limitations.
