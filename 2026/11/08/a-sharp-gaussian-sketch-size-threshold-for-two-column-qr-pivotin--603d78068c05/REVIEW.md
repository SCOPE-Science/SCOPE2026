# Scientific review: A sharp Gaussian sketch-size threshold for two-column QR pivoting

## Correctness — PASS

The theorem fixes two independent nonzero real columns, arbitrary ambient dimension at least two, and an integer number of independent Gaussian sketch rows. The denominator is the smaller of the two squared least-squares *column-projection* errors, not the SVD optimum; it is strictly positive under the rank-two assumption. Projection onto the longer column leaves residual \(\|a\|_2^2(1-\rho^2)\), whereas projection onto the shorter one leaves \(t^2\) times as much. Orthogonal invariance converts the wrong-pivot event to a sum of independent indefinite Gaussian quadratic forms. Its two eigenvalues have opposite signs; independent rotation of every coordinate produces two independent chi-square variates, whose ratio gives the exact symmetric-beta probability.

The correlation extremizer follows because the beta threshold increases strictly with \(1-\rho^2\). The symmetric-beta CDF is bounded above by the uniform CDF on the lower half for \(k\ge2\), yielding an input-uniform strict risk bound below two. The \(k=1\) divergence, \(k=2\) sharp supremum, and \(k=4\) rational optimizer are derived exactly. The high-contrast constant follows from the small-argument beta asymptotics. These steps prove the continuum claims without relying on finite numerical enumeration. The included standard-library diagnostic replays rational identities, exact derivatives, Gaussian event simulations and bounded-range comparisons; these are supplementary checks rather than an infinite-domain certificate.

## Originality — PASS, qualified

The 2015 primary works of Martinsson (arXiv:1505.08115) and Martinsson et al. (arXiv:1512.02671) motivate Gaussian-sketch QR pivot selection, together with the original 2015 randomized QRCP paper and its 2020 revised analysis; the revised paper's Bayesian treatment concerns the uncertainty of individual sketched column norms. Xiao–Gu–Langou (2018) provide high-probability reliability bounds for randomized QRCP, rather than the joint correlated two-column event and its complete mean-risk optimization. Melnichenko et al. (2023), examined through the full public text and Appendix A, establish rank-revealing and numerical-stability results for a different complete algorithm, not a sharp expected first-pivot, one-column projection risk constant. Their broader results do not state or algebraically determine the uniform four-sketch-row constant \((17+7\sqrt7)/27\) or the sharp one-versus-two-row expected-loss threshold.

Related publicly indexed results on multistage adaptive randomized pivoting and complete-pivot ACA use distinct selection laws and loss objectives; their statements do not imply the exact event on two correlated Gaussian-sketched columns. Simple beta-distribution identities are classical and not claimed as new; the claimed contribution is their sharp all-input numerical-algorithm risk classification. Originality remains limited by publication-precedence uncertainty: the 2015 predecessor's full text was not materially accessible, and an older specialized first-pivot analysis could imply parts or all of the theorem. This warrants independent literature verification.

## Value — PASS

The motivating numerical tradeoff is the minimum Gaussian sketch size needed to make expected truncated approximation loss bounded uniformly over ill-conditioned two-column inputs. This is a natural first step in randomized QR column pivoting, not an arbitrary parameter evaluation. The theorem supplies an exact all-correlation failure distribution, proves that one sketch row has unbounded worst-case expected loss whereas two rows have sharp supremum two, and computes a nontrivial attained global four-row constant. It separates expected loss from high-probability reliability and provides a reference test case for sketched pivoting and oversampling choices.

## Limits and closest sources

The result does not describe subsequent QR pivots, full CQRRPT output, SVD-optimal rank-one approximation, finite-precision behavior, or non-Gaussian sketches. The cited papers give broader algorithmic settings but were compared at statement and implication level; no independent formal or human audit has occurred. The public 2015 precursor was inspected only at the abstract level. Source references and detailed comparisons are in RESULT.md and AUDIT.json.

Self-review: passed. Independent audit: not yet performed.
