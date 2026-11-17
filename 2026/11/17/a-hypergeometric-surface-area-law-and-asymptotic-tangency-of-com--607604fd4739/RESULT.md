# A hypergeometric surface-area law and asymptotic tangency of complete type-A root polytopes

## Finding

For every integer \(n\ge3\), let \(H_n=\{x\in\mathbb R^n:\sum_i x_i=0\}\), equipped with the Euclidean metric induced from \(\mathbb R^n\), and let
\[
Q_n=\operatorname{conv}\{e_i-e_j:1\le i\ne j\le n\}\subset H_n.
\]
Write \(d=n-1\), \(V_n=\operatorname{Vol}_d(Q_n)\), \(A_n=\operatorname{Vol}_{d-1}(\partial Q_n)\), and \(r_n\) for its Euclidean inradius. A facet is indexed by a nonempty proper subset \(S\subset[n]\), with \(s=|S|\), and has intrinsic area
\[
\boxed{a_{n,s}=\frac{\sqrt{s(n-s)}}{(s-1)!(n-s-1)!}.}
\]
Consequently, if a facet is sampled with probability proportional to its intrinsic Euclidean area and \(K_n\) denotes the size of its indexing subset, then for \(1\le s\le n-1\),
\[
\boxed{\mathbb P(K_n=s)=\frac{\binom ns^2[s(n-s)]^{3/2}}{\sum_{j=1}^{n-1}\binom nj^2[j(n-j)]^{3/2}}.}
\]
Let \(X_n\) have the hypergeometric law \(\mathbb P(X_n=s)=\binom ns^2/\binom{2n}{n}\) for \(0\le s\le n\). The total variation distance between the laws of \(K_n\) and \(X_n\) satisfies the explicit bound
\[
\boxed{d_{\mathrm{TV}}(K_n,X_n)\le\frac3{4n-5}.}
\]
Thus
\[
\boxed{\frac{K_n-n/2}{\sqrt{n/8}}\xrightarrow{\mathrm d}N(0,1).}
\]
By contrast, a uniformly chosen facet has an asymptotically binomial cut-size law with variance \(n/4\): area sampling halves the limiting cut-size variance on the scale of \(n\).

The complete intrinsic surface area and volume satisfy
\[
\boxed{A_n=\frac1{n!}\sum_{s=1}^{n-1}\binom ns^2[s(n-s)]^{3/2},\qquad
V_n=\frac{\sqrt n}{(n-1)!}\binom{2n-2}{n-1}.}
\]
In particular, as \(n\to\infty\),
\[
\boxed{A_n=\frac{n^3}{8n!}\binom{2n}{n}\left(1-\frac3{4n}+O(n^{-2})\right),\qquad
\frac{A_n}{V_n}=\frac{n^{3/2}}2\left(1-\frac5{4n}+O(n^{-2})\right).}
\]
The origin is an incenter, with \(r_n=\sqrt{n/\lfloor n^2/4\rfloor}\), and the exact first-order deficit from being a tangential polytope is
\[
\boxed{\frac{r_n A_n}{(n-1)V_n}=1-\frac1{4n}+O(n^{-2}).}
\]
This means that although most individual facets do not touch the largest centered insphere, their area-weighted supporting distances approach the inradius with the quantified deficit shown above.

## Assumptions and scope

All measures are intrinsic Hausdorff measures in \(H_n\), not lattice-normalized volumes or volumes after deleting an ambient coordinate. All \(2^n-2\) facets are counted once. Area sampling chooses a facet with weight equal to its positive \((n-2)\)-dimensional Euclidean measure; it is not uniform sampling among facets and not Gaussian sampling of supporting directions. Total variation uses the usual half-\(\ell_1\) convention. The limit and error terms concern integers \(n\to\infty\) and hold for both parities.

## Proof

