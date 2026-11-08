# Exact correlation and sharp moment thresholds for two logarithmic-potential first-passage functionals

## Finding

A one-dimensional diffusion in a logarithmic potential has a full, explicit *mixed-moment threshold* for two different absorption functionals. With the definitions in the next section, and arbitrary \(p,q>0\),

\[
\mathbb E[Z_pZ_q]<\infty\quad\Longleftrightarrow\quad\beta>p+q.
\]

In the finite regime,

\[
\mathbb E[Z_pZ_q]
=\frac{x_0^{p+q}}{D^2(p+q)(\beta-p-q)}
\left(\frac{1}{p(\beta-p)}+\frac{1}{q(\beta-q)}\right),
\]

and the covariance simplifies to the strictly positive expression

\[
\operatorname{Cov}(Z_p,Z_q)
=\frac{2x_0^{p+q}}{D^2(\beta-p)(\beta-q)(p+q)(\beta-p-q)}.
\]

The Pearson correlation is defined precisely when \(\beta>2\max(p,q)\), and then

\[
\rho_{p,q}(\beta)
=\frac{2\sqrt{pq}}{p+q}
\sqrt{1-\frac{(p-q)^2}{(\beta-p-q)^2}}.
\]

For \(p\ne q\), this function is strictly increasing in \(\beta\), ranging from zero at the finite-variance boundary to the *sharp, never-attained* ceiling

\[
\lim_{\beta\to\infty}\rho_{p,q}(\beta)
=\frac{2\sqrt{pq}}{p+q}<1.
\]

For \(p=q\), the correlation is identically one wherever it is defined. The ceiling has the equivalent exponent-distance form \(\operatorname{sech}(|\log(p/q)|/2)\).

Of particular physical interest, the absorption time \(T=Z_2\) and area \(A=Z_3\) have finite mixed moment exactly when \(\beta>5\); their Pearson correlation exists only when \(\beta>6\), where

\[
\operatorname{Corr}(T,A)
=\frac{2\sqrt6}{5}\sqrt{1-\frac1{(\beta-5)^2}}.
\]

Thus the time-area correlation rises strictly from zero to the limiting value \(2\sqrt6/5\) as the attraction parameter grows, despite both observables arising from the same trajectory.

## Assumptions and scope

Let \(D>0\), \(x_0>0\) and \(\beta>0\). On the positive half-line, stop the diffusion at its first hit of zero, where prior to absorption it satisfies

\[
 dX_t=-\frac{D(\beta-1)}{X_t}\,dt+\sqrt{2D}\,dW_t,
 \qquad X_0=x_0,
 \qquad T=\inf\{t\ge0:X_t=0\}.
\]

Equivalently, the logarithmic potential is \(V(x)=V_0\log x\) with \(\beta=1+V_0/D\). For \(\beta>0\), absorption is almost sure; the boundary is killing, not reflection or resetting. For each real \(p>0\) define the nonnegative absorption functional

\[
Z_p=\int_0^T X_t^{p-2}\,dt.
\]

The functional is almost surely finite in this setting, although its mean or higher moments may be infinite. The theorem applies to every pair of positive real exponents, and is not a claim about the complete joint distribution.

## Proof

**1. Killed Green kernel.** The backward generator is

\[
\mathcal L f(x)=D f''(x)-\frac{D(\beta-1)}x f'(x).
\]

Its increasing scale function may be taken as \(s(x)=x^\beta/\beta\), and its speed density in the generator normalization is \(x^{1-\beta}/D\). For killing at zero and the natural upper boundary, the potential density with respect to Lebesgue measure is

\[
G(x,y)=\frac{\min(x,y)^\beta y^{1-\beta}}{D\beta},\qquad x,y>0.
\]

It vanishes as \(x\downarrow0\), is constant in \(x\) above \(y\), solves \(\mathcal L_xG(x,y)=0\) off the diagonal, and its first-derivative jump gives \(\mathcal L_xG(x,y)=-\delta_y(x)\). Hence for nonnegative measurable \(f\), by monotone approximation,

\[
\mathbb E_x\!\left[\int_0^T f(X_t)\,dt\right]
=\int_0^\infty G(x,y)f(y)\,dy
\]

with the value \(+\infty\) permitted.

**2. First moments and their exact thresholds.** Split the integral at \(y=x\). For any \(p>0\),

\[
\begin{aligned}
\mathbb E_x Z_p
&=\frac{1}{D\beta}\left(\int_0^x y^{p-1}\,dy+x^\beta\int_x^\infty y^{p-\beta-1}\,dy\right)\\
&=\frac{x^p}{Dp(\beta-p)},\qquad \beta>p.
\end{aligned}
\]

For \(\beta\le p\), the second integral diverges (logarithmically at equality), so \(\mathbb E_xZ_p=\infty\). The same calculation with exponent \(p+q\) identifies the exact threshold for \(\mathbb E_x Z_{p+q}\).

**3. Mixed moment via temporal ordering.** The diagonal of the two-dimensional time integral has zero Lebesgue measure. Ordering the two time coordinates and applying the strong Markov property and Tonelli's theorem gives, with extended nonnegative expectations,

