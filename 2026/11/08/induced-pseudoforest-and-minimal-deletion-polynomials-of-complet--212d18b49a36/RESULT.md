# Induced pseudoforest and minimal-deletion polynomials of complete multipartite graphs

## Finding

Let \(r\ge3\), let \(n_1,\ldots,n_r\ge1\) be integers, put \(N=\sum_i n_i\), and let \(G=K_{n_1,\ldots,n_r}\). A pseudoforest has at most one cycle in each connected component. Let \(P_G(z)\) count all vertex sets \(S\subseteq V(G)\) for which \(G[S]\) is a pseudoforest, and let \(M_G(z)\) count inclusion-maximal such sets, each by cardinality.

Put \(s=|\{i:n_i=1\}|\), \(q_2=|\{i:n_i=2\}|\), and
\[
B=\sum_{1\le i<j\le r}\binom{n_i}{2}\binom{n_j}{2},
\qquad
E_3=\sum_{1\le i<j<k\le r}n_i n_j n_k.
\]
The complete polynomials are
\[
\begin{aligned}
P_G(z)={}&\sum_{k=0}^{3}\binom Nk z^k
+\sum_{i=1}^{r}\sum_{k=4}^{n_i}\binom{n_i}{k}z^k\\
&+\sum_{i=1}^{r}(N-n_i)\sum_{k=3}^{n_i}\binom{n_i}{k}z^{k+1}+Bz^4,
\end{aligned}
\]
\[
\boxed{M_G(z)=(E_3+s q_2)z^3+Bz^4+\sum_{i:n_i\ge3}(N-n_i)z^{n_i+1}.}
\]
Empty sums are zero. Coincident exponents contribute to the same coefficient. The complementary inclusion-minimal pseudoforest-deletion sets are enumerated by \(z^N M_G(z^{-1})\).

In particular, for every integer \(m\ge5\), the connected, regular, vertex-transitive graph \(K_{m,m,m}\) has
\[
M_{K_{m,m,m}}(z)=m^3z^3+3\binom m2^2z^4+6mz^{m+1}.
\]
Its inclusion-maximal induced pseudoforests have exactly the cardinalities \(\{3,4,m+1\}\), so every cardinality \(5,6,\ldots,m\) is impossible. A uniformly selected maximal induced pseudoforest has cardinality four with probability \(1-\frac{4}{3m}+O(m^{-2})\), although the maximum cardinality is \(m+1\); the probability of maximum cardinality is \(8m^{-3}+O(m^{-4})\).

## Assumptions and scope

All graphs are finite, simple, and undirected. A vertex set is **inclusion-maximal** if no strict superset induces a pseudoforest; this is distinct from having largest cardinality. A deletion set \(D\) is **inclusion-minimal** if deleting \(D\) leaves a pseudoforest and no proper subset of \(D\) does. The graph has at least three nonempty partite classes; no assertion is made for an empty part or a one- or two-part presentation. Binomial coefficients with \(k>n\) vanish by the usual convention. The polynomial \(P_G\) includes the empty vertex set.

## Proof

**Classification of allowable profiles.** Let \(p_i=|S\cap V_i|\), and let \(q\) be the number of positive \(p_i\). If \(q\le1\), the induced graph has no edges. For \(q=2\), its only nontrivial component is \(K_{a,b}\), with \(a,b\ge1\), \(a+b\) vertices and \(ab\) edges. A connected finite graph has at most one cycle if and only if its edge count does not exceed its vertex count, so the condition is
\[
ab\le a+b\iff(a-1)(b-1)\le1.
\]
Thus either \(a=1\), \(b=1\), or \(a=b=2\). For \(q\ge3\), if some part contributes at least two vertices, the induced graph contains \(K_{2,1,1}\), which has five edges on four vertices, hence at least two independent cycles. If four parts contribute, the induced graph contains \(K_4\), also not a pseudoforest. Conversely, three parts each contributing one vertex induce one triangle. Therefore the complete list of allowed positive profiles is: one occupied part of arbitrary size; two occupied parts with occupancies \((a,1)\) or \((2,2)\); and three occupied parts with occupancies \((1,1,1)\).

**Classification of maximal profiles.** Pseudoforesthood is hereditary under deleting vertices, so maximality is equivalent to the impossibility of adding any one outside vertex. A one-part profile is never maximal, since another nonempty part can contribute one vertex. A two-part profile \((1,1)\) is not maximal because \(r\ge3\) and adding one vertex from a third part creates a triangle. A profile \((a,1)\), \(a\ge3\), is maximal exactly when all \(n_i=a\) vertices of its larger part \(i\) are present: otherwise that part can be enlarged, while after it is full any other addition yields \((a,2)\) or \((a,1,1)\), neither of which is allowed. A profile \((2,1)\) is maximal exactly when its size-two occupied part is a full part of size \(2\) and its singleton occupied part is a full part of size \(1\). Indeed, any unused vertex from either occupied part would extend it to an allowed \((3,1)\) or \((2,2)\); with both parts full any vertex from a third part creates a forbidden \((2,1,1)\). Every \((2,2)\) profile is maximal, since adding to either part produces \((3,2)\) and adding in any third part produces \((2,2,1)\). Every \((1,1,1)\) profile is maximal, since any extra vertex produces \((2,1,1)\) or occupies a fourth part. This proves necessity and sufficiency.

