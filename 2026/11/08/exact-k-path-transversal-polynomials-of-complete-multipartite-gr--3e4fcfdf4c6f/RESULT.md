# Exact \(k\)-path transversal polynomials of complete multipartite graphs

## Finding
Let \(G=K_{n_1,\ldots,n_r}\), with \(r\ge2\), positive part sizes \(n_i\), and \(N=\sum_i n_i\). Fix an integer \(4\le k\le N\). A vertex set is \(P_k\)-free if its induced subgraph contains no ordinary (not necessarily induced) path on \(k\) vertices. Write \(\mathcal A_{G,k}(z)\) for the cardinality polynomial of all \(P_k\)-free sets and \(\mathcal M_{G,k}(z)\) for that of their inclusion-maximal members.

Put
\[
t=\left\lfloor\frac{k-2}{2}\right\rfloor,\qquad
c=k-1-t=\left\lceil\frac{k}{2}\right\rceil,\qquad
q_G=N-\max_i n_i,
\]
and define the explicit coefficient
\[
B_{G,k}=[u^{k-1}]\prod_{i=1}^r
\left(\sum_{j=0}^{\min(n_i,c-1)}\binom{n_i}{j}u^j\right).
\]
Then
\[
\boxed{\mathcal A_{G,k}(z)=
\sum_{s=0}^{k-1}\binom Ns z^s+
\sum_{i=1}^r\sum_{b=0}^{t}\sum_{a=k-b}^{n_i}
\binom{n_i}{a}\binom{N-n_i}{b}z^{a+b}.}
\]
Here and below empty sums equal zero. Moreover,
\[
\boxed{\mathcal M_{G,k}(z)=
\begin{cases}
z^N,&q_G\le t,\\[2mm]
B_{G,k}z^{k-1}+\displaystyle\sum_{i:n_i\ge c}
\binom{N-n_i}{t}z^{n_i+t},&q_G>t.
\end{cases}}
\]
The polynomial counting inclusion-minimal \(k\)-path vertex covers is exactly \(z^N\mathcal M_{G,k}(z^{-1})\); this is a polynomial because \(\mathcal M_{G,k}\) has degree at most \(N\).

The maximal-set formula is a full structural classification. If \(q_G>t\), each maximal \(P_k\)-free set is either (i) a set of \(k-1\) vertices with no part occupancy exceeding \(c-1\), or (ii) a complete part of size at least \(c\), together with exactly \(t\) selected vertices outside that part. These two types are disjoint. If \(q_G\le t\), the entire graph is \(P_k\)-free and its vertex set is the unique maximal set.

For the balanced complete bipartite graph \(K_{m,m}\), this produces an exact parity dichotomy. For \(h\ge2\) and \(m\ge h+1\),
\[
\mathcal M_{K_{m,m},2h+1}(z)
=\binom mh^2 z^{2h}+2\binom m{h-1}z^{m+h-1}.
\]
For \(h\ge2\) and \(m\ge h\),
\[
\mathcal M_{K_{m,m},2h}(z)=2\binom m{h-1}z^{m+h-1}.
\]
Thus all inclusion-minimal even-order path covers of \(K_{m,m}\) have the same cardinality, whereas the odd-order case has two cardinalities as soon as \(m\ge h+2\). For fixed \(h\) and \(m\ge h+3\), the odd-order maximal \(P_k\)-free spectrum misses all \(m-h-2\) integers from \(2h+1\) through \(m+h-2\). The fraction of its maximal \(P_k\)-free sets belonging to the larger-cardinality class is
\[
\frac{2\binom m{h-1}}{\binom mh^2+2\binom m{h-1}}
=2h\,h!\,m^{-(h+1)}(1+O(m^{-1})).
\]
Equivalently, almost all inclusion-minimal odd-order path covers have cardinality \(2m-2h\), although their minimum cardinality is \(m-h+1\).

