# Complete general-position enumerators and gapped maximal spectra of rook graphs

## Finding
Let \(2\le m\le n\), and let \(R_{m,n}=K_m\square K_n\) be the rook graph on the \(m\)-by-\(n\) board. A *general-position set* is a vertex set containing no three vertices on one shortest path. A set is *maximal* if it cannot be enlarged while preserving this property. Let \(P_{m,n}(z)\) count all general-position sets (including the empty set) by cardinality, and let \(M_{m,n}(z)\) count inclusion-maximal general-position sets by cardinality.

Work with formal power series in commuting variables \(x,y,z\), and define
\[
 B(x,y,z)=xyz+x(e^{zy}-1-zy)+y(e^{zx}-1-zx),
\]
\[
 L(x,y,z)=x(e^{zy}-1-zy),\qquad
 R(x,y,z)=y(e^{zx}-1-zx).
\]
Then the two complete labeled counting polynomials are
\[
 \boxed{P_{m,n}(z)=m!n!\,[x^my^n]\exp(x+y+B(x,y,z))}
\]
and
\[
 \boxed{M_{m,n}(z)=m!n!\,[x^my^n]\left(\exp B+(e^x-1)\exp L+(e^y-1)\exp R\right).}
\]
The coefficients are nonnegative integers, and these identities hold simultaneously for every pair of integers \(2\le m\le n\).

**Maximal cardinality spectrum.** Exactly the following sizes occur among inclusion-maximal general-position sets:
\[
 \boxed{\operatorname{supp}M_{m,n}=\{m\}\cup\{n,n+1,\ldots,m+n-2\}.}
\]
Here \(\operatorname{supp}M=\{k:[z^k]M>0\}\); the second interval is interpreted as the integers from \(n\) through \(m+n-2\). Consequently, for \(n\ge m+2\), every size strictly between \(m\) and \(n\) is absent. In particular, these gaps have unbounded length even on the two-row rook graphs, for which
\[
 \boxed{M_{2,n}(z)=nz^2+2^nz^n\qquad(n\ge2).}
\]
Terms of the same degree are combined when \(n=2\).

**Boundary multiplicities.** Write \(S_{\ge2}(m,t)\) for the number of partitions of an \(m\)-element labeled set into exactly \(t\) blocks, each of cardinality at least two, and \((n)_t=n!/(n-t)!\). Then
\[
 [z^m]M_{m,n}(z)=
 \begin{cases}
 \displaystyle\sum_{t=1}^{\lfloor m/2\rfloor}(n)_tS_{\ge2}(m,t),&m<n,\\[3pt]
 \displaystyle m!+2\sum_{t=1}^{\lfloor m/2\rfloor}(m)_tS_{\ge2}(m,t),&m=n.
 \end{cases}
\]
The maximum-degree coefficient is \(mn\) when \(m\ge3\), equals \(2^n\) when \(m=2<n\), and equals \(6\) when \(m=n=2\).

For example,
\[
 M_{2,5}(z)=5z^2+32z^5,\qquad
 M_{3,5}(z)=5z^3+213z^5+15z^6,
\]
\[
 M_{4,4}(z)=104z^4+144z^5+16z^6.
\]

## Assumptions and scope
All graphs are finite and simple. The Cartesian product \(K_m\square K_n\) has vertices \((i,j)\), adjacent when exactly one coordinate differs. Both factors have order at least two. All sets and graph vertices are labeled; no quotient by row or column symmetry is taken. A maximal set is maximal **under inclusion**, not necessarily of maximum size. Coefficient extraction is formal, so no analytic convergence assumption is needed. The associated Stirling number \(S_{\ge2}(m,t)\) is zero outside its natural range.

