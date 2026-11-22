# Sharp bounded-variation contraction of opposed power Hardy averages

## Finding
For every \(\alpha,\beta>0\), the two orders of normalized one-sided power averaging are **strict** contractions on real \(BV(0,1)\) modulo constants, even though each one-sided average separately has seminorm one. Their sharp operator norms are determined by different unique interior jump locations. Specifically, let \(s_{\alpha,\beta}\in(0,1)\) and \(t_{\alpha,\beta}\in(0,1)\) be the unique roots
\[
\beta\int_{s_{\alpha,\beta}}^1\frac{(1-u)^{\beta-1}}{u^\alpha}\,du=1,
\qquad
\alpha\int_0^{t_{\alpha,\beta}}\frac{u^{\alpha-1}}{(1-u)^\beta}\,du=1.
\]
Then the best constants are
\[
\|R_\beta L_\alpha\|_{BV/\mathbb R}=1-(1-s_{\alpha,\beta})^\beta,
\qquad
\|L_\alpha R_\beta\|_{BV/\mathbb R}=1-t_{\alpha,\beta}^\alpha.
\]
Both lie strictly between zero and one. In each order, all nonconstant norming real BV inputs are exactly a nonzero multiple of the one-jump Heaviside function at the specified root, plus an arbitrary constant (up to almost-everywhere equivalence).

For the unweighted pair, both orders have norm \(e^{-1}\). On the one-parameter slice \(\beta=1\), the first norm has the closed form
\[
\|R_1L_\alpha\|_{BV/\mathbb R}
=\begin{cases}\alpha^{1/(1-\alpha)},&\alpha\ne1,\\ e^{-1},&\alpha=1.\end{cases}
\]
The two orders genuinely differ: at \((\alpha,\beta)=(1,2)\),
\[
\|L_1R_2\|_{BV/\mathbb R}=\frac12
\quad\text{but}\quad
\|R_2L_1\|_{BV/\mathbb R}=0.512390465\ldots>\frac12.
\]

## Assumptions and scope
The domain is the real space \(BV(0,1)\) of Lebesgue-a.e. equivalence classes with distributional derivative \(Df\) a finite signed Radon measure on the *open* interval; the seminorm is \(V(f)=|Df|((0,1))\). It vanishes exactly on constants. For \(x\in(0,1)\) define
\[
(L_\alpha f)(x)=\frac{\alpha}{x^\alpha}\int_0^x u^{\alpha-1}f(u)\,du,
\qquad
(R_\beta f)(x)=\frac{\beta}{(1-x)^\beta}\int_x^1(1-u)^{\beta-1}f(u)\,du.
\]
For \(\alpha,\beta>0\) each integral exists for bounded BV representatives, and both maps preserve constants and increasing functions. All operator norms below are with respect to \(V\), not \(L^p\), supremum, essential oscillation or derivative-weighted norms. The endpoints of output functions are understood by their one-sided continuous limits; they contribute to total variation only through their interior variation.

## Proof
**1. Positive step decomposition.** For each \(s\in(0,1)\) let \(h_s(x)=\mathbf1_{(s,1)}(x)\). Every \(f\in BV(0,1)\) has, a.e., the representation \(f(x)=c+\int_{(0,1)}h_s(x)\,d\mu(s)\), where \(\mu=Df\) and \(V(f)=|\mu|((0,1))\). The identities \(L_\alpha f(x)=\int_0^1 f(xv^{1/\alpha})\,dv\) and \(R_\beta f(x)=\int_0^1 f(1-(1-x)v^{1/\beta})\,dv\) show that each operator maps nondecreasing inputs to nondecreasing outputs. Thus the two compositions send each \(h_s\) to a nondecreasing continuous function, and its variation equals the difference of its endpoint limits. Linearity, Fubini, and the triangle inequality for distributional derivatives give, for either composition \(T\),
\[
V(Tf)\le\int_{(0,1)}V(Th_s)\,d|\mu|(s)
\le \Big(\sup_{0<s<1}V(Th_s)\Big)V(f).
\]
A step \(h_s\) gives the reverse inequality at each \(s\). Hence the norm is exactly the supremum of the single-jump output variations.

**2. Right after left.** For \(x<s\), \(L_\alpha h_s(x)=0\), while for \(x>s\), \(L_\alpha h_s(x)=1-(s/x)^\alpha\). At \(x=1\), \((R_\beta L_\alpha h_s)(1)=1-s^\alpha\). At \(x=0\), its value is \(\beta\int_s^1(1-u)^{\beta-1}[1-(s/u)^\alpha]du\). The variation is therefore
\[
A(s)=1-s^\alpha-(1-s)^\beta+
\beta s^\alpha\int_s^1(1-u)^{\beta-1}u^{-\alpha}\,du.
\]
Differentiation (valid at every \(0<s<1\)) yields
\[
A'(s)=\alpha s^{\alpha-1}\left[\beta\int_s^1(1-u)^{\beta-1}u^{-\alpha}\,du-1\right].
\]
The bracket is continuous and strictly decreasing; at \(s=1\) it equals \(-1\), and at \(s\downarrow0\) it is positive, since it equals \(\mathbb E[U^{-\alpha}]-1\) for \(U\sim\operatorname{Beta}(1,\beta)\), interpreted as \(+\infty\) if necessary. Consequently there is a unique maximizer \(s_{\alpha,\beta}\), and its stationarity equation cancels the two \(s^\alpha\) terms in \(A\), giving \(A(s_{\alpha,\beta})=1-(1-s_{\alpha,\beta})^\beta\). Both endpoint limits \(A(0+)=A(1-)=0\) follow either directly from the normalized probability kernels or by dominated convergence for fixed parameter values.