## Assumptions and scope
Graphs are finite, simple and undirected. Parts are distinguished vertex classes, and vertices within a part are labeled for counting. A \(k\)-path is a simple path with \(k\) distinct vertices; extra edges among path vertices do not invalidate it. Inclusion maximality is with respect to adding graph vertices, not edge-maximality or maximum cardinality. The theorem covers all \(r\ge2\), positive \(n_i\), and \(4\le k\le N\), including the boundary where \(G\) has no \(k\)-path. Binomial coefficients outside their ordinary ranges are zero. The known \(k=3\) dissociation case is deliberately not asserted as a new result.

## Proof
**Longest-path occupancy lemma.** For a selected nonempty set \(S\), let \(s=|S|\), let \(x_i\) count its vertices in part \(i\), let \(L=\max_i x_i\), and let \(q=s-L\). The largest number of vertices on a simple path of \(G[S]\) is
\[
\ell(S)=\min\{s,2q+1\}.
\]
Indeed, between two appearances of a vertex from a part attaining \(L\), a path needs a vertex outside that part, giving the upper bound \(2q+1\). If \(L\ge q+1\), alternate \(q+1\) vertices of the largest part with all \(q\) outside vertices to attain that bound. If \(L\le q+1\), the elementary rearrangement criterion for a multiset says its class labels can be ordered without equal adjacent labels exactly when the largest multiplicity is at most one more than the sum of the others; this yields a spanning path on all \(s\) selected vertices. For completeness, that criterion follows by arranging the largest class in distinct gaps among the remaining classes (or by repeatedly placing the two currently largest distinct classes); the maximum multiplicity inequality is preserved at each placement. Every two consecutive different class labels are adjacent in a complete multipartite graph. The empty set has \(\ell=0\).

Consequently,
\[
G[S]\text{ is }P_k\text{-free}\quad\Longleftrightarrow\quad
s\le k-1\ \text{or}\ q\le t.
\]
Every selected set of size at most \(k-1\) is feasible. For size at least \(k\), feasibility requires \(q\le t\), and therefore the largest selected part has \(s-q\ge k-t>t\) vertices. That part is unique; choose it as part \(i\), choose \(a\) of its vertices and \(b\le t\) of the other \(N-n_i\) vertices, with \(a+b\ge k\). Such sets are counted once by the triple sum in \(\mathcal A_{G,k}\), proving the all-set formula.

If \(q_G\le t\), the longest-path lemma makes \(V(G)\) itself feasible; it is the unique inclusion-maximal feasible set. Assume henceforth \(q_G>t\), so that \(V(G)\) is infeasible. A maximal feasible set \(S\) cannot have fewer than \(k-1\) vertices: if it did, adding one vertex would still leave fewer than \(k\) vertices.

Suppose first \(s=k-1\). If \(q\ge t+1\), adding any unselected vertex increases \(s\) to \(k\) but cannot decrease \(q=s-L\): the largest part occupancy can rise by at most one. Thus every extension contains a \(k\)-path, so \(S\) is maximal. These are exactly the profiles with \(L\le k-1-(t+1)=c-1\), counted by \(B_{G,k}\). If \(q\le t\), any unselected vertex in a largest occupied part could be added without changing \(q\), so maximality forces that entire part to be selected. If \(q<t\), there is an unselected vertex outside that part (otherwise \(S=V(G)\)), and adding it keeps \(q\le t\); hence maximality fails. Thus \(q=t\), the selected largest part is complete and has exactly \(c=k-1-t\) vertices, giving the boundary case of type (ii).

Suppose next \(s\ge k\). Feasibility forces \(q\le t\). Again, an unselected vertex in a largest occupied part could be added while keeping \(q\) fixed, so that part must be complete. If \(q<t\), an unselected vertex outside it exists (since \(V(G)\) is infeasible) and could be added; hence \(q=t\). The full selected part then has \(n_i=s-t\ge k-t>c\) vertices. Conversely, a full part of size \(n_i\ge c\) accompanied by \(t\) outside vertices is feasible, and every further addition is outside its uniquely largest selected part (because \(c>t\)), increasing \(q\) to \(t+1\) and producing a \(k\)-path. It is maximal.

