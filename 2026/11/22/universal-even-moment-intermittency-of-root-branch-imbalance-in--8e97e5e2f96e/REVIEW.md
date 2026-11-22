# Review of root-branch imbalance moments

## Correctness: PASS

The claim is for every fixed positive integer order in the continuous-time root-clock embedding initialized immediately after the first doubling. The proof explicitly verifies the mass generator and a triangular positive moment hierarchy, conditions on the last rate-one Poisson root reset, decomposes each branch into independent Yule families, and bounds non-pairing moment partitions. Strict exponent inequalities justify neglect of all remainder terms, and dominated convergence gives the beta integral. Exact generator checks through order six provide a separate finite diagnostic, not an infinite proof. The initialization and clock rates matter; discrete-step asymptotics are not asserted.

## Originality: PASS under inspected evidence

The closest primary source is Björnberg and Mailler, *A random recursive tree model with doubling events* (arXiv:2501.18466, first public 2025-01-30). Its full accessible manuscript covers total-size moments at discrete times, degree and height statistics, and continuous-time Yule embedding, but not this root-daughter even-moment ratio. The accessible summary of *Exact Poisson-tilted leaf imbalance in a random tree with root doublings* treats global leaf imbalance, not daughter-subtree mass difference; the related root-doubling tree-size weak-limit records concern total mass alone. General Yule theory supplies a conditional distribution but does not itself supply the common-reset beta coefficient. Residual risk: a stronger general correlated-branch/reset-process moment theorem or unseen expanded text could subsume the claim. Lack of a match is not proof of novelty.

## Value: PASS

Root doublings enforce exact symmetry of the two daughter populations at each reset. The first-order total-size results do not quantify how that symmetry breaks between resets. The all-order ratio and explicit exponentially increasing moment exponents classify a natural fluctuation invariant of the original growth mechanism, including a non-Gaussian third-order change from the first two equal ratios. These facts aid analysis of large deviations and moment intermittency in coupled growth-and-duplication systems without asserting a distributional limit.

Self-review: passed. Independent audit: not yet performed.
