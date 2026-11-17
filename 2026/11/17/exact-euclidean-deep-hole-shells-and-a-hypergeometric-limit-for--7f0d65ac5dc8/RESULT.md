# Exact Euclidean deep-hole shells and a hypergeometric limit for panhandle matroid polytopes

## Finding

Fix integers \(3\le r\le s\) and \(h\ge2\), and put \(n=s+h\). The rank-\(r\) hypersimplex and panhandle base polytope in their canonical Euclidean realization are
\[
\Delta_{r,n}=\{x\in[0,1]^n:\sum_{i=1}^{n}x_i=r\},\qquad
P_{r,s,n}=\{x\in\Delta_{r,n}:\sum_{i=s+1}^{n}x_i\le1\}.
\]
For any \(r\)-element subset \(S\subset[n]\), put \(j=|S\cap\{s+1,\ldots,n\}|\), and let \(v_S\) be its indicator vector. Its squared Euclidean distance to the panhandle polytope is precisely
\[
\operatorname{dist}_2(v_S,P_{r,s,n})^2=
\begin{cases}
0,&j\le1,\\
(j-1)^2\left(\dfrac1j+\dfrac1{s-r+j}\right),&2\le j\le \min\{r,h\}.
\end{cases}
\]
For each \(j\ge2\) this positive squared-distance shell contains exactly \(\binom hj\binom s{r-j}\) vertices. These shell values increase strictly with \(j\).

Consequently, writing \(J=\min\{r,h\}\), the exact (continuous) Euclidean Hausdorff distance is
\[
\boxed{d_H(\Delta_{r,n},P_{r,s,n})^2=(J-1)^2\left(\frac1J+\frac1{s-r+J}\right).}
\]
**Every** farthest point of the whole hypersimplex is a vertex having exactly \(J\) tail coordinates equal to one. There are exactly \(\binom hJ\binom s{r-J}\) farthest points; there are no nonvertex maximizers.

If \(S\) has \(j\ge2\) tail elements, write \(A=S\cap[s]\), \(B=S\cap\{s+1,\ldots,n\}\), and \(c=s-r+j\). The unique nearest point \(p_S\in P_{r,s,n}\) is
\[
(p_S)_i=
\begin{cases}
1,&i\in A,\\
(j-1)/c,&i\in[s]\setminus A,\\
1/j,&i\in B,\\
0,&i\in\{s+1,\ldots,n\}\setminus B.
\end{cases}
\]
It lies in the relative interior of an exposed face isometric to the product of two hypersimplices \(\Delta_{j-1,c}\times\Delta_{1,j}\), of dimension \(s-r+2j-2\).

There is also a typical-shell limit. Consider sequences with \(n\to\infty\), \(s/n\to\alpha\), \(r/n\to\rho\), and \(0<\rho<\alpha<1\); put \(\beta=1-\alpha\). Choose \(S\) uniformly among all \(r\)-subsets, and let \(D_n=\operatorname{dist}_2(v_S,P_{r,s,n})^2\), \(m_n=rh/n\), \(c_n=s-r\), and
\[
f_n(t)=(t-1)^2\left(\frac1t+\frac1{c_n+t}\right)\quad(t>0).
\]
Define \(g(x)=x+x^2/(\alpha-\rho+x)\) and \(x_0=\rho\beta\). Then
\[
\frac{D_n}{n}\xrightarrow{\mathsf P}g(x_0),\qquad
\frac{D_n-f_n(m_n)}{\sqrt n}\xrightarrow{\mathrm d}N(0,\sigma^2),
\]
where
\[
\boxed{\sigma^2=\rho(1-\rho)\alpha\beta
\left[2-\frac{(\alpha-\rho)^2}{(\alpha-\rho+\rho\beta)^2}\right]^2.}
\]
By contrast, \(d_H(\Delta_{r,n},P_{r,s,n})^2/n\to g(\min\{\rho,\beta\})>g(\rho\beta)\). Thus typical and worst-case squared losses have different positive linear-order constants.

## Assumptions and scope

