# Scientific review: a universal mixed-angular Bergman Toeplitz threshold

## Correctness — PASS

On the normalized monomial basis of the power-weighted analytic Bergman space, the Toeplitz operator with symbol \(az+bz\bar z^2\) is a sum of weighted forward and backward one-step shifts with explicitly derived coefficients. Its self-commutator has only diagonal and distance-two bands. The exact rational identity for \(3A_n+B_n\) has a positive numerator for every \(n\ge0\) and \(q=\alpha+1>0\). The bounds \(C_n+C_{n-2}<2A_n\) prove positivity at and above \(|a|=3|b|\). For smaller ratios, long alternating-phase test vectors and the common large-degree limits show failure. This establishes the full necessity, sufficiency and equality boundary without relying on finite enumeration. The included standard-library checker passed 22,332 supplementary assertions.

## Originality — PASS, qualified

Fleeman–Liaw, arXiv:1707.09677, treat nonharmonic Bergman Toeplitz questions and mixed terms. Kim–Lee (2021) and their openly available 2022/2023 weighted-space paper examine two-term nonharmonic symbols; the latter's Theorem 2.8 is especially close but only states a necessary diagonal estimate for opposite angular degrees. Theorem 2.7 assumes equal signed angular degree and Theorem 2.6 covers a true mirror pair rather than a radially modified backward symbol. These hypotheses and implications were compared, not just publication titles. Additional semantic searches of published findings under exact symbols and weighted-shift aliases found adjacent but noncovering results. The possibility of an undiscovered historical equivalent remains; absence from search is not a priority certificate.

## Mathematical value — PASS

Oppositely directed angular terms form the smallest model in which cancellation of cross terms fails. The weaker scalar diagonal criterion allows ratios down to \(\sqrt3\), whereas the sharp all-vector criterion requires \(3\). The classification is exact across every real Bergman exponent \(\alpha>-1\), all complex coefficient phases and its critical boundary. This resolves a motivated full hyponormality problem rather than an arbitrary isolated calculation.

## Limits and further validation

There is no classification here for all nonharmonic bivariate polynomials, higher angular degrees, subnormality, or spectral type of the self-commutator. The standard-library program independently checks many finite values and forms but is not an infinite proof. Historical priority remains qualified by accessible-source coverage, and no independent mathematical validation has occurred.

Self-review: passed. Independent audit: not yet performed.
