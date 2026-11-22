# Forty terminal points and a stringy Hodge coincidence for a Heisenberg Kummer fourfold

## Finding
Let \(X\subset\mathbb P^8_{\mathbb C}\) be a smooth residual fourfold in the general Heisenberg-invariant cubic-web family of Giovenzana–Rojas–Song (arXiv:2611.16593v1). It is an irreducible holomorphic symplectic fourfold of generalized Kummer type. Let \(G\cong(\mathbb Z/3\mathbb Z)^4\) be its canonical level-three translation subgroup, and let \(Y=X/G\) denote the coarse projective quotient.

Then \(Y\) has precisely **40 isolated singular points**, all analytically of cyclic type \(\frac13(1,1,2,2)\). They are Gorenstein, \(\mathbb Q\)-factorial, and terminal; in particular \(Y\) has **no crepant resolution**. The rational Poincaré polynomial and Euler characteristic are
\[
P_Y(t)=1+7t^2+8t^3+28t^4+8t^5+7t^6+t^8,
\qquad\chi_{\mathrm{top}}(Y)=28.
\]
Moreover \(\pi_1(Y)=1\) while \(\pi_1(Y^{\mathrm{reg}})\cong G\). The unique middle Hodge row of the quotient is
\[
(h^{4,0},h^{3,1},h^{2,2},h^{1,3},h^{0,4})(Y)=(1,5,16,5,1).
\]
All other rational Hodge numbers are determined by the following nonzero entries (and Hodge symmetry): \(h^{0,0}=h^{4,4}=1\), \(h^{2,0}=h^{0,2}=h^{4,2}=h^{2,4}=1\), \(h^{1,1}=h^{3,3}=5\), and \(h^{2,1}=h^{1,2}=h^{3,2}=h^{2,3}=4\). In particular, if \(E(-;u,v)\) denotes the Hodge–Deligne polynomial, then the **stringy** Hodge–Deligne polynomial satisfies
\[
\boxed{E_{\mathrm{st}}(Y;u,v)=E(Y;u,v)+80u^2v^2=E(X;u,v).}
\]
The stringy Euler characteristic equals \(108\), despite the absence of a crepant resolution. These are exact equalities for every smooth member of the stated family, not numerical evidence from isolated examples.

## Assumptions and scope
Work over \(\mathbb C\). The family, its smooth members, the action of \(G\), and the fixed-point theorem are the objects of [1], specifically its main theorem, Section 2.2 and Section 5. The input from [1] is that the nonfree locus on \(X\) consists of exactly \(1080\) points, each with stabilizer of order \(3\), and that these are all nonfree points. It also gives the characteristically defined subgroup \(G=T(X)\) in the group of automorphisms acting trivially on second cohomology. The fixed loci of distinct order-three subgroups are disjoint because a point is not fixed by a rank-two subgroup.

Write \(X^g\) for the fixed locus of \(g\in G\). For every \(g\ne1\), \(X^g\) is a set of exactly \(27\) points: in the standard generalized Kummer model they are length-three subschemes with support \(\{x,x+y,x+2y\}\), where the line \(\langle y\rangle\subset A[3]\) corresponds to \(\langle g\rangle\), and \(x\) ranges over \(A[3]/\langle y\rangle\) (source [1], Section 5). The same holds across the family as asserted in [1]. The known generalized Kummer cohomology and the translation action on odd cohomology used below are from [2]. No singular residual fibers and no characteristic-three reductions are claimed.

## Proof
**1. Orbits and local singularities.** The group \(G\) has \((3^4-1)/(3-1)=40\) subgroups of order \(3\). Since each of the \(1080\) nonfree points has a unique such stabilizer \(H\), its \(G\)-orbit has size \(|G|/|H|=27\). Thus the singular support of \(Y\) consists of \(1080/27=40\) points, and there are no other candidates. For any point with stabilizer \(H\), finite-group holomorphic linearization identifies the analytic quotient germ with the linear action of \(H\) on \(T_pX\). The fixed point is isolated, so no eigenvalue of its generator is one. Because the action is symplectic, its eigenvalues occur in reciprocal pairs; for a primitive cubic root \(\zeta\), they must be \(\zeta,\zeta,\zeta^2,\zeta^2\). Hence the cyclic type is \(\frac13(1,1,2,2)\). Both nonidentity elements have Reid–Tai age \(2\). The quotient is isolated Gorenstein and terminal (ages strictly greater than one), and it is \(\mathbb Q\)-factorial as a small finite cyclic quotient. A nontrivial \(H\)-action has no symplectic reflections, so Verbitsky's necessary condition [4] excludes a symplectic or crepant resolution of this germ. Any global crepant resolution would resolve it crepantly, which is impossible.

