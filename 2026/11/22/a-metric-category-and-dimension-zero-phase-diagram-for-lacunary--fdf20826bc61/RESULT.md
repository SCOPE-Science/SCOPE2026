# A metric-category and dimension-zero phase diagram for lacunary two-atom Kaczmarz recovery

## Finding

Fix an odd integer \(b\ge3\), a mass \(0<\alpha<1\), and a separation \(t\in(0,1)\). On the two-dimensional complex Hilbert space \(H_t=L^2(\alpha\delta_0+(1-\alpha)\delta_t)\), observe a target vector by the unit Fourier vectors \(e_n(x)=e^{2\pi i n x}\), but retain only the geometrically separated indices
\[
n_j=\frac{b^j-1}{b-1},\qquad j=0,1,2,\ldots.
\]
Let \(Q_j=I-e_{n_j}\otimes e_{n_j}\) be the orthogonal residual projector and let \(E_N(t)=\|Q_NQ_{N-1}\cdots Q_0\|\), the worst-case residual after \(N+1\) exact measurements. Put \(m_\alpha=|2\alpha-1|\) and
\[
h_\alpha(x)=|\alpha+(1-\alpha)e^{2\pi ix}|=\sqrt{1-4\alpha(1-\alpha)\sin^2(\pi x)}.
\]
The following statements all hold.

1. **Exact residual and the complete success/failure boundary:** For every \(N\ge1\),
\[
E_N(t)=\prod_{j=0}^{N-1}h_\alpha(b^j t).
\]
The sampled Kaczmarz algorithm recovers every vector (equivalently \(E_N(t)\to0\)) **if and only if** \(t\notin\mathbb Z[1/b]\pmod1\). For the excluded, countable dense set of \(b\)-adic rational separations, the residual norm stays eventually constant and strictly positive.

2. **Lebesgue-typical exact exponential rate:** For Lebesgue-almost every \(t\in(0,1)\),
\[
\lim_{N\to\infty} E_N(t)^{1/N}=\max\{\alpha,1-\alpha\}.
\]
This includes the balanced case \(\alpha=1/2\), for which the rate is \(1/2\).

3. **Baire-typical opposite extremes, but Hausdorff dimension zero:** A dense \(G_\delta\) subset of non-\(b\)-adic separations (excluding any exact-zero factors) satisfies
\[
\liminf_{N\to\infty}E_N(t)^{1/N}=m_\alpha,
\qquad
\limsup_{N\to\infty}E_N(t)^{1/N}=1.
\]
Every separation in this set still yields \(E_N(t)\to0\). More sharply, the entire set of separations satisfying \(\limsup_{N\to\infty}E_N(t)^{1/N}=1\) has Hausdorff dimension zero, despite being dense \(G_\delta\).

4. **No gaps in attainable rates for unequal atom masses:** When \(\alpha\ne1/2\), every \(\lambda\in[m_\alpha,1]\) is realized as an ordinary limit \(\lim_{N\to\infty}E_N(t)^{1/N}=\lambda\) by a separation \(t\notin\mathbb Z[1/b]\); in particular, the rate \(1\) can coexist with successful recovery.

## Assumptions and scope

The Hilbert space is complex, both atomic masses are strictly positive, the atoms are distinct, the integer base is odd and at least three, and each update is the unrelaxed orthogonal Kaczmarz step with noiseless inner-product data. The operator norm of the residual equals the supremum of reconstruction errors over unit target vectors. A rate of one means subexponential convergence, not failure. Only these two-atomic measures and these prescribed geometric gaps are covered. The motivating full Fourier sequence uses every nonnegative integer rather than the retained subsequence.

## Proof

**The two-dimensional product identity.** Identify \(H_t\) unitarily with \(\mathbb C^2\), taking \(e_n\) to the unit vector \((\sqrt\alpha,\sqrt{1-\alpha}\,e^{2\pi i n t})\). Every \(Q_j\) is rank one. If \(u_j\) is a unit vector spanning its range, rank-one multiplication gives
\[
\|Q_N\cdots Q_0\|=\prod_{j=0}^{N-1}|\langle u_{j+1},u_j\rangle|.
\]
For two-dimensional complementary rank-one projections, the absolute overlap of the complementary vectors equals that of the original Fourier vectors. The difference \(n_{j+1}-n_j=b^j\), so each factor is \(h_\alpha(b^jt)\). This also proves the normalization and the exact finite-\(N\) formula, including zeros.

