# A sharp entropy bound for John ellipsoids of enriched chain polytopes

## Finding
Let \(P\) be a nonempty finite poset on \(n\) elements, with height \(h\ge2\) (the maximum cardinality of a chain) and width \(w\) (the maximum cardinality of an antichain). In the canonical Euclidean coordinates, let
\[
E(P)=\operatorname{conv}\{x\in\{-1,0,1\}^{P}:\operatorname{supp}(x)\text{ is an antichain}\}.
\]
Let \(J(P)\) denote its unique maximum-volume inscribed ellipsoid, let \(\kappa_n\) denote the volume of the unit Euclidean ball, and define the binary relative entropy (with natural logarithms)
\[
D(t\|s)=t\log\frac ts+(1-t)\log\frac{1-t}{1-s},\quad 0<t,s<1.
\]
Then the following inequality holds for **every** finite poset of height at least two:
\[
\boxed{\frac{\operatorname{vol}_n J(P)}{\kappa_n h^{-n/2}}\ \ge\ \exp\!\left(\frac n2D\!\left(\frac wn\middle\|\frac1h\right)\right).}\tag{1}
\]
The denominator is the volume of a largest Euclidean ball in \(E(P)\). The bound is strict relative to that ball whenever \(n<hw\). More precisely,
\[
\boxed{J(P)\text{ is a Euclidean ball}\ \Longleftrightarrow\ n=h w.}\tag{2}
\]
If \(n=hw\), then \(J(P)=h^{-1/2}B_2^n\), so the ratio in (1) is exactly one.

The inequality is **attained** for every ordinal sum of \(h\) nonempty antichains having cardinalities \(w,b,\ldots,b\), where \(b\) is a positive integer not exceeding \(w\) and \(n=w+(h-1)b\). More generally, for an ordinal sum of arbitrary nonempty antichains with sizes \(m_1,\ldots,m_h\), the complete John ellipsoid has squared coordinate semiaxes \(m_j/n\) throughout layer \(j\).

## Assumptions and scope
The poset is finite, nonempty and is not required to be graded, connected or naturally labeled. The height \(h\) and width \(w\) count elements, not edges; \(h\ge2\), hence \(1\le w<n\). The inequality \(n\le hw\) is the standard height-width bound. The enriched chain polytope uses **independently signed antichain vectors**, not signed-order-polytope or signed-chain conventions with linear terms of the form \(x_i+x_j\). The Euclidean metric is the ordinary coordinate metric, not an arbitrary affine metric. All volumes are ordinary \(n\)-dimensional Euclidean volumes, not normalized lattice volumes.

The case \(h=1\) is an antichain: \(E(P)=[-1,1]^n\), its John ellipsoid is the unit ball, and (2) remains true with \(n=hw\); (1) is restricted to \(h\ge2\) because its displayed binary divergence has \(s=1/h<1\).

## Proof
**1. The ellipsoid optimization.** By the signed-antichain description and the chain inequalities, the polytope has the exact halfspace description
\[
E(P)=\left\{x\in\mathbb R^P:\sum_{i\in C}|x_i|\le1\ \text{for every chain }C\right\}.\tag{3}
\]
It is full-dimensional and invariant under all independent coordinate sign changes. Existence and uniqueness of its John ellipsoid, and these reflections, force \(J(P)\) to have center zero and diagonal positive shape: for uniquely determined \(u_i>0\),
\[
J(P)=\left\{x:\sum_{i\in P}\frac{x_i^2}{u_i}\le1\right\}.\tag{4}
\]
For a fixed chain \(C\), the maximum of \(\sum_{i\in C}|x_i|\) over (4) is \(\sqrt{\sum_{i\in C}u_i}\), by weighted Cauchy--Schwarz (with equality). Therefore (4) is contained in \(E(P)\) if and only if \(\sum_{i\in C}u_i\le1\) for every chain. Its volume is \(\kappa_n\sqrt{\prod_i u_i}\). Hence the exact problem for the John ellipsoid is
\[
\max_{u_i>0}\ \sum_i\log u_i\quad\text{subject to}\quad
\sum_{i\in C}u_i\le1\quad(C\text{ any chain}).\tag{5}
\]
The objective is strictly concave, so its maximizer and (4) are unique. In particular the radius-\(1/\sqrt h\) centered ball is feasible, since all chains have at most \(h\) elements. It is also a largest Euclidean ball: the inequalities belonging to a longest chain have normals of norm \(\sqrt h\), and central symmetry ensures that no translated ball has larger radius.

