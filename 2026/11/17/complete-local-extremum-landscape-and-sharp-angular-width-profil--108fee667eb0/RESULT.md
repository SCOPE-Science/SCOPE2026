# Complete local-extremum landscape and sharp angular width profiles of regular permutohedra

## Finding
For every integer \(n\ge3\), let \(\Pi_n=\operatorname{conv}\{(\sigma(1),\ldots,\sigma(n)):\sigma\in S_n\}\), with the induced Euclidean metric on its affine span. On the oriented unit-direction sphere
\[
\mathbb S_n=\{u\in\mathbb R^n:\sum_{i=1}^n u_i=0,\ \sum_{i=1}^n u_i^2=1\},
\]
its directional width is \(W_n(u)=\sum_{i<j}|u_i-u_j|\). All local extrema are strict, and they are exactly as follows.

Every nonempty proper subset \(A\subsetneq[n]\) yields one strict local minimum \(u_A\): its coordinates have one common lower value on \(A\), one common higher value on \(A^c\), and \(u_A\in\mathbb S_n\). These \(2^n-2\) points are *all* local minima. Writing \(t=|A|\), their widths are
\[
W_n(u_A)=w_{n,t}=\sqrt{nt(n-t)}.
\]
Exactly \(2n\) of them, those with \(t=1\) or \(n-1\), are global minima, of value \(\sqrt{n(n-1)}\); the remaining \(2^n-2-2n\) are strict nonglobal local minima.

The \(n!\) strict local maxima are exactly the normalized permutations of the vector \((2j-n-1)_{j=1}^n\). All are global maxima, of value
\[
\sqrt{n(n^2-1)/3}.
\]
There are no other local extrema.

Moreover, put \(\delta_{n,t}=\sqrt{n/[t(n-t)]}\), and define
\[
\gamma_{n,t}=\min\left\{\sqrt{m(m-1)}:\ m\in\{t,n-t\},\ m\ge2\right\}.
\]
The exact lower envelope of widths at angular distance \(\theta\) from \(u_A\) is
\[
\min_{\substack{h\perp u_A,\ \sum_i h_i=0\\\|h\|_2=1}}
 W_n(u_A\cos\theta+h\sin\theta)
 =w_{n,t}\cos\theta+\gamma_{n,t}\sin\theta
\]
for every \(0<\theta<\arctan(\delta_{n,t}/\sqrt2)\). The bound is attained by an explicit two-valued tangent perturbation supported on a smallest non-singleton block. In particular \(\gamma_{n,t}\) is the exact positive one-sided angular-growth coefficient.

## Assumptions and scope
The statement concerns \(n\ge3\), oriented Euclidean unit directions in the \((n-1)\)-dimensional linear subspace perpendicular to \(\mathbf1\), and the standard (unscaled) permutohedron whose vertices are permutations of \((1,\ldots,n)\). Opposite oriented directions are counted separately; in particular \(u_A=-u_{A^c}\). An angular profile is asserted only on the explicit open interval above. No assertion about angular behavior past the first permitted inter-block crossing is made.

## Proof
**1. Exact width and chamber gradients.** The translated segment-sum identity
\[
\Pi_n=\mathbf1+\sum_{1\le i<j\le n}[e_i,e_j]
\]
shows, by additivity of width under Minkowski sums, that \(W_n(u)=\sum_{i<j}|u_i-u_j|\). If the coordinates of \(u\) are strictly increasing, then
\[
W_n(u)=\langle a,u\rangle,\qquad a_j=2j-n-1.
\]
The same expression after a permutation holds on each open order chamber. Since \(a\) has zero sum and \(\|a\|_2^2=n(n^2-1)/3\), Cauchy–Schwarz gives the asserted global maximum. Its equality vectors are precisely the normalized permutations of \(a\), which have distinct coordinates and are strict local maxima within their chambers.

