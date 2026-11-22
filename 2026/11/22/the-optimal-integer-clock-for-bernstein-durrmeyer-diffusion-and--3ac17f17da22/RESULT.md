# The optimal integer clock for Bernstein–Durrmeyer diffusion and a trace-class second-order law

## Finding

For the classical Bernstein–Durrmeyer Markov operator \(M_n\) on \(L^2(0,1)\), the smallest nonnegative integer \(q\) for which the selfadjoint operator inequality \(M_n^q\preccurlyeq e^{-L}\) holds is exactly \(q=n+1\), where \(L=-\partial_x(x(1-x)\partial_x)\) is the nonnegative selfadjoint Legendre diffusion generator. At this *optimal integer clock* the approximation is one-sided, second order and trace-class:

\[
0\preccurlyeq e^{-L}-M_n^{n+1}\preccurlyeq \frac{4}{(n+1)^2}L^2e^{-L},
\qquad
(n+1)^2(e^{-L}-M_n^{n+1})\xrightarrow[\ n\to\infty\ ]{\mathcal S_1}\frac16L^2e^{-L}.
\]

In particular,
\[
\lim_{n\to\infty}(n+1)^2\|e^{-L}-M_n^{n+1}\|_{\mathcal S_1}
=\frac16\sum_{k=1}^{\infty}k^2(k+1)^2e^{-k(k+1)}
=0.1052436337384979\ldots,
\]
\[
\lim_{n\to\infty}(n+1)^2\|e^{-L}-M_n^{n+1}\|_{\mathrm{op}}
=\frac23e^{-2}=0.0902235221577418\ldots.
\]

The offset \(n+1\) is also the **unique fixed integer clock correction** which removes the first-order approximation error. Specifically, for every fixed integer \(c\) (and sufficiently large \(n\) such that \(n+c\ge0\)),
\[
n\bigl(M_n^{n+c}-e^{-L}\bigr)\xrightarrow{\mathcal S_1}
(1-c)Le^{-L}.
\]
Thus \(c\ne1\) leaves a nonzero trace-class limit of order \(n^{-1}\), whereas \(c=1\) gives the sharp order \(n^{-2}\).

## Assumptions and scope

