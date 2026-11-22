# The exact convex-order dual for two-exit renewal resetting and a gambler's-ruin obstruction

## Finding

Consider independent, repeated attempts ending at one of two terminal outcomes. The outcome probability under a renewal reset clock is a ratio of two expectations. We determine exactly when a *mean-preserving spread of the reset clock* can only increase, or can only decrease, this outcome probability.

For the definitions below, let \(\mathcal R\) be the class of integrable, positive-integer reset deadlines \(R\) satisfying \(\mathbb E b_R>0\). Define \(u_j=a_j/b_j\) for indices with \(b_j>0\), and
\[
 u_- = \inf_{j:b_j>0}u_j,\qquad u_+=\sup_{j:b_j>0}u_j,
 \qquad \Delta^2 f_i=f_{i-1}-2f_i+f_{i+1}.
\]
**Exact dual:** The implication
\[
 R\le_{\mathrm{cx}}S \quad\Longrightarrow\quad Q(R)\ge Q(S)
\]
holds for *every* pair of clocks in \(\mathcal R\) if and only if, at *each* integer \(i\ge2\), both
\[
 \Delta^2a_i-u_-\Delta^2b_i\le0,
 \qquad \Delta^2a_i-u_+\Delta^2b_i\le0.
\]
The reverse universal ordering, \(Q(R)\le Q(S)\), holds if and only if both inequalities are reversed for every \(i\ge2\). Neither ordering is inferred just from the convexity of \(a_i/b_i\); the ratio of expectations matters.

**Sharp geometric consequence:** For an ordinary nearest-neighbour walk on \(\{0,1,\dots,2m\}\), \(m\ge2\), with arbitrary fixed right-step probability \(0<p<1\), reset to its initial site \(z\), **the midpoint \(z=m\) is exactly the only site at which a universal convex-order response is possible**. At the midpoint the lower-exit probability is independent of every admissible clock and equals \((1-p)^m/(p^m+(1-p)^m)\). At each other site there are two explicit one-step mean-preserving spreads of deterministic clock deadlines that produce *opposite* strict changes in the lower-exit probability. Hence neither universal direction is true away from the midpoint.

## Assumptions and scope

An attempt has an almost-surely finite, positive-integer completion time \(T\) and terminal label \(J\in\{0,1\}\), without assuming independence of \(T\) and \(J\). Choose label \(0\) as the desired outcome. Set
\[
 a_n=\Pr(T\le n,J=0),\qquad b_n=\Pr(T\le n),\qquad n\ge1,
\]
with \(a_0=b_0=0\). Then \(0\le a_n\le b_n\le1\) and both sequences increase to their terminal probabilities (\(b_n\to1\)). Each attempt uses a new independent copy of \((T,J)\), interrupted by an independent positive-integer clock \(R\). Completion at a tied clock time \(T=R\) counts as completion, not interruption. A clock is *admissible* when \(\mathbb E b_R>0\), and is integrable when \(\mathbb ER<\infty\). Under a reset, all input randomness is freshly sampled. The eventual probability of label \(0\) is
\[
 Q(R)=\frac{\mathbb Ea_R}{\mathbb Eb_R}.
\]
For integrable random variables, \(R\le_{\mathrm{cx}}S\) means \(\mathbb E\phi(R)\le\mathbb E\phi(S)\) for every convex \(\phi\) for which both expectations exist; this implies equal means. The theorem compares only such clock pairs and imposes no higher moments on the clock. Its criterion contains two endpoint inequalities even when neither extremal ratio is achieved at a finite deadline.

## Proof

**1. Renewal reduction.** The probability that one independent attempt ends with label \(0\) before interruption is \(\mathbb E a_R\), and the probability it ends with either label is \(\mathbb E b_R\). Attempt count is geometric with success parameter \(\mathbb E b_R>0\). Summing over attempts gives the expression for \(Q(R)\). Equivalently, writing \(b_j>0\) and \(u_j=a_j/b_j\),
\[
 Q(R)=\frac{\sum_j \Pr(R=j)b_j u_j}{\sum_j\Pr(R=j)b_j}\in[u_-,u_+].
\]
This interval statement remains valid if the extrema are not attained.

