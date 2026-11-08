# Idempotent-rank spectra of strict graph semigroups on paths and cycles

## Finding
For every finite simple graph \(G\), let \(\operatorname{St}(G)\) be the semigroup of partial transformations of its vertex set whose inverse image of each vertex is either empty or exactly one edge, and whose inverse image of every edge is also either empty or an edge. Let
\[
E_G(t)=\sum_{\substack{f\in\operatorname{St}(G)\\ f^2=f}}t^{|\operatorname{im} f|}.
\]
Then for the path \(P_n\) with \(n\ge1\) vertices,
\[
\boxed{E_{P_n}(t)=\sum_{k=0}^{\lfloor n/2\rfloor}\binom{2n-3k+1}{k}t^k,\qquad
\sum_{n\ge0}E_{P_n}(t)x^n=\frac1{1-x-2tx^2+t^2x^4}.}
\]
In the generating function only, \(P_0\) denotes the empty graph, with \(E_{P_0}(t)=1\).

For the simple cycle \(C_n\) with \(n\ge3\),
\[
\boxed{E_{C_n}(t)=\sum_{k=0}^{\lfloor n/2\rfloor} c_{n,k}t^k,\qquad
c_{n,k}=\begin{cases}
\displaystyle\frac{n}{n-2k}\binom{2n-3k-1}{k},&2k<n,\\[4pt]
4,&2k=n.
\end{cases}}
\]
Every coefficient counts idempotents of exactly the specified transformation rank, not arbitrary elements of the strict semigroup. In particular, maximum-rank idempotents number \(\lfloor n/2\rfloor+1\) for \(P_{2\lfloor n/2\rfloor}\), \(\binom{(n-1)/2+3}{3}\) for odd paths, \(4\) for even cycles, and \(n(n+1)/2\) for odd cycles.

For every finite graph \(G\) whose connected components are paths, cycles or isolated vertices, \(E_G(t)\) is the product of the displayed component polynomials. **Every zero of \(E_G(t)\) is real and strictly negative.** Consequently its nonzero coefficient sequence is ultra-log-concave and hence unimodal.

## Assumptions and scope
All graphs are finite, undirected and simple. A partial map is allowed to be empty. The rank of a partial map is its number of image vertices. The strict semigroup \(\operatorname{St}(G)\) is not generally a monoid with the identity map. The conventional cycle \(C_n\) is used only for \(n\ge3\). The graph \(P_n\) has \(n\) vertices. The product formula also applies to disconnected graphs of maximum degree at most two; the empty graph has polynomial \(1\).

## Proof
**1. Idempotents as oriented matchings.** By the definition of \(\operatorname{St}(G)\), a strict map has domain a union of pairwise disjoint edges, and has an independent image set, with each domain edge collapsed to its associated image vertex (the matching-independent-image characterization in Margolis–Rhodes, Lemma 3.3). If \(f^2=f\), then every vertex in \(\operatorname{im}f\) is fixed. The image vertex assigned to a particular domain edge must therefore lie on that very edge: it lies in a domain edge, and its image equals itself, so it belongs to its own nonempty fiber. Conversely, choosing a matching of edges and selecting one endpoint from each, with all selected endpoints pairwise nonadjacent, defines a strict idempotent. Thus the rank-\(k\) idempotents are in bijection with \(k\)-edge matchings with one marked endpoint per edge and with the marked endpoints independent. No other idempotents exist.

**2. Paths.** Read the vertices of \(P_n\) from left to right. Each oriented matching is a tiling into \(m=n-2k\) unused single vertices (monomers) and \(k\) ordered adjacent pairs (dimers), each dimer marked \(L\) if its left endpoint is selected and \(R\) if its right endpoint is selected. The selected endpoints are nonadjacent exactly when two consecutive dimers are not in the forbidden order \(RL\), with no intervening monomer. A run of \(r\) consecutive dimers therefore has exactly \(r+1\) valid markings, namely \(L^aR^{r-a}\) with \(0\le a\le r\). The \(m\) monomers separate the dimers into \(m+1\) runs of lengths totaling \(k\). Hence the number of rank-\(k\) idempotents is
\[
[t^k](1-t)^{-2(m+1)}=\binom{2m+k+1}{k}=\binom{2n-3k+1}{k}.
\]
The weighted ordinary generating series over \(n\) is obtained by putting \(n=m+2k\):
\[
\sum_{m\ge0}\sum_{k\ge0}\binom{2m+k+1}{k}x^{m+2k}t^k
=\sum_{m\ge0}\frac{x^m}{(1-tx^2)^{2m+2}}
=\frac1{(1-tx^2)^2-x}.
\]
This equals the claimed rational function and implies the fourth-order recurrence \(E_{P_n}=E_{P_{n-1}}+2tE_{P_{n-2}}-t^2E_{P_{n-4}}\) for \(n\ge4\), with \(E_{P_0}=E_{P_1}=1\), \(E_{P_2}=1+2t\), and \(E_{P_3}=1+4t\).

**3. Cycles.** Let \(k\) edges be selected in \(C_n\). If \(m=n-2k>0\), select one of the \(n\) labeled vertices as a distinguished monomer; cyclically from this vertex, the \(m\) monomers determine \(m\) runs of dimers, whose length-sum is \(k\). Again a run of \(r\) dimers has \(r+1\) markings. Summing the product of these counts gives \([u^k](1-u)^{-2m}=\binom{2m+k-1}{k}\). Each actual idempotent has exactly \(m\) choices for the distinguished monomer, whereas the initial marked vertex has \(n\) choices. Therefore the desired number is \(\frac{n}{m}\binom{2m+k-1}{k}\). If \(m=0\), necessarily \(n=2k\ge4\); there are two perfect matchings of the even cycle, and for each only the two constant orientation choices avoid the forbidden \(RL\) adjacency around the circle, giving exactly four idempotents. The formula also covers \(k=0\), producing the unique empty partial map.

