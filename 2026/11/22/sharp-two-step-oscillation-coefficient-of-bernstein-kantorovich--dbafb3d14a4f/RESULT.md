# Sharp two-step oscillation coefficient of Bernstein–Kantorovich averaging

## Finding

For every integer \(n\geq1\), consider the classical Bernstein–Kantorovich Markov operator on real essentially bounded measurable functions on \([0,1]\):

\[
(K_nf)(x)=\sum_{k=0}^{n}\binom nk x^k(1-x)^{n-k}(n+1)
\int_{k/(n+1)}^{(k+1)/(n+1)}f(t)\,dt.
\]

Write \(\operatorname{osc}(f)=\operatorname*{ess\,sup}f-\operatorname*{ess\,inf}f\) for the input, and use the ordinary maximum minus minimum for polynomial outputs. The exact two-step oscillation coefficient is

\[
\boxed{\quad \sup_{\operatorname{osc}(f)>0}
 \frac{\operatorname{osc}(K_n^2f)}{\operatorname{osc}(f)}
 =1-\delta_n,\qquad
 \delta_n=\sum_{j=0}^{n}\min\{p_{n,j},p_{n,n-j}\}\quad}
\]

where

\[
p_{n,j}=(n+1)\binom nj\int_0^{1/(n+1)}t^j(1-t)^{n-j}\,dt.
\]

Every constant is attained by the indicator of the union of cells \((j/(n+1),(j+1)/(n+1))\) with \(j>n/2\). In contrast, the one-step oscillation coefficient of \(K_n\) is exactly one. More explicitly, for \(m\geq0\),

\[
\delta_{2m}=p_{2m,m}+2\sum_{j=m+1}^{2m}p_{2m,j}
\quad(m\geq1),\qquad
\delta_{2m+1}=2\sum_{j=m+1}^{2m+1}p_{2m+1,j}.
\]

The two-step contraction deficit is super-exponentially small as the polynomial degree increases. In the sharper parity-resolved form, as \(m\to\infty\),

\[
\delta_{2m}=\frac{e^{-1/2}}{m+1}\,
 \frac{\binom{2m}{m}}{(2m+1)^m}\bigl(1+O(m^{-1})\bigr),
\]
\[
\delta_{2m+1}=\frac{2e^{-1/2}}{m+2}\,
 \frac{\binom{2m+1}{m+1}}{(2m+2)^{m+1}}\bigl(1+O(m^{-1})\bigr).
\]

In particular \(\log\delta_n=-\tfrac12 n\log n+O(n)\). The first exact values of the coefficient \(1-\delta_n\) are \(1/2,2/3,57/64,116/125,3815/3888,16602/16807\) at degrees one through six, respectively.

## Assumptions and scope

The input functions are real and in \(L^\infty([0,1])\), identified almost everywhere. Each of the \(n+1\) averaging cells has positive length. For the definition of oscillation, a function with zero oscillation is excluded from the ratio. The output is the polynomial obtained after two applications of the *same* \(K_n\); \(n\) is a fixed positive integer before the dimension asymptotic is taken. The constant \(O(m^{-1})\) is uniform along each parity sequence, not in arbitrary changes to the averaging rule.

## Proof

**1. Positive two-step cell kernel.** Put \(b_{n,j}(t)=\binom njt^j(1-t)^{n-j}\), \(I_k=[k/(n+1),(k+1)/(n+1)]\), and

\[
A_{k,j}=(n+1)\int_{I_k}b_{n,j}(t)\,dt.
\]

Let \(\overline f_j=(n+1)\int_{I_j}f(t)\,dt\). Because \(\sum_j A_{k,j}=1\), the two-step operator is

\[
K_n^2f(x)=\sum_{j=0}^n P_x(j)\overline f_j,
\qquad P_x(j)=\sum_{k=0}^n b_{n,k}(x)A_{k,j}.
\]