For each integer \(n\ge1\), let \(b_{n,j}(x)=\binom njx^j(1-x)^{n-j}\), \(0\le j\le n\), and define
\[
(M_nf)(x)=(n+1)\sum_{j=0}^n b_{n,j}(x)\int_0^1b_{n,j}(y)f(y)\,dy.
\]
The Hilbert space is complex \(H=L^2((0,1),dx)\) and \(\mathcal S_1\) is its trace-class ideal. The operator \(L\) is the nonnegative selfadjoint realization of the quadratic form \(\int_0^1 x(1-x)|f'(x)|^2dx\); equivalently it has orthonormal shifted Legendre eigenvectors \(e_k(x)=\sqrt{2k+1}P_k(2x-1)\) and eigenvalues \(h_k=k(k+1)\), for all integers \(k\ge0\). These data uniquely define \(L\). All operator inequalities are in the Hilbert-space quadratic-form (Loewner) order, *not* pointwise order of kernels. No claim is made for Jacobi-weighted, genuine, or multivariate variants.

## Proof

**1. Exact common diagonalization.** The integral kernel \((n+1)\sum_jb_{n,j}(x)b_{n,j}(y)\) is symmetric and positive semidefinite. Thus \(M_n\) is a selfadjoint positive Markov contraction and preserves every polynomial space of degree at most \(k\). It follows by orthogonality that shifted Legendre polynomials are eigenvectors. More explicitly, for \(0\le k\le n\),
\[
(n+1)\int_0^1 b_{n,j}(y)y^k\,dy=\frac{(j+1)^{\overline{k}}}{(n+2)^{\overline{k}}},
\]
where \(a^{\overline{k}}=a(a+1)\cdots(a+k-1)\). The coefficient of \(x^k\) after Bernstein averaging is \((n)_{\underline{k}}/(n+2)^{\overline{k}}\), giving
\[
M_ne_k=\lambda_{n,k}e_k,\qquad
\lambda_{n,k}=\prod_{r=1}^k\frac{n+1-r}{n+1+r}\quad(0\le k\le n),
\qquad \lambda_{n,k}=0\quad(k>n).
\]
Here \(\lambda_{n,0}=1\). Selfadjointness plus rank at most \(n+1\) proves the zero tail.

**2. Optimal clock and one-sidedness.** Put \(m=n+1\). For \(1\le k\le n\), the convergent inverse-hyperbolic-tangent identity gives
\[
-m\log\lambda_{n,k}=2m\sum_{r=1}^k\operatorname{artanh}(r/m)
=h_k+R_{m,k},\qquad R_{m,k}>0,
\]
with \(h_k=2\sum_{r=1}^kr\). Therefore \(\lambda_{n,k}^m\le e^{-h_k}\), and the same inequality holds for the zero tail \(k>n\). This proves \(M_n^m\preccurlyeq e^{-L}\). Conversely the degree-one eigenvalue is \(\lambda_{n,1}=n/(n+2)\), so
\[
-\log\lambda_{n,1}^{n}=n\log(1+2/n)<2=h_1.
\]
Hence \(M_n^n\not\preccurlyeq e^{-L}\); monotonicity in the integer exponent proves minimality of \(m=n+1\), including exponent zero.

**3. Uniform order bound.** For \(0\le z\le1/2\),
\[
0\le\operatorname{artanh}(z)-z\le\frac{z^3}{3(1-z^2)}\le\frac49 z^3.
\]
For \(k\le m/2\), summing the inequalities and using \(\sum_{r=1}^k r^3=h_k^2/4\) yields \(0\le R_{m,k}\le2h_k^2/(9m^2)\). Therefore
\[
0\le e^{-h_k}-\lambda_{n,k}^m=e^{-h_k}(1-e^{-R_{m,k}})
\le \frac{2h_k^2e^{-h_k}}{9m^2}.
\]
For \(k>m/2\), including the zero eigenvalue tail, the cruder estimate \(0\le e^{-h_k}-\lambda_{n,k}^m\le e^{-h_k}\le4h_k^2e^{-h_k}/m^2\) applies because \(m<2k\le2h_k\). For \(k=0\) the difference vanishes. The displayed uniform operator inequality follows by diagonalization.

**4. Trace-class limit.** For every *fixed* \(k\ge1\), the Taylor expansion \(\operatorname{artanh}(z)=z+z^3/3+O(z^5)\) and the cubic power sum give
\[
R_{m,k}=\frac{h_k^2}{6m^2}+O_k(m^{-4}),\qquad
m^2(e^{-h_k}-\lambda_{n,k}^{m})\longrightarrow \frac16h_k^2e^{-h_k}.
\]
The uniform bound in Step 3 dominates the absolute difference by \(4h_k^2e^{-h_k}\), a summable sequence. Dominated convergence on the common Legendre eigenbasis proves convergence in trace norm, including all ranks \(k>n\). Positivity identifies the trace norm with the trace, yielding the series constant. Since \(x^2e^{-x}\) is nonincreasing for \(x\ge2\), its largest nonzero sampled value at \(h_k=k(k+1)\) occurs at \(k=1\); the operator-norm limit is \(h_1^2e^{-h_1}/6=2e^{-2}/3\).

**5. Uniqueness of the first-order-free clock.** Fix integer \(c\) and put \(d=c-1\). For each fixed \(k\),
\[
\log\lambda_{n,k}=-h_k/m+O_k(m^{-3}),\quad
m(\lambda_{n,k}^{m+d}-e^{-h_k})\longrightarrow -d h_ke^{-h_k}.
\]
For \(k\le m/2\) and fixed \(d\), the inequality \(|a^{m+d}-a^m|\le |d|\,|\log a|\,a^{m-|d|}\) for \(0<a\le1\), together with \(-\log\lambda_{n,k}\le C h_k/m\) and \(a^{m-|d|}\le e^{-h_k/2}\) for all sufficiently large \(m\), supplies the summable majorant \(C_d(h_k+h_k^2)e^{-h_k/2}\) for \(m\) times the entire difference. For \(k>m/2\), bound both spectral powers by \(e^{-h_k/2}\) (and note the zero tail), and use \(m<2k\le2h_k\) to obtain another summable majorant. The finite exceptional small \(m\) are irrelevant. Dominated convergence proves the asserted \(\mathcal S_1\) limit. Because \(Le^{-L}\ne0\), only \(d=0\), i.e. \(c=1\), cancels it.

## Verification

A standalone numerical checker `check.py` independently evaluates the finite-rank integral kernel by Gauss–Legendre quadrature and compares its matrix with the claimed shifted-Legendre spectral diagonalization. It also tests exact clock minimality, one-sidedness, the explicit finite-degree trace bound, and the trace/operator asymptotics. The checker reports **148 passed finite assertions**. The proof above is analytic; these checks are diagnostic, not certification of an infinite statement.

## Relationship to prior work

The exact Bernstein–Durrmeyer eigenvalues and complete *single-step* asymptotic expansions are classical and not claimed as new. Abel and Berdysheva (2010) derive eigenvalue formulas and asymptotic expansions in a more general approximation setting. Altomare (2019), in the work that motivated this question, proves strong-type Markov-iterate convergence to diffusion semigroups, including Jacobi-weighted Bernstein–Durrmeyer operators. The present specific result extracts an **optimal integer time**, a **Loewner upper approximation with an explicit uniform trace-class bound**, and a **nonzero second-order trace-class limit** for the classical one-dimensional unweighted case. These conclusions are stronger than strong-operator semigroup convergence alone; the exact eigenvalues by themselves do not state the infinite-rank, trace-norm limit. Related older quantitative approximation and genuinely modified Bernstein–Durrmeyer results should not be conflated with this exact operator family.

## Limitations

This result concerns one fixed selfadjoint Markov family and the Legendre diffusion at time one. It does not establish pointwise kernel ordering, weighted-Jacobi uniformity, or a general theorem for Markov approximation schemes. Known spectral formulas make the proof comparatively short; the contribution is the sharp combination of clock optimality, global order control, and trace-ideal asymptotics. Earlier specialized work on iterates of genuine and ultraspherical Durrmeyer operators (Gonska–Heilmann–Raşa, 2009) was checked at abstract level only because the full text was unavailable; possible historical-priority overlap is a residual risk. The result has not undergone independent mathematical audit.

## References

1. F. Altomare, *Iterates of Markov Operators and Constructive Approximation of Semigroups*, Constructive Mathematical Analysis **2** (2019), 22–39; first published online **4 January 2019**. DOI: https://doi.org/10.33205/cma.491601 . Full text: https://dergipark.org.tr/en/download/article-file/618613 .
2. U. Abel and E. Berdysheva, *Complete asymptotic expansion for multivariate Bernstein–Durrmeyer operators and quasi-interpolants*, Journal of Approximation Theory **162** (2010), 201–220. https://www.academia.edu/21476089/Complete_asymptotic_expansion_for_multivariate_Bernstein_Durrmeyer_operators_and_quasi_interpolants .
3. H. Gonska, M. Heilmann and I. Raşa, *Convergence of iterates of genuine and ultraspherical Durrmeyer operators to the limiting semigroup: C²-estimates*, Journal of Approximation Theory **160** (2009), 243–255. https://doi.org/10.1016/j.jat.2008.11.002 .
4. F. Altomare, M. Cappelletti Montano and V. Leonessa, *On the positive semigroups generated by Fleming–Viot type differential operators*, Communications on Pure and Applied Analysis **18** (2019), 323–340. https://doi.org/10.3934/cpaa.2019017 .
5. T. Hirano and R. Namba, *Iterates of multidimensional Bernstein-type operators and diffusion processes in population genetics*, arXiv:2310.13983 (first posted 2023). https://arxiv.org/abs/2310.13983 .
