# Graph-conditioned isomorphism fibers of minimal cubic-nilpotent semigroups

## Finding

Let \(H=(V,E)\) be an arbitrary finite simple graph of order \(r\ge2\), with no universal vertex, and put \(G=\operatorname{Aut}(H)\). Let \(\mathcal N(H)\) denote the isomorphism classes of semigroups \(S\) with zero satisfying \(S^3=\{0\}\ne S^2\), \(|S|=r+2\), and \(\Gamma(S)\cong H\), where \(\Gamma(S)\) is the simple commuting graph on \(S\setminus Z(S)\). This note classifies and counts every member of \(\mathcal N(H)\).

For a permutation \(\sigma\in G\), let its disjoint cycle lengths be \(\lambda_1,\ldots,\lambda_t\), and define
\[
 c(\sigma)=t,\qquad
 b(\sigma)=\sum_{i=1}^{t}\left\lfloor\frac{\lambda_i}{2}\right\rfloor+
 \sum_{1\le i<j\le t}\gcd(\lambda_i,\lambda_j).
\]
Call \(\sigma\) *admissible* if, for each of its even cycles
\(C=(v_0,v_1,\ldots,v_{2a-1})\), all antipodal pairs
\(\{v_i,v_{i+a}\}\) are edges of \(H\), for \(0\le i<a\).
Then the number of isomorphism classes of minimal cubic-nilpotent realizations is
\[
\boxed{\lvert\mathcal N(H)\rvert=\frac{1}{|G|}
\sum_{\substack{\sigma\in G\\\sigma\ \mathrm{admissible}}}
2^{c(\sigma)+b(\sigma)}}.
\]
For a fixed labeling of \(V\), exactly \(2^{r(r+1)/2}\) multiplication tables realize \(H\). The automorphism group of any such semigroup is exactly the stabilizer of its table under \(G\). In particular, **all** realizations of \(H\) are rigid if and only if no nonidentity graph automorphism is admissible.

For the edgeless graph \(\overline K_r\), the result specializes to the explicit integer-partition formula
\[
|\mathcal N(\overline K_r)|=
\sum_{\substack{\lambda\vdash r\\\text{every part of }\lambda\text{ odd}}}
\frac{2^{\,(r+\ell(\lambda))/2+\sum_{i<j}\gcd(\lambda_i,\lambda_j)}}
{\prod_{j\ge1}j^{m_j(\lambda)}m_j(\lambda)!}.
\]
Its values at \(r=2,3,4,5,6\) are \(4,12,48,296,3040\). Additional graph-conditioned values are \(|\mathcal N(C_4)|=144\), \(|\mathcal N(2K_2)|=170\), and \(|\mathcal N(C_5)|=3280\).

A sampling consequence follows: when a multiplication table is chosen uniformly from the labeled cubic-nilpotent semigroups having two central elements and \(r\) noncentral elements, its commuting graph is exactly \(G(r,1/2)\) conditioned on having no universal vertex. Thus its total-variation distance from the unconditioned \(G(r,1/2)\) law is at most \(r2^{-(r-1)}\).

## Assumptions and scope

All semigroups are finite, associative, and have a distinguished absorbing zero. The phrase *strictly cubic-nilpotent* means every product of three elements is zero and some product of two is nonzero. A universal vertex is adjacent to every other vertex; this is excluded because vertices of the commuting graph are, by definition, noncentral. Isomorphism is ordinary semigroup isomorphism, not anti-isomorphism, and all counts of tables use a fixed labeling of the \(r\) noncentral vertices and the two intrinsic central elements.

## Proof

**Step 1 (minimal central layer).** If \(S^3=\{0\}\ne S^2\), then all elements of \(S^2\) annihilate \(S\) on both sides and so belong to \(Z(S)\). Both \(0\) and some nonzero element lie in \(S^2\), hence \(|Z(S)|\ge2\). Since \(|S\setminus Z(S)|=r\) and \(|S|=r+2\), necessarily \(Z(S)=S^2=\{0,z\}\), with \(z\ne0\). Any product involving \(0\) or \(z\) is zero. Accordingly a multiplication table is completely specified by an array \(m:V\times V\to\{0,z\}\). Conversely every such array yields an associative, cubic-nilpotent multiplication because each triple product is zero.

**Step 2 (exact graph fiber).** For distinct \(u,v\), commutation is equivalent to \(m(u,v)=m(v,u)\). Thus when \(uv\in E\), the two entries must be equal; when \(uv\notin E\), they must be opposite. Each diagonal entry is free, and each unordered distinct pair contributes one independent bit. Hence the number of labeled tables is \(2^{r+\binom r2}\). Because no vertex of \(H\) is universal, each vertex fails to commute with something and remains outside the center. At least one nonedge exists and forces \(z\) to occur as a product. Therefore every counted table is strictly cubic-nilpotent with center exactly \(\{0,z\}\), and every desired semigroup appears uniquely in this family after labeling its noncentral vertices.

**Step 3 (isomorphisms).** An isomorphism preserves the zero, the center, and the unique nonzero element \(z\) of the center. Its restriction to \(V\) preserves commutation, so it belongs to \(G\). Conversely a permutation in \(G\) is a semigroup isomorphism between two tables precisely when it carries one table into the other. Thus \(\mathcal N(H)\) is exactly the orbit set of this table family under \(G\); automorphism groups are its point stabilizers.