## Proof
**1. General-position sets are bipartite star forests.** Distinct squares of a rook graph have distance one if they share a row or column, and distance two otherwise. Three selected squares violate general position exactly when their induced subgraph contains a three-vertex path with its endpoints nonadjacent. Thus the induced graph on a selected set must be a disjoint union of cliques. Identify a square \((i,j)\) with the edge joining left vertex \(i\) to right vertex \(j\) in \(K_{m,n}\). Under this identification, the rook graph is the line graph of \(K_{m,n}\). Any clique of size at least two in this line graph consists of edges incident to one common original vertex: a competing triangle configuration is impossible because \(K_{m,n}\) is bipartite. Distinct induced clique components use disjoint original vertices. Hence selected squares are in general position if and only if their corresponding original edges form a disjoint union of nonempty stars (including one-edge stars). Isolated original bipartite vertices are allowed.

**2. All-set enumeration.** The exponential generating weights of a single nonempty star component, with \(x\) for left vertices, \(y\) for right vertices, and \(z\) for selected edges, are: \(xyz\) for a one-edge star; \(x(e^{zy}-1-zy)\) for a star with its center on the left and at least two leaves on the right; and \(y(e^{zx}-1-zx)\) for the reverse orientation. Their sum is \(B\). A star forest is an unordered set of disjoint star components, contributing \(\exp B\). Arbitrarily many isolated original left or right vertices contribute \(\exp(x+y)\). Extracting the coefficient of \(x^my^n\) and restoring the labels by \(m!n!\) gives \(P_{m,n}\).

**3. Inclusion-maximal star forests.** Suppose the chosen original edges form a star forest \(F\). If \(F\) has unused original vertices on both sides, an edge between two unused vertices can be added, so the corresponding general-position set is not maximal. If no original vertices are unused, \(F\) is maximal: an unchosen edge joins vertices in different nontrivial star components and creates a three-edge path, or lies within one star (and is already present). The former is not a star forest; the latter supplies no new edge. No one-star spanning configuration exists for \(m,n\ge2\).

Now suppose at least one left vertex is unused, but every right vertex is used. If any component is a one-edge star, connecting its right endpoint to an unused left vertex enlarges it to a larger star, contradicting maximality. Similarly, if any component has its center on the right, an unused left vertex can be joined to that center. Thus every nontrivial component must be centered on the left and have at least two right leaves. Conversely, when every right vertex belongs to such a component, every additional original edge either creates a path of three edges across components or joins an unused left vertex to a right leaf of a nontrivial star, again creating a path of three edges. Hence precisely these configurations are maximal. The third case, with unused right vertices, is symmetric. This proves the exhaustive, disjoint classification: (a) no unused original vertices; (b) unused left vertices only, with nontrivial left-centered stars; (c) unused right vertices only, with nontrivial right-centered stars.

Case (a) contributes \(\exp B\), case (b) contributes \((e^x-1)\exp L\), and case (c) contributes \((e^y-1)\exp R\). Extracting labeled coefficients proves the claimed maximal-set generating function.

**4. Cardinality support and constructions.** In case (a), if there are \(c\) star components, the spanning forest has \(m+n-c\) edges. Because each star uses at least one left vertex, \(2\le c\le m\). Every integer in this range occurs: make \(c-2\) disjoint single-edge stars, leaving at least two original vertices on each side; on the remaining vertices take one star centered on a left vertex, with all but one remaining right vertex as leaves, and a second star centered on that last right vertex, with all remaining left vertices as leaves. Therefore the spanning cases have precisely sizes \(n,n+1,\ldots,m+n-2\). In case (b), every right vertex is a leaf of exactly one left-centered star, so there are exactly \(n\) selected edges. In case (c), there are exactly \(m\). Both nonspanning cardinalities occur, from a full row and a full column respectively. The stated spectrum follows, including the possibility that \(m=n\).

**5. Extremal multiplicities.** For \(m<n\), an inclusion-maximal set of size \(m\) must be a case-(c) forest. Its \(m\) left vertices are partitioned into \(t\) groups of size at least two, assigned injectively to \(t\) distinct right centers, yielding \((n)_tS_{\ge2}(m,t)\). Summing proves the first formula. When \(m=n\), case (b) contributes the same count, and case (a) contributes exactly the \(m!\) perfect matchings with \(m\) single-edge stars. This proves the second formula.