**2. A feasible width-sensitive ellipsoid.** Let \(A\) be a maximum antichain, \(|A|=w\), and put
\[
a=\frac wn,\qquad b=\frac{n-w}{n(h-1)},\qquad
u_i=\begin{cases}a&i\in A,\\ b&i\notin A.\end{cases}\tag{6}
\]
Because \(n\le hw\), we have \(a\ge b>0\). A chain contains at most one element of \(A\) and at most \(h\) elements altogether. Consequently
\[
\sum_{i\in C}u_i\le a+(h-1)b=1\tag{7}
\]
for every chain, including chains avoiding \(A\), since \(a\ge b\). Thus the diagonal ellipsoid \(E_A=\{x:\sum_i x_i^2/u_i\le1\}\) lies in \(E(P)\). Its volume compared with the centered largest ball is exactly
\[
\begin{aligned}
\log\frac{\operatorname{vol}_n(E_A)}{\kappa_nh^{-n/2}}
&=\frac12\left[w\log\frac{hw}{n}+(n-w)\log\frac{h(n-w)}{n(h-1)}\right]\\
&=\frac n2D\!\left(\frac wn\middle\|\frac1h\right).
\end{aligned}\tag{8}
\]
Optimality of \(J(P)\) over all inscribed ellipsoids proves (1). If \(n<hw\), then \(w/n>1/h\). Strict positivity of binary relative entropy for unequal probabilities gives \(\operatorname{vol}E_A>\kappa_nh^{-n/2}\). No largest ball can therefore be the John ellipsoid.

**3. Exact roundness criterion.** If \(n=hw\), Dilworth's theorem partitions \(P\) into \(w\) disjoint chains. Since each chain has at most \(h\) elements and their cardinalities total \(hw\), all \(w\) chains have exactly \(h\) elements. For *any* feasible \(u\) from (5), the arithmetic--geometric mean inequality on each chain gives
\[
\prod_{i\in C}u_i\le\left(\frac{\sum_{i\in C}u_i}{h}\right)^h\le h^{-h}.
\]
Multiplying these inequalities over the chain partition yields \(\prod_{i\in P}u_i\le h^{-n}\). Equality is achieved by \(u_i=1/h\) for all coordinates, so the John ellipsoid is the radius-\(1/\sqrt h\) ball. Uniqueness follows from strict concavity of (5). This proves the converse in (2).

**4. Exact sharpness on layered posets.** Suppose \(P=A_{m_1}\oplus\cdots\oplus A_{m_h}\) is an ordinal sum of antichains, with \(\sum_jm_j=n\). Independent permutations of elements in the same layer preserve the polytope and its unique John ellipsoid. Therefore its \(u_i\) are constant on layers, say \(u_i=t_j\) for \(i\in A_{m_j}\). Maximal chains select one vertex from every layer, so (5) reduces to
\[
\max\ \sum_{j=1}^h m_j\log t_j\quad\text{subject to}\quad t_j>0,\ \sum_jt_j\le1.
\]
Strict concavity or weighted AM--GM gives the unique optimizer \(t_j=m_j/n\). In the special case \((m_1,\ldots,m_h)=(w,b,\ldots,b)\), this optimizer coincides coordinate by coordinate with (6), so inequality (1) is attained exactly. This completes the proof.