**3. Left after right.** For \(x<s\), \(R_\beta h_s(x)=((1-s)/(1-x))^\beta\), and for \(x>s\), it equals one. The endpoint difference for \(L_\alpha R_\beta h_s\) is
\[
B(s)=1-s^\alpha-(1-s)^\beta+
\alpha(1-s)^\beta\int_0^s u^{\alpha-1}(1-u)^{-\beta}\,du.
\]
Its derivative is
\[
B'(s)=\beta(1-s)^{\beta-1}\left[1-\alpha\int_0^s u^{\alpha-1}(1-u)^{-\beta}\,du\right].
\]
The bracket strictly decreases from \(1\) to a negative value, because the limiting integral is the expectation of \((1-U)^{-\beta}\) for \(U\sim\operatorname{Beta}(\alpha,1)\), strictly larger than one (possibly infinite). The only maximizer is therefore \(t_{\alpha,\beta}\), and substituting its equation gives \(B(t_{\alpha,\beta})=1-t_{\alpha,\beta}^\alpha\). Both maxima are strictly between zero and one.

**4. Equality and special cases.** Since each profile \(A\) or \(B\) has one strict maximizer, equality in the bound from Step 1 for nonconstant \(f\) forces \(|Df|\) to be supported at that single interior point. Hence \(Df=c\delta_s\), so \(f\) is a nonzero one-jump function plus a constant. Conversely those functions attain equality. When \(\beta=1\), the first root solves \(\int_s^1u^{-\alpha}du=1\), yielding the closed form stated above and the continuous \(\alpha=1\) limit \(e^{-1}\). For \((\alpha,\beta)=(1,1)\), reflection gives the same value in the opposite order.

At \((\alpha,\beta)=(1,2)\), Step 3 simplifies to \(B(s)=2s(1-s)\), with unique maximum \(1/2\) at \(s=1/2\). Step 2 gives \(A(s)=-s+s^2-2s\log s\). Its exact value at \(s=1/3\) is \((2/3)\log3-2/9>1/2\), because the positive power series \(\log3=2\sum_{k\ge0}(1/2)^{2k+1}/(2k+1)\) is strictly greater than \(1+1/12=13/12\). Thus the other order has a strictly larger norm. The exact optimal root solves \(2s-3-2\log s=0\).

## Verification
The standalone Python standard-library file `verify_hardy.py` checks the root equations and step-profile gains for six positive parameter pairs, confirms the \(e^{-1}\) and \(\beta=1\) cases, checks a rational strict inequality certificate for order noncommutativity, and stress-tests 24 random signed four-step combinations on a spatial grid. Execute `python verify_hardy.py`. The numerical quadrature is a check, not a substitute for the all-parameter analytical proof. The checker uses deterministic test inputs and no external datasets.

## Relationship to prior work
Classical Hardy/Cesàro operator norm inequalities address a different operator geometry. Fu, Lu and Yuan (2012) study positive weighted Hardy averaging, its adjoints, and sharp estimates in central Morrey and Campanato spaces; their full-text conclusions concern those norms and weighted commutators, not \(BV\)-seminorms of *oppositely oriented normalized* compositions. Gogatishvili and Mustafayev (2017) establish reduction/equivalence and weighted Lebesgue inequalities for iterated Hardy and Copson operators; their full text includes monotone-cone restrictions but does not state the present sharp real-BV contraction formulas or uniquely norming jump locations. The general step-measure representation is standard; the two-parameter exact constants and order comparison are the proposed contribution. Operator bounds implicit in more abstract historical results have not been ruled out categorically.

## Limitations
These results concern scalar real BV on one finite open interval, strictly positive power parameters, normalized left/right averages and exactly two stages. They make no claim about complex BV, more stages, arbitrary weights, multidimensional domains, \(L^p\) norms or other notions of oscillation. The explicit \(0.512390465\ldots\) is a numerical approximation to a uniquely defined transcendental root, not a rational certificate for that decimal. Published priority has not been independently certified.

## References
1. Z. W. Fu, S. Z. Lu and W. Yuan, “A Weighted Variant of Riemann-Liouville Fractional Integrals on \(\mathbb R^n\),” *Abstract and Applied Analysis* (first published 2012-09-12), https://doi.org/10.1155/2012/780132 .
2. A. Gogatishvili and R. Ch. Mustafayev, “Weighted iterated Hardy-type inequalities,” *Mathematical Inequalities & Applications* **20** (2017), 683–728, https://doi.org/10.7153/mia-20-45 .
3. Y. Mizuta, A. Nekvinda and T. Shimomura, “Hardy Averaging Operator on Generalized Banach Function Spaces and Duality,” *Z. Anal. Anwend.* **32** (2013), 233–255, https://doi.org/10.4171/ZAA/1483 (abstract consulted; complete text not accessible during comparison).