**Counting.** Every vertex set of cardinality at most three is a pseudoforest. At cardinality at least four, the allowable profiles are uniquely: a selection of at least four vertices from one part; a selection of at least three from part \(i\) and exactly one from outside it; or a selection of exactly two from each of two parts. They contribute the three additional terms of \(P_G\), without duplication. For maximal profiles, triangles selected from three parts contribute \(E_3 z^3\). The exceptional full-part stars \((2,1)\) contribute \(s q_2z^3\). Four-cycles \((2,2)\) contribute \(Bz^4\). Full-part stars of larger part size \(n_i\ge3\) contribute \((N-n_i)z^{n_i+1}\). This proves the displayed formula for \(M_G\). Complementation exchanges maximal induced-pseudoforest vertex sets with minimal deletion sets, proving the reciprocal formula.

**Balanced tripartite graphs.** Setting \(r=3\) and all \(n_i=m\ge5\) gives \(E_3=m^3\), \(B=3\binom m2^2\), \(s=q_2=0\), and \(\sum_i(N-n_i)=6m\). The three exponents are distinct. The missing interval has \(m-4\) integers. The total number of maximal sets is \(m^3+3\binom m2^2+6m\). Since \(3\binom m2^2=\frac34 m^4-\frac32m^3+O(m^2)\), division gives the two stated probability expansions. The graph is connected and vertex-transitive because all parts have equal size. This finishes the proof.

## Verification

The self-contained script `pseudoforest_verifier.py` reconstructs complete multipartite adjacency, checks every vertex subset for the componentwise cycle condition by a graph search and edge count, and tests maximality through all one-vertex extensions. It compares independently obtained cardinality Counters with both formulas for 52 unordered positive part-size tuples with three to five parts and total order at most twelve. It tests another 47 balanced triples by symbolic binomial arithmetic. Running `python3 pseudoforest_verifier.py` produced:

```
VERIFY_OK graph_instances=52 candidate_subsets=41384 balanced_arithmetic_orders=47
```

The graph-enumeration tests are finite and do not certify the infinite theorem; the proof above supplies the unrestricted argument.

## Relationship to prior work

Pseudoforest deletion is a long-established graph optimization problem. Hanaka and collaborators investigate deletion to bounded-orientability classes and pseudoforest-deletion complexity; Sheng establishes fixed-parameter algorithms for generalized pseudoforest deletion; Lokshtanov and collaborators establish an EPTAS for pseudoforest deletion on disk graphs. Those algorithmic and extremal results do not directly give the inclusion-maximal cardinality enumerator of a fixed complete multipartite graph, let alone the three-point spectrum and typical-size law on balanced tripartite graphs. The present result counts all minimal solutions of a different question, rather than reasserting that deletion is tractable.

The structural proof applies specifically to complete multipartite graphs and is not implied by a table of unlabeled pseudoforests, since the latter counts graphs rather than vertex subsets inside a fixed host graph. Potential earlier unindexed family-specific formulas remain a limitation of publication-priority claims.

## Limitations

The formulas assume at least three nonempty parts. The mathematical review and executable checks were performed without an independent mathematical audit. Finite enumeration through order twelve is a corroboration, not a general proof. The novelty comparison includes primary full-text material on related deletion algorithms, but cannot eliminate the possibility of obscure or differently indexed exact family enumerators; particularly, the complete 2018 journal treatment of generalized deletion was not materially inspected. No result for arbitrary host graphs or generalized \(\ell\)-pseudoforests is asserted.

## References

1. T. Hanaka, I. Katsikarelis, M. Lampis, Y. Otachi, F. Sikora, *Parameterized Orientable Deletion*, SWAT 2018, DOI:10.4230/LIPIcs.SWAT.2018.24; publicly available June 4, 2018. Related open text: https://arxiv.org/abs/1807.11518.
2. B. Sheng, *FPT algorithms for generalized feedback vertex set problems*, arXiv:1912.06966, publicly posted December 15, 2019. https://arxiv.org/abs/1912.06966.
3. D. Lokshtanov, F. Panolan, S. Saurabh, J. Xue, M. Zehavi, *A Framework for Approximation Schemes on Disk Graphs*, arXiv:2211.02717, publicly posted November 4, 2022. https://arxiv.org/abs/2211.02717.
4. G. Philip, A. Rai, S. Saurabh, *Generalized Pseudoforest Deletion: Algorithms and Uniform Kernel*, SIAM Journal on Discrete Mathematics 32 (2018), 882–901, DOI:10.1137/16M1100794. Abstract and bibliographic coverage consulted, not complete article.
5. OEIS A134964, unlabeled pseudoforests by number of vertices. https://oeis.org/A134964 (different counting problem).
