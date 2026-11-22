# Six minimal forbidden bipartite patterns for a common-determinant dependence split

## Finding

Let \(X,Y,Z\) be finite nonempty sets with \(|X|=m\), \(|Y|=r\), and \(|Z|=s\). For teams \(T\subseteq X\times Y\times Z\), consider the lax-splitting dependence-logic formula
\[
\Phi=\operatorname{dep}(x,y)\lor\operatorname{dep}(x,z).
\]
A team is *minimally falsifying* when it does not satisfy \(\Phi\), but all its proper subteams do.

**Theorem (complete forbidden-pattern basis and exact census).** Every minimally falsifying team is concentrated in a unique \(x\)-fiber. Regard that fiber as the edge set of a simple bipartite graph with named shores \(Y\) and \(Z\). Up to permutations within each shore, its edge set is precisely one of these six types:

1. Three independent edges \(3K_2\) (three assignments).
2. A four-cycle \(C_4\) (four assignments).
3. A five-vertex, four-edge path \(P_5\), with middle vertex in \(Y\).
4. The same \(P_5\), with middle vertex in \(Z\).
5. Two disjoint two-edge stars \(2K_{1,2}\), with both centers in \(Y\).
6. The same two-star forest, with both centers in \(Z\).

Conversely, every such graph, in any one \(x\)-fiber, is minimally falsifying. Therefore the full size enumerator of minimally falsifying labelled teams is
\[
\mathcal B_{m;r,s}(t)=m\bigl(A_{r,s}t^3+B_{r,s}t^4\bigr),
\]
where
\[
A_{r,s}=6\binom r3\binom s3
\]
and
\[
\begin{aligned}
B_{r,s}={}&\binom r2\binom s2
+2r\binom{r-1}2\binom s2
+2s\binom{s-1}2\binom r2\\
&+6\binom r2\binom s4
+6\binom s2\binom r4.
\end{aligned}
\]
The convention is \(\binom nk=0\) for \(n<k\). In particular, for one fiber with \(r=s=2\), there is one minimal falsifier, while \(r=s=3\) gives six of size three and forty-five of size four, and \(r=s=4\) gives ninety-six and three hundred ninety-six respectively. An arbitrary finite team satisfies \(\Phi\) if and only if it contains **no** subteam of the six described pattern types.

## Assumptions and scope

A team is a set, not a multiset, of assignments to the three **named** variables \(x,y,z\). An atom \(\operatorname{dep}(x,y)\) holds when equal \(x\)-coordinates force equal \(y\)-coordinates; the other atom is analogous. Lax disjunction permits a cover of the team by two (possibly overlapping or empty) subteams, satisfying the respective disjuncts. Because dependence atoms are downward closed, an overlapping cover can be replaced by a partition. All alphabets are finite and nonempty; they need not have equal sizes. For the pattern classification, graph isomorphisms must preserve the two named shores. Terms such as \(C_4\), \(P_5\), and \(K_{1,2}\) refer to ordinary finite simple graphs.

## Proof

**1. Fiberwise reduction.** For every \(a\in X\), let \(E_a=\{(b,c)\in Y\times Z:(a,b,c)\in T\}\). A split witnessing \(\Phi\) restricts in each \(x\)-fiber to one set with a common \(y\)-value and another with a common \(z\)-value. Hence for some \(b_a\in Y\) and \(c_a\in Z\),
\[
E_a\subseteq (\{b_a\}\times Z)\cup(Y\times\{c_a\}).
\]
Conversely, if this containment holds for every fiber, assign to the first subteam those assignments with \(y=b_a\) and to the second subteam all remaining assignments; the remaining ones have \(z=c_a\). Thus the split exists. Equivalently, \(\Phi\) holds exactly when each bipartite edge set \(E_a\) has a vertex cover comprising at most one vertex of \(Y\) and at most one vertex of \(Z\). Call this *cross-coverable*.

If a minimally falsifying team had nonempty edges in two fibers, its unsatisfied fiber could be retained while deleting all assignments in the others, contradicting minimality. Thus it has precisely one nonempty fiber, which must itself be inclusion-minimal among non-cross-coverable edge sets.