## Verification
The proof is symbolic and all-dimensional. The standalone `verify.py` reconstructs chain and antichain families from finite acyclic relations; for all \(1{,}099\) naturally labeled DAG profiles on at most five elements it checks the height-width inequality, exact rational feasibility of (6), and a longest-chain partition in each rectangular case. It verifies \(89\) rectangular and \(1{,}010\) nonrectangular instances, nine layered examples, exact probability/multiplier identities for their optimal ellipsoids, and numerical agreement of the logarithmic determinant identity (8). The program uses Python's exact `fractions.Fraction` for combinatorial feasibility. Its finite tests are not used as an all-dimensional proof.

To reproduce, place `verify.py` beside this file and run `python3 verify.py`. The required mathematical inputs are the classical chain/antichain facet description, Dilworth's theorem, and the standard existence/uniqueness theorem for the maximum-volume inscribed ellipsoid.

## Relationship to prior work
Ohsugi and Tsuchiya introduced enriched chain polytopes and established their signed-antichain geometry; Okada and Tsuchiya established enriched transfer maps and exact descriptions. Kohl, Olsen and Sanyal independently investigated the same bodies as unconditional chain polytopes. These sources address Ehrhart, triangulation, and unconditional-reflexive structures rather than the sharp Euclidean John-volume bound (1).

The exact centered Euclidean inradius \(1/\sqrt h\), tangent-facet description and height-width recovery were already established in the public mathematical record entitled *Height and width are the exact Euclidean radii of enriched chain polytopes*. They are used as background here, not claimed as new. Existing work on the John ellipsoid of *ordinary nonnegative* complete-height-two chain polytopes concerns different bodies; the signed-chain volume polytopes defined using \(|x_i+y_j|\le1\) are also different from (3).

Classical graph entropy provides a related variational framework: the positive orthant of (3) is the stable-set polytope of the comparability graph, and maximizing \(\sum_i\log u_i\) is a standard graph-entropy convex program. The contribution assessed here is specifically the **sharp, attained geometric lower bound (1), explicit optimal inscribed ellipsoid (6), and exact universal roundness criterion (2)**. Graph-entropy equalities may imply the roundness part after this geometric identification; that logical relationship is a genuine priority caveat rather than evidence of a previously published matching quantitative ellipsoid statement.

## Limitations
The bound concerns standard coordinate Euclidean geometry and positive-dimensional full-dimensional enriched chain polytopes. It need not survive nonorthogonal affine changes of coordinates. The candidate ellipsoid (6) is not claimed to be the John ellipsoid for every poset; it is provably optimal on the stated layered families, and when \(n=hw\). For other posets it gives a lower bound only. No elementary closed formula for the full semiaxis spectrum of an arbitrary poset is claimed. The originality assessment is limited by finite literature access; graph-entropy and unconditional-convexity formulations could contain an equivalent quantitative statement.

## References
1. H. Ohsugi and A. Tsuchiya, *Enriched chain polytopes*, arXiv:1812.02097, first publicly posted 2018-12-05; Israel Journal of Mathematics 237 (2020), 485--500.
2. S. Okada and A. Tsuchiya, *Two enriched poset polytopes*, arXiv:2003.12271, first publicly posted 2020-03-27; Annals of Combinatorics 28 (2024), 257--282.
3. F. Kohl, M. Olsen and R. Sanyal, *Unconditional Reflexive Polytopes*, Discrete & Computational Geometry 64 (2020), 427--452, DOI 10.1007/s00454-020-00199-8.
4. J. Körner, G. Simonyi, *Graph entropy*, classical perfect-graph entropy theory; see also S. S. C. Rezaei and C. Godsil, *Entropy of Symmetric Graphs*, arXiv:1311.6561 (2013).
5. P. M. Gruber and F. E. Schuster, *An arithmetic proof of John's ellipsoid theorem*, arXiv:1207.7246 (2012).
