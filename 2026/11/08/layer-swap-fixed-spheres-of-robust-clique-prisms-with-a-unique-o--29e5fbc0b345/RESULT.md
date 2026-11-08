# Layer-swap fixed spheres of robust clique prisms with a unique odd cycle

## Finding

Let \(H\) be a finite simple graph with \(N\ge3\) vertices and let \(P=H\square K_2\). The involution \(\tau\) interchanges the two levels. For each integer \(k\ge2\), the robust clique complex is
\[
\operatorname{Cliq}_k(P)=\{W\subseteq V(P):\alpha(P[W])<k\}.
\]
Here \(\alpha\) is the independence number of the induced graph. If \(H\) is bipartite, then for every \(2\le k\le N\),
\[
\left|\operatorname{Cliq}_k(P)\right|^{\tau}\simeq\bigvee^{\binom{N-1}{k-1}}S^{k-2}.
\]
If \(H\) has exactly one simple cycle of odd length \(\ell\), with any number of even cycles and other edges permitted, then
\[
\boxed{\left|\operatorname{Cliq}_k(P)\right|^{\tau}\simeq\bigvee^{\binom{N-1}{k-1}-\binom{N-\ell}{k-\ell}}S^{k-2}}\qquad(2\le k\le N).
\]
The binomial coefficient is zero for an out-of-range lower index, and a wedge of zero spheres is interpreted as contractible. For \(k>N\), each fixed space is contractible. The result is integral and describes geometric fixed points, not orbit quotients. In fact, an exact simplicial model is obtained as the full \((k-2)\)-skeleton of the simplex on \(V(H)\), with precisely those \((k-1)\)-simplices supported on \(k\)-subsets containing the unique odd cycle added. In the bipartite case no such simplices are added.

## Assumptions and scope

All graphs are finite, simple, undirected, with \(N\ge3\). “Exactly one odd simple cycle” means one undirected simple odd cycle in the entire graph, not one cycle per component; \(H\) need not be connected. Even cycles may occur, including in components disjoint from the odd cycle. The cycle has \(\ell\ge3\) distinct vertices. The convention \(\binom{a}{b}=0\) applies for \(b<0\) or \(b>a\). The ordinary geometric realization is used. The label \(\tau\) is the involution \((v,0)\leftrightarrow(v,1)\).

## Proof

**1. Geometric fixed points and rung orbits.** Every \(\tau\)-orbit of vertices of \(P\) is the two-element rung \(\{(v,0),(v,1)\}\). A point in a geometric simplex is fixed precisely when its barycentric coefficients are equal within each orbit. It follows, by rescaling orbit weights, that the fixed-point space is PL-homeomorphic to a simplicial complex \(F_k(H)\) with vertex set \(V(H)\): a set \(S\subseteq V(H)\) is a face exactly when its full rung union \(S\times\{0,1\}\) belongs to \(\operatorname{Cliq}_k(P)\).

**2. The independence/bipartiteness identity.** For every \(S\subseteq V(H)\),
\[
\alpha\big(P[S\times\{0,1\}]\big)
=\max\{|T|:T\subseteq S,\ H[T]\text{ is bipartite}\}.
\]
Indeed, an independent set of the prism contains at most one vertex in each rung. Its layer labels provide a proper two-coloring of the induced graph on its selected rung labels. Conversely any two-coloring of an induced bipartite subgraph selects one endpoint in each rung, yielding an independent set of the same size. Thus the identity holds for every finite simple \(H\).

If \(H\) is bipartite, the right-hand side is \(|S|\). If \(H\) has exactly one odd cycle \(C\), the induced subgraph \(H[S]\) is bipartite whenever \(C\nsubseteq S\). If \(C\subseteq S\), it is not bipartite, but removing any one vertex of \(C\) destroys the only odd cycle, so the maximum is precisely \(|S|-1\). Therefore \(F_k(H)\) consists of all subsets of cardinality at most \(k-1\) and, in the unique-odd-cycle case, all subsets of cardinality \(k\) containing \(C\). No larger subsets are faces. For \(k>N\), every subset is a face and the complex is a simplex.

