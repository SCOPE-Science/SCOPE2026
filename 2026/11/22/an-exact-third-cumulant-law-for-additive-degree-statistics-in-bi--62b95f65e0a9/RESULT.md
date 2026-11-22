# An exact third-cumulant law for additive degree statistics in binomial random graphs

## Finding

For every integer \(n\ge3\), all edge probabilities \(0<p<1\), and any real function \(h\colon\{0,\ldots,n-1\}\to\mathbb R\), the third cumulant of an additive vertex-degree statistic in \(G(n,p)\) is an explicit sum of three contributions from one, two, and three distinct vertices. The three-vertex contribution involves only the first two binomially averaged finite differences of \(h\), and captures skewness invisible in the usual covariance law.

Let \(B_r\sim\mathrm{Bin}(r,p)\) in the expectation definitions below. Set
\[
\begin{gathered}
T_h=\sum_{v=1}^{n}h(D_v),\qquad \Delta h(k)=h(k+1)-h(k),\\
\mu=\mathbb E h(B_{n-1}),\quad M_2=\mathbb E[h(B_{n-1})^2],\quad M_3=\mathbb E[h(B_{n-1})^3],\\
a=\mathbb E\Delta h(B_{n-2}),\quad b=\mathbb E\Delta(h^2)(B_{n-2}),\\
\beta=\mathbb E\Delta h(B_{n-3}),\quad\gamma=\mathbb E\Delta^2 h(B_{n-3}).
\end{gathered}
\]
The exact identity is
\[
\boxed{\begin{aligned}
\kappa_3(T_h)={}&n(M_3-3\mu M_2+2\mu^3)\\
&+3n(n-1)p(1-p)a(b-2\mu a)\\
&+n(n-1)(n-2)p^2(1-p)^2\gamma\bigl(3\beta^2+6p\beta\gamma+p(2p+1)\gamma^2\bigr).
\end{aligned}}
\]
Here \(\kappa_3(X)=\mathbb E[(X-\mathbb EX)^3]\), not a standardized skewness.

A substantive specialization is the isolated-vertex count \(Z_n\). For \(q=1-p\),
\[
\boxed{\begin{aligned}
\kappa_3(Z_n)={}&nq^{n-1}(1-q^{n-1})(1-2q^{n-1})\\
&+3n(n-1)pq^{2n-3}(1-2q^{n-1})\\
&+n(n-1)(n-2)p^2q^{3n-6}(3-2p).
\end{aligned}}
\]
At sparse edge probability \(p=c/n\) with fixed \(c>0\),
\[
\frac{\kappa_3(Z_n)}n\longrightarrow
K(c)=e^{-c}+(3c-3)e^{-2c}+(3c^2-6c+2)e^{-3c}.
\]
There is exactly one positive number \(c_*\) such that \(K(c_*)=0\), numerically \(c_*\approx0.500975328666459\). The function is strictly negative below this threshold and strictly positive above it. This is a unique transition in the limiting *third cumulant*, not a theorem of unique finite-sample zeros.

## Assumptions and scope

The graph is simple, undirected, loopless, and has independent identically distributed Bernoulli edges. No boundedness, smoothness, or monotonicity is imposed on the finite-domain degree score \(h\). All binomial expectations are finite sums and may be computed exactly for rational \(p\) and rational-valued \(h\). The terms using \(B_{n-3}\) remain defined at \(n=3\) by the degenerate \(B_0=0\). The sparse limit considers fixed positive \(c\) and integer \(n>c\); it is not uniform in unbounded \(c\).

## Proof

**1. Partition a third cumulant.** By multilinearity, \(\kappa_3(T_h)\) is the sum over ordered triples of vertex labels of their joint third cumulants. There are \(n\) triples with every label equal, \(3n(n-1)\) with precisely two equal, and \(n(n-1)(n-2)\) with all different. The all-equal cumulant is \(M_3-3\mu M_2+2\mu^3\).

**2. Precisely two equal labels.** For distinct vertices \(u,v\), expose their common edge \(Y\sim\mathrm{Bernoulli}(p)\). The degrees are \(Y+S_u\) and \(Y+S_v\), with independent \(S_u,S_v\sim\mathrm{Bin}(n-2,p)\), independent of \(Y\). Conditional expectation of \(h(Y+S_u)\) is affine in \(Y\), with increment \(a\), and that of its square has increment \(b\). Thus
\[
\operatorname{Cov}(h(D_u),h(D_v))=p(1-p)a^2,\quad
\operatorname{Cov}(h(D_u)^2,h(D_v))=p(1-p)ab.
\]
For arbitrary \(X,Y\), \(\kappa(X,X,Y)=\operatorname{Cov}(X^2,Y)-2\mathbb E[X]\operatorname{Cov}(X,Y)\). Hence each precisely-two-equal triple contributes \(p(1-p)a(b-2\mu a)\).

