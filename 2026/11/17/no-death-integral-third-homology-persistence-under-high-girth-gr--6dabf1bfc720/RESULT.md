# No-death integral third-homology persistence under high-girth graph edge insertions

## Finding
Let \(G\) be any finite connected simple graph of girth at least seven, let \(T\) be any spanning tree, and order the edges of \(E(G)\setminus E(T)\) arbitrarily as \(e_1,\ldots,e_b\), where \(b=|E(G)|-|V(G)|+1\). Put \(G_i=T\cup\{e_1,\ldots,e_i\}\), and write \(K_i=\operatorname{BI}_3(G_i)\) for the vertex-subset complex defined by \(\alpha(G_i[S])\le 2\).

**Theorem (new persistence conclusion).** For every \(1\le i\le b\), the actual inclusion \(K_{i-1}\hookrightarrow K_i\) induces a primitive split monomorphism of integral degree-three homology groups, with a free cokernel of rank \(i\). Equivalently,
\[
H_j(K_i,K_{i-1};\mathbb Z)\cong
\begin{cases}\mathbb Z^i,&j=3,\\0,&j\neq3.\end{cases}
\]
The degree-three integral persistence module therefore has no deaths and exactly \(i\) births at the \(i\)-th non-tree edge. The known absolute calculation \(K_i\simeq\bigvee^{\binom{i+1}{2}}S^3\) is included for context only and is not a novelty claim.

## Assumptions and scope
Graphs are finite and simple; girth of a forest is infinite. A spanning tree exists because \(G\) is connected. Every intermediate graph \(G_i\) has girth at least seven. The complex is the **bounded-independence** (also called three-robust clique) complex on vertex subsets, not the ordinary graph clique complex. All homology groups have integral coefficients. For \(b=0\), the filtration has only the contractible initial term and the assertion about insertion maps is vacuous.

