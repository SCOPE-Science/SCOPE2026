# A rank-gap transition in the extreme tails of Cauchy quantile-ratio statistics

## Finding
Let \(X_1,\ldots,X_n\) be independent observations from any nondegenerate Cauchy location-scale distribution, let \(n\ge4\), and choose integer ranks \(2\le b<c\le n-1\). Define
\[
R_{n;b,c}=\frac{X_{(c)}-X_{(b)}}{X_{(n)}-X_{(1)}},\qquad r=c-b.
\]
This is a range-normalized four-quantile spacing with empirical inverse-CDF quantiles at ranks \(1,b,c,n\). Its sharp fixed-\(n\) lower tail changes discontinuously with the number of intervening ranks:
\[
\Pr(R_{n;b,c}<t)\sim
\begin{cases}
A_{n,b}\,t\log(1/t),&r=1,\\
B_{n;b,c}\,t,&r\ge2,
\end{cases}\quad t\downarrow0.
\]
The constants are finite and positive. To specify them, let \(Y_{(1)}<\cdots<Y_{(m)}\) be order statistics from \(m=n-1\) independent *standard* Cauchy draws. Write \(p_{m;j,k}(g)\) for the density of \(Y_{(k)}-Y_{(j)}\) for \(1\le j<k\le m\). Then
\[
A_{n,b}=\frac{n}{\pi}\{p_{n-1;b,b+1}(0)+p_{n-1;b-1,b}(0)\},
\]
where the density at zero denotes its continuous right limit, and
\[
B_{n;b,c}=\frac{n}{\pi}\left\{\mathbb E\frac1{Y_{(c)}-Y_{(b)}}+\mathbb E\frac1{Y_{(c-1)}-Y_{(b-1)}}\right\}\quad (r\ge2).
\]
All expectations in the last display are finite. These formulas are independent of the Cauchy location and scale. An explicit one-dimensional representation for the adjacent-gap density is
\[
p_{m;j,j+1}(0)=\frac{m!}{(j-1)!(m-j-1)!\,\pi}
\int_0^1u^{j-1}(1-u)^{m-j-1}\sin^2(\pi u)\,du.
\]
For the minimal four-distinct-rank instance \(n=4,b=2,c=3\), both endpoints admit elementary sharp constants:
\[
\boxed{\Pr(R_{4;2,3}<t)\sim\frac{12}{\pi^2}\,t\log(1/t),\qquad
\Pr(R_{4;2,3}>1-t)\sim\frac3{\pi^2}t^2.}
\]
Consequently \(\mathbb E[R_{4;2,3}^{-q}]<\infty\) exactly for \(q<1\), and \(\mathbb E[(1-R_{4;2,3})^{-q}]<\infty\) exactly for \(q<2\), with \(q\ge0\).

## Assumptions and scope
All limits are \(t\downarrow0\) at **fixed** finite \(n,b,c\); they are not large-sample limits. The parent is any Cauchy \(C(\mu,\sigma)\) with real \(\mu\) and \(\sigma>0\). Quantiles in the connection to rank-based testing mean \(Q_n(p)=X_{(\lceil np\rceil)}\) for \(p\in(0,1)\), not an interpolated quantile convention. The interior indices satisfy \(2\le b<c\le n-1\), so the denominator uses genuinely different extremal observations. This is a class of four-quantile ratios, not a claim about every particular software interpolation implementation.

For example, the reported four probabilities \((0.02217468,0.25,0.75,0.97782532)\) in Pekgör's Cauchy test give ranks \((1,3,8,10)\) at \(n=10\) under this explicit inverse-CDF convention; hence that small-sample rank version has a linear, rather than a fifth-power, lower null tail. No numerical value of its linear coefficient is claimed here.

## Proof
Put \(f(x)=1/[\pi(1+x^2)]\), \(F(x)=1/2+\arctan(x)/\pi\), \(G=X_{(c)}-X_{(b)}\), \(L=X_{(n)}-X_{(1)}\) and \(V=L^{-1}\), so \(R=GV\). Location-scale invariance allows this standard-Cauchy normalization.

