# A sharp girth-five sphere-wedge theorem for ordered graph length nerves

## Finding

Let \(G=(V,E)\) be a finite connected simple graph with \(v=|V|\ge2\), \(e=|E|\ge1\), and no cycles of lengths three or four. Give its vertices the unit-edge shortest-path metric. For \(r\ge0\), define the ordered length nerve \(N_{\le r}(G)\) to be the simplicial set whose \(n\)-simplices are tuples \((x_0,\ldots,x_n)\in V^{n+1}\) with \(\sum_{j=1}^{n}d(x_{j-1},x_j)\le r\), with ordinary face deletion and adjacent-repetition degeneracies. Write \(X_r=|N_{\le r}(G)|\).

**Theorem.** The first two positive integer stages satisfy
\[
 X_1\simeq\bigvee^{2e-v+1}S^1,\qquad
 X_2\simeq |G|\vee\bigvee^e S^2
 \simeq \bigvee^{e-v+1}S^1\vee\bigvee^e S^2.
\]
In particular, \(\widetilde H_1(X_2;\mathbb Z)\cong\mathbb Z^{e-v+1}\), \(\widetilde H_2(X_2;\mathbb Z)\cong\mathbb Z^e\), and all other reduced integral homology vanishes.

There is a canonical \(\operatorname{Aut}(G)\)-equivariant identification
\[
 H_2(X_2;\mathbb Z)\cong C_1^{\mathrm{or}}(G;\mathbb Z),
\]
where \(C_1^{\mathrm{or}}(G;\mathbb Z)\) is the signed oriented-edge lattice: its generators \([u,v]\) for graph edges satisfy \([v,u]=-[u,v]\). For an oriented edge \(u\to v\), the corresponding primitive homology class is represented by the normalized two-cycle
\[
 z_{u,v}=\langle u,v,u\rangle-\langle v,u,v\rangle,
 \qquad z_{v,u}=-z_{u,v}.
\]
Thus an automorphism reversing an edge negates its corresponding two-dimensional generator.

The first persistent homology transition is integral and natural:
\[
 0\longrightarrow\mathbb Z[E]\overset{\iota}{\longrightarrow}
 H_1(X_1;\mathbb Z)\longrightarrow H_1(X_2;\mathbb Z)
 \longrightarrow0,
\]
where \(\mathbb Z[E]\) is the **unsigned** edge-permutation lattice and \(\iota(\{u,v\})=[\langle u,v\rangle+\langle v,u\rangle]\). The sequence is exact as \(\mathbb Z[\operatorname{Aut}(G)]\)-modules. Therefore, for every field, exactly \(e\) first-homology intervals die at length two, while \(e\) second-homology intervals are born there; the \(e-v+1\) graph-cycle classes survive that transition. Nothing is asserted about their later death times.

The exclusion of triangles and quadrilaterals is sharp for this uniform statement. For the three-cycle and four-cycle, respectively, exact computations give \((\beta_1(X_2),\beta_2(X_2))=(0,8)\) and \((0,7)\), rather than the predicted \((1,3)\) and \((1,4)\).

## Assumptions and scope

All graph edges have length one. A graph of girth at least five means no triangle and no four-cycle; acyclic graphs qualify. The word **ordered** is essential: \(N_{\le r}\) is a simplicial set, not the unordered Vietoris--Rips or graph-Čech simplicial complex. Its nondegenerate simplices have no equal consecutive vertices, but may have repeated nonconsecutive vertices, so \(\langle u,v,u\rangle\) is a genuine two-cell. A pair \((u,w)\) with \(d(u,w)=2\) is a genuine directed one-cell. A face is deleted in the simplicial set, and a degenerate face contributes zero in normalized chains. The theorem is a nonequivariant homotopy classification with a separately specified natural integral action on homology; it is not a claim of an equivariant wedge splitting.

## Proof

