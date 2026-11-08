# Sharp slide-connectivity threshold for optimum identifying codes on crown graphs

## Finding
For each integer \(n\ge5\), let \(H_n=K_{n,n}-M\) be the **crown graph** with vertices \(a_1,\ldots,a_n,b_1,\ldots,b_n\), where \(a_i b_j\) is an edge exactly when \(i\ne j\). Let \(\mathcal R_n\) have as vertices the minimum closed-neighborhood identifying codes of \(H_n\); two codes are adjacent precisely if one is obtained from the other by removing one selected vertex and adding one of its **neighbors** in \(H_n\), while remaining a minimum identifying code.

Then the exact component structure is
\[
\boxed{\mathcal R_5\cong30K_1,\qquad \mathcal R_6\cong20K_{3,3},\qquad \mathcal R_n\text{ is connected for all }n\ge7.}
\]
Every state has a representation by one unoccupied matched index \(h\) and disjoint index sets \(A,B\) partitioning \([n]\setminus\{h\}\), with \(|A|,|B|\ge2\); it selects \(a_i\) for \(i\in A\) and \(b_i\) for \(i\in B\). Writing \(p=|A|\), \(q=|B|\), its slide degree is
\[
\deg_{\mathcal R_n}(A,B,h)=p\mathbf{1}_{p\ge3}+q\mathbf{1}_{q\ge3}.
\]
Consequently, \(\mathcal R_n\) has \(n(2^{n-1}-2n)\) vertices and
\[
\boxed{|E(\mathcal R_n)|=\frac{n(n-1)}2(2^{n-1}-4n+4)}
\]
edges. The minimum-code characterization and the vertex count were obtained previously and are **not** claimed as new here; the result is the slide-component classification, its infinite-family connectivity threshold, and the exact slide-edge structure.

## Assumptions and scope
Graphs are finite, simple, undirected, and vertex-labeled. An identifying code \(C\subseteq V(H_n)\) satisfies \(N[v]\cap C\ne\varnothing\) for each vertex \(v\), and the \(2n\) traces \(N[v]\cap C\) are pairwise distinct. Only minimum-cardinality identifying codes are admissible states. In particular, a move between the endpoints of a deleted-matching pair \(a_i,b_i\) is **not** a slide. The theorem is restricted to \(n\ge5\); no assertion is made about the exceptional three- and four-pair crowns or about token jumping.

## Proof
**1. Reconstructing the minimum states.** For any code \(C\), write \(A=\{i:a_i\in C\}\) and \(B=\{i:b_i\in C\}\). The traces are exactly
\[
N[a_i]\cap C=(\{a_i\}\cap C)\cup\{b_j:j\in B\setminus\{i\}\},\qquad
N[b_i]\cap C=(\{b_i\}\cap C)\cup\{a_j:j\in A\setminus\{i\}\}.
\]
If two distinct matched indices contribute no codeword, the corresponding two \(a\)-vertices have equal traces. Thus at most one matched index can be empty, and every identifying code has size at least \(n-1\). A code of size \(n-1\) must have exactly one empty index, and must choose exactly one endpoint of every other matched pair. If \(|A|\le1\), either \(A\) is empty, producing an undominated \(b\)-vertex at the empty index, or its sole index \(i\) has \(N[b_i]\cap C=\varnothing\). Hence \(|A|\ge2\), and symmetrically \(|B|\ge2\).