**4. Connected components.** An idempotent sends every nonempty matching fiber to a vertex of that same fiber, hence to its own connected component. Its restrictions to distinct components are independently strict idempotents. This gives \(E_{G\sqcup H}=E_GE_H\), including isolated vertices which contribute factor \(1\).

**5. Real-rootedness.** Define an oriented-edge conflict graph \(H(G)\) whose vertices are pairs \((e,v)\) with \(e\in E(G)\) and \(v\) one endpoint of \(e\). Distinct pairs conflict if their underlying edges coincide, their underlying edges share an endpoint, or their selected endpoints are adjacent in \(G\). By part 1, \(E_G(t)\) is exactly the independence polynomial of \(H(G)\).

For a path or cycle of length at least four, index successive edges \(e_i=\{i,i+1\}\) linearly or cyclically and write \(L,R\) for the selected left/right endpoint. The neighbors of \((e_i,L)\) are contained in the union of the two cliques
\[
\{(e_{i-2},R),(e_{i-1},L),(e_{i-1},R)\},\qquad
\{(e_i,R),(e_{i+1},L),(e_{i+1},R)\},
\]
with nonexistent edge indices omitted. Similarly, the neighbors of \((e_i,R)\) are contained in the two cliques
\[
\{(e_{i-1},L),(e_{i-1},R),(e_i,L)\},\qquad
\{(e_{i+1},L),(e_{i+1},R),(e_{i+2},L)\}.
\]
For the shortest cycle \(C_3\), all distinct oriented edges conflict, so \(H(C_3)\) is complete. The path case with at most three vertices is immediate. This neighborhood two-clique property proves that \(H(G)\) is claw-free for all graphs with maximum degree at most two (disjoint unions preserve the property). The Chudnovsky–Seymour theorem states that the independence polynomial of every claw-free graph is real-rooted. The positive coefficients and constant coefficient one exclude nonnegative real zeros, proving strict negativity whenever the polynomial is nonconstant. Newton's inequalities give ultra-log-concavity of its coefficients (divided by the corresponding binomial coefficients), and therefore unimodality.

For the top rank, the path formula gives \(k+1\) at \(n=2k\), and \(\binom{k+3}{3}\) at \(n=2k+1\); the cycle formula gives \(4\) at \(n=2k\ge4\) and \(n(k+1)=n(n+1)/2\) at \(n=2k+1\).

## Verification
A standalone Python 3 checker, `verify.py`, independently enumerates all partial maps for small paths/cycles and tests the original inverse-image definition plus \(f^2=f\). It separately enumerates oriented matchings, enumerates independent sets of the conflict graph, and tests its claw-free property across larger finite cases. It compares each rank polynomial against both exact formulas and reports `VERIFY_OK`. The direct finite enumerations corroborate the theorem but do not prove it for unbounded graph sizes; the symbolic argument above does.

For instance,
\[
E_{P_6}(t)=1+10t+21t^2+4t^3,\qquad
E_{C_6}(t)=1+12t+30t^2+4t^3.
\]

## Relationship to prior work
Margolis and Rhodes (arXiv:2609.39370, first submitted 2026-09-30) define \(\operatorname{St}(G)\), give its matching/independent-image description (Lemma 3.3), prove regularity for path and cycle examples (Theorems 7.3 and 7.4), and count *all strict maps* by rank in Section 8. They construct some explicit idempotents in Section 11. None of those statements gives the number of composition-idempotent maps of each rank: for idempotents the selected image vertices must lie on their associated domain edges. The formulas here enumerate that constrained subfamily.

Chudnovsky and Seymour's 2007 theorem is the known general real-rootedness result and is not asserted as new. The new application consists of the oriented-edge conflict construction and its claw-free structure, coupled to the exact idempotent-rank formulas. Older papers on degree-two continuous-map semigroups and idempotents of different diagram monoids do not imply the displayed exact path/cycle formulas through the statements examined.

## Limitations
No assertion is made that \(E_G(t)\) is real-rooted for arbitrary graphs of degree greater than two, nor that the exact formulas describe the full Margolis–Rhodes monoid \(\operatorname{MR}(G)\). The polynomials count composition-idempotents of the **strict** subsemigroup only. The Cauchy/independence-polynomial consequence uses the established Chudnovsky–Seymour theorem. Historical priority under alternative enumerative formulations remains subject to further specialist comparison. Computations were exhaustive only for the finite cases specified in the checker and are not substitutes for the symbolic proof.

## References
- S. Margolis and J. Rhodes, *The Margolis-Rhodes Monoid of a Graph* / *The Margolis-Rhodes Monoid of Continuous Functions on a Graph*, arXiv:2609.39370v2 (first version 2026-09-30), Sections 3, 7, 8, 11, 12. https://arxiv.org/pdf/2609.39370v2
- S. W. Margolis and J. Rhodes, *Degree 2 Transformation Semigroups as Continuous Maps on Graphs: Foundations and Structure*, arXiv:2005.02606 (2020). https://arxiv.org/abs/2005.02606
- M. Chudnovsky and P. Seymour, *The roots of the independence polynomial of a clawfree graph*, J. Combin. Theory Ser. B 97 (2007), 350–357, DOI: 10.1016/j.jctb.2006.06.001.
