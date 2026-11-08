# Mixed-dimensional clique-free windmills and their integral automorphism modules

## Finding
Let \(t\ge3\) and \(k\ge2\) be integers. For any positive integers \(a_1,\ldots,a_k\), form the generalized windmill graph
\[
G=K_1\vee\left(K_{a_1}\sqcup\cdots\sqcup K_{a_k}\right).
\]
The graph has a central vertex \(v\) and \(k\) disjoint clique blades \(V_i\) of sizes \(a_i\). Write \(X=\mathsf{CF}_t(G)\) for the simplicial complex of subsets of \(V(G)\) containing no complete subgraph on \(t\) vertices. If any \(a_i<t-1\), then \(X\) is a simplicial cone and hence contractible.

If every \(a_i\ge t-1\), put
\[
p=k(t-1)-1,\quad q=k(t-2),\quad
A=\prod_{i=1}^{k}\binom{a_i-1}{t-1},\quad
B=\prod_{i=1}^{k}\binom{a_i-1}{t-2},
\]
where an out-of-range binomial coefficient is zero. Then the **integral homotopy type** is
\[
\boxed{\ |X|\simeq\left(\bigvee^A S^p\right)\vee\left(\bigvee^B S^q\right).\ }
\]
Both summands occur for every \(a_i\ge t\), giving genuinely different dimensions because \(p-q=k-1\ge1\); the upper wedge is absent if any \(a_i=t-1\).

The full automorphism group \(\Gamma=\operatorname{Aut}(G)\) fixes the unique central vertex and acts by permutations inside equally sized blades and by exchanging these blades. Let \(P_i=\mathbb Z[V_i]\) be the vertex-permutation lattice and \(U_i=\ker(\varepsilon_i:P_i\to\mathbb Z)\), where \(\varepsilon_i\) sums coefficients. The natural integral homology lattices, with the full \(\Gamma\)-action, are
\[
\boxed{\begin{aligned}
\widetilde H_p(X;\mathbb Z)&\cong_{\mathbb Z[\Gamma]}\bigotimes_{i=1}^{k}\bigwedge^{t-1} U_i,\\
\widetilde H_q(X;\mathbb Z)&\cong_{\mathbb Z[\Gamma]}\bigotimes_{i=1}^{k}\bigwedge^{t-2} U_i.
\end{aligned}}
\]
All other reduced integral homology groups vanish. A blade permutation \(\beta\) acts on the indicated tensor factors with the Koszul factor \(\operatorname{sgn}(\beta)^r\), where \(r=t-1\) in the first line and \(r=t-2\) in the second. Within each blade, the usual exterior power of the permutation action on \(U_i\) is used. This specifies the integral representation, not only its rank or its rational character.

In particular, for an automorphism \(g\in\Gamma\), let \(\beta\) be its blade permutation. For a blade orbit \(\mathcal O\) of length \(d\), its monodromy \(\pi_{\mathcal O}\) is the composition of the \(d\) internal vertex bijections around that orbit, a permutation of any one blade in \(\mathcal O\). For \(r\ge0\), set
\[
c_r(\pi)=[z^r]\,\frac{\prod_{\ell\text{ a cycle length of }\pi}(1-(-z)^\ell)}{1+z}.
\]
The complete rational characters in the two nonzero degrees are
\[
\boxed{\operatorname{tr}\bigl(g\mid\widetilde H_{d_r}(X;\mathbb Q)\bigr)
=\operatorname{sgn}(\beta)^r\prod_{\mathcal O}c_r(\pi_{\mathcal O}),\quad r\in\{t-2,t-1\}.}
\]
Here \(d_{t-1}=p=k(t-1)-1\) and \(d_{t-2}=q=k(t-2)\). In particular, the character formula is to be read with those specified degrees, rather than as a general formula for arbitrary \(r\).

For example, with \(t=3\) and two triangular blades, \(X\simeq S^3\vee\bigvee^4S^2\). Swapping the two blades without changing internal labels has rational traces \(+1\) in degree three and \(-2\) in degree two.

