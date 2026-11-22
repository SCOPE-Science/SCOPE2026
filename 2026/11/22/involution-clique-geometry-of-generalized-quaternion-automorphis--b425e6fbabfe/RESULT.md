# Involution clique geometry of generalized quaternion automorphism groups

## Finding

Let \(k\geq3\), put \(N=2^k\), \(h=N/2\), and \(t=N/4\), and let \(Q_{2N}\) be the generalized quaternion group of order \(2N\). Write \(G=\operatorname{Aut}(Q_{2N})\). Let \(\Gamma_k\) have as vertices the **nonidentity involutions** of \(G\), with two distinct vertices adjacent exactly when the corresponding automorphisms commute. Let \(K_r\) denote a complete graph on \(r\) vertices, \(\sqcup\) disjoint union, and \(\vee\) graph join. Then

\[
\boxed{\Gamma_k\cong K_1\vee\bigl[(K_2\vee(tK_4))\sqcup(tK_2)\bigr].}
\]

Here \(tK_r\) means a disjoint union of \(t\) copies of \(K_r\). In particular, \(\Gamma_k\) has exactly \(3N/2+3\) vertices; its degree multiset consists of one vertex of degree \(3N/2+2\), two vertices of degree \(N+2\), \(N\) vertices of degree \(6\), and \(N/2\) vertices of degree \(2\). The edge and triangle numbers are respectively

\[
|E(\Gamma_k)|=\frac{21N}{4}+3,\qquad T(\Gamma_k)=\frac{35N}{4}+1.
\]

The maximal commuting cliques correspond precisely to the inclusion-maximal elementary abelian \(2\)-subgroups of \(G\). There are \(t\) such subgroups of order \(8\) and \(t\) of order \(4\), and exactly \(7N/4+1\) distinct Klein-four subgroups in all.

## Assumptions and scope

We use the presentation

\[
Q_{2N}=\langle a,b\mid a^N=1,\ b^2=a^{N/2},\ bab^{-1}=a^{-1}\rangle.
\]

The condition \(k\ge3\) is essential: it makes \(\langle a\rangle\) the unique cyclic subgroup of order \(N\), and the four square roots of unity modulo \(N\) are pairwise distinct. The graph excludes the identity, includes central involutions, and has no loops. Throughout, all arithmetic on parameters \(v,u\) is modulo \(N\). The claim is about automorphisms of \(Q_{2N}\), not about the ordinary commuting graph of \(Q_{2N}\) itself or the graph induced by all noncentral elements of \(G\).

## Proof

**Step 1: an explicit automorphism group.** Every element outside \(\langle a\rangle\) has the form \(a^vb\) and square \(a^{N/2}\), so it has order four. Since \(N\ge8\), all elements of order \(N\) lie in the characteristic subgroup \(\langle a\rangle\). Every automorphism therefore has a unique expression

\[
\alpha_{v,u}(a)=a^u,\qquad\alpha_{v,u}(b)=a^vb,
\]

where \(v\in\mathbb Z/N\mathbb Z\) and \(u\in(\mathbb Z/N\mathbb Z)^\times\). Conversely these substitutions respect the defining relations and generate the group, hence are automorphisms. Composition has the affine multiplication rule

\[
(v,u)(w,s)=(v+uw,us).
\]

Thus \(G\cong (\mathbb Z/N\mathbb Z)\rtimes(\mathbb Z/N\mathbb Z)^\times\), the holomorph of the cyclic group.

**Step 2: exhaustive classification of involutions.** The equation \((v,u)^2=(0,1)\) means

\[
u^2\equiv1\pmod N,\qquad (1+u)v\equiv0\pmod N.
\]

For \(k\ge3\) the only solutions of the first congruence are \(u\in\{1,-1,1+h,-1+h\}\). This follows from \(N\mid(u-1)(u+1)\) and \(\gcd(u-1,u+1)=2\) up to their common power of two: one factor must be divisible by \(h\). The second congruence now gives the disjoint sets

\[
\begin{aligned}
\{c\}&=\{(h,1)\},\\
C&=\{(0,1+h),(h,1+h)\},\\
A_0&=\{(v,-1):v\text{ even}\},\\
A_1&=\{(v,-1):v\text{ odd}\},\\
B&=\{(v,h-1):v\text{ even}\}.
\end{aligned}
\]

The identity \((0,1)\) is omitted. Their sizes are \(1,2,N/2,N/2,N/2\), proving the vertex count.

**Step 3: the commutation relation.** The affine product formula gives

\[
(v,u)(w,s)=(w,s)(v,u)
\quad\Longleftrightarrow\quad
(u-1)w\equiv(s-1)v\pmod N.
\]

Because all units \(u\) are odd, \(uh\equiv h\pmod N\); thus \(c=(h,1)\) commutes with every vertex. The two elements of \(C\) commute with each other and with every element of \(A_0\cup B\), but with no element of \(A_1\): in the latter case the commutation congruence would force \(h\equiv0\pmod N\).

