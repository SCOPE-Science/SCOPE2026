# Cubic resonance and sharp skewness-optimal truncation for circular Sobolev tests

## Finding
Let \(\Theta_1,\ldots,\Theta_n\) be independent uniform angles on \([0,2\pi)\), where \(n\ge2\). For each integer \(k\ge1\), put
\[
T_k=\frac1n\left|\sum_{j=1}^n e^{\mathrm i k\Theta_j}\right|^2.
\]
For finitely supported nonnegative real weights \(w_k\), define \(H_w=\sum_{k\ge1}w_kT_k\). Then
\[
\mathbb EH_w=\sum_k w_k,\qquad
\operatorname{Var}(H_w)=\frac{n-1}{n}\sum_k w_k^2,
\]
and the exact third centered moment is
\[
\boxed{\mathbb E(H_w-\mathbb EH_w)^3
=\frac{n-1}{n^2}\left[2(n-2)\sum_k w_k^3+3\sum_{a,b\ge1}w_aw_bw_{a+b}\right].}
\]
All sums are finite because the weights have finite support. The second term is an *additive frequency-resonance count*, rather than the third moment of a collection of independent harmonic energies. At \(n=2\) it vanishes exactly when the positive-weight support contains no triple \(a+b=c\); for \(n\ge3\) the cubic moment is strictly positive whenever at least one weight is positive.

In particular, let \(H_{n,M}=\sum_{k=1}^M T_k\), for positive integer \(M\), and write \(\gamma_{n,M}\) for its standardized third central moment (skewness). Then
\[
\boxed{\gamma_{n,M}=\frac{3M+4n-11}{2\sqrt{n(n-1)M}}.}
\]
For each fixed \(n\ge3\) the skewness has a **unique** minimum over positive integer cutoffs, attained at the smallest integer \(M\ge1\) satisfying
\[
9M(M+1)>(4n-11)^2.
\]
The minimizer is strict, and as \(n\to\infty\),
\[
M_{\mathrm{opt}}/n\longrightarrow4/3,
\qquad \sqrt n\,\gamma_{n,M_{\mathrm{opt}}}\longrightarrow2\sqrt3.
\]
For \(n=2\), the unique minimum is \(M=1\), where the skewness equals zero. In the joint large-sample regime \(M/n^2\to c\in(0,\infty)\), the exact skewness tends to \(3\sqrt c/2\); if \(M\to\infty\) and \(M=o(n^2)\), it tends to zero. These are moment statements, **not** claims that a central limit theorem fails whenever the third moment does not vanish.

## Assumptions and scope
The null hypothesis is fully specified continuous circular uniformity. Observations are independent and identically distributed, and ties have probability zero. All frequencies are positive integers and the weights are finitely supported, real and nonnegative. For the cutoff result all weights in \(\{1,\ldots,M\}\) equal one, with zero weights outside. For comparison with conventional notation, the circular Sobolev statistic in the primary source is \(S_{n,w}=2H_w\); its unweighted standardized statistic \((S_{n,M}-2M)/(2\sqrt M)\) equals \((H_{n,M}-M)/\sqrt M\) and has exact variance \((n-1)/n\), not one at finite sample size.

## Proof
For each positive integer \(k\), define \(Y_k=T_k-1\). Expanding the squared modulus and discarding the diagonal terms gives
\[
Y_k=\frac1n\sum_{1\le i<j\le n}\left(e^{\mathrm i k(\Theta_i-\Theta_j)}+e^{-\mathrm i k(\Theta_i-\Theta_j)}\right).
\]
The elementary Haar-character identity \(\mathbb E e^{\mathrm i r\Theta_i}=\mathbf1_{r=0}\), for integer \(r\), shows \(\mathbb EY_k=0\) and
\[
\mathbb E(Y_aY_b)=\frac{n-1}{n}\mathbf1_{a=b}.
\]
Indeed, a product of two edge characters integrates to zero unless the same unordered sampled edge appears twice with equal frequencies and opposite orientations. This proves the variance assertion.

To compute \(\mathbb E(Y_aY_bY_c)\), expand all three edge sums. An edge configuration with a sampled vertex of degree one has zero expectation by integrating at that vertex. The only remaining configurations, with multiplicities counted in the ordered three-factor product, are:

1. **One edge used three times.** There are \(\binom n2\) choices, and the expectation of the product of the three two-orientation character sums equals two precisely if one of \(a,b,c\) is the sum of the other two, otherwise zero. The three possible relations are mutually exclusive for positive frequencies. Its contribution after dividing by \(n^3\) is \((n-1)/n^2\) times the resonance indicator.
2. **Three distinct edges of a triangle.** There are \(6\binom n3\) ordered configurations. At each vertex, character balance forces all three frequencies to agree, and the two directed cycles give expectation two. Its contribution is \(2(n-1)(n-2)/n^2\) times the indicator that \(a=b=c\).

Thus, for positive \(a,b,c\),
\[
\mathbb E(Y_aY_bY_c)=\frac{n-1}{n^2}\mathbf1_{\{a+b=c\ \mathrm{or}\ a+c=b\ \mathrm{or}\ b+c=a\}}
+\frac{2(n-1)(n-2)}{n^2}\mathbf1_{a=b=c}.
\]
Because each \(Y_k\) has mean zero, this mixed central moment is also the third mixed cumulant. Multiplying by \(w_aw_bw_c\) and summing gives the stated weighted identity: the resonance indicator yields exactly \(3\sum_{a,b\ge1}w_aw_bw_{a+b}\), whereas the triangle term yields \(2(n-2)\sum_k w_k^3\). Both are nonnegative, which proves the zero/positivity statements.

