# Two logarithmic scales of Gini amplification in the binomial death semigroup

## Finding
Fix an integer \(n\ge2\). The pure-death (independent survival) Markov semigroup on states \(\{0,\ldots,n\}\) is
\[
 (P_{n,t}f)_i=\sum_{j=0}^{i}\binom{i}{j}e^{-tj}(1-e^{-t})^{i-j}f_j,\qquad t\ge0.
\]
With complete-pair Gini seminorm
\[
 G_n(f)=\sum_{0\le i<j\le n}|f_i-f_j|,
 \quad \gamma_n(t)=\sup_{G_n(f)>0}\frac{G_n(P_{n,t}f)}{G_n(f)},
\]
the following assertions all hold. Put \(p=e^{-t}\) and \(q=1-p\).

1. **Finite bounds and a sharp small-survival expansion.** For every \(0<p\le1\),
\[
 \frac1n\sum_{i=0}^{n}(n-2i)q^i\ \le\ \gamma_n(-\log p)\ \le\ \min\left\{\frac1p,\frac{\lfloor(n+1)^2/4\rfloor}{n}\right\},
\]
and
\[
 \left|\gamma_n(-\log p)-\frac{(n+1)(n+2)}6p\right|
 \le\frac{n(n+1)(n-1)}2p^2.
\]
2. **Two uniform limiting regimes.** Along any positive sequence \(p_n\), if \(np_n\to0\), then
\[
 \gamma_n(-\log p_n)\sim\frac{n^2p_n}{6}.
\]
If \(np_n\to\infty\), then
\[
 \gamma_n(-\log p_n)\sim\frac1{p_n}.
\]
3. **Logarithmic time scales.** For any fixed real \(s\), at \(t=\log n+s\) the coefficient is of order \(n\):
\[
 0<F(e^{-s})\le\liminf_{n\to\infty}\frac{\gamma_n(\log n+s)}n
 \le\limsup_{n\to\infty}\frac{\gamma_n(\log n+s)}n\le\frac14,
\]
where
\[
 F(c)=\int_0^1(1-2u)e^{-cu}\,du
 =\frac{c-2+(c+2)e^{-c}}{c^2}>0 \quad(c>0).
\]
At the later scale \(t=2\log n+s\),
\[
 \lim_{n\to\infty}\gamma_n(2\log n+s)=\frac{e^{-s}}6.
\]
Thus for fixed \(s<-\log6\) this late-window coefficient eventually exceeds one, while for fixed \(s>-\log6\) it is eventually below one. This asserts a sharp crossover **within that window**, not uniqueness of a finite-dimensional threshold at all times.
4. **Separation from oscillation contraction.** The classical Dobrushin oscillation coefficient is exactly
\[
 \delta_n(t)=1-(1-e^{-t})^n.
\]
For \(np_n\to0\),
\[
 \frac{\gamma_n(-\log p_n)}{\delta_n(-\log p_n)}\sim\frac n6.
\]
In particular the Gini coefficient can be of constant size while the oscillation coefficient tends to zero.

These statements concern the operator seminorm, not the Gini dispersion of a randomly sampled population size. The finite-dimensional exact norm for arbitrary \(n,p\) is not claimed.

## Assumptions and scope
All inputs are real-valued vectors on \(\{0,\ldots,n\}\) with equal site weights; \(G_n\) sums all unordered pairs once. There is one independent per-individual exponential death clock of rate one, hence survival parameter \(p=e^{-t}\). The matrix has nonnegative entries and every row sums to one. At \(t=0\) it is the identity, and \(t=\infty\) denotes the constant limit operator. Limits in \(n\) are taken along integers \(n\ge2\). No reversible measure or stationary-weighted seminorm is used.

