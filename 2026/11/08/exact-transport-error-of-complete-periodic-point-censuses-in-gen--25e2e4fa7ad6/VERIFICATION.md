---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

For H>=2 the two inverse branches S0=x/H, S1=1-x/H contract with disjoint cylinder interiors (the H=2 shared boundary has zero Bernoulli mass). Every length-n word has one fixed point, distinct across words, with 2^-n per cylinder, so one-dimensional monotone optimal coupling matches each cylinder’s mass to its periodic fixed point. W1=H^-n E|X-Y_n|. Affine-branch sign average computes exact census barycenter m_n=(1-H^{-(2n-1)})/[2(1-H^{-2n})]. A self-similar absolute-deviation recurrence averaged over all fixed points permuted by f_H gives the stated exact W1 formula, including nonzero H^-3n correction; a jump at 0 yields exact Kolmogorov distance 2^-n. Independently recomputed rational periodic points and mean transport for n=1..3 at H=2,3,5/2. All-real H claim supported by algebra, not finite extrapolation.

## originality

PASS

PASS WITH OVERLAP: An independent same-date published result explicitly covers exact W1 for H=2 (full tent, Lebesgue), and classical periodic-coordinate papers cover part of the construction. The surviving all-H>=2 formula, including fractal Cantor repellers H>2 and the exact transport coefficient/correction, is not implied by the full-tent special case or optimal free-node quantization. Historical full-text gap in skew-tent paper remains real.

## value

PASS

The complete fixed-point census is a canonical reproducible way to approximate invariant measures of generalized tent repellers; exact W1 cost for every H>=2 and every period, especially fractal H>2, quantifies bias and the missing H^-2n term, while sharp Kolmogorov 2^-n separates order discrepancy from transport. It is a motivated complete parametric quantization law, not a few isolated orbit examples.

The dated certificate retains the supplied scientific assessment, sources and limitations.
