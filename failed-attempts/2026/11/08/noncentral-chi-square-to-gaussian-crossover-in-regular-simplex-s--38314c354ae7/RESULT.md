# Noncentral chi-square-to-Gaussian crossover in regular-simplex section face vectors

## Finding

Let \(n\ge4\), and take the regular Euclidean \((n-1)\)-simplex
\[
S_n=\operatorname{conv}\{e_1,\ldots,e_n\}
\subset \{x\in\mathbb R^n:\sum_i x_i=1\},
\qquad b_n=(1/n,\ldots,1/n).
\]
For each \(t\ge0\), let \(U\) be Haar-uniform on the Euclidean unit sphere of \(L_n=\{u:\sum_i u_i=0\}\), and define its random affine hyperplane section by
\[
Q_n(t)=S_n\cap\{x:\langle U,x-b_n\rangle=t\}.
\]
Write \(F_{n,j}(t)\) for the number of \(j\)-faces of \(Q_n(t)\), with \(F_{n,j}=0\) if the section is empty; for asymptotics \(j\) is fixed and \(0\le j\le n-3\). Set
\[
\phi(c)=\frac{e^{-c^2/2}}{\sqrt{2\pi}},\quad
p(c)=1-\Phi(c),\quad
v(c)=p(c)(1-p(c))-\phi(c)^2\left(1+\frac{c^2}{2}\right),
\]
\[
g_j(p)=\frac{1-p^{j+2}-(1-p)^{j+2}}{(j+2)!},\quad
B_{n,j}=\binom{n}{j+2}-\binom{\lfloor n/2\rfloor}{j+2}-\binom{\lceil n/2\rceil}{j+2}.
\]
In particular \(v(c)>0\) for every finite \(c\), and \(s^2=v(0)=1/4-1/(2\pi)>0\). The following is a single **offset-dependent face-vector fluctuation theorem**, with convergence joint over every fixed finite set of face ranks.

**Critical, distance \(1/n\).** If \(nt_n\to h\in[0,\infty)\), then, with one common Gaussian \(Z_0\sim N(0,s^2)\),
\[
\boxed{\left(\frac{B_{n,j}-F_{n,j}(t_n)}{n^{j+1}}\right)_{j=0}^{J}
\Longrightarrow
\left(\frac{(Z_0-h\phi(0))^2}{2^j j!}\right)_{j=0}^{J}.}
\tag{1}
\]
For \(h>0\) this is a rank-one **noncentral** chi-square law. Its \(h=0\) central specialization was previously established; the new assertion is the off-center crossover.

**Intermediate distances.** If \(nt_n\to\infty\) and \(\sqrt n\,t_n\to0\), put \(p_n=p(\sqrt n\,t_n)\). Then
\[
\boxed{\left(\frac{F_{n,j}(t_n)-n^{j+2}g_j(p_n)}{n^{j+2}t_n}\right)_{j=0}^{J}
\Longrightarrow
\left(\frac{2^{1-j}\phi(0)}{j!}Z_0\right)_{j=0}^{J}.}
\tag{2}
\]
This regime has joint Gaussian fluctuations, at a scale that varies continuously with the distance.

**Fixed scaled noncentral distances.** If \(t_n=c/\sqrt n\) for fixed \(c>0\), with one common \(Z_c\sim N(0,v(c))\), then
\[
\boxed{\left(\frac{F_{n,j}(t_n)-n^{j+2}g_j(p(c))}{n^{j+3/2}}\right)_{j=0}^{J}
\Longrightarrow
\left(\frac{(1-p(c))^{j+1}-p(c)^{j+1}}{(j+1)!}Z_c\right)_{j=0}^{J}.}
\tag{3}
\]
The positive coefficient in each rank is explicit. Thus \(t\asymp1/n\) is the sharp boundary between chi-square-type rank-one fluctuations and Gaussian rank-one fluctuations. For vertices, (1) reads
\[
\frac{n^2/4-F_{n,0}(h/n)}n\Longrightarrow(Z_0-h/\sqrt{2\pi})^2,
\]
whereas (3) has \(n^{3/2}\)-scale Gaussian deviations about \(n^2p(c)(1-p(c))\). Neither formula asserts a finite-dimensional continuous distribution: all face counts are integer-valued.

## Assumptions and scope

The simplex has side length \(\sqrt2\) and the distance \(t\) is the ordinary Euclidean distance from its centroid in its affine span. A positive \(t\) and Haar-uniform **oriented** \(U\) together induce the natural invariant law on unoriented hyperplanes at that fixed distance. Hyperplanes are not sampled from a translation-invariant Crofton measure. Empty sections are assigned zero face counts; their probability tends to zero in every stated regime. Genericity (the hyperplane contains no simplex vertex) holds almost surely at each deterministic \(t\). Joint limits concern fixed \(J\) with \(n\ge J+3\), not face dimensions growing with \(n\).

## Proof