The dimension is \(n\), the rank is \(r\), and all coordinates carry the ordinary Euclidean norm without rescaling. The stated finite formulas require \(3\le r\le s\) and \(h=n-s\ge2\). The two source polytopes lie in the same affine hyperplane \(\sum_i x_i=r\). The panhandle polytope is the convex hull of indicators of rank-\(r\) sets containing at most one tail element, equivalently the stated halfspace truncation; the defining description is established in the cited original literature. Binomial coefficients with an inadmissible lower index are zero. The Gaussian statement assumes the specified strictly interior limiting proportions and concerns uniformly selected *hypersimplex vertices*, not uniformly sampled continuous volume.

## Proof

**Exact projection and contact face.** If \(j\le1\), the indicator already lies in \(P_{r,s,n}\). For \(j\ge2\), the proposed \(p_S\) belongs to \([0,1]^n\): note \(c=s-r+j\ge j\) and \(0<(j-1)/c<1\). Its head coordinates sum to \(r-j+(j-1)=r-1\), and its tail coordinates sum to one, so it belongs to \(P_{r,s,n}\).

Put \(d=(j-1)/c\), \(e=(j-1)/j\), and \(w=v_S-p_S\). Then \(w=-d\) on \([s]\setminus A\), \(w=e\) on \(B\), and \(w=0\) elsewhere. For arbitrary \(y\in P_{r,s,n}\), let \(t=\sum_{i>s}y_i\le1\). Since \(\sum_{i\in A}y_i\le |A|=r-j\) and \(\sum_{i\in B}y_i\le t\), we have
\[
\langle w,y\rangle
=-d\sum_{i\in[s]\setminus A}y_i+e\sum_{i\in B}y_i
\le-d(j-t)+et\le-d(j-1)+e=\langle w,p_S\rangle.
\]
Thus \(\langle v_S-p_S,y-p_S\rangle\le0\) for all \(y\in P_{r,s,n}\), the Euclidean projection criterion. Strict convexity yields uniqueness. The squared residual norm is \(c d^2+j e^2\), establishing the displayed formula.

Equality in the supporting inequality requires \(y_i=1\) on \(A\), zero outside \(B\) in the tail, and tail sum one. The remaining head coordinates sum to \(j-1\). Hence the exposed equality face is \(\Delta_{j-1,c}\times\Delta_{1,j}\), with the stated dimension, and both factors have strictly interior coordinates at \(p_S\).

**Shell counts and the global Hausdorff maximum.** A subset with \(j\) tail elements can be chosen in exactly \(\binom hj\binom s{r-j}\) ways. For real \(t>1\), both functions \((t-1)^2/t\) and \((t-1)^2/(s-r+t)\) are strictly increasing: their derivatives are \(1-t^{-2}\) and \((t-1)(2(s-r)+t+1)/(s-r+t)^2\), respectively. Hence the largest vertex distance occurs precisely at \(j=J\).

The squared distance to any nonempty closed convex set is convex. More precisely, for a convex combination \(x=\sum_i\lambda_i v_{S_i}\), with \(p_i\) the respective projections and \(w_i=v_{S_i}-p_i\), convexity of the target and the Euclidean variance identity imply
\[
\operatorname{dist}_2(x,P_{r,s,n})^2
\le\left\|\sum_i\lambda_i w_i\right\|_2^2
=\sum_i\lambda_i\|w_i\|_2^2-
\frac12\sum_{i,k}\lambda_i\lambda_k\|w_i-w_k\|_2^2.
\]
The first sum is at most the squared vertex maximum. For distinct maximizing vertices, \(w_i\ne w_k\), since their negative head supports and positive tail supports recover \(A\) and \(B\) uniquely. Therefore, equality is possible only when one maximizing vertex has all the weight. Every point of the hypersimplex is a convex combination of its vertices, proving both the continuous Hausdorff formula and the *complete* maximizing locus.