**1. Describe every nondegenerate cell at length two.** Each nondegenerate \(n\)-simplex has length at least \(n\), hence no cells exist above dimension two. The vertices are \(V\). The directed one-cells are \(\langle u,w\rangle\) for \(d(u,w)=1\) or \(2\). Every two-cell is a directed length-two walk \(\langle u,t,w\rangle\) along graph edges. If \(u=w\) it is a backtrack; otherwise its endpoints have distance two because triangles are forbidden. The boundary is
\[
 \partial\langle u,t,w\rangle
 =\langle t,w\rangle-\langle u,w\rangle+\langle u,t\rangle
\]
when \(u\ne w\), and \(\partial\langle u,t,u\rangle=\langle t,u\rangle+\langle u,t\rangle\) because the middle deleted face is degenerate.

**2. Collapse the length-two shortcuts.** For every ordered pair \((u,w)\) with \(d(u,w)=2\), the intervening vertex \(t\) on a shortest path is unique: two such vertices produce a four-cycle. Thus its directed one-cell \(\langle u,w\rangle\) occurs as a face of exactly one two-cell, namely \(\langle u,t,w\rangle\). There are no three-cells, so this is an elementary free CW face pair. Collapse all these pairs. The pairs are disjoint because no other two-cell contains any of the shortcut directed edges, and removing them creates no ambiguity. The resulting two-dimensional CW complex has two oppositely directed edges for each underlying graph edge, together with precisely two backtrack disks \(B_{u,v}=\langle u,v,u\rangle\) and \(B_{v,u}=\langle v,u,v\rangle\) attached along the same directed bigon \(\langle u,v\rangle+\langle v,u\rangle\).

**3. Extract the wedge type.** Attach just one of the two backtrack disks for each unoriented edge. Each such disk identifies the reversed arc up to homotopy with the negative of the forward arc. Equivalently, the complex formed by these chosen disks is a mapping cylinder of the evident cellular collapse onto the usual geometric graph \(|G|\); explicitly, the chosen disk and the reversed directed arc constitute a free relative CW pair after omitting its partner backtrack disk. This intermediate complex deformation retracts onto \(|G|\). Attach the second disk for each edge. Its attaching bigon is now nullhomotopic, since it already bounds the first disk. Attaching a disk along a nullhomotopic based loop contributes a wedge summand \(S^2\). Repeating this for all \(e\) edges yields \(X_2\simeq |G|\vee\bigvee^eS^2\). The graph has cycle rank \(e-v+1\). At scale one only the vertices and the \(2e\) directed graph arcs exist, so \(X_1\) is a connected graph with first Betti number \(2e-v+1\). No step relies on finite sampling, and the cellular collapse respects integral attaching degrees.

**4. Verify the primitive generators and the automorphism character.** Each pair of backtrack disks has identical cellular boundary, so \(z_{u,v}=B_{u,v}-B_{v,u}\) is an integral cycle. Shortcut collapses eliminate all other two-cells by elementary unit-incidence operations. In the residual complex, the two backtrack disks for each edge have the same primitive (coefficient-one) boundary on their own pair of directed arcs, disjoint from other edges' directed arcs. Consequently the kernel of the degree-two boundary is precisely the free lattice generated by these \(e\) differences. An automorphism sends \(z_{u,v}\) to \(z_{g(u),g(v)}\), which reverses sign when it reverses the chosen orientation of the image edge. This proves the integral \(\operatorname{Aut}(G)\)-module claim, without claiming an equivariant collapse.

**5. Identify the exact persistence kernel.** At length one, the two directed arcs over every graph edge yield the primitive backtrack one-cycle \(b_{u,v}=\langle u,v\rangle+\langle v,u\rangle\). The \(e\) such cycles are independent and generate a primitive sublattice of \(H_1(X_1;\mathbb Z)\): quotienting the double-directed graph cycle lattice by them is the ordinary integral graph cycle lattice. Every \(b_{u,v}\) becomes a backtrack-disk boundary at length two. Step 2 shows all additional length-two shortcut edges are removed by unit-incidence cells, so no further degree-one classes are killed. The quotient of first homology is exactly \(H_1(G;\mathbb Z)\), and the exact sequence follows. The edge cycle \(b_{u,v}\) is unchanged by exchanging endpoints, giving the unsigned edge-permutation kernel, unlike the signed degree-two representation.