**2. Discrete convex-order summation identity.** For \(R\le_{\mathrm{cx}}S\), define, for \(i\ge1\),
\[
 c_i=\mathbb E(i-S)_+-\mathbb E(i-R)_+
 =\mathbb E(S-i)_+-\mathbb E(R-i)_+.
\]
Every \(c_i\ge0\), \(c_1=0\), and \(c_i\to0\) because the clocks have finite, equal means. For their mass-function difference \(d_j=\Pr(S=j)-\Pr(R=j)\), direct differencing yields \(d_j=c_{j-1}-2c_j+c_{j+1}\), with \(c_0=c_1=0\). Therefore, for \(h=a\) or \(h=b\),
\[
 \mathbb Eh_S-\mathbb Eh_R=\sum_{i=2}^{\infty}c_i\Delta^2h_i.\tag{1}
\]
The interchange is legitimate: the first differences of each cumulative probability are nonnegative and summable, so \(\sum_i|\Delta^2 h_i|\le2\), and \(c_i\) is bounded and tends to zero. Truncating the summation-by-parts identity has vanishing boundary terms. This is an exact infinite-lattice identity, not a finite truncation approximation.

**3. Dual curvature certificate.** Subtract \(Q(R)\mathbb Eb_S\) from \(\mathbb Ea_S\), use (1), and divide by the positive denominator. This gives the exact signed formula
\[
 Q(S)-Q(R)=\frac{1}{\mathbb Eb_S}
 \sum_{i=2}^{\infty}c_i
 \bigl(\Delta^2a_i-Q(R)\Delta^2b_i\bigr).\tag{2}
\]
An admissible \(R\le_{\mathrm{cx}}S\) has admissible \(S\): if \(S\) were a.s. below the first possible completion deadline, the convex function \(x\mapsto(x-j)_+\) would force the same of \(R\). For fixed \(i\), the expression in parentheses in (2) is affine in the scalar \(Q(R)\in[u_-,u_+]\). Its two endpoint values are nonpositive exactly when its value is nonpositive throughout this interval. Since \(c_i\ge0\), the two displayed curvature inequalities suffice. Reversing signs yields the reverse-order sufficiency.

**4. Necessity and exactness.** Fix any \(i\ge2\) and a deadline \(j\) with \(b_j>0\). For \(0<\epsilon<1\), let \(R_\epsilon\) put mass \(1-\epsilon\) at \(j\) and mass \(\epsilon\) at \(i\); if \(j=i\) this is simply the point mass at \(i\). Let \(S_{\epsilon,\eta}\) replace a mass \(\eta\) at \(i\) by equal masses \(\eta/2\) at each of \(i-1\) and \(i+1\), where \(0<\eta\le\epsilon\). This elementary mean-preserving spread proves \(R_\epsilon\le_{\mathrm{cx}}S_{\epsilon,\eta}\), and both are admissible. Exactly,
\[
 Q(S_{\epsilon,\eta})-Q(R_\epsilon)
 =\frac{\eta}{2\,\mathbb Eb_{S_{\epsilon,\eta}}}
 \bigl(\Delta^2a_i-Q(R_\epsilon)\Delta^2b_i\bigr).
\]
As \(\epsilon\downarrow0\), \(Q(R_\epsilon)\to u_j\). If the universal response has one sign for all admissible clocks, the corresponding curvature expression has that sign at every \(u_j\). Taking the infimum and supremum over such \(j\) gives the required two endpoint inequalities, without an attainment assumption. This completes both equivalences.