**Step 4 (fixed tables).** Fix \(\sigma\in G\). Each of its \(c(\sigma)\) vertex cycles forces all diagonal entries on that cycle to have a common value, with two choices. For unordered pairs \(\{u,v\}\), the permutation action has exactly \(b(\sigma)\) orbits: an \(\ell\)-cycle contributes \(\lfloor\ell/2\rfloor\) within-cycle distance classes, and two disjoint cycles of lengths \(a,b\) contribute \(\gcd(a,b)\) pair-orbits. Since \(\sigma\) preserves edges, each pair-orbit lies entirely within the edges or the nonedges.

On an edge pair-orbit, the two directed entries coincide, and one bit determines the entire orbit. On a nonedge pair-orbit, the two directed entries are complementary. This is consistent with \(\sigma\)-invariance unless some power of \(\sigma\) interchanges the endpoints of a pair in that orbit. Such interchange occurs if and only if the endpoints are antipodes in one even-length cycle of \(\sigma\). Therefore fixed tables exist precisely when every such antipodal pair is an edge of \(H\). In that case each of the \(b(\sigma)\) pair-orbits contributes one independent bit, giving \(2^{c(\sigma)+b(\sigma)}\) fixed tables; otherwise the fixed-point count is zero. Burnside's lemma now gives the boxed formula. The fixed-point count also proves the rigidity criterion, since a nontrivial automorphism of a table exists precisely when a nonidentity admissible \(\sigma\) fixes it.

**Step 5 (edgeless and sampling cases).** For an edgeless graph, admissibility forces all cycles of \(\sigma\) to be odd. On a cycle type \(\lambda\vdash r\) with \(t=\ell(\lambda)\) odd cycles, the exponent simplifies to \((r+t)/2+\sum_{i<j}\gcd(\lambda_i,\lambda_j)\); grouping permutations by cycle type and using the conjugacy-class factor \(\prod_j j^{m_j}m_j!\) gives the stated partition sum. Finally, the labeled-table count is constant over all graphs on \(r\) labeled vertices with no universal vertex. Choosing a table uniformly therefore chooses such a graph uniformly. Under \(G(r,1/2)\), the probability that a fixed vertex is universal is \(2^{-(r-1)}\), and a union bound yields the stated total-variation estimate.

## Verification

The standalone standard-library program `verify_minimal_nilpotent_graph_fibers.py` independently (i) enumerates all simple labeled graphs with no universal vertex for \(2\le r\le4\), (ii) constructs every compatible binary multiplication table, (iii) computes orbits by explicit graph automorphism permutations, and (iv) compares these exhaustive orbit counts to the cycle formula and its antipodal criterion. It checks all \(46\) eligible graphs in those ranges. A second calculation gives the edgeless counts through \(r=6\), together with \(C_4\), \(2K_2\), and \(C_5\). Run with `python verify_minimal_nilpotent_graph_fibers.py`. The final output token is `GRAPH_CONDITIONED_NILPOTENT_SEMIGROUP_FIBERS_VERIFIED`. These are finite checks; the arbitrary-order statement follows from the proof, not from extrapolation.

## Relationship to prior work

Giudici and Kuzma (2015), Theorem 2.2, already prove that every finite graph without a universal vertex is the commuting graph of a semigroup of order two greater than its vertex count; the realization and its order are **not claimed as new**. Distler and Mitchell (2012) already count all degree-three nilpotent semigroups by order, including isomorphism classes, but their global totals do not resolve the fiber of each prescribed commuting graph. Dolinka, FitzGerald, and Mitchell (2024), especially Section 4, give the general table-partition orbit framework; Section 7 identifies symmetric pair-orbits produced by even-cycle antipodes, which is **explicitly credited**. The claim here is the *graph-conditioned* fiber formula under the smaller group \(\operatorname{Aut}(H)\), its edge-dependent admissibility test, the complete rigidity criterion for this fiber, and the graph distribution resulting from equal fiber sizes. These conclusions require imposing fixed edge/nonedge commutation constraints on the general table action; they are not counts of the unrestricted table orbits or of commutative semigroups.

## Limitations

Only strict cubic nilpotency, the minimum possible central-layer size two, and commuting graphs without universal vertices are addressed. The formula requires knowing \(\operatorname{Aut}(H)\); it does not guarantee a computationally efficient evaluation for arbitrary large graphs. The graph-conditioned formula is a specialization and refinement of established nilpotent-semigroup orbit-counting techniques, not an independent replacement for the general enumeration. Although the cited primary texts were inspected, historical priority against every earlier equivalent formulation is not certified. Independent external mathematical verification has not been performed.

## References

- M. Giudici and B. Kuzma, *Realizability problem for commuting graphs*, first public 2015-05-20, https://arxiv.org/abs/1505.05397 (Theorem 2.2 and its construction).
- A. Distler and J. D. Mitchell, *The number of nilpotent semigroups of degree 3*, first public 2012-01-17, https://arxiv.org/abs/1201.3529 (Sections 2, 5, 6).
- I. Dolinka, D. G. FitzGerald, and J. D. Mitchell, *Semirigidity and the enumeration of nilpotent semigroups of index three*, first public 2024-11-01, https://arxiv.org/abs/2411.00466 (Sections 1, 4, 7).
- C. Bauer and N. Greenfeld, *Commuting Graphs of Boundedly Generated Semigroups*, first public 2017, https://arxiv.org/abs/1710.05250 (additional semigroup realizations).
