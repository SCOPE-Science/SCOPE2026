# All-time stochastic ordering of bouncing and bunching reflection in persistent lattice search

## Finding

Consider a finite one-dimensional correlated walk that is absorbed at its right endpoint and reflected at its left endpoint. There are two left-reflection protocols: **bouncing**, which changes a forbidden outward heading into an inward heading, and **bunching**, which retains the previous heading. Let \(T_{\mathrm{bounce}}\) and \(T_{\mathrm{bunch}}\) be their first absorption times, from the same initial position and heading.

**Theorem.** For every integer \(N\ge 2\), every \(f,b>0\) with \(f+b\le1\), every initial state strictly left of the target, and every integer \(t\ge0\),
\[
\operatorname{sgn}(f-b)\bigl[\Pr(T_{\mathrm{bounce}}\le t)-\Pr(T_{\mathrm{bunch}}\le t)\bigr]\ge0.
\]
For \(f>b\), bouncing is stochastically faster; for \(f<b\), bunching is stochastically faster; at \(f=b\), their entire first-passage laws coincide. If \(N\ge3\) and \(f\ne b\), for **every** initial state the inequality is strict for at least one finite time. At the degenerate size \(N=2\), it is strict at some time precisely when the initial heading points left; a right-facing walker immediately adjacent to the target never reaches the protocol-dependent state. The result extends to arbitrary mixtures of initial states by linearity, with the evident strictness condition.

The statement concerns all finite observation horizons, not only mean first-passage times or individual peaks of the probability mass function. An exact coefficientwise-positive generating-function factorization gives the sign.

## Assumptions and scope

The sites are \(\{1,\ldots,N\}\), with \(N\) absorbing. Before absorption the internal heading is \(h\in\{-1,+1\}\). In one discrete time step, the walker moves one site along its existing heading with probability \(f>0\); reverses heading and moves one site in the opposite direction with probability \(b>0\); or stays in place with heading unchanged with probability \(c=1-f-b\ge0\). An attempted move to site \(0\) instead leaves position at site \(1\). Under bouncing, the new heading is \(+1\); under bunching, the previous heading is retained. Thus the sole protocol distinction is the fate of an outward continuation from \((1,-1)\): its probability \(f\) moves to \((1,+1)\) under bouncing but stays at \((1,-1)\) under bunching. A reversed step from \((1,+1)\) already leaves heading \(+1\) under both. First arrival at \(N\) causes immediate absorption, regardless of arrival heading.

All claims quantify over the finite state space \(\mathcal S=\{1,\ldots,N-1\}\times\{+1,-1\}\), all allowed positive \(f,b\), all allowed laziness \(c\), and all nonnegative integer observation times. Because \(f,b\) are strictly positive, a rightward run of positive probability is available from every state, so absorption occurs almost surely under either protocol.

## Proof

Write \(Q_{\mathrm B}\) and \(Q_{\mathrm U}\) for the substochastic transient transition matrices, with row indexed by the initial state and column by the next state. Here \(\mathrm B\) means bouncing and \(\mathrm U\) means bunching. Let \(w=(1,-1)\), \(u=(1,+1)\), and \(e_i\) denote a unit coordinate column. The outgoing absorption probabilities are identical under both protocols. The exact rank-one difference is
\[
Q_{\mathrm B}-Q_{\mathrm U}=f e_w(e_u-e_w)^{\mathsf T}.
\]
For \(0\le z<1\) define the first-hitting generating functions \(F_i^{\mathrm B}(z)=\mathbb E_i[z^{T_{\mathrm B}}]\), \(F_i^{\mathrm U}(z)=\mathbb E_i[z^{T_{\mathrm bunch}}]\), and the nonnegative matrix resolvent
\[
R_{\mathrm B}(z)=(I-zQ_{\mathrm B})^{-1}=\sum_{k=0}^{\infty}z^kQ_{\mathrm B}^k.
\]
First-step conditioning and the common one-step absorption vector imply the resolvent identity
\[
F_i^{\mathrm B}(z)-F_i^{\mathrm U}(z)
=zf[R_{\mathrm B}(z)]_{i,w}\,[F_u^{\mathrm U}(z)-F_w^{\mathrm U}(z)].\tag{1}
\]
Under **bunching** at the left boundary, let \(H(z)=F_{(2,+1)}^{\mathrm U}(z)\) for \(N\ge3\), and set \(H(z)=1\) for \(N=2\), where site \(2\) is already absorbing. The two exact boundary first-step equations are
\[
F_u^{\mathrm U}=z\{fH+(b+c)F_u^{\mathrm U}\},\qquad
F_w^{\mathrm U}=z\{bH+(f+c)F_w^{\mathrm U}\}.
\]
Solving and using \(f+b+c=1\) gives
\[
F_u^{\mathrm U}(z)-F_w^{\mathrm U}(z)
=\frac{z(f-b)(1-z)H(z)}{[1-(b+c)z][1-(f+c)z]}.\tag{2}
\]
Because the first-hit times are integer-valued, the cumulative distribution differences have generating function \((F_i^{\mathrm B}-F_i^{\mathrm U})/(1-z)\). Combining (1) and (2) yields the exact identity
\[
\boxed{\sum_{t\ge0}\bigl[\Pr_i(T_{\mathrm B}\le t)-\Pr_i(T_{\mathrm U}\le t)\bigr]z^t
=(f-b)\frac{fz^2[R_{\mathrm B}(z)]_{i,w}H(z)}{[1-(b+c)z][1-(f+c)z]}.}\tag{3}
\]
Every coefficient in the final fraction is nonnegative: matrix powers of a substochastic kernel are nonnegative; \(H(z)\) is a first-hit probability generating function; and the geometric factors expand with nonnegative coefficients, since \(b+c=1-f\ge0\) and \(f+c=1-b\ge0\). Coefficientwise comparison proves the claimed sign simultaneously for all \(t\), including equality at \(f=b\).

