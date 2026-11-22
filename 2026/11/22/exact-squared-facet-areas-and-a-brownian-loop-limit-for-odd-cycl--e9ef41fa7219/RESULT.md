# Exact squared facet areas and a Brownian-loop limit for odd-cycle symmetric edge polytopes

## Finding
For each odd integer \(n\ge3\), let \(C_n\) be the cycle on vertices \(0,\ldots,n-1\), with indices modulo \(n\), and let the **canonical intrinsic Euclidean** symmetric-edge polytope be
\[
 P_n=\operatorname{conv}\{\pm(e_i-e_{i+1}):0\le i<n\}\subseteq H_n,
 \qquad H_n=\{x\in\mathbb R^n:\sum_i x_i=0\}.
\]
Every facet is an \((n-2)\)-simplex. There are exactly \(n\binom{n-1}{(n-1)/2}\) facets. Sample a facet \(F_n\) uniformly, and denote its intrinsic Euclidean \((n-2)\)-volume by \(A_n\). Then
\[
\boxed{\mathbb E A_n^2=\frac{n(n^2-1)}{12((n-2)!)^2}.}\tag{1}
\]
For the standard symmetric-edge polytope of an \(n\)-vertex **path**, a uniformly sampled facet has squared area with expectation \(n(n^2-1)/(6((n-2)!)^2)\). Thus **closing the path into an odd cycle halves the mean squared facet area exactly**, for every odd \(n\ge3\), despite changing the facet count and the polytope.

