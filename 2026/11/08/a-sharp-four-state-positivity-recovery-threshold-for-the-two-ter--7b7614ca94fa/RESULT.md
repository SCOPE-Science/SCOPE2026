# A sharp four-state positivity-recovery threshold for the two-term Magnus exponential

## Finding

A two-term Magnus approximation to a nonautonomous continuous-time Markov chain can fail entrywise positivity for **every sufficiently small nonzero integrated rate**, yet recover it beyond a **unique, sharply determined positive rate**. This phenomenon already occurs on a four-state reverse-ordered pure-birth cascade.

Let \(G_i=E_{i,i+1}-E_{i,i}\) for \(i=1,2,3\), acting on row probability vectors. Activate \(G_3\), then \(G_2\), then \(G_1\) in three successive disjoint time intervals, each with integrated rate \(h\ge0\). The exact transition matrix is
\[
P_{\mathrm{exact}}(h)=e^{hG_3}e^{hG_2}e^{hG_1},
\qquad (P_{\mathrm{exact}}(h))_{14}=0.
\]
Let \(P_{[2]}(h)=\exp(\Omega_1(h)+\Omega_2(h))\) be the Magnus exponential retaining the first two terms, in the right-acting convention. Then
\[
(P_{[2]}(h))_{14}
=1-e^{-h}\left(1+h+\frac{h^2}{2}+\frac{h^3}{2}+\frac{h^4}{8}\right).
\]
There is a **unique positive root** \(h_*\) of
\[
e^{h_*}=1+h_*+\frac{h_*^2}{2}+\frac{h_*^3}{2}+\frac{h_*^4}{8},
\qquad h_*=5.20228372790060182518\ldots.
\]
The *entire* approximate transition matrix is entrywise nonnegative **if and only if** \(h=0\) or \(h\ge h_*\); for \(0<h<h_*\), its unique negative entry is the \((1,4)\) entry. Its most negative value is attained at \(h=\sqrt8\), where it equals \(-0.60425618932648555185\ldots\).

More generally, for every \(n\ge4\) and arbitrary fixed positive integrated-rate ratios \(a_1,\ldots,a_{n-1}\), activate the \(n-1\) pure-birth edges in the reverse order, with integrated rates \(ha_i\). Then the two-term Magnus map obeys
\[
(P_{[2],n}(h))_{14}=-\frac{a_1a_2a_3}{3}h^3+O(h^4)
\quad (h\downarrow0),
\]
and is therefore not nonnegative for all sufficiently small positive \(h\). By contrast, the two- and three-state **equal-rate** reverse cascades have nonnegative two-term Magnus maps for every \(h\ge0\). Four states are minimal within this equal-rate reverse-cascade family.

## Assumptions and scope

