# Subgroup-fixed homotopy of complete-graph generalized Mycielskians

## Finding
Let \(n\ge2\), \(\ell\ge1\), and let \(\mu_\ell(K_n)\) be the generalized Mycielskian described below. The symmetric group \(S_n\) simultaneously permutes the original labels at every level and fixes the apex. For **every** subgroup \(H\le S_n\), put \(f=|\{a\in\{1,\ldots,n\}:h(a)=a\text{ for every }h\in H\}|\). Then the *geometric* fixed-point space of the independence complex has the following simple-homotopy classification:
\[
\left|\operatorname{Ind}(\mu_\ell(K_n))\right|^H\simeq
\begin{cases}
\operatorname{Ind}(P_{\ell+1}),& f=0,\\
\operatorname{Ind}(\mu_\ell(K_f)),& f\ge1.
\end{cases}
\]
The equivalences are induced by **simplicial strong collapses** of an exact simplicial orbit model, rather than inferred from character calculations. In particular, the answer depends on the number of labels fixed *by the whole subgroup*, and not on the sizes, number, or stabilizers of its other orbits.

Writing \(\ell=3k+r\), with \(r\in\{0,1,2\}\) (and \(k\ge1\) if \(r=0\)), the complete integral homotopy types are:

* If \(f=0\), the space is contractible when \(r=0\), and is \(S^k\) when \(r=1\) or \(r=2\).
* If \(f=1\), the space is contractible for every \(\ell\ge1\).
* If \(f\ge2\), it is \(\bigvee^{f(f-1)^k} S^{2k}\) when \(r=0\), and \(\bigvee^{(f-1)^{k+1}}S^{2k+1}\) when \(r=1\) or \(r=2\).

Consequently all integral reduced homology groups are free abelian and vanish except in the explicitly displayed sphere degree; for a contractible case all reduced homology vanishes. The description applies to the trivial subgroup as well as to transitive and intransitive nontrivial subgroups.

## Assumptions and scope
For a finite simple graph \(G\), \(\operatorname{Ind}(G)\) denotes the simplicial complex of independent vertex sets. The graph \(\mu_\ell(K_n)\) has vertex set
\[
\{w\}\cup\{(j,a):0\le j\le\ell,\ 1\le a\le n\}.
\]
Here \(w\) is an apex; there are edges \(w(0,a)\) for every \(a\); edges \((j,a)(j+1,b)\) exactly when \(a\ne b\) and \(0\le j<\ell\); and all edges \((\ell,a)(\ell,b)\) with \(a\ne b\). There are no other edges. This indexing agrees with the definition in Carnero Bravo (2026), up to reversing the displayed path-level orientation. An \(H\)-fixed *point* of the realization means a point whose barycentric coordinates are invariant under every \(h\in H\); vertices themselves need not be fixed. \(P_q\) means the simple path on \(q\) vertices.

The case \(f=0\) means that no original label is fixed by **every** element of \(H\), not merely that each nonidentity element acts freely; groups may have arbitrary large orbits and nontrivial stabilizers. When \(f\ge1\), \(K_f\) is interpreted as the simple complete graph on \(f\) vertices, including \(K_1\). All equivalences are nonequivariant homotopy equivalences of the indicated subgroup-fixed spaces; no stronger global equivariant equivalence of the original \(S_n\)-spaces is asserted.

## Proof
**1. Orbit-complex description of geometric fixed points.** For any finite simplicial complex \(L\) with simplicial \(H\)-action, form a complex \(L_H\) whose vertices are \(H\)-orbits of vertices of \(L\) which individually form faces, and whose faces are families of orbits whose *entire union* is a face of \(L\). For a vertex orbit \(O\), take the uniform barycenter \(|O|^{-1}\sum_{v\in O}v\) in the realization. The affine map sending \(O\) to this barycenter induces a PL homeomorphism \(|L_H|\to |L|^H\): invariant barycentric coordinates are precisely those constant on each orbit; normalized orbit masses give its explicit inverse. This directly excludes the erroneous practice of retaining only individually fixed original vertices.

For \(L=\operatorname{Ind}(\mu_\ell(K_n))\), list the orbits of \(H\) on original labels as \(O_1,\ldots,O_b\), with the \(f\) one-element orbits listed separately. At levels \(j<\ell\), every \(\{(j,a):a\in O_t\}\) is an independent orbit and hence a vertex of \(L_H\). At the top level \(j=\ell\), which induces a clique, *only* the one-element label orbits survive. The apex is another orbit vertex. Because \(L\) is an independence complex, \(L_H\) is itself the independence complex of the graph \(Q\) with those admissible orbit vertices, where two vertices of \(Q\) are adjacent if some original graph edge joins their supporting orbits.

**2. Exact orbit graph.** Denote by \(F_{j,a}\) the orbit vertex at level \(j\) from a singleton label \(\{a\}\), and by \(B_{j,t}\) the orbit vertex from a label orbit \(O_t\) of size at least two (such a vertex exists only for \(0\le j<\ell\)). Within a level below the top there are no edges. At consecutive levels all pairs of orbit vertices are adjacent, *except* \(F_{j,a}F_{j+1,a}\), which is a nonedge. Every two distinct \(F_{\ell,a}\) are adjacent at the top level. Finally, the apex is adjacent exactly to all level-zero orbit vertices. These statements follow immediately from the rule that a cross-level original edge joins distinct labels: if a supporting orbit has at least two labels, there exists a distinct-label cross pair even when the other supporting orbit is the same orbit.