Thus \(P_x\) is a probability vector whose entries are positive (including at endpoint inputs). The optimization over \(f\) is exactly the optimization over \(\overline f\in[0,1]^{n+1}\), after subtracting the essential infimum and dividing by the oscillation. Every such vector is realized by a cellwise constant input.

**2. Monotone-likelihood-ratio ordering.** For \(x<y\) and \(k<l\), the binomial minors

\[
b_{n,k}(x)b_{n,l}(y)-b_{n,l}(x)b_{n,k}(y)\geq0
\]

follow because \(b_{n,l}(t)/b_{n,k}(t)\) increases in \(t\in(0,1)\). The same monotone ratio and ordered, nonoverlapping cells show that for \(k<l\) and \(j<r\),

\[
A_{k,j}A_{l,r}-A_{k,r}A_{l,j}
=(n+1)^2\int_{I_k}\!\int_{I_l}
\bigl[b_{n,j}(t)b_{n,r}(s)-b_{n,r}(t)b_{n,j}(s)\bigr]ds\,dt\geq0.
\]

All two-by-two minors of the matrix product defining \(P_x(j)\) are therefore nonnegative by the Cauchy–Binet identity. The family \(P_x\) has monotone likelihood ratio in its cell index; in particular, for \(x<y\) the signed sequence \(P_y(j)-P_x(j)\) has at most one change from negative to positive. Hence its total-variation distance is the difference of some upper-tail probabilities:

\[
\operatorname{TV}(P_x,P_y)
=\max_{0\leq r\leq n+1}\left(\sum_{j=r}^{n}P_y(j)-\sum_{j=r}^{n}P_x(j)\right).
\]

Since binomial distributions are stochastically increasing in their parameter and \(A\) maps higher cell indices to stochastically higher output cells, every upper-tail probability of \(P_x\) is increasing in \(x\). Consequently every displayed upper-tail difference is bounded by its difference between \(x=0\) and \(x=1\), so

\[
\sup_{x,y}\operatorname{TV}(P_x,P_y)=\operatorname{TV}(P_0,P_1).
\]

The elementary dual identity between total-variation distance of probability vectors and the maximum difference of expectations of \([0,1]\)-valued test vectors proves that this is precisely the oscillation norm of \(K_n^2\).

**3. Endpoint crossing and sharp input.** At \(x=0\), \(P_0(j)=A_{0,j}=p_{n,j}\). Reflection of the cells gives \(P_1(j)=A_{n,j}=p_{n,n-j}\). For \(t\in(0,1/(n+1))\) and \(j<n/2\), \(b_{n,j}(t)>b_{n,n-j}(t)\), with the reverse inequality for \(j>n/2\) and equality at the middle when \(n\) is even. Thus the positive part of \(P_1-P_0\) lies exactly on \(j>n/2\), and

\[
\operatorname{TV}(P_0,P_1)=1-\sum_{j=0}^n\min\{p_{n,j},p_{n,n-j}\}.
\]

The cell indicator specified in the finding attains the difference between output endpoint values. Each \(p_{n,j}\) is strictly positive, so \(0<\delta_n<1\). For one application, the endpoint transition measures are uniform on the first and last cells, which are disjoint up to null sets, making its oscillation coefficient exactly one.

**4. Parity reduction and asymptotic.** The crossing immediately yields the two parity formulas. For \(j\geq\lfloor n/2\rfloor\) the probability ratio satisfies

\[
\frac{p_{n,j+1}}{p_{n,j}}=
\frac{n-j}{j+1}
\frac{\int_0^{1/(n+1)}t^j(1-t)^{n-j}\,\frac{t}{1-t}\,dt}
{\int_0^{1/(n+1)}t^j(1-t)^{n-j}\,dt}
\leq\frac1n.
\]

Hence the upper-half sum after its first term has relative size \(O(n^{-1})\). Substituting \(u=(n+1)t\) shows that for \(j=\lfloor(n+1)/2\rfloor\),