**2. Odd and second cohomology under \(G\).** The rational Betti numbers of a generalized Kummer fourfold are \((b_0,b_1,b_2,b_3,b_4,b_5,b_6,b_7,b_8)=(1,0,7,8,108,8,7,0,1)\), hence \(\chi(X)=108\). By definition of \(T(X)\), \(G\) acts trivially on \(H^2(X,\mathbb Q)\). Kapfer–Menet [2], Corollary 6.3, identifies the natural translation action on \(H^3(K_2(A),\mathbb Z)\cong H^1(A,\mathbb Z)\oplus H^3(A,\mathbb Z)\) as the identity. This extends to the canonical \(T(X)\)-action throughout the Kummer deformation class: the characteristic subgroup \(T(X)\) forms a sub-local-system of the automorphism group on connected marked deformations, as recalled explicitly in [1], Section 2.2, and its finite-order cohomological representation is locally constant. Thus \(G\) fixes \(H^3(X,\mathbb Q)\), and by Poincaré duality also \(H^5\) and \(H^6\); all other Betti spaces except \(H^4\) are fixed as well.

**3. Middle cohomology.** For each \(g\ne1\), the topological Lefschetz formula gives \(27=\chi(X^g)=\sum_{i=0}^8(-1)^i\operatorname{tr}(g\mid H^i(X,\mathbb Q))\). The already determined terms outside degree four sum to \(1+7-8-8+7+1=0\), hence \(\operatorname{tr}(g\mid H^4)=27\). Averaging characters,
\[
\dim H^4(X,\mathbb Q)^G=\frac{108+80\cdot27}{81}=28.
\]
Equivalently, as rational \(G\)-representations, \(H^4(X,\mathbb Q)\cong\mathbb Q[G]\oplus\mathbb Q^{27}\); this is an isomorphism of representations, not an assertion about integral lattice splitting. For any finite group on a smooth compact variety, rational cohomology of the coarse quotient is the invariant rational cohomology. The displayed Poincaré polynomial and ordinary Euler characteristic follow immediately.

**4. Hodge and stringy calculations.** The 28-dimensional image of \(\operatorname{Sym}^2H^2(X,\mathbb Q)\longrightarrow H^4(X,\mathbb Q)\) is injective by the generalized Kummer cup-product calculation in [2], Section 6.4, and is pointwise fixed by \(G\). Thus it equals the whole invariant fourth cohomology. Its Hodge decomposition follows from \((h^{2,0},h^{1,1},h^{0,2})=(1,5,1)\) and has Hodge row \((1,5,16,5,1)\). The remaining 80-dimensional quotient of the fourth cohomology is purely of Hodge type \((2,2)\), since the holomorphic \(H^{4,0}\), \(H^{3,1}\), \(H^{1,3}\), and \(H^{0,4}\) groups all lie in the symmetric-square sector. The odd Hodge numbers follow from the Hodge-theoretic version of [2], Corollary 6.3, with the Tate twist on the \(H^1\) summand, or from the standard generalized Kummer Hodge diamond.

For each \(g\ne1\), \(X^g\) consists of 27 points and \(G/\langle g\rangle\) acts freely on that set, hence transitively: \(X^g/G\) is one point. The age is \(2\) at each such point. The global-quotient (Batyrev) orbifold formula [5] therefore adds exactly one \((uv)^2\) term for each of the 80 nonidentity elements. Consequently \(E_{\mathrm{st}}(Y)=E(Y)+80u^2v^2\), and this agrees with \(E(X)\) because precisely those 80 \((2,2)\)-classes disappear from invariant cohomology. Evaluating \(u=v=1\) yields \(\chi_{\mathrm{st}}(Y)=108\).

**5. Fundamental groups.** Removing finitely many points from the simply connected real eight-dimensional manifold \(X\) leaves a simply connected manifold. The action on \(X\setminus\Gamma\) is free, so \(\pi_1(Y^{\mathrm{reg}})\cong G\). Armstrong's orbit-space theorem [6] says \(\pi_1(Y)\) is \(G\) modulo the normal subgroup generated by elements with fixed points. Every nonidentity element fixes 27 points, so \(\pi_1(Y)=1\).

