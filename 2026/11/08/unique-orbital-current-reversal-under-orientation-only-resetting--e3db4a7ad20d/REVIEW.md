# Self-review

## Correctness — PASS

The proof closes the first two angular harmonics and the two complex position-heading mixed moments exactly under the joint Markov generator. The stationary \(XY\) balance reduces the Stratonovich circulation to those mixed moments, yielding a rational function with strictly positive denominator. A sign-variation argument establishes exactly one positive polynomial root for every \(a>3/2\) and \(t>0\); it also handles the borderline \(a=3/2\). Independent additive Brownian forcing cancels from the relevant mean quantities. Replaying the standard-library checker produces 237 deterministic assertions, including a separate reset-age numerical quadrature. Numerical finite tests do not substitute for the algebraic proof.

## Originality — PASS, subject to priority risk

The closest primary sources are Baouche et al., arXiv:2405.06769 (orientation-only resets without a trap or chiral torque); Caprini et al., arXiv:2306.11133 (elliptic confinement plus chirality without resetting); Shee, arXiv:2409.06920 (harmonic confinement with simultaneous resetting of both position and orientation), and Olsen and Löwen, arXiv:2405.14326 (relative-angle Poisson tumbles and free-space diffusion). The relevant accessible full texts, including model sections and results, were inspected. Their published statements do not imply a unique orientation-only-reset rate that reverses orbital circulation under fixed positive angular drift in an anisotropic trap. The algebraic threshold is not a mere parameter substitution in any of those claims. Relevant broader reset literature may remain unindexed or inaccessible and could alter publication priority; absence from searches does not prove novelty.

## Mathematical value — PASS

The theorem resolves a physically motivated transport-control problem: when can a reset rule reverse an angular current without changing the swimmer's intrinsic rotation direction? It gives a sharp stiffness threshold at high reset rates, an exact unique zero for the full nontrivial regime, and robustness to independent translational noise. The broad continuous parameter classification, rather than an arbitrarily chosen special case, is the central value.

## Limits

Angular Brownian diffusion, oblique reset directions, non-Poisson reset laws, positional resets, and the full intermediate-rate classification below the stiffness boundary lie outside the theorem. Independent scientific audit has not been performed.

Self-review: passed. Independent audit: not yet performed.