## Assumptions and scope
All graphs are finite, simple and undirected. The join \(\vee\) of graphs adds all edges between the joined vertex sets; \(\sqcup\) denotes disjoint union. The clique-free complex contains the empty face. The homotopy statement is an ordinary, not equivariant, homotopy equivalence; the homology-lattice statement is nevertheless canonically \(\Gamma\)-equivariant and integral. The cases \(a_i<t-1\) are contractible, and the exterior-power formulas are asserted only when all \(a_i\ge t-1\). In the character formula, the transposition of tensor factors includes their graded orientation signs. Unreduced integral homology is obtained by adding one copy of \(\mathbb Z\) in degree zero, since the complexes are connected in the noncontractible range.

## Proof
**1. The two joins.** A forbidden \(t\)-clique lies wholly inside a blade, or contains \(v\) and \(t-1\) vertices of a blade. Thus the vertex deletion of \(v\) in \(X\) is
\[
D=\ast_{i=1}^k\{F\subseteq V_i:|F|\le t-1\},
\]
while the link of \(v\) is
\[
L=\ast_{i=1}^k\{F\subseteq V_i:|F|\le t-2\}.
\]
The symbol \(\ast\) denotes simplicial join. The exact simplicial identity \(X=D\cup(v\ast L)\), with intersection \(L\), exhibits \(X\) as the mapping cone of \(L\hookrightarrow D\).

**2. Cone boundary.** If \(a_j<t-1\), that blade is an entire simplex factor in both the deletion and link, and any chosen vertex \(w\in V_j\) lies in no \(t\)-clique of \(G\). Every face therefore extends by \(w\), proving that \(X\) is a cone. Henceforth assume all \(a_i\ge t-1\).

**3. Skeletons and their integral modules.** Let \(K(a,r)=\{F\subseteq[a]:|F|\le r\}\), where \(1\le r\le a\). This is the \((r-1)\)-skeleton of the full simplex on \(a\) vertices. Its reduced integral chain complex in positive degrees is the usual truncated augmented simplex complex, with \(\widetilde C_{r-1}=\bigwedge^r\mathbb Z^a\) and boundary the contraction \(\iota_\varepsilon\) by the all-ones augmentation map. The full augmented simplex complex is exact, so
\[
\widetilde H_{r-1}(K(a,r);\mathbb Z)=\ker\bigl(\iota_\varepsilon:\bigwedge^r\mathbb Z^a\to\bigwedge^{r-1}\mathbb Z^a\bigr)
\cong\bigwedge^r\ker\varepsilon,
\]
with every other reduced group zero. The displayed isomorphism is equivariant for any permutation of the vertices. If \(r=a\), its right side is zero and \(K(a,a)\) is a simplex. Otherwise the skeleton is homotopy equivalent to a wedge of \(\binom{a-1}{r}\) spheres of dimension \(r-1\), by elementary simplex-face collapses or its standard skeletal CW attachment; in particular it is \((r-2)\)-connected. For \(r=1\), the statement uses the conventional wedge-of-zero-spheres interpretation.

**4. Join connectivity and ranks.** For the deletion, \(D=\ast_iK(a_i,t-1)\). Each factor is either contractible (when \(a_i=t-1\)) or \((t-3)\)-connected. Consequently \(D\) is either contractible or \((p-1)\)-connected and its only possible nonzero reduced homology is in degree \(p=k(t-1)-1\), of rank \(A\). Likewise \(L=\ast_iK(a_i,t-2)\) is a wedge of \(B\) spheres of dimension \(q-1=k(t-2)-1\), with \(B>0\). Since \(q-1\le p-1\) for \(k\ge2\), the inclusion \(L\to D\) is nullhomotopic: its source is a wedge of \((q-1)\)-spheres and its target is \((p-1)\)-connected, or contractible. The mapping cone of a nullhomotopic map is homotopy equivalent to \(D\vee\Sigma L\). Substituting the two wedge decompositions proves exactly the claimed ordinary homotopy type and torsion freeness.

