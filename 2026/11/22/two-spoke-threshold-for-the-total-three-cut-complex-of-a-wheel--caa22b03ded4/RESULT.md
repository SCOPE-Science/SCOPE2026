# Two-spoke threshold for the total three-cut complex of a wheel

## Finding
For every integer \(n\ge6\), delete precisely two spokes \(ha,hb\) from the wheel \(W_{n+1}=K_1\vee C_n\). The total three-cut complex is contractible if \(a,b\) are rim-adjacent; otherwise it has integral homotopy type \(S^{n-5}\). With zero or one spoke deleted, the complex is contractible. A sphere of arbitrarily high dimension is therefore born exactly when the second failed spoke is nonadjacent to the first.

## Assumptions and scope
All graphs are finite, undirected and simple. The rim has vertices \(V=\mathbb Z/n\mathbb Z\), with edges between consecutive residues; the hub is a distinct vertex \(h\). For a graph \(G\) on vertex set \(V(G)\), the *total three-cut complex* \(\Delta^t_3(G)\) consists of all subsets of complements of independent sets of cardinality three:
\[\Delta^t_3(G)=\{F\subseteq V(G):\exists I\subseteq V(G)\setminus F,\ |I|=3,\ G[I]\text{ has no edges}\}.\]
For a finite set \(P\), \(\Delta_P\) denotes the full simplex on \(P\), and \(\partial\Delta_P\) its boundary. Joins and unions below are simplicial; all homotopy equivalences concern geometric realizations. The theorem requires exactly two *hub* spokes to be removed, not arbitrary edges or more than two spokes. Every two-spoke configuration is covered.

## Proof
Set \(B=\Delta^t_3(C_n)\), considered on the rim vertices. Since \(n\ge6\), \(B\) is nonvoid. With zero or one missing spoke, or with two missing adjacent spokes, no independent triple involves the hub: the hub has at most two non-neighbors, and they are adjacent if two adjacent spokes are missing. Thus every independent triple lies in the rim and the resulting complex is \(\Delta_{\{h\}}*B\), a cone.

Suppose \(a,b\) are nonadjacent on the rim. The independent triples involving the hub consist of the single triple \(\{h,a,b\}\). Put \(A=V\setminus\{a,b\}\), \(D=\Delta_A\) and \(T=B|_A\) (the induced subcomplex of \(B\) on \(A\)). The exact decomposition is
\[\Delta^t_3(G_{a,b})=(\Delta_{\{h\}}*B)\cup D,\qquad (\Delta_{\{h\}}*B)\cap D=T.\]
Both pieces are nonempty contractible simplicial complexes; consequently their homotopy pushout is the unreduced suspension of \(|T|\). It remains to prove \(|T|\simeq S^{n-6}\).

Let \(N_a=\{a-1,a+1\}\) and \(N_b=\{b-1,b+1\}\) (indices modulo \(n\)), put \(W=N_a\cup N_b\) and \(U=A\setminus W\). If \(F\subseteq A\) omits a vertex \(c\in U\), then \(\{a,b,c\}\) is an independent triple in the rim disjoint from \(F\), hence \(F\in T\). Such faces form \(\partial\Delta_U*\Delta_W\) whenever \(U\ne\varnothing\).

**Separation two.** Then \(N_a\cap N_b\) consists of one vertex, \(|W|=3\), and \(|U|=n-5\ge1\). The three vertices of \(W\) are pairwise nonadjacent for every \(n\ge6\). The *only* independent triple in \(C_n[\{a,b\}\cup W]\) is \(W\). Thus a face containing \(U\) belongs to \(T\) exactly when it contains no vertex of \(W\), giving
\[T=(\partial\Delta_U*\Delta_W)\cup\Delta_U.\]
For \(|U|=1\), this is the disjoint union of two nonempty simplices and is equivalent to \(S^0\). For \(|U|\ge2\), its two contractible pieces intersect in \(\partial\Delta_U\simeq S^{|U|-2}\), so \(T\simeq S^{|U|-1}=S^{n-6}\).