We use **row generators** and the right differential equation \(P'(t)=P(t)Q(t)\), \(P(0)=I\); this convention matters for commutator signs. For \(n\ge2\), \(G_i\) has a \(-1\) in position \((i,i)\), a \(+1\) in \((i,i+1)\), and zeros elsewhere. Let nonnegative integrable scalar functions \(\phi_{n-1},\ldots,\phi_1\) have pairwise disjoint supports in that chronological order, with \(\int\phi_i(t)\,dt=1\). The generator is \(Q_h(t)=h\sum_{i=1}^{n-1}a_i\phi_i(t)G_i\), with \(a_i>0\). These functions can in particular be smooth and compactly supported. All statements concern the exact exponential of the **truncated Magnus logarithm**, not truncation of the exponential series and not positivity of intermediate stages.

The chronological exact transition matrix is \(e^{ha_{n-1}G_{n-1}}\cdots e^{ha_1G_1}\), which is row-stochastic and nonnegative. The repeated-edge term \(\Omega_2\) is exactly a sum of chronological commutators because disjoint supports reduce the double integrals to products of total pulse masses.

## Proof

**1. Exact two-term logarithm.** By the right-acting Magnus convention,
\[
\Omega_1(h)=h\sum_{i=1}^{n-1}a_iG_i,
\qquad
\Omega_2(h)=\frac{h^2}{2}
\sum_{i=1}^{n-2}a_i a_{i+1}[G_{i+1},G_i].
\]
The only noncommuting generator pairs are adjacent. Direct matrix multiplication yields
\[
[G_{i+1},G_i]=E_{i,i+1}-E_{i,i+2}.
\]
Each \(G_i\) and each commutator annihilates the all-ones column, hence every \(\Omega_1+\Omega_2\) has zero row sums and its exponential has row sums one. This does **not** imply its entries are nonnegative.

**2. Exact four-state matrix.** With all \(a_i=1\), put \(u=h+h^2/2\) and \(v=h^2/2\). Then
\[
\Omega_1+\Omega_2=
\begin{pmatrix}
-h&u&-v&0\\
0&-h&u&-v\\
0&0&-h&h\\
0&0&0&0
\end{pmatrix}.
\]
The leading \(3\times3\) block is \(-hI+N\), where \(N^3=0\). Thus \(e^{-h}e^N=e^{-h}(I+N+N^2/2)\). Using zero row sums of the exponential to obtain its final column gives the complete explicit matrix
\[
P_{[2]}(h)=
\begin{pmatrix}
e^{-h}&ue^{-h}&e^{-h}(h^3/2+h^4/8)&1-e^{-h}p(h)\\
0&e^{-h}&ue^{-h}&1-e^{-h}(1+u)\\
0&0&e^{-h}&1-e^{-h}\\
0&0&0&1
\end{pmatrix},
\]
where \(p(h)=1+h+h^2/2+h^3/2+h^4/8\). Every entry other than position \((1,4)\) is nonnegative at all \(h\ge0\): in particular \(e^h>1+h+h^2/2=1+u\) for \(h>0\).

**3. Sharp sign interval and minimum.** Write \(F(h)=1-e^{-h}p(h)\). Direct differentiation simplifies to
\[
F'(h)=\frac18e^{-h}h^2(h^2-8).
\]
Therefore \(F\) decreases strictly from \(F(0)=0\) to a negative minimum at \(h=\sqrt8\), then increases strictly to \(\lim_{h\to\infty}F(h)=1\). By continuity and monotonicity there exists exactly one positive zero \(h_*>\sqrt8\), yielding the asserted if-and-only-if statement, minimum, and numerical root enclosure. The small-rate expansion is \(F(h)=-h^3/3+h^4/4+O(h^5)\).

**4. General dimension and weights.** Let \(A=\sum a_iG_i\) and \(B=\tfrac12\sum a_ia_{i+1}[G_{i+1},G_i]\), so the logarithm is \(hA+h^2B\). The coefficient of \(h^3\) in the exponential is
\[
\frac{A^3}{6}+\frac{AB+BA}{2}.
\]
The \((1,4)\) coefficient receives a direct triple-edge path \(a_1a_2a_3/6\) from \(A^3/6\) and two paths using one negative two-edge commutator shortcut, of weight \(-a_1a_2a_3/4\) each, from \((AB+BA)/2\). Summing them gives \(-a_1a_2a_3/3\). All coefficients of lower powers of \(h\) at this position vanish. Positivity fails for all sufficiently small positive \(h\) when \(n\ge4\). The exact reverse-ordered propagator has no \((1,4)\) transition at any \(h\) because edges needed to traverse from state one to state four have already switched off before their source state becomes occupied.

**5. Two and three states.** With three equal-rate states, the corresponding matrix is upper triangular with nonzero entries \(e^{-h}\) on the first two diagonal positions, \(u e^{-h}\) at \((1,2)\), \(1-e^{-h}\) at \((2,3)\), and \(1-e^{-h}(1+u)\) at \((1,3)\). All are nonnegative for all \(h\ge0\). The two-state case has a single generator and its Magnus exponential is exact. This establishes the minimal equal-rate reverse-cascade dimension.

## Verification

`verify_magnus.py` is a standalone Python 3 program using only the standard library. Execute `python3 verify_magnus.py` in the same directory as this file. It checks the ordered commutator logarithm and row conservation in exact fractions, tests the cubic coefficient for multiple dimensions and unequal positive rational rates in exact arithmetic, and independently computes the four-state matrix exponential using high-precision Taylor-series matrix multiplication. It also brackets the unique positive root and checks the sign/minimum formulas. A successful invocation prints `VERIFICATION_PASS` and a checked-assertion count; these finite checks are corroboration, not the proof of the infinite-dimensional quantifier or uniqueness, which are established algebraically above.

## Relationship to prior work

Iserles and Macnamara (arXiv:1701.02522, Sections 2 and 4.5) explicitly explain that truncating a Magnus expansion generally fails to preserve positivity because commutators of Markov generators need not themselves be Markov generators. That qualitative observation is **prior art** and is not claimed as new. Blanes, Iserles and Macnamara (arXiv:2102.08242, Sections 3.3 and 3.5) analyze positivity-preserving Magnus-type and commutator-free numerical approaches and emphasize the same commutator obstruction. Jasuja and Atzberger (arXiv:2212.08978, Sections 1–2) study Magnus exponential integrators for time-dependent stochastic systems, focusing on statistical structure and fluctuation-dissipation balance. The more narrowly evaluated distinction here is the *exact four-state if-and-only-if positivity set*, its maximum negative excursion, the three-state comparison, and the dimension-uniform cubic negative path law for reversed cascades. None of those exact claims was identified in the materially inspected portions of the cited articles; absence in these particular sources does not establish comprehensive publication priority.

## Limitations

The exact threshold is for three reverse-ordered **nonoverlapping unit-mass pure-birth pulses**, the right-acting two-term Magnus logarithm, and four equal-rate states. The general \(n\ge4\) statement proves local failure only; it does not claim an all-dimensional recovery threshold or positivity for unequal pulse orders. The restoration at large \(h\) is an *entrywise-sign fact*, not an accuracy guarantee; in particular the exact transition \((1,4)\) entry remains zero while the approximate entry eventually approaches one. The method can preserve total probability without preserving individual probabilities. Specialized prior-art overlap beyond the inspected primary sources remains possible. No independent mathematical review has been performed.

## References

1. A. Iserles and S. Macnamara, *Magnus expansions and pseudospectra of Master Equations*, arXiv:1701.02522 (first public January 10, 2017), https://arxiv.org/abs/1701.02522, especially Sections 2 and 4.5.
2. S. Blanes, A. Iserles, and S. Macnamara, *Positivity-preserving methods for population models*, arXiv:2102.08242 (first public February 16, 2021), https://arxiv.org/abs/2102.08242, Sections 3.3 and 3.5 (the HTML manuscript also bears the alternative title *Positivity-preserving methods for ordinary differential equations*).
3. D. Jasuja and P. J. Atzberger, *Magnus Exponential Integrators for Stiff Time-Varying Stochastic Systems*, arXiv:2212.08978 (first public December 18, 2022), https://arxiv.org/abs/2212.08978, Sections 1–2.
