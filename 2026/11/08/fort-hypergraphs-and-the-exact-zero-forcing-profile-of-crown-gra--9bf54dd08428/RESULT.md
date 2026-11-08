# Fort hypergraphs and the exact zero-forcing profile of crown graphs

## Finding

**Theorem.** For each integer \(n\ge 3\), let \(H_n=K_{n,n}\setminus M_n\) be the labelled crown graph with parts \(A=\{a_1,\ldots,a_n\}\) and \(B=\{b_1,\ldots,b_n\}\), where \(a_i\) and \(b_j\) are adjacent exactly when \(i\ne j\). Write \(A_I=\{a_i:i\in I\}\) and \(B_I=\{b_i:i\in I\}\).

The **entire family of inclusion-minimal forts** is exactly
\[
\bigl\{A_I:|I|=3\bigr\}\;\cup\;
\bigl\{B_I:|I|=3\bigr\}\;\cup\;
\bigl\{A_I\cup B_I:|I|=2\bigr\}.
\]
Consequently its cardinality enumerator is
\[
\mathcal F_n(t)=2\binom n3t^3+\binom n2t^4.
\]

A set \(S\subseteq V(H_n)\) is zero forcing if and only if, writing its white complement as \(V(H_n)\setminus S=A_X\cup B_Y\), one has
\[
|X|\le 2,\qquad |Y|\le 2,\qquad
\neg\bigl(|X|=|Y|=2\ \text{and}\ X=Y\bigr).
\]
Thus the zero-forcing polynomial, counting **all** labelled zero-forcing sets by their sizes, is
\[
\boxed{\mathcal Z_n(z)=\left(z^n+nz^{n-1}+\binom n2z^{n-2}\right)^2-\binom n2z^{2n-4}.}
\]
All inclusion-minimal zero-forcing sets have the same size \(2n-4\), and there are exactly \(\binom n2\bigl(\binom n2-1\bigr)\) of them.

For the maximum number \(\operatorname{ft}(H_n)\) of pairwise disjoint forts, fractional zero-forcing number \(Z^*(H_n)\) (the fractional transversal number of the minimal-fort hypergraph), and ordinary zero-forcing number \(Z(H_n)\), one has
\[
\boxed{\operatorname{ft}(H_n)=\left\lfloor\frac{2n}{3}\right\rfloor,\qquad
Z^*(H_n)=\frac{2n}{3},\qquad Z(H_n)=2n-4.}
\]
In particular, \(Z(H_n)/Z^*(H_n)=3-6/n\), which tends to \(3\). The maximal-failed-zero-forcing-set polynomial is
\[
2\binom n3z^{2n-3}+\binom n2z^{2n-4}.
\]

## Assumptions and scope

All graphs are finite, simple, undirected and vertex-labelled. A **fort** is a nonempty vertex set \(F\) such that every vertex outside \(F\) has either zero or at least two neighbors in \(F\). A fort is **inclusion-minimal** when it contains no proper nonempty fort. A **zero-forcing set** is an initial blue set from which the standard rule, “a blue vertex with exactly one white neighbor makes that neighbor blue,” eventually colors every vertex blue. These definitions apply for every integer \(n\ge3\), including the six-cycle \(H_3\) and cube \(H_4\). No assertion is made for the disconnected graphs obtained at \(n=1,2\).

The fort number is the maximum cardinality of a family of pairwise disjoint forts. The fractional parameter minimizes \(\sum_{v\in V(H_n)}w_v\) over \(w_v\ge0\) satisfying \(\sum_{v\in F}w_v\ge1\) for every inclusion-minimal fort \(F\). The cardinality polynomials count vertex subsets, not automorphism orbits.

## Proof

**1. Exact classification of forts.** For a nonempty candidate \(F=A_X\cup B_Y\), put \(a=|X|\) and \(b=|Y|\). Its neighbors in \(F\), when the vertex itself is outside \(F\), obey
\[
|N(a_i)\cap F|=b-\mathbf1_{\{i\in Y\}}\quad(i\notin X),\qquad
|N(b_i)\cap F|=a-\mathbf1_{\{i\in X\}}\quad(i\notin Y).
\]
Every three-element subset of either part is a fort: its outside neighbors are always zero, two or three. Every \(A_I\cup B_I\) with \(|I|=2\) is also a fort: every outside vertex lies outside the two chosen indices and sees exactly two vertices of the opposite part.

