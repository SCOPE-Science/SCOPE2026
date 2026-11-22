# Modular attachment gaps govern proper conflict-free three-colouring of every unicyclic graph

## Finding
Let \(G\) be a finite connected simple unicyclic graph other than its bare cycle. Let its unique cycle be \(v_0v_1\cdots v_{m-1}v_0\), \(m\ge3\). Set \(t_i=\deg_G(v_i)-2\), and list the \(k\ge1\) indices \(s_1,\ldots,s_k\) for which \(t_i>0\), in cyclic order. Write \(\ell_j\) for the positive number of cycle edges from \(v_{s_j}\) to \(v_{s_{j+1}}\), cyclically (for \(k=1\), \(\ell_1=m\)). Define
\[
r(G)=\left|\{j:3\nmid\ell_j\}\right|.\]
Then the **exact proper open-neighbourhood conflict-free chromatic number** is
\[
\boxed{\chi_{\mathrm{pcf}}(G)=\begin{cases}4,&r(G)=1,\\3,&r(G)\ne1.\end{cases}}
\]
The criterion depends only on the positions of cycle vertices bearing off-cycle attachments, not on the sizes or shapes of the attached rooted trees. In particular, putting single leaves at adjacent vertices of \(C_5\) yields a three-colourable graph, whereas moving the second leaf two cycle edges away forces four colours.

Furthermore, the **exact number of proper conflict-free three-colourings from the three named colours** is given by a cyclic signed sum. Define \(b(1)=b(2)=1\) and \(b(d)=d\) for \(d\ge3\); define
\[
B(G)=\prod_{u\notin V(C_m)} b(\deg_G(u)),\qquad
w_i(a,b)=\begin{cases}t_i,&a\ne b,\\1,&a=b\text{ and }t_i=0,\\2,&a=b\text{ and }t_i>0.\end{cases}
\]
Then
\[
\boxed{N_3(G)=3B(G)\!\sum_{\substack{\sigma_0,\ldots,\sigma_{m-1}\in\{-1,+1\}\\\sum_i\sigma_i\equiv0\;(\mathrm{mod}\ 3)}}\ \prod_{i=0}^{m-1}w_i(\sigma_{i-1},\sigma_i),}
\]
where indices are cyclic. This provides an exact polynomial-time counting algorithm (by a constant-state cyclic transfer recurrence) and shows that \(N_3(G)\) depends only on the **cyclic ordered vector** of cycle-vertex degrees and the **multiset** of off-cycle degrees. The result includes all attachment multiplicities and arbitrary rooted trees, but does not claim the already-known cycle-only chromatic values.

## Assumptions and scope
All graphs are undirected, finite, simple and connected. A proper conflict-free (PCF) colouring with a palette of \(q\) named colours assigns different colours to endpoints of each edge, and every vertex of positive degree has at least one colour occurring **exactly once** among its open neighbours. The palette need not be used surjectively. Here the chromatic number is the least palette size. A connected unicyclic graph has exactly one simple cycle; the theorem's classification assumes at least one vertex outside that cycle.

The term \(N_3(G)\) counts distinct vertex functions into \(\{1,2,3\}\), without quotienting by graph automorphisms or colour permutations. The cyclic sum contains \(2^m\) sign strings, but is evaluable in \(O(m)\) arithmetic operations on integers (of possibly large bit size) by tracking the current sign and the partial sum modulo three. For a bare cycle \(C_m\), the known chromatic values are \(3\) when \(3\mid m\), \(4\) when \(3\nmid m\) and \(m\ne5\), and \(5\) when \(m=5\). This pre-existing cycle result is not asserted as new; the signed enumeration also applies to bare cycles by taking \(B=1\) and \(t_i=0\).