**1. Extreme-range density lemma.** Let \(h(g,v)\) be the joint density of \((G,V)\). The ordered-sample density \(n!\prod_i f(x_i)\), with the constraints \(G=g\) and \(L=v^{-1}\), gives, for each \(g>0\),
\[
\lim_{v\downarrow0}h(g,v)=H_{n;b,c}(g):=\frac n\pi\{p_{n-1;b,c}(g)+p_{n-1;b-1,c-1}(g)\}.
\]
The convergence is locally uniform for \(g\ge0\), using continuous right limits at zero. The two summands correspond respectively to a single right or left extreme escaping to infinity. Indeed \(f(x)\sim1/(\pi x^2)\) at both ends; choosing the extreme observation gives factor \(n\), while the remaining \(n-1\) observations retain their ordinary order-statistic spacing density. The region with two escaping observations is smaller order: after changing from extreme endpoints to range and one endpoint, its integrand has at least two Cauchy tail-density factors. Splitting the endpoint integral into bounded neighborhoods of its two ends and a middle region proves the displayed limit by dominated convergence. The same representation and \(\sup f<\infty\) give \(h(g,v)\le Cg^{r-1}\) for \(0<g\le\delta\), \(0<v\le v_0\), with fixed sufficiently small \(\delta,v_0>0\). The \(r-1\) internal observations between the specified ranks produce the power \(g^{r-1}\).

In particular, standard order-statistic integration gives
\[
p_{m;j,j+1}(0)=\frac{m!}{(j-1)!(m-j-1)!}\int_{\mathbb R}f(y)^2F(y)^{j-1}(1-F(y))^{m-j-1}\,dy.
\]
The substitution \(u=F(y)\), \(f(F^{-1}(u))=\sin^2(\pi u)/\pi\), yields the stated one-dimensional formula. For separated ranks \(k-j=r\), the gap density is \(O(g^{r-1})\) near zero. Therefore \(\mathbb E[(Y_{(k)}-Y_{(j)})^{-1}]<\infty\) exactly when \(r\ge2\).

**2. Transfer from the joint density to the ratio tail.** The basic integral is
\[
\Pr(GV<t)=\int_0^\infty\int_0^\infty\mathbf1_{\{gv<t\}}h(g,v)\,dv\,dg.
\]
For \(r=1\), \(h(g,v)\to H(0)>0\) as \((g,v)\to(0,0)\). On a fixed square \((0,\delta)^2\), its integral is \((H(0)+o_\delta(1))\{t\log(\delta^2/t)+t\}\). The two exterior strips contribute \(O_\delta(t)\): \(\Pr(G<t/\delta)=O(t)\) by bounded adjacent-gap density, and \(\Pr(V<t/\delta)=O(t)\) by the Cauchy sample-range tail. Letting \(t\to0\), then \(\delta\downarrow0\), gives \(A_{n,b}=H(0)\).

For \(r\ge2\), fix \(0<\delta<M\). On \(\delta<g<M\), local uniformity gives
\[
\lim_{t\downarrow0}\frac1t\Pr(GV<t,\ \delta<G<M)=\int_\delta^M\frac{H(g)}g\,dg.
\]
The \(g>M\) contribution is at most \(\Pr(V<t/M)=O(t/M)\). The \(g<\delta\) contribution is \(O(t\delta^{r-1})+O(t^r)\), by splitting at \(v=v_0\) and using the joint bound \(Cg^{r-1}\) for smaller \(v\) and the ordinary \(O(s^r)\) small-gap law for bounded ranges. Thus the \(t\)-coefficient is \(\int_0^\infty H(g)g^{-1}\,dg\). Substituting the two gap densities gives the stated \(B_{n;b,c}\). Positivity is immediate.

**3. The four-rank left constant.** For \(n=4,b=2,c=3\), the three-sample adjacent-gap densities satisfy \(p_{3;1,2}(0)=p_{3;2,3}(0)=3/(2\pi)\); their evaluation uses symmetry and \(\int f(y)^2dy=1/(2\pi)\). Hence \(A_{4,2}=4(3/\pi)/\pi=12/\pi^2\).

