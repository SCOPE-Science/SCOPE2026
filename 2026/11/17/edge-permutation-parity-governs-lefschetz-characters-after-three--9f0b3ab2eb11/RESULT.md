# Edge-permutation parity governs Lefschetz characters after threefold edge subdivision

## Finding

For every finite simple graph \(G\), let \(e=|E(G)|\) and let \(G^{[4]}\) be obtained by replacing every edge by a path of length four (three new internal vertices per edge). Every \(g\in\operatorname{Aut}(G)\) induces an automorphism \(g^{[4]}\) of this subdivision. Write \(c_E(g)\) for the number of cycles of the permutation of \(E(G)\) induced by \(g\), and \(\varepsilon_E(g)=\operatorname{sgn}(g|_{E(G)})\). For the *reduced* rational Lefschetz number of the independence complex, the following identity holds for every \(g\):

\[
\widetilde L\bigl(g^{[4]};\operatorname{Ind}(G^{[4]})\bigr)
=(-1)^{c_E(g)}\widetilde L\bigl(g;\operatorname{Ind}(G)\bigr)
=(-1)^e\varepsilon_E(g)\widetilde L\bigl(g;\operatorname{Ind}(G)\bigr).
\]

In particular, if the reduced rational homology of \(\operatorname{Ind}(G)\) is concentrated in degree \(d\), then the reduced homology of \(\operatorname{Ind}(G^{[4]})\) is concentrated in degree \(d+e\), and the resulting representations of \(\operatorname{Aut}(G)\) satisfy

\[
\widetilde H_{d+e}\bigl(\operatorname{Ind}(G^{[4]});\mathbb Q\bigr)
\cong \varepsilon_E\otimes\widetilde H_d\bigl(\operatorname{Ind}(G);\mathbb Q\bigr).
\]

For every \(n\ge2\), the complete-graph specialization yields an explicit symmetric-group module:

\[
\widetilde H_{\binom n2}\bigl(\operatorname{Ind}(K_n^{[4]});\mathbb Q\bigr)
\cong (\operatorname{sgn})^{n-2}\otimes
\ker\bigl(\mathbb Q^n\xrightarrow{\sum}\mathbb Q\bigr).
\]

All other reduced rational homology groups vanish. The underlying ordinary homotopy type of this complex is the **previously implied** wedge \(\bigvee^{n-1}S^{\binom n2}\); the new assertion is its *complete natural symmetric-group homology character*.

## Assumptions and scope

Graphs are finite, simple and loopless; isolated vertices and disconnected graphs are allowed. An empty edge set is allowed, with \(c_E(g)=0\) and \(\varepsilon_E(g)=1\). The three subdivision vertices on a geometric edge have the intrinsic positions at distances one, two, three from an endpoint; thus a graph automorphism exchanging the endpoints of an edge reverses these three positions. The action here is the natural lift of \(\operatorname{Aut}(G)\), not an assertion about all automorphisms of the subdivided graph.

For a finite simplicial complex \(X\), including the augmented empty simplex, define \(\widetilde L(g;X)=\sum_{q\ge-1}(-1)^q\operatorname{tr}(g_*\mid\widetilde H_q(X;\mathbb Q))\). The sign representation \(\varepsilon_E\) is the one-dimensional representation given by the permutation of the **unoriented edge set**. The representation statement is over \(\mathbb Q\), not an asserted integral lattice isomorphism or equivariant homotopy equivalence.

## Proof

**Step 1 (signed invariant independent sets).** For a finite graph \(J\) with automorphism \(h\), put
\[
 Z(J,h)=\sum_{\substack{S\subseteq V(J)\\S\,\text{independent}\\hS=S}}(-1)^{c(h|_S)},
\]
where \(c(h|_S)\) is the number of cycles of the permutation on the selected vertices, and \(c(h|_\varnothing)=0\). The augmented simplicial Hopf trace formula gives \(\widetilde L(h;\operatorname{Ind}(J))=-Z(J,h)\). Indeed, an invariant independent face \(S\) of cardinality \(k\) contributes \((-1)^{k-1}\operatorname{sgn}(h|_S)=(-1)^{c(h|_S)+1}\) to the alternating oriented simplex trace, including \(S=\varnothing\) at degree minus one. The chain and homology traces agree.

**Step 2 (factorization over edge orbits).** Fix a \(g\)-invariant subset \(T\subseteq V(G)\) of original vertices, not presumed independent. The new internal vertices on different original edges have no mutual adjacency. Hence, once \(T\) is fixed, their signed invariant-independent-set enumerator factors over the cycles of \(g\) on \(E(G)\). Let \(O\) be one such cycle, of length \(\ell\), represented by edge \(\{u,v\}\).

If \(g^{\ell}\) preserves both \(u\) and \(v\) individually, the three levels of internal vertices form three separate \(g\)-orbits, with the incompatibility graph a three-vertex path. The selected original endpoints prohibit the respective outer positions. If neither endpoint is selected, the alternating independence sum of that path is \(1-3+1=-1\). If exactly one is selected, it is the sum for a two-vertex edge, \(1-2=-1\). If both are selected, it is the sum for a single available middle vertex, \(1-1=0\).