For elements of \(A_0\cup B\), the commutation relation reduces to agreement of the even translation parameters modulo \(h\). Thus, for each even residue \(r\) with \(0\le r<h\), the four elements

\[
(r,-1),\quad(r+h,-1),\quad(r,h-1),\quad(r+h,h-1)
\]

form a clique \(K_4\), and no element in this clique commutes with one from another such clique (apart from \(c\) and the two elements of \(C\)). There are \(h/2=t\) even residues \(r\) modulo \(h\).

For elements of \(A_1\), commutation inside \(A_1\) again means equal translation parameters modulo \(h\), producing the \(t\) disjoint edges \(\{(r,-1),(r+h,-1)\}\) for odd \(0\le r<h\). No \(A_1\) vertex commutes with \(A_0\cup B\): for the mixed case with \(B\), the congruence would require the odd integer \(v-w\) to equal \(N/4\) modulo \(h\), impossible because \(N/4\) and \(h\) are even. The other exclusions follow directly by parity. These are all vertex pairs, proving the displayed graph isomorphism.

**Step 4: subgroup and graph invariants.** Removing the universal vertex \(c\), one component is \(K_2\vee(tK_4)\), and the other \(t\) components are edges. Accordingly the maximal cliques are \(\{c\}\cup C\cup K_4^{(r)}\) of size seven, for each even \(r\) modulo \(h\), and \(\{c\}\cup K_2^{(r)}\) of size three, for each odd \(r\) modulo \(h\). As commuting involutions generate elementary abelian \(2\)-groups, adjoining the identity converts these cliques bijectively into inclusion-maximal elementary abelian \(2\)-subgroups. Their orders are eight and four respectively, and their numbers are both \(t\).

The degree counts follow from this join decomposition. Writing \(t=N/4\), the graph without \(c\) has \(1+15t\) edges and \(20t\) triangles; adding \(c\) adds \(2+6t\) edges and \(1+15t\) triangles. Hence the claimed \(3+21t\) edges and \(1+35t\) triangles. Every edge \(\{x,y\}\) corresponds to one Klein-four subgroup \(\{1,x,y,xy\}\), and each such subgroup has exactly three edges, so the number of these subgroups is \((3+21t)/3=1+7t\). This proves all assertions.

## Verification

The accompanying standalone `verification.py` independently constructs the full affine group and its multiplication table as needed; enumerates all nonidentity square-one elements; checks every pairwise commutation decision against the predicted adjacency structure; checks degree counts, edge/triangle numbers, and explicit maximal-clique candidates for \(3\le k\le8\). It reports `QUATERNION_AUTOMORPHISM_INVOLUTION_GRAPH_VERIFIED` when all assertions succeed. The finite check is corroboration only; the modular arithmetic argument above proves the theorem for all \(k\ge3\).

## Relationship to prior work

Velten, *The commuting graphs of certain cyclic-by-abelian groups* (arXiv:2405.18103, first submitted 28 May 2024), analyzes the entire commuting graph on noncentral elements of finite cyclic-by-abelian groups, chiefly connectivity, diameter and a disconnected complete-component alternative. The automorphism group above has a cyclic normal factor and an abelian unit subgroup, so the broad family overlaps. But the graph here is **induced specifically on nonidentity involutions including a central involution**; the exact join structure, rank-two/rank-three elementary abelian subgroup census, degrees and triangles are not conclusions of the cited connectivity/diameter theorem. Its original 2024 preprint and the later full-text presentation were inspected.

Cameron and Kuzma, *Between the enhanced power graph and the commuting graph* (first published 8 August 2022), introduce the deep commuting graph and characterize how it compares with ordinary and enhanced power graphs. Their full open-access paper treats group elements generally, not this automorphism-group involution incidence structure. The result here uses only the standard affine presentation and derives the involution graph directly; it does not claim discovery of holomorphs, commuting graphs or elementary abelian \(2\)-groups.

## Limitations

The result does not assert a classification for quaternion order eight, for automorphisms of unrelated \(2\)-groups, or for elements of higher order. The graph formula applies only to \(k\ge3\). An equivalent specialized result under holomorph, modular affine group, or elementary abelian subgroup terminology may predate this analysis; searches and inspected primary texts do not certify historical uniqueness. The accompanying finite enumerations do not establish any infinite assertion on their own. There is no independent audit.

## References

1. T. Velten, *The commuting graphs of certain cyclic-by-abelian groups*, arXiv:2405.18103, version 1 submitted 28 May 2024. https://arxiv.org/abs/2405.18103
2. P. J. Cameron and B. Kuzma, *Between the enhanced power graph and the commuting graph*, Journal of Graph Theory 102 (2023), 295–303, first published 8 August 2022. https://doi.org/10.1002/jgt.22871
3. J. K. Hai and J. X. Liu, *Coleman Outer Automorphism Groups of Generalized Quaternion Groups*, 2022. https://doi.org/10.12386/A2022sxxb0014 (potentially relevant inaccessible full text; no negative whole-text coverage conclusion is asserted).
