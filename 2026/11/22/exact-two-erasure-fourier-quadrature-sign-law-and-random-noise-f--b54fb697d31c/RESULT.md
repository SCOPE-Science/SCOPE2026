# Exact two-erasure Fourier quadrature sign law and random-noise floor

## Finding

Let \(n\ge5\) be odd and \(m=(n-3)/2\). On the periodic grid \(x_j=j/n\), erase exactly two distinct indices \(a,b\). There is one and only one set of real weights on the remaining \(n-2=2m+1\) nodes that integrates every real trigonometric polynomial of degree at most \(m\) exactly with respect to \(\int_0^1 f(x)\,dx\). The weights are explicitly classified by the cyclic separation of the erased nodes.

Put \(v=(n-1)/2\) and, by exchanging \(a,b\) if necessary, assume \(\delta=v(b-a)\pmod n\) is the representative in \(\{1,\ldots,(n-1)/2\}\). For each original grid index \(j\), let \(k_j=v(j-a)\pmod n\) be the representative in \(\{0,\ldots,n-1\}\). Extend the weights by zero at the erased indices. The unique rule is

\[
w_j=\frac1n\left(1-\frac{\cos((2k_j-\delta)\pi/n)}{\cos(\delta\pi/n)}\right).
\]

Exactly \(\delta-1\) surviving weights are strictly negative (those with \(k_j=1,\ldots,\delta-1\)); every other surviving weight is strictly positive. Thus all surviving weights are strictly positive **if and only if** \(\delta=1\), equivalently if the erased nodes are two grid increments apart cyclically, \(b-a\equiv\pm2\pmod n\). The *exact total negative weight mass* and sharp bounded sample-error amplification are

\[
H_{n,\delta}=\frac1n\left[\cot(\pi/n)\tan(\delta\pi/n)-\delta\right],\qquad
\|Q\|_{\infty\to\mathbb R}=1+2H_{n,\delta}.
\]

For independent zero-mean observation errors each with variance \(\sigma^2\), conditional on the two erased positions, the error variance is exactly

\[
\operatorname{Var}(Q(\varepsilon)\mid a,b)
=\frac{\sigma^2}{n}\left(1+\frac1{2\cos^2(\pi\delta/n)}\right).
\]

If the unordered pair of erased indices is uniform among the \(\binom n2\) pairs and independent of the observation errors, then \(\delta\) is uniform on \(\{1,\ldots,(n-1)/2\}\); hence

\[
\Pr(\hbox{all retained weights positive})=\frac2{n-1},\qquad
\mathbb E_{a,b}\operatorname{Var}(Q(\varepsilon)\mid a,b)
=\frac{n+3}{2n}\sigma^2\longrightarrow\frac{\sigma^2}{2}.
\]

Thus removing only two samples from a minimally redundant, near-Nyquist equally spaced rule creates a nonvanishing mean measurement-noise variance, versus \(\sigma^2/n\) on the intact grid. More precisely, the variance ratio to intact-grid equal-weight quadrature is \(R_n=1+\tfrac12\sec^2(\pi\delta/n)\). Under uniform random erasures,

\[
R_n\ \Rightarrow\ R=1+\frac12\sec^2(\pi U),\quad U\sim\operatorname{Unif}(0,1/2),
\qquad\Pr(R>t)=\frac2\pi\arcsin\left(\frac1{\sqrt{2(t-1)}}\right)
\quad(t\ge3/2),
\]

and \(\Pr(R>t)\sim \sqrt{2}/(\pi\sqrt t)\). The limiting law has infinite mean, consistent with \(\mathbb E R_n=(n+3)/2\to\infty\).

## Assumptions and scope

The domain is the unit circle identified with \([0,1)\), and the target functional is normalized Lebesgue integration on one period. The trigonometric input space is \(\operatorname{span}\{e^{2\pi i r x}:-m\le r\le m\}\), restricted to real-valued members. The design has exactly \(n=2m+3\) equally spaced potential nodes, and exactly two are lost without replacement. The observations at retained sites are exact except when independent additive measurement noise is explicitly discussed. Uniform missingness refers to the *unordered pair* of lost indices, independent of errors, not to independently missing sites or to perturbed node locations. Every formula is for finite odd \(n\ge5\).

