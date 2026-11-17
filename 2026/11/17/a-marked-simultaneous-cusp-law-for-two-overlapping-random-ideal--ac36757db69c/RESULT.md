# A marked simultaneous-cusp law for two overlapping random ideal-quadrilateral cross ratios

## Finding

Let \(Z_1,\ldots,Z_5\) be independent points sampled uniformly by arclength from the unit circle, with **fixed labels**, not sorted by cyclic order. Define two real projective cross ratios of overlapping ideal quadrilaterals by
\[
 R_4=\frac{(Z_1-Z_3)(Z_2-Z_4)}{(Z_1-Z_4)(Z_2-Z_3)},\qquad
 R_5=\frac{(Z_1-Z_3)(Z_2-Z_5)}{(Z_1-Z_5)(Z_2-Z_3)}.
\]
Almost surely all denominators are nonzero. For \(t>0\) let \(E_t=\{|R_4|>t,\ |R_5|>t\}\). The simultaneous extremal probability has the precise asymptotic
\[
 \boxed{\lim_{t\to\infty}t\,\Pr(E_t)=K},\qquad
 K=2\int_{\mathbb R}f(b)^2\,\mathbb E\min(|D-b|,|E-b|)\,db,
 \quad f(x)=\frac1{\pi(1+x^2)},
\]
where \(D,E\) are independent standard Cauchy variables. The constant is positive and finite, with alternative absolutely convergent expression
\[
 K=\frac{2}{\pi^2}\int_{-\infty}^{\infty}\frac{db}{(1+b^2)^2}
  \int_0^\infty\left[1-\frac{\arctan(b+s)-\arctan(b-s)}\pi\right]^2ds
 \approx0.343103352834.
\]

There is a stronger **marked limit in total variation**. Rotate the circle to send \(Z_1\) to angle zero and use the stereographic coordinate \(x=\cot(\phi/2)\). Write \((B,C,D,E)\) for the stereographic coordinates of \((Z_2,Z_3,Z_4,Z_5)\). Define \(Y_t=t(C-B)\). Conditional on \(E_t\), the joint law of \((B,D,E,Y_t)\) converges in total variation to the probability measure with density
\[
 \boxed{\frac{f(b)^2f(d)f(e)}{K}
 \mathbf1_{\{|y|<m(b,d,e)\}}},\qquad
 m(b,d,e)=\min(|d-b|,|e-b|),
\]
with respect to \(db\,dd\,de\,dy\). Equivalently, the limiting triple \((B,D,E)\) has density \(2m(b,d,e)f(b)^2f(d)f(e)/K\), and its normalized collision displacement \(Y/m(B,D,E)\) is independent and uniform on \((-1,1)\).

Martin's established one-quadrilateral density implies \(\Pr(|R_4|>t)\sim 2\log(t)/(\pi^2t)\); hence this joint theorem yields the sharp conditional rarity
\[
 \boxed{\Pr(|R_5|>t\mid |R_4|>t)
 \sim \frac{\pi^2K}{2\log t}}.
\]

## Assumptions and scope

The sample size is exactly five; labels are retained (no random reordering to enforce a canonical cross ratio). Each sample is arclength-uniform on a single Euclidean circle, viewed as the ideal boundary of the hyperbolic disk. The cross ratios are real because all points lie on a generalized circle. The conditional measures are on the real-coordinate quadruple \((B,D,E,Y_t)\), with total variation taken after the deterministic rescaling \(Y_t=t(C-B)\). The result is invariant under an initial rotation; it is not a claim that the sampling distribution is invariant under arbitrary Möbius transformations. At zero-measure point coincidences, cross ratios can be assigned arbitrarily.

## Proof

**1. Exact Cauchy coordinate reduction.** Conditional on the argument of \(Z_1\), rotate all five points by its negative. The remaining four arguments are still independent uniform angles. The cotangent half-angle map sends their angular coordinates to independent standard real Cauchy variables \(B,C,D,E\) with density \(f(x)=1/[\pi(1+x^2)]\). Because a cross ratio is preserved by the projective coordinate map and the first point maps to infinity, its defining differences simplify exactly to
\[
 R_4=\frac{D-B}{C-B},\qquad R_5=\frac{E-B}{C-B}.
\]
Thus \(E_t\) is precisely the event \(t|C-B|<m(B,D,E)\).

**2. Exact scaled density.** Condition on \((B,D,E)=(b,d,e)\), put \(m=m(b,d,e)\), and substitute \(y=t(c-b)\). The conditional event \(E_t\) has, after multiplying its probability by \(t\), the unnormalized density
\[
 h_t(b,d,e,y)=f(b)f(d)f(e)f(b+y/t)
 \mathbf1_{\{|y|<m(b,d,e)\}}.
\]
Pointwise, \(h_t\) converges to
\[
 h(b,d,e,y)=f(b)^2f(d)f(e)\mathbf1_{\{|y|<m(b,d,e)\}}.
\]
We must justify passing the integral through the limit despite the Cauchy tails.

**3. A uniform-integrability argument.** Since the Cauchy tail is bounded by a constant times the reciprocal of its argument, \(\mathbb E\min(|D|,|E|)<\infty\), and
\[
 \mathbb E\,m(b,D,E)\le |b|+\mathbb E\min(|D|,|E|).
\]
Consequently \(\int_{\mathbb R}f(b)^2\mathbb Em(b,D,E)\,db<\infty\); in particular \(\int h=K\in(0,\infty)\).

