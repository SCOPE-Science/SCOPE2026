# Exact four-vertex geometric volumes and dimension-sensitive first-order laws on random tori

## Finding

Let \(D\ge1\) be an integer. For each connected unlabelled four-vertex graph \(H\), let \(\gamma_D(H)\) be the \(3D\)-dimensional configuration volume defined in the assumptions below. There are precisely six such graphs, and their **complete exact volume table** is

\[
\begin{aligned}
\gamma_D(K_{1,3})&=4\bigl[8^D-3\cdot6^D+3(14/3)^D-4^D\bigr],\\
\gamma_D(P_4)&=12\bigl[8^D-2\cdot6^D-(16/3)^D+3(14/3)^D-4^D\bigr],\\
\gamma_D(\mathrm{paw})&=12\bigl[6^D-2(14/3)^D+4^D\bigr],\\
\gamma_D(C_4)&=3\bigl[(16/3)^D-2(14/3)^D+4^D\bigr],\\
\gamma_D(K_4-e)&=6\bigl[(14/3)^D-4^D\bigr],\\
\gamma_D(K_4)&=4^D.
\end{aligned}
\]

Here the paw is a triangle with a pendant vertex, and \(K_4-e\) is the diamond. In one dimension the ordered values for \((K_{1,3},P_4,\mathrm{paw},C_4,K_4-e,K_4)\) are \((0,8,8,0,4,4)\); in two dimensions they are \((64/3,464/3,304/3,8/3,104/3,16)\). In particular, a four-cycle or claw is impossible as an induced connected component for \(D=1\), whereas all six connected types have strictly positive volumes for every \(D\ge2\).

For the sparse random torus graph in the fourth-component critical window \(n^4r_n^{3D}\to a\in(0,\infty)\), the number of components of each of these six isomorphism types converges jointly to independent Poisson random variables of means \(a\gamma_D(H)/24\). This Poisson convergence itself is the published theorem of Haber–Mirabi–Shelah; the contribution here is the **explicit evaluation of its six intensity parameters**, rather than a new convergence theorem. For the first-order sentence asserting that a connected component is an induced four-cycle, its limiting probability is zero for \(D=1\) and exactly \(1-e^{-a/9}\) for \(D=2\). For the corresponding claw sentence, the planar limit is \(1-e^{-8a/9}\).

The normalized intensity mass of the six four-vertex component types has a further shape limit as \(D\to\infty\): the probability weight tends to \(3/4\) for \(P_4\), to \(1/4\) for \(K_{1,3}\), and to zero for every other type, with total error \(O((3/4)^D)\). This is a *sequential* statement about the explicitly computed parameters, with the graph-size limit taken for each fixed dimension; it does not claim uniform joint asymptotics in \(n\) and \(D\).

## Assumptions and scope

For \(D\ge1\) and four points \(z_0=0,z_1,z_2,z_3\in\mathbb R^D\), join \(i,j\) exactly when \(\|z_i-z_j\|_\infty\le1\). Define

\[
\gamma_D(H)=\int_{(\mathbb R^D)^3}\mathbf1\{G_\infty(0,z_1,z_2,z_3)\cong H\}\,dz_1\,dz_2\,dz_3.
\]

The integral is finite for connected \(H\) because each point lies within \(3\) unit steps of the anchor. Hyperplanes where a distance equals \(1\) have zero volume. In the probability application, \(n\) points are sampled independently and uniformly from \(\mathbb T^D=(\mathbb R/\mathbb Z)^D\), and adjacency is torus \(L^\infty\)-distance at most \(r_n\). The dimension \(D\) is fixed as \(n\to\infty\); assume \(n^4r_n^{3D}\to a\in(0,\infty)\). All component counts are unlabelled isomorphism-type counts, and the factor \(24=4!\) is required in their Poisson means.

## Proof

**1. Reduce each volume to mandatory-edge integrals.** For each connected **labelled** graph \(F\) on \(\{0,1,2,3\}\), write