\[
\begin{aligned}
\mathbb E_x[Z_pZ_q]
=\mathbb E_x\int_0^T\!\left(
X_t^{p-2}\mathbb E_{X_t}Z_q
+X_t^{q-2}\mathbb E_{X_t}Z_p\right)dt.
\end{aligned}
\]

When \(\beta>\max(p,q)\), substitute the first-moment formulas. The powers combine to \(X_t^{p+q-2}\), yielding

\[
\mathbb E_x[Z_pZ_q]
=\frac1D\left(\frac1{p(\beta-p)}+\frac1{q(\beta-q)}\right)\mathbb E_x Z_{p+q}.
\]

By Step 2 this is finite exactly when \(\beta>p+q\), giving the stated expression. If \(\beta\le\max(p,q)\), at least one conditional expectation is infinite at every positive starting point; positivity in the ordered-time formula then forces the mixed expectation to be infinite. If \(\max(p,q)<\beta\le p+q\), the same formula and Step 2 force it to be infinite. This proves the *if and only if*, including equality boundaries.

**4. Covariance and Pearson correlation.** The product of first moments is \(x^{p+q}/[D^2pq(\beta-p)(\beta-q)]\). Subtraction and cancellation of the numerator using

\[
p(\beta-p)+q(\beta-q)-(p+q)(\beta-p-q)=2pq
\]

give the covariance formula. The special case \(q=p\) yields

\[
\operatorname{Var}(Z_p)
=\frac{x^{2p}}{D^2p(\beta-p)^2(\beta-2p)},\qquad \beta>2p.
\]

Thus both finite positive variances exist exactly when \(\beta>2\max(p,q)\). Division by their geometric mean proves the Pearson formula; all \(x\) and \(D\) factors cancel.

**5. Sharp monotone boundary.** For unequal exponents write

\[
\rho_{p,q}(\beta)
=\frac{2\sqrt{pq}}{p+q}\sqrt{1-\frac{(p-q)^2}{(\beta-p-q)^2}},
\quad \beta>2\max(p,q).
\]

In this domain \(\beta-p-q>|p-q|\). The square-root term is strictly increasing from zero to one as \(\beta\) grows, proving the exact range, strict monotonicity and limiting ceiling. By arithmetic-geometric mean the ceiling is less than one exactly when \(p\ne q\). The case \(p=q\) is immediate because both observables are identical.

## Verification

The accompanying standalone `checker.py` independently reconstructs first and mixed moments by numerical quadrature against the killed Green kernel, rather than by calling the final covariance formula. It compares these to the closed forms, checks variances and correlations over distinct exponents, diffusivities and starting locations, and checks strict monotonicity and the limiting ceiling. Executing `python checker.py` produced: `PASS: 248 kernel-integral, mixed-moment, variance, and sharp-correlation checks`.

The proof of the divergence boundaries is analytic, using the power integral at infinity and nonnegative Tonelli identities; numerical testing cannot prove these infinite-domain claims.

## Relationship to prior work

Radice, *Physical Review E* 108, 044151 (2023), arXiv:2307.12699, establishes the inverse-gamma **one-functional** distribution and its moment thresholds for logarithmic-potential Brownian motion. Its conclusion specifically identifies correlations between observables with different power exponents, especially time versus area, as a future direction. The theorem above supplies exact mixed moments, covariance, the sharp moment-finiteness boundary and the complete Pearson monotonicity/range classification, not the full joint probability density.

Kearney and Martin, *Journal of Physics A* 54, 055002 (2021), arXiv:2007.13129, compute an area-time correlation for a different Ornstein–Uhlenbeck first-passage process. Its linear restoring force is distinct from the inverse-position drift, and its formulas do not imply the present power-family correlation or threshold. Earlier Bessel-like first-passage literature establishes related hitting-time marginals, but those alone do not determine two-functional dependence.

## Limitations

The theorem concerns the absorbed positive-half-line diffusion with \(\beta>0\) and positive power indices. It does not give the full joint law, conditional law, or analogous formulas for finite intervals, nonlinear restoring potentials or negative indices. Pearson correlation is undefined when either variance is infinite; this must not be interpreted as a zero covariance. At the finite-variance boundary for unequal indices, only a one-sided limiting correlation is asserted. The exact result is analytically reproducible, but potential overlap with broader uninspected mixed-additive-functional literature and independent validation remain open scientific considerations.

## References

1. M. Radice, “First-passage functionals of Brownian motion in logarithmic potentials and heterogeneous diffusion,” *Physical Review E* **108**, 044151 (2023); arXiv:2307.12699, first version public 2023-07-24; https://arxiv.org/abs/2307.12699.
2. M. J. Kearney and R. J. Martin, “Statistics of the first passage area functional for an Ornstein–Uhlenbeck process,” *Journal of Physics A: Mathematical and Theoretical* **54**, 055002 (2021); arXiv:2007.13129; https://arxiv.org/abs/2007.13129.
3. E. Martin, U. Behn and G. Germano, “First-passage and first-exit times of a Bessel-like stochastic process,” *Physical Review E* **83**, 051115 (2011); arXiv:1007.4588; https://arxiv.org/abs/1007.4588.
