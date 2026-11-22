# Acute–obtuse reflection dominance and a Dirichlet ridge-angle law for simplex-sum cyclohedra

## Finding
For every integer \(n\ge3\), let \(C_n\) be the cycle on \(\mathbb Z/n\mathbb Z\), and let \(\mathcal B_n\) contain all nonempty vertex subsets inducing connected subgraphs, including the full vertex set. In standard coordinates define the simplex-sum cyclohedron
\[
\mathcal W_n=\sum_{T\in\mathcal B_n}\operatorname{conv}\{e_i:i\in T\}\subset\mathbb R^n.
\]
Use the intrinsic Euclidean metric of its affine hull. A *ridge* means a codimension-two face, and an angle means the **interior** angle between its two facets.

The complete **multiset** of ridge angles (so coincident numerical angles are added with multiplicity) is as follows.

* **Nested facets.** For each \(1\le a<b\le n-1\), there are \(n(b-a+1)\) ridges with angle
\[
\theta^{\mathrm{nested}}_{a,b}=\pi-\arccos\sqrt{\frac{a(n-b)}{b(n-a)}}.
\]
* **Disjoint nonadjacent facets.** For each \(1\le a\le b\) with \(a+b\le n-2\), there are
\[
\frac{n(n-a-b-1)}{1+\mathbf1_{a=b}}
\]
ridges with angle
\[
\theta^{\mathrm{disjoint}}_{a,b}=\arccos\sqrt{\frac{ab}{(n-a)(n-b)}}.
\]

All these angles are strictly obtuse in the nested class and strictly acute in the disjoint class; no right angles occur. The respective numbers of obtuse, acute and total ridges are
\[
O_n=\frac{n(n-1)(n-2)(n+3)}6,\qquad
A_n=\frac{n(n-1)(n-2)(n-3)}{12},\qquad
R_n=\frac{n(n-1)(n-2)(n+1)}4.
\]
Thus a uniformly sampled ridge is acute with probability \((n-3)/(3(n+1))\), which tends to \(1/3\). The case \(n=3\) has six obtuse vertices (the ridges of its hexagon) and no acute ridges.

There is also a **finite-dimensional reflected-angle dominance** statement. For every angle \(\theta\in(0,\pi/2)\) occurring in the ridge multiset, the multiplicity of \(\pi-\theta\) is strictly greater than twice the multiplicity of \(\theta\). More precisely, for disjoint lengths \(a\le b\), set \(r=n-a-b\ge2\). The acute contribution of this length pair is \(n(r-1)/(1+\mathbf1_{a=b})\); corresponding nested pairs with exactly the complementary obtuse angle contribute \(2n(r+1)/(1+\mathbf1_{a=b})\). Additional nested pairs may contribute to that same angle.

Finally, take \((Z_1,Z_2,Z_3,Z_4)\sim\operatorname{Dirichlet}(1,1,1,1)\) and set
\[
C=\sqrt{\frac{Z_1Z_2}{(1-Z_1)(1-Z_2)}}\in(0,1).
\]
If \(\Theta_n\) is the interior angle at a uniformly sampled ridge of \(\mathcal W_n\), then
\[
\Theta_n\ \Longrightarrow\
\begin{cases}
\arccos C,&\text{with probability }1/3,\\
\pi-\arccos C,&\text{with probability }2/3,
\end{cases}
\]
where the branch choice is independent of \(C\). In particular, the conditional limiting **absolute exterior-normal cosine** is the same on the acute and obtuse classes, despite their asymptotic multiplicities being in the ratio \(1:2\).

## Assumptions and scope
The statement is for the explicit unweighted Minkowski sum of all connected-subset simplices, in the coordinate hyperplane \(\sum_i x_i=|\mathcal B_n|\) with the ordinary inner product inherited from \(\mathbb R^n\). The result holds for any positive simplex coefficients that preserve the full nested normal fan, since ridge angles depend on facet normals and incidence rather than facet offsets. It does **not** assert the same Euclidean angles for affine or combinatorially equivalent but differently oriented realizations of the cyclohedron.