## Proof
**1. Off-cycle local choices.** Delete the cycle edges, regarding each resulting off-cycle component as a tree rooted at its adjacent cycle vertex. At an off-cycle vertex \(u\), its own colour \(X\) and the colour \(A\) of its parent are fixed and distinct. Its \(d-1\) children, where \(d=\deg_G(u)\), can each be coloured \(A\) or the third colour \(B\). The parent gives exactly one \(A\)-coloured neighbour. For \(d=1\), the parent alone is its witness. For \(d=2\), its only child must have colour \(B\), giving one choice. For \(d\ge3\), an exactly-once neighbour colour occurs precisely if **all** children have colour \(B\) (the parent alone supplies colour \(A\)), or **exactly one** child has colour \(B\) (the child supplies a unique \(B\)). These cases are disjoint and give \(1+(d-1)=d\) choices. Each choice is independent of the identities of \(X,A\) and all choices at different vertices are independent. Their total multiplicative contribution is \(B(G)\).

**2. Cycle-vertex local choices.** Fix a proper three-colouring \(c_0,\ldots,c_{m-1}\) of the cycle. Its two neighbours at \(v_i\) have colours in the two-colour set other than \(c_i\). If the two neighbours have **equal** colour \(A\), a witness is possible precisely when exactly one of the \(t_i\) off-cycle children receives the third colour \(B\); there are \(t_i\) ways, including zero if \(t_i=0\). If the two neighbours have **different** colours \(A,B\), then for \(t_i=0\) they already give two unique witnesses; for \(t_i>0\), all off-cycle children must have colour \(A\), or all must have colour \(B\), giving exactly two ways. Once the cycle and the colours of its off-cycle children are fixed, step 1 completes all remaining vertices independently, yielding the local weight table \(w_i\).

**3. Cyclic signs and the exact count.** Identify the three colour names with residues \(0,1,2\) modulo three, which only relabels the named palette. Each consecutive proper cycle edge has a unique increment \(\sigma_i\in\{-1,+1\}\) such that \(c_{i+1}-c_i\equiv\sigma_i\pmod3\). The sequence closes if and only if \(\sum_i\sigma_i\equiv0\pmod3\). Every closing sign sequence and one of three initial colour names determine exactly one proper cycle-colouring. The two neighbours of \(v_i\) have equal colours if and only if \(\sigma_{i-1}\ne\sigma_i\). Multiplying the independent local weights from step 2 and the factor from step 1, and summing over all closed sign sequences, proves the displayed count. The sum is finite and exact; it is not inferred from sampled dimensions.

**4. The modular-gap criterion.** At a cycle vertex with \(t_i=0\), step 2 forces \(\sigma_{i-1}=\sigma_i\). At a vertex with \(t_i>0\), both choices of equality or change have positive local weight. Therefore feasible sign strings are exactly those that are constant on the \(k\) cyclic arcs of \(\ell_j\) edges between consecutive attachment vertices, with freely chosen arc signs \(\varepsilon_j\in\{-1,+1\}\), and satisfying
\[
\sum_{j=1}^{k}\varepsilon_j\ell_j\equiv0\pmod3.
\]
Arcs with \(3\mid\ell_j\) contribute zero. For every other arc, choosing \(\varepsilon_j\) allows either of the two nonzero residues \(1,-1\). A sum of \(r\) independently selectable values in \(\{1,-1\}\) vanishes modulo three exactly when \(r=0\) or \(r\ge2\): pair opposite signs for \(r=2\), use three equal signs for \(r=3\), and decompose every larger \(r\) into pairs and triples. Exactly one nonzero arc makes closure impossible. Thus \(N_3(G)>0\) exactly when \(r(G)\ne1\).

**5. The sharp four-colour upper bound.** Every connected unicyclic graph has a degree-two-or-higher vertex. In a proper two-colouring, all its neighbours have the opposite colour, so no two-colouring is PCF. Hence \(\chi_{\mathrm{pcf}}(G)\ge3\). If \(m\ne5\), write \(m=3a+4b\) for nonnegative integers \(a,b\) (possible for all \(m\ge3\) except \(m=5\)). Colour the cycle by concatenating \(a\) copies of the block \((1,2,3)\) and \(b\) copies of \((1,2,3,4)\); cyclically every three consecutive vertices have distinct colours. Thus each cycle vertex already has two differently coloured cycle neighbours. Give all off-cycle children at that cycle vertex a colour distinct from the vertex and from those two neighbours; such a fourth-palette colour exists. The two cycle-neighbour colours remain unique, and properness is preserved.