**Gaussian regime.** The number \(J_n\) of chosen tail elements is hypergeometric with parameters \((n,h,r)\), mean \(m_n=rh/n\) and variance \(rh(n-h)(n-r)/(n^2(n-1))\). Its standard finite-population central limit theorem gives
\[
\frac{J_n-m_n}{\sqrt n}\xrightarrow{\mathrm d}
N\bigl(0,\rho(1-\rho)\alpha\beta\bigr).
\]
Moreover \(J_n/n\xrightarrow{\mathsf P}x_0>0\), so the event \(J_n\le1\) has vanishing probability. Uniformly for \(t/n\) in a compact neighborhood of \(x_0\), \(f_n(t)/n\to g(t/n)\) with convergence of first derivatives, and
\[
g'(x)=2-\frac{(\alpha-\rho)^2}{(\alpha-\rho+x)^2}.
\]
Taylor expansion at \(m_n\), the hypergeometric central limit theorem, and Slutsky's theorem yield the displayed limit and variance. Finally, \(J/n\to\min\{\rho,\beta\}\), and monotonicity of \(g\) with \(\rho\beta<\min\{\rho,\beta\}\) proves the strict typical-versus-worst-case separation.

## Verification

A standalone exact checker, `verify_panhandle_distance.py`, enumerates small panhandle polytopes by their basis vertices, constructs every proposed projection using rational arithmetic, checks its feasibility and squared distance, and verifies the supporting-normal inequality against **every** feasible basis. Across its tested parameter range this covers 56 configurations, 6,034 source hypersimplex vertices, 3,174 excluded vertices and 168,870 supporting inequalities. It verifies all 102 positive shell-count cases independently by binomial counts. It then independently solves 1,116 small quadratic programs with SciPy and compares their projected coordinates to the formula, with maximum discrepancy below \(1.1\times10^{-14}\). One further finite-population variance check at growing dimensions agrees with the displayed asymptotic variance; no finite experiment is asserted to prove the limiting theorem. To reproduce, run `python verify_panhandle_distance.py` with Python, NumPy and SciPy installed.

## Relationship to prior work

Hanely, Martin, McGinnis, Miyata, Nasr, Vindas-Meléndez and Yin (arXiv:2201.12442, first submitted January 28, 2022), Definition 4.1 and Proposition 4.4, establish the panhandle basis system and the exact truncation description, and study Ehrhart functions and volumes. Fan and Li (arXiv:2110.11549) study Ehrhart polynomials of Schubert matroids, including the panhandle subclass. Wang and Lu (arXiv:1503.01002) give a general algorithm for Euclidean projection onto capped simplices; the general projection principle is a known ingredient, not claimed here. None of those inspected primary results states the complete two-polytope distance spectrum, all continuous farthest points, product-hypersimplex contact faces, or the hypergeometric metric limit. The previously determined paving-matroid hyperplane-distance theorem already includes the rank-two panhandle case, which is excluded from the present rank-at-least-three scope. Other publicly indexed results on inballs, covariance, minimum spheres and width laws for panhandle matroids address different metric quantities; claims of priority beyond these comparisons remain conditional on a wider independent literature audit.

## Limitations

The theorem concerns standard unweighted Euclidean coordinates. It does not describe general input-point projections, weighted metrics, other Schubert or lattice-path matroids, or the continuous-volume distribution of distances. The Gaussian limit needs nondegenerate proportional rank and block sizes; other scaling regimes are not classified. The finite checker covers only the specified parameters, and bibliographic novelty is provisional rather than independently certified.

## References

1. D. Hanely, J. L. Martin, D. McGinnis, D. Miyata, G. D. Nasr, A. R. Vindas-Meléndez and M. Yin, *Ehrhart Theory of Paving and Panhandle Matroids*, arXiv:2201.12442 (first public version 2022-01-28), especially Definition 4.1 and Proposition 4.4. https://arxiv.org/abs/2201.12442
2. N. J. Y. Fan and Y. Li, *On the Ehrhart Polynomial of Schubert Matroids*, arXiv:2110.11549 (first public version 2021-10-22). https://arxiv.org/abs/2110.11549
3. W. Wang and C. Lu, *Projection onto the capped simplex*, arXiv:1503.01002 (first public version 2015-03-03). https://arxiv.org/abs/1503.01002
