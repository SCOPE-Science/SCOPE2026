# Elementary-collapse dichotomy for tournaments with one transitive-deletion vertex

## Finding

Let \(T\) be a tournament with at least three vertices, and suppose that deleting a distinguished vertex \(h\) leaves a transitive tournament. Then its directed flag complex \(\operatorname{dFl}(T)\), consisting of all vertex subsets inducing acyclic subtournaments, admits a sequence of **elementary simplicial collapses** to either a single vertex or the boundary of a triangle. The latter occurs exactly when \(h\) points to a nonempty initial segment of the ordered transitive tournament and receives arrows from its nonempty final segment.

In the exceptional case the complex has homotopy type \(S^1\), and otherwise is simplicially collapsible. All integral homology above dimension one vanishes. For an order of the remaining \(n-1\) vertices, precisely \(n-2\) out of \(2^{n-1}\) orientations at the distinguished vertex yield the circle case.

## Assumptions and scope

Write the vertices outside \(h\) as \(u_1,\ldots,u_m\), where \(m=n-1\) and all their arcs point forward in this order. Define \(O=\{u_j:h\to u_j\}\) and \(I=\{u_j:u_j\to h\}\). These sets partition the \(m\) vertices. Let \(L\) denote the simplicial complex of subsets containing no pair \(o\in O\), \(i\in I\) with \(o\) preceding \(i\). Empty simplices are understood in cone and join notation, and all simplicial collapses are elementary free-face removals from the entire current complex.

The theorem is a classification for tournaments **admitting a vertex whose deletion is transitive**; no classification of arbitrary tournaments or higher-feedback-number tournaments is asserted. It also counts distinguished-vertex orientations, not distinct unlabeled tournaments.

## Proof

**1. The precise forbidden pairs.** A tournament has a directed cycle exactly when it has a directed triangle. Every triangle avoiding \(h\) is transitive. For \(a<b\) in the remaining order, the triangle \(\{h,u_a,u_b\}\) is directed cyclic exactly if \(u_a\in O\) and \(u_b\in I\). Let \(F\) be the bipartite graph on \(O\sqcup I\) consisting of those ordered pairs. Then \(L=\operatorname{Ind}(F)\), and the complete acyclic-set complex is

\[
\operatorname{dFl}(T)=\Delta(U)\cup\bigl(h*L\bigr),\qquad \Delta(U)\cap(h*L)=L,
\]

where \(U=V(T)\setminus\{h\}\) and \(\Delta(U)\) is the full simplex on \(U\).

**2. Elementary folds of the independence complex.** If \(O\ne\varnothing\), put \(p=\max O\) in the given order. For any \(o\in O\setminus\{p\}\), the open neighborhoods in \(F\) satisfy \(N_F(p)\subseteq N_F(o)\). Hence \(L\) elementarily collapses to the independence complex of the graph obtained by deleting \(o\): pair every face containing \(o\) and not \(p\) with the face also containing \(p\), in descending face-size order. Both faces are legal because \(p\) is nonadjacent to \(o\) and \(N_F(p)\subseteq N_F(o)\). The upper face is the unique remaining coface of the lower one at its removal. Do this for every \(o\ne p\).

The surviving graph has just the possible star edges from \(p\) to \(I_+=\{i\in I:p<i\}\), along with isolated vertices in \(I_-=\{i\in I:i<p\}\). If \(I_-\ne\varnothing\), a vertex in \(I_-\) is isolated, so the independence complex is a cone and collapses to that vertex. If \(I_+=\varnothing\), the entire surviving graph is edgeless and its independence complex is a simplex, again collapsing to one vertex. If \(I_-\) is empty and \(I_+\) is nonempty, the independence complex is the disjoint union of the vertex \(p\) and the simplex \(\Delta(I_+)\); the latter collapses to one vertex \(i\in I_+\), leaving the two vertices \(p,i\). If \(O\) is empty then \(F\) is edgeless and \(L\) is a simplex, so this is also the one-vertex case.

The two-vertex case therefore happens exactly when \(O,I\) are nonempty and every vertex of \(O\) precedes every vertex of \(I\).

