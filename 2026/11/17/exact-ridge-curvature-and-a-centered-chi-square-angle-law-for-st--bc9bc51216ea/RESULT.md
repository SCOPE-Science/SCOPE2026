# Exact ridge curvature and a centered chi-square angle law for star symmetric-edge polytopes

## Finding
For every integer \(d\ge2\), let \(H_d=\{x\in\mathbb R^{d+1}:\sum_{i=0}^d x_i=0\}\), with the restricted standard Euclidean metric, and consider the \(d\)-dimensional star symmetric-edge polytope
\[
P_d=\operatorname{conv}\{\pm(e_i-e_0):1\le i\le d\}\subset H_d.
\]
It has exactly \(d2^{d-1}\) ridges. Each ridge is determined by a missing leaf index and the signs on the other \(d-1\) leaves. Let \(t\) be the sum of the latter signs, \(j=|t|\) and \(B=d(d-1)-j^2\). Its intrinsic \((d-2)\)-volume and its **exterior** dihedral angle are exactly
\[
\boxed{A_{d,j}=\frac{\sqrt B}{(d-2)!},\qquad
\phi_{d,j}=\operatorname{atan2}\bigl(2\sqrt{(d+1)B},B-1\bigr).}
\tag{1}
\]
Here \(\operatorname{atan2}(y,x)\in(0,\pi)\) denotes the argument of \(x+iy\) for \(y>0\). The interior dihedral angle is \(\theta_{d,j}=\pi-\phi_{d,j}\). The possible \(j\)'s are \(d-1,d-3,\ldots\), terminating at zero or one. For each such \(j\), the exact multiplicity is
\[
\boxed{m_{d,j}=d\bigl(2-\mathbf1_{\{j=0\}}\bigr)
\binom{d-1}{(d-1+j)/2}.}
\tag{2}
\]
For \(d=2\), all four ridge angles are right angles. For every \(d\ge3\), all ridge interior angles are strictly obtuse, with exactly \(\lfloor(d-1)/2\rfloor+1\) distinct levels, strictly decreasing with \(j\).

The **second Steiner intrinsic volume**, defined by the coefficient convention
\[\operatorname{Vol}_d(P_d+\varepsilon B_2^d)=\sum_{k=0}^d\kappa_{d-k}V_k(P_d)\varepsilon^{d-k}\quad(\varepsilon\ge0),\]
has the explicit finite formula
\[
\boxed{V_{d-2}(P_d)=\frac{d}{2\pi(d-2)!}
\sum_{k=0}^{d-1}\binom{d-1}{k}
\sqrt{d(d-1)-(d-1-2k)^2}\;
\phi_{d,|d-1-2k|}.}
\tag{3}
\]
This formula includes \(V_0(P_2)=1\). Its leading curvature asymptotic and first nontrivial correction are
\[
\boxed{V_{d-2}(P_d)=\frac{2^{d-1}d^{3/2}}{\pi(d-2)!}
\left(1-\frac{5}{6d}+O(d^{-2})\right).}
\tag{4}
\]
Since \(\operatorname{Vol}_d(P_d)=2^d\sqrt{d+1}/d!\), the corresponding volume-normalized curvature satisfies
\[
\boxed{\frac{V_{d-2}(P_d)}{\operatorname{Vol}_d(P_d)}
=\frac{d^3}{2\pi}\left(1-\frac7{3d}+O(d^{-2})\right).}
\tag{5}
\]
If \(\Theta_d\) is the **interior** dihedral angle of a uniformly chosen ridge, then
\[
\boxed{d^{3/2}\left(\pi-\Theta_d-\frac2{\sqrt d}\right)
\ \xrightarrow{\mathrm d}\ \chi^2_1-\frac23.}
\tag{6}
\]
The centered chi-square distribution occurs in related bipartite examples; here the additional new geometric information is the complete **area-weighted ridge curvature**, with the cancellation producing the coefficient \(-5/6\) in (4).

## Assumptions and scope
The edge vectors have unit graph-edge weights and are embedded as signed standard coordinate roots; unimodular or other nonorthogonal deformations do not preserve these Euclidean assertions. All ridge volumes, dihedral angles, and intrinsic volumes are measured **intrinsically** inside the \(d\)-plane \(H_d\), not in all of \(\mathbb R^{d+1}\). For \(d=2\), ridges are vertices and have zero-dimensional Hausdorff measure one. Ridges are **unoriented**, hence counted only once. No statement about a random graph, or about all tree symmetric-edge polytopes, is intended.