**3. Removing the nonsingleton label orbits when \(f\ge1\).** Fix one globally fixed label \(a\). For every \(0\le j<\ell\) and every nonsingleton label orbit \(O_t\), the exact adjacency description gives
\[
N_Q(F_{j,a})\subseteq N_Q(B_{j,t}),
\]
where \(N_Q\) denotes the **open** neighborhood. The two vertices are nonadjacent, being in the same level. The graph-fold lemma says that if \(u,v\) are nonadjacent and \(N(u)\subseteq N(v)\), then \(v\) is a dominated vertex of \(\operatorname{Ind}(Q)\): every maximal independent set containing \(v\) also contains \(u\). Hence deleting \(v\) gives an elementary simplicial strong collapse. Deleting the \(B_{j,t}\) in any order retains the neighborhood inclusion. After all these deletions, the induced graph on the apex and the singleton-label vertices at all levels is *exactly* \(\mu_\ell(K_f)\). This proves the \(f\ge1\) assertion, including \(f=n\) (no deletions).

**4. Removing redundant orbit vertices when \(f=0\).** No orbit vertex survives in the top clique level. Every lower level \(j\in\{0,\ldots,\ell-1\}\) contains at least one vertex \(B_{j,t}\). All such vertices at the same level have identical open neighborhoods, because consecutive levels are completely joined and the apex is attached to level zero. Again they are pairwise nonadjacent, and all but one can be removed by strong collapses. The remaining graph consists of the apex, one vertex per lower level, and precisely the successive edges of the path \(P_{\ell+1}\). This proves the \(f=0\) assertion.

**5. Integral homotopy types.** The standard path-independence recurrence \(\operatorname{Ind}(P_{q})\simeq\Sigma\operatorname{Ind}(P_{q-3})\), with the three smallest path complexes as base cases, gives contractibility for \(q\equiv1\pmod3\), and the respective spheres for \(q\equiv0,2\pmod3\). Setting \(q=\ell+1\) yields the \(f=0\) line. For \(f=1\), the top-level vertex of \(\mu_\ell(K_1)\) is isolated (the original label has no distinct label to which it can connect), so its independence complex is a cone. For \(f\ge2\), Carnero Bravo (2026), Corollary 7, gives exactly the two wedge-multiplicity formulas displayed above (the equivalent calculation appears in Goyal–Shukla–Singh 2019 with a shifted indexing convention). Together these steps establish the full claim for all \(n\), \(\ell\), and \(H\).

## Verification
Run `python3 verify.py` with Python 3 standard library. Its explicit graph generator builds the original Mycielskian and forms vertex orbits for a permutation with each prescribed orbit size. A separate symbolic formula constructs the quotient-orbit graph. The code checks the two adjacency models pairwise, independently verifies each neighborhood inclusion *at its deletion stage*, checks the remaining exact graph, and computes reduced mod-two boundary-matrix homology on a bounded suite of the full orbit complexes. The recorded run reports 168 combinations of a label-orbit partition and a level parameter, 16,579 orbit-pair checks, 462 dominated-vertex removals, and 110 mod-two homology calculations involving 9,647 enumerated faces. Its success marker is `ALL_FIXED_MYC_CHECKS_OK`.

These finite tests do not prove any infinite-parameter statement. The proof above derives the reductions for every subgroup and level; the mod-two calculations are finite corroboration and do not substitute for integral or homotopy arguments.

## Relationship to prior work
Carnero Bravo (2026), Theorem 5 and Corollary 7, computes the **ordinary** homotopy types for generalized Mycielskians and supplies the sphere counts used only after our stronger subgroup-fixed-space reduction. Goyal, Shukla and Singh (2019), Section 4, independently supplies ordinary wedge formulas under a different index convention. A published rational \(S_n\)-homology-character computation for these same complexes gives individual-permutation traces but not geometric fixed spaces for arbitrary subgroups; homology characters alone do not recover subgroup-fixed homotopy types. A related fixed-space calculation for an involution on generalized Mycielskians of complete bipartite graphs concerns a different base graph and does not imply this complete-graph classification. The new structural content is the all-subgroup orbit-graph collapse and its dependence solely on the number of **globally fixed labels**.

## Limitations
The result concerns the natural label-permuting \(S_n\)-action, not every automorphism of the constructed graph; it classifies spaces fixed by each subgroup separately, not their inclusion maps or full equivariant homotopy type. The modular formulas are asserted for \(\ell\ge1\), and all conclusions use the specific convention for generalized Mycielskians stated above. Strong collapse is asserted for the canonical orbit simplicial complex, which is PL-homeomorphic to the geometric fixed set; the original unsplit fixed locus is not a vertex-induced subcomplex of the original independence complex. An unindexed stronger equivariant treatment could overlap this result.

## References
1. Andrés Carnero Bravo, *Independence complexes of generalized Mycielskian graphs*, arXiv:2601.13432v1 (first posted January 19, 2026), Theorem 5 and Corollary 7, https://arxiv.org/html/2601.13432.
2. Shuchita Goyal, Samir Shukla, Anurag Singh, *Homotopy Type of Independence Complexes of Certain Families of Graphs*, arXiv:1905.06926v1 (first posted May 16, 2019), Section 4, https://arxiv.org/html/1905.06926v1.
3. *The symmetric-group homology modules of generalized Mycielskians of complete graphs*, public mathematical record a69c919d2b95 (2026), rational homology-character theorem.
