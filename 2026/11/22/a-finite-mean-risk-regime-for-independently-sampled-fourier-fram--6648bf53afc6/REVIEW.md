# Self-review

## Correctness — PASS

The claim addresses unnormalized consecutive Fourier sampling at \(N\ge3\) with independent Haar nodes. The collision lower estimate uses a unit coefficient vector with a zero of multiplicity \(N-1\), and its probability exponent is exactly \((m-1)/(2N-2)\). The complementary upper bound uses an exact Lagrange inverse, a stochastically dominated gamma variable, and the sum of \(k\) independent positive Gram matrices. The resulting inverse moments hold only for \(p<k/2\), never at the endpoint. The checker completed 5715 finite assertions. No finite sample is used as an infinite proof.

## Originality — PASS relative to inspected material

Xu–Shen (2026, Theorem 6, Appendix A.2) assert divergence in the same iid random-sampling model; the new tall-frame result gives a rigorous contrary finite regime at \(m\ge3N\). The earlier published exact square inverse-moment theorem covers \(m=N\) and can be combined with an elementary Gram-block argument to deduce a sufficient tall-model condition; that direct derivative connection is explicitly acknowledged. The two-mode circular sketch is a separate \(N=2\) result, and the Kunis–Nagel cluster estimate addresses a different row/column setting. The Bass–Gröchenig paper has a plausible title and condition-number abstract, but its full text could not be reviewed. Earlier implied coverage remains an explicit priority risk, not proof of original worldwide priority.

## Value — PASS

Unconditionally finite or infinite mean squared reconstruction error is a structural sampling-design distinction, not merely a fitted numerical improvement. The theorem supplies a uniform, dimension-scaled finite-risk regime and an all-cluster divergent regime, identifying a concrete limitation of universal-collision heuristics. The gap \(2N\le m<3N\) remains open by this method; no optimal threshold is claimed.

## Verification and limitations

The exact proof is in RESULT.md, with an independent supplementary executable CHECK.py. The sample size condition \(m\ge3N\) is sufficient only. A complete review of the older Bass–Gröchenig article was not possible. This review is not independent validation.

Self-review: passed. Independent audit: not yet performed.
