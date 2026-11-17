# A sharp Alexander-dual collapse for ordinary three-cut complexes of cycle powers

## Finding
For integers \(p\ge2\) and \(n\ge4p+1\), the Alexander dual of the ordinary three-cut complex of \(C_n^p\) admits a fully explicit elementary simplicial collapse
\[
\Delta_3(C_n^p)^\vee\searrow
\operatorname{Cl}(C_n^p)\cup
\bigl\{\{a,b\}:d_{C_n}(a,b)\ge2p+1\bigr\}.
\]
The notation on the right means adjoining these edges and their faces to the clique complex. The resulting complex is homotopy equivalent to \(\bigvee^{1+n(n-4p-1)/2}S^1\). Therefore
\[
\widetilde H_i(\Delta_3(C_n^p);\mathbb Z)=
\begin{cases}
\mathbb Z^{1+n(n-4p-1)/2},&i=n-4,\\
0,&i\ne n-4.
\end{cases}
\]
This statement includes the previously uncovered parameter range \(4p+1\le n<6p-3\) when \(p\ge5\). At the lower endpoint, the Alexander dual is homotopy equivalent to a single circle.

## Assumptions and scope
The graph has vertex set \(V=\mathbb Z/n\mathbb Z\), with distinct vertices adjacent precisely when their circular distance \(d(a,b)=\min\{|a-b|,n-|a-b|\}\) is at most \(p\). The ordinary three-cut complex \(\Delta_3(G)\) has as its facets the complements of triples \(T\subseteq V\) for which the induced three-vertex graph \(G[T]\) is disconnected. Its Alexander dual \(K=\{\sigma\subseteq V:V\setminus\sigma\notin\Delta_3(G)\}\) therefore consists exactly of subsets with **no disconnected induced triple**. In particular, a triple is allowed precisely when it contains at least two edges of \(G\). The graph is neither a path power nor a total three-cut complex.

## Proof
**1. Each dual face has at most one missing edge.** Call a pair \(ab\) a missing edge if \(p<d(a,b)\le\lfloor n/2\rfloor\). The absence of disconnected triples is equivalent to the complement of \(G[\sigma]\) having maximum degree at most one: a vertex missing two neighbors creates a disconnected triple, and a disconnected triple must have such a vertex. For any missing pair \(ab\), write \(C(a,b)=N_G(a)\cap N_G(b)\). For \(n\ge4p+1\), the shorter circular arc from \(a\) to \(b\) has length \(d=d(a,b)\). Directly intersecting the two cyclic radius-\(p\) neighborhoods gives
\[
|C(a,b)|=\begin{cases}2p-d+1,&p<d\le2p,\\0,&d\ge2p+1.\end{cases}
\]
When nonempty, \(C(a,b)\) is a consecutive subinterval of that shorter arc, hence spans a clique. If a face \(\sigma\in K\) contains missing pair \(ab\), every other vertex must lie in \(C(a,b)\). As \(C(a,b)\) is a clique, no second missing pair can occur. Thus either \(\sigma\in\operatorname{Cl}(G)\), or it has a **unique** missing pair \(ab\) and takes the form \(\{a,b\}\cup T\) with \(T\subseteq C(a,b)\). Conversely, all such faces are allowed.

**2. Elementary collapse.** Divide missing pairs into *near* pairs with \(p<d\le2p\) and *far* pairs with \(d\ge2p+1\). For each near pair choose one vertex \(c(a,b)\in C(a,b)\), e.g. its smallest numerical representative. Pair every face \(\{a,b\}\cup T\), with \(T\subseteq C(a,b)\setminus\{c(a,b)\}\), with its extension \(\{a,b\}\cup T\cup\{c(a,b)\}\). Perform these pairs in descending order of \(|T|\) for that missing pair, and then move to any other near pair. At the step for \(T\), every other possible coface of its lower face contains another vertex of \(C(a,b)\setminus(T\cup\{c(a,b)\})\) and has already been removed. No face from a different missing-pair fiber can be a coface because the missing pair is unique. Therefore each lower face is free, each step is an elementary simplicial collapse, and all near-pair fibers disappear. Far pairs have no common neighbor, so only their edges remain. This yields the displayed collapse onto \(Y\).