For \(m,n\ge3\), a largest configuration has \(m+n-2\) edges and exactly two spanning star components. Both cannot be centered on the same side because that would cover at most two vertices of that side, which has at least three. Thus exactly one center lies on each side; choosing these centers gives \(mn\) possibilities, with every other original vertex forced to join the opposite-side center. When \(m=2\), every spanning two-component star forest is a surjection assigning the \(n\) right vertices to the two left centers, contributing \(2^n-2\). The additional two full rows are maximal and have cardinality \(n\), giving \(2^n\). The square \(2\)-by-\(2\) board has four vertices arranged as a cycle, and every two-vertex subset is maximal: there are six. This finishes the theorem.

## Verification
The accompanying standalone Python 3 program `verify.py` uses only the standard library. For eight boards from \(2\times2\) to \(4\times4\), it directly enumerates every vertex subset, checks general position by shortest-path distances of selected triples, tests inclusion maximality through one-vertex extensions, and compares both entire distributions with exact bivariate exponential-generating-function calculations. It examines \(104272\) subsets, finding \(3543\) general-position subsets and \(665\) maximal ones. Independently, it checks the complete maximal-cardinality support and the minimum/maximum coefficient formulas for \(41\) additional pairs of board dimensions. The verifier returns `VERIFY_OK`. These finite checks supplement, but do not replace, the unrestricted proof.

## Relationship to prior work
Di Stefano, Klavžar, Krishnakumar, Tuite, and Yero (2023, arXiv:2306.09965), Theorem 5.3, determine the *minimum cardinality* of a maximal general-position set of a Cartesian product of complete graphs. The resulting scalar \(\operatorname{gp}^{-}(K_m\square K_n)=\min(m,n)\) is already known. Klavžar, Patkós, Rus, and Yero (2021) establish the corresponding *maximum* cardinality \(m+n-2\). Both results are recovered here but are not new claims. Anand, Chandran, Changat, Klavžar, and Thomas (2019) establish a general structural characterization of arbitrary graph general-position sets; this work specializes the diameter-two case and supplies new family-specific enumeration and maximality analysis. Iršič, Klavžar, Rus, and Tuite (2024, arXiv:2401.05696) introduce the general-position polynomial and count several families, including Cartesian products of paths, but do not give the above two rook-graph polynomials in their inspected presentation. No inspected source supplied the exact all-set and maximal-set distributions, the maximal-set support gap, or these boundary multiplicities. This is a best-knowledge comparison, not proof of publication priority.

## Limitations
The theorem concerns labeled rook graphs with both factors of order at least two, not arbitrary Cartesian products or generic line graphs. The generating functions count graph-theoretic general-position sets, not nonattacking-rook placements. Earlier scalar extrema and the generic disjoint-clique criterion are acknowledged as known. Novelty remains contingent on publications or databases not identified in the searches. Computational verification covers finite cases only; the proof is the evidence for all parameters.

## References
1. G. Di Stefano, S. Klavžar, A. Krishnakumar, J. Tuite, I. Yero, *Lower General Position Sets in Graphs*, arXiv:2306.09965 (initial public version 2023-06-16), https://arxiv.org/abs/2306.09965.
2. V. Iršič, S. Klavžar, G. Rus, J. Tuite, *General Position Polynomials*, arXiv:2401.05696 (2024), https://arxiv.org/abs/2401.05696.
3. S. Klavžar, B. Patkós, G. Rus, I. G. Yero, *On General Position Sets in Cartesian Products*, Results in Mathematics 76 (2021), DOI:10.1007/s00025-021-01438-x, https://link.springer.com/article/10.1007/s00025-021-01438-x.
4. B. S. Anand, U. Chandran S. V., M. Changat, S. Klavžar, E. J. Thomas, *Characterization of General Position Sets and Its Applications to Cographs and Bipartite Graphs*, arXiv:1812.08460, https://arxiv.org/abs/1812.08460.