**Exact effectiveness.** On the circle, \(h_\alpha(x)=1\) only at \(x=0\). If \(t=k/b^r\pmod1\), then \(b^jt=0\pmod1\) for all \(j\ge r\), hence the product becomes constant. It is positive: when \(\alpha\ne1/2\), no factor can vanish; when \(\alpha=1/2\), a zero would require \(b^jt=1/2\pmod1\), impossible for a fraction with odd denominator. Conversely, if \(b^jt\) does not tend to zero on the circle, there are infinitely many \(j\) whose distance to zero is at least some \(\delta>0\), so infinitely many factors are bounded above by a fixed constant smaller than one, forcing the product to zero. Finally, if \(b^jt\to0\pmod1\), choose signed representatives \(y_j\in(-1/(2b),1/(2b))\) for all sufficiently large \(j\). Then \(y_{j+1}=by_j\), because the next representative has no modular wrap. Boundedness forces \(y_j=0\) eventually; thus \(t\) is \(b\)-adic. This proves both directions.

**Almost-everywhere rate.** The circle map \(T_bx=bx\pmod1\) preserves Lebesgue measure and is ergodic (its base-\(b\) digits form the one-sided Bernoulli shift). The function \(f_\alpha(x)=\log h_\alpha(x)\) is integrable, even at \(\alpha=1/2\), where its only logarithmic singularity lies at \(x=1/2\). Birkhoff's theorem gives the almost-everywhere limit of \(N^{-1}\log E_N(t)\). Jensen's circle integral, or elementary averaging of the logarithm of a linear polynomial, yields
\[
\int_0^1\log|\alpha+(1-\alpha)e^{2\pi ix}|\,dx
=\log\max\{\alpha,1-\alpha\}.
\]
Exponentiation proves the claimed rate.

**Baire extremes.** Since \(m_\alpha\le h_\alpha\le1\), every positive \(N\)-th root lies in \([m_\alpha,1]\). The preimages of \(0\) under powers of \(T_b\) are dense. At each such separation with distinct atoms the product is eventually a fixed positive constant, so its \(N\)-th root tends to one. Thus for every \(r\ge2\) and \(M\ge1\), the open set
\[
\bigcup_{N\ge M}\{t:E_N(t)^{1/N}>1-1/r\}
\]
is dense. Similarly the preimages of \(1/2\) are dense; because \(b\) is odd, \(1/2\) is fixed by \(T_b\). At such a separation the root tends to \(m_\alpha\) when it is positive, and after finitely many updates becomes zero when \(m_\alpha=0\). Hence the open set
\[
\bigcup_{N\ge M}\{t:E_N(t)^{1/N}<m_\alpha+1/r\}
\]
is also dense. Baire's theorem, followed by deletion of the countable sets of \(b\)-adic rationals and finite-termination phases, gives the asserted dense \(G_\delta\) set with both extremal subsequential rates and nevertheless successful recovery.

**Hausdorff dimension of the maximally slow upper-rate set.** Let \(S=\{t:\limsup_NE_N(t)^{1/N}=1\}\). Write \(F(x)=-\log h_\alpha(x)\ge0\) with the value \(+\infty\) at a zero. For \(\delta=b^{-2}\), there is \(c_\delta>0\) such that \(F(x)\ge c_\delta\) whenever the circle distance of \(x\) from zero is at least \(\delta\). Every \(t\in S\) admits arbitrarily long prefixes of length \(N\) for which fewer than \(\varepsilon N\) orbit positions have circle distance at least \(\delta\), for each fixed \(\varepsilon>0\). In the canonical base-\(b\) digit expansion of \(t\), any orbit position closer than \(b^{-2}\) to zero has its next two digits either both zero or both \(b-1\). Call all other adjacent digit pairs bad. It follows that for infinitely many lengths \(N\) the first \(N+1\) digits contain at most \(\varepsilon N\) bad adjacent pairs. The number of such words is bounded by
\[
b\sum_{k\le\varepsilon N}\binom Nk b^k
\le b(N+1)\exp\bigl(N[H(\varepsilon)+\varepsilon\log b]\bigr),
\]
where \(H(\varepsilon)=-\varepsilon\log\varepsilon-(1-\varepsilon)\log(1-\varepsilon)\), for \(0<\varepsilon<1/2\). Each word gives an interval of diameter \(b^{-(N+1)}\). The sum of their \(s\)-dimensional costs over all \(N\) converges whenever \(H(\varepsilon)+\varepsilon\log b<s\log b\). Thus the limsup cover has Hausdorff dimension at most \([H(\varepsilon)+\varepsilon\log b]/\log b\). Letting \(\varepsilon\downarrow0\) gives \(\dim_H S=0\) because \(S\) is nonempty. The previous paragraph also shows that \(S\) is dense \(G_\delta\).

