# Euclidean integrality gap of matching polytopes equals reciprocal odd-cycle packing

## Finding

For any finite loopless simple graph \(G=(V,E)\), let the **matching polytope** be \(\mathcal M(G)=\operatorname{conv}\{\mathbf 1_M:M\text{ a matching of }G\}\subseteq\mathbb R^E\), and let its degree-relaxation or **fractional matching polytope** be
\[
\mathcal F(G)=\left\{x\in\mathbb R^E_{\ge0}:\sum_{e\ni v}x_e\le1\text{ for all }v\in V\right\}.
\]
Write \(\mathfrak C(G)\) for all collections of pairwise vertex-disjoint *simple odd cycles*, including the empty collection. Equip edge-coordinate space with its ordinary, unweighted Euclidean norm. Then
\[
\boxed{d_H(\mathcal F(G),\mathcal M(G))^2
 =\frac14\max_{\mathcal C\in\mathfrak C(G)}\sum_{C\in\mathcal C}\frac1{|E(C)|}.}
\tag{1}
\]
Here \(d_H\) is the ordinary symmetric Hausdorff metric; since \(\mathcal M(G)\subseteq\mathcal F(G)\), it equals the maximum distance from \(\mathcal F(G)\) to \(\mathcal M(G)\).

More precisely, every vertex \(x\) of \(\mathcal F(G)\) consists of disjoint unit-valued matching edges and vertex-disjoint odd cycles \(\mathcal C_x\) with half-valued cycle edges. Its **unique** Euclidean projection \(\pi(x)\) onto \(\mathcal M(G)\) is obtained by retaining the unit matching edges and all zero coordinates and replacing each half-valued edge of a cycle \(C\) of length \(\ell\) by \((\ell-1)/(2\ell)\). In particular,
\[
\boxed{\operatorname{dist}_2(x,\mathcal M(G))^2=\frac14\sum_{C\in\mathcal C_x}\frac1{|E(C)|}.}
\tag{2}
\]
The vertex-distance spectrum (including multiplicities) follows: for each fixed disjoint odd-cycle collection \(\mathcal C\), the number of fractional vertices with precisely those half-cycles is the number of ordinary matchings in the graph induced by \(V\setminus\bigcup_{C\in\mathcal C}V(C)\), and all have squared distance \(\sum_{C\in\mathcal C}1/(4|E(C)|)\).

If \(n=|V|\), the sharp universal order bound and its equality case are
\[
\boxed{d_H(\mathcal F(G),\mathcal M(G))\le\frac{\sqrt n}{6},}
\tag{3}
\]
with equality precisely when \(G\) admits a spanning collection of vertex-disjoint triangles. Consequently, when \(n\) is divisible by three, deciding whether equality holds is NP-complete by the classical triangle-partition problem.

## Assumptions and scope

All graphs are finite, undirected, loopless and simple; isolated vertices are permitted. Empty edge sets are permitted, with both polytopes equal to the singleton origin. Every coordinate corresponds to one *actual graph edge*, and all edge coordinates have identical Euclidean weight one. A cycle is simple, has at least three vertices and an odd number of edges. Cycle collections must be vertex-disjoint (not merely edge-disjoint). There is no assertion that the projection formula applies to arbitrary nonvertex points of the fractional polytope; it applies to every vertex and suffices for the Hausdorff maximum. The equality characterization in (3) is valid for any positive order; if the order is not divisible by three equality is impossible.

## Proof

**1. Fractional vertices.** The classical half-integral vertex theorem for the degree relaxation states that every extreme point \(x\) is supported on a matching of pairwise disjoint edges with coefficient one, together with pairwise vertex-disjoint odd simple cycles, each having edge coefficient one half, and that all such feasible vectors are extreme. This statement is recalled as Theorem 4 of Sanità (2018), and is also consistent with the incidence-rank characterization in Behrend (2013). An elementary justification is that a nontrivial fractional support must have as many independent tight degree equations as free edges: a fractional leaf cannot satisfy a tight degree equation; a fractional even cycle has an alternating two-sided perturbation; an odd cycle has a nonsingular signless incidence matrix and forces coefficient one half. All other fractional components have a nontrivial feasible perturbation.

**2. Lower bound for each fractional vertex.** Let \(C\in\mathcal C_x\) be an odd support cycle of length \(\ell\). Every integral matching uses at most \((\ell-1)/2\) of its \(\ell\) edges. By convexity, every \(z\in\mathcal M(G)\) obeys
\[
\sum_{e\in E(C)}z_e\le\frac{\ell-1}{2},
\qquad\sum_{e\in E(C)}(x_e-z_e)\ge\frac12.
\]
The Cauchy–Schwarz inequality therefore yields
\[
\sum_{e\in E(C)}(x_e-z_e)^2\ge\frac1{4\ell}.
\]
Distinct support cycles have disjoint edge coordinates; summing gives \(\|x-z\|_2^2\ge\sum_{C\in\mathcal C_x}1/(4|E(C)|)\). This lower bound applies regardless of any chords or edges joining the cycles.

**3. Constructing and certifying the projection.** On an odd cycle \(C\) of length \(\ell=2h+1\), there are exactly \(\ell\) maximum matchings of its cycle edges, each of cardinality \(h\). Every cycle edge is contained in exactly \(h\) of these matchings, by cyclic symmetry (equivalently by double-counting their \(\ell h\) incidences). Their uniform average thus assigns each cycle edge the value \(h/\ell=(\ell-1)/(2\ell)\). Independently choose one of these maximum matchings on each half-cycle and include every original unit edge. Each union is a genuine matching because the cycles and unit edges are mutually vertex-disjoint. Their averaged incidence vector \(y\) belongs to \(\mathcal M(G)\), equals the stated projection candidate, and attains the squared-distance lower bound from Step 2 on every cycle, with zero discrepancy elsewhere. Thus \(y\) is a nearest point; it is unique because Euclidean squared distance is strictly convex and \(\mathcal M(G)\) is closed and convex. This proves (2).