Suppose \(F\) is an inclusion-minimal fort. If \(a\ge3\), then \(F\) contains a pure \(A\)-triple fort and therefore equals that triple; similarly \(b\ge3\) forces \(F\) to be a pure \(B\)-triple. It remains to analyze \(a,b\le2\). If one of \(a,b\) is zero and the other is one or two, an outside vertex has exactly one neighbor in \(F\): for two vertices in one part, use the opposite vertex with one of their indices; for one vertex, use any opposite vertex with a different index (possible since \(n\ge3\)). If \(b=2\) and \(a\le1\), choose \(i\in Y\setminus X\); then the outside vertex \(a_i\) has exactly one neighbor in \(F\). The case \(a=2,b\le1\) is symmetric. If \(a=b=1\), there is an index outside \(X\cup Y\) (as \(n\ge3\)), giving a blue vertex with exactly one neighbor in \(F\). Finally, if \(a=b=2\) but \(X\ne Y\), choose \(i\in Y\setminus X\); again \(a_i\) has exactly one neighbor in \(F\). Therefore the only possible fort with \(a,b\le2\) is \(a=b=2\) and \(X=Y\), which was already proved to be a fort. Its proper nonempty subsets are not forts by the same cases. The pure triples also have no proper nonempty fort subset. This proves the exact, nonredundant minimal-fort list.

**2. Forts and zero forcing.** If the white set contains a fort, no force can ever color the first vertex of that fort: every outside vertex sees either zero or at least two white vertices of it. Conversely, if a zero-forcing procedure stops with a nonempty white set \(W\), every blue vertex sees either zero or at least two vertices of \(W\), so \(W\) itself is a fort. Thus an initial blue set succeeds exactly when its white complement contains no fort. Every fort contains an inclusion-minimal fort, by finite descent. By part 1, the complement \(A_X\cup B_Y\) contains no fort exactly when \(|X|,|Y|\le2\) and it does not contain a matched-index four-set. Within these size bounds, the latter condition means not both \(X\) and \(Y\) equal the same two-element set. This proves the characterization.

**3. Exact polynomials and minimality.** For each part separately the size-generating polynomial of blue sets leaving at most two white vertices is
\[
z^n+nz^{n-1}+\binom n2z^{n-2}.
\]
The choices of white indices on the two sides are independent, except for the \(\binom n2\) forbidden pairs \(X=Y\) of size two. Subtracting their contribution proves \(\mathcal Z_n(z)\). In particular, the smallest exponent is \(2n-4\), with coefficient \(\binom n2(\binom n2-1)>0\) for every \(n\ge3\).

Every allowed pair \((X,Y)\) can be extended, without losing the stated condition, to two **unequal** two-element sets \((X',Y')\). Indeed, if one side already has two elements, the other side can be extended to a different two-set; any prescribed singleton belongs to at least \(n-1\ge2\) two-sets. If both sides have at most one element, extend one side arbitrarily and the other to a different two-set. Hence any successful blue set strictly larger than \(2n-4\) contains a smaller successful blue set. Conversely, removing any blue vertex from a successful set with exactly two white vertices on each side creates at least three whites on one side, which includes a triple fort and fails. Therefore these, and only these, are the inclusion-minimal zero-forcing sets.

A failed zero-forcing set is inclusion-maximal as failed exactly when its white complement is an inclusion-minimal fort: this follows immediately from the fort-obstruction characterization and complementation. Taking the complements of the classified triples and matched-index fours proves the maximal-failed polynomial.

**4. Fort packing and the fractional optimum.** Since each inclusion-minimal fort has at least three vertices and any disjoint fort packing can be replaced by one consisting of minimal subforts, there can be at most \(\lfloor2n/3\rfloor\) disjoint forts. Write \(n=3q+r\), with \(r\in\{0,1,2\}\). Select \(q\) disjoint triples from each part, using the same \(3q\) index positions on both sides. If \(r=2\), add the matched-index four-set using the two remaining indices. The resulting number of pairwise disjoint forts is \(2q+\mathbf1_{\{r=2\}}=\lfloor2n/3\rfloor\), proving the packing formula.

