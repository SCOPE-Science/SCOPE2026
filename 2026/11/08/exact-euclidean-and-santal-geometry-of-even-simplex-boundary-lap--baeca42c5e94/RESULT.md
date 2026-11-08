# Exact Euclidean and Santaló geometry of even simplex-boundary Laplacian polytopes

## Finding

**Theorem.** Let \(k\ge 2\) be an integer, put \(N=2k\) and \(d=N-2\), and let \(\Delta\) be the boundary of the \((d+1)\)-simplex on \(N\) ordered vertices. Form its top combinatorial Laplacian \(L=\partial_d^{\mathsf T}\partial_d\) in the oriented-facet basis with the alternating boundary signs, and let \(P=\operatorname{conv}\{Le_i:1\le i\le N\}\) with the intrinsic Euclidean metric of its affine hull. Write \(c=\mathbf 1_N\) and \(K=P-c\).

Then \(K\), as an **isometric** Euclidean polytope, is the free sum in orthogonal \((k-1)\)-dimensional spaces of two congruent centered regular simplices, each with circumradius \(2\sqrt{k(k-1)}\). Its intrinsic dimension is \(d\), and all the following hold:

1. The volume centroid and Santaló point of \(P\) are both \(c\). Its unique John and Löwner ellipsoids are Euclidean balls centered at \(c\), respectively of radii
   \[
   r_k=\sqrt{\frac{2k}{k-1}},\qquad R_k=2\sqrt{k(k-1)}.
   \]
   All \(k^2\) facets touch the John ball; all \(2k\) vertices touch the Löwner ball. The full set of maximum-radius Euclidean inball centers is \(\{c\}\).
2. For \(X\) uniformly distributed according to intrinsic \(d\)-volume on \(P\), the covariance operator on the affine tangent space is exactly
   \[
   \operatorname{Cov}(X)=\frac{2k}{2k-1}\,I_d.
   \]
3. With Euclidean polarity in the \(d\)-space at \(c\), the exact primal and polar volumes and Santaló-Mahler volume product are
   \[
   \operatorname{Vol}_d(K)=\frac{k(2k)^{2k-2}}{(2k-2)!},\qquad
   \operatorname{Vol}_d(K^\circ)=\frac{k^{2k-1}}{(2k)^{2k-2}((k-1)!)^2},
   \]
   \[
   \boxed{\operatorname{Vol}_d(K)\operatorname{Vol}_d(K^\circ)
   =\frac{k^{2k}}{(2k-2)!((k-1)!)^2}.}
   \]
   Relative to the dimension-\(d\) simplex's Santaló volume product \(M_{\mathrm{simplex}}(d)=(d+1)^{d+1}/(d!)^2\), the exact ratio is
   \[
   \frac{M(K)}{M_{\mathrm{simplex}}(d)}
   =\frac{k^{2k}\binom{2k-2}{k-1}}{(2k-1)^{2k-1}}
   \sim \frac{e}{2\sqrt\pi}\sqrt{k}\quad(k\to\infty).
   \]

The preceding lines form one metric/affine-invariant evaluation theorem for one natural family; no extremal assertion over arbitrary cyclic polytopes is made.

## Assumptions and scope

The top Laplacian is **not** a graph Laplacian and should not be confused with a lower-dimensional Laplacian simplex. Standard Euclidean inner products are used on the \(N\) oriented top-face coordinates, but all volume, polar, inradius, and covariance quantities are evaluated intrinsically in \(\operatorname{aff}(P)\), not in \(\mathbb R^N\). The orientation convention is essential to the *canonical Euclidean realization*: reorienting individual basis faces conjugates \(L\) by a diagonal sign matrix but also changes which signed columns are used, and need not give a Euclidean-isometric convex hull. No invariance under arbitrary reorientation is asserted. The integer parameter range begins at \(k=2\), so \(d=2\); the zero-dimensional case is excluded.

The standard alternating orientation gives a sign vector \(s\in\{\pm1\}^N\) with \(s_i=(-1)^{i-1}\). There are exactly \(k\) positive and \(k\) negative entries. The kernel of the top Laplacian is the span of \(s\), and \(L=NI_N-ss^{\mathsf T}\); this is consistent with the explicit matrix from Juhnke-Kubitzke and Köhne, arXiv:2301.11602, Section 3.

## Proof

