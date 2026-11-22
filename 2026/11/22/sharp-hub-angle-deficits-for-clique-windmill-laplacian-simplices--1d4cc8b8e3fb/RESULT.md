# Sharp hub-angle deficits for clique-windmill Laplacian simplices

## Finding
Let \(r\ge1\) be fixed. For every integer \(m\ge2\), form the windmill \(W_{r,m}=K_1\vee(mK_r)\) from one hub and \(m\) disjoint \(r\)-cliques; \(r=1\) gives a star and \(r=2\) a friendship graph of triangles. Let \(L_{r,m}\) be its unweighted graph Laplacian. In the usual Euclidean zero-sum hyperplane \(H=\{x\in\mathbb R^{rm+1}:\sum_i x_i=0\}\), consider the full-dimensional Laplacian simplex
\[
P_{r,m}=\operatorname{conv}\{L_{r,m}e_i:0\le i\le rm\},
\]
where index \(0\) denotes the hub. Let \(p_{r,m}\) be the normalized spherical measure of its hub's outward normal cone, equivalently the probability that a Haar-uniform linear objective uniquely exposes the hub vertex. Then
\[
\boxed{\frac12-p_{r,m}\sim
\frac{\sqrt{r^2+r-1}}{\sqrt\pi}\frac{\sqrt{\log m}}{rm+1}},
\qquad m\to\infty\quad(r\text{ fixed}).
\]
All \(rm\) peripheral vertices are equivalent under graph automorphisms; each therefore has normal-cone probability \((1-p_{r,m})/(rm)\) **exactly**. Hence one hub retains asymptotic normal-cone mass \(1/2\) while the remaining half is spread among a diverging number of peripheral vertices.

This correction detects a natural graph modification at equal vertex count and unchanged hub degree. A star with \(2m\) leaves has the same hub and edges from the hub as the friendship graph with \(m\) triangles, but adding the \(m\) disjoint leaf-to-leaf edges gives
\[
\boxed{\lim_{m\to\infty}\frac{\frac12-p_{2,m}}{\frac12-p_{1,2m}}=\sqrt5}.
\]
The comparison is of the **first nonzero angular correction**, not of the limiting hub angles (which are both \(1/2\)).

## Assumptions and scope
All graphs are finite, connected, simple, undirected and unweighted. The ambient inner product is the standard Euclidean one on the zero-sum subspace; the probabilities are not preserved by arbitrary lattice-unimodular changes of coordinates. Fix \(r\) before taking \(m\to\infty\). No uniformity for growing clique size is claimed. The hub probability is less than \(1/2\) for each \(r\ge1\), \(m\ge2\). The Laplacian has rank \(rm\), so its \(rm+1\) columns are affinely independent in \(H\) and Gaussian exposure has no ties with positive probability.

## Proof
**Exact Gaussian representation.** Write \(d=rm\), \(n=d+1\). Let \(G_0\), and \(G_{b,j}\) for \(1\le b\le m\), \(1\le j\le r\), be independent standard normal variables. Maximizing a Gaussian linear functional against the Laplacian columns gives precisely the same exposed vertex as a Haar-uniform direction of \(H\), because orthogonal projection of the ambient Gaussian onto \(H\) leaves all inner products with these columns unchanged.

The hub and peripheral scores are
\[
X_0=dG_0-\sum_{b,j}G_{b,j},\qquad
X_{b,j}=(r+1)G_{b,j}-\sum_{k=1}^rG_{b,k}-G_0.
\]
Define the peripheral sample mean and centered coordinates
\[
\mu=\frac1d\sum_{b,j}G_{b,j},\qquad H_{b,j}=G_{b,j}-\mu,
\]
and the centered block maximum
\[
T_{r,m}=\max_{b,j}\left((r+1)H_{b,j}-\sum_{k=1}^rH_{b,k}\right).
\]
The array of peripheral coefficients sums to zero across all \(d\) indices; therefore \(T_{r,m}\ge0\), and it is positive almost surely when \(d\ge2\). Direct subtraction of support scores shows that the hub wins if and only if
\[
G_0-\mu>\frac{T_{r,m}}{n}.
\]
For a Gaussian vector, its mean is independent of its centered component, so \(G_0-\mu\) is independent of \(T_{r,m}\) and has law \(N(0,1+1/d)\). Writing \(\Phi\) for the standard normal distribution function gives the **finite-dimensional identity**
\[
p_{r,m}=\mathbb E\,\Phi\left(-\frac{T_{r,m}}{(rm+1)\sqrt{1+1/(rm)}}\right).\tag{1}
\]
This immediately gives \(0<p_{r,m}<1/2\) for all stated finite parameters.