## Proof
**1. Semigroup and finite geometry.** Independent survival gives the binomial transition matrix \(B_{n,p}\) and \(B_{n,p}B_{n,r}=B_{n,pr}\), since surviving two independent Bernoulli filters is Bernoulli with parameter \(pr\). For any nonconstant real vector \(f\),
\[
 n\operatorname{osc}(f)\le G_n(f)
 \le\left\lfloor\frac{(n+1)^2}{4}\right\rfloor\operatorname{osc}(f).
\]
The lower bound pairs a minimum and maximum with every other coordinate; the upper bound follows by writing \(f\) as an integral of binary superlevel-set indicators, each contributing \(k(n+1-k)\) to \(G_n\). Since \(B_{n,p}\) preserves the range, its Gini norm is at most the upper-to-lower geometric ratio stated in part 1.

**2. The \(1/p\) bound.** The column masses satisfy
\[
 \sum_{i=0}^{n}B_{n,p}(i,j)
 \le\sum_{i=j}^{\infty}\binom{i}{j}p^j(1-p)^{i-j}=\frac1p.
\]
It suffices by the same superlevel-set decomposition to estimate \(g=B_{n,p}\mathbf1_S\), where \(S\) is a nonempty proper set with \(k=|S|\). Replace \(S\) by its complement when necessary, so \(1\le k\le(n+1)/2\). Let \(N=n+1\) and \(M=\sum_i g_i\le k/p\). For \(0\le g_i\le1\), the elementary pairwise comparison
\[
 |g_i-g_j|\le g_i(1-g_j)+g_j(1-g_i)
\]
gives \(G_n(g)\le M(N-M)\). If \(M\le k\), monotonicity of \(x(N-x)\) on \([0,N/2]\) bounds this by \(k(N-k)\). If \(M>k\), then \(M(N-M)\le(k/p)(N-k)\). Since \(p\le1\), in either case \(G_n(g)\le k(N-k)/p\). Integrating binary cuts proves \(\gamma_n\le1/p\).

**3. Exact endpoint lower bound.** For \(f=\mathbf1_{\{0\}}\), the input seminorm is \(n\), whereas \((B_{n,p}f)_i=q^i\). This sequence is decreasing, so
\[
 G_n(B_{n,p}f)=\sum_{i=0}^{n}(n-2i)q^i,
\]
proving the first lower bound. Direct finite summation yields
\[
 \frac1p-\frac{G_n(B_{n,p}f)}n
 =\frac{q^{n+1}}p+
 \frac{2q}{np^2}\left[1-(n+1)q^n+nq^{n+1}\right].
\]
The bracket lies in \([0,1]\). Consequently the lower-bound deficit relative to \(1/p\) is at most \(q^{n+1}+2q/(np)\), which tends to zero whenever \(np\to\infty\). This proves the large-survival regime, even when \(p\) depends on \(n\).

**4. Uniform small-survival expansion.** Define the rank-one modulo constants operator
\[
 (L_{n,p}f)_i=f_0+ip(f_1-f_0).
\]
By \(G_n(f)\ge n|f_1-f_0|\) and
\[
 \sum_{0\le i<j\le n}(j-i)=\frac{n(n+1)(n+2)}6,
\]
its exact induced Gini norm is \(p(n+1)(n+2)/6\), attained by \(f=\mathbf1_{\{0\}}\). Let \(X_i\sim\operatorname{Bin}(i,p)\). The inequalities
\[
 ip-\Pr(X_i=1)\le i(i-1)p^2,\qquad
 \Pr(X_i\ge2)\le\tbinom{i}{2}p^2
\]
show that the remainder \(r_i=(B_{n,p}f)_i-(L_{n,p}f)_i\) satisfies
\[
 |r_i|\le\tfrac32i(i-1)p^2\operatorname{osc}(f).
\]
Then
\[
 G_n(r)\le n\sum_{i=0}^n|r_i|
 \le\frac12n^2(n+1)(n-1)p^2\operatorname{osc}(f).
\]
Division by \(G_n(f)\ge n\operatorname{osc}(f)\) bounds the operator remainder by \(\frac12n(n+1)(n-1)p^2\). The reverse triangle inequality for operator seminorms proves the expansion in part 1. When \(np\to0\), this error divided by its leading term is \(O(np)\), proving the small-survival asymptotic.

