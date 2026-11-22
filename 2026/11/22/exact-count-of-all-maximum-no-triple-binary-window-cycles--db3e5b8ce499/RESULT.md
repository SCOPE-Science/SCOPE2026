# Exact count of all maximum no-triple binary window cycles

## Finding
For every integer \(n\ge4\), let \(C_n\) count **all** rotation classes of circular binary words whose cyclic length-\(n\) windows are pairwise distinct, whose cyclic runs of either symbol have length at most two, and whose length is the largest possible under these conditions. Rotations are identified; reflection and bit complementation are **not** identified.

Prior work establishes that the optimum length is \(2(F_{n+1}-F_{n-3})\), with \(F_0=0\), \(F_1=1\), and \(F_{j+2}=F_{j+1}+F_j\), and that the set of windows of every maximizer is precisely
\[
E_n=\{w\in\{0,1\}^{n}:w\text{ avoids }000,111\text{ and }\neg[(w_1=w_2)\wedge(w_{n-1}=w_n)]\}.
\]
The **new enumeration result** is an exact, all-order determinant for the number of distinct maximizers, not merely their known maximum length or their known support.

Let \(B_n\) be the length-\((n-1)\) words avoiding \(000,111\) whose first adjacent pair and last adjacent pair both consist of distinct bits. Then \(|B_n|=2F_{n-2}\). For each \(v\in B_n\) and each bit \(b\in\{0,1\}\), append \(b\), shift left by one position, and, until another state of \(B_n\) is reached, repeatedly shift and append the bit **opposite** the current final bit. This defines two distinguishable directed arcs from \(v\) to vertices of \(B_n\). Let \(A_n\) be their adjacency matrix, retaining multiplicity, and let \(r=0101\cdots\) truncated to length \(n-1\). The exact count is
\[
\boxed{C_n=\det\!\left((2I-A_n)_{B_n\setminus\{r\},\,B_n\setminus\{r\}}\right),\qquad n\ge4.}
\]
The determinant has dimension \(2F_{n-2}-1\), less than the \(2F_n-1\) dimension of the uncontracted overlap-graph cofactor. (The latter graph has \(2F_n\) vertices.) The entries are explicit nonnegative arc multiplicities apart from the Laplacian diagonal.

Exact values obtained by integer arithmetic are:

| \(n\) | Optimal length (known) | Number of rotation classes \(C_n\) |
|---:|---:|---:|
| 4 | 8 | 1 |
| 5 | 14 | 5 |
| 6 | 22 | 12 |
| 7 | 36 | 44 |
| 8 | 58 | 6720 |
| 9 | 94 | 1832544 |
| 10 | 152 | 48681971200 |
| 11 | 246 | 4431338775673113600 |

## Assumptions and scope
All circular words are nonempty, indexed over the labeled alphabet \(\{0,1\}\); cyclic windows wrap around the endpoint. A circular word of length \(m\) provides exactly \(m\) indexed length-\(n\) windows, even when \(m<n\). The two forbidden triples apply across the boundary. A cycle is considered the same after rotation only. Distinct edge labels are kept distinct in the overlap multigraph, including when compressed paths have identical endpoints. The maximum-length and unique-window-support premises are cited, previously established results rather than new claims.

## Proof
**1. Fixed overlap graph.** Let \(G_n\) be the directed overlap graph with one labeled arc for each word in \(E_n\), running from its length-\((n-1)\) prefix to its length-\((n-1)\) suffix. Every length-\((n-1)\) word avoiding the two triples is a vertex, since it has at least one retained incoming and outgoing extension. The previously established optimum-and-rigidity theorem identifies all the required maximizers with the edge-distinguished Euler circuits of \(G_n\), modulo cyclic choice of starting edge. Its proof also establishes that \(G_n\) is strongly connected and balanced. These facts can be independently seen as follows: append the complement of the current last bit repeatedly to reach an alternating vertex; such edges cannot be excluded because their last two bits differ. The two alternating vertices communicate. Starting at an alternating vertex whose last bit differs from the first bit of a chosen target, append the target's bits. During these \(n-1\) shifts the initial two bits of every length-\(n\) arc differ, so no arc is excluded, and the unequal junction prevents a triple. This reaches every target. Finally, reversal interchanges in- and out-extensions and direct inspection of the first and last adjacent pairs gives equal degrees below.

**2. Degree-two vertices.** For any vertex \(v\), two extensions are allowed exactly when both its initial and terminal adjacent pairs differ; these vertices constitute \(B_n\). Otherwise there is exactly one outgoing extension, namely append the bit opposite to its current last bit. The same degree classification holds for incoming arcs. Thus every vertex has equal indegree and outdegree, both in \(\{1,2\}\). To count \(B_n\), select the first letter in two ways, fix the first and last run lengths to one, and decompose the remaining \(n-3\) positions into runs of lengths one or two. The number of such compositions is \(F_{n-2}\). Hence \(|B_n|=2F_{n-2}\).