## Proof
Write \(b_i=e_i-e_0\) and let \(B_0\) denote the matrix with columns \(b_i\). These form a basis of \(H_d\) and have Gram matrix \(G=B_0^{\mathsf T}B_0=I_d+\mathbf1\mathbf1^{\mathsf T}\), with determinant \(d+1\). The polytope is the invertible linear image of the standard \(d\)-crosspolytope. Its facets are indexed by sign vectors \(\sigma\in\{\pm1\}^d\), and a ridge corresponds uniquely to two sign vectors differing at exactly one coordinate \(i\).

The facet outward normal \(h_\sigma\in H_d\), scaled so its supporting hyperplane is \(\langle h_\sigma,x\rangle=1\), satisfies \(\langle h_\sigma,b_i\rangle=\sigma_i\). If \(S=\sum_i\sigma_i\), this uniquely gives
\[
(h_\sigma)_0=-\frac{S}{d+1},\qquad
(h_\sigma)_i=\sigma_i-\frac{S}{d+1}.
\tag{7}
\]
In particular \(\langle h_\sigma,h_\tau\rangle=\sigma^{\mathsf T}G^{-1}\tau\), where \(G^{-1}=I_d-\mathbf1\mathbf1^{\mathsf T}/(d+1)\). Fix the missing coordinate and let \(t\) be the sum of the other \(d-1\) facet signs. Denote the two adjacent facet normals by \(h_+\) and \(h_-\). Then
\[
\|h_\pm\|^2=d-\frac{(t\pm1)^2}{d+1},\qquad
\langle h_+,h_-\rangle=\frac{B-1}{d+1}.
\tag{8}
\]
The two-normal Gram determinant is
\[
\|h_+\|^2\|h_-\|^2-\langle h_+,h_-\rangle^2
=\frac{4B}{d+1}.
\tag{9}
\]
Thus the angle between outward normals has sine-to-cosine ratio \(2\sqrt{(d+1)B}/(B-1)\), proving the angular formula (1) with the stated \(\operatorname{atan2}\) convention. Since \(B\ge d-1\), the quantity \(B-1\) is positive for \(d\ge3\), and it vanishes when \(d=2\). For \(d\ge3\), \(\tan\phi_{d,j}\) strictly increases as \(j^2\) increases: differentiate \(\log\tan\phi\) with \(y=j^2\), obtaining
\[
-\frac1{2[d(d-1)-y]}+\frac1{d(d-1)-1-y}>0
\]
throughout the allowed interval. Hence the claimed strict angle ordering and distinct levels.

To compute ridge measure independently of the normals, let \(m=d-1\) and let \(v_1,\dots,v_m\) be the signed root vertices constituting a ridge. Their column Gram matrix is \(G_m=I_m+ss^{\mathsf T}\), for \(s\in\{\pm1\}^m\) of sum \(t\). The squared \((m-1)\)-dimensional parallelepiped measure of the difference vectors \(v_2-v_1,\ldots,v_m-v_1\) is the standard Gram identity
\[
\det(G_m)\,\mathbf1^{\mathsf T}G_m^{-1}\mathbf1
=m(m+1)-t^2=B.
\tag{10}
\]
Indeed, \(\det(G_m)=m+1=d\), \(G_m^{-1}=I_m-ss^{\mathsf T}/d\). Divide the square root by \((m-1)!\) to obtain (1). For fixed omitted leaf, exactly \(\binom{d-1}{(d-1+t)/2}\) sign configurations have sum \(t\). Combining the two signs of \(t\) proves (2), and summing gives \(d2^{d-1}\) ridges.

For a convex Euclidean \(d\)-polytope the codimension-two Steiner coefficient is the sum of the ridge \((d-2)\)-measures weighted by their **exterior** dihedral angles divided by \(2\pi\). Apply this identity to (1), enumerate signs by \(t=d-1-2k\), and account for the \(d\) choices of missing leaf to obtain (3). This normalization is checked at \(d=2\): four right angles contribute exactly one to \(V_0\).

