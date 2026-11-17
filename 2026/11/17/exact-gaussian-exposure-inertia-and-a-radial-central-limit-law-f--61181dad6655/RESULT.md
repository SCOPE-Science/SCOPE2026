# Exact Gaussian-exposure inertia and a radial central limit law for path 2-graph polytopes

## Finding
For every integer \(n\ge5\), let \(\Delta_I=\operatorname{conv}\{e_i:i\in I\}\subset\mathbb R^n\) and let
\[
P_n=\sum_{j=1}^{n-1}\Delta_{\{j,j+1\}}+\sum_{j=1}^{n-2}\Delta_{\{j,j+1,j+2\}}.
\]
This is the path 2-graph polytope, up to its immaterial singleton-simplex translation. Let \(G\) be a standard Gaussian vector in \(\mathbb R^n\) and let \(X_n\) be the almost surely unique vertex maximizing \(\langle G,x\rangle\) over \(P_n\). Put \(\mu_n=\mathbb EX_n\). Then the Euclidean Gaussian-exposure inertia has the **exact finite-dimensional value**
\[
\mathbb E\|X_n-\mu_n\|_2^2=\frac{56}{15}n-\frac{739}{90}.
\]
For independent copies \(X_n,X_n'\), the expected squared separation is exactly
\[
\mathbb E\|X_n-X_n'\|_2^2=\frac{112}{15}n-\frac{739}{45}.
\]
There is also a nondegenerate **radial central limit law**:
\[
\frac{\|X_n-\mu_n\|_2^2-\bigl(56n/15-739/90\bigr)}{\sqrt n}
\ \xrightarrow{\mathrm d}\ \mathcal N\!\left(0,\frac{4352}{1575}\right).
\]
For two interior coordinates \(i,i+k\in\{3,\ldots,n-2\}\), the exact covariance of the exposed vertex is zero when \(k\ge5\), and for \(0\le k\le4\) is, in order,
\[
\left(\frac{56}{15},-\frac{173}{90},-\frac3{20},\frac{11}{60},\frac1{45}\right).
\]
Thus near-neighbor coordinates are negatively correlated but separation three and four produces strictly positive correlation. These are statements about **Gaussian-normal-cone-weighted vertex exposure**, not uniform counting of vertices or uniform interior volume.

## Assumptions and scope
The ambient metric is the ordinary Euclidean metric on \(\mathbb R^n\). The affine hull of \(P_n\) has coordinate sum \(2n-3\); isotropy of the Gaussian implies that its projected direction in the affine-hull translation space is Haar-uniform on the corresponding sphere. The original 2-graph-polytope convention includes every singleton simplex \(\Delta_{\{i\}}\), whose Minkowski sum translates \(P_n\) by the all-ones vector and changes none of the centered quantities above.

Coordinates are indexed from 1 to \(n\). In the displayed interval sums, each interval has length exactly two or exactly three. The random direction has independent standard normal components, so all comparison orders are equiprobable and ties have probability zero.

The mean vector is explicit:
\[
\mu_n=\left(\frac56,\frac53,\underbrace{2,\ldots,2}_{n-4\text{ coordinates}},\frac53,\frac56\right).
\]
The centering in the central limit law is the exact expected squared radius, not a circumradius or a uniform-volume second moment.

## Proof
**1. Exposure reduces to five-site rank statistics.** A linear functional on a Minkowski sum of coordinate simplices is maximized by choosing the largest coordinate of the direction on each summand. Thus, almost surely,
\[
(X_n)_i=\sum_{\ell=2}^3\sum_{\substack{1\le j\le n-\ell+1\\j\le i<j+\ell}}
\mathbf1\!\left\{G_i=\max_{j\le a<j+\ell}G_a\right\}.
\]
In the bulk, the contributing intervals relative to position 0 are precisely
\[
\{-1,0\},\ \{0,1\},\ \{-2,-1,0\},\ \{-1,0,1\},\ \{0,1,2\}.
\]
Consequently a bulk coordinate depends on five consecutive independent continuous random labels. Since the probability of winning an interval of length \(\ell\) is \(1/\ell\), the two edge terms and three triple terms have mean \(2/2+3/3=2\). At either endpoint the mean is \(1/2+1/3=5/6\); one step from either endpoint it is \(2/2+2/3=5/3\). This proves the stated mean vector.

**2. Exact finite local enumeration.** Write \(V_i\) for the five-site stationary bulk winner count on a bi-infinite sequence of independent continuous labels, and set \(R_i=(V_i-2)^2\). A joint pair \((V_0,V_k)\), \(0\le k\le4\), depends on exactly \(5+k\) labels. Each of their \((5+k)!\) strict relative orders has probability \(1/(5+k)!\). For each order \(\pi\), put
\[
L_i(\pi)=\sum_{A\in\mathcal W_i}\mathbf1\{\pi_i>\pi_j\text{ for every }j\in A\setminus\{i\}\},
\quad \mathcal W_i=\{i+W:W\in\mathcal W_0\},
\]
where \(\mathcal W_0\) is the five-interval family written above. Summing \(L_0L_k\) and \((L_0-2)^2(L_k-2)^2\) over all orders yields the following **exact finite identities**. The standalone verifier reconstructs every one of these sums using integer arithmetic before reducing rational fractions.

| \(k\) | \((5+k)!\) | \(\operatorname{Cov}(V_0,V_k)\) | \(\operatorname{Cov}(R_0,R_k)\) |
|---|---:|---:|---:|
| 0 | 120 | \(56/15\) | \(2114/225\) |
| 1 | 720 | \(-173/90\) | \(-187/75\) |
| 2 | 5040 | \(-3/20\) | \(-8173/6300\) |
| 3 | 40320 | \(11/60\) | \(2147/6300\) |
| 4 | 362880 | \(1/45\) | \(421/3150\) |

The summands are explicit indicator polynomials in a finite total ordering; checking all of the finitely many orderings is exhaustive, not an extrapolation from small polytope dimensions. For \(k\ge5\) the underlying five-site windows are disjoint, hence both covariances vanish. Direct exact enumeration of the endpoint windows similarly gives the single-site variances \(29/36\) at positions 1 and \(n\), \(23/9\) at positions 2 and \(n-1\), and \(56/15\) in the bulk. In particular,
\[
\mathbb E\|X_n-\mu_n\|_2^2=(n-4)\frac{56}{15}+2\left(\frac{29}{36}+\frac{23}{9}\right)
=\frac{56}{15}n-\frac{739}{90}.
\]
The independent-pair identity follows by expanding \(\|X_n-X_n'\|_2^2\), using identical means and independence.

**3. Limit law and its exact variance.** Set \(S_n=\|X_n-\mu_n\|_2^2\). Apart from four endpoint terms, \(S_n\) is the sum of the stationary bounded sequence \(R_i\) above. It is four-dependent. Its bulk long-run variance is, by the exact local table,
\[
\sigma^2=\operatorname{Var}(R_0)+2\sum_{k=1}^4\operatorname{Cov}(R_0,R_k)=\frac{4352}{1575}>0.
\]
To justify the normal limit without relying on simulations, split the bulk sequence into blocks of length \(\lfloor n^{1/3}\rfloor\), separated by four omitted indices. The retained block sums are independent; their centered absolute values are bounded by a constant times \(n^{1/3}=o(\sqrt n)\). Their total variance is \(\sigma^2n+o(n)\), so the elementary Lindeberg central limit theorem applies. The omitted terms have variance \(O(n^{2/3})=o(n)\), because the sequence is bounded and four-dependent; the endpoint terms have bounded variance. Restoring these terms does not affect the limit. The exact finite-sample expectation already calculated provides the stated centering.

## Verification
Run `python3 verify_path2.py` with Python 3 standard library only. It exhaustively checks the \(409080\) possible relative orders for local windows of sizes 5 through 9, the exact covariance and quadratic-covariance tables, and the first- and second-moment identities for every direction-order permutation at \(n=5,6,7,8\). The latter covers \(46200\) global permutations. The local rank enumeration proves the rational finite identities because it covers **every** possible ordering of the finitely many labels involved. The passage from the local identities to arbitrary \(n\) and to the central limit follows from the analytical steps above; finite experiments alone are not being used to establish an infinite theorem.

Expected terminal message: `PATH2_GAUSSIAN_EXPOSURE_PASS local_rank_orders=409080 global_rank_orders=46200 sigma2=4352/1575`.

## Relationship to prior work
Pešović and Stojadinović define the \(m\)-graph polytopes and analyze their face enumerators, normal fans and poset models. The family here is their first non-zonotopal stage for paths, \(m=2\), after removing a common translation. Pešović's earlier treatment of hypergraphic polytopes develops integer-point enumerators and face-polynomial information. Neither work, in the inspected relevant text, gives an exact Gaussian-exposure covariance, Euclidean expected squared separation, or a radial limit law for this family. Results on Poisson extreme directional widths for full interval-simplex associahedra concern a different summand range and a different functional of the exposed geometry; they do not imply these local quadratic-rank moments. The standard four-dependent blocking argument alone does not determine the geometric rational constants or their nondegeneracy.

## Limitations
The conclusions use isotropic random directions, **not** uniform vertex selection, and apply to the canonical unit-summand Euclidean realization, not arbitrary affinely equivalent or weighted realizations. The limit is for growing path length at fixed maximal simplex size three; it is not a result for the full graph-associahedron where interval sizes grow with dimension. Bibliographic priority remains provisional: absence from searched references cannot exclude an unindexed equivalent statement. No independent mathematical audit has been performed.

## References
1. M. Pešović and T. Stojadinović, *Between graphical zonotope and graph-associahedron*, arXiv:2209.12053, first public version September 24, 2022, especially Definition 2.1, Example 3.4, and §§3–4. https://arxiv.org/abs/2209.12053
2. M. Pešović, *Integer points enumerator of hypergraphic polytopes*, arXiv:1812.09770, first public version December 23, 2018, especially §§3–4. https://arxiv.org/abs/1812.09770
3. S. Forcey and M. Ronco, *Algebraic structures on graph associahedra*, Journal of the London Mathematical Society 106 (2022), 1189–1231, DOI:10.1112/jlms.12596. This supplies background on the combinatorial graph-associahedron setting, not a proof of the present metric formulas.
