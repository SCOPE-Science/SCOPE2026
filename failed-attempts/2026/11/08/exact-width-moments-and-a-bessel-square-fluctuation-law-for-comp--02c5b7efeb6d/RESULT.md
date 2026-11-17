# Exact width moments and a Bessel-square fluctuation law for complete-bipartite symmetric edge polytopes

## Finding

For the intrinsic Euclidean realization of the symmetric edge polytope of any complete bipartite graph, all positive moments of the uniform-direction width have an exact, explicitly normal-integral representation. For balanced graphs, these widths exhibit a sharp non-Gaussian fluctuation law whose cumulative distribution is the square of a modified-Bessel expression; its moment generating function is a gamma quotient, and its mean and variance simplify to \(2\gamma+1\) and \(3\).

Precisely, for integers \(p,q\ge2\), let \(A=\{1,\ldots,p\}\), \(B=\{p+1,\ldots,p+q\}\), and
\[
P_{p,q}=\operatorname{conv}\bigl\{\pm(e_i-e_j):i\in A,\ j\in B\bigr\}\subset H_{p,q},\qquad H_{p,q}=\bigl\{x:\sum_{i=1}^{p+q}x_i=0\bigr\}.
\]
Let \(U\) be uniformly distributed on the Euclidean unit sphere of \(H_{p,q}\), and let \(W_{p,q}=h_{P_{p,q}}(U)+h_{P_{p,q}}(-U)\) be the directional width. Write \(d=p+q-1\) and let \(\phi,\Phi\) denote the standard-normal density and CDF. For \(t\ge0\), define
\[
F_{p,q}(t)=p(p-1)\int_{-\infty}^{\infty}\int_{\ell}^{\ell+2t}
\phi(\ell)\phi(u)[\Phi(u)-\Phi(\ell)]^{p-2}
[\Phi(\ell+t)-\Phi(u-t)]^q\,du\,d\ell.
\]
Then every real \(r>0\) satisfies the **exact finite-dimensional moment formula**
\[
\mathbb E[W_{p,q}^{r}]
=\frac{2^r r\,\Gamma(d/2)}{2^{r/2}\Gamma((d+r)/2)}
\int_0^\infty t^{r-1}[1-F_{p,q}(t)]\,dt.
\]
These moments determine the distribution because \(0\le W_{p,q}\le2\sqrt2\).

For balanced parts \(p=q=m\ge3\), put \(a_m=\Phi^{-1}(1-1/m)\), \(d=2m-1\), and \(\mu_d=\sqrt2\,\Gamma((d+1)/2)/\Gamma(d/2)\). Then
\[
\frac{a_m\sqrt d}{2}W_{m,m}-2a_m^2\ \xrightarrow{d}\ Y,
\]
with convergence of first and second moments. If \(E_1,E_2,E_3,E_4\) are independent \(\operatorname{Exp}(1)\) variables, the limit is
\[
Y=-\log\min\{E_1E_2,E_3E_4\}.
\]
With \(K_1\) denoting the modified Bessel function of the second kind of order one, for all real \(y\),
\[
\mathbb P(Y\le y)=\bigl[2e^{-y/2}K_1(2e^{-y/2})\bigr]^2.
\]
Moreover its moment generating function and first two cumulants are
\[
\mathbb E e^{tY}=\frac{\Gamma(1-t)^3\Gamma(2-t)}{\Gamma(2-2t)}\quad(t<1),\qquad
\mathbb EY=2\gamma+1,\quad \operatorname{Var}(Y)=3,
\]
where \(\gamma\) is Euler's constant. In particular,
\[
\lim_{m\to\infty}\left[\frac{\mu_d a_m}{2}\mathbb E W_{m,m}-2a_m^2\right]=2\gamma+1,
\qquad
\lim_{m\to\infty}\frac{d a_m^2}{4}\operatorname{Var}(W_{m,m})=3.
\]

## Assumptions and scope

The graph is precisely the complete bipartite graph \(K_{p,q}\), with all edge roots of equal Euclidean length \(\sqrt2\). The ambient metric is inherited from the standard Euclidean metric on the intrinsic sum-zero subspace, not a lattice-coordinate metric. Directions are Haar-uniform on its unit sphere. The finite moment identity holds for all \(p,q\ge2\) and all real \(r>0\); the explicit non-Gaussian limit and cumulant constants concern the balanced sequence \(p=q=m\to\infty\). No probabilistic randomness is imposed on the polytope itself.