If \(g^{\ell}\) exchanges \(u\) and \(v\), the outer internal positions together constitute one orbit, while the middle positions constitute a second orbit; these two orbits are incompatible. The \(g\)-invariance of \(T\) forces either both endpoints selected or neither. With neither selected, the alternating sum for this two-vertex incompatibility edge is \(1-2=-1\). With both selected, only the middle orbit is available and the sum is \(1-1=0\).

Thus **in both edge-orbit types** the local sum is \(-1\) if \(T\) does not contain both endpoints of any edge in \(O\), and zero otherwise. This statement treats edge inversions, which are essential for the general automorphism formula.

**Step 3 (the character identity).** Multiplying the local factors shows that the signed sum conditioned on \(T\) vanishes unless \(T\) is independent in \(G\), and equals \((-1)^{c_E(g)}\) otherwise. The selected original vertex-orbit sign remains \((-1)^{c(g|_T)}\). Summing over all invariant \(T\) gives \(Z(G^{[4]},g^{[4]})=(-1)^{c_E(g)}Z(G,g)\), hence the first formula by Step 1. A permutation of \(e\) elements with \(c_E\) cycles has sign \((-1)^{e-c_E}\), proving the second formula.

**Step 4 (homology representations).** Csorba's three-vertex edge-subdivision suspension theorem, applied successively to all original edges, supplies the *nonequivariant* homotopy equivalence \(\operatorname{Ind}(G^{[4]})\simeq\Sigma^e\operatorname{Ind}(G)\). Therefore the assumed homology concentration in degree \(d\) yields concentration in degree \(d+e\) with equal dimensions. The alternating homology traces in the first formula then yield \(\operatorname{tr}(g|\widetilde H_{d+e})=\varepsilon_E(g)\operatorname{tr}(g|\widetilde H_d)\) for every \(g\). Rational representations of finite groups are determined by their characters, proving the representation isomorphism. There is no claim that an arbitrary choice of Csorba's homotopy equivalences is equivariant.

**Step 5 (complete graphs).** For \(K_n\), the independence complex is the discrete \(n\)-point space; its reduced degree-zero homology is the augmentation kernel of the vertex-permutation module. The transposition of two vertices exchanges exactly \(n-2\) pairs of edges and fixes the edge joining them, so its sign on the edge set is \((-1)^{n-2}\). Since transpositions generate the symmetric group, \(\varepsilon_E=(\operatorname{sgn})^{n-2}\). Apply Step 4 with \(d=0\) and \(e=\binom n2\). The ordinary wedge assertion follows only from Csorba's known suspension theorem and is not claimed as new.

## Verification

The standalone reproducible verifier `verify.py` constructs the lifted automorphism on the subdivided graph, independently computes vertex-orbit conflicts and evaluates the signed invariant-independent-set sum recursively. It compares the two sides of Step 3 without using the edge-orbit factorization. It covers every automorphism of every labeled graph on at most four vertices with at most four edges, and six further examples with larger edge orbits and endpoint inversions. The recorded output reports 251 successful graph/automorphism cases, including 70 automorphisms directly inverting a graph edge. The finite checks test the proof but do not constitute a proof for unbounded graphs.

## Relationship to prior work

Péter Csorba, *Subdivision Yields Alexander Duality on Independence Complexes* (2009), establishes the ordinary suspension equivalence after inserting three vertices on each edge, both by Theorem 11 and the all-edge formula in Section 3. That entire nonequivariant assertion is treated here as **known**. The present theorem adds a character identity for every original graph automorphism, including edge-inverting elements, and a natural rational representation classification when the initial homology is concentrated in one degree. It is not a mere restatement of the homotopy-suspension formula: an ordinary homotopy equivalence does not determine how a nontrivial automorphism acts on homology. The classical simplicial Hopf trace identity is also used as a known fact.

Search comparisons with records on subdivided multitheta independence complexes (specialized arm-permutation and pole-reversal characters), Kneser independence modules, and other symmetric graph-complex representations did not exhibit the all-graph edge-permutation sign rule. This absence is not proof of publication priority.

## Limitations

Only the *alternating* reduced rational homology character is determined without additional homology-concentration hypotheses. The stronger graded representation statement requires concentration in one degree; the theorem does not construct a natural equivariant suspension equivalence, determine integral representation lattices, or classify quotient homotopy types. Equivalence to an unindexed older equivariant subdivision argument remains a novelty risk, and there has been no independent mathematical audit.

## References

1. P. Csorba, *Subdivision Yields Alexander Duality on Independence Complexes*, Electronic Journal of Combinatorics **16**(2) (2009), R11, DOI: 10.37236/77. Publicly published 2009-05-12. See Section 3 (all-edge suspension) and Theorem 11 (one-edge suspension).
2. Simplicial Hopf trace formula for finite simplicial automorphisms (standard chain-complex identity), used in its augmented/reduced form.