**3. Forced-corridor contraction.** Every nonbranch vertex has only one outgoing arc. Iterating it appends the opposite of the last bit, so after at most \(n-1\) steps it has shifted into an alternating word, which belongs to \(B_n\). Consequently no directed cycle consists solely of nonbranch vertices. Contract each such forced corridor between successive branch vertices, retaining the first-arc label so that parallel arcs remain distinguishable. This constructs precisely the two-outregular directed multigraph \(H_n\) with adjacency matrix \(A_n\). In-arborescences directed to \(r\) in \(G_n\) and \(H_n\) are in bijection: in any such tree the unique outgoing edge of every nonbranch vertex is forced; choosing one outgoing edge of each nonroot branch produces a tree exactly when the compressed choices are acyclic and lead to \(r\). Every cycle in the original choices contains a branch and projects to a compressed cycle, proving both directions.

**4. Euler circuits to a determinant.** The directed BEST theorem counts edge-distinguished Euler circuits up to starting-edge rotation as
\[
t_r(G_n)\prod_{v\in V(G_n)}(\deg^+(v)-1)!=t_r(G_n),
\]
since every outdegree is one or two. The binary window labels are distinct and determine the cyclic word, so there is no further quotient factor. By Step 3, \(t_r(G_n)=t_r(H_n)\). The directed matrix-tree theorem applied to the outgoing Laplacian \(2I-A_n\) expresses this in-arborescence count as the displayed principal cofactor. This establishes the exact formula for every \(n\ge4\).

## Verification
Run `python3 verify.py` with Python 3 (standard library only). Its exact fraction-free integer determinant is applied to the contracted graph for \(4\le n\le11\), independently to the full overlap graph for \(4\le n\le9\), and checked against a separate direct Euler-circuit enumeration with a fixed initial labeled edge for \(4\le n\le7\). The same script regenerates the allowed windows, checks balance, verifies branch characterization, and tests directed reachability in the compressed graph. These finite checks confirm the displayed table and implementation, while the proof supplies the all-order statement.

## Relationship to prior work
Chee, Etzion, Nguyen, Ta, Tran, and Vu analyze maximum-length run-limited sequences for a one-sided run cap and enumerate admissible necklaces and maximum lengths; Section 4 of their 2024 preprint does not enumerate all two-sided no-triple maximizers. Sawada, Williams, and Wong study generalized greedy and necklace constructions of universal cycles, not the complete two-sided optimal-tour population. A related 2026 result supplies the **previously proved** sharp two-sided maximum length and the unique window set \(E_n\), explicitly leaving enumeration of maximizers outside its scope. Another 2026 result gives a compressed-tree count for the **different** one-sided no-adjacent-ones language; its branching predicate, graph, and numerical counts are different. Neither result determines the present all-order enumeration. BEST and the directed matrix-tree theorem themselves are classical and are not asserted as novel.

## Limitations
The new contribution is the exact count of all maximal cycles for the binary two-sided cap of two; maximum length and the rigid window set are cited premises. The count is determinant-defined, not a closed elementary product. Values are evaluated through \(n=11\); larger \(n\) are covered by the proof, not by numerical extrapolation. This does not enumerate minimum cyclic covering words when repeated windows are allowed, optimize a one-sided constraint, or identify words under reflection/complement. Unindexed equivalent historical treatments remain a possible priority risk. No independent mathematical audit is asserted.

## References
1. Y. M. Chee, T. Etzion, T. L. Nguyen, D. H. Ta, V. D. Tran, V. K. Vu, *Maximum Length RLL Sequences in de Bruijn Graph*, arXiv:2403.01454, first public version 2024-03-03, especially Sections 2–4. https://arxiv.org/abs/2403.01454
2. J. Sawada, A. Williams, D. Wong, *Generalizing the Classic Greedy and Necklace Constructions of de Bruijn Sequences and Universal Cycles*, Electron. J. Comb. 23(1), P1.24 (2016), DOI 10.37236/5517. https://doi.org/10.37236/5517
3. *Sharp Fibonacci capacity and canonical window set for doubly run-limited de Bruijn cycles* (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-sharp-fibonacci-capacity-and-canonical-window-set-for-doubly-run--aa3ac12cc70f
4. *Exact count of all maximum-length no-adjacent-ones de Bruijn cycles* (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-count-of-all-maximum-length-no-adjacent-ones-de-bruijn-cyc--19257b27b2ec
5. The directed BEST theorem and directed matrix-tree theorem (standard Euler-tour and arborescence counting tools).