A tube is a nonempty proper connected vertex set of \(C_n\), equivalently a proper cyclic interval. Two distinct tubes are compatible precisely if they are strictly nested or disjoint with no edge of the cycle between them. The standard graph-associahedron/nested-complex construction implies that proper tubes index the facets and compatible tube pairs index the ridges. The cited primary sources give this face-lattice realization for the specific Minkowski-sum model. The argument below computes the metric invariant from that established structural description.

## Proof
**1. Intrinsic facet normals and angles.** For a proper tube \(S\) of cardinality \(s\), the defining supporting inequality has the form \(\sum_{i\in S}x_i\ge c_S\), with outward intrinsic normal
\[
\nu_S=-\left(\mathbf1_S-\frac{s}{n}\mathbf1\right).
\]
This follows directly because the minimum of the coordinate sum on a simplex \(\Delta_T\) is \(1\) when \(T\subseteq S\), and \(0\) otherwise. Its intrinsic norm is \(\|\nu_S\|^2=s(n-s)/n\). For two proper tubes \(S,T\) of sizes \(s,t\),
\[
\frac{\langle\nu_S,\nu_T\rangle}{\|\nu_S\|\|\nu_T\|}
=\frac{n|S\cap T|-st}{\sqrt{s(n-s)t(n-t)}}.\tag{1}
\]
For nested tubes with \(|S|=a<|T|=b\), (1) is \(\sqrt{a(n-b)/(b(n-a))}\), strictly positive. For disjoint nonadjacent tubes with lengths \(a,b\), (1) is \(-\sqrt{ab/((n-a)(n-b))}\), strictly negative. The interior angle at a ridge equals \(\pi\) minus the angle between outward normals, giving both formulas and excluding right angles.

**2. Exact ridge census.** Fix a larger cyclic interval \(T\) with length \(b<n\). There are \(n\) choices for \(T\). A strictly smaller interval of length \(a<b\) can start at any of \(b-a+1\) positions inside it. This gives \(n(b-a+1)\) nested ridges for the ordered length parameters.

For disjoint nonadjacent intervals of sizes \(a,b\), the complementary circle must consist of two nonempty gaps with lengths \(g,h\ge1\) and \(g+h=n-a-b\). When \(a<b\), orienting the circle at the unique shorter interval yields \(n(n-a-b-1)\) unordered pairs. When \(a=b\), every unordered pair is counted twice, giving exactly half that number. The allowed lengths obey \(a+b\le n-2\). The compatibility theorem ensures no other facet pair forms a ridge.

Summing the nested counts gives
\[
O_n=n\sum_{b=2}^{n-1}\sum_{a=1}^{b-1}(b-a+1)
=\frac{n(n-1)(n-2)(n+3)}6.
\]
Alternatively, a disjoint pair can be encoded by four positive cyclic block lengths in order: first tube, first gap, second tube, second gap. There are \(n\binom{n-1}{3}\) oriented encodings, and every unordered ridge has exactly two, so
\[
A_n=\frac n2\binom{n-1}{3}
=\frac{n(n-1)(n-2)(n-3)}{12}.
\]
Adding and taking the ratio proves the displayed census and acute probability.

**3. Reflected-angle dominance.** Fix \(1\le a\le b\) with \(r=n-a-b\ge2\). Its disjoint angle has squared cosine \(ab/((n-a)(n-b))\). Nested length pairs \((a,n-b)\) and \((b,n-a)\) have the same squared cosine but a positive normal inner product. For \(a<b\), these pairs are distinct and together contribute \(2n(r+1)\) obtuse ridges; for \(a=b\), they coincide and contribute \(n(r+1)\). Their corresponding acute counts are respectively \(n(r-1)\) and \(n(r-1)/2\). Thus the ratio of the paired contributions is exactly \(2(r+1)/(r-1)>2\). Summing over all length pairs that yield any fixed acute numerical angle preserves this strict inequality; other nested pairs can only increase its complementary multiplicity. This proves dominance, including numerical angle collisions.

**4. Limiting Dirichlet law.** Every disjoint ridge has precisely two rooted four-block descriptions \((a,g,b,h)\) with all parts positive and sum \(n\). Uniform selection therefore induces a uniform positive four-part composition. As \(n\to\infty\), its four normalized parts converge to the uniform distribution on the three-simplex, namely \(\operatorname{Dirichlet}(1,1,1,1)\). Its acute cosine is \(\sqrt{ab/((n-a)(n-b))}\), which converges to the indicated \(C\).