For sharpness, take \(f\ne b\). If \(N\ge3\), any initial transient state can reach \(w\) before absorption by a finite sequence of permitted moves of strictly positive probability. From \(w\), the factor \(H\) includes at least one positive-probability path to absorption. Therefore the nonnegative factor in (3) is not the zero series, so the sign is strict for at least one finite horizon. At \(N=2\), the only transient initial state from which \(w\) can be visited is \(w\) itself; this proves the stated small-size exception. This exhausts all cases.

## Verification

The standalone `check.py` implements both protocols as separate rational-arithmetic substochastic Markov matrices, checks the rank-one difference, independently computes the first-hitting cumulative distributions, and reconstructs all coefficients in identity (3) using finite convolutions of nonnegative series. Running `python3 check.py` with Python's standard library produces `PASS 17760 exact rational temporal identities and sign checks across 40 finite systems`. The test cases include \(N=2,3,4,5,6\), both signs of \(f-b\), \(f=b\), lazy and non-lazy motion, every initial transient heading and site, and horizons through time \(36\). The proof above establishes the infinite-horizon theorem; these finite checks only test its implementation and special cases.

## Relationship to prior work

Marris and Giuggioli (2024) introduced and compared these two reflective interactions for correlated lattice random walks, including a complete transition-matrix setup in Section VII (their equation (34)) and numerical first-passage distributions in Figure 9. They observe enhanced intermediate-time second peaks under bouncing in a strong-persistence example. Their general propagator and first-passage formulas do not themselves state the present exact sign factorization or the uniform **cumulative** stochastic ordering for all time horizons, all positive persistence or anti-persistence parameters, and arbitrary starting states. A probability-mass-function comparison in an example cannot be substituted for such a statement: the individual time-density differences need not have one sign. The present result instead follows from the rank-one wall perturbation and the explicit bunching wall equations.

Related work on one-dimensional active first passage and partially reactive or sticky boundaries addresses continuous-time run-and-tumble absorption, not this pair of discrete-heading reflection protocols. A separate published result on a non-sticky persistent particle in an asymmetric finite interval optimizes a capture rate, not the reflection-protocol order. Searches for equivalent first-passage stochastic-order and coupling statements found no demonstrably covering theorem; non-indexed equivalent formulations cannot be ruled out.

## Limitations

This theorem uses a **fully absorbing right endpoint**, a single left reflecting endpoint, and direction-retaining lazy steps. It does not assert stochastic ordering for partially absorbing interior targets, two simultaneously reflecting endpoints, nonuniform bulk probabilities, or asymmetric turning. It does not assert pointwise ordering of first-hit probability mass functions. The public record may contain an unindexed equivalent theorem; the source comparison supports best-knowledge originality, not a uniqueness guarantee. No independent scientific validation has been conducted.

## References

1. D. Marris and L. Giuggioli, *Persistent and anti-Persistent Motion in Bounded and Unbounded Space: Resolution of the First-Passage Problem*, arXiv:2404.13360, first submitted 20 April 2024; *New Journal of Physics* **26** (2024), 073020, doi:10.1088/1367-2630/ad5d85. Sections II, V-VII and Appendix A. https://arxiv.org/html/2404.13360v2
2. V. Malakar et al., *Steady state, relaxation and first-passage properties of a run-and-tumble particle in one dimension*, *J. Stat. Mech.* (2018), 043215, arXiv:1711.08474. Different continuous-time model and boundary dynamics.
