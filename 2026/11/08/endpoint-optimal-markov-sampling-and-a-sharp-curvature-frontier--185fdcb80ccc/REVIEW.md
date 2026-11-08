# Review of the exact Markov-sampling stationary-risk frontier

## Correctness — PASS

The four moments \(\mathbb Ey\), \(\mathbb E[yS]\), \(\mathbb Ey^2\), and \(\mathbb E[y^2S]\) close under the affine two-state iteration. Both mode maps are strict contractions in the stated step range, so the exact fixed point is the limiting covariance for every deterministic initial iterate, including the two nonmixing endpoints. A strictly positive quadratic denominator and the factored endpoint differences reduce the global comparison to one derivative sign. Those signs follow from an explicit sum of nonnegative terms or an elementary sign inequality. The exact symbolic and rational checker tests those identities, but the proof of the continuum statement is analytic. Risk: an extension outside the uniform-contraction range is not covered.

## Originality — PASS with residual precedence risk

Mathieu Even's two-state equal-curvature example in Appendix D.2 of arXiv:2302.14428 is expressly acknowledged; the equal-curvature correlation formula is not counted as new. The present result concerns heterogeneous quadratic curvatures, optimizes the **stationary** error across every symmetric transition probability (including the degenerate endpoints), and proves a sharp curvature threshold. Doan et al. (arXiv:2003.10973) provide finite-time convergence bounds with diminishing steps; Liu and Xu (arXiv:1810.03124) couple samples within minibatches, so their mechanisms do not imply the transition-level optimizer classification. Semantic searches of mathematical records and comparisons with accessible preceding work found no equivalent claim. Risk: a general Markov-jump affine-system optimization theorem may indirectly cover the exact formula or optimizer, and independent publication-precedence checks remain necessary.

## Value — PASS

Markov sampling can trade mixing against error rather than simply improve with negative correlation: at sufficiently large stable steps, *more* persistent sampling can have lower stationary risk even though it sacrifices exploration. The exact phase boundary \(t=1/2\) separates curvature regimes in which this reversal is possible or impossible. The result is a direct sampling-design diagnostic for a natural, noninterpolating stochastic-gradient model, not merely a one-off numerical table or routine perturbation.

## Limitations

This is a two-component scalar quadratic theorem at positive constant step under symmetric stationary sampling. Perfect persistence does not optimize the full objective consistently; it only minimizes the specified stationary risk among these schedules in the identified regime. Literature coverage remains best-knowledge, and no independent specialist audit has been performed.

Self-review: passed. Independent audit: not yet performed.