**4. The four-rank right constant.** Let \(y=X_{(1)}\), \(z=X_{(4)}\), \(d=z-y\). Writing \(X_{(2)}=y+s\), \(X_{(3)}=z-u\) gives \(R>1-t\) if and only if \(s,u\ge0\) and \(s+u<td\). The exact integral is
\[
24t^2\int_{y<z}d^2f(y)f(z)\int_{\substack{a,b\ge0\\a+b<1}}f(y+tad)f(z-tbd)\,da\,db\,dy\,dz.
\]
As \(t\downarrow0\), its coefficient becomes \(12\int_{y<z}(z-y)^2f(y)^2f(z)^2\,dy\,dz\). To justify interchanging limit and integration, put \(d=z-y\) and split the integration over \(y\) into neighborhoods of the two endpoint clusters \(y\approx0\) and \(y\approx-d\) and their complement. Since \(0\le ta,tb\le1/4\), the two pairs of Cauchy densities are separated by at least \(d/2\). Their integrated product is bounded by \(C(1+d)^{-4}\) for \(d\ge1\), uniformly in \(a,b,t\); the remaining \(d\le1\) integral is bounded by \(\sup f\). Multiplication by \(d^2\) is therefore integrable, proving dominated convergence. Symmetry and \(\int f^2=\int x^2f(x)^2dx=1/(2\pi)\) yield
\[
12\int_{y<z}(z-y)^2f(y)^2f(z)^2\,dy\,dz
=12\left[\int x^2f(x)^2dx\right]\left[\int f(x)^2dx\right]
=3/\pi^2.
\]
Integrating the two sharp endpoint tails by the layer-cake identity yields the reciprocal-moment thresholds.

## Verification
The standalone `check.py` verifies the adjacent-density integral and symmetry at several integer rank pairs, the explicit constants \(12/\pi^2\) and \(3/\pi^2\), the finite separated-rank reciprocal-gap example, and two numerical quadrature comparisons against the exact four-rank integral. It does not substitute finite arithmetic for the limiting argument above. Run with `python check.py` using NumPy and SciPy.

## Relationship to prior work
Pekgör (2023) defines Cauchy goodness-of-fit through an affine-invariant ratio of four sample quantile spacings, derives a fixed-quantile large-sample null normal approximation, and tabulates simulated finite-sample calibration; the fixed-small-sample, extreme-range lower-tail phase transition is not established in the inspected main article. Rublík (2001) studies a *different*, extreme-order-statistic quadratic-form Cauchy test. Ghosh and Jammalamadaka (1998) analyze spacing tests on probability-integral-transformed uniform observations, not the raw-Cauchy range-normalized four-quantile ratio. Nagaraja, Bharath and Zhang (2015) analyze local spacings as sample size grows, not fixed-sample vanishing-threshold tails. These works explain the motivation or establish general tools but do not directly imply the explicit logarithmic and linear constants without the joint boundary calculation above.

## Limitations
The theory is fixed-\(n\) only and applies to the explicitly defined empirical inverse-CDF rank convention with both extreme ranks selected. It neither calibrates an interpolated-sample-quantile implementation nor asserts a uniform approximation at moderate thresholds or as \(n\to\infty\). The right-tail constant is proved only in the four-rank case. Existing general spacing/regular-variation methods may provide alternative derivations; absence of a matching search result is not a uniqueness or historical-priority certificate. Independent mathematical checking has not been performed.

## References
1. A. Pekgör, *A Novel Goodness-of-Fit Test for Cauchy Distribution*, Journal of Mathematics (2023), DOI: 10.1155/2023/9200213, first published 2023-03-14. https://doi.org/10.1155/2023/9200213
2. F. Rublík, *A quantile goodness-of-fit test for Cauchy distribution, based on extreme order statistics*, Applications of Mathematics 46 (2001), 339–351. https://dml.cz/dmlcz/134472
3. K. Ghosh and S. R. Jammalamadaka, *Small sample approximations for spacing statistics*, Journal of Statistical Planning and Inference 69 (1998), 245–261. https://jammalam.faculty.pstat.ucsb.edu/html/Some%20Publications/1998_SmallSample%20AppoxSpacings_JSPI.pdf
4. H. N. Nagaraja, K. Bharath and F. Zhang, *Spacings around an order statistic*, Annals of the Institute of Statistical Mathematics 67 (2015), 515–540. https://doi.org/10.1007/s10463-014-0466-9
