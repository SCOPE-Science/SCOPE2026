# Sharp contact-orbit transitions for ratio-bounded simplex ellipsoids

## Finding
Fix an integer \(m\ge4\) and a real ratio \(c>1\). In the Euclidean affine hyperplane \(H_m=\{x\in\mathbb R^m:\sum_i x_i=1\}\), define the ratio-bounded central simplex polytope
\[
P_{m,c}=\{x\in H_m:x_i\le c x_j\text{ for all }i\ne j\},\qquad b_m=m^{-1}(1,\ldots,1).
\]
Both its unique maximum-volume inscribed ellipsoid and unique minimum-volume containing ellipsoid are Euclidean balls centered at \(b_m\). With \(a=c-1\), their respective radii \(r\) and \(R\) satisfy
\[
\boxed{r^2=\frac{a^2}{m^2(1+c^2-a^2/m)},\qquad R^2=\max_{1\le k\le m-1}\frac{a^2k(m-k)}{m(m+ka)^2}.}
\]
Set \(h=\lfloor m/2\rfloor\) and define the strictly decreasing thresholds
\[
\boxed{\gamma_k=\sqrt{\frac{(m-k)(m-k-1)}{k(k+1)}}\quad(1\le k<h),\qquad\gamma_0=+\infty,\ \gamma_h=1.}
\]
For each \(1\le k\le h\), whenever \(\gamma_k<c<\gamma_{k-1}\), **exactly** the \(\binom mk\) vertices with \(k\) larger barycentric coordinates contact the enclosing sphere; at \(c=\gamma_k\) (\(1\le k<h\)), precisely the two adjacent cardinality classes \(k\) and \(k+1\) contact, with total cardinality \(\binom mk+\binom m{k+1}\). No nonvertex boundary points contact the enclosing sphere. All \(m(m-1)\) facets contact the inscribed ball, for every \(c>1\).

The sharp ellipsoid-radius ratio is **strictly increasing** through the complete homotopy \(c>1\), despite the successive contact-orbit switches, and obeys
\[
\boxed{\lim_{c\downarrow1}\frac Rr=\sqrt{\frac{2h(m-h)}m},\qquad \lim_{c\to\infty}\frac Rr=m-1.}
\]
The special case \(c=2\) and its dimension-modulo-three contact classification were known; the contribution here is the sharp full real-parameter phase diagram and the global monotonic radius-ratio interpolation.

## Assumptions and scope
The simplex has vertices \(e_1,\ldots,e_m\), each pair at Euclidean distance \(\sqrt2\), so the intrinsic dimension is \(m-1\). All stated distances refer to the Euclidean metric induced on \(H_m\); they are not the numerical semiaxes in arbitrary nonregular Euclidean simplices. An arbitrary affine simplex inherits the corresponding John and Löwner ellipsoids by its unique affine map from the coordinate simplex. The definitions require \(c>1\), with the endpoint limits taken only after forming the ratio. Every feasible point has positive coordinates: if some \(x_j\le0\), all \(x_i\le c x_j\le0\), contradicting \(\sum_i x_i=1\).

## Proof
**1. Symmetry forces extremal balls.** The polytope is compact, full-dimensional in \(H_m\), and invariant under all coordinate permutations. The John and Löwner ellipsoids exist and are unique. Each is permutation-invariant; therefore its center is the unique fixed point \(b_m\), and its positive-definite quadratic form on the sum-zero subspace \(E_m\) commutes with the standard irreducible real permutation representation. Every invariant symmetric form there is scalar: writing its full matrix as one diagonal value and one off-diagonal value, its restriction to \(E_m\) is a scalar multiple of the Euclidean form. Thus both ellipsoids are centered Euclidean balls. Equivalently, the contact identities at the end of this proof directly certify their ellipsoid optimality.