\[
p_{n,j}=\frac{\binom nj}{(n+1)^j(j+1)}
\int_0^1(j+1)u^j\bigl(1-u/(n+1)\bigr)^{n-j}\,du.
\]

Under the probability density \((j+1)u^j\) on \([0,1]\), \(\mathbb E(1-u)=1/(j+2)=O(n^{-1})\); uniformly in \(u\), \((1-u/(n+1))^{n-j}=e^{-(n-j)u/(n+1)}(1+O(n^{-1}))\). The integrand average is therefore \(e^{-1/2}(1+O(n^{-1}))\). Inserting this central-binomial estimate into the parity formulas proves the asserted asymptotics. Elementary factorial bounds or Stirling's formula give the logarithmic consequence.

## Verification

The standalone checker `verify_kantorovich.py` uses only Python's standard library. It computes the transition integrals independently as exact rational polynomial antiderivatives, checks each transition row sums to one and endpoint reflection, compares the endpoint total-variation distance to the parity overlap formula, and checks upper bounds on a rational grid of intermediate input locations for degrees one through fourteen. It verifies the first listed exact coefficients. Run with `python verify_kantorovich.py`. These finite calculations are supplementary; the inequalities for all positive integers and the asymptotic are proved above rather than inferred from the tests.

## Relationship to prior work

Classical Kantorovich and Bernstein variation-diminishing theory gives a one-input variation inequality. Czudek (2016), Theorem 2, proves \(V_\Lambda(K_nf)\leq V_\Lambda(f)\), which does not determine the oscillation coefficient of the *second iterate*. Cooper and Waldron (2000), Section 7, give the eigenstructure of \(K_n\), and Heilmann and Raşa (2016 online), Theorem 1 and Example 1, derive convergence of iterates and estimates on differentiable functions; neither inspected analysis computes the exact worst-case two-step \(L^\infty/\mathbb R\) contraction or its degree asymptotic. Kivinukk and Metsmägi (2011), Theorems 1–2, obtain variation-norm approximation rates under smoothness assumptions; the proof and conclusions concern \(K_nf-f\), not the oscillation norm of \(K_n^2\). The standard total-positivity/monotone-likelihood-ratio mechanism is used here to reduce an operator norm to endpoint overlap; it is not claimed as a new general principle. The specific finite binomial-overlap formula and super-exponential deficiency are the claim.

## Limitations

This is only the classical unweighted Bernstein–Kantorovich operator on the unit interval and its second iterate. It does not give the exact coefficient for higher powers, generalized Jacobi or nonuniform Kantorovich kernels, or alternative functional seminorms. Publication searches and inspected full texts cannot exclude a historically unindexed equivalent computation; publication priority has not been independently established. The proof does not claim a new total-positivity theorem or a new spectral eigenvalue formula.

## References

1. K. Czudek, *Bernstein and Kantorovich polynomials diminish the \(\Lambda\)-variation*, initial public arXiv version September 4, 2016, https://arxiv.org/abs/1609.00973, Theorem 2 and its proof.
2. S. Cooper and S. Waldron, *The Eigenstructure of the Bernstein Operator*, Journal of Approximation Theory 105 (2000), 133–165, https://doi.org/10.1006/jath.2000.3464, especially Section 7.
3. M. Heilmann and I. Raşa, *Eigenstructure and iterates for uniquely ergodic Kantorovich modifications of operators*, Positivity 21 (2017), 897–910, first online August 23, 2016, https://doi.org/10.1007/s11117-016-0441-1, Theorem 1 and Example 1.
4. M. Kivinukk and E. Metsmägi, *Approximation in variation by the Kantorovich operators*, Proceedings of the Estonian Academy of Sciences (2011), https://doi.org/10.3176/proc.2011.4.01 (full original nine-page paper inspected, especially Theorems 1–2).