For unit weights on \(1,\ldots,M\), the ordered additive-pair count is
\[
\sum_{a,b\ge1}\mathbf1_{a+b\le M}=\frac{M(M-1)}2.
\]
Consequently
\[
\operatorname{Var}(H_{n,M})=\frac{M(n-1)}n,
\qquad
\mathbb E(H_{n,M}-M)^3=\frac{n-1}{n^2}
\left[2M(n-2)+\frac32M(M-1)\right],
\]
which after division by the variance to the power \(3/2\) yields the skewness formula.

For \(n\ge3\) set \(b=4n-11>0\). Apart from the fixed positive factor \(1/(2\sqrt{n(n-1)})\), the skewness equals \(f(M)=3\sqrt M+b/\sqrt M\). Exact subtraction gives
\[
f(M+1)-f(M)=\bigl(\sqrt{M+1}-\sqrt M\bigr)
\left[3-\frac{b}{\sqrt{M(M+1)}}\right].
\]
The bracket increases strictly through zero, so there is exactly one integer minimum, as described. Equality cannot occur: it would imply \(9M(M+1)=b^2\), so \(b\) is divisible by three and \(M(M+1)\) is a perfect square; since the two positive consecutive factors are coprime, each would have to be a square, impossible for consecutive positive integers. At \(n=2\), \(b=-3\) and \(f(M)\) is strictly increasing for positive \(M\). The limiting statements follow by substituting the formula and the root asymptotics for the cutoff.

## Verification
The complete standalone Python checker is `check.py`; run it with `python3 check.py` in the same directory. It directly expands Fourier characters on every ordered pair of sampled edges, retains only exactly balanced vertex exponents, and calculates the moments with rational arithmetic. The checker compares every third mixed moment and second mixed moment for \(2\le n\le5\) and frequencies \(1\le a,b,c\le4\), checks all unweighted sums with \(1\le M\le6\), checks several uneven nonnegative weight vectors, and tests the exact discrete cutoff inequality and strictness for many sample sizes. It passed 13,229 assertions. This is a finite corroboration of the proof, not a substitute for its all-\(n\), all-\(M\) argument. No numerical integration, approximate exhaustive enumeration of an infinite domain, or stochastic convergence simulation is used to establish the identities.

## Relationship to prior work
Jammalamadaka, Meintanis and Verdebout (2020), Section 2, equation (4), define the same weighted circular Sobolev family; their Proposition 4.1 establishes asymptotic Gaussian calibration for unweighted growing cutoffs \(M=o(n^2)\). Their Appendix provides degenerate-kernel and fourth-product identities. The exact weighted finite-sample **third** moment, its additive resonances, and the integer cutoff minimizing standardized skewness are distinct assertions: neither Gaussian convergence nor second/fourth-moment bounds give these formulas or the optimal cutoff by direct implication. Earlier circular characteristic-function tests, including Jammalamadaka, Jiménez-Gamero and Meintanis (2019), concern composite-family null distributions and asymptotic calibration rather than this exact fully uniform, finitely truncated cubic law. Fernández-de-Marcos and García-Portugués (2021 preprint) study distribution stabilizations, particularly quantile accuracy, but not this frequency-optimal cubic moment. Exact pairwise harmonic orthogonality was previously studied separately and is not new here. Standard character orthogonality and diagram-counting principles are acknowledged; the concrete all-weight identity and strict integer minimization are the proposed contribution.

## Limitations
Skewness is a moment descriptor, not a complete measure of approximation error, tail size, power, or the size of a test. The cutoff that minimizes skewness need not optimize power or any discrepancy to a Gaussian distribution. Nonzero or diverging skewness does not on its own rule out weak convergence to normal without suitable moment uniform integrability; no such impossibility is asserted. Claims apply only to independent uniform angles and finite frequency support, not estimated-null, dependent, nonuniform, or continuous-frequency models. Prior-art searches and comparisons cannot establish exhaustive historical priority, and the result has not received independent validation.

## References
- Jammalamadaka, S. R., Meintanis, S. G., and Verdebout, T. (2020). *On Sobolev tests of uniformity on the circle with an extension to the sphere*. Bernoulli 26(3), 2226–2252. DOI: 10.3150/19-BEJ1191. Lawful open text: https://escholarship.org/content/qt7mb6w6k6/qt7mb6w6k6.pdf
- Jammalamadaka, S. R., Jiménez-Gamero, M. D., and Meintanis, S. G. (2019). *A class of goodness-of-fit tests for circular distributions based on trigonometric moments*. SORT 43(2), 317–336. DOI: 10.2436/20.8080.02.90. https://www.idescat.cat/sort/sort432/43.2.6.meintanis-etal.pdf
- Fernández-de-Marcos, A., and García-Portugués, E. (2021 preprint; 2023 journal). *Data-driven stabilizations of goodness-of-fit tests*. arXiv:2112.01808. https://arxiv.org/pdf/2112.01808
