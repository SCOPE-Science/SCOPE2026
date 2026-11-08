# The crepant small contraction of an unexpected toric Richardson fourfold

## Finding
Consider the closed Richardson fourfold \(X=\overline R_{1324,4231}\) in the complex complete flag variety \(\operatorname{Fl}(4)\), with the four-dimensional torus action and moment polytope described in Example 5.2 of Gorsky–Kim–Sherman-Bennett [1]. Then \(X\) is a smooth weak Fano but non-Fano toric variety, with \(\operatorname{Pic}(X)\cong\mathbb Z^4\). Its anticanonical class is divisible by exactly two in the Picard group. Writing \(-K_X=2L\), one has \(L^4=20\) and \((-K_X)^4=320\).

The semiample, big divisor \(L\) induces a crepant small toric morphism \(\phi:X\to Y\), where \(Y\) is a normal Gorenstein Fano fourfold. The exceptional locus is exactly two disjoint surfaces, each isomorphic to \(\mathbb P^1\times\mathbb P^1\). Each is contracted along a ruling to a projective line. The two image lines are disjoint and constitute the entire singular locus of \(Y\). Étale-locally along either line the singularity is the product of an ordinary three-dimensional double point \(uv-wz=0\) with a smooth one-dimensional factor. Thus \(\phi\) is a small crepant resolution of this explicit toric Fano fourfold.

## Assumptions and scope
Work over \(\mathbb C\). The toric identification of the stated Richardson variety and its four-character-lattice moment polytope are supplied by [1]; the assertions here concern its intrinsic toric birational geometry, not an extension to all Richardson varieties. Use the lattice \(M=\mathbb Z^4\) and its dual \(N\), and write the moment polytope as the Minkowski sum of the convex hulls of
\[
\begin{aligned}
P_1:&\ (0,1,1,0),(0,1,0,0),(1,0,0,0),(0,0,0,0),\\
P_2:&\ (1,0,1,0),(0,0,1,0),(1,0,0,0),(0,0,0,0),\\
P_3:&\ (1,0,0,1),(0,0,0,1),(0,0,1,0),(0,0,0,0).
\end{aligned}
\]
All claims of smoothness, divisor positivity, intersection numbers, exceptional strata and singularities refer to the normal projective toric model with this fan.

## Proof
**Recovering the smooth fan.** Integer convex-hull and half-space calculations give exactly eight primitive inward facet normals, in the following order:
\[
\begin{aligned}
r_0&=(1,0,0,0),&r_1&=(0,1,0,0),\\
r_2&=(0,0,1,0),&r_3&=(0,0,0,1),\\
r_4&=(0,0,0,-1),&r_5&=(0,1,-1,-1),\\
r_6&=(0,-1,0,0),&r_7&=(-1,-1,0,1).
\end{aligned}
\]
The support inequalities \(\langle u,r_i\rangle\ge b_i\) have right sides \(b=(0,0,0,0,-1,-2,-1,-2)\). There are precisely sixteen vertices, one for each choice of one ray in each of the four pairs \((0,7),(1,6),(2,5),(3,4)\). At each vertex its four active primitive normals have determinant \(\pm1\), so \(X\) is smooth. Its Picard rank is the number of rays minus dimension, namely \(8-4=4\).

**Weak Fano, non-Fano, and index.** These four pairs are exactly the primitive collections. Their primitive relations are
\[
 r_0+r_7=r_6+r_3,\qquad r_2+r_5=r_1+r_4,\qquad r_1+r_6=0,\qquad r_3+r_4=0.
\]
The primitive degrees are \(0,0,2,2\); the toric primitive-collection criterion [4] shows that \(-K_X\) is nef but not ample. The polytope \(Q=\{u:\langle u,r_i\rangle\ge-1\text{ for all }i\}\) is four-dimensional (it contains the origin in its interior), hence \(-K_X\) is big. Let \(D_i\) be the invariant divisor for \(r_i\). For \(m=(1,1,1,1)\in M\), the coefficients \(1-\langle m,r_i\rangle\) are \((0,0,0,0,2,2,2,2)\). Therefore \(-K_X\sim2L\) for \(L=D_4+D_5+D_6+D_7\). If \(-K_X\) were divisible by an integer \(q>2\), then its coefficients at opposite rays \(r_3\) and \(r_4=-r_3\) would sum to \(2\) modulo \(q\), impossible. Thus the index is exactly \(2\).