**5. The two logarithmic windows.** When \(p=e^{-s}/n\), the endpoint lower bound divided by \(n\) is a Riemann sum converging to
\[
 \int_{0<u<v<1}(e^{-cu}-e^{-cv})\,du\,dv=F(c),
 \qquad c=e^{-s}.
\]
The integral is strictly positive because its integrand is positive on a set of positive measure. The universal finite-dimensional bound from step 1 gives the upper limit \(1/4\). When \(p=e^{-s}/n^2\), the uniform expansion from step 4 instead gives \(\gamma_n\to e^{-s}/6\).

**6. Oscillation comparison.** Every binomial row assigns mass at least \(q^n\) to state zero, so the total-variation distance between any two rows is at most \(1-q^n\). The rows corresponding to zero and \(n\) attain this distance exactly. The Dobrushin formula therefore gives \(\delta_n=1-q^n\). If \(np\to0\), then \(\delta_n\sim np\) while step 4 gives \(\gamma_n\sim n^2p/6\), and their ratio tends to \(n/6\) in the stated asymptotic sense, i.e. \(\gamma_n/\delta_n\sim n/6\). This concludes all assertions.

## Verification
The independent exact-rational script `check_binomial_death.py` reconstructs the binomial transition matrix, enumerates all binary cuts through nine states at several rational parameters, tests the finite upper and lower bounds and small-survival error, and verifies exact semigroup and Dobrushin identities on additional sizes. Run with `python check_binomial_death.py`. The script is supplementary finite evidence; the unrestricted claims rest on the inequalities and limits proved above.

## Relationship to prior work
Steutel and van Harn introduced the binomial-thinning operation in their 1978 memorandum and 1979 Annals of Probability paper, particularly the Bernoulli-sum definition and probability-generating-function substitution. Their subject is discrete self-decomposability and stability, not the complete-pair operator seminorm on finite bounded state spaces. Gaubert and Qu's 2013 preprint (and its later expanded article) establishes Dobrushin/Hopf-oscillation and dual total-variation contraction formulas; those coefficients differ from the present Gini seminorm. A published dimension-dependent general Gini–oscillation comparison is consistent with, but does not determine, the exact asymptotic ratio \(n/6\), the small-survival expansion, or the two logarithmic windows. A related study of critical-tail thinning concerns survivor distributions, rather than an operator seminorm on all real test functions. None of the inspected statements supplies the theorem here; undiscovered equivalent prior results remain a historical risk.

## Limitations
No exact finite-\(n\) closed form for \(\gamma_n(t)\) is asserted outside the displayed bounds. The first-window limit \(\gamma_n(\log n+s)/n\) is bounded, not shown to exist or to equal the endpoint-witness integral. The late-window threshold is asymptotic and does not assert uniqueness or monotonicity of finite-dimensional crossings. The oldest thinning memorandum was dated by month in the inspected copy; its exact public-release day was not established and has not been fabricated.

## References
- F. W. Steutel and K. van Harn, *Discrete analogues of self-decomposability and stability*, Eindhoven Memorandum COSOR 78-07 (March 1978), https://research.tue.nl/files/1719387/340666.pdf ; *Annals of Probability* 7 (1979), 893–899, DOI:10.1214/aop/1176994950.
- S. Gaubert and Z. Qu, *Dobrushin ergodicity coefficient for Markov operators on cones, and beyond*, arXiv:1302.5226 (first submitted February 21, 2013), https://arxiv.org/abs/1302.5226.
- S. Gaubert and Z. Qu, *Dobrushin’s ergodicity coefficient for Markov operators on cones*, https://www.cmap.polytechnique.fr/~gaubert/PAPERS/GaubertQuIEOTD14QuFinal.pdf.