**3. Homotopy type of the remainder.** The clique complex \(\operatorname{Cl}(C_n^p)\) is a circle for \(n>3p\); here is a direct nerve argument. For each vertex \(i\), take the closed circular arc from \(i\) to \(i+p\), of length \(p\). A set of starting vertices forms a graph clique exactly when its arcs have a common intersection: if all starts are within a cyclic interval of length \(p\), the arcs meet; conversely, any clique can be lifted to \([-p,p]\) around one vertex. If there are vertices on both sides, their extremal distances must sum to at most \(p\), because the alternative circular distance exceeds \(p\) when \(n>3p\). Thus every clique lies in such an interval. As these short arcs cover the circle and their nonempty finite intersections are contractible, the nerve lemma gives \(|\operatorname{Cl}(G)|\simeq S^1\). The number of far edges is exactly \(M=n(n-4p-1)/2\): there are \(n-1-4p\) far neighbors at each vertex, and every edge is counted twice. Attaching \(M\) edges to a connected circle complex without new vertices adds \(M\) independent free loops, giving \(|Y|\simeq\bigvee^{M+1}S^1\).

**4. Integral homology of the original cut complex.** Combinatorial Alexander duality over \(\mathbb Z\) gives \(\widetilde H_i(\Delta_3(G);\mathbb Z)\cong\widetilde H^{n-i-3}(K;\mathbb Z)\). The dual is a wedge of circles and has torsion-free first cohomology of rank \(M+1\). The homology formula follows in every degree.

## Verification
The standalone Python 3 program in `code/verify_cycle_dual.py` independently constructs the entire Alexander dual from all disconnected induced triples, rather than using the proposed description; it then constructs every proposed collapse pair and checks that its lower face has exactly one remaining immediate coface at its turn. It also independently tests the surviving faces and Euler characteristic. Exhaustive instances cover \((p,n)=(2,9),(2,10),(2,11),(3,13),(3,14),(4,17)\), plus a small out-of-scope sanity check. For \((p,n)=(5,21),(5,22),(6,25),(8,33)\), the program independently tests the common-neighborhood and near/far-pair counts without enumerating all simplices. These finite checks corroborate, but do not replace, the universal argument. See `code/OUTPUT.txt` for the actual recorded run.

## Relationship to prior work
Chauhan and Shukla (arXiv:2603.23155, first public 2026-03-24) establish **shellability and sphere-wedge homotopy of the original ordinary three-cut complex** for \(n\ge6p-3\). Their Theorem 1.4 already implies the displayed homology formula in that range; the new portion concerns the entire sharper range \(n\ge4p+1\), especially \(p\ge5\) and \(4p+1\le n<6p-3\), together with an explicit **simple-homotopy collapse of the Alexander dual**, not an assertion of shellability. Their paper states the boundary \(n\ge4p+1\) as a proposed shellability range; this result establishes a weaker but complete integral homology conclusion at that boundary. Earlier results solve \(p=2\), and published individual cases solve \(p=3,4\); those are not counted as new. Bravo (arXiv:2602.21427) studies **total** cut complexes and bounded independence complexes of powers of cycles, which differ in the forbidden-triple condition and do not imply this result. Adamaszek (arXiv:1104.0433) computes clique complexes of cycle powers; its circle classification is used explicitly.

## Limitations
No claim that the ordinary cut complex is shellable, a sphere wedge, or even simply connected is made for the new parameter range. The simple-homotopy collapse concerns only its **Alexander dual**; Alexander duality supplies integral homology, not a homotopy equivalence for the original cut complex. No extension to larger cut size or arbitrary circulants is claimed. Earlier equivalently phrased results not indexed in the searches may exist; there has been no independent mathematical audit.

## References
- P. Chauhan and S. Shukla, *Shellability of 3-cut complexes of powers of cycle graphs*, arXiv:2603.23155, first posted 2026-03-24. https://arxiv.org/abs/2603.23155
- P. Chauhan, S. Shukla, and K. Vinayak, *Shellability of 3-Cut Complexes of Squared Cycle Graphs*, arXiv:2406.01979, first posted 2024-06-04. https://arxiv.org/abs/2406.01979
- A. Carnero Bravo, *Total cut complexes and their duals*, arXiv:2602.21427, first posted 2026-02-24. https://arxiv.org/abs/2602.21427
- M. Adamaszek, *Clique complexes and graph powers*, arXiv:1104.0433, first posted 2011-04-03. https://arxiv.org/abs/1104.0433
- Combinatorial Alexander duality and the nerve lemma, in their standard integral forms.