For nested ridges, root the larger interval and write the consecutive block lengths \((a,u,v,w)\), where \(a,w\ge1\), \(u,v\ge0\), \(u+v\ge1\), and \(a+u+v+w=n\). The inner interval begins \(u\) positions after the larger interval's beginning; its length is \(a\), and the outside complement has length \(w\). Each nested pair has exactly one such description after the larger interval's start is fixed. The restrictions \(u=0\), \(v=0\), or \(u+v=0\) account for only \(O(n^2)\) compositions, compared with \(\Theta(n^3)\) overall. Therefore the normalized four block sizes again converge to the uniform three-simplex law. Since the larger interval has length \(n-w\), the positive exterior-normal cosine is \(\sqrt{aw/((n-a)(n-w))}\). The marginal joint law of the first and fourth Dirichlet coordinates equals that of any other two coordinates, hence its limit has exactly the same law \(C\) as the disjoint case.

Finally, the exact acute proportion converges to \(1/3\), and the remaining probability tends to \(2/3\). The continuity of \(\arccos\) on the interior yields the claimed weak mixture limit, with the branch chosen independently of the common magnitude law.

## Verification
Run `python3 verify.py` from the extracted package. It uses only the Python standard library. It verifies the complete compatibility and squared-normal-cosine formulas for \(3\le n\le12\), enumerates all Minkowski-sum vertices and verifies every facet and pair-face rank for \(3\le n\le6\), and checks strict reflected multiplicity dominance with exact rational squared-cosine keys for \(4\le n\le25\). The expected final line is `CYCLO_RIDGE_AND_REFLECTION_PASS`. These computations are finite cross-checks, not replacements for the proof for arbitrary \(n\). The Dirichlet law is established by the composition argument, not by simulation.

## Relationship to prior work
The graph-associahedron and nested-complex theory supplies the underlying tube-compatible face structure and the projected characteristic-vector facet rays; it does not in the inspected sources supply this full Euclidean ridge-angle multiset, reflected multiplicity dominance, or the two-branch Dirichlet law. Jevtić–Jelić–Živaljević (2018) explicitly discuss the cyclohedron as a Minkowski sum of connected-set simplices and study Kantorovich–Rubinstein duality, rather than ridge metric statistics. Cardinal–Pournin–Valencia-Pabon (2021) study combinatorial rotation-graph diameter, and Pilaud–Santos–Ziegler (2023) survey the nested fan and simplex-sum realization. The new calculations rely on those structural inputs, without claiming the underlying polytope construction, tube enumeration, or face incidence as novel.

## Limitations
The claim concerns the specified simplex-sum realization and all positive coefficients with the same normal fan; it is not invariant under arbitrary affine equivalence. Equal numerical angle values from different length parameters must have their multiplicities summed. The limiting law is a weak limit; no finite-dimensional convergence rate is asserted. The published-literature comparison supports provisional originality, not an exhaustive historical-priority certification. Independent external review has not been performed.

## References
1. V. Pilaud, F. Santos, G. M. Ziegler, *Celebrating Loday's Associahedron*, arXiv:2305.08471 (first posted 2023-05-15), Sect. 5.1; https://arxiv.org/abs/2305.08471 .
2. J. Cardinal, L. Pournin, M. Valencia-Pabon, *Diameter estimates for graph associahedra*, arXiv:2106.16130 (first posted 2021-06-30), Sect. 1.1; https://arxiv.org/abs/2106.16130 .
3. F. D. Jevtić, M. Jelić, R. T. Živaljević, *Cyclohedron and Kantorovich–Rubinstein Polytopes*, Arnold Mathematical Journal **4** (2018), 87–112, especially Sects. 3.1 and 5.1; https://doi.org/10.1007/s40598-018-0083-4 .
4. C. Hohlweg, C. Lange, *Realizations of the Associahedron and Cyclohedron*, Discrete & Computational Geometry (2007), DOI 10.1007/s00454-007-1319-6, particularly Section 4; https://doi.org/10.1007/s00454-007-1319-6 .