**5. Natural integral symmetry modules.** This is not an appeal to the non-equivariant wedge splitting. The long exact sequence of the mapping cone gives canonical \(\Gamma\)-equivariant isomorphisms \(\widetilde H_p(X;\mathbb Z)\cong\widetilde H_p(D;\mathbb Z)\) and \(\widetilde H_q(X;\mathbb Z)\cong\widetilde H_{q-1}(L;\mathbb Z)\). The degree inequalities in step 4 ensure all potentially interfering groups vanish. The integral join-chain Künneth isomorphisms identify these groups with the stated tensor products of \(\bigwedge^{t-1}U_i\) and \(\bigwedge^{t-2}U_i\). Exchanging two degree-\((r-1)\) reduced homology classes in a join introduces the sign \((-1)^{r^2}=(-1)^r\); hence an arbitrary blade permutation contributes \(\operatorname{sgn}(\beta)^r\), proving the full integral module formulas.

**6. Character calculation.** The splitting \(\mathbb Q[V_i]\cong\mathbb Q\mathbf 1\oplus(U_i\otimes\mathbb Q)\) gives \(\det(1+z\pi\mid U_i\otimes\mathbb Q)=\det(1+z\pi\mid\mathbb Q[V_i])/(1+z)\). Each cycle of length \(\ell\) contributes \(1-(-z)^\ell\), so its \(r\)-th coefficient is \(c_r(\pi)\). For any orbit \(\mathcal O\) of permuted blades, the trace of a cyclic permutation of tensor factors with internal maps is the trace of its monodromy on one factor. Combining orbits and the graded permutation sign proves the displayed character rule.

## Verification
The included standalone Python checker (`verify_windmill.py`) constructs the graph from the edge list, independently enumerates its forbidden \(t\)-cliques and all faces, computes reduced boundary ranks over \(\mathbb F_2\), and compares the results with the claimed Betti numbers for 16 parameter choices. It enumerates 4,861 simplices in total and directly evaluates signed Lefschetz traces of 3,886 graph automorphisms, comparing them with the cycle-index character formula, including exhaustive automorphism tests for five example graphs. The recorded output finishes with `ALL_VERIFY_OK cases=16 simplices=4861 character_tests=3886`. These finite tests are **not** an infinite-family proof or an integral torsion test; the all-parameter integral claims follow from steps 1–6.

## Relationship to prior work
Ghosh and Selvaraja, *Shellability in Clique-Free Complexes of Graphs*, arXiv:2602.09623v1 (first posted 10 February 2026), define the same \(t\)-clique-free complex and prove decomposability and shellability for block graphs, a broader category containing generalized windmills. That shellability result, its known implications, and the basic definition are prior art and are **not** claimed as new. The full preprint was inspected; its results concern shellability, clique attachments, and resolutions, not the two-degree homotopy formula or the full integral automorphism lattice claimed here. Earlier work on \(t\)-clique ideals and higher independence complexes, notably Moradi (2018), likewise addresses other graph classes and algebraic properties. The present result is the explicit integral, representation-theoretic refinement for clique windmills, including inter-blade Koszul signs and character values. Related graph families in other complexes (such as Lovász neighborhood complexes and general-position polynomials) have different definitions and do not imply these formulas.

## Limitations
The homotopy equivalence is not asserted to be equivariant. The integral lattice is established in homology only; attaching maps and geometric fixed-point spaces under automorphism subgroups are not classified. The formula covers joins of one hub with disjoint complete blades (all blade sizes permitted) and \(t\ge3\), \(k\ge2\), not arbitrary block graphs. Qualitative shellability for these graphs follows from the preexisting broad theorem and is not novel. An equivalent representation calculation could exist in unindexed literature, and independent external validation has not occurred.

## References
- Rakesh Ghosh and S. Selvaraja, *Shellability in Clique-Free Complexes of Graphs*, arXiv:2602.09623v1, 10 February 2026. https://arxiv.org/html/2602.09623v1 ; https://arxiv.org/abs/2602.09623 . Full original text inspected, particularly the definition, Theorem 3.3, and Corollary 3.4.
- S. Moradi, *\(t\)-clique ideal and \(t\)-independence ideal of a graph*, Communications in Algebra 46 (2018), DOI 10.1080/00927872.2017.1412445. Earlier algebraic context, not the present integral equivariant result.