**The contraction and its singular target.** Enumerating the vertices of \(Q\) yields exactly twelve integral vertices. The sixteen maximal cones of the smooth fan coalesce into eight singleton cones and four pairs under the normal fan of \(Q\). The four merged pairs have common walls respectively indexed by \((0,1,4),(1,4,7),(2,3,6),(3,5,6)\). They arise from just the two square circuits \(r_2+r_5=r_1+r_4\) and \(r_0+r_7=r_6+r_3\). Accordingly the exceptional locus of the induced toric contraction is the union of \(V(\langle r_1,r_4\rangle)\) and \(V(\langle r_3,r_6\rangle)\). Quotienting the star fan of either two-dimensional cone leaves four rays \((\pm1,0),(0,\pm1)\), so each invariant surface is \(\mathbb P^1\times\mathbb P^1\). The two surfaces are disjoint, since no maximal cone contains both generating pairs. Each is mapped along one ruling to the one-dimensional orbit closure corresponding to the associated three-dimensional square cone, hence to \(\mathbb P^1\). All eight rays survive in the coarser fan, so no divisor is contracted, and the contraction is small.

Each square cone has four primitive rays satisfying one parallelogram relation with unit coefficients; three of these rays form a basis of its rank-three lattice. Its affine toric variety is therefore the ordinary double point \(uv-wz=0\). The two four-dimensional cones over its endpoints split off a primitive complementary ray, giving a product with \(\mathbb A^1\). Every other maximal cone remains unimodular; hence the reduced singular locus of \(Y\) is precisely the two disjoint image \(\mathbb P^1\)'s. The lattice vertices of the anticanonical polytope give a Cartier ample anticanonical class on the target; furthermore \(K_X=\phi^*K_Y\), so the small resolution is crepant.

**Degree computation.** The polytope of \(L\) is obtained by translating and halving \(Q\): \(Q_L=\tfrac12(Q+(1,1,1,1))\). Its twelve vertices are integral. The exact lattice-point counts in its first five dilations are
\[
\bigl(\#(tQ_L\cap M)\bigr)_{t=0}^4=(1,14,69,216,525).
\]
Ehrhart's theorem says the fourth forward difference is \(4!\operatorname{Vol}(Q_L)=L^4\). Direct subtraction yields \(L^4=525-4(216)+6(69)-4(14)+1=20\), and \((-K_X)^4=2^4L^4=320\).

## Verification
The accompanying standalone Python program `richardson_weak_fano_check.py` uses only the standard library and rational-integer arithmetic. Running `python3 richardson_weak_fano_check.py` checks that the Minkowski sum has 34 distinct vertex sums, computes all integral vertices and supporting facets, verifies sixteen unimodular cones, the primitive relations and the twelve-vertex anticanonical contraction, the two four-cone exceptional stars, and exact Ehrhart counts through degree four. Its exact checks corroborate the combinatorial inputs to the written toric argument; they do not by themselves prove the general toric correspondence or the local double-point normal form.

## Relationship to prior work
Gorsky–Kim–Sherman-Bennett [1] identify this unexpected Richardson variety as toric and explicitly construct the moment polytope; those results are not claimed as new here. Gorsky–Kim–Scroggin–Simental [2] discuss the earlier torus-parameterization example. Lee–Masuda–Park [3] treat a separate Catalan-type class of toric Richardson varieties. Suyama [4] proves general positivity criteria for Bott manifolds, which already imply the *method* for the weak-Fano check after a fan is known. The specific contraction, its two disjoint conifold singular curves, Cartier index, and exact intersection degree for this unexpected fourfold are the additional conclusions. No assertion of exhaustive historical priority is made.

## Limitations
The claims concern this single naturally distinguished fourfold and the normal anticanonical model, rather than all toric Richardson varieties. The defining polytope and general toric positivity/geometry results are previously known. The finite exact checker verifies the required input computations; the geometric interpretation uses standard toric fan–orbit and divisor theory. Independent mathematical audit and exhaustive historical-priority confirmation have not been performed.

## References
[1] E. Gorsky, S. Kim, M. Sherman-Bennett, *Unexpected toric Richardson varieties*, arXiv:2603.29260v1 (2026-03-31), especially Example 5.2, https://arxiv.org/abs/2603.29260.

[2] E. Gorsky, S. Kim, M. Scroggin, J. Simental, *Splicing braid varieties*, arXiv:2505.08211v1 (2025-05-13), especially Example 5.17, https://arxiv.org/abs/2505.08211.

[3] J. Lee, M. Masuda, S. Park, *Toric Richardson varieties of Catalan type and Wedderburn–Etherington numbers*, arXiv:2105.12274, https://arxiv.org/abs/2105.12274.

[4] Y. Suyama, *Fano generalized Bott manifolds*, arXiv:1811.06209 (2018-11-15), especially Theorems 1 and 4, https://arxiv.org/abs/1811.06209.