## Verification
`CHECK.py` provides an exact finite-group reconstruction using vectors of \(\mathbb F_3^4\). It enumerates all 40 order-three subgroups, their 27 cosets, all 1080 point labels, all fixed and jointly fixed point counts, and the ordinary and orbifold Euler averages. It also checks the invariants and Hodge totals used in the formulas. The checker was run and its four assertions groups passed. These finite computations verify the incidence and arithmetic implications of the geometric inputs; they do **not** establish the actual 1080-point theorem, cohomological local-system theorem, analytic linearization or stringy-Hodge formula, which are justified separately in the proof and cited primary sources.

For a hand check: \(40\cdot27=1080\), \(\chi(Y)=(108+80\cdot27)/81=28\), and the stringy Euler commuting-pair average is \((108+40\cdot8\cdot27)/81=108\). The absence of a crepant resolution is a mathematical consequence of the nonreflection local analytic action, not inferred from a computational timeout.

## Relationship to prior work
The 2026 construction [1] proves existence of the family, canonical \(G\)-action and the 1080 nonfree points with order-three stabilizers. Those are inputs, **not** new claims here. The 2018 work [2] computes the integral cohomology of generalized Kummer fourfolds, the structure of the middle cohomology and translation action on third cohomology; the representation decomposition is an explicit rational consequence of these inputs and the Lefschetz calculation, not a new computation of the covering fourfold itself. Bertini–Grossi–Mauri–Mazzon [3] study terminalizations of *strictly canonical* quotients with codimension-two fixed loci, thus do not assert the present already-terminal order-three translation quotient's 40 isolated points or full Hodge and stringy equality. Verbitsky's nonresolution criterion [4], Batyrev's stringy formalism [5], and Armstrong's fundamental-group theorem [6] are credited as standard inputs.

The contribution is the **complete singularity, cohomological, and stringy accounting for the natural quotient of this new geometric family**, particularly the juxtaposition \(E_{\mathrm{st}}(X/G)=E(X)\) with **no** crepant resolution. The explicit computation is an extension/application of known Kummer cohomology and recent fixed-locus geometry; no general theory of symplectic quotients is claimed.

## Limitations
The assertion is conditional on smoothness and on the canonical symplectic \(G\)-action of [1]. It does not apply to singular residual fibers, to larger semidirect-product groups, or to characteristic three. The cohomological decomposition is rational; integral quotient cohomology, torsion, cup-product ring and intersection cohomology of nonisolated variants are not calculated. The stated stringy polynomial is not the Hodge polynomial of a nonexistent smooth crepant model. The historical-priority search included the primary 2026 paper and the strongest relevant 2018 and 2025 comparison, but cannot exclude an unindexed specialized quotient computation. Independent mathematical audit has not been performed.

## References
1. F. Giovenzana, A. Rojas, J. Song, *A locally complete family of Kummer type hyperkähler fourfolds*, arXiv:2611.16593v1, 12 November 2026. https://arxiv.org/html/2611.16593v1 (Sections 2.2, 3, 5, especially the final corollary on stabilizers).
2. S. Kapfer, G. Menet, *Integral cohomology of the generalized Kummer fourfold*, Algebraic Geometry 5 (2018), 523–567, https://content.algebraicgeometry.nl/2018-5/2018-5-014.pdf (Corollary 6.3, Section 6.4, Theorem 6.31; read with the 2020 corrigendum on integral torsion-freeness).
3. V. Bertini, A. Grossi, M. Mauri, E. Mazzon, *Terminalizations of quotients of compact hyperkähler manifolds by induced symplectic automorphisms*, arXiv:2401.13632v2, https://arxiv.org/html/2401.13632v2 (Section 1.2 assumptions; Sections 10–11).
4. M. Verbitsky, *Holomorphic symplectic geometry and orbifold singularities*, arXiv:math/9903175, https://arxiv.org/abs/math/9903175.
5. V. Batyrev, *Stringy Hodge numbers of varieties with Gorenstein canonical singularities*, arXiv:alg-geom/9711008, https://arxiv.org/abs/alg-geom/9711008.
6. M. A. Armstrong, *The fundamental group of the orbit space of a discontinuous group*, Proc. Cambridge Philos. Soc. 64 (1968), 299–301, https://doi.org/10.1017/S0305004100042845.