## Proof

**(1) Exact Gaussian support reduction.** Let \(G\) be a standard Gaussian vector in \(\mathbb R^{p+q}\), partitioned into samples \(X_1,\dots,X_p\) and \(Y_1,\dots,Y_q\). Write \(\overline G\) for its coordinate average, \(G_H=G-\overline G\mathbf1\), and \(R=\|G_H\|\). Orthogonal Gaussian projection gives \(R\sim\chi_d\) and \(U=G_H/R\) uniform on the intrinsic sphere, independent of \(R\). Every vertex is orthogonal to \(\mathbf1\). Hence, with \(S=h_{P_{p,q}}(G)\),
\[
S=\max_{i,j}|X_i-Y_j|
=\max\{\max_i X_i-\min_jY_j,\ \max_jY_j-\min_iX_i\}
=\frac R2 W_{p,q}.
\]
Here the last equality uses central symmetry and positive homogeneity of support functions.

**(2) Exact finite moments.** Condition on \(L=\min_i X_i=\ell\) and \(M=\max_i X_i=u\). Their joint density is
\[
p(p-1)\phi(\ell)\phi(u)[\Phi(u)-\Phi(\ell)]^{p-2}\mathbf1_{\ell<u}.
\]
The event \(S\le t\) is exactly that every \(Y_j\) lies in \([u-t,\ell+t]\); the interval is nonempty precisely if \(u-\ell\le2t\). Conditional probability is \([\Phi(\ell+t)-\Phi(u-t)]^q\). Integrating proves \(\mathbb P(S\le t)=F_{p,q}(t)\). The survival-integral formula gives \(\mathbb ES^r=r\int_0^\infty t^{r-1}(1-F_{p,q}(t))dt\). Since \(R\) and \(U\) are independent and \(\mathbb ER^r=2^{r/2}\Gamma((d+r)/2)/\Gamma(d/2)\), the stated formula follows. The support of a vertex has norm \(\sqrt2\), giving the compact width bound and hence moment determinacy.

**(3) Four asymptotically independent extremes.** For balanced parts, the four quantities
\[
a_m(\max_iX_i-a_m),\quad a_m(-\min_iX_i-a_m),\quad
a_m(\max_jY_j-a_m),\quad a_m(-\min_jY_j-a_m)
\]
converge jointly to four independent standard Gumbel variables. Indeed, for each Gaussian sample, the joint upper/lower extreme probability equals
\[
[1-\overline\Phi(a_m+s/a_m)-\overline\Phi(a_m+t/a_m)]^m
\longrightarrow\exp(-e^{-s}-e^{-t}),
\]
by the normal tail-ratio limit; the two samples are independent. Therefore
\[
a_m(S-2a_m)\ \xrightarrow{d}\ \max\{G_1+G_2,\ G_3+G_4\}.
\]
The standard Gumbel representation \(G_j\stackrel d=-\log E_j\) identifies this limit with \(Y\).

**(4) Removing the Gaussian radius; moments.** The normalized directional statistic differs from \(a_m(S-2a_m)\) by
\[
a_mS\left(\frac{\sqrt d}{R}-1\right).
\]
Gaussian tail-ratio bounds show that the centered, \(a_m\)-scaled upper and lower extrema have bounded fourth moments uniformly in sufficiently large \(m\): their positive tails are bounded exponentially, their negative tails by \(\exp[-\exp(t/2)]\) up to \(t=a_m^2\), and by a Gaussian bound thereafter. In particular \(\mathbb E[(a_mS)^4]=O(a_m^8)\). Chi-square inverse-moment formulas give \(\mathbb E(\sqrt d/R-1)^4=O(d^{-2})\). Cauchy–Schwarz therefore bounds the squared error by \(O(a_m^4/d)=o(1)\), since \(a_m^2=O(\log m)\). This establishes convergence of the first two moments alongside distributional convergence.