**Step 1: exact Euclidean decomposition.** Since \(s^{\mathsf T}\mathbf1_N=0\), \(L\mathbf1_N=N\mathbf1_N\), and \(c=N^{-1}\sum_iLe_i=\mathbf1_N\). The centered vertices are
\[
 v_i=Le_i-c=Ne_i-s_i s-\mathbf1_N.
\]
Let \(A=\{i:s_i=+1\}\) and \(B=\{i:s_i=-1\}\). If \(i\in A\), then \(v_i=Ne_i-2\mathbf1_A\) on the \(A\)-coordinates and is zero on the \(B\)-coordinates. If \(i\in B\), then \(v_i=Ne_i-2\mathbf1_B\) on the \(B\)-coordinates and is zero on \(A\). Thus the first \(k\) vertices form a regular simplex \(S_A\) in \(U_A=\{x:\operatorname{supp}x\subseteq A,\sum_{i\in A}x_i=0\}\), the other \(k\) form an isometric regular simplex \(S_B\) in the orthogonal \(U_B\), and \(K=\operatorname{conv}(S_A\cup S_B)\). Each \(S\) contains \(0\) in its interior; hence this is the orthogonal free sum. The squared norm of any vertex is \(N^2(1-1/k)=4k(k-1)\), and \(\dim K=2k-2\).

**Step 2: facets, spheres, uniqueness, and Santaló center.** Each regular \((k-1)\)-simplex with circumradius \(R_k\) and centroid zero has inradius \(R_k/(k-1)\); every facet opposite vertex \(v_i\) has normal \(-v_i\) and supporting constant \(R_k^2/(k-1)\). Polarity exchanges a free sum with a Cartesian product:
\[
 K^\circ=S_A^\circ\times S_B^\circ.
\]
The polar of each regular simplex has \(k\) vertices of norm \((k-1)/R_k\). Hence every one of the \(k^2\) vertices of \(K^\circ\) has norm \(\sqrt2(k-1)/R_k\); these are exactly the \(k^2\) facet normals (suitably rescaled) of \(K\). Thus the ball about zero tangent to every facet has radius \(R_k/(\sqrt2(k-1))=\sqrt{2k/(k-1)}\).

Coordinate permutations within \(A\) and \(B\), together with swapping the two blocks, act by Euclidean symmetries of \(K\). The only fixed vector is zero; every invariant positive-definite quadratic form on \(U_A\oplus U_B\) is scalar, since the two standard permutation modules are irreducible and the block swap equates their scalars. The unique maximal-volume inscribed ellipsoid (John) and unique minimal-volume enclosing ellipsoid (Löwner) must therefore be centered spherical ellipsoids. Their radii are respectively the least facet distance and the largest vertex norm, already computed. The unique Santaló point is fixed by the same symmetry group, so it is zero for \(K\). The uniform-volume centroid is also fixed by the group and equals zero. Since the origin lies in the strict interior of the convex hull of the \(k^2\) outward unit facet normals (their group average is zero and their span is all \(U_A\oplus U_B\)), no nonzero center admits another radius-\(r_k\) ball, establishing uniqueness of the incenter.

**Step 3: intrinsic covariance.** Write \(m=k-1\), so \(d=2m\). Each facet of \(K\) is the join of a facet of \(S_A\) and a facet of \(S_B\). Coning every facet to the interior point zero partitions \(K\), up to measure-zero overlaps, into \(k^2\) equal-volume \(d\)-simplices. The \((a,b)\)-simplex has vertices zero and all \(v_i\) except the two vertices \(v_a\in S_A\), \(v_b\in S_B\). Uniform integration on a \(d\)-simplex with vertices \(0,w_1,\ldots,w_d\) gives
\[
 \mathbb E[XX^{\mathsf T}]=\frac{\sum_jw_jw_j^{\mathsf T}+(\sum_jw_j)(\sum_jw_j)^{\mathsf T}}{(d+1)(d+2)}.
\]
Averaging over \((a,b)\) and using \(\sum_{i\in A}v_i=\sum_{i\in B}v_i=0\), the numerator becomes \(\sum_{i=1}^{N}v_iv_i^{\mathsf T}=N^2\Pi\), where \(\Pi\) is orthogonal projection onto \(U_A\oplus U_B\). Indeed, on each block \(\sum_{i\in A}v_iv_i^{\mathsf T}=N^2(I_A-\mathbf1_A\mathbf1_A^{\mathsf T}/k)\), with an analogous identity on \(B\). Since the overall centroid is zero, \(\operatorname{Cov}(X)=N^2/((N-1)N)\,I_d=N/(N-1)\,I_d\).