**Realization of every intermediate rate.** Suppose \(m_\alpha>0\); then \(f_\alpha\) is continuous and \(f_\alpha(0)=0\), \(f_\alpha(1/2)=\log m_\alpha\). Write the digit \(c=(b-1)/2\); the constant base-\(b\) word \(cccc\cdots\) represents \(1/2\). For \(0<p<1\), form a digit sequence by concatenating blocks of \(0\)'s of lengths asymptotic to \((1-p)k\) and blocks of \(c\)'s of lengths asymptotic to \(pk\), for successive \(k=1,2,\ldots\). The frequency of \(c\)-digits tends to \(p\), while the fraction of positions within any fixed distance of a block boundary tends to zero. Away from boundaries, the shifted digit string begins with an arbitrarily long constant block; uniform continuity of \(f_\alpha\) therefore shows that its ergodic average tends to \(p\log m_\alpha\). The resulting separation is not \(b\)-adic and has ordinary root rate \(m_\alpha^p\). The endpoint \(m_\alpha\) is achieved by \(t=1/2\). For the endpoint one, use an infinite digit string with \(c\) only in square-numbered positions and zero elsewhere; the bad-position density is zero, the root rate is one, and the algorithm still converges since the separation is not \(b\)-adic. Taking \(p=\log\lambda/\log m_\alpha\) gives the entire interval.

## Verification

The embedded standalone program `verify_lacunary_kaczmarz.py` evaluates the actual two-by-two complex residual projector products independently of the scalar product identity, using three odd bases, five atomic masses, four off-resonance phases, and seven nontrivial horizons. It also checks the exact antipodal factor at half-turn phases, rational tail stabilization, and representative finite ergodic averages. It reports `LACUNARY_KACZMARZ_MATRIX_DIAGNOSTIC_OK 537`. Finite tests corroborate the algebraic identity but do not establish the infinite-time, category, or Hausdorff-dimension assertions; those are established above.

## Relationship to prior work

Berner, Herr and Jorgensen (arXiv:2611.03358, first public version 2 November 2026) classify unconditional reconstruction for effective stationary Fourier sequences and discuss finitely atomic measures, but the analysis concerns the full consecutive Fourier sequence, not the geometrically thinned observation schedule. Kwapień and Mycielski (2001) provide the foundational effectiveness criterion for stationary sequences. The present result instead treats a prescribed nonstationary lacunary subsequence of a two-atom stationary sequence: it gives an exact arithmetic success boundary, the almost-everywhere Lyapunov rate, a Baire-opposite oscillation, a zero-dimensional exceptional set, and full interpolation of rates for unequal masses. Contemporary results on cyclic finite-atomic Fourier Kaczmarz rates and on regular-polygon perturbative continuum limits were compared; their sequential or cyclic settings do not imply this lacunary arithmetic and category classification. The proof uses standard rank-one geometry, ergodic averaging and symbolic digit counting; no new general ergodic theorem is asserted.

## Limitations

The base must be odd for the antipodal phase to be fixed. The statements have not been extended to even bases, more than two atoms, noisy measurements, or arbitrary irregular gaps. The category and metric results are not uniform finite-horizon bounds. The embedded finite diagnostic is not a certificate for the infinite assertions. Unindexed literature on irregular Kaczmarz sampling and general cocycle multifractals could contain related or stronger implications; no claim of comprehensive bibliographic uniqueness or independent validation is made.

## References

- C. Berner, J. E. Herr and P. E. T. Jorgensen, *Frame properties of effective stationary sequences*, arXiv:2611.03358 (first public version 2 November 2026), https://arxiv.org/abs/2611.03358.
- S. Kwapień and J. Mycielski, *On the Kaczmarz algorithm of approximation in infinite-dimensional spaces*, Studia Math. 148 (2001), 75–86, https://doi.org/10.4064/sm148-1-7.
- W. Czaja and J. Tanis, *Kaczmarz algorithm and frames*, arXiv:1409.8310, https://arxiv.org/abs/1409.8310.
- The standard pointwise ergodic theorem and Jensen's circle integral are used in their usual forms.