**2. Inscribed ball and facet contacts.** Write \(\Pi=I-\mathbf1\mathbf1^{\mathsf T}/m\). Each ordered-pair constraint \(x_i-cx_j\le0\), after putting \(x=b_m+u\), becomes
\[
\langle \Pi(e_i-ce_j),u\rangle\le \frac{c-1}{m},\qquad
\|\Pi(e_i-ce_j)\|^2=1+c^2-\frac{(c-1)^2}{m}.
\]
Its supporting hyperplane has exactly the stated distance \(r\) from \(b_m\). Every inequality is a genuine facet: choose an unnormalized positive coordinate pattern with \(x_j=1\), \(x_i=c\), and each other coordinate strictly between \(1\) and \(c\), then normalize by the total sum. Only the designated ordered-pair inequality is tight. The centered ball of radius \(r\) lies in every halfspace and touches each facet; by Step 1 it is the John ellipsoid. Because distinct facet-normal vectors are not parallel with the same outward orientation, each tangent point lies in the relative interior of its facet.

**3. The complete vertex shell spectrum.** For each nonempty proper \(S\subset\{1,\ldots,m\}\), with \(k=|S|\), let
\[
D_k=m+k(c-1),\qquad (v_S)_i=\begin{cases}c/D_k,&i\in S,\\1/D_k,&i\notin S.\end{cases}
\]
All these points are vertices: the equality constraints \(x_i=cx_j\) for \(i\in S\), \(j\notin S\), together with coordinate sum one, determine exactly \(v_S\). Conversely, at any vertex at least one such constraint must be tight. Writing the minimum coordinate as \(t>0\), equality can only occur between a maximum \(ct\) and a minimum \(t\). If any intermediate coordinate were present, varying that coordinate and the common extreme scale slightly, while preserving the sum, would give a nontrivial feasible segment. Thus every vertex is some \(v_S\); this general real-parameter vertex description is already established in prior ratio-bounded polytope work.

The distance of \(v_S\) from the barycenter is exactly
\[
\|v_S-b_m\|^2=\frac{(c-1)^2 k(m-k)}{mD_k^2}=:\rho_k^2.
\]
The squared norm is strictly convex along any nonconstant segment; a nonvertex convex combination cannot attain its maximum over the polytope. Consequently the containing radius is \(R^2=\max_k\rho_k^2\), and contacts are exactly the maximizing vertex orbits.