Conversely, fix such a partial one-per-index selection with \(p=|A|,q=|B|\ge2\). Every \(a_i\) has at least \(q-1\ge1\) selected \(b\)-neighbors, and every \(b_i\) has at least \(p-1\ge1\) selected \(a\)-neighbors. Two distinct \(a\)-vertices have distinct traces: either one of them is selected (and supplies its private \(a\)-symbol), or neither is selected, in which case their traces differ unless both indices are outside \(A\cup B\); but there is only one such index. The same applies to distinct \(b\)-vertices. Finally, each \(a_i\)-trace has at most one \(a\)-symbol and at least \(q-1\) \(b\)-symbols, whereas a \(b_j\)-trace has at least \(p-1\) \(a\)-symbols and at most one \(b\)-symbol. If \(p\ge3\) or \(q\ge3\), cross-side equality is impossible. If \(p=q=2\), equality would require \(i\in A\) and \(j\in B\) to make both traces contain both an \(a\)-symbol and a \(b\)-symbol. But \(N[a_i]\cap C\) then contains one \(a\)-symbol whereas \(N[b_j]\cap C\) contains both selected \(a\)-symbols; equality is impossible. Hence precisely these states are minimum identifying codes. There are \(n\sum_{p=2}^{n-3}\binom{n-1}{p}=n(2^{n-1}-2n)\) of them.

**2. Exact slide rule and degree.** A legal slide from \(a_i\) must land at an unselected \(b_j\) with \(j\ne i\). The resulting optimum must still have at most one empty matched index and at most one selected endpoint per occupied index. Thus the arrival index \(j\) must be the unique empty index \(h\). The new empty index is \(i\), and the move transfers \(i\) from \(A\) to the empty class while transferring \(h\) to \(B\); this is legal precisely when \(p\ge3\). Analogously, moving \(b_i\) to \(a_h\) is legal exactly when \(q\ge3\). Therefore the stated degree formula holds. Summing degrees over the \(n\binom{n-1}{p}\) states of each red-population size gives
\[
2|E|=n(n-1)(2^{n-1}-2n)-4n\binom{n-1}{2}
=n(n-1)(2^{n-1}-4n+4),
\]
valid also at \(n=5\), where both boundary deductions apply to the same states.

**3. The two small regimes.** At \(n=5\), every minimum code has \(p=q=2\); every move would leave one side with fewer than two codewords, so all thirty states are isolated. At \(n=6\), \((p,q)\) is either \((2,3)\) or \((3,2)\). Associate to each state the three-index set \(S=A\cup\{h\}\) in the former case and \(S=A\) in the latter case. Every legal move preserves \(S\). For fixed \(S\in\binom{[6]}3\), exactly six states occur: three with the hole in \(S\) and three with the hole in its complement. Each state with the hole in \(S\) slides to every one of the three states with the hole outside \(S\), and no same-side slides occur. Thus these six states form \(K_{3,3}\), and there are \(\binom63=20\) components.

**4. A three-slide recoloring lemma.** Let \(n\ge7\), fix the empty index \(h\), and consider an admissible assignment with \(p,q\ge2\). Changing the side of one selected vertex while keeping the hole at \(h\) can be performed by exactly three legal slides whenever the resulting counts remain at least two. For clarity, an expression \(a_i\to b_j\) denotes a slide, and all indices used as catalysts are distinct from the target and hole.

To recolor \(b_j\) to \(a_j\): if \(p,q\ge3\), choose \(i\in A\) and use
\[a_i\to b_h,\quad b_j\to a_i,\quad b_h\to a_j.\]
If \(p=2\), then \(q\ge4\); choose \(i\in B\setminus\{j\}\) and use
\[b_j\to a_h,\quad b_i\to a_j,\quad a_h\to b_i.\]
To recolor \(a_j\) to \(b_j\), use the symmetric sequences: for \(p,q\ge3\), choose \(i\in B\) and perform
\[b_i\to a_h,\quad a_j\to b_i,\quad a_h\to b_j;\]
if \(q=2\), then \(p\ge4\), choose \(i\in A\setminus\{j\}\) and perform
\[a_j\to b_h,\quad a_i\to b_j,\quad b_h\to a_i.\]
In every case the intermediate red and blue populations stay at least two, and inspection shows that exactly the target position is recolored and \(h\) is empty again. Because binary assignments with both population sizes in the interval \([2,n-3]\) are connected by permissible single-coordinate recolorings (change excess colors first, or interchange a miscolored pair through a temporary count of three at a boundary), these length-three moves connect **all** feasible color assignments with any fixed hole.