**Facet classification and Euclidean measure.** In the hyperplane \(H_n\), every root satisfies \(\sum_{i\in S}x_i\le1\). Equality holds precisely at roots \(e_i-e_j\) with \(i\in S\), \(j\notin S\); its convex hull is \(\Delta_{S}-\Delta_{S^c}\), the orthogonal Cartesian product of the standard simplices on the disjoint supports. Its dimension is \((s-1)+(n-s-1)=n-2\), so it is a facet. Conversely, a supporting linear functional on the roots maximizes the difference between its largest and smallest coordinate. A facet requires the maximizing roots to span dimension \(n-2\), which forces exactly two distinct functional values; their level sets define a unique proper nonempty \(S\). This proves the complete classification without relying on a counting guess. The \((s-1)\)-volume of the simplex on \(s\) unit coordinate vectors is \(\sqrt{s}/(s-1)!\): its edge Gram matrix is \(I+\mathbf 1\mathbf 1^{\mathsf T}\), of determinant \(s\). Multiplying the orthogonal factor volumes gives \(a_{n,s}\).

There are \(\binom ns\) facets with subset size \(s\). Since \((s-1)!(n-s-1)!=s!(n-s)!/[s(n-s)]\), their aggregate area is \(\binom ns^2[s(n-s)]^{3/2}/n!\). This yields the finite area formula and the displayed law.

**Hypergeometric approximation and Gaussian limit.** The random variable \(X_n\) counts successes in a sample of size \(n\) from a population of \(2n\) with \(n\) successes. It has mean \(n/2\) and exact variance \(n^2/[4(2n-1)]\). Put \(Y_n=X_n-n/2\) and \(h_n(s)=(1-4(s-n/2)^2/n^2)^{3/2}\in[0,1]\). The area law is the hypergeometric law tilted by \(h_n\), normalized by \(\mu_n=\mathbb E h_n(X_n)\). The inequality \(1-(1-t)^{3/2}\le3t/2\) for \(0\le t\le1\) gives
\[
1-\mu_n\le\frac6{n^2}\mathbb E Y_n^2=\frac3{2(2n-1)}.
\]
Since \(\tfrac12\mathbb E|h_n/\mu_n-1|\le(1-\mu_n)/\mu_n\), this proves \(d_{\mathrm{TV}}\le3/(4n-5)\). The hypergeometric central limit theorem with variance \(n^2/[4(2n-1)]\sim n/8\) follows directly by applying Stirling's formula to \(\binom ns^2/\binom{2n}{n}\) uniformly in bounded standardized windows, together with standard hypergeometric tail tightness. Total-variation convergence transfers that limit to the area law. Since the tilt density is at most \(1/\mu_n=O(1)\) and the hypergeometric standardized variables have uniformly bounded fourth moments, their squared standardized values are uniformly integrable under both laws; hence their variance ratios also converge to the stated limits. A uniformly chosen facet has the law of \(\operatorname{Binomial}(n,1/2)\) conditioned on \(1\le s\le n-1\), which instead has limiting variance \(n/4\).

**Volume, asymptotics, and inradius.** The inward distance from zero to facet \(S\) is
\[
\rho_s=\frac1{\|\mathbf 1_S-(s/n)\mathbf1\|}=\sqrt{\frac n{s(n-s)}}.
\]
Coning all facets to zero partitions \(Q_n\) up to measure-zero boundaries. Therefore
\[
(n-1)V_n=\sum_{s=1}^{n-1}\binom ns\rho_s a_{n,s}
=\frac{\sqrt n}{(n-2)!}\sum_{s=1}^{n-1}\binom ns\binom{n-2}{s-1}
=\frac{\sqrt n}{(n-2)!}\binom{2n-2}{n-1},
\]
by Vandermonde's identity, proving the volume formula. Central symmetry and permutation invariance permit an inball centered at zero, hence \(r_n=\min_s\rho_s=\sqrt{n/\lfloor n^2/4\rfloor}\).