For fractional zero forcing, the constant assignment \(w_v=1/3\) is feasible: each pure triple has total weight one and each matched-index four-set weight \(4/3\). Thus \(Z^*(H_n)\le2n/3\). Conversely, sum the constraints \(\sum_{i\in I}w_{a_i}\ge1\) over all \(\binom n3\) triples \(I\). Each \(a_i\) appears in \(\binom{n-1}{2}\) such constraints, giving \(\sum_i w_{a_i}\ge n/3\). The same argument in the other part gives \(\sum_i w_{b_i}\ge n/3\). Hence the objective is at least \(2n/3\), establishing equality. The ordinary forcing number and the ratio follow from part 3.

## Verification

The standalone finite checker `verify.py` uses only the Python standard library and constructs the labelled crown graph from its adjacency relation. It tests **every vertex subset** for \(3\le n\le8\), applies the zero-forcing rule directly, checks the actual fort condition, verifies that every fort contains one of the classified minimal forts, verifies that each classified candidate is a fort with no proper nonempty fort subset, and compares the entire zero-forcing polynomial with the formula. It also computes optimal disjoint fort packings independently by subset dynamic programming for \(3\le n\le7\).

Run `python3 verify.py`. A successful run ends with `VERIFY_OK`. The verifier checks 87,360 vertex subsets in total, finding 3,037 zero-forcing sets and 66,243 forts. An additional numerical linear-program comparison of the minimal-fort fractional transversal for \(3\le n\le8\) agreed with the analytic value \(2n/3\); this numerical check is supplementary, and the unrestricted fractional result is proved by the explicit matching upper and lower certificates above.

## Relationship to prior work

Boyer, Brimkov, English and collaborators introduced the zero-forcing polynomial and established general extremal-coefficient results (arXiv:1801.08910, first public 2018). These results do not enumerate all size classes of the crown-graph family. Pelayo and Abara (arXiv:2202.04997, first public 2022) study maximal failed forcing sets for Cartesian, strong, lexicographic and corona graph products, not the direct product \(K_n\times K_2\) constituting the crown graph. Curtis, Gan, Haddock, Lawrence and Spiro (arXiv:2208.12899, first public 2022) study random zero-forcing sets and general coefficient inequalities; their inspected family-specific calculations do not give the crown-graph coefficient distribution.

Cameron, Hogben, Kenter, Mojallal and Schuerger (arXiv:2310.17904, first public 2023-10-27) introduce the minimal-fort hypergraph and fractional zero-forcing number and compute those parameters for several graph families including complete bipartite graphs. Their inspected graph-family results and summary table do not state the crown-graph classification. Their general definitions and duality are used here, not claimed as new. The crown \(K_{n,n}\setminus M_n\) is not a complete bipartite graph when \(n\ge3\), so those complete-bipartite parameter formulas do not imply the present values. In fact, deleting the matching changes the known fractional value \(Z^*(K_{n,n})=n\) to \(2n/3\), whereas the integral zero-forcing number changes from \(2n-2\) to \(2n-4\).

## Limitations

The theorem concerns standard zero forcing and simple labelled crown graphs only, with \(n\ge3\). It does not assert analogous formulas for general matching-deleted bipartite graphs or higher bipartite Kneser graphs. Finite exhaustive tests are not an infinite proof; all infinite conclusions above follow from the fort classification and the supplied arguments. Originality is qualified by possible unindexed or later equivalent literature and has not been independently assessed. No claim is made about uniqueness of optimal fractional weight assignments.

## References

1. K. Boyer, B. Brimkov, S. English, D. Ferrero, A. Keller, R. Kirsch, M. Phillips and C. Reinhart, *The zero forcing polynomial of a graph*, arXiv:1801.08910, first posted 2018-01-26, https://arxiv.org/abs/1801.08910.
2. P. A. B. Pelayo and M. N. M. Abara, *Maximal failed zero forcing sets for products of two graphs*, arXiv:2202.04997, first posted 2022-02-10, https://arxiv.org/abs/2202.04997.
3. B. Curtis, L. Gan, J. Haddock, R. Lawrence and S. Spiro, *Zero Forcing with Random Sets*, arXiv:2208.12899, first posted 2022-08-27, https://arxiv.org/abs/2208.12899.
4. T. R. Cameron, L. Hogben, F. H. J. Kenter, S. A. Mojallal and H. Schuerger, *Forts, (fractional) zero forcing, and Cartesian products of graphs*, arXiv:2310.17904, first posted 2023-10-27, https://arxiv.org/abs/2310.17904.
5. E. W. Weisstein, *Crown Graph*, MathWorld, https://mathworld.wolfram.com/CrownGraph.html (family identification only).
