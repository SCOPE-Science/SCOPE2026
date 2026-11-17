# Rung-fault Möbius ladder independence complexes collapse in two residue classes

## Finding
For every integer \(n\ge3\) such that \(n\equiv0,3\pmod4\), deleting one antipodal rung from a Möbius ladder gives a **collapsible** independence complex. More precisely,
\[
\operatorname{Ind}(M_{2n}-e)\searrow\Delta^1*(S^0)^{*r},\qquad
r=\begin{cases}n/2-1,&n\equiv0\pmod4,\\ (n-3)/2,&n\equiv3\pmod4.\end{cases}
\]
The right-hand complex is a simplicial ball (a join with an edge) and itself collapses to a vertex. The result classifies exactly these two residue classes; the complementary residue classes are separately studied in earlier work.

## Assumptions and scope
Take \(n\ge3\). Label the two rails \(U_j,V_j\), \(0\le j<n\). The Möbius ladder has all rungs \(U_jV_j\), all rail edges \(U_jU_{j+1}\) and \(V_jV_{j+1}\) for \(0\le j<n-1\), and twisted terminal edges \(U_{n-1}V_0\) and \(V_{n-1}U_0\). Delete exactly \(e=U_0V_0\), leaving all other edges. Any rung is equivalent to this one by rotation.

Let \(J=\{0\}\cup\{2,4,\ldots,2\lfloor(n-2)/2\rfloor\}\), let \(Z=\{U_j,V_j:j\in J\}\), and set \(W=V(M_{2n})\setminus Z\). Here \(j=0\) is a deleted rung; the selected positive even columns remain rungs. Their columns are separated, so the induced graph on \(Z\) is the disjoint union of an edgeless two-vertex graph and \(r=|J|-1\) ordinary edges. Thus \(\operatorname{Ind}(G[Z])=\Delta^1*(S^0)^{*r}\).

## Proof
**Fiber matching.** Let \(K=\operatorname{Ind}(G)\), with \(G=M_{2n}-e\). Map its face poset by \(S\mapsto S\cap W\) to the inclusion poset of independent subsets of \(W\). The fiber over a fixed independent \(T\subseteq W\) consists of all \(T\cup A\) with \(A\) independent in \(G[Z\setminus N(T)]\), where \(N(T)\) is the union of open neighborhoods of vertices of \(T\). We retain the fiber \(T=\varnothing\), which is exactly \(\operatorname{Ind}(G[Z])\).

For nonempty \(T\), we show that its fiber has an explicit toggle vertex. Call an endpoint of a selected pair *blocked* when it is adjacent to a vertex of \(T\). If at least one of \(U_0,V_0\) is unblocked, it is a cone vertex of the fiber, since the edge \(U_0V_0\) was deleted and neither endpoint has any other neighbor in \(Z\). If a positive even selected rung has precisely one unblocked endpoint, that endpoint is a cone vertex: its only possible neighbor in the induced graph on \(Z\) is its now-blocked rung mate. Therefore only the contrary situation needs exclusion: both \(U_0,V_0\) are blocked, and on every positive even selected rung either both endpoints are blocked or both are unblocked.

**Parity obstruction when \(n=4k\).** The exterior columns are exactly the odd columns \(1,3,\ldots,n-1\). Each contains a surviving rung, so an independent \(T\) takes at most one endpoint per column. Blocking both endpoints of a selected even rung requires selected exterior vertices in *both* adjacent odd columns, with opposite rail labels. Starting from the requirement to block both vertices in column \(0\), this propagates across all odd columns and forces their chosen rail labels to alternate. There are \(n/2=2k\) odd columns, so the labels in columns \(1\) and \(n-1\) must differ. But the twisted terminal edges imply that both endpoints of column \(0\) are blocked only if those two rail labels **agree**. Contradiction.

**Parity obstruction when \(n=4k+3\).** The exterior comprises odd columns \(1,3,\ldots,n-2\) and the last column \(n-1\). Blocking both vertices in column \(0\) forces exterior choices in column \(1\) and terminal column \(n-1\) with the same rail label (because terminal edges are twisted). The blocking condition at successive positive selected even rungs propagates choices through every odd column, alternately switching rail labels. There are \((n-1)/2=2k+1\) odd columns; hence the choices at columns \(1\) and \(n-2\) have the same rail label. Consequently the choices in adjacent columns \(n-2\) and \(n-1\) lie on the same rail and are joined by an edge, contradicting independence. This includes \(n=3\), for which there are no positive selected rungs and the last contradiction is immediate.

Thus every nonempty independent exterior face \(T\) has a cone vertex \(q(T)\) in its fiber, chosen as the first qualifying selected endpoint in a fixed vertex order. Match every face \(T\cup A\) not containing \(q(T)\) with \(T\cup A\cup\{q(T)\}\). This pairs **all** faces of the fiber; its directed Hasse diagram is acyclic because all matching edges toggle the same vertex. The combined matching is also acyclic: along any unmatched descending face-poset step, the exterior set can only decrease, while matched edges preserve it; hence a closed directed gradient path would stay in one acyclic fiber. The unmatched faces are exactly those in \(\operatorname{Ind}(G[Z])\). The relative acyclic-matching collapse criterion therefore supplies a sequence of elementary simplicial collapses from \(K\) onto this induced subcomplex. Since it has a simplex factor \(\Delta^1\), it is collapsible. \(\square\)

## Verification
The standalone `verify.py` enumerates all nonempty independent exterior sets \(T\) and checks the precise cone-vertex property for \(n=3,4,7,8,11,12,15,16\). It checks \(6,8,62,80,566,728,5102,6560\) cases respectively, with no exception. The general assertion follows from the parity obstruction above, not from a finite search.

## Relationship to prior work
Agarwal and Basak (2026), arXiv:2608.30601, classify independence complexes of **intact** Möbius and circular ladders; their Section 4.1, pages 7–9, treats vertex deletion and closed-neighborhood deletion, not deletion of an antipodal **edge**. An earlier publicly available rung-fault finding covers the *different* residue classes \(n\equiv1,2\pmod4\), giving two sphere summands; that result is not claimed anew. The present theorem provides the missing contractible cases and an explicit **simplicial collapse**, stronger than an abstract homotopy equivalence. This comparison does not exclude unavailable or unindexed literature.

## Limitations
Only one missing antipodal rung is allowed. No assertion is made for deletion of a rim edge, multiple edge faults, or equivariant collapse. The cone-fiber proof is complete for the stated residue classes; there is no claim that the induced ball is a deformation retract equivariantly under the surviving automorphism group. Independent validation has not been performed.

## References
- A. Agarwal and B. Basak, *The Homotopy Types of the Independence and Perfect Matching Complexes of Möbius and Circular Ladder Graphs*, arXiv:2608.30601v2 (first public preprint 2026-08-31; v2 2026-09-14), Sections 3–4.
- *Two-sphere homotopy after deleting a rung of a Möbius ladder* (2026-11-08), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-two-sphere-homotopy-after-deleting-a-rung-of-a-m-bius-ladder--354974543b20 (comparison only).
- R. Forman, *Morse theory for cell complexes*, Advances in Mathematics 134 (1998), 90–145 (acyclic matching principle).
