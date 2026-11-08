# Two distinct allocation bifurcations for a two-type careless collector

## Finding

Consider a discrete-time collector with two equally likely labels. Each round acquires its drawn label and then independently erases each currently held label \(i\) with probability \(p_i\); completion is checked **after** erasure. Fix the total loss budget \(B=p_1+p_2\in(0,1)\), allowing \(p_i=0\). Write
\[
q_i=1-p_i,\qquad s=q_1+q_2=2-B,\qquad t=q_1q_2.
\]
The feasible interval for \(t\) is \([s-1,s^2/4]\); its left endpoint corresponds to concentrating all loss on one label, and its right endpoint to equal losses. Let \(\Pi\) be the stationary probability of holding both labels, and \(H\) the expected first post-erasure completion time starting empty. Both admit exact expressions:
\[
\boxed{\Pi(s,t)=\frac{t(s-t)}{4-2s+t},\qquad
H(s,t)=\frac{(5-s)t+4-2s}{t(s-t)}.}
\]

Define four loss-budget thresholds
\[
\begin{aligned}
B_{\Pi,-}&=\sqrt2-1\approx0.4142135624,\\
B_{\Pi,+}&=2\sqrt5-4\approx0.4721359550,\\
B_{H,-}&=2-\sigma_-\approx0.5719932683,\\
B_{H,+}&=2-\sigma_+\approx0.7074055727,
\end{aligned}
\]
where \(\sigma_-\) is the unique root of \(-u^3+5u^2-3u-3=0\) in \((1,2)\), and \(\sigma_+\) is the unique root of \(u^3-u^2+12u-16=0\) in \((1,2)\). They obey
\[
0<B_{\Pi,-}<B_{\Pi,+}<B_{H,-}<B_{H,+}<1.
\]

**Complete stationary-availability optimum.** The unique optimal \(t\) maximizing \(\Pi\) is \(s-1\) if \(B\le B_{\Pi,-}\), is \(s^2/4\) if \(B\ge B_{\Pi,+}\), and otherwise is
\[
t_{\Pi}=\sqrt{(4-2s)(4-s)}-(4-2s).
\]
**Complete first-arrival optimum.** The unique optimal \(t\) minimizing \(H\) is \(s-1\) if \(B\le B_{H,-}\), is \(s^2/4\) if \(B\ge B_{H,+}\), and otherwise is
\[
t_H=\frac{\sqrt{(4-2s)^2+s(5-s)(4-2s)}-(4-2s)}{5-s}.
\]
Each interior optimum gives precisely the two allocations obtained by interchanging
\[
p_{1,2}=1-\frac{s\pm\sqrt{s^2-4t}}2.
\]
At the equal or boundary endpoint, the optimal allocation is unique up to permutation. The two objectives select different allocations **if and only if**
\[
\boxed{\sqrt2-1<B<2-\sigma_+.}
\]
For the concrete budget \(B=1/2\), stationary availability is uniquely maximized at \((p_1,p_2)=(1/4,1/4)\), giving \(\Pi=27/80\) and \(H=152/27\), whereas first-arrival speed is uniquely optimized (up to interchange) at \((0,1/2)\), giving \(H=11/2\) and \(\Pi=1/3\). Hence maximizing stationary availability can give a **strictly slower** expected first completion.

## Assumptions and scope

Each draw is uniform and independent, all loss decisions are independent across labels and rounds, and the loss probabilities remain fixed. The state is the **post-loss** set. The budget is restricted to \(B\in(0,1)\), including one zero-loss label but not allowing an impossible-to-retain label. We optimize over the entire closed feasible budget segment, not just interior positive losses. The stationary distribution is unique: for two positive loss probabilities the four-state chain is irreducible and aperiodic; if one loss probability is zero, there is a single accessible recurrent class containing that eventually permanent label. The hitting time from empty has finite expectation because there is a uniform positive chance of completing on any suitable two-round acquisition sequence.

## Proof

Write the post-loss state as \(\emptyset,\{1\},\{2\},\{1,2\}\), and define \(q_i=1-p_i\). The transition matrix, indexed in this order, is
\[
P=\begin{pmatrix}
1-(q_1+q_2)/2&q_1/2&q_2/2&0\\
(1-q_1)(2-q_2)/2&q_1(2-q_2)/2&(1-q_1)q_2/2&q_1q_2/2\\
(1-q_2)(2-q_1)/2&(1-q_2)q_1/2&q_2(2-q_1)/2&q_1q_2/2\\
(1-q_1)(1-q_2)&q_1(1-q_2)&(1-q_1)q_2&q_1q_2
\end{pmatrix}.
\]
All rows sum to one. In stationarity, if \(m_i\) denotes the probability label \(i\) is held, the one-label balance equation reads \(m_i=q_i(1+m_i)/2\), so \(m_i=q_i/(2-q_i)\). For both labels to survive the round, the old state must contain the label **not** drawn; thus the stationary full-state mass is
\[
\Pi=\frac{q_1q_2}{2}(m_1+m_2)
=\frac{q_1q_2(q_1+q_2-q_1q_2)}{(2-q_1)(2-q_2)}
=\frac{t(s-t)}{4-2s+t}.
\]
For hitting times \(h_0,h_1,h_2\) from the three nonfull states, first-step analysis gives
\[
\begin{pmatrix}h_0\\h_1\\h_2\end{pmatrix}
=\begin{pmatrix}1\\1\\1\end{pmatrix}
+P_{\{0,1,2\},\{0,1,2\}}
\begin{pmatrix}h_0\\h_1\\h_2\end{pmatrix}.
\]
Eliminating these three equations (with \(h_{\{1,2\}}=0\)) yields
\[
h_0=\frac{q_1^2q_2+q_1q_2^2-5q_1q_2+2q_1+2q_2-4}{q_1q_2(q_1q_2-q_1-q_2)}
=\frac{(5-s)t+4-2s}{t(s-t)}.
\]
The first numerator and denominator are simultaneously negative, so the ratio is positive; the transformed second expression is manifestly positive.