**Separation at least three in both cyclic directions.** Now \(N_a,N_b\) are disjoint two-element sets, \(|W|=4\), and \(|U|=n-6\). An independent triple inside \(C_n[\{a,b\}\cup W]\) must contain all of \(N_a\) or all of \(N_b\). Indeed, a triple consisting of neighbors alone contains a complete neighbor pair by pigeonhole; one containing \(a\) must use both vertices of \(N_b\), and one containing \(b\) must use both vertices of \(N_a\). Conversely, \(\{b\}\cup N_a\) and \(\{a\}\cup N_b\) are independent triples. Consequently, for \(F=U\cup S\) with \(S\subseteq W\), the condition \(F\in T\) is equivalent to \(S\subseteq N_a\) or \(S\subseteq N_b\). Let \(L=\Delta_{N_a}\cup\Delta_{N_b}\), a disjoint union of two edges, so \(|L|\simeq S^0\).

If \(n=6\), then \(U=\varnothing\) and \(T=L\simeq S^0=S^{n-6}\) directly. If \(n\ge7\), \(|U|=r=n-6\ge1\) and
\[T=(\partial\Delta_U*\Delta_W)\cup(\Delta_U*L).\]
These two pieces are contractible. Their intersection is \(\partial\Delta_U*L\). For \(r=1\), this intersection is \(L\simeq S^0\), so \(T\simeq S^1\). For \(r\ge2\), \(\partial\Delta_U*L\simeq S^{r-2}*S^0\simeq S^{r-1}\), giving \(T\simeq S^r=S^{n-6}\). This covers all cyclic separations.

Finally, the original two-cone union gives \(|\Delta^t_3(G_{a,b})|\simeq\Sigma|T|\simeq S^{n-5}\). Since this is an actual homotopy equivalence, the asserted integral homology groups follow without any coefficient restriction.

## Verification
The accompanying standalone `wheel_fault_verifier.py` independently enumerates all independent triples, their complementary facets and their downward-closed face sets. For every pair of spokes at each rim size from six through twelve, it checks the exact cone-or-extra-simplex description, verifies the explicit intersection decomposition for nonadjacent pairs, and computes reduced mod-two homology by exhaustive boundary ranks. All \(266\) pairs passed. The unbounded result does not depend on these finite experiments: the proof above classifies every possible independent triple in the relevant induced subgraphs and uses standard homotopy pushouts. Run `python3 wheel_fault_verifier.py`.

## Relationship to prior work
Bayer, Denker, Jelić Milutinović, Rowlands, Sundaram and Xue introduced the total cut complex and established general tools and family classifications, including the distinction from ordinary cut complexes [1]. Carnero Bravo developed the theory of total cut complexes and their Alexander duals for cycle powers and several other graph families [2]. Neither of the inspected treatments supplies the two-missing-spoke wheel calculation. A related published ordinary three-cut calculation for one missing wheel spoke concerns a strictly larger complex with a different independent-set condition [3]; its one-spoke conclusion does not imply this total-cut two-spoke threshold. The present theorem is a direct explicit classification for an infinite family with a sharp minimal configuration effect.

## Limitations
The conclusion is about homotopy type, not a specified homeomorphism or simple-homotopy equivalence. It does not classify arbitrary rim-edge deletions, three or more spoke failures, or other values of the cut parameter. Bibliographic novelty is assessed against the accessible works listed below; undiscovered equivalent prior work remains possible. Independent validation has not been performed.

## References
[1] M. Bayer, M. Denker, M. Jelić Milutinović, R. Rowlands, S. Sundaram and L. Xue, *Total Cut Complexes of Graphs*, arXiv:2209.13503, first submitted 2022-09-27, https://arxiv.org/html/2209.13503v2.

[2] A. Carnero Bravo, *Total cut complexes and their duals*, arXiv:2602.21427, first submitted 2026-02-24, https://arxiv.org/abs/2602.21427.

[3] *One missing wheel spoke creates a wedge of top-dimensional spheres in the ordinary three-cut complex*, searchable published-finding corpus finding, 2026-11-17, https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-one-missing-wheel-spoke-creates-a-wedge-of-n-5-top-dimensional-s--93bd4a365ab0.