## Proof

**Uniqueness.** The \(n-2=2m+1\) retained nodes are distinct. A trigonometric polynomial of degree at most \(m\), multiplied by \(z^m\), is an ordinary polynomial of degree at most \(2m\) in \(z=e^{2\pi ix}\). Such a polynomial cannot vanish at the \(2m+1\) distinct retained points unless identically zero. Thus trigonometric interpolation, and its integral weights, are unique.

**Explicit formula.** Temporarily use an \(n\)-vector of weights with zeros at the erased indices, and define \(g_j=nw_j-1\). Trigonometric exactness says that the finite Fourier coefficients of \(g\) vanish at frequencies \(-m,\ldots,m\), including the zero frequency. Since \(n=2m+3\), the only two remaining residue frequencies are \(\pm v\), where \(v=m+1\). Realness gives \(g_j=A\cos(2\pi v(j-a)/n)+B\sin(2\pi v(j-a)/n)\). Because \(w_a=w_b=0\), one has \(g_a=g_b=-1\). Set \(\theta_j=2\pi v(j-a)/n\) and orient \(a,b\) so \(v(b-a)\equiv\delta\pmod n\), with \(1\le\delta\le(n-1)/2\). The two constraints give \(A=-1\) and \(B=-\tan(\pi\delta/n)\); their denominator is nonzero because \(0<\pi\delta/n<\pi/2\). Thus \(g_j=-\cos(\theta_j-\pi\delta/n)/\cos(\pi\delta/n)\), proving the stated weights and exactness.

**Sign classification.** As \(j\) ranges over the grid, \(k_j\equiv v(j-a)\pmod n\) ranges bijectively over \(0,\ldots,n-1\) because \(\gcd(v,n)=1\). The factor \(\cos(\pi\delta/n)\) is positive. Comparing \(\cos((2k-\delta)\pi/n)\) with \(\cos(\delta\pi/n)\) on one full period shows that the equality indices are exactly \(k=0,\delta\), strict reversal (negative weights) occurs exactly for \(1\le k\le\delta-1\), and all remaining indices have strictly positive weights. Finally, \(2v=n-1\equiv-1\pmod n\), so \(\delta=1\) is equivalent to \(b-a\equiv\pm2\pmod n\).

**Negative mass.** Summing the negatives, using the finite cosine progression identity

\[
\sum_{k=1}^{\delta-1}\cos((2k-\delta)h)=\frac{\sin((\delta-1)h)}{\sin h},\qquad h=\frac\pi n,
\]

produces \(H_{n,\delta}=[\cot h\tan(\delta h)-\delta]/n\). Since the weights sum to one, the norm of the linear functional on bounded nodal errors is \(\sum_j|w_j|=1+2H_{n,\delta}\), attained by errors with the signs of the weights. The expression strictly grows with \(\delta\): the difference of its unnormalized values at successive integers is positive because \(\tan((\delta+1)h)-\tan(\delta h)>\tan h\) for \(\delta\ge1\) in the given range.

**Noise variance and missing-pair average.** Independence yields variance \(\sigma^2\sum_jw_j^2\). Expanding the weight formula and summing the cosine mode over the odd cyclic grid gives \(\sum_j\cos((2k_j-\delta)h)=0\) and \(\sum_j\cos^2((2k_j-\delta)h)=n/2\), since \(n\ge5\). Therefore \(\sum_jw_j^2=n^{-1}(1+\tfrac12\sec^2(\delta h))\). Every \(\delta\in\{1,\ldots,(n-1)/2\}\) corresponds to exactly \(n\) unordered erased pairs, so the separation is uniform. The identity \(\sum_{r=0}^{n-1}\sec^2(\pi r/n)=n^2\) for odd \(n\) follows by differentiating the cotangent multiplication formula, or equivalently from \(\sum_{r=0}^{n-1}\csc^2(x+r\pi/n)=n^2\csc^2(nx)\) at \(x=\pi/(2n)\). It implies \(\sum_{\delta=1}^{(n-1)/2}\sec^2(\pi\delta/n)=(n^2-1)/2\), and the stated exact expectation follows. There are exactly \(n\) positivity-preserving erased pairs, giving probability \(n/\binom n2=2/(n-1)\).