\[
J(F)=\int_{\mathbb R^3}\mathbf1\{|x_i-x_j|\le1\text{ for all }ij\in E(F)\}\,dx_1dx_2dx_3,\quad x_0=0.
\]

Because a connected spanning tree bounds all point distances, \(J(F)<\infty\). Coordinate-wise factorization of the \(L^\infty\) inequalities gives \(J(F)^D\) in dimension \(D\). For any fixed connected labelled representative \(H\), inclusion–exclusion over its missing edges gives

\[
\gamma_D(H)=\frac{24}{|\operatorname{Aut}(H)|}
\sum_{S\subseteq E(\overline H)}(-1)^{|S|}J(H\cup S)^D.
\tag{1}
\]

The orbit factor accounts for **all** labelled realizations isomorphic to \(H\). Relabelling including the distinguished anchor does not change the integral: translate the new anchor to zero and change the other three difference variables, a linear transformation of absolute determinant \(1\). In (1), nonexistent edges are ruled out by inclusion–exclusion; equality at the threshold has measure zero.

**2. Exact one-coordinate integrals.** Partition the domain into the \(24\) strict linear orders of \(0,x_1,x_2,x_3\). On one such order let \(g_1,g_2,g_3>0\) be the consecutive gaps. Since \(F\) is connected, at least one edge crosses each gap, and therefore \(0<g_i\le1\). The change from ordered coordinates to the gaps has Jacobian \(1\), even if the anchored coordinate \(x_0=0\) is not the leftmost point. Edges spanning consecutive positions \((0,3)\), \((0,2)\), or \((1,3)\) impose respectively \(g_1+g_2+g_3\le1\), \(g_1+g_2\le1\), or \(g_2+g_3\le1\). Constraints on consecutive positions are already imposed. Thus the order-cell volume is exactly \(1/6\) when the full span is an edge; otherwise \(1/3\) if both double spans are edges; otherwise \(1/2\) if exactly one double span is an edge; otherwise \(1\). These are elementary simplex and triangular-prism integrals.

For the six connected graph types, the counts of coordinate orders contributing to the four classes \((1/6,1/3,1/2,1)\), respectively, are

| Type | \(1/6\) | \(1/3\) | \(1/2\) | \(1\) | \(J(F)\) |
| --- | ---: | ---: | ---: | ---: | ---: |
| \(K_{1,3}\) | 12 | 0 | 12 | 0 | 8 |
| \(P_4\) | 12 | 6 | 4 | 2 | 8 |
| paw | 16 | 4 | 4 | 0 | 6 |
| \(C_4\) | 16 | 8 | 0 | 0 | \(16/3\) |
| diamond | 20 | 4 | 0 | 0 | \(14/3\) |
| \(K_4\) | 24 | 0 | 0 | 0 | 4 |

The last column follows by summing cell volumes. The standalone exact checker enumerates every ordering independently from the table and verifies these counts. Substitution into (1), with the respective automorphism counts \(6,2,2,8,4,24\), gives the six formulas in the Finding. The same calculation verifies both numerical specializations; all calculations are rational, not rounded integrals.

**3. Positivity and dimensional transition.** A one-dimensional configuration cannot induce a claw or a chordless four-cycle: an interval graph has neither. The exact formulas give zero in these two cases and positive volume for the other four. For \(D=2\), a strict four-cycle is represented in order by \((0,0),(0.7,0.7),(1.4,0),(0.7,-0.7)\), and a strict claw is represented by center \((0,0)\) and leaves \((0.9,0.9),(-0.9,0.9),(0,-0.9)\). All required distances are strictly below \(1\), all excluded distances are strictly above \(1\). Embedding the witnesses into higher dimensions by adjoining zero coordinates gives positive-volume open neighborhoods of the configurations; the other four graph types are already realizable on the line. Thus all six have positive volume for every \(D\ge2\).