Writing \(u=4Y_n^2/n^2\), the uniform Taylor estimate \((1-u)^{3/2}=1-3u/2+O(u^2)\) on \([0,1]\) and \(\mathbb E Y_n^4=O(n^2)\) yield
\[
\mu_n=1-\frac6{n^2}\frac{n^2}{4(2n-1)}+O(n^{-2})
=1-\frac3{4n}+O(n^{-2}).
\]
The stated fourth-moment bound follows, for example, by expanding powers using the factorial-moment identity \(\mathbb E(X_n)_{j}=(n)_{j}^2/(2n)_{j}\) for \(0\le j\le4\), or from the subgaussian tail of sampling without replacement. Since \([s(n-s)]^{3/2}=(n^3/8)h_n(s)\), the surface-area expansion follows. Divide by the exact volume and use \(\binom{2n}{n}/\binom{2n-2}{n-1}=2(2n-1)/n\) to obtain the ratio expansion. Finally, \(r_n=2n^{-1/2}(1+O(n^{-2}))\), for both parities, which gives the displayed tangency-deficit expansion.

## Verification

Run `python checker.py` with Python 3, NumPy and SciPy installed. This standalone checker rebuilds the ambient root vertices, orthogonally projects to \(H_n\), and uses independent Qhull convex-hull volume calculations for \(n=3,4,5,6\). For each of the resulting \(6,14,30,62\) facets it also computes the Euclidean area directly from the facet's vertices in a numerical orthonormal affine basis. It checks the exact volume identity, all individual facet areas, and the boundary-cone volume relation. Additional integer hypergeometric checks cover \(n=3,4,5,7,10,30,70,120\), including the total-variation bound. These finite computations support, but do not replace, the all-dimensional proof. The expected ending token is `ROOT_SURFACE_PASS`.

## Relationship to prior work

Higashitani, Jochemko and Michałek (2018, §3.1, Corollary 3.3) explicitly identify the two-level subset labeling of facets of complete-graph symmetric edge polytopes; this classification is background, not a new assertion. D'Alì, Delucchi and Michałek (2019, §2 and §3) place these polytopes in the Kantorovich–Rubinstein/root-polytope setting and develop their volume and combinatorial theory. Chen, Davis and Korchevskaia (2021, §4) characterize facet subgraphs, but do not give the particular Euclidean facet-area weighting or its hypergeometric Gaussian law. The known volume formula is independently derived here and is not claimed as a new isolated fact. The contribution is the exact intrinsic surface-area distribution, quantitative hypergeometric approximation, variance-halving surface law, and sharp first-order tangency deficit in the fixed coordinate metric. Unlike a tree symmetric-edge polytope, the complete-graph root polytope has product-of-simplices facets, not crosspolytope simplices.

## Limitations

The result concerns only the complete-graph symmetric edge polytope in its standard root-coordinate embedding, not arbitrary graph root polytopes or arbitrary affine realizations. No quantitative Berry–Esseen constant is claimed for the Gaussian approximation itself; the explicit total-variation rate compares the facet law to the hypergeometric law. The first-order tangency statement does not assert that every facet approaches the insphere or that the polytope is exactly tangential in any finite dimension. The result has not undergone independent mathematical audit, and unidentified literature on classical root polytopes, metric entropy or surface measures could affect priority.

## References

1. A. Higashitani, K. Jochemko, M. Michałek, *Arithmetic aspects of symmetric edge polytopes*, arXiv:1807.07678, first public 2018-07-20; §3.1 (facet description). https://arxiv.org/abs/1807.07678
2. A. D'Alì, E. Delucchi, M. Michałek, *Many faces of symmetric edge polytopes*, arXiv:1910.05193, first public 2019-10-11; §§2–4 (combinatorics and volume). https://arxiv.org/abs/1910.05193
3. T. Chen, R. Davis, E. Korchevskaia, *Facets and facet subgraphs of symmetric edge polytopes*, arXiv:2107.12315, first public 2021-07-26; §4 (facet subgraphs). https://arxiv.org/abs/2107.12315
4. *Exact inertia of complete-graph root polytopes and a sharp isotropic deficit*, published-finding corpus record `2026/10/25/SCOPE-exact-inertia-of-complete-graph-root-polytopes-and-a-sharp-isotr--cfc3c48a6fc4` (continuous interior covariance, not surface-area distribution).
5. *Facet-area Wiener identity and Brownian surface separation for tree root polytopes*, published-finding corpus record `2026/10/18/SCOPE-facet-area-wiener-identity-and-brownian-surface-separation-for-t--e112c873390a` (trees, not the complete graph).