**3. Lift the folds to the actual flag complex.** Any elementary pair \((\sigma,\tau)\) removed from \(L\) lifts to the elementary pair \((\{h\}\cup\sigma,\{h\}\cup\tau)\) in \(\Delta(U)\cup(h*L)\). All cofaces containing \(h\) correspond exactly to cofaces in the current copy of \(L\); the simplex \(\Delta(U)\) contributes no extra cofaces of a face containing \(h\). Thus the original complex collapses to \(\Delta(U)\) with either one edge from \(h\), or two such edges to \(p\) and \(i\).

In the one-edge case the free vertex \(h\) and its edge collapse away, and the full simplex \(\Delta(U)\) collapses to one vertex. In the two-edge case, successively remove every vertex of \(U\setminus\{p,i\}\) from \(\Delta(U)\) by the standard simplex collapse relative to the edge \(\{p,i\}\). The result is precisely the boundary graph of the triangle on \(\{h,p,i\}\). The elementary-collapse dichotomy follows.

**4. Integral homology and counting.** Elementary collapses are simple-homotopy equivalences. A vertex has zero reduced homology, whereas the three-edge cycle has exactly one integral degree-one class. If \(m\) outside vertices have fixed order, there are exactly \(m-1=n-2\) nonempty proper initial segments assignable to \(O\), among \(2^m\) possible assignments. This proves the claimed count without identifying differently distinguished representations of the same tournament.

## Verification

The included `verify.py` independently generates the directed flag complex by enumerating every nonempty vertex subset, constructs the explicit ordered elementary-collapse pairs, checks that each lower face has the displayed upper face as its **only** proper coface at that moment, and confirms the final one-vertex or three-edge boundary exactly. Exhaustive checks cover all distinguished-vertex orientations for orders \(3\le n\le9\): 4,092 instances and 196 circle cases, with the maximum of 127 internal folds. A five-vertex strongly connected tournament with outgoing-hub pattern `1010` collapses to a point, illustrating that strong connectivity does not imply the circle case. Run `python verify.py`; the exact captured output is included as `verification_output.txt`.

## Relationship to prior work

Govc (2020) develops directed flag complexes of tournaments, proves their fundamental groups are free, and computes finite tournament homotopy types. The earlier Burzio–Demaria classification of tournaments with nontrivial fundamental group, discussed by Kiihl and Guadalupe (2011), already addresses the fundamental-group distinction. **Neither the freeness theorem nor a fundamental-group criterion, on its own, proves the all-dimensional elementary-collapse statement here.** Deniz (2021/2022) studies sectionable tournaments and their Morse cell structures, which is a different hypothesis. The claimed contribution is the explicit, uniform **elementary-collapse dichotomy for every tournament with one transitive-deletion vertex**, not the general free-fundamental-group result or an independently novel characterization of the first homotopy group.

## Limitations

This does not establish uniqueness of the result against all historical literature. A plausible earlier related paper, Deniz's *Topology of acyclic complexes of tournaments and coloring* (2015), was found only in abstract form rather than fully inspected; it concerns trisectionable tournaments, and its possible additional specializations remain a bibliographic risk. The same remains true of older unindexed formulations. No statement is made for tournaments requiring deletion of two or more vertices to become transitive. Finite verification supports but does not replace the elementary-collapse proof above. No external independent audit has been performed.

## References

- Dejan Govc, *Computing Homotopy Types of Directed Flag Complexes*, 2020, arXiv:2006.05333, https://arxiv.org/abs/2006.05333 (first public 2020-06-09).
- Zakir Deniz, *Sectionable Tournaments: Their Topology and Coloring*, arXiv:2104.05839, https://arxiv.org/abs/2104.05839 (first public 2021-04-12).
- J. C. S. Kiihl and I. Valle Guadalupe, *Either Digraphs or Pre-Topological Spaces?* (2011), https://revistailuminart.ti.srt.ifsp.edu.br/iluminart/article/download/115/119 (section on classical simply disconnected tournaments).
- Zakir Deniz, *Topology of acyclic complexes of tournaments and coloring*, *Applicable Algebra in Engineering, Communication and Computing* 26 (2015), 213–226, https://doi.org/10.1007/s00200-014-0245-0 (abstract accessible, full text not verified).
- H. Belkhechine, H. Ben Salha, and F. Romdhane, *Irreducible pairings and indecomposable tournaments* (2023), arXiv:2312.04039, https://arxiv.org/abs/2312.04039 (tournament construction, not a topological theorem).