**2. Sharp within-block variation inequality.** For \(m\ge2\) and \(z\in\mathbb R^m\) of coordinate sum zero, let \(T_m(z)=\sum_{i<j}|z_i-z_j|\). Then
\[
T_m(z)\ge\sqrt{m(m-1)}\,\|z\|_2.
\]
To prove this, sort the entries. For \(1\le k<m\), let \(b_k\) be the zero-mean step vector whose first \(k\) coordinates equal \(-(m-k)/m\) and last \(m-k\) equal \(k/m\). Any sorted zero-mean \(z\) decomposes as \(z=\sum_{k=1}^{m-1}d_kb_k\), where \(d_k=z_{k+1}-z_k\ge0\). Direct calculation gives \(T_m(b_k)=k(m-k)\) and \(\|b_k\|_2^2=k(m-k)/m\). Since \(k(m-k)\ge m-1\), linearity of \(T_m\) inside the sorted cone and the Euclidean triangle inequality give
\[
T_m(z)=\sum_k d_k T_m(b_k)
\ge\sqrt{m(m-1)}\sum_kd_k\|b_k\|_2
\ge\sqrt{m(m-1)}\|z\|_2.
\]
The constant is attained by \(b_1\) and \(b_{m-1}\), so it is sharp.

**3. Two-level points are all strict local minima, with exact angular growth.** Fix a nonempty proper set \(A\), \(|A|=t\), and take
\[
(u_A)_i=\begin{cases}-\sqrt{(n-t)/(nt)},&i\in A,\\
\sqrt{t/[n(n-t)]},&i\notin A.
\end{cases}
\]
The gap between the two values is \(\delta_{n,t}\), and the \(t(n-t)\) cross-group pairs give \(W_n(u_A)=w_{n,t}\).

Any unit tangent vector \(h\in\mathbb S_n\cap u_A^\perp\) has zero sum separately on \(A\) and \(A^c\). For \(\tan\theta<\delta_{n,t}/\sqrt2\), no cross-group order can reverse, because \(|h_i-h_j|\le\sqrt2\). The cross-group terms sum to \(w_{n,t}\cos\theta\) (their linear perturbations cancel). The within-group terms sum to
\[
\sin\theta\,[T_t(h|_A)+T_{n-t}(h|_{A^c})],
\]
with the singleton term understood as zero. By Step 2, this is at least \(\gamma_{n,t}\sin\theta\), because \(\|h|_A\|_2+\|h|_{A^c}\|_2\ge1\). Equality is attained by taking \(h\) supported on the smaller available non-singleton block and proportional there to \(b_1\), and zero elsewhere. This proves the exact angular formula and its sharp coefficient. Since \(\gamma_{n,t}>0\), it also proves strict local minimality.

**4. No other local extrema.** Suppose \(u\) has exactly \(r\) distinct coordinate values, with nonempty ordered level blocks \(B_1,\ldots,B_r\) of sizes \(m_1,\ldots,m_r\). On the submanifold of unit directions constant within each \(B_j\), with strict inequalities between successive levels, width is the linear functional \(\langle c,u\rangle\), where the constant coefficient on block \(B_j\) is
\[
c_j=2\sum_{\ell<j}m_\ell+m_j-n.
\]
The coefficients \(c_j\) increase strictly with \(j\). In this \((r-1)\)-dimensional linear subspace of zero-mean block-constant vectors, \(c\) itself has zero mean. If \(r\ge3\), the unit sphere in that subspace has positive dimension. Its only critical points for the linear functional are \(\pm c/\|c\|_2\). The negative one has decreasing block values and cannot lie in the given ordered stratum; the positive one is a strict *maximum* along this positive-dimensional submanifold. Thus no \(r\ge3\) point is a local minimum.