**4. Convert to first-order probabilities.** Under the stated scaling, \(r_n\to0\) and \(nr_n^D\to0\). Theorem 1.4 of Haber–Mirabi–Shelah proves joint independent Poisson limits with means \(a\gamma_D(H)/4!\), using factorial moments of disjoint components. In particular, the absence probability for a specified type tends to \(e^{-a\gamma_D(H)/24}\). The event that a component is isomorphic to fixed \(H\) is first-order expressible by four existential witnesses, their complete adjacency table, their distinctness, and a universal quantifier forbidding edges from those witnesses to any other vertex. With \(\gamma_1(C_4)=0\) and \(\gamma_2(C_4)=8/3\), the limit is respectively \(0\) and \(1-e^{-a/9}\); with \(\gamma_2(K_{1,3})=64/3\), the claw limit is \(1-e^{-8a/9}\). No independent proof of the published joint Poisson theorem is claimed here.

**5. Large-dimension intensity shares.** The exact table gives

\[
\gamma_D(P_4)=12\cdot8^D[1+O((3/4)^D)],\quad
\gamma_D(K_{1,3})=4\cdot8^D[1+O((3/4)^D)],
\]

while each remaining \(\gamma_D(H)=O(6^D)\). Therefore the sum of six volumes is \(16\cdot8^D[1+O((3/4)^D)]\), yielding weights \(3/4\), \(1/4\), and \(0\), respectively. This concerns the ratios of fixed-dimension limiting Poisson intensities, rather than a joint variable-dimension graph limit.

## Verification

Run `python3 checker.py` using Python 3.9 or later; the script requires only the standard library. It enumerates all \(64\) simple four-vertex labelled edge sets, tests connectivity and the six isomorphism classes, independently enumerates the \(24\) coordinate orders in the definition of \(J(F)\), computes the inclusion–exclusion formulas over every missing-edge subset, and checks the exact one- and two-dimensional values using rational arithmetic. It additionally checks strict planar witnesses for the claw and four-cycle, and exact positivity for dimensions \(2\) through \(19\). The arbitrary-dimensional positivity proof is analytic, not inferred from the finite positivity tests. The exact output is `FOUR_COMPONENT_ALL_CHECKS_OK: exact inclusion-exclusion, D=1,2, six graph types, strict witnesses`.

## Relationship to prior work

Haber, Mirabi and Shelah, *First-Order Laws for Random Geometric Graphs on the Torus*, arXiv:2609.26230, Theorem 1.4 and Lemmas 4.1–4.3, establish the sparse critical-window Poisson component law, introduce exactly these configuration volumes, and compute explicitly the clique volume \(\gamma_D(K_k)=k^D\). Therefore the **general Poisson theorem, the geometric-integral definition and the clique row are not novel**. The present finite but all-dimensions evaluation supplies the five non-clique rows, the complete four-component intensity vector, a dimension-separating first-order readout with an exact constant, and its high-dimensional shape asymptotics. The known impossibility of induced claws and chordless four-cycles in one-dimensional unit interval graphs is also not claimed new. Nearby geometric-graph Poisson and cluster-integral literature may contain equivalent numerical evaluations; priority is not independently established.

## Limitations

The result concerns \(L^\infty\) torus adjacency at a fixed-dimension sparse four-component window, not Euclidean \(L^2\) radii, fixed positive radii, arbitrary connection bodies, or a joint \(D=D(n)\) limit. It uses the published Poisson component theorem as an explicitly identified premise. A more general published cluster-integral identity may subsume the finite constants, though the inspected primary source does not list them. No independent audit or priority certification has been performed.

## References

- S. Haber, M. Mirabi, and S. Shelah, *First-Order Laws for Random Geometric Graphs on the Torus*, arXiv:2609.26230, especially Theorem 1.4, Lemmas 4.1–4.3, and Section 4; https://arxiv.org/abs/2609.26230.
- M. Penrose, *Random Geometric Graphs*, Oxford University Press, 2003 (background reference only; no claim that its entire text was checked).