Furthermore, with \(B\) a standard Brownian bridge on \([0,1]\),
\[
\boxed{\left(\frac{(n-2)!A_n}{n^{3/2}}\right)^2
 \ \xrightarrow{\mathrm d}\
 Y:=\int_0^1\left(B(t)-\int_0^1 B(u)\,du\right)^2dt.}\tag{2}
\]
The limit is nondegenerate. In terms of independent standard Gaussian variables \(Z_k,Z_k'\), it has the explicit representation
\[
 Y\ \overset{\mathrm d}=\ \sum_{k=1}^{\infty}\frac{Z_k^2+(Z_k')^2}{4\pi^2k^2},
 \qquad
 \boxed{\mathbb E e^{-uY}=\frac{\sqrt{u/2}}{\sinh\sqrt{u/2}}\quad(u\ge0),}\tag{3}
\]
where the expression at \(u=0\) is interpreted by continuity; in particular \(\mathbb EY=1/12\) and \(\operatorname{Var}Y=1/360\). The distribution in (3), also known through the classical centered-bridge/Watson quadratic functional, is **not** claimed as a new probability law; its appearance as an exact limiting Euclidean facet-area law is the geometric contribution.

Let \(S(P)\) denote the sum of intrinsic Euclidean facet areas. As \(n\to\infty\) through odd values,
\[
\boxed{\frac{S(P_n)}{S(P_{\operatorname{Path}_n})}
 \sim \sqrt{\frac{2n}{\pi}}\frac{c_{\mathrm{cyc}}}{c_{\mathrm{path}}}
 =(0.5834883620\ldots)\sqrt n,}\tag{4}
\]
where \(c_{\mathrm{cyc}}=\mathbb E\sqrt Y\) has the convergent integral
\[
 c_{\mathrm{cyc}}=\frac{1}{\sqrt{2\pi}}\int_0^\infty
 \frac{1-z/\sinh z}{z^2}\,dz=0.276525716866\ldots,
\]
and \(c_{\mathrm{path}}=\mathbb E\sqrt{\int_0^1(W(t)-\int_0^1W(u)du)^2dt}=0.3781319637\ldots\) for standard Brownian motion \(W\). The path constant and its tree-polytope interpretation are established in the separately cited prior work; equation (4) is the new odd-cycle comparison.

## Assumptions and scope
All root vectors are literally the standard \(\pm(e_i-e_{i+1})\) in the zero-sum hyperplane equipped with the inherited ordinary Euclidean inner product. An arbitrary unimodular coordinate change need not preserve facet areas. Only **odd** simple cycle lengths \(n\ge3\) are covered; even cycles have different facet structure. Areas are facet volumes of dimension \(n-2\), not lattice-normalized volumes. Uniformity refers to choosing one of the actual facets with equal probability, not to choosing a random boundary point.

## Proof
**1. Complete facet parametrization.** By the facet-potential characterization of Higashitani–Jochemko–Michałek, a facet is defined by an integer vertex potential \(h\), modulo additive constants, whose differences across graph edges have absolute value at most one and whose *tight* edges (absolute difference one) connect all graph vertices. On an odd cycle, the tight set must omit at most one edge, since a connected spanning subgraph must have at least \(n-1\) edges. It cannot contain all \(n\) edges: their signed potential increments would be an odd number of \(\pm1\) values summing to zero. It therefore omits exactly one edge. By a cyclic relabeling, assume that this is \(\{n-1,0\}\). The \(m=n-1\) successive differences along the remaining path are signs \(s_1,\ldots,s_m\), and the missing-edge difference zero enforces \(\sum_{i=1}^m s_i=0\). Conversely every balanced sign word satisfies the cited spanning-tight-edge criterion, and defines a unique facet. The \(m\) signed edge roots on that path are affinely independent and constitute precisely the vertices of its simplex facet. There are \(\binom m{m/2}\) such facets for each of \(n\) possible omitted edges.

**2. Exact facet metric.** Put \(S_0=0\) and \(S_j=\sum_{i=1}^j s_i\) for \(1\le j\le m\); thus \(S_m=0\), and write \(\bar S=n^{-1}\sum_{j=0}^mS_j\). Up to a global sign convention, the centered supporting potential is \(h_j=S_j-\bar S\), with facet equation \(\langle h,x\rangle=1\). Its origin distance is \(\|h\|^{-1}\). Let \(T\) be the \(n\)-by-\(m\) incidence matrix for the path formed by deleting the missing cycle edge. Every maximal square minor of \(T\) is \(\pm1\), and Cauchy–Binet gives \(\det(T^{\mathsf T}T)=n\). The simplex with apex \(0\) and the \(m\) signed root vertices has Euclidean \((n-1)\)-volume \(\sqrt n/(n-1)!\). Writing the same volume as facet area times normal height divided by \(n-1\) yields
\[
\boxed{A_n=\frac{\sqrt n}{(n-2)!}
 \left(\sum_{j=0}^{m}(S_j-\bar S)^2\right)^{1/2}.}\tag{5}
\]
This formula is exact facet by facet, not merely in expectation.

**3. Exact bridge quadratic moment.** With independent uniform selection among balanced words, the signs are exchangeable, \(\mathbb E s_i=0\), \(\mathbb E s_i^2=1\), and \(\mathbb E s_is_j=-1/(m-1)\) for distinct indices. Therefore for \(0\le i\le j\le m\),
\[
 \mathbb ES_iS_j=\frac{i(m-j)}{m-1}.
\]
Summing the diagonal covariances, then the full covariance matrix, gives
\[
 \mathbb E\sum_{j=0}^{m} S_j^2=\frac{m(m+1)}6,
 \qquad
 \mathbb E\left(\sum_{j=0}^m S_j\right)^2=\frac{m^2(m+1)}{12}.
\]
Consequently
\[
 \mathbb E\sum_{j=0}^{m}(S_j-\bar S)^2
 =\frac{m(m+2)}{12}=\frac{n^2-1}{12}.
\]
Insert this into the square of (5) to prove (1). For comparison, with **unconditioned** path signs the same centered-potential computation gives \(\mathbb E\|h\|^2=(n^2-1)/6\), proving the asserted exact one-half ratio directly and agreeing with the previously established tree Wiener-index identity.

**4. Bridge functional limit.** The sign sequence is an equal-positive/equal-negative random permutation, i.e. a simple random-walk bridge of duration \(m\). The functional bridge invariance principle yields \(m^{-1/2}S_{\lfloor mt\rfloor}\Rightarrow B(t)\) in the space of continuous interpolations with uniform topology. Centering the discrete path and taking its Riemann-sum squared norm are continuous at continuous paths. Since \(m/n\to1\), equation (5) and the continuous mapping theorem imply (2). Moreover \(\mathbb E[( (n-2)!A_n/n^{3/2})^2]=(n^2-1)/(12n^2)\le1/12\), so the unsquared normalized areas are uniformly integrable and their expectations converge to \(c_{\mathrm{cyc}}\).

**5. Limit Laplace law.** The covariance kernel of the centered bridge \(B(t)-\int_0^1B\) is the periodic mean-zero Green kernel
\[
 K(s,t)=\frac12\left(|s-t|^2-|s-t|+\frac16\right).
\]
On \(L^2([0,1])\) its nonzero eigenvalues are \((4\pi^2k^2)^{-1}\), each with multiplicity two, with cosine/sine modes. The Karhunen–Loève expansion gives the series in (3). Using \(\mathbb Ee^{-cZ^2}=(1+2c)^{-1/2}\), Euler's product for \(\sinh\) gives the displayed Laplace transform. Summing the eigenvalues and their squares yields \(\mathbb EY=1/12\) and \(\operatorname{Var}Y=1/360\). Finally the standard nonnegative-variable fractional-moment integral applied to (3), followed by the substitution \(z=\sqrt{u/2}\), gives the stated integral for \(c_{\mathrm{cyc}}\).

**6. Surface comparison.** The odd-cycle count from step 1 and the path facet count \(2^{n-1}\), together with the common natural area scale \(n^{3/2}/(n-2)!\), show
\[
 \frac{S(P_n)}{S(P_{\operatorname{Path}_n})}
 =\frac{n\binom{n-1}{(n-1)/2}}{2^{n-1}}
 \frac{\mathbb E[(n-2)!A_n/n^{3/2}]}{\mathbb E[(n-2)!A_{\mathrm{path},n}/n^{3/2}]}.
\]
The central-binomial ratio is asymptotic to \(\sqrt{2n/\pi}\). The numerator mean tends to \(c_{\mathrm{cyc}}\) by step 4, and the denominator to the positive Brownian-motion constant \(c_{\mathrm{path}}\) by the tree/path theorem, completing (4).

## Verification
Run `python verify_odd_cycle.py` (Python 3 standard library). For every balanced bridge word of lengths \(2,4,6,8\), the program builds the **actual signed-root facet simplex** in \(\mathbb Z^n\), computes its Euclidean edge Gram determinant by fraction-free integer elimination, independently computes the right side of (5), and verifies exact equality. It then computes the exact empirical average of the squared facet areas and compares it to (1), with no floating-point tolerance. The cases \(n=3,5,7,9\) comprise \(98\) balanced words for a designated missing edge and, by cyclic symmetry, represent \(806\) facets altogether. The program prints `ODD_CYCLE_FACET_AREA_EXACT_PASS facets=806 n=3,5,7,9`.

Separately, a convex-hull computation with floating-point Gram checks was performed for \(n=3,5,7,9\) and agreed with facet counts and area distributions. The exact checker is the supplied reproducible certificate for the finite tests; neither finite enumeration nor numerical quadrature proves the all-dimensional statement, which is established in the preceding steps. The limiting decimal is a numerical evaluation of the convergent integral and does not enter the proof.

## Relationship to prior work
Higashitani, Jochemko and Michałek (2018, Theorem 3.1) supply the facet-potential description; D'Alì, Delucchi and Michałek (2019, Theorem 3.1) restate it and investigate arithmetic and combinatorial invariants; Chen, Davis and Korchevskaia (2021, Corollary 14) characterize when graph-root polytopes are simplicial. Their facet classification and counting input are credited. The prior result *Facet-area Wiener identity and Brownian surface separation for tree root polytopes* proves the squared-facet-area identity and centered-**Brownian-motion** limit for **trees**; the path half-factor comparator and its constant are not claimed as new here. The present result treats the linearly dependent roots of a **cycle**, proves the constrained **balanced-bridge** facet metric, extracts a distinct periodic Brownian-bridge limit, and obtains the path-versus-cycle comparison. The probability laws and invariance principle are classical tools, not newly invented distributions.

## Limitations
The result covers simple odd cycles only; no statement is made for even cycles, arbitrary cactus graphs or weighted edges. It does not establish the full finite-dimensional probability mass function of all facet areas, rates of weak convergence, or the extremal area among facets. The displayed decimal constants are approximate. Independent mathematical validation and exhaustive historical priority are not asserted; the proof and numerical checks should be independently reviewed before formal publication.

## References
1. A. Higashitani, K. Jochemko, M. Michałek, *Arithmetic aspects of symmetric edge polytopes*, arXiv:1807.07678v1, first public 2018-07-20, especially Theorem 3.1; https://arxiv.org/abs/1807.07678.
2. A. D'Alì, E. Delucchi, M. Michałek, *Many faces of symmetric edge polytopes*, arXiv:1910.05193v1, first public 2019-10-11, especially Theorem 3.1 and cycle discussion; https://arxiv.org/abs/1910.05193.
3. T. Chen, R. Davis, E. Korchevskaia, *Facets and facet subgraphs of symmetric edge polytopes*, arXiv:2107.12315v1, first public 2021-07-26; https://arxiv.org/abs/2107.12315.
4. *Facet-area Wiener identity and Brownian surface separation for tree root polytopes* (2026), publicly indexed mathematical result with complete proof; https://github.com/published-finding corpus/2026/blob/main/2026/10/18/SCOPE-facet-area-wiener-identity-and-brownian-surface-separation-for-t--e112c873390a/RESULT.md.
5. P. Billingsley, *Convergence of Probability Measures*, 2nd ed. (1999), for functional convergence principles; the spectral calculation for centered Brownian bridge is derived here.