**Limiting law.** The uniform discrete positions \(\delta/n\) converge in law to \(U\sim\operatorname{Unif}(0,1/2)\). The transformation \(u\mapsto1+\tfrac12\sec^2(\pi u)\) is continuous on \((0,1/2)\) and diverges only at an endpoint of zero limiting probability. For \(t\ge3/2\), solving the inequality gives \(\Pr(R>t)=\tfrac2\pi\arcsin((2(t-1))^{-1/2})\). Its stated asymptotic follows from \(\arcsin z\sim z\) as \(z\downarrow0\). This is a distributional limit, not convergence of expectations.

## Verification

Run `python verify.py` with `numpy` installed. The script evaluates all unordered erased pairs at each odd size from 5 through 55 (14,235 pairs), verifies the weight zeros, all frequency moments, exact negative-count classification, negative-mass and noise-norm identities, solves selected independent square interpolation systems, and checks the exact random-erasure average through odd size 199. These are finite implementation and boundary checks only; the preceding Fourier and trigonometric arguments prove the universal statements.

## Relationship to prior work

Kircheis and Potts (first public 2023) provide the general exact trigonometric quadrature linear-system/density-compensation framework for nonequispaced Fourier sampling, but not the explicit two-site-erasure sign law or noise-floor distribution derived here. Peherstorfer (2010) gives a broad characterization of positivity of trigonometric quadrature formulas; that general positivity theory is not claimed as new, and the finite-grid criterion here must be understood as a specific derivation consistent with it. Yu and Townsend (2022) and Austin and Trefethen (2016) treat perturbed *retained* regular grids rather than deleted sites. Van den Bos and Sanderse (2021) study algebraic polynomial quadrature under node removal, not these periodic near-Nyquist Fourier weights. A published Fourier result on symmetric pair collision changes sample locations continuously and does not give the present missing-observation noise law. The claimed contribution is the joint explicit *two-erasure*, all-size negative-weight count, mass, variance, and random-erasure tail and noise-floor formulas—not a general novel quadrature method.

## Limitations

The weights integrate exactly only the stated degree-\(m\) trigonometric space. The result does not address arbitrary irregular grids, three or more erasures, noisy *node positions*, correlated observation errors, Gaussian-process posterior rules, or computationally stable recovery in finite precision. The constant variance floor concerns uniformly sampled erased pairs and independent homoscedastic errors, not all dropout processes. Historical priority remains provisional, especially for specialized trigonometric-quadrature positivity formulas and unpublished treatments of equispaced erasures. Finite numerical checks cannot prove uniqueness relative to the historical literature.

## References

1. M. Kircheis and D. Potts, *Fast and direct inversion methods for the multivariate nonequispaced fast Fourier transform* (first public 2023-02-01), https://arxiv.org/abs/2302.00414 ; open journal version https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2023.1155484/full .
2. F. Peherstorfer, *Positive Trigonometric Quadrature Formulas and Quadrature on the Unit Circle* (2010), https://arxiv.org/abs/1001.2451 .
3. A. Yu and A. Townsend, *On the Stability of Unevenly Spaced Samples for Interpolation and Quadrature* (2022), https://arxiv.org/abs/2202.04722 .
4. A. Austin and L. N. Trefethen, *Trigonometric Interpolation and Quadrature in Perturbed Points* (2016), https://arxiv.org/abs/1612.04018 .
5. L. van den Bos and B. Sanderse, *A Geometrical Interpretation of the Addition of Nodes to an Interpolatory Quadrature Rule* (2021), https://ir.cwi.nl/pub/30613/30613.pdf .
6. *Positive Fourier quadrature survives symmetric pair collision with a sharp singular-value law* (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/16/SCOPE-positive-fourier-quadrature-survives-symmetric-pair-collision-wi--92a65f43a0d4 .