If \(m=5\), use cyclic core colours \((1,2,3,4,2)\), rotated so its only vertex whose cycle neighbours agree has at least one attached child. At that vertex the two cycle neighbours have colour \(A\); give one off-cycle child a colour \(B\notin\{A,c_i\}\) and all remaining children colour \(A\), so \(B\) is a unique witness. At every other cycle vertex the two cycle-neighbour colours are distinct, so colour all off-cycle children with a colour different from all three already-used colours at the vertex and its two cycle neighbours. Finally, work outward through each attached tree: when a vertex and its parent have been coloured, give all of its children a colour different from both. This leaves its parent as a uniquely coloured neighbour. Thus four colours suffice whenever the graph is not a bare cycle. Combined with step 4 this proves the exact chromatic classification and completes the proof.

## Verification
The standalone standard-library Python 3 script `verify_unicyclic.py` independently enumerates proper conflict-free three-colourings by vertex-colour backtracking and checks the neighbourhood singleton condition directly; its implementation of the signed sum separately computes the mathematical formula. It compares 276 reproducibly generated labelled unicyclic instances with three to nine vertices, including arbitrary rooted-branch shapes, and all 504 choices of one-leaf attachment subsets of cycles of orders three to eight. It also checks the three-colour gap criterion, and checks four-colour existence by exhaustive search on smaller obstructions and the exceptional bare \(C_5\). A completed run returned `VERIFY_OK`. These finite tests corroborate, but do not replace, the proof for all finite unicyclic graphs.

## Relationship to prior work
Caro, Petruševski and Škrekovski (2022) determine the PCF chromatic number of trees and bare cycles, and prove basic facts about graph coronas. Their cycle-only classification and the bound of three for trees are not claimed as new here. Caro, Petruševski, Škrekovski and Tuza (2024/2025) prove the stronger-colouring **four-colour existence bound** for unicyclic graphs other than \(C_5\); the four-colour existence bound in step 5 is therefore also **not** a novelty claim. That strong-odd result does not furnish the PCF three-versus-four modular criterion or the exact three-colouring census.

Santra (2026) investigates proper conflict-free colouring of structured chordal, interval and ordered bipartite classes, including algorithms for some subclasses. These findings do not characterize PCF three-colourability and its complete counting distribution on arbitrary tree-decorated cycles. A separately available exact four-mode enumeration treats cycle coronas with the same positive number of pendant leaves at **every** cycle vertex, for which the modular obstruction never arises. Neither it nor the forest strong-odd degree-factorization count covers the arbitrary-attachment, PCF-specific cyclic product formula.

## Limitations
The complete palette-count formula is for **exactly three named colours**. It is not an all-palette PCF counting polynomial, and no count of all four-colourings or optimal four-colourings is asserted. The modular classification requires at least one off-cycle vertex; bare cycles use the previously known exceptional values. The proof depends on there being exactly one cycle and does not extend directly to cacti with multiple cycles. Unindexed or inaccessible literature could contain an equivalent enumeration, so absolute priority remains subject to independent expert validation.

## References
1. K. Santra, *Proper Conflict-Free Coloring on Structured Graph Classes: Bounds, Exact Algorithms, and Hardness*, arXiv:2611.03906v1, first public 2026-11-02, https://arxiv.org/abs/2611.03906.
2. Y. Caro, M. Petruševski and R. Škrekovski, *Remarks on proper conflict-free colorings of graphs*, arXiv:2203.01088v1 (2022), https://arxiv.org/abs/2203.01088.
3. Y. Caro, M. Petruševski, R. Škrekovski and Z. Tuza, *On strong odd colorings of graphs*, arXiv:2410.02336v1 (2024), https://arxiv.org/abs/2410.02336; Discrete Mathematics 348 (2025), 114601.
4. *A four-mode counting law for proper conflict-free colorings of hairy cycles* (2026), publicly available mathematical result for uniformly decorated cycles.