**5. Relocating the hole.** Suppose \(p,q\ge3\). To relocate the hole from \(h\) to an index \(j\in B\), choose any \(i\in A\) and slide \(a_i\to b_h\), then \(b_j\to a_i\). The effect is simply to replace the original selected \(b_j\) by \(b_h\) and move the hole to \(j\), preserving the other assignments and the two side populations. If \(j\in A\), the symmetric two-slide construction, using any \(i\in B\), has the same effect.

Given any two minimum codes with \(n\ge7\), first use the recoloring lemma at the initial hole to obtain \(p,q\ge3\). Move the hole to the target hole in two slides, and then recolor selected indices at that fixed hole to match the target code. Every intermediate state is optimal; hence \(\mathcal R_n\) is connected. This completes the proof.

## Verification
The attached standalone Python programs require no external libraries. `verify_direct.py` constructs the actual \(2n\)-vertex crown graph, exhaustively checks all smaller candidates and all size-\(n-1\) subsets, then builds the legal slide graph for \(5\le n\le9\). It verifies the exact optimum-state list, degree-sum edge counts, and component decomposition; for \(n=6\) it also checks each component is complete bipartite. `verify_structural.py` constructs the separate ternary-state graph for \(5\le n\le12\), verifies all components and edges, and tests 150 random pairs per \(n\ge7\) using explicit three-slide recolorings and two-slide hole transfers. Both programs were executed against the embedded versions and passed. These finite tests support implementation accuracy; the all-\(n\) connectivity assertion rests on the preceding proof, not on extrapolation from computations.

Run: `python3 verify_direct.py` and `python3 verify_structural.py`.

## Relationship to prior work
Identification using closed neighborhoods originated in the classical code literature. Gravier, Moncel, and Semri (2008) treat identifying codes of Cartesian products of cliques, a **different** graph family; Foucaud and Perarnau (2012) give general size bounds. Nikandish, Khani Nasab, and Dodonge (2020) compute the scalar minimum for complete bipartite graphs with a maximum matching deleted. Earlier archived mathematical records also establish the complete all-minimizer characterization and \(n(2^{n-1}-2n)\) count for balanced crowns; none of those scalar, enumerative, or code-skeleton statements by themselves determines the connected components under adjacency-restricted, optimum-preserving slides. Mynhardt and Teshima (2017), and Teshima's later dissertation, define minimum identifying-code reconfiguration and prove general realization theorems, not the present component classification for crowns. The conclusion is claim-relative: no equivalent crown slide-connectivity classification was found in inspected material, but the 2020 article's full body was inaccessible and historical priority is not independently certified.

## Limitations
The result concerns only labeled balanced crowns with \(n\ge5\), only radius-one closed-neighborhood identifying codes, and only adjacency-restricted **single** token slides at exact minimum cardinality. It does not establish shortest-path diameters in the connected regime, token-jump distances, or any corresponding theorem for unbalanced matching-deleted bipartite graphs. The entire novelty claim is relative to the stated comparisons and may be superseded by unindexed previous work. The 2020 matching-deletion article's abstract was available, but its full text could not be reviewed.

## References
- S. Gravier, J. Moncel, and A. Semri, *Identifying Codes of Cartesian Product of Two Cliques of the Same Size*, Electron. J. Combin. 15 (2008), #N4, first published 2008-02-11, DOI 10.37236/879.
- F. Foucaud and G. Perarnau, *Bounds for Identifying Codes in Terms of Degree Parameters*, Electron. J. Combin. 19 (2012), #P32, DOI 10.37236/2036.
- C. M. Mynhardt and L. E. Teshima, *A note on some variations of the gamma-graph*, arXiv:1707.02039, 2017.
- R. Nikandish, O. Khani Nasab, and E. Dodonge, *Minimum identifying codes in some graphs differing by matchings*, Discrete Math. Algorithms Appl. 12 (2020), 2050046, DOI 10.1142/S1793830920500469.
- L. E. Teshima, *The i-Graph and Other Variations on the gamma-Graph*, dissertation (2022), University of Victoria repository record published 2023-01-03.
