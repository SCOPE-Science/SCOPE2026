# Robust clique homotopy stability under middle-edge contraction in pentagonal bouquets

## Finding
For every integer \(m\ge1\), let \(F_m\) be the bouquet of \(m\) unfilled five-cycles meeting at exactly one common vertex. Let \(B_m\) be the corresponding bouquet of \(m\) unfilled four-cycles. For every integer \(k\ge2\), simultaneously contract in each pentagon the edge joining the two vertices not adjacent to the common vertex. The resulting vertex map induces a **homotopy equivalence** of simplicial complexes
\[
 |\operatorname{Cliq}_k(F_m)|\longrightarrow |\operatorname{Cliq}_k(B_m)|.
\]
Here \(\operatorname{Cliq}_k(G)=\{S\subseteq V(G):\alpha(G[S])<k\}\), and \(\alpha\) is the induced independence number. Consequently the exact **integral homotopy type** for every \(m\ge1\) and \(k\ge2\) is
\[
 |\operatorname{Cliq}_k(F_m)|\simeq\bigvee^{\binom{m}{k-1}}S^{2k-3},
\]
with the empty wedge interpreted as a point. In particular the higher thresholds \(k\ge4\) on these nonbipartite bouquets have one homological degree, with free integral homology of rank \(\binom{m}{k-1}\). The threshold \(k=3\) was previously classified for this same family, and is included to show the map is uniform; it is not an independent novelty assertion.

## Assumptions and scope
All graphs are finite, simple, loopless, and undirected. A pentagonal petal has vertex sequence \(h,a_i,b_i,c_i,d_i,h\), where \(h\) is shared between all petals. A square petal has sequence \(h,a_i,z_i,d_i,h\); distinct petals have no other common vertices or cross edges. The contraction sends \(b_i,c_i\) to \(z_i\), fixes \(a_i,d_i,h\), and is applied to the abstract simplicial complexes (rather than asserting a graph-homotopy equivalence). The statement includes the contractible cases \(m<k-1\). These are homotopy equivalences of geometric realizations, not claims of simplicial isomorphism or equivariant equivalence.

## Proof
**1. The two independent-set statistics.** Deleting \(h\) leaves disjoint paths \(a_i-b_i-c_i-d_i\) in \(F_m\) and \(a_i-z_i-d_i\) in \(B_m\). For a set \(S\) of noncentral vertices, write \(p_i(S)\) for the independence number of the selected vertices in the \(i\)-th private path. Write \(q_i(S)\) for the independence number of the selected middle vertices: \(\{b_i,c_i\}\) is an edge, as is the singleton \(\{z_i\}\), so \(q_i\) equals zero when no middle vertex is chosen and one otherwise. Hence
\[
 \alpha(F_m[S])=\sum_i p_i(S),\qquad
 \alpha(F_m[S\cup\{h\}])=\max\!\left(\sum_i p_i(S),\;1+\sum_iq_i(S)\right),
\]
and identical formulas hold for the square bouquet. Contraction preserves every \(q_i\), and never increases \(p_i\): an independent set in the image path containing the middle vertex cannot contain either endpoint, whereas one omitting the middle vertex lifts unchanged. Therefore contraction maps robust-clique faces to robust-clique faces at every threshold.

**2. Local filtered diagrams.** Let \(D_{p,q}^{(5)}\) consist of private-vertex subsets in one pentagonal petal with \(p_i\le p\) and \(q_i\le q\); define \(D_{p,q}^{(4)}\) analogously for the quadrilateral. It suffices to consider \(p\in\{0,1,2\}\) and \(q\in\{0,1\}\). The local complexes, as well as the simplicial contraction restricted to them, are:

| \((p,q)\) | Pentagonal private complex | Quadrilateral private complex | Map |
|---|---|---|---|
| \((0,0),(0,1)\) | \(\{\varnothing\}\) | \(\{\varnothing\}\) | identity |
| \((1,0)\) | the two isolated endpoints | the two isolated endpoints | identity |
| \((2,0)\) | endpoint edge | endpoint edge | identity |
| \((1,1)\) | the path \(a-b-c-d\) | the path \(a-z-d\) | collapses edge \(bc\) |
| \((2,1)\) | full tetrahedron | full triangle | surjective simplicial contraction |

Each nonempty realization map in the table is a homotopy equivalence; the augmented empty-face complexes map identically. The path contraction is a homotopy equivalence of trees, while the final map is between contractible full simplices. These statements verify the entire nonstandard local lemma, including both boundary regimes of the two statistics.

**3. Passage to arbitrarily many petals.** The noncentral subcomplex \(X_m=\operatorname{Cliq}_k(F_m)\setminus\{h\}\) is the union, over \(p_i\in\{0,1,2\}\) with \(\sum_i p_i\le k-1\), of the simplicial joins \(\bigast_iD^{(5)}_{p_i,1}\). The link \(L_m=\operatorname{lk}_{\operatorname{Cliq}_k(F_m)}(h)\) is the union, over \((p_i,q_i)\) with \(\sum_i p_i\le k-1\) and \(\sum_iq_i\le k-2\), of \(\bigast_iD^{(5)}_{p_i,q_i}\). The corresponding covers for \(B_m\) use the superscript \((4)\). These descriptions follow directly from the two independent-set statistics; in particular, they apply also when an individual threshold is zero.

