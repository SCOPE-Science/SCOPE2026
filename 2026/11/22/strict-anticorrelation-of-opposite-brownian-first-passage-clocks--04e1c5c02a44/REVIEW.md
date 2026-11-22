# Mathematical review: strict anticorrelation of opposite Brownian first-passage clocks

## Correctness — PASS

For Brownian motion with generator \(D\partial_{xx}\), Poisson return-to-zero rate \(r>0\), and targets \(-a,+b\) with \(a,b>0\), the clocks continue after the first target is visited. Discounted two-sided first-exit transforms yield the joint exit-side transforms \(G_\pm\). Strong Markov continuation from the actual first-hit boundary yields the other-hit transforms \(H_\pm\), giving a complete bivariate Laplace transform. Differentiation and symbolic rational elimination establish

\[
\operatorname{Cov}(T_-,T_+)=-\frac{A+B}{r^2}\frac{\sinh A\sinh B}{\sinh A+\sinh B}<0,\quad A=a\sqrt{r/D},\;B=b\sqrt{r/D}.
\]

The symbolic checker verifies the full identity and weak-reset cancellation exactly. Independent numerical high-precision mixed derivatives and a finite-lattice Markov generator provide separate sanity checks. Boundary assumptions, conditional-clock definitions, moment finiteness, and the distinction between numerical evidence and general proof are explicit in RESULT.md. The primary calculations passed under the supplied parameters; finite tests alone cannot prove the continuous claim.

## Originality — PASS, with residual priority risks

The closest paper, Linn and Lawley, *Cover times with stochastic resetting* (arXiv:2406.12154v1, Section 2.1; first posted June 17, 2024), evaluates the **mean of the maximum** of two first-visit times for the same persistent two-target process, and does not provide their joint transform or covariance in the inspected primary sections. Pal and Prasad, *First passage under stochastic resetting in an interval* (arXiv:1812.03009v1), study **absorption at the first hit**, not both continuing clocks; their first-exit formulas are reused explicitly. Calvert and Evans, *Searching for clusters of targets under stochastic resetting* (European Physical Journal B 94, 228 (2021), Section 2), **restart at the origin upon the first target hit**, so their time-to-second-discovery law is different. A related published reflected-interval cover-time variance result was compared through its accessible scientific summary only, not unread full text. Relevant aliases, exact parameters, secondary claims, and semantic scientific-record searches are specified in AUDIT.json.

The newly assessed item is the **exact cross moment and strict negative covariance of two persistent, opposite first-hit clocks**, plus their weak-reset mixed-moment cancellation, not the elementary one-target mean or known cover-time mean. Search failure alone is not proof of global novelty; unindexed joint first-passage literature and the inaccessible reflected-variance full text are explicit residual risks.

## Mathematical value — PASS

A single particle's two opposite-target discovery times are coupled by their common trajectory and reset clock. Their exact anticorrelation for every positive rate, every pair of target distances, and the singular weak-reset cancellation answer a motivated multi-target reliability question not contained in scalar mean cover times. This is a structural sign theorem with a full bivariate transform, not a numerical point, arbitrary special case, or routine code certificate. The result does not claim negative quadrant dependence or extensions to different resetting/absorption mechanisms.

Self-review: passed. Independent audit: not yet performed.