**1. Exact face-vector reduction.** For a fixed generic normal \(u\), let \(K=\#\{i:u_i>t\}\). An original simplex face spanned by \(r\) vertices cuts the hyperplane in an \((r-2)\)-face precisely when its vertex set contains heights on both sides of \(t\). Every section face arises uniquely this way: a supporting face of a generic codimension-one simplex section is its intersection with one supporting face of the ambient simplex. Counting mixed subsets gives, for all \(0\le j\le n-3\),
\[
F_{n,j}=\binom n{j+2}-\binom K{j+2}-\binom{n-K}{j+2}.\tag{4}
\]
This remains true for \(K\in\{0,n\}\) (both sides equal zero). Discrete convexity of \(k\mapsto\binom k{j+2}+\binom{n-k}{j+2}\) proves \(F_{n,j}\le B_{n,j}\) and identifies the balanced maximizers.

**2. Gaussian normalization and exact moving threshold.** Let \(G_1,\ldots,G_n\) be iid standard Gaussians, and set \(\bar G=n^{-1}\sum_iG_i\) and \(s_n^2=n^{-1}\sum_i(G_i-\bar G)^2\). Orthogonal projection of \((G_i)\) onto \(L_n\), followed by normalization, has the required Haar law. Since \(\|(G_i-\bar G)_i\|=\sqrt n\,s_n\), the exact law of \(K\) is
\[
K_n(t)=\sum_{i=1}^n\mathbf1\{G_i>\bar G+\sqrt n\,t s_n\}.\tag{5}
\]
In particular the threshold uses the sample standard deviation, not an independent normalizer; ignoring it would give the wrong fixed-\(c\) variance.

**3. Moving-threshold central limit lemma.** Suppose a deterministic sequence \(c_n\to c\in\mathbb R\), and write \(p_n=p(c_n)\), \(K_n=K_n(c_n/\sqrt n)\). Then
\[
\sqrt n\left(\frac{K_n}{n}-p_n\right)
=\frac1{\sqrt n}\sum_{i=1}^n\psi_{c_n}(G_i)+o_{\mathbb P}(1),\tag{6}
\]
where
\[
\psi_c(z)=\mathbf1\{z>c\}-p(c)
-\phi(c)z-\frac{c\phi(c)}2(z^2-1).
\]
To justify the random threshold, first \(\bar G=O_{\mathbb P}(n^{-1/2})\) and \(s_n-1=(2n)^{-1}\sum_i(G_i^2-1)+o_{\mathbb P}(n^{-1/2})\). For \(F_n\), the Gaussian empirical cdf, the centered increments \(\sqrt n[(F_n(c_n+\delta)-F_n(c_n))-(\Phi(c_n+\delta)-\Phi(c_n))]\) converge to zero uniformly on \(|\delta|\le C/\sqrt n\). An elementary proof grids that interval with mesh \(n^{-3/4}\): there are \(O(n^{1/4})\) grid points, each count over an interval of length \(O(n^{-1/2})\) has variance \(O(\sqrt n)\), and Chebyshev plus union bound makes all centered grid increments \(o_{\mathbb P}(\sqrt n)\). Counts in individual grid cells have mean \(O(n^{1/4})\); a binomial Chernoff bound makes their maximum \(o_{\mathbb P}(\sqrt n)\). Finally let \(C\) increase. Taylor expansion of \(\Phi\) at \(c_n\) proves (6). All constants here are uniform on bounded ranges of \(c_n\).

The iid triangular-row summands have mean zero, uniformly bounded moments, and variance
\[
\operatorname{Var}\psi_c(G)=p(c)(1-p(c))-\phi(c)^2(1+c^2/2)=v(c).\tag{7}
\]
Indeed \(\mathbb E[G\mathbf1\{G>c\}]=\phi(c)\), \(\mathbb E[(G^2-1)\mathbf1\{G>c\}]=c\phi(c)\), and \(\mathbb E(G^2-1)^2=2\). The variance is strictly positive because a step indicator is not almost surely a polynomial of degree two. The triangular-array Lindeberg theorem gives \(\sqrt n(K_n/n-p_n)\Rightarrow Z_c\sim N(0,v(c))\).

**4. Critical noncentral chi-square limit.** When \(nt_n\to h\), set \(c_n=\sqrt n\,t_n\). Then \(c_n\to0\), and
\[
\frac{K_n(t_n)-n/2}{\sqrt n}
=\sqrt n\left(\frac{K_n}{n}-p(c_n)\right)
+\sqrt n\,[p(c_n)-1/2]\Longrightarrow Z_0-h\phi(0).\tag{8}
\]
For any fixed \(j\), Taylor expansion of the polynomial in (4) at the balanced split gives, uniformly whenever \(|K_n-n/2|=O(\sqrt n)\),
\[
\frac{B_{n,j}-F_{n,j}}{n^{j+1}}
=\frac1{2^j j!}\left(\frac{K_n-n/2}{\sqrt n}\right)^2+o(1).\tag{9}
\]
The possible half-integer center changes the numerator by only \(O(n^j)\). Joint continuous mapping of (8) and (9) proves (1).

**5. Intermediate and fixed-scaled Gaussian limits.** For fixed \(j\), the binomial polynomial identity (4), uniformly in \(K\in\{0,\ldots,n\}\), implies
\[
F_{n,j}=n^{j+2}g_j(K_n/n)+O_j(n^{j+1}).\tag{10}
\]
The derivatives are
\[
g_j'(p)=\frac{(1-p)^{j+1}-p^{j+1}}{(j+1)!},\qquad
g_j''(1/2)=-\frac{2^{1-j}}{j!}.\tag{11}
\]
For \(c_n=c>0\), Taylor expansion around \(p(c)\), (6), and the fact that the error in (10) is \(o(n^{j+3/2})\) give (3).

For \(nt_n\to\infty\), \(\sqrt n t_n\to0\), expand at \(p_n=p(\sqrt n t_n)=1/2-\phi(0)\sqrt n t_n+O((\sqrt n t_n)^3)\). Then
\[
g_j'(p_n)=\frac{2^{1-j}\phi(0)}{j!}\sqrt n t_n+o(\sqrt n t_n).\tag{12}
\]
Multiplying (6) by the derivative and scaling by \(n^{j+2}t_n\) proves (2). The quadratic Taylor remainder is \(O_{\mathbb P}(n^{j+1})\), negligible because \(nt_n\to\infty\); the deterministic error in (10) is negligible for the same reason. This completes all three regimes.

## Verification

`verify.py` implements the exact face-count formula with Python's standard library, exhaustively enumerates all \(2^n\) sign assignments for \(4\le n\le8\) and all eligible face ranks, and compares combinatorial face counts directly with mixed-subset enumeration. It independently generates Haar directions by normalizing centered Gaussian samples, then numerically compares the critical-offset imbalance mean/variance and the fixed-scaled-offset variance with (7). It checks the quadratic expansion of each fixed face rank through rank four. Successful execution prints `ALL_NONCENTRAL_SIMPLEX_SECTION_CHECKS_PASSED`. The numerical tests corroborate finite identities and limiting constants; neither simulation nor finite enumeration is an infinite-dimensional convergence proof.

## Relationship to prior work

König's *Non-central sections of the regular n-simplex* (first public version December 3, 2023) studies extremal **section volumes** at prescribed distance, not the random face-vector distribution; its Euclidean normalization is used here. Brandenburg–De Loera–Meroni provide slicing chambers and algorithms for optimizing face counts over affine sections, not Haar orientation fluctuations. De Loera–Lopez-Campos–Torres describe attainable counts and maximal section vertex counts, not their invariant-probability laws. The published results *Exact mean and chi-square fluctuations of Haar central simplex-section vertex counts* and *Joint chi-square face-vector fluctuations of random central regular-simplex sections* already establish the \(t=0\) phenomenon, including all fixed ranks; that central case is **prior art**, not the present novelty. The present theorem determines the positive-offset \(t\asymp1/n\) noncentral law and the transition through intermediate offsets to fixed \(t\asymp1/\sqrt n\) Gaussian laws, with an explicit studentized-threshold variance correction. The probability arguments draw on classical Gaussian empirical-process asymptotics and do not claim their general invention.

## Limitations

Only side-length-\(\sqrt2\) regular simplices with Haar-oriented fixed-offset hyperplanes are covered, for face ranks fixed as dimension increases. The theorem does not describe random offset laws, arbitrary nonregular simplices, or proportional-to-dimension face ranks. It provides weak convergence rather than total-variation bounds or quantitative rates. Published central-section formulas and generic empirical-process central limit theorems are not claimed as new. Independent historical and mathematical audit remains outstanding; an unindexed equivalent in older noncentral-section or empirical-process literature cannot be excluded.

## References

1. H. König, *Non-central sections of the regular n-simplex*, arXiv:2312.01325 (first submitted December 3, 2023), https://arxiv.org/abs/2312.01325 .
2. M.-C. Brandenburg, J. A. De Loera and C. Meroni, *The Best Ways to Slice a Polytope*, arXiv:2304.14239 (first submitted April 27, 2023), https://arxiv.org/abs/2304.14239 .
3. J. A. De Loera, G. Lopez-Campos and A. J. Torres, *On the Number of Vertices in a Hyperplane Section of a Polytope*, arXiv:2412.12419 (first submitted December 17, 2024), https://arxiv.org/abs/2412.12419 .
4. *Joint chi-square face-vector fluctuations of random central regular-simplex sections*, publicly available research note (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-joint-chi-square-face-vector-fluctuations-of-random-central-regu--aa90c887fe90 .
5. *Exact mean and chi-square fluctuations of Haar central simplex-section vertex counts*, publicly available research note (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-mean-and-chi-square-fluctuations-of-haar-central-simplex-s--d3f9b0447a8e .
6. H. Dirksen, *Sections of the regular simplex—Volume formulas and estimates*, arXiv:1509.06408 (first submitted September 21, 2015), https://arxiv.org/abs/1509.06408 .