**Sharp size of the competing maximum.** Before centering, define
\[
Z_{b,j}=(r+1)G_{b,j}-\sum_{k=1}^rG_{b,k}
=rG_{b,j}-\sum_{k\ne j}G_{b,k},\qquad
M_{r,m}=\max_{b,j}Z_{b,j}.
\]
Each \(Z_{b,j}\) is centered normal with variance
\[
\sigma_r^2=r^2+r-1,
\]
and vectors from distinct cliques are independent. Their dependence within each clique is harmless for the leading extreme-value scale. Indeed, the \(m\) variables \(Z_{b,1}\) are independent normals of variance \(\sigma_r^2\), so
\[
\sigma_r\,\mathbb E\max_{1\le b\le m}N_b
\le\mathbb E M_{r,m},
\]
where the \(N_b\) are independent standard normals. On the other hand, the normal exponential moment bound, which does not require independence, gives
\[
\mathbb E M_{r,m}
\le\inf_{\lambda>0}\frac{\log(rm)+\lambda^2\sigma_r^2/2}{\lambda}
=\sigma_r\sqrt{2\log(rm)}.
\]
The classical elementary maximum-normal estimate \(\mathbb E\max_{b\le m}N_b\sim\sqrt{2\log m}\) follows, for example, by a Gaussian union bound for the upper tail and the formula \(\Pr(\max_{b\le m}N_b\le t)=\Phi(t)^m\) together with Gaussian tail bounds for the lower tail. Since \(r\) is fixed, the two estimates squeeze
\[
\mathbb E M_{r,m}\sim\sigma_r\sqrt{2\log m}.\tag{2}
\]
But \(T_{r,m}=M_{r,m}-\mu\), and \(\mathbb E\mu=0\), so \(\mathbb E T_{r,m}=\mathbb E M_{r,m}\). A union bound on the \(rm\) Gaussian magnitudes and the normal moment bound for \(\mu\) also give
\[
\mathbb E T_{r,m}^3=O_r((\log m)^{3/2}).\tag{3}
\]

**Angular asymptotic.** For all nonnegative \(x\), Taylor's theorem and boundedness of the second derivative of the normal density yield
\[
\Phi(-x)=\frac12-\frac{x}{\sqrt{2\pi}}+O(x^3).
\]
Substitute \(x=T_{r,m}/(n\sqrt{1+1/d})\) in (1) and use (2)–(3):
\[
\frac12-p_{r,m}
=\frac{\mathbb E T_{r,m}}{\sqrt{2\pi}\,n\sqrt{1+1/d}}
+O_r\left(\frac{(\log m)^{3/2}}{n^3}\right)
\sim\frac{\sigma_r}{\sqrt\pi}\frac{\sqrt{\log m}}{rm+1}.
\]
There is one orbit of peripheral vertices under permutations of the cliques and permutations within each clique; their probabilities sum to \(1-p_{r,m}\), proving the exact peripheral formula. For the fixed-order comparison, evaluate \(\sigma_1=1\) at \((r,m)=(1,2m)\) and \(\sigma_2=\sqrt5\) at \((r,m)=(2,m)\). Both graph orders are \(2m+1\), and \(\sqrt{\log(2m)}/\sqrt{\log m}\to1\), proving the stated ratio.

## Verification
The standalone `verify.py` builds the Laplacian matrices directly and checks the Gaussian score identities, hub inequality and variance formula for \(480\) random vectors spanning \(40\) small parameter pairs. It independently compares the conditional probability identity with direct sampling of ambient Gaussian support scores for three parameter pairs; the discrepancies lie within conservative binomial tolerances. Finally, it reports Monte Carlo estimates of normalized hub-angle deficits for \(r=1,2,3\) and \(m=32,128,512,2048\), alongside the proved constants. Sampling only checks finite-dimensional consequences; it is **not** an infinite-dimensional proof of the asymptotic or originality.

To reproduce, run `OPENBLAS_NUM_THREADS=1 python verify.py` with Python, NumPy and SciPy; fixed random seeds are included. The printed terminal marker is `WINDMILL_LAPLACIAN_CONE_EXACT_PASS`.

## Relationship to prior work
Braun and Meyer introduced the graph Laplacian simplex and systematically studied lattice and Ehrhart properties of trees, cycles, and complete graphs. Balletti, Hibi, Meyer and Tsuchiya extended the construction to digraphs and proved general normalized-volume results. Neither paper's inspected geometric statements evaluate Gaussian normal-cone probabilities for the clique windmill.

A public 2026 note entitled *Cubic suppression of endpoint normal cones in path Laplacian simplices* derives the **leading** star-hub probability \(p_{1,m}\to1/2\), along with much sharper and different path endpoint estimates. Its full mathematical statement and proof give no first-order angular deficit for the star and no clique-windmill comparison. The present theorem supplies the sharp, graph-dependent deficit coefficient, and the \(\sqrt5\) change under a disjoint edge matching. Generic Gaussian-maxima estimates provide an essential tool but are not an evaluated Laplacian-simplex geometric claim.

## Limitations
The result requires fixed \(r\) and increasingly many cliques, and does not give a uniform error estimate when \(r\) grows with \(m\). Equation (1) is an exact expectation but generally not an elementary finite closed form. The normal-cone distribution may change under nonorthogonal affine maps. Although relevant published constructions and the closest indexed angular result were compared, an unindexed equivalent angular-asymptotic statement remains a historical-priority risk. No independent audit has been performed.

## References
1. Benjamin Braun and Marie Meyer, *Laplacian Simplices*, arXiv:1706.07085v1, first public 2017-06-21, Sections 1–6. https://arxiv.org/abs/1706.07085
2. Gabriele Balletti, Takayuki Hibi, Marie Meyer and Akiyoshi Tsuchiya, *Laplacian Simplices Associated to Digraphs*, arXiv:1710.00252v1, first public 2017-09-30, Sections 1–3. https://arxiv.org/abs/1710.00252
3. *Cubic suppression of endpoint normal cones in path Laplacian simplices*, publicly indexed research note, October 2026, for the established leading star-hub angle.
