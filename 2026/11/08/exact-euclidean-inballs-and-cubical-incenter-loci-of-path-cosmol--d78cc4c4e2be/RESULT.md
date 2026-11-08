# Exact Euclidean inballs and cubical incenter loci of path cosmological polytopes

## Finding
For every integer \(n\ge4\), the standard cosmological polytope of the path on \(n\) vertices has an **exact intrinsic Euclidean inradius**
\[
 r_n=\frac{1}{c_2+c_3+\frac{n-3}{2}c_4},\qquad
 c_j=\sqrt{\frac{j(2n-1-j)}{2n-1}}.
\]
Its **entire set of centers of maximal Euclidean balls is a nondegenerate affine cube of dimension \(n-4\)**, with \(2^{n-4}\) vertices; the incenter is unique precisely at \(n=4\) within this family. An explicit independent box parametrization of all centers is given below. In particular \(\lim_{n\to\infty}nr_n=1\).

## Assumptions and scope
Fix \(n\ge4\). Let \(e_1,\ldots,e_n,f_1,\ldots,f_{n-1}\) denote the standard orthonormal basis of \(\mathbb R^{2n-1}\). The **path cosmological polytope** \(C_n\) is the convex hull of the following \(3(n-1)\) points, one triple for each \(1\le i<n\):
\[
 e_i+e_{i+1}-f_i,\quad e_i-e_{i+1}+f_i,\quad -e_i+e_{i+1}+f_i.
\]
All points lie in the affine hyperplane \(H=\{(x,y):\sum_{i=1}^n x_i+\sum_{i=1}^{n-1}y_i=1\}\). The metric is the one inherited from the ambient orthonormal basis, **not** an arbitrary affine-equivalent metric. For an interval \([a,b]\), \(1\le a\le b\le n\), write
\[
 h_{ab}(x,y)=\sum_{i=a}^b x_i+\mathbf1_{a>1}y_{a-1}+\mathbf1_{b<n}y_b.
\]
The connected-subgraph facet theorem for cosmological polytopes yields exactly the inequalities \(h_{ab}\ge0\), one for every interval. Put \(D=2n-1\). The indicator normal has \(q_{ab}=(b-a+1)+\mathbf1_{a>1}+\mathbf1_{b<n}\) nonzero unit entries. Its orthogonal projection onto the linear space parallel to \(H\) has norm \(c_{q_{ab}}=\sqrt{q_{ab}(D-q_{ab})/D}\). Thus a ball of intrinsic radius \(r\) with center \(z\in H\) lies in \(C_n\) if and only if \(h_{ab}(z)\ge r c_{q_{ab}}\) for every interval.

## Proof
**1. A sharp covering certificate.** Consider the \(n+1\) facets indexed by \([1,1]\), \([n,n]\), and the \(n-1\) adjacent-pair intervals \([i,i+1]\). Every site coordinate and every edge coordinate occurs exactly twice in the sum of their indicator normals, so for \(z\in H\),
\[
 h_{11}(z)+h_{nn}(z)+\sum_{i=1}^{n-1}h_{i,i+1}(z)=2.
\]
The two end singletons have normal norm \(c_2\), the two end pairs have norm \(c_3\), and the remaining \(n-3\) pairs have norm \(c_4\). Consequently every inscribed radius satisfies
\[
 2\ge r\bigl(2c_2+2c_3+(n-3)c_4\bigr),
\]
proving \(r\le r_n\).

**2. A center attaining the bound.** Define \(z^0=(x^0,y^0)\) by
\[
 x^0_1=x^0_n=\frac{r_nc_2}{2},\qquad
 x^0_2=x^0_{n-1}=\frac{r_n(c_4-c_2)}2,\qquad
 x^0_i=r_n(c_4-c_3)\ (3\le i\le n-2),
\]
\[
 y^0_1=y^0_{n-1}=\frac{r_nc_2}{2},\qquad
 y^0_i=r_n\left(c_3-\frac{c_4}{2}\right)\ (2\le i\le n-2).
\]
Empty index ranges contribute no coordinates. The covering identity gives \(\sum x^0+\sum y^0=1\), because all its constituent facets attain their required radii. Each internal singleton has \(h_{ii}(z^0)=r_nc_3\), and the end singletons have \(h_{11}(z^0)=h_{nn}(z^0)=r_nc_2\). An interior interval of length \(\ell\ge2\) has
\[
 h_{ab}(z^0)/r_n=c_4+(\ell-2)(c_4-c_3),\quad 2\le a\le b\le n-1;
\]
a proper prefix or suffix of length \(\ell\ge2\) has
\[
 h_{ab}(z^0)/r_n=c_3+(\ell-2)(c_4-c_3);
\]
and the full interval has
\[
 h_{1n}(z^0)/r_n=c_3+(n-3)(c_4-c_3).
\]
The function \(t\mapsto\sqrt{t(D-t)/D}\) is strictly concave on \((0,D)\). Therefore its increasing-index consecutive secant slopes decrease strictly, and all displayed expressions are at least their required \(c_{q_{ab}}\). Thus \(z^0\) supports a radius-\(r_n\) ball, proving equality in step 1.