Counting all choices in type (ii) yields \(\binom{N-n_i}{t}\) sets for each eligible part \(i\). Type (ii) has a unique full dominant part, so there is no double counting; type (i) has smaller maximum occupancy. This proves \(\mathcal M_{G,k}\). Complements give inclusion-minimal path covers, because a set hits all \(k\)-paths if and only if its complement is \(P_k\)-free.

For \(G=K_{m,m}\) and \(k=2h+1\), we have \(t=h-1\) and \(c=h+1\). A balanced profile of size \(2h\) with both occupancies at most \(h\) must be \((h,h)\), accounting for \(\binom mh^2\) sets, while the two full-part classes contribute \(2\binom m{h-1}\). For \(k=2h\), the balanced profile would require \(2h-1\) vertices with at most \(h-1\) in each of two parts, which is impossible. This establishes both parity formulas. Their supports give the gap count, and expansion of the displayed binomial ratio with fixed \(h\) yields the stated asymptotic probability.

## Verification
The accompanying standard-library program `verify.py` directly searches for ordinary simple \(k\)-paths using graph adjacency rather than the occupancy lemma. For all positive nondecreasing multipartite size vectors of total order \(4\) through \(10\), with at least two parts, and all \(4\le k\le\min(N,8)\), it compares the full cardinality distributions of feasible and inclusion-maximal subsets against the exact formulas. It also checks the balanced-bipartite parity identities arithmetically for \(2\le h\le8\) and \(h+1\le m\le24\). Run `python verify.py` from a directory containing that file. The check produced `VERIFY_OK instances=557 independently_tested_subsets=320576 all_and_maximal_polynomials=PASS bipartite_parity_cases=PASS`.

## Relationship to prior work
The \(k\)-path vertex cover problem and its practical motivation are established in Bujtás–Jakovac–Tuza (arXiv:2105.02018, first publicly posted May 5, 2021). Li–Zuo (2018) and Tu (2022, Theorems 37–38) supply scalar minimum \(k\)-path vertex-cover values for complete bipartite graphs. Those scalar values agree with, and are recovered from, the largest degree of \(\mathcal M_{G,k}\), but do not determine its coefficients, inclusion-minimal classes, or parity dichotomy. The longest-path occupancy fact is classical (compare Gutin 1993) and is not claimed as novel. General \(k=3\) dissociation-set enumerations are likewise prior work. The contribution here is the complete all-set and maximal-set enumerators for arbitrary complete multipartite profiles and the resulting exact parity and gap laws.

## Limitations
The result concerns complete multipartite graphs and ordinary path subgraphs, not induced-path-free sets in arbitrary graphs. It makes no algorithmic improvement claim for general graphs and no independent verification claim. Finite enumeration checks are supporting evidence, not a proof for unbounded parameters. An especially relevant Li–Zuo 2018 paper was available in abstract and secondary theorem quotations but not in its complete publisher text; thus undetected equivalent prior enumeration remains a publication-priority risk. No independent mathematical audit has been performed.

## References
1. C. Bujtás, M. Jakovac, Z. Tuza, *The \(k\)-path vertex cover: general bounds and chordal graphs*, arXiv:2105.02018 (first version May 5, 2021), https://arxiv.org/html/2105.02018v1 .
2. Z. Li and L. Zuo, *The \(k\)-path vertex cover in Cartesian product graphs and complete bipartite graphs*, Applied Mathematics and Computation 331 (2018), 69–79, https://doi.org/10.1016/j.amc.2018.03.008 .
3. J. Tu, *A Survey on the \(k\)-Path Vertex Cover Problem*, Axioms 11 (2022), 191, https://doi.org/10.3390/axioms11050191 .
4. G. Gutin, *Finding a longest path in a complete multipartite digraph*, SIAM Journal on Discrete Mathematics 6 (1993), 270–273, https://doi.org/10.1137/0406020 .
