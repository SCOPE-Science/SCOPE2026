# Scientific review

## Correctness — PASS

The result fixes the covariance normalization and proves strict positive definiteness from the positive periodized Fourier spectrum. The real-line order-two inverse transform yields the lattice symbol \(f(\theta)=(A+B\cos\theta)/(1+r^2-2r\cos\theta)^2\), where \(0<B<A\). Exact polynomial division, absolute convergence, and finite cyclic periodization give every precision entry. At cyclic distance at least two, the geometric term proves nonzero alternating signs. The nontrivial nearest-neighbor case follows from an explicit strict inequality for even orders and a monotonic odd-order comparison with the strictly negative three-site inverse. The finite-distance truncation estimate follows by a geometric tail bound. The order-one comparison is a Laurent-polynomial inverse symbol. A standalone verifier constructs the covariance independently, tests the explicit precision and signs, and compares the Fourier spectrum at 60-digit precision. Numerical tests do not replace the proof for arbitrary \(n\) and \(\kappa\).

## Originality — PASS (provisional priority)

The directly relevant 2016 Guinness–Fuentes paper establishes the circular Matérn model, positive definiteness, and covariance representations; these are treated as existing tools. Huang–Li's January 2022 manuscript specifically derives the exact order-one nearest-neighbor CAR and an order-two **approximating** CAR covariance, rather than the exact order-two grid-sampled inverse and its all-distance noncancellation signs. Lindgren–Rue–Lindström's sparse finite-element precision is a different discretized object and is not identical to point-sampling precision. Comparisons therefore turn on the implication between the full sampling inverse and prior theorems, not the terminology. General ARMA inverse theory, cyclic oscillation/total-positivity theorems, and possible unlocated equivalent formulae present residual priority risk. Search failure is not a priority proof. The accessible scholarly record inspected does not provide this exact sign-and-support conclusion.

## Mathematical value — PASS

Gaussian precision zeros encode exact conditional independences. The sharp contrast between a nearest-neighbor inverse for first-order circular Matérn and a complete, sign-alternating inverse for second order resolves a concrete statistical-structural question raised by attempts to relate circular Matérn fields to sparse conditional autoregressions. The explicit finite-grid geometric tail bound quantifies approximate locality without mistaking small entries for zeros, useful in interpreting sparse approximate samplers and truncations. This is an all-size statement, not an arbitrary small-case census or routine renaming.

## Sources and remaining risks

C. Huang and A. Li, *The Circular Matérn Covariance Function and its Link to Markov Random Fields on the Circle*, arXiv:2201.12856, Sections 2–3 and appendices, first posted January 30, 2022. J. Guinness and M. Fuentes, *Isotropic covariance functions on spheres: Some properties and modeling considerations*, J. Multivariate Analysis 143 (2016), 143–152, Example 3 and supplement. F. Lindgren, H. Rue and J. Lindström, *An explicit link between Gaussian fields and Gaussian Markov random fields*, JRSS B 73 (2011), 423–498, Section 2 and Result 2. J. N. Haddad, *On the closed form of the covariance matrix and its inverse of the causal ARMA process*, J. Time Series Analysis 25 (2004), 443–448; abstract inspected, full text unavailable. An older general inverse/total-positivity classification may imply the signs and would change the priority assessment.

Self-review: passed. Independent audit: not yet performed.