For any two local threshold pairs, \(D_{p,q}\cap D_{p',q'}=D_{\min(p,p'),\min(q,q')}\). Hence *every finite intersection* of the displayed covering joins is again a join of local complexes in the table. A join of the indicated homotopy-equivalence maps is a homotopy equivalence (the augmented empty complex acts as the join unit). The finite-subcomplex-cover gluing lemma now implies that contraction induces homotopy equivalences on both \(X_m\) and \(L_m\): the gluing lemma follows, for example, by replacing such covers with their Čech homotopy-colimit diagrams, since all inclusions are cofibrations. Finally,
\[
\operatorname{Cliq}_k(F_m)=X_m\cup(h*L_m)
\]
with the indicated common subcomplex \(L_m\); the analogous square-bouquet decomposition commutes with contraction. The ordinary homotopy gluing lemma gives the claimed equivalence of full robust-clique complexes.

**4. Exact wedge ranks.** For completeness, the quadrilateral-bouquet calculation can be reconstructed directly. A face not containing \(h\) has private independence number \(\sum_i\max(e_i,\epsilon_i)\), where \(e_i\in\{0,1,2\}\) counts selected endpoints \(a_i,d_i\) and \(\epsilon_i\in\{0,1\}\) indicates selection of \(z_i\). In the full bouquet its independence number after adding \(h\) is \(\max\{\sum_i\max(e_i,\epsilon_i),1+\sum_i\epsilon_i\}\). Pair every nonempty face omitting \(h\) with its coface obtained by inserting \(h\), whenever permitted; leave \(\{h\}\) unpaired. The remaining faces have exactly \(k-1\) selected middle vertices, no vertices on other petals, and at most one selected endpoint in each represented petal. For each represented petal, pair the local state with no endpoint to that with endpoint \(a_i\), in increasing petal order; this leaves exactly one face \(\{z_i,d_i:i\in I\}\) for every \((k-1)\)-element petal set \(I\). Its dimension is \(2k-3\). The matching is acyclic: on upward arrows the hub indicator cannot decrease, the selected-middle set cannot increase outside hub pairs, and within a fixed middle set the ordered endpoint-state matching has no directed cycle (the first unfrozen endpoint state can only increase). Thus Forman's theorem yields one zero-cell and \(\binom{m}{k-1}\) cells of dimension \(2k-3\), with no other cells. As \(k\ge2\), the attaching maps land at the single point, giving the claimed integral wedge. This also matches the independently published quadrilateral-bouquet theorem. Combined with Steps 1–3 it proves the pentagonal formula for every quantified parameter.

## Verification
The standalone standard-library Python program `verify.py` checks the local threshold diagrams by full enumeration, the contraction of every robust-clique face, surjectivity on the face sets, and independent mod-two simplicial boundary ranks for all \(16\) pairs \(1\le m\le4\), \(2\le k\le5\). It independently computes induced independence numbers from the actual graph edge lists, rather than accepting the symbolic formulas. All cases passed; for the first nontrivial higher-threshold case \((m,k)=(3,4)\), the pentagonal complex has \(1618\) nonempty faces and homology of a single five-sphere, and for \((4,4)\) it has \(4297\) nonempty faces and four such generators. The complete output is `verification_output.txt`. The all-parameter conclusion is the proof above, not extrapolation from finite tests.

## Relationship to prior work
Filakovský [1] studies robust clique complexes of bipartite square-sequence graphs; the pentagonal bouquets here are nonbipartite, so those results do not imply this statement. Kim and Lew [2] introduced the identical bounded-independence complex under the name \(I_k(G)\), emphasizing collapsibility bounds. The published quadrilateral-bouquet classification [3] determines the target's homotopy type, not a contraction equivalence for pentagonal bouquets; the latter is the structural contribution of Steps 1–3. A separate previous classification [4] treats the pentagonal bouquet at \(k=3\) only. In particular this result's new range is all \(k\ge4\), and its map-level comparison is not a generic edge-contraction principle: ordinary clique complexes already show that contracting an edge of an unfilled quadrilateral into a triangle can destroy \(S^1\).

## Limitations
The contraction theorem is restricted to the specified middle edges in bouquets of four- and five-cycles, not arbitrary graph edge contractions, longer petals, mixed gluing patterns or equivariant homotopy. The proof establishes the homotopy type over the integers but not a preferred integral basis compatible with every graph automorphism. An equivalent theorem under an alternative bounded-independence or total-cut-complex formulation may exist outside inspected sources. Independent validation has not been performed.

## References
[1] M. Filakovský, *The Topology of \(k\)-Robust Clique Complexes in Grid-like Graphs*, arXiv:2602.11365, initially public 2026-02-11. https://arxiv.org/html/2602.11365

[2] M. Kim and A. Lew, *Complexes of graphs with bounded independence number*, arXiv:1912.12605, initially public 2019-12-29. https://arxiv.org/abs/1912.12605

[3] *All-threshold sphere wedges for bouquets of quadrilaterals*, public mathematical result, 2026-11-08, repository published-finding corpus/2026, record ending `eb26c76015bf`.

[4] *A signed integral homology lattice for bouquets of pentagons*, public mathematical result, 2026-11-09, separate threshold-three classification.