**3. Three distinct labels.** Expose the three internal edges among vertices \(1,2,3\), and write their centered independent indicators as \(x_{12},x_{13},x_{23}\). Their common variance is \(v=p(1-p)\). The external incident edge sets at these vertices are mutually independent, each yielding a \(\mathrm{Bin}(n-3,p)\) degree contribution. Conditional on the three internal edges, the three degree scores are independent. By finite differences, the conditional mean at vertex \(1\) minus its unconditional mean is exactly
\[
A(x_{12}+x_{13})+\gamma x_{12}x_{13},\quad A=\beta+p\gamma,
\]
with the analogous expressions at vertices \(2,3\). Consequently, their joint third cumulant equals the expected product of these centered conditional means. Every nonzero term must use each independent centered edge at least twice. There are precisely three products with one quadratic factor and two linear factors, totaling \(3A^2\gamma v^2\), and one with three quadratic factors, totaling \(\gamma^3v^3\). Substituting \(A=\beta+p\gamma\) and \(v=p(1-p)\) yields
\[
\kappa(h(D_1),h(D_2),h(D_3))=p^2(1-p)^2\gamma[3\beta^2+6p\beta\gamma+p(2p+1)\gamma^2].
\]
Combining the three vertex-label cases proves the exact identity for all stated \(n,p,h\).

**4. Isolated vertices and the sparse sign switch.** Substitute \(h(k)=\mathbf1_{\{k=0\}}\). Then \(h^2=h\), \(\mu=q^{n-1}\), \(a=b=-q^{n-2}\), \(\beta=-q^{n-3}\), \(\gamma=q^{n-3}\), obtaining the isolated-vertex formula. For \(p=c/n\), take each exponential limit \((1-c/n)^{kn+O(1)}\to e^{-kc}\) and divide by \(n\), proving \(K(c)\). Finally set
\[
F(c)=e^{3c}K(c)=e^{2c}+(3c-3)e^c+3c^2-6c+2.
\]
Direct differentiation gives \(F(0)=0\), \(F'(0)=-4\), and
\[
F''(c)=4e^{2c}+3(c+1)e^c+6>0\qquad(c\ge0).
\]
Since \(F(c)\to+\infty\) as \(c\to\infty\), strict convexity implies exactly one positive zero, with the asserted sign pattern. The displayed numerical root is a reproducible approximation, not needed for the uniqueness proof.

## Verification

The standalone script `checker.py` performs exhaustive rational-probability enumeration of every labeled graph on \(3\) through \(6\) vertices for seven distinct degree-score families and three nontrivial edge probabilities, then verifies the arbitrary-degree identity. It additionally checks the degree-sum specialization for \(3\le n\le39\). It reports **195 exact assertions passed**. In that specialization, the formula reduces to \(\kappa_3(2|E|)=4n(n-1)p(1-p)(1-2p)\), as required by the binomial edge count. Finite enumeration does not establish the theorem; the proof above does.

Reproduction: run `python3 checker.py` with a standard Python 3 installation. No external packages or data are necessary.

## Relationship to prior work

Janson [1], especially Section 4 and Theorem 4.1, establishes Gaussian joint limits and a covariance law for degree-count statistics in the sparse Erdős–Rényi regime, and discusses their fixed-edge counterparts. Lin and Reinert [2], especially Sections 2–3, derive dependent degree-count approximations, including second-order covariances, under general independent-edge probabilities. These are directly applicable background on the same random-graph degree-count object but do not state the exact third-order identity or the isolated-count sparse cumulant sign boundary. The result is an explicit third-order calculation, not a new Gaussian limit or a claim to have invented the vertex-degree dependence method.

## Limitations

The formula does not extend without modification to dependent-edge models or fixed-edge sampling. The sparse sign theorem concerns the sign of the \(n\)-normalized third cumulant at fixed mean degree, not all finite graph orders, finite-sample unique crossings, standardized skewness errors, or an Edgeworth expansion. General third-cumulant diagram expansions may contain this formula as a specialization; a comprehensive historical-priority search beyond the inspected works remains desirable. No independent audit has been performed.

## References

[1] S. Janson, *Monotonicity, asymptotic normality and vertex degrees in random graphs*, first publicly available as arXiv:math/0605642, 2006-05-24; Bernoulli 13 (2007), 952–965. https://arxiv.org/abs/math/0605642

[2] K. Lin and G. Reinert, *Joint Vertex Degrees in an Inhomogeneous Random Graph Model*, first publicly available as arXiv:0912.4812, 2009-12-24; Advances in Applied Probability 44 (2012), 139–165. https://arxiv.org/abs/0912.4812