**4. Continuous Hausdorff maximum.** The function \(x\mapsto\operatorname{dist}_2(x,\mathcal M(G))\) is convex: apply the triangle inequality to convex combinations of nearest points. Every point of the compact polytope \(\mathcal F(G)\) is a convex combination of its vertices, so its distance cannot exceed the largest vertex distance. Conversely, every vertex is feasible. By Step 1 and (2), maximizing the squared distance is exactly the reciprocal-length odd-cycle packing problem in (1). A given cycle collection can be realized by a fractional vertex using coefficient one half on its edges and zero elsewhere, so no packing is excluded by constraints outside the cycles. The spectral multiplicity statement follows from the same unique support decomposition.

**5. Bound, equality and complexity.** Every odd cycle has length \(\ell\ge3\), whence \(1/\ell\le\ell/9\), with equality exactly at \(\ell=3\). Vertex-disjointness gives \(\sum_{C\in\mathcal C}|E(C)|\le n\). Hence (1) implies \(d_H^2\le n/36\). Equality requires and is attained by vertex-disjoint triangles covering all \(n\) vertices. For orders divisible by three this is precisely the NP-complete partition-into-triangles decision problem; the equality decision is in NP because a triangle partition certifies it. This proves (3) and the complexity consequence.

## Verification

The accompanying exact checker `verify.py` enumerates 518 fractional vertices across twelve named graphs (including complete graphs, odd and even cycles, disjoint triangles, a bowtie and a triangular prism). It checks their rational candidate projections, all degree constraints, all relevant Edmonds odd-subset inequalities, and all cycle-specific lower-bound certificates. In 85 instances it independently minimizes the quadratic objective using numerical SLSQP subject to the entire small-graph Edmonds linear description. It reports `MATCHING_HAUSDORFF_PASS packs=157 vertices=518 independent_QP=85`.

A second checker, `exhaustive_graphs.py`, verifies the rational certificates for all \(2^{10}=1024\) labeled graphs on five vertices, comprising 12,287 fractional vertices, and reports `FIVE_NODE_GRAPH_EXHAUSTIVE_PASS graphs=1024 vertices=12287 packs=2687`. Its imports and Python dependencies are listed in `VERIFICATION.md`. These finite tests supplement, but do not substitute for, the proof for all finite graphs.

## Relationship to prior work

The structural half-integral vertex classification is classical and is *not* claimed here. Sanità (arXiv:1806.03397, 2018) derives the **one-skeleton combinatorial diameter** of the fractional matching polytope from vertex supports and cycle counts, not Hausdorff separation from its integer hull. Blanchard–De Loera–Louveaux (arXiv:2001.09575, 2020) analyze monotone simplex-path lengths on the two polytopes, not Euclidean metric projection. Guo–Vishvajeet N (arXiv:2409.07283, 2024) approximate truncated fractional-polytope volume, not matching-hull distance. A separately published result on weighted Euclidean diameter and minimum-enclosing balls of both matching polytopes asserts equality of those **outer** invariants; that statement neither asserts nor entails that the two sets have zero or a prescribed *mutual* Hausdorff distance. Indeed their Hausdorff distance is positive as soon as \(G\) has an odd cycle. The construction here is an explicit Euclidean **inner-hull projection**, not a farthest-point or skeletal-distance computation. No historical priority claim is made beyond this documented comparison.

## Limitations

Equation (1) is an exact structural formula, not a claimed polynomial-time algorithm for arbitrary graphs; the triangle-partition boundary shows computing it exactly is NP-hard. The proof relies on ordinary unweighted edge-coordinate Euclidean geometry and does not establish analogous formulas for nonuniform weights, arbitrary convex quadratic norms, hypergraphs, or fractional perfect-matching polytopes. The projection formula is proved for vertices, not every fractional matching. Unidentified earlier formulations using metric integrality gaps or quadratic projection terminology remain possible. The result has not undergone an independent mathematical audit.

## References

1. L. Sanità, *The diameter of the fractional matching polytope and its hardness implications*, arXiv:1806.03397, first public 2018-06-09. Theorem 4 gives the half-integral vertex characterization; §§1–4 treat one-skeleton diameter and hardness. https://arxiv.org/html/1806.03397v2
2. M. Blanchard, J. A. De Loera and Q. Louveaux, *On the Length of Monotone Paths in Polyhedra*, arXiv:2001.09575, first public 2020-01-27, §§1,3. https://arxiv.org/html/2001.09575v1
3. H. Guo and Vishvajeet N, *Deterministic Approximation for the Volume of the Truncated Fractional Matching Polytope*, arXiv:2409.07283, first public 2024-09-11, §§1–4. https://arxiv.org/html/2409.07283v1
4. R. E. Behrend, *Fractional Perfect b-Matching Polytopes I: General Theory*, arXiv:1301.7356 (2013), classical incidence-rank and vertex descriptions (background only; earlier than the lead-source cohort). https://arxiv.org/abs/1301.7356
5. *Weighted Euclidean distance extrema survive fractional matching relaxation*, published mathematical record, 2026-10-11; inspected RESULT.md, on equal enclosing balls and diameters, not Hausdorff separation. https://github.com/published-finding corpus/2026/blob/main/2026/10/11/SCOPE-weighted-euclidean-distance-extrema-survive-fractional-matching--7e2404daa627/RESULT.md