If \(r<n\), at least one block has size at least two. A small mean-zero perturbation within that block is tangent to \(u\), leaves all cross-block terms unchanged to first order, and *increases* width by a strictly positive amount to first order. Hence no point with \(3\le r<n\) is a local maximum: nonstationary ones already fail along the block-constant submanifold; stationary ones fail by the block-splitting perturbation. If \(r=n\), every direction lies in an open order chamber, where width is a linear functional on the sphere, so its only local extremum is the unique positive-gradient maximum described in Step 1. Finally \(r=2\) was settled by Step 3. This proves completeness.

**5. Global minima and counts.** The two-level directions are in bijection with the \(2^n-2\) proper nonempty subsets of \([n]\), and \(w_{n,t}^2=nt(n-t)\) is smallest precisely when \(t=1\) or \(n-1\). Since a global minimum exists and the preceding classification covers all local minima, its value and \(2n\) equality directions follow. The maximum count is \(n!\), since the gradient has pairwise different coordinates.

## Verification
Execute `python3 check_permuto_width.py` with Python 3 and no third-party packages. It checks the sharp complete-graph variation inequality on 48,534 nonzero integer zero-sum vectors, 275 partition-size profiles for \(3\le n\le24\), all 275 explicit sharp angular perturbations, and 5,910 permutation representations of maximum directions in small ranks. The expected final line is `PERMUTO_WIDTH_CHECKS_PASS integer_inequalities=48534 cut_profiles=275 sharp_geodesics=275 maxima_permutations=5910`. The infinite assertions are proved in Steps 1–5; the finite checker is not an exhaustive verification of all real directions or all dimensions.

## Relationship to prior work
Ardila, Castillo, Eur and Postnikov (2019, arXiv:1904.11029, especially Sections 2.3 and 4.1–4.3) give the Coxeter-permutohedral and graphic-zonotope framework from which the width formula follows. Ardila, Supina and Vindas-Meléndez (2019, arXiv:1911.11159, Sections 1–2) develop the fixed-polytope and Ehrhart theory of the same permutohedron. The NIST Gini mean-difference reference documents the equivalent normalized pairwise-absolute-difference functional. Those ingredients and the global Cauchy upper bound are not claimed as novel. The result here is the *complete spherical local-extremum classification* and its *attained quantitative angular profile*, not a reformulation of face counts, Ehrhart data, or the Gini definition. Related results on the local-width landscape of regular simplices concern the different functional \(\max_i u_i-\min_i u_i\); neither its local width values nor its sharp tangent constants imply this theorem.

## Limitations
The equivalence with complete-graph total variation creates a potential historical-priority risk from nonsmooth spectral graph theory or older inequalities for sample Gini dispersion. No general classification of this exact Euclidean-spherical local-extremum landscape was identified in the checked sources; absence from those searches is not a proof of priority. The angular envelope is asserted only before the specified cross-level threshold. The result does not cover unequal segment weights, generalized permutohedra, or changing the Euclidean normalization. Independent mathematical validation has not been performed.

## References
1. F. Ardila, F. Castillo, C. Eur, A. Postnikov, *Coxeter submodular functions and deformations of Coxeter permutahedra*, arXiv:1904.11029, first submitted 2019-04-24; *Advances in Mathematics* 365 (2020), 107039, DOI 10.1016/j.aim.2020.107039.
2. F. Ardila, M. Supina, A. R. Vindas-Meléndez, *The equivariant Ehrhart theory of the permutahedron*, arXiv:1911.11159, first submitted 2019-11-25; *Proceedings of the American Mathematical Society*.
3. NIST/SEMATECH, *GINI MEAN DIFFERENCE*, Dataplot reference, https://www.itl.nist.gov/div898/software/dataplot/refman2/auxillar/gmd.htm (implementation dated 2023-07).
4. Y. van Gennip, N. Guillen, B. Osting, A. L. Bertozzi, *Mean Curvature, Threshold Dynamics, and Phase Field Theory on Finite Graphs* (2014), DOI 10.1007/s00032-014-0216-8 (background on graph total variation; not a claim of the present result).