**Step 4: exact volumes and the comparison.** The intrinsic \(m\)-volume of either centered regular simplex with vertices \(N(e_i-\mathbf1_A/k)\) equals \(N^m\sqrt{k}/m!\). The Euclidean free-sum volume identity, obtained by coning the product's facet-simplex decomposition, is
\[
 \operatorname{Vol}_{2m}(S_A\oplus_1 S_B)=\frac{(m!)^2}{(2m)!}\operatorname{Vol}_m(S_A)\operatorname{Vol}_m(S_B)=\frac{kN^{2m}}{(2m)!}.
\]
The centered regular simplex's volume product in dimension \(m\) is \(k^k/(m!)^2\); hence its polar volume is \(k^{k-1/2}/(N^m m!)\). Because \(K^\circ=S_A^\circ\times S_B^\circ\) orthogonally, its volume is the square of that expression. Multiplication gives the claimed Santaló volume product. Finally division by \((d+1)^{d+1}/(d!)^2\) yields the exact central-binomial ratio; Stirling's formula \(\binom{2k-2}{k-1}\sim4^{k-1}/\sqrt{\pi(k-1)}\) and \((1-1/(2k))^{-(2k-1)}\to e\) yield the stated asymptotic. Every step applies to all integers \(k\ge2\).

## Verification

The standalone file `checker.py` reconstructs the alternating top-Laplacian matrices; checks \(L^2=NL\); uses orthonormal affine coordinates; independently computes the convex hull of the vertices and of its polar facet normals; compares intrinsic primal/polar volumes, all \(k^2\) facet distances, and vertex radii for \(k=2,3,4,5\). It separately evaluates the actual simplicial second-moment formula in every conical facet-simplex and compares it with the claimed scalar covariance. The computation also checks the unrelated odd-parity simplex covariance formula as a normalization control. All tests pass with printed marker `LAPLACIAN_METRIC_FINITE_CHECKS_PASSED` (Python with NumPy and SciPy). The proof above, not the finite tests, establishes the all-dimensional theorem.

## Relationship to prior work

Juhnke-Kubitzke and Köhne [1] introduce top Laplacian polytopes of simplicial complexes; for boundaries of simplices, their Theorem 3.2 gives the alternating matrix, Theorem 5.3 gives the full even-dimensional facet description, Theorem 5.4 gives the cyclic-polytope combinatorial type, and Corollary 6.7 determines normalized lattice volume. These are prior results. This theorem makes the canonical **intrinsic Euclidean** free-sum geometry explicit and uses it to evaluate Santaló-Mahler product, John/Löwner metric geometry and all interior-volume covariance directions. The intrinsic volume formula itself is not claimed as new, because it is consistent with their known lattice-volume result after the appropriate affine-lattice covolume conversion. Braun and Meyer [2] introduce graph Laplacian simplices, which are a distinct, earlier construction; their results do not cover the top-dimensional simplex-boundary polytope here.

The elementary simplex polar-volume identity and general free-sum/product polarity are standard and are not themselves claimed as original. The contribution is the evaluated metric profile for the specific Laplacian family together with the asymptotic comparison to the simplex benchmark.

## Limitations

The theorem covers the standard alternating orientation of top Laplacians of boundaries of simplices only in the **even boundary-dimension** regime. Arbitrary reorientation of top-face bases may change the Euclidean realization. For odd boundary dimension the polytope is a simplex with a different affine span and generally anisotropic Euclidean covariance; no all-parity John/Löwner theorem is asserted. This result does not solve the paper's questions on Ehrhart roots, unimodular triangulations or arbitrary complexes. Historical novelty remains provisional pending external expert literature review; an equivalent isometric free-sum interpretation in independent work cannot be ruled out. Numerical tests cover only the stated finite dimensions and do not constitute exhaustive prior-art proof or validation of an infinite-dimensional family.

## References

1. M. Juhnke-Kubitzke and D. Köhne, *Laplacian polytopes of simplicial complexes*, arXiv:2301.11602, first posted 2023-01-27, https://arxiv.org/abs/2301.11602. Sections 3–7, especially Theorem 3.2 and Theorems 5.3–5.4.
2. B. Braun and M. Meyer, *Laplacian Simplices*, arXiv:1706.07085, 2017-06-21, https://arxiv.org/abs/1706.07085. Sections 1–3, 4–6.