**2. Reduction to at most four edges.** Consider a non-cross-coverable simple bipartite edge set \(E\). If it has a matching of size at least three, select three independent edges. These three edges are non-cross-coverable: a row and column jointly touch at most two edges of the matching. If the matching number is at most two, the bipartite vertex-cover theorem (Kőnig's theorem) supplies a vertex cover of size at most two. A cover of size zero or one makes \(E\) cross-coverable, as does a two-vertex cover meeting both shores. Therefore the cover has two vertices on the same shore; suppose they lie in \(Y\). If either chosen vertex has degree at most one, the other \(Y\)-vertex together with the unique adjacent \(Z\)-vertex (if any) cross-covers \(E\). Consequently each chosen \(Y\)-vertex has at least two different neighbours. Choose two incident edges at each. No cross can cover these four edges: choosing either of the two \(Y\)-vertices leaves two edges on the other, with different \(Z\)-endpoints; choosing a different \(Y\)-vertex leaves all four. The four selected edges therefore form a falsifying subteam. The case where the two cover vertices lie in \(Z\) is symmetric.

**3. Exhaustive classification under minimality.** If \(E\) is inclusion-minimal and contains a three-edge matching, it equals that matching. Otherwise, the preceding proof produces a non-cross-coverable four-edge subset, so minimality forces \(E\) to have exactly four edges: two incident to each of two same-shore centers, with distinct neighbours at each center. Their neighbour pairs have intersection size zero, one, or two. These cases are respectively the disjoint two-star forest, the five-vertex path, and the four-cycle. The chosen shore of the centers distinguishes two versions of the first two cases; the cycle is independent of that choice. This gives the six listed shore-preserving types.

Every listed graph is non-cross-coverable. For the matching, a cross meets at most two of three edges. For the other five types, a cross containing one center misses two edges incident to the other center, while a cross containing neither center also misses edges. Deleting any one edge from the three-matching leaves only two edges, covered by selecting one endpoint in each shore. Deleting any one edge from a four-edge pattern leaves a graph with one center of degree at most one while the other center covers the other two edges, so the resulting three-edge set is cross-coverable. Downward closure then gives cross-coverability for all proper subsets. Thus all six types are precisely the minimal falsifiers.

**4. Enumerating the six disjoint types.** Three-edge matchings are obtained by choosing three vertices in each shore and a bijection, giving \(6\binom r3\binom s3\). Four-cycles are chosen by selecting two vertices in each shore, giving \(\binom r2\binom s2\). To form a path with middle vertex in \(Y\), choose that vertex, two other \(Y\)-vertices, two \(Z\)-vertices, and one of two bijections from the ends to the \(Z\)-vertices. The count is \(2r\binom{r-1}2\binom s2\); exchange \(r,s\) for the opposite orientation. To form two disjoint two-edge stars centered in \(Y\), choose two \(Y\)-centers and four \(Z\)-leaves and allocate two leaves to the first chosen center; this has \(\binom42=6\) choices. The count is \(6\binom r2\binom s4\), and exchanging shores yields the last term. Six graph types are disjoint, and all patterns lie in one of \(m\) possible \(x\)-fibers, completing the size polynomial and the forbidden-pattern test.

## Verification

The standalone Python 3 program `verify.py` examines all subsets of \(Y\times Z\) for each of sixteen alphabet pairs with \(1\le r,s\le4\), checks minimality directly, classifies every observed graph by its two degree signatures, and compares each count with the two formulas. For all pairs with \(r,s\le3\), it also independently tests *every possible split* of each team instead of relying on the cross criterion. It additionally enumerates the two-fiber binary case to confirm the claimed fiberwise minimal-falsifier count. Run `python3 verify.py`; its final line begins `VERIFY_OK`. These finite tests support, but do not replace, the all-cardinality mathematical proof above.

## Relationship to prior work

Fröhlich, Kolaitis and Meier prove that the formula \(\operatorname{dep}(x,y)\lor\operatorname{dep}(x,z)\) has coherence level four (their Theorem 22), meaning a false team contains a false subteam of at most four assignments. This already establishes a *cutoff*, and is not claimed as new here. Their work does not state the six exhaustive shore-preserving minimal-falsifier shapes or their exact labelled counts. The previously published exact satisfying-team size enumerator uses the same cross-coverability criterion and counts **all satisfying teams**, not the canonical inclusion-minimal *failing* teams or their graph types; the present result is not obtained by matching any coefficient of that enumerator. The 2026 general coherence study addresses first-order rewritability and complexity of coherence rather than these counts. Other recorded results on disjoint-variable or inverse functional-dependence splits concern nonequivalent formulas; their enumerators do not specialize to this shared-determinant formula. The use of Kőnig's theorem and the elementary cross description are credited as known tools, not new results.

## Limitations

This classification concerns exactly the given two-atom split, with a common determinant and finite set-valued teams. It makes no claim about arbitrary dependence-logic formulas, strict disjunction, multiteams, constrained input relations beyond a chosen Cartesian product, or minimal falsifiers for other variable-overlap patterns. The enumeration distinguishes all named alphabet values and is not a count modulo relabelling. Published priority has been compared with accessible primary sources and related records but cannot be guaranteed globally, particularly against uncatalogued bipartite forbidden-pattern enumerations. Mathematical verification is a proof and finite cross-checks, not an independent formal certification.

## References

1. N. Fröhlich, P. G. Kolaitis, A. Meier, *Disjunctions of Two Dependence Atoms*, first public preprint 22 August 2025, arXiv:2508.16146, https://arxiv.org/abs/2508.16146; CSL 2026, DOI:10.4230/LIPIcs.CSL.2026.10, https://drops.dagstuhl.de/storage/00lipics/lipics-vol363-csl2026/html/LIPIcs.CSL.2026.10/LIPIcs.CSL.2026.10.html. Especially Theorem 22 and its proof.
2. *Exact size enumerator for a two-dependence-atom disjunction*, published mathematical record 18 October 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-exact-size-enumerator-for-a-two-dependence-atom-disjunction--e22bc6a91416. Especially RESULT.md, Finding and Proof, for the cross description and the all-satisfying-team enumerator.
3. T. Barlag, N. Fröhlich, M. Hannula, P. G. Kolaitis, J. Kontinen, A. Meier, J. Väänänen, *Aspects of Coherence in Dependence Logic*, first public preprint 29 May 2026, arXiv:2605.31269, https://arxiv.org/abs/2605.31269. Introductory material and abstract inspected; later sections not fully accessible.
4. D. König, *Graphen und Matrizen*, Matematikai és Fizikai Lapok 38 (1931), 116–119; classical bipartite matching–vertex-cover theorem, used only as a standard lemma.