**4. All contact transitions, with no hidden ties.** If \(k<m/2\), then \(\rho_k^2>\rho_{m-k}^2\) for \(c>1\), because the two numerators agree and \(D_k<D_{m-k}\). Hence only \(1\le k\le h\) can maximize. Introduce \(q_k=(m-k)/k\), a strictly decreasing sequence, and factor out the common positive \((c-1)^2/m\). The objective becomes
\[
F_k(c)=\frac{q_k}{(c+q_k)^2}.
\]
For \(q>q'>0\), direct cross multiplication, or taking positive square roots, gives
\[
\frac{q}{(c+q)^2}=\frac{q'}{(c+q')^2}
\quad\Longleftrightarrow\quad c=\sqrt{qq'}.
\]
For \(c\) below that threshold the smaller \(q'\) has larger \(F\), and above it the larger \(q\) wins. Adjacent thresholds are precisely \(\sqrt{q_kq_{k+1}}=\gamma_k\), and these decrease strictly with \(k\). More globally, if \(\gamma_k<c<\gamma_{k-1}\), then for any \(j<k\) we have \(c<\gamma_{k-1}\le\sqrt{q_jq_k}\), so shell \(k\) beats shell \(j\). For any \(j>k\), we have \(c>\gamma_k\ge\sqrt{q_kq_j}\), so shell \(k\) again wins. At \(c=\gamma_k\), the same strict comparisons exclude all other shells, so only \(k\) and \(k+1\) tie. This proves every open regime, excludes skipped indices or triple ties, and gives all exact contact counts. The arithmetic \(\gamma_{h-1}>1\) follows from \(q_{h-1}>q_h\ge1\).

**5. Strictly increasing ratio and limiting values.** For \(1\le k\le h\), put \(B=1-1/m\) and \(a=c-1\). The ratio of the \(k\)-th shell radius to the inradius is
\[
T_k(a)=\frac{\sqrt{mk(m-k)}\sqrt{2+2a+Ba^2}}{m+ka}.
\]
Its logarithmic derivative has the sign of
\[
(m-2k)+(m-1-k)a>0\qquad(a>0,\ 1\le k\le h,\ m\ge4).
\]
All candidate ratios increase strictly, hence their finite maximum \(R/r\) increases strictly. As \(a\downarrow0\), the largest shell index approaches \(h\), producing the first limit. As \(a\to\infty\), the largest shell index is \(1\), and the ratio tends to \(m-1\). These are limiting values only: neither endpoint is part of the stated parameter domain.

**6. Optional direct optimality certificates.** Normalize each facet normal \(w_{ij}=\Pi(e_i-ce_j)/\|\Pi(e_i-ce_j)\|\). By permutation invariance, \(\sum_{i\ne j}w_{ij}=0\) and \(\sum_{i\ne j}w_{ij}w_{ij}^{\mathsf T}=m\Pi\), so weights \(1/m\) on the tangent normals give the classical John contact identity. For any maximizing orbit \(\mathcal O_k=\{v_S:|S|=k\}\), normalize \(z_S=(v_S-b_m)/R\). Then \(\sum_{\mathcal O_k}z_S=0\) and \(\sum_{\mathcal O_k}z_Sz_S^{\mathsf T}=\binom mk\Pi/(m-1)\). Weights \((m-1)/\binom mk\) give the corresponding Löwner contact identity, including at ties (either contacting orbit alone suffices). Thus no appeal to numerical optimization is required.

## Verification
The standalone `verify.py` runs exact rational barycentric checks, exact shell-distance identities, finite threshold and ratio-monotonicity comparisons, and an **independent** halfspace-intersection vertex extraction for several small dimensions. Run `python3 verify.py` with Python 3, NumPy and SciPy; rational and scalar checks use the standard library. A complete test run passed **35,495 finite assertions**, including independent H-polytope vertex extraction through \(m=7\). This finite verification supports but does not replace the general arguments in Proof Steps 1–6.

## Relationship to prior work
Kazakov's 2026 simplex edge-trisection construction corresponds to \(c=2\); its original paper provides volume and combinatorial data but does not classify ellipsoid contact transitions as the edge ratio varies. The published 2026 result *Exact John and Löwner ellipsoids of the trisected-simplex central polytope* already determines both Euclidean radii and the dimension-residue contact orbit **for \(c=2\)**. The 2026 result *Exact polar volumes of ratio-bounded simplex central polytopes* establishes the complete vertex shells and dual volumes **for all \(c>1\)** but does not provide an ellipsoid phase classification. The claimed increment here is the exact sequence of \(h-1\) real thresholds, all contact counts at and between them, the radius formula throughout, and strictly increasing global John-to-Löwner radius ratio. The source's \(c=2\) specialization is therefore explicitly prior, not independently novel.

## Limitations
The claim does not evaluate Euclidean radii after an arbitrary nonorthogonal affine deformation of the simplex; its extremal ellipsoids transform by the affine map. The theorem does not address independently varied pairwise ratio bounds, lattice/Ehrhart questions, or volume of the convex body. Earlier publications may contain equivalent all-parameter contact diagrams under different names; literature search cannot certify historical priority. Independent audit has not been performed.

## References
[1] Yu. V. Kazakov, *Generalization of Marion's Theorem: Volumes of Central Polytopes Obtained by Trisecting the Edges of Simplices*, arXiv:2606.02087v1, first public 2026-06-01, https://arxiv.org/abs/2606.02087.

[2] *Exact John and Löwner ellipsoids of the trisected-simplex central polytope*, published-finding corpus public research record, 2026-10-25, identifier e5eca0d45d36 (\(c=2\) case).

[3] *Exact polar volumes of ratio-bounded simplex central polytopes*, published-finding corpus public research record, 2026-11-08, identifier d79d6553a85b (all-real-ratio polar volume and vertex list).

[4] P. M. Gruber and F. E. Schuster, *An arithmetic proof of John's ellipsoid theorem*, arXiv:1207.7246 (standard extremal ellipsoid contact criterion), https://arxiv.org/abs/1207.7246.