**(5) Limit CDF and all cumulants.** Put \(T=E_1E_2\) and \(Z=\min(E_1E_2,E_3E_4)\). The product-exponential survival function is
\[
\mathbb P(T>z)=\int_0^\infty e^{-x-z/x}\,dx=2\sqrt z\,K_1(2\sqrt z),\quad z>0.
\]
The two products are independent, hence \(\mathbb P(Y\le y)=\mathbb P(Z\ge e^{-y})=[\mathbb P(T>e^{-y})]^2\). For real \(s>0\), Tonelli's theorem and the change of variables \(x=uv\), \(y=(1-u)v\) give
\[
\begin{aligned}
\mathbb EZ^s
&=s\int_0^\infty z^{s-1}\left[\int_0^\infty e^{-x-z/x}\,dx\right]^2dz\\
&=\Gamma(s+1)\Gamma(s+2)\,B(s+1,s+1)\\
&=\frac{\Gamma(s+1)^3\Gamma(s+2)}{\Gamma(2s+2)}.
\end{aligned}
\]
Both sides extend analytically to \(s>-1\): negative moments exist because \(Z^s\le (E_1E_2)^s+(E_3E_4)^s\) when \(-1<s<0\). Substitution \(s=-t\) gives the displayed moment generating function for \(t<1\). Differentiating its logarithm at zero yields \(2\gamma+1\) and \(3\), using \(\psi(2)=\psi(1)+1\) and \(\psi_1(2)=\psi_1(1)-1\). The MGF diverges as \(t\uparrow1\), so the limit cannot be Gaussian. Finally, \(\mathbb ES=\mu_d\mathbb EW_{m,m}/2\) and the first-two-moment convergence prove the sharp mean/variance statements.

## Verification

The standalone `check_width.py` independently tests the support maximum over all signed edge roots against the two-sample extreme reduction, validates the exact Gaussian-support CDF integral for small part sizes against seeded samples, and checks the product-exponential representation, gamma-moment formula, limiting CDF, and first two cumulants. It also checks the slowly converging finite-dimensional normalization at two large sample sizes. Execute `python check_width.py` with NumPy and SciPy installed; it prints `COMPLETE_BIPARTITE_SYMMETRIC_EDGE_WIDTH_CHECKS_PASSED` upon successful completion. The analytic proof, not simulation, supplies the all-dimensional and limiting assertions.

## Relationship to prior work

Higashitani, Jochemko and Michałek (first public arXiv version 2018-07-20) give facet, arithmetic, and Ehrhart results for the same complete-bipartite symmetric edge polytopes. D'Alì, Delucchi and Michałek (2019 preprint; 2022 journal) study faces and connections to adjacency and Kantorovich–Rubinstein polytopes. Chen, Davis and Korchevskaia (2021 preprint) study facet/face subgraphs. D'Alì, Juhnke-Kubitzke and Koch (2023) develop matroidal generalizations. Their relevant inspected statements do not yield the exact intrinsic Euclidean directional-width moments or the Bessel-square fluctuation law. In particular, unimodular equivalences do not preserve Euclidean widths. The Gaussian-extremes and Bessel-product methods are classical ingredients, but the polytope-specific combination and explicit cumulant law were not located in the inspected sources.

## Limitations

The full moment formulas involve normal integrals rather than elementary closed forms, and the sharp limit with explicit gamma MGF is established only for balanced complete bipartite graphs. No rate of convergence, general unequal-part asymptotic, different root lengths, or other graph family is claimed. Historical novelty remains provisional pending independent domain-specialist review, especially literature under the equivalent two-sample cross-range statistic. No independent audit has been performed.

## References

1. A. Higashitani, K. Jochemko and M. Michałek, *Arithmetic aspects of symmetric edge polytopes*, arXiv:1807.07678, first public 2018-07-20; published in *Mathematika* 65 (2019), 763–784. https://arxiv.org/abs/1807.07678
2. A. D'Alì, E. Delucchi and M. Michałek, *Many faces of symmetric edge polytopes*, arXiv:1910.05193, first public 2019-10-11; *Electronic Journal of Combinatorics* 29(3) (2022), #P3.24. https://doi.org/10.37236/10387
3. T. Chen, R. Davis and E. Korchevskaia, *Facets and facet subgraphs of symmetric edge polytopes*, arXiv:2107.12315, first public 2021-07-26. https://arxiv.org/abs/2107.12315
4. A. D'Alì, M. Juhnke-Kubitzke and M. Koch, *On a generalization of symmetric edge polytopes to regular matroids*, arXiv:2307.04933, first public 2023-07-10. https://arxiv.org/abs/2307.04933