## Proof
**1. Local edge insertion.** Fix connected \(F\) with girth at least seven and a non-edge \(ab\) such that \(F'=F+ab\) still has girth at least seven. Thus \(d_F(a,b)\ge6\). Let \(K=\operatorname{BI}_3(F)\) and \(K'=\operatorname{BI}_3(F')\). A set is a simplex precisely when it contains no independent triple. Because an induced five-vertex triangle-free graph with independence number at most two would have to be a five-cycle, neither complex has a simplex with five or more vertices (every five-set would contain an independent triple). Both are at most three-dimensional.

**2. Exact links.** Set \(A=N_F(a)\), \(B=N_F(b)\), \(Q=F[V(F)\setminus\{a,b\}]\). Distance at least six makes \(A\) and \(B\) disjoint, with no edges joining them, and forbids edges within either neighborhood. The link of the edge \(\{a,b\}\) in \(K\) is precisely the complete bipartite one-dimensional graph \(L_0=K_{A,B}\). The link in \(K'\) is precisely \(L_1=Q\cup K_{A,B}\), with the shared vertices identified. To verify the latter, adding \(ab\) automatically protects the independent-triple condition for triples containing both poles; a pair \(x,y\) completes a permitted four-set exactly when \(xy\) is an edge of \(Q\) or \(x,y\) meet the two different neighborhoods. No two-simplex occurs in either link.

**3. Relative incidence lattice.** Every connected component of \(Q\) meets \(A\cup B\) because \(F\) is connected. Hence \(L_1\) is connected and \(L_0\) is connected and nonempty. With \(n=|V(F)|\), \(m=|E(F)|\), \(p=\deg_F(a)\), \(q=\deg_F(b)\), the relative cellular group \(C_1(L_1,L_0;\mathbb Z)\) has rank \(m-p-q\), and \(C_0(L_1,L_0;\mathbb Z)\) has rank \(n-2-p-q\). Since every vertex of \(Q\) outside \(A\cup B\) has a path into \(L_0\), the integral relative incidence boundary \(C_1\to C_0\) is surjective. Its kernel is therefore a free, saturated lattice of rank \((m-p-q)-(n-2-p-q)=m-n+2=b(F)+1\). Thus \(H_1(L_1,L_0;\mathbb Z)\cong\mathbb Z^{b(F)+1}\) and every other relative group vanishes.

**4. Shift and long exact sequence.** Every newly admitted face of \(K'\setminus K\) contains both poles \(a,b\). Removing the poles from its oriented simplex identifies the relative simplicial chain groups (including the empty-face convention) with those of the relative link pair, shifted upward by two degrees. Since all relative vertices of \(L_1\) are outside \(L_0\), the empty face cancels, and this gives \(H_j(K',K;\mathbb Z)\cong H_{j-2}(L_1,L_0;\mathbb Z)\). Consequently the only nonzero relative group is \(\mathbb Z^{b(F)+1}\) in degree three. In the exact sequence, \(H_2(K)=0\) then forces \(H_3(K)\to H_3(K')\) to be injective with free cokernel. The resulting short exact sequence splits as abelian groups (not canonically).

**5. Iterate.** A tree is chordal, so its bounded-independence complex is contractible (Carnero Bravo, Proposition 15). At stage \(i\), \(b(G_{i-1})=i-1\), giving exactly \(i\) new generators in the cokernel. Induction gives all the assertions about relative groups, no deaths, and total third Betti rank \(\sum_{j=1}^{i}j=\binom{i+1}{2}\). Since the complexes are simply connected by the connected-graph theorem (Carnero Bravo, Proposition 21), standard Hurewicz and Whitehead arguments recover the already-published sphere-wedge homotopy type. None of the persistence assertions follow just from those known absolute ranks.

## Verification
The standalone script `verify_chord.py` recomputes all faces from forbidden independent triples and their mod-two boundary matrices, then checks the exact two links of a newly inserted edge. It covers 28 long-chord cycle cases for lengths \(12\) through \(18\), plus a noncycle 19-vertex barbell graph whose cycle rank increases from two to three. In each case the numerical absolute homology ranks and link description agree with the theorem. The executable's actual output is in `verification_output.txt`. These finite tests are not the unrestricted proof and do not by themselves prove integral torsion-freeness; the surjective integral incidence boundary does.

## Relationship to prior work
The bounded-independence / robust-clique terminology and general homotopy program are discussed by Filakovský (arXiv:2602.11365v1) and Carnero Bravo (arXiv:2602.21427v1). A previously published result entitled *Cycle-rank homology of total three-cut complexes of high-girth graphs* already gives the **absolute** integral sphere-wedge count for girth at least six. That count is not new here. The claim established here instead computes the **actual homomorphisms induced by every edge insertion**, including their saturated integral images and canonical no-death persistence property. The absolute theorem alone cannot determine these maps. Closely related results on all connected bipartite graphs also concern absolute homotopy types and Euler characteristics rather than these filtration maps.

## Limitations
The argument requires graph connectivity, an edge addition whose endpoints were at distance at least six, and hence girth at least seven throughout; it is not a classification for arbitrary graph edge additions. It does not claim a canonical splitting basis, equivariant splitting, or formulas for an arbitrary disconnected graph filtration. The absence of a matching published map theorem in the inspected sources does not prove global uniqueness; inaccessible relevant full texts and unindexed work remain residual originality risks. Independent mathematical audit has not been performed.

## References
- M. Filakovský, *The topology of k-robust clique complexes in grid-like graphs*, arXiv:2602.11365v1, 11 February 2026, https://arxiv.org/abs/2602.11365.
- A. Carnero Bravo, *Total cut complexes and their duals*, arXiv:2602.21427v1, 24 February 2026, https://arxiv.org/abs/2602.21427; accessible expanded full text https://arxiv.org/html/2602.21427v3, Propositions 15 and 21.
- *Cycle-rank homology of total three-cut complexes of high-girth graphs*, published research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-cycle-rank-homology-of-total-three-cut-complexes-of-high-girth-g--9341d892cb0d (existing absolute classification).
