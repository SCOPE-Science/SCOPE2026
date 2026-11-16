# An irredundant Walsh positivity polygon and exact singular-subset thresholds for quadratic Hamming heat kernels

## Finding
Fix an integer \(d\ge2\) and \(0<r<1\). On the binary Hamming cube \(G=\{-1,1\}^d\), set \(h(x,y)=\#\{j:x_j\ne y_j\}\) and consider the two-parameter real translation-invariant covariance family
\[
K_{a,b}(x,y)=r^{h(x,y)}\left[1+a h(x,y)+b\binom{h(x,y)}2\right],\qquad a,b\in\mathbb R.
\]
Write
\[
\alpha=\frac r{1+r},\qquad \beta=\frac r{1-r},\qquad
u_k=(d-k)\alpha-k\beta,
\]
\[
 v_k=\frac12\left[u_k^2-(d-k)\alpha^2-k\beta^2\right],
 \qquad Q_k(a,b)=1+a u_k+b v_k\quad(0\le k\le d).
\]
Then the *complete* positive-semidefiniteness region for all Gram matrices is the compact convex polygon
\[
\boxed{\mathcal P_{d,r}=\bigcap_{k=0}^{d}\{(a,b):Q_k(a,b)\ge0\}.}
\]
It has **exactly \(d+1\) nonredundant facets**, with boundary edges indexed by the individual Walsh degrees \(0,\ldots,d\). In counterclockwise adjacency order its vertices arise from pairs of active degrees \((0,1),(1,2),\ldots,(d-1,d),(d,0)\). For \(i\ne j\) in these pairs, putting \(D_{ij}=u_i v_j-u_j v_i\ne0\), the corresponding vertex is exactly
\[
\boxed{(a,b)=\left(\frac{v_i-v_j}{D_{ij}},\frac{u_j-u_i}{D_{ij}}\right).}
\]
The full Gram matrix has eigenvalues
\[
\boxed{\lambda_k=(1+r)^{d-k}(1-r)^kQ_k(a,b),\qquad
\text{multiplicity }\binom dk.}
\]
It is positive definite in the polygon interior. At the relative interior of facet \(k\), it has nullity \(\binom dk\); at the vertex where facets \(i,j\) meet, it has nullity \(\binom di+\binom dj\).

There is a further *sharp local-to-global singularity law*. For a positive-semidefinite \(K_{a,b}\), define \(s(K)\) as the minimum cardinality of a set of **distinct** cube vertices whose principal Gram matrix is singular. Then at the relative interior of facet \(k\),
\[
\boxed{s(K)=2^{\max\{k,d-k\}}.}
\]
At the vertex shared by consecutive facets \(k,k+1\), \(0\le k<d\),
\[
\boxed{s(K)=2^{\max\{k,d-k-1\}}.}
\]
At the remaining vertex, shared by degrees \(0,d\),
\[
\boxed{s(K)=2^{d-1}.}
\]
Every smaller principal Gram matrix is positive definite, and explicit singular configurations attain every threshold. Thus some full-cube degeneracies are invisible on exponentially many fewer than \(2^d\) sampling sites.

## Assumptions and scope
All Gram matrices use distinct sampling vertices of the full binary cube, and unnormalized counting-measure convolution is used for spectral eigenvalues. The kernel diagonal is \(K_{a,b}(x,x)=1\). The parameter \(r\) is fixed in \((0,1)\); \(a,b\) are arbitrary real numbers, with no independent pointwise nonnegativity assumption on off-diagonal kernel values. Positive semidefiniteness means nonnegative complex quadratic forms on every finite selection (equivalently, on the full finite group); a *singular subset* is a principal matrix with a nonzero null vector. The minimum \(s(K)\) is asserted only on the polygon boundary; in the interior no singular subset exists.

## Proof
**1. Exact Walsh spectrum.** Identify the cube with the product group under coordinatewise multiplication and let \(\chi_S(x)=\prod_{j\in S}x_j\). A character of degree \(k=|S|\) diagonalizes the base kernel \(r^{h}\) with eigenvalue
\[
L_k(r)=\sum_{z\in G}r^{h(z,\mathbf 1)}\chi_S(z)=(1+r)^{d-k}(1-r)^k.
\]
Acting on \(L_k\) with \(r\partial_r\) and \(r^2\partial_r^2/2\) gives the Fourier transforms of \(h r^h\) and \(\binom h2r^h\). Division by \(L_k>0\) gives exactly \(u_k,v_k\), hence the eigenvalue and multiplicity formula. Fourier diagonalization proves the stated positivity inequalities and the nullity rule once their facet structure is established.

**2. Every one of the \(d+1\) inequalities is essential.** The normal vectors \(p_k=(u_k,v_k)\) satisfy
\[
 u_k=d\alpha-k(\alpha+\beta),\qquad
 2v_k=u_k^2+(\beta-\alpha)u_k-d\alpha\beta.
\]
Thus their distinct first coordinates lie on a strictly convex parabola. Its strict tangent at each \(p_k\) exposes \(p_k\) uniquely in \(\operatorname{conv}\{p_0,\ldots,p_d\}\); the convex hull is a polygon with precisely these \(d+1\) vertices and boundary chain \(p_0p_1\cdots p_dp_0\).

To prove this polygon contains the origin in its **interior**, use the strictly positive weights
\[
 w_k=\binom dk(1+r)^{d-k}(1-r)^k.
\]
Orthogonality of cube characters and the vanishing of \(h(\mathbf1,\mathbf1)\) and \(\binom{h(\mathbf1,\mathbf1)}2\) give
\[
 \sum_{k=0}^d w_k u_k=\sum_{k=0}^d w_k v_k=0.
\]
Since at least three \(p_k\) are noncollinear, a strictly positive barycentric representation forces the origin into the two-dimensional interior. Taking the negative polar of this convex hull produces exactly \(\mathcal P_{d,r}\), bounded with one genuine facet for every \(k\). The dual vertex/edge correspondence proves the claimed adjacency and uniqueness of the two active levels at every vertex. Cramer's rule gives the displayed exact vertex coordinates. There are no triple contacts, because no three distinct points on the strict parabola are collinear.

**3. A sharp homogeneous-Walsh support lemma.** A nonzero multilinear polynomial on \(\{-1,1\}^d\) of degree at most \(t\) has at least \(2^{d-t}\) nonzero values (for \(0\le t\le d\)). For completeness, induct on \(d\): if the last variable is absent, double the lower-dimensional support; otherwise write \(f(x',x_d)=g(x')+x_d h(x')\) with nonzero \(h\) of degree at most \(t-1\). On every point where \(h\ne0\), at least one of \(g+h,g-h\) is nonzero. Induction gives the bound in both cases.

If \(f\) is supported in the *homogeneous Walsh degree* \(k\), apply the lemma to \(f\) and to \(\chi_{[d]}f\), whose Fourier degree is exactly \(d-k\). Therefore
\[
 |\operatorname{supp}f|\ge \max\{2^{d-k},2^k\}=2^{\max\{k,d-k\}}.
\]
This is attained. Put \(m=\min\{k,d-k\}\); with empty products interpreted as \(1\), the homogeneous degree-\(k\) polynomial
\[
 f(x)=\prod_{j=1}^{m}(x_{2j-1}+x_{2j})
       \prod_{i=2m+1}^{k+m}x_i
\]
uses at most \(d\) coordinates and is nonzero at exactly \(2^{d-m}=2^{\max\{k,d-k\}}\) cube vertices.

**4. Two consecutive degrees and the antipodal pair.** If \(f\) has Walsh degrees only in \(\{k,k+1\}\), the degree bound \(k+1\), followed by multiplying by \(\chi_{[d]}\) (giving maximum degree \(d-k\)), yields
\[
|\operatorname{supp}f|\ge 2^{\max\{k,d-k-1\}}.
\]
Let \(m=\min\{k,d-k-1\}\). Equality is attained by
\[
 f(x)=\left[\prod_{j=1}^{m}(x_{2j-1}+x_{2j})\right]
 \left[\prod_{i=2m+1}^{k+m}x_i\right](1+x_{k+m+1}),
\]
whose only degrees are \(k,k+1\), and whose support has size \(2^{d-m-1}\). For degrees \(\{0,d\}\), the entire space consists of \(A+B\chi_{[d]}\). Every nonzero member is supported on at least one entire parity class, of size \(2^{d-1}\), and \(1+\chi_{[d]}\) attains this value.

**5. Principal-matrix singularity.** At a boundary point, the nullspace of the positive-semidefinite convolution matrix is precisely the span of Walsh characters at the active zero-degree levels. For a set \(E\subset G\), its principal Gram is singular if and only if the extension by zero of some nonzero vector supported in \(E\) belongs to the full Gram nullspace: a vanishing principal quadratic form also vanishes for the full positive-semidefinite matrix, hence the extended vector is in its kernel; the reverse implication is immediate. The minimum support results of Steps 3–4 therefore equal the minimum singular-subset cardinalities. The explicit polynomials also specify the attaining subsets as their nonzero evaluation sets.

## Verification
The accompanying standalone `check.py` uses exact rational arithmetic. It checks \(d=2,3,4,5,6\) and \(r\in\{1/4,1/3,1/2,2/3,3/4\}\): barycentric identities, parabola equations, all polygon vertices, exact full Walsh diagonalization, the unique active shell pairs, and explicit singular-vector constructions. It passed 125 distinct vertex spectra and 3,820 vertex-grid witness-value cases. Execute `python check.py`. These finite checks corroborate the algebra; the uniform statements for all dimensions and real parameters are proven in Steps 1–5, not extrapolated from finite experiments.

## Relationship to prior work
Classical Walsh character diagonalization, Krawtchouk transforms, finite-group Bochner positivity, and Reed–Muller-type minimum-weight arguments are the established ingredients. Zhao and Ge (2026) use distance-polynomial Fourier inertia on the **even subcube** to bound restricted-distance families, not to classify a damped quadratic positive-definite covariance family on the full cube or its minimum singular principal minors. Ivanisvili (2026) studies degree-sensitive Bohnenblust–Hille inequalities for cube Walsh polynomials; Han and Wang (2026) establish sharp \(L^1\)-Poincaré and Fourier-positivity inequalities on graphs, not the parameter polygon here. Related recent Hamming-product Gaussian-squared-distance and damped-cosine kernel results use different radial functions and different spectral boundary tests. The new combined assertion is the exact irredundant \(d+1\)-facet covariance region together with the degree-by-degree sharp local singularity thresholds.

## Limitations
This is a fixed-\(r\), full **binary** Hamming cube theorem. It does not classify nonbinary alphabets, arbitrary polynomial degree, weighted Hamming distances, or principal ranks beyond the *first* singular subset size. The spectral-facet description alone is not a claim that the classical Walsh/Fourier or Boolean polynomial-support lemmas are new. Published statements with different wording could contain an equivalent specialized cone or singular-subset theorem; no independent priority audit has been performed.

## References
- X. Zhao and G. Ge, *Universal Fourier-inertia bounds for prescribed even distances*, arXiv:2606.07261v1, first posted 2026-06-05, https://arxiv.org/abs/2606.07261.
- P. Ivanisvili, *Polynomial growth of Bohnenblust--Hille constants on the Hamming cube*, arXiv:2609.12427v1, first posted 2026-09-11, https://arxiv.org/abs/2609.12427.
- B.-X. Han and Y.-H. Wang, *Fourier Positivity and Sharp Poincaré Inequalities on Graphs*, arXiv:2611.09620v1, first posted 2026-11-06, https://arxiv.org/html/2611.09620v1.
- P. Feinsilver and R. Schott, *Krawtchouk transforms and convolutions*, 2019, https://doi.org/10.1142/S1664360719500097.