**3. Necessity of the box coordinates.** Let \(z\) be any center at the optimal radius. Equality in the covering certificate forces all \(n+1\) covering facets tight. For internal singleton indices introduce nonnegative slacks
\[
 \sigma_i=h_{ii}(z)-r_nc_3\quad(2\le i\le n-1),
\]
and put \(\sigma_0=\sigma_1=\sigma_n=\sigma_{n+1}=0\). The adjacent-pair tight equations and the singleton identities uniquely determine every coordinate relative to \(z^0\):
\[
 x_i=x_i^0-\tfrac12(\sigma_{i-1}+\sigma_{i+1})\quad(1\le i\le n),
\qquad
 y_i=y_i^0+\tfrac12(\sigma_i+\sigma_{i+1})\quad(1\le i<n).
\]
For any interval of length at least two, telescoping gives the precise slack loss
\[
 h_{ab}(z)=h_{ab}(z^0)-\sum_{i=a+1}^{b-1}\sigma_i.
\]
The prefix \([1,3]\) and suffix \([n-2,n]\) are tight already at \(z^0\); therefore \(\sigma_2=\sigma_{n-1}=0\). Set the strictly positive discrete concavity gap
\[
 \kappa_n=2c_4-c_3-c_5>0.
\]
The interior triple \([i-1,i+1]\), \(3\le i\le n-2\), has baseline excess \(r_n\kappa_n\), so its inequality forces \(0\le\sigma_i\le r_n\kappa_n\).

**4. Sufficiency of all independent box coordinates.** Conversely choose independently any \(\sigma_i\in[0,r_n\kappa_n]\) for \(3\le i\le n-2\), with every other \(\sigma\) zero, and use the coordinate formulas above. The end singletons, internal singletons, and adjacent pairs hold automatically. Write \(\delta_j=c_{j+1}-c_j\), so \(\delta_3-\delta_j\ge\kappa_n\) for every \(j\ge4\). An interior interval of length \(\ell\ge3\) has baseline excess over its required facet distance equal to
\[
 r_n\sum_{j=4}^{\ell+1}(\delta_3-\delta_j)
 \ge r_n(\ell-2)\kappa_n,
\]
whereas its slack loss involves at most \(\ell-2\) free slacks. A proper prefix or suffix of length \(\ell\ge3\) has excess
\[
 r_n\sum_{j=3}^{\ell}(\delta_3-\delta_j)
 \ge r_n(\ell-3)\kappa_n,
\]
and at most \(\ell-3\) free slacks because \(\sigma_2=\sigma_{n-1}=0\). The full interval has excess
\[
 r_n\sum_{j=3}^{n-1}(\delta_3-\delta_j)
 \ge r_n(n-4)\kappa_n,
\]
with at most \(n-4\) free slacks. Every interval inequality is therefore satisfied, so every point of the box is an incenter. The independent coordinates \(\sigma_i\) can be recovered from the singleton support values, proving injectivity. Their number is \(n-4\), giving a cube with \(2^{n-4}\) vertices and the asserted uniqueness criterion. Finally \(c_j\to\sqrt j\) for each fixed \(j\) as \(n\to\infty\), hence \(nr_n\to1\).

## Verification
The accompanying `verify.py` reconstructs all \(n(n+1)/2\) interval normals, checks the double-cover certificate, solves an independent intrinsic Chebyshev linear program for dimensions corresponding to \(4\le n\le11\), and validates explicit box vertices. It also confirms by linear-algebra rank tests for \(4\le n\le8\) that the interval hyperplanes are actual facets of the original vertex hull. The finite checks are supporting computations; the universal proof is the four-part argument above. Run `python3 verify.py` with NumPy and SciPy.

## Relationship to prior work
Arkani-Hamed, Benincasa, and Postnikov introduced the cosmological-polytope vertex construction [1]. Kühne and Monin proved the connected-subgraph facet classification and derived face-vector recurrences for trees, including paths [2, Theorem 2.1, Sections 3–4]. Juhnke-Kubitzke, Solus, and Venturello studied triangulations and volumes of path and other cosmological polytopes [3]. The exact intrinsic Euclidean inradius and the full cubical center locus proved here are not consequences of the reported face-vector, triangulation, or volume formulas without additional metric analysis. Related metric results for star cosmological polytopes and for other graph-derived polytopes concern nonidentical vertex configurations or graph families. No claim of established global priority is made.

## Limitations
This theorem applies to the unweighted standard coordinate realization for paths with \(n\ge4\); it does not establish a formula for arbitrary trees, weighted cosmological polytopes, other affine embeddings, or the metric geometry of their faces. Bibliographic priority remains provisional, and independent external mathematical validation has not been performed.

## References
[1] N. Arkani-Hamed, P. Benincasa, A. Postnikov, *Cosmological Polytopes and the Wavefunction of the Universe*, arXiv:1709.02813 (2017), https://arxiv.org/abs/1709.02813.

[2] L. Kühne, L. Monin, *Faces of Cosmological Polytopes*, arXiv:2209.08069 (first posted 2022-09-16), https://arxiv.org/abs/2209.08069; Ann. Inst. Henri Poincaré D (2025).

[3] M. Juhnke-Kubitzke, L. Solus, L. Venturello, *Triangulations of Cosmological Polytopes*, arXiv:2303.05876 (2023), https://arxiv.org/abs/2303.05876.