**3. The topology of the filled skeleton.** Fix \(2\le k\le N\) and put \(d=k-2\). Let \(L\) be the \(d\)-skeleton of the full simplex with \(N\) vertices. Standard simplex-skeleton collapses give \(L\simeq\bigvee^{\binom{N-1}{k-1}}S^d\). In the unique-odd-cycle case, the extra \((d+1)\)-faces correspond to the \(r=\binom{N-\ell}{k-\ell}\) sets \(C\cup T\), where \(|T|=k-\ell\) and \(T\cap C=\varnothing\). When \(k<\ell\) there are none. For \(k\ge\ell\), choose once and for all one vertex \(c\in C\). In the simplicial boundary of the added face \(C\cup T\), the codimension-one face \((C\setminus\{c\})\cup T\) has coefficient \(\pm1\). It does not appear in the boundary of any other added face, because adjoining a vertex to it to recover a set containing the whole of \(C\) necessarily adjoins \(c\). Thus the matrix of the boundaries of the added cells has an \(r\times r\) diagonal submatrix with entries \(\pm1\). In particular its image is a **primitive** rank-\(r\) subgroup of the simplicial \(d\)-chains, lying in the \(d\)-cycles, so it kills exactly \(r\) integral \(d\)-homology generators and creates no torsion or higher homology. The resulting reduced integral homology is \(\mathbb Z^{\binom{N-1}{k-1}-r}\) in degree \(d\) and zero elsewhere.

For \(k\ge4\), the skeleton \(L\) is \((d-1)\)-connected and the added \((d+1)\)-cells cannot change this connectivity. A map from a wedge of \(d\)-spheres representing a basis of integral \(d\)-homology is a homology equivalence by Hurewicz; the simply-connected homology Whitehead theorem makes it a homotopy equivalence. When \(k=3\), the only possible added face is the triangular odd cycle \(C\) (necessarily \(\ell=3\)), whose unique two-simplex collapses across any one of its edges; the resulting connected graph has cycle rank \(\binom{N-1}{2}-1\). When \(k=2\), the complex consists of \(N\) isolated vertices and is a wedge of \(N-1\) copies of \(S^0\). The bipartite case is just the original skeleton. All asserted homotopy types follow.

## Verification

A standalone standard-library Python verifier reconstructs the full prism independence-number condition from graph adjacency for every subset on nine graphs, including bipartite paths/even cycles, odd cycles of lengths three, five and seven, and odd-cycle graphs with attached trees. It independently reconstructs the quotient simplices, compares the predicted formula, and computes all reduced mod-two Betti numbers by exhaustive boundary-matrix reduction. The verifier checks \(52\) graph/parameter cases with \(2\le k\le N+1\), including contractible endpoints, and reports `ALL_PRISM_FIXED_CHECKS_OK`. It is corroboration; the theorem relies on the all-parameter proof above. Run `python3 verify_prism_fixed.py` with the standard Python 3 library.

## Relationship to prior work

Filakovský introduced and analyzed robust clique complexes for square-sequence graphs, particularly grid graphs, establishing ordinary nonequivariant wedge-of-spheres theorems in its stated regime [1]. The present result concerns **fixed points under exchanging the two layers of a graph prism** and applies to bipartite or one-odd-cycle base graphs at every robust level, so the conclusions do not follow from those ordinary grid homotopy statements. Related graph-complex work has studied symmetry on circular ladders and ordinary robust clique complexes, but rational symmetry characters for different complexes and ordinary homotopy results are insufficient to identify these geometric fixed-point spaces. A targeted novelty search did not locate an identical statement; this is not a claim of exhaustive literature coverage.

## Limitations

The involution must be the simultaneous layer swap of a two-level Cartesian prism; other reflections and subgroups are not classified. If the base graph has two distinct odd cycles, the proof's single-deletion argument fails and no conclusion is claimed. The theorem gives the homotopy types of fixed-point spaces, not full equivariant homotopy equivalences or maps between them. An independent mathematical audit has not been performed.

## References

[1] Marek Filakovský, *The Topology of \(k\)-Robust Clique Complexes in Grid-like Graphs*, arXiv:2602.11365 (first version February 11, 2026), https://arxiv.org/abs/2602.11365.

[2] A. Chandrakar et al., *Topology of total cut complexes and cut complexes of grid graphs*, arXiv:2408.07646 (2024), https://arxiv.org/abs/2408.07646. Used for subject context only, not a premise of the proof.