**6. Sharpness of the short-cycle hypothesis.** A triangle adds length-two two-cells whose three vertices are distinct and pairwise adjacent, thereby killing the graph's triangular loop. A quadrilateral makes some distance-two ordered edge occur in two two-cells, preventing the unique-free-face elimination and killing the graph's quadrilateral loop. The explicit exact chain computations recorded below check the first two counterexamples, showing the excluded structures genuinely change the invariants.

## Verification

Run `python verify_enriched2.py` with Python 3 and SymPy. The script enumerates all nondegenerate cells and constructs the normalized integer boundary matrices through degree two, verifies \(\partial_1\partial_2=0\), computes ranks in three distinct characteristics (two, three and 101), checks explicit edge two-cycles, and compares with the claimed ranks. It tests the edge, paths, stars, five- and six-cycles, a lollipop, and a three-arm theta graph, plus triangles and quadrilaterals outside the hypotheses. Reported results for the five-cycle are \((\beta_1,\beta_2)=(1,5)\), for the three-arm length-three theta \((2,9)\), and for the two excluded short cycles \((0,8)\) and \((0,7)\). The exact integer CW proof above, not finite-field testing, establishes integral torsion-freeness and the universal statement. These tests do not classify larger filtration lengths.

## Relationship to prior work

Melodia's *Persistent Magnitude Homology for Quantitative Equational Theories* (arXiv:2608.21479, publicly available since 21 August 2026) establishes that length-nerve filtrations generate persistent magnitude homology; Proposition 4.4 identifies their normalized chain complexes, and Lemma 4.6 already gives the elementary observation that a backtrack one-cycle dies by twice its edge length. That general observation is an acknowledged input, not an originality claim. Melodia does **not** give this sharp girth-five homotopy classification, the exact primitive first-homology kernel in its graph family, or the signed integral action on two-dimensional homology. His examples concern a small metric polygon and quantitative semilattice spaces, not graphs of arbitrary girth-five branching and cycle rank.

Ivanov and Xu's work on ordered \(\ell^1\)-Vietoris--Rips complexes distinguishes the ordered simplicial-set construction from the unordered Rips complex, supplying important background but not this all-graph scale-two homotopy theorem. A published high-girth **graph-Čech nerve of a Cartesian prism** has the same nonequivariant wedge multiplicities for a given base graph, but it uses a different ambient space and unordered closed-ball nerve. In that construction, the integral second-homology representation is the **unsigned** edge permutation lattice, not the signed oriented-edge lattice proved here; its first-homology kernel also has a different integral symmetry action. These matching Betti numbers therefore do not supply this result by equivalence of constructions. Other indexed work on Boolean Čech nerves and symmetrized length-Rips persistence likewise addresses different spaces. No uniqueness assertion follows from a negative literature search.

## Limitations

Only finite connected simple unit-edge graphs without triangles or four-cycles, and only the inclusive length-one and length-two stages, are classified. The proof supplies a nonequivariant CW homotopy splitting and natural integral homology modules, not an equivariant CW splitting or later-scale persistence barcode. The sharpness examples are finite checks; no universal theorem about every graph containing short cycles is claimed. Equivalent unindexed prior literature may exist. Independent validation of the proof has not been performed.

## References

1. Luciano Melodia, *Persistent Magnitude Homology for Quantitative Equational Theories*, arXiv:2608.21479v2, originally posted 21 August 2026, particularly Sections 4, 5, 8 and Lemma 4.6. https://arxiv.org/abs/2608.21479
2. Sergei O. Ivanov and Xiaomeng Xu, *On \(\ell^p\)-Vietoris--Rips complexes*, arXiv:2411.01857, originally posted 4 November 2024, especially the ordered simplicial-set construction. https://arxiv.org/abs/2411.01857
3. *A high-girth prism Čech collapse and its integral symmetry modules*, publicly available scientific comparison, 2026. Its graph-Čech construction on a prism is distinct from the ordered length nerve on the base graph.