For (4) and (6), choose a ridge uniformly and write \(T_d=\sum_{i=1}^{d-1}\varepsilon_i\) with independent fair signs, and \(Z_d=T_d/\sqrt d\). The central limit theorem gives \(Z_d\Rightarrow Z\sim N(0,1)\). Taylor expansion of the exact \(\operatorname{atan2}\) formula, uniformly on \(|T_d|\le d^{3/5}\), yields
\[
\phi_{d,|T_d|}=\frac2{\sqrt d}
+\frac{Z_d^2-2/3}{d^{3/2}}
+O\!\left(\frac{1+Z_d^4}{d^{5/2}}\right),
\tag{11}
\]
and
\[
\sqrt{d(d-1)-T_d^2}\;\phi_{d,|T_d|}
=2\sqrt d\left(1-\frac{5}{6d}
+O\!\left(\frac{1+Z_d^4}{d^2}\right)\right).
\tag{12}
\]
The cancellation of the \(Z_d^2\)-term in (12) is exact at order \(d^{-1}\): its positive contribution from the angle cancels the negative contribution from ridge volume. Hoeffding's bound makes the complement of the central event exponentially small in \(d^{1/5}\). Uniform fourth-moment bounds \(\mathbb E Z_d^4\le3\), together with the elementary global bounds \(0<\phi\le\pi\) and \(0<\sqrt B\le d\), permit expectation of (12), giving
\[
\mathbb E[\sqrt B\,\phi]=2\sqrt d\left(1-\frac{5}{6d}+O(d^{-2})\right).
\]
Since the number of ridges is \(d2^{d-1}\), the Steiner angle-sum identity yields (4). The volume follows from \(\det G=d+1\) and the standard crosspolytope's volume \(2^d/d!\); division and a first-order binomial expansion give (5). Finally, (11) and Slutsky's theorem prove (6), because \(Z^2\) is \(\chi^2_1\).

## Verification
The standalone `star_ridge_verify.py` computes **actual** facet normals in rational arithmetic and checks all \(768\) ridges for \(2\le d\le7\) against the exact squared ridge Gram determinants and the two-normal dihedral tangent identity. It checks the multiplicities of all \(15\) distinct finite spectrum classes across those dimensions. Independent numerical evaluations of the finite curvature sum at \(d=30,100,300\) check the first curvature correction; these do not prove the asymptotic expansion or the infinite-dimensional assertions. Running `python star_ridge_verify.py` in the package prints `STAR_RIDGE_PASS`.

## Relationship to prior work
Higashitani, Jochemko and Michałek's 2018 paper gives the foundational symmetric-edge-polytope definition and facets. D'Alì, Delucchi and Michałek's 2019 manuscript establishes that all tree symmetric-edge polytopes are unimodularly equivalent to crosspolytopes, a relation **not** preserving intrinsic Euclidean angles. Chen, Davis and Korchevskaia's 2021 paper concerns facet subgraphs and incidences. Existing studies determine the exact canonical star inradius and its incenter locus, and give identities for the **facet** areas of arbitrary tree symmetric-edge polytopes; neither statement supplies the **ridge** measures, paired facet angles, or their area-weighted Steiner curvature. A related complete-bipartite angle calculation produces the same centered chi-square fluctuation shape, so (6) by itself is **not** represented as a novel universal distribution. The independent geometric contribution is the exact star ridge area-angle spectrum and second-intrinsic-volume law, particularly the cancellation of random angular fluctuations in its first curvature correction.

## Limitations
The theorem applies only to unweighted star graphs in the specified Euclidean realization, and is not a formula for arbitrary trees or a guarantee of priority over every unindexed geometric-metric literature source. The claimed novelty is not the standard polytope face lattice, the elementary normal-vector identity, or the stand-alone occurrence of a centered chi-square limit. The full finite curvature formula is exact; the displayed asymptotic remainder is for \(d\to\infty\) only, with no uniformity asserted over weighted or graph-varying families. A finite test run corroborates but cannot replace the unrestricted proof. Independent validation has not been performed.

## References
1. A. Higashitani, K. Jochemko and M. Michałek, *Arithmetic aspects of symmetric edge polytopes*, arXiv:1807.07678v1, first public 2018-07-20, https://arxiv.org/abs/1807.07678.
2. A. D'Alì, E. Delucchi and M. Michałek, *Many faces of symmetric edge polytopes*, arXiv:1910.05193v1, first public 2019-10-11, https://arxiv.org/abs/1910.05193.
3. T. Chen, R. Davis and E. Korchevskaia, *Facets and facet subgraphs of symmetric edge polytopes*, arXiv:2107.12315v1, first public 2021-07-26, https://arxiv.org/abs/2107.12315.