At fixed \(s\in(1,2)\), elementary differentiation gives the signs
\[
\operatorname{sgn}\partial_t\Pi
=\operatorname{sgn}D_{\Pi}(t),\qquad
D_{\Pi}(t)=(4-2s)(s-2t)-t^2,
\]
\[
\operatorname{sgn}\partial_tH
=\operatorname{sgn}D_H(t),\qquad
D_H(t)=(5-s)t^2+2(4-2s)t-s(4-2s).
\]
The former is strictly decreasing and the latter strictly increasing throughout the feasible interval, so there is exactly one maximum and one minimum, respectively, attained at either an endpoint or the unique interior zero. The endpoint tests are
\[
\begin{array}{ll}
D_{\Pi}(s-1)=s^2-6s+7,&
D_{\Pi}(s^2/4)=-s(s-4)(s^2-12s+16)/16,\\
D_H(s-1)=-s^3+5s^2-3s-3,&
D_H(s^2/4)=-s(s-4)(s^3-s^2+12s-16)/16.
\end{array}
\]
Their unique crossings inside \((1,2)\), together with the ordering of those crossings, give the four thresholds above. For example, \(D_{\Pi}(s-1)=0\) at \(s=3-\sqrt2\), while \(D_{\Pi}(s^2/4)=0\) at \(s=6-2\sqrt5\). The quadratic formula gives the interior roots. The other two endpoint polynomials each have exactly one root in \((1,2)\): \(u^3-u^2+12u-16\) is strictly increasing there; the derivative of \(-u^3+5u^2-3u-3\) is positive there because \(-3u^2+10u-3>0\) on \([1,2]\). The four roots are strictly ordered by direct substitution and elementary sign bounds (or rational interval enclosures). Since no two interior regimes overlap, the two optimizers agree precisely on the two outer budget intervals, including their endpoints. Direct substitution at \(B=1/2\) yields the asserted strict contrast.

## Verification

The included `verify_two_coupon.py` uses exact rational linear algebra on the four-state chain and independently compares the stationary mass and first-hit expectation against both closed forms at hundreds of parameter pairs, including zero-loss boundaries. It also checks derivative monotonicity, both exact values for \(B=1/2\), and numerical finite-mesh objective envelopes across 199 fixed budgets. Execute with `python3 verify_two_coupon.py` in the extracted package. The finite checks support the symbolic calculations; the optimization for all real budgets follows from the derivative-sign proof, not the mesh.

## Relationship to prior work

Cruciani and Dudeja (2026, arXiv:2602.20705) introduce the post-loss careless model with one common loss probability and explicitly propose type-dependent loss probabilities as a future direction. Their count-chain algorithm and asymptotic results do not solve this heterogeneous fixed-budget optimization. Long (2026, arXiv:2605.14511) establishes stationary-entry asymptotics for the uniform-loss careless collector; its unequal-selection reset-button model has a different global-reset transition. Kleiner (2026, doi:10.3390/math14203729) studies fragile *unseen* coupons that disappear before discovery and become safe thereafter, not repeatable post-acquisition erasure. The elementary Markov-chain and one-dimensional calculus tools used here are standard; the claimed distinction is the complete two-type, two-objective allocation classification.

## Limitations

The exact classification covers two coupon types and total loss budget strictly between zero and one, with **uniform acquisition**. It does not claim a general-\(n\) Schur-convexity law, arbitrary sampling probabilities, a stochastic order between completion times, or any global asymptotic phase transition as the number of types grows. The equal-budget stationary optimum is not itself an optimizer of initial completion time except in the specified extreme budget ranges. External priority remains subject to broader historical Markov reliability and cache-availability literature; comparison of the inspected directly relevant papers found no covering theorem. Independent audit has not been performed.

## References

- E. Cruciani and A. Dudeja, *The Careless Coupon Collector's Problem*, arXiv:2602.20705, first publicly posted 2026-02-24. https://arxiv.org/abs/2602.20705
- C. D. Long, *Clumsy and Careless: Stationary-Entry Flux in Non-monotone Coupon Collectors*, arXiv:2605.14511, first publicly posted 2026-05-14. https://arxiv.org/abs/2605.14511
- I. Kleiner, *The Fragile Coupon Collector: Random Deadlines, Critical Fragility, and Optimal Sampling*, Mathematics 14 (2026), 3729. https://doi.org/10.3390/math14203729