For \(|b|\le1\), \(f(b+y/t)\le1/\pi\), and the bound \(\mathbb E m(b,D,E)\le1+\mathbb E\min(|D|,|E|)\) is integrable. For \(|b|>1\), split the \(y\)-region into \(|y|\le t|b|/2\) and its complement. On the first part, \(|b+y/t|\ge |b|/2\), so \(f(b+y/t)\le4f(b)\); the resulting dominating function integrates by the preceding estimate. On the second part, its nonempty intersection with \(|y|<m\) requires \(m>t|b|/2\). For \(t\ge4\), this forces both \(|D|>t|b|/4\) and \(|E|>t|b|/4\). Since these are independent Cauchy variables, the probability is at most \(C/(t^2b^2)\) for a fixed numerical \(C\). Using \(\int_{\mathbb R}f(b+y/t)\,dy=t\), the full contribution of this second part to \(\int h_t\) is at most
\[
 \frac Ct\int_{|b|>1}\frac{f(b)}{b^2}\,db=O(t^{-1}).
\]
Therefore dominated convergence on the main part, plus this vanishing remainder, proves \(\int h_t\to\int h=K\), which is precisely \(t\Pr(E_t)\to K\).

**4. Marked total-variation convergence.** The nonnegative densities \(h_t\) converge almost everywhere to \(h\), and their integrals converge to the same finite positive \(K\). Scheffé's lemma gives \(\|h_t-h\|_1\to0\). Dividing each by its total mass proves the claimed convergence in total variation of the conditional distributions. Integrating \(h/K\) over the interval \((-m,m)\) gives the stated size-biased triple density; transforming \(u=y/m\) shows that \(u\) is uniform on \((-1,1)\) independently of that triple.

**5. Explicit constant and conditional probability.** For fixed \(b\), the survival probability of \(|D-b|\) at \(s>0\) is
\[
 1-\frac{\arctan(b+s)-\arctan(b-s)}{\pi}.
\]
Using the tail-integral identity for the minimum of two independent nonnegative variables yields the displayed absolutely convergent double integral for \(K\). The established one-cross-ratio density of Martin [2, Theorem 4.1] satisfies \(p(r)=(\log|r|+O(1))/(\pi^2r^2)\) as \(r\to\pm\infty\). Integrating both tails gives \(\Pr(|R_4|>t)\sim 2\log(t)/(\pi^2t)\). Divide the joint asymptotic by this marginal asymptotic to obtain the conditional formula.

## Verification

A standalone script `verify_pentagon_crossratios.py` uses an independent Cauchy-tail integral for the constant, Gaussian-adaptive numerical quadrature, and a Rao–Blackwellized simulation: the rare-coordinate \(C\) is integrated exactly conditional on \(B,D,E\), rather than estimated by a handful of rare raw Bernoulli events. It compares finite-threshold \(t\Pr(E_t)\) at four thresholds to the integral, with explicit random seed and standard errors. This is numerical corroboration only; the proof of the full limits is Steps 1–5 above.

## Relationship to prior work

Kato and McCullagh [1] analyze Möbius transformations and stereographic/Cauchy laws on spheres. Their paper establishes the probabilistic coordinate framework, not a joint five-point cross-ratio tail. Martin [2] derives the **one-dimensional** cross-ratio density of four independent uniform ideal-boundary points (Theorem 4.1); it supplies the marginal tail used in the conditional comparison, but cannot determine the joint law for two ratios sharing three of five points, or the size-biased marked collision distribution. Relevant comparisons against published mathematical records on random pentagons, circular crossings, and ideal-hyperbolic cusp statistics did not find an equivalent statement; name-based or semantic search alone cannot certify priority.

The present result concerns a natural simultaneous degeneration of two overlapping ideal quadrilaterals, or a codimension-one cusp direction in the random ideal-pentagon configuration. The distinction from independently sampled quadrilaterals is essential: the denominators are **shared**, and the resulting joint tail is \(t^{-1}\), whereas the product of the two individual tails is of order \(t^{-2}(\log t)^2\).

## Limitations

Only five independent uniformly distributed **labelled** ideal-boundary points, and the specified two overlapping cross ratios, are covered. Canonically ordered polygonal moduli can use a different cross-ratio normalization and need not have the same tail event. The coefficient is an absolutely convergent integral, not a claimed elementary constant. The total-variation result is about the conditional stereographic marks, not a uniform approximation for all thresholds. The work does not classify every degeneration stratum of higher ideal polygons. Historical priority remains provisional, and no independent mathematical audit has been performed.

## References

[1] S. Kato and P. McCullagh, *Möbius transformation and a Cauchy family on the sphere*, first public 26 October 2015, arXiv:1510.07679, https://arxiv.org/abs/1510.07679 (especially introduction and §3, stereographic transformation).

[2] G. J. Martin, *Random Ideal Hyperbolic Quadrilaterals, the Cross Ratio Distribution and Punctured Tori*, first public 17 July 2018, arXiv:1807.06202, https://arxiv.org/abs/1807.06202 (especially §4 and Theorem 4.1); later J. London Math. Soc. 100 (2019), 851–870, https://doi.org/10.1112/jlms.12249.