**5. Exact gambler's-ruin obstruction.** Put \(q=1-p\). A nearest-neighbour walk starting at \(z<m\) can reach the near boundary \(0\) in \(z\) steps, but first reaches the far boundary \(2m\) in \(k=2m-z\) steps; \(k\ge3\). Both exits occur only at times of parity \(z\). Consequently,
\[
 Q(k-2)=Q(k-1)=1,
 \qquad Q(k)=Q(k+1)<1,
\]
where \(Q(j)\) denotes the probability under deterministic deadline \(j\). Indeed \(k-2\ge z\), near-boundary paths have positive probability by then, and the first far-boundary path has strictly positive probability at \(k\); there is no exit at the intervening opposite-parity steps. For the first spread, use \(R\equiv k-1\) and \(S\in\{k-2,k\}\) with equal probabilities. Then \(Q(R)>Q(S)\). For the *oppositely directed* spread, use \(R\equiv k\) and \(S\in\{k-1,k+1\}\) equally; its extra positive near-only component gives \(Q(R)<Q(S)\). Both spreads preserve the mean of their respective deterministic clocks. Reflecting the state space yields the opposite inequalities for \(z>m\).

If \(z=m\), reflection bijects lower-first and upper-first paths of every possible length. The relative path weights are exactly \(q^m/p^m\), so \(a_n/b_n=q^m/(p^m+q^m)\) whenever \(b_n>0\), and every admissible clock has that same splitting probability. The midpoint is thus both necessary and sufficient for a universal convex-order direction in this family.

## Verification

The included standalone `checker.py` uses only Python standard-library exact fractions. It replays the convex-order stop-loss identity and the resulting signed response formula on integer-clock probability grids. It checks both strictly opposite gambler's-ruin spreads for even intervals of lengths \(4,6,8,10\), three exact right-step probabilities, and every non-midpoint start, as well as midpoint neutrality. It reports **4,221 passed exact-rational assertions**. These are finite regression checks; the equivalences for all admissible clocks and all horizons are proved analytically in Sections 2–4 above.

To reproduce, run `python checker.py` in the same folder. No external datasets or third-party Python modules are required.

## Relationship to prior work

Newton and Vega Coso [1] derive the renewal splitting formula, exact duality for hazard-rate/likelihood-ratio clock comparisons, and midpoint neutrality, and identify the convex-order clock dual as an open problem in Section 10.3. Equation (2) supplies a new two-endpoint curvature dual for that specifically named order, while the gambler's-ruin construction shows a sharp obstruction not implied by their hazard-rate result. Their results about the same walk under *other* clock orders are credited here. Vidmar [2] treats universal restarting comparisons for a single completion time, not the two-outcome splitting ratio under two convex-ordered clocks. Pal et al. [3] give local mean/variation criteria for selective outcomes; Belan [4] studies optimizing success probabilities by resetting. Neither source's accessible materials contain the universal convex-order two-clock criterion. No claim of an exhaustive historical novelty proof is made.

## Limitations

The universal test is for *positive-integer*, *integrable* renewal deadlines and almost-surely finite two-outcome completion times; it does not establish an analogous continuous-time criterion, nor any mean-residual-life dual. The criterion compares clock pairs with equal mean and does not turn the hazard-rate dual of [1] into a convex-order statement. The gambler's-ruin corollary concerns even intervals with strictly positive up/down transition probabilities; it does not classify odd intervals or spatially inhomogeneous chains. Historical results on fractional expectation orders may imply an equivalent general criterion and should be independently examined. Finite exact checks do not establish infinite claims.

## References

[1] T. Newton and J. A. Vega Coso, *Stochastic Orders of the Exit Pair and the Monotone Response to Resetting*, arXiv:2611.01756v1, first posted 2026-11-01, https://arxiv.org/html/2611.01756v1, especially Sections 2, 3, 4, 6, 10.3.

[2] M. Vidmar, *On laws exhibiting universal ordering under stochastic restart*, arXiv:1904.10495, 2019; Communications in Statistics - Theory and Methods 51 (2022), 1290–1305, https://arxiv.org/abs/1904.10495.

[3] S. Pal, L. Dagdug, D. Ghosh, D. Boyer, and A. Pal, *Universal criterion for selective outcomes under stochastic resetting*, arXiv:2502.09127 (2025), https://arxiv.org/abs/2502.09127.

[4] S. Belan, *Restart Could Optimize the Probability of Success in a Bernoulli Trial*, arXiv:1703.01486 (2017), https://arxiv.org/abs/1703.01486.
