# Reachability cuts classify maximal commuting families in finite acyclic path semigroups

## Finding
Let \(Q\) be any finite, loopless, directed **acyclic multiquiver** with a nonempty vertex set \(V\) of size \(n\). Distinct parallel arrows and different walks with the same endpoints are retained as different paths. In the zero path semigroup \(P(Q)\), every inclusion-maximal commutative subsemigroup is uniquely one of the following:

1. \(D=\{0\}\cup\{e_v:v\in V\}\), where \(e_v\) is the stationary path at vertex \(v\).
2. \(M(S,T)=\{0\}\cup\{e_v:v\notin S\cup T\}\cup\{p:s(p)\in S,\ t(p)\in T,\ |p|\ge1\}\), where \(S,T\subseteq V\) are nonempty and disjoint, **each** vertex of \(S\) has a directed path to some vertex of \(T\), and **each** vertex of \(T\) has a directed path from some vertex of \(S\).

The parameters \(S,T\) are uniquely recoverable as the source and target vertex sets of the nonstationary elements of the family. In particular, this classification depends only on the reachability relation of \(Q\), although family cardinalities depend on path multiplicities.

Define \(m_{uv}\) as the number of paths from \(u\) to \(v\), including the one stationary path when \(u=v\), and put \(L=\sum_{u,v}m_{uv}\). The complete cardinality-generating polynomial is
\[
F_Q(z)=z^{n+1}+\sum_{(S,T)\text{ admissible}}z^{1+n-|S|-|T|+\sum_{s\in S,t\in T}m_{st}}.
\]
The first term is \(D\), and each ordered cut occurs once. Thus the total number is \(F_Q(1)\), independent of parallel-edge multiplicities as long as reachability is unchanged.

For a positive path \(p:u\to v\), the number of its commuting partners in \(P(Q)\), including itself and zero, is
\[
|C(p)|=L-a_u-b_v+1,\quad a_u=\sum_xm_{xu},\quad b_v=\sum_ym_{vy}.
\]
For stationary \(e_v\), \(|C(e_v)|=L-a_v-b_v+3\). For zero, \(|C(0)|=L+1\). Summing these expressions gives all ordered commuting pairs, and in particular for the directed line \(L_n:1\to2\to\cdots\to n\),
\[
F_{L_n}(1)=1+\frac{3^n-2n-1}{4},\qquad
\max_M|M|=\max\{n+1,1+\lfloor n^2/4\rfloor\},
\]
\[
K(L_n)=\frac{(n+2)(3n^3-4n^2+11n+6)}{12}.
\]
All formulas hold for \(n\ge1\), including isolated vertices.

## Assumptions and scope
\(P(Q)\) is the **semigroup with absorbing zero** whose nonzero elements are **all** finite directed paths of \(Q\) and whose product is path concatenation if terminal and initial vertices coincide, or zero otherwise. This differs from the partial-path semigroup where an undefined product is not an element. A stationary path \(e_v\) has length zero, start and end \(v\), and satisfies \(e_v^2=e_v\). As \(Q\) is finite and acyclic, there are finitely many paths, and each nonstationary path has distinct endpoints. Maximality is **inclusion-maximal commutativity in the fixed semigroup**, not maximum cardinality. The centralizer includes zero. A directed cut is admissible only when the complete source and target sets are supported by at least one positive path per vertex, not merely when some edge crosses the cut.

## Proof
**Commutation obstruction.** Let \(p\) and \(q\) be nonstationary paths. If \(t(p)=s(q)\), then \(pq\ne0\). The reverse product \(qp\) is zero, since \(qp\ne0\) would imply a directed cycle (indeed two positive composable paths closing the endpoints). Hence \(p,q\) do not commute. Conversely, if \(t(p)\ne s(q)\) and \(t(q)\ne s(p)\), both products are zero and they commute. For a stationary path \(e_v\), its products with any nonstationary \(p\) are unequal exactly when \(v\) is an endpoint of \(p\); for another stationary path they commute. Zero commutes with everything.

**Classification.** In an inclusion-maximal commutative subsemigroup \(M\), zero must occur because adjoining zero preserves closure and commutativity. If no nonstationary path occurs, every stationary path must occur, giving \(D\). Otherwise define \(S\) and \(T\) to be respectively the sources and targets of the nonstationary paths of \(M\). If a vertex lay in both \(S\) and \(T\), there would be a nonstationary path ending there and another beginning there, a noncommuting pair. Thus \(S\cap T=\varnothing\). No stationary \(e_v\) with \(v\in S\cup T\) may belong to \(M\), whereas every other stationary \(e_v\) must belong to \(M\): it commutes with all of \(M\), its multiplication with members is zero except for its own square, and adjoining it preserves closure.

Every positive-length path \(p\) with \(s(p)\in S\) and \(t(p)\in T\) commutes with everything in \(M\); its products with all nonstationary members vanish (their sources lie in \(S\), their targets lie in \(T\)), and it is disjoint from every retained stationary path. Adding it preserves closure, so maximality forces its presence. Conversely, no other nonstationary path can be added: a path whose source or target is outside \(S\cup T\) conflicts with the stationary path at that endpoint; among paths with both endpoints in \(S\cup T\), only paths directed from \(S\) to \(T\) can avoid conflict with the existing sources and targets (acyclicity excludes same-set cycles and diagonal nontrivial paths). Explicitly, a new path beginning in \(T\) conflicts with any existing path ending there, and a path ending in \(S\) conflicts with an existing path beginning there. Each source and target was defined from an existing path, proving the per-vertex admissibility condition. Conversely, for any admissible cut, the constructed \(M(S,T)\) is commutative and closed, and the same endpoint obstruction rules out every omitted path or stationary idempotent. It is maximal. Uniqueness follows from reconstructing \(S,T\).

**Counting.** An admissible ordered cut contributes exactly \(1+n-|S|-|T|+\sum_{s\in S,t\in T}m_{st}\) elements: zero, the stationary paths outside the cut, and all directed paths across it; stationary contributions do not occur between disjoint sets. This proves the polynomial. The existence of a directed path, not its count, determines admissibility.

**Centralizers.** Of the \(L+1\) semigroup elements, the noncommuting partners of \(e_v\) are precisely the nonstationary paths starting or ending at \(v\), numbering \(b_v-1+a_v-1\); hence \(|C(e_v)|=L+1-(a_v+b_v-2)=L-a_v-b_v+3\). For a nonstationary path \(p:u\to v\), noncommuting partners comprise all paths ending at \(u\) (\(a_u\) choices), and all paths starting at \(v\) (\(b_v\) choices). These are disjoint because a path from \(v\) to \(u\) would close a directed cycle with \(p\). Thus \(|C(p)|=L+1-a_u-b_v\). Zero commutes with all \(L+1\) elements.

**Directed line specialization.** For vertices labeled \(1,\ldots,n\), an admissible cut corresponds exactly to a word in three symbols \(S,T,D\) whose first non-\(D\) symbol is \(S\) and last non-\(D\) symbol is \(T\). Indeed the first condition is \(\max S<\max T\) and the second is \(\min S<\min T\). Reversing a word exchanges the two strict inequalities symmetrically, and direct enumeration by its first and last non-\(D\) positions yields
\[
\sum_{1\le i<j\le n}3^{j-i-1}=\frac{3^n-2n-1}{4}.
\]
For any such cut the nonstationary path count is the number of ordered pairs \((s,t)\in S\times T\) with \(s<t\), at most \(\lfloor(|S|+|T|)^2/4\rfloor\); including the stationary paths gives the upper bound \(1+(n-|S|-|T|)+\lfloor(|S|+|T|)^2/4\rfloor\). This is at most \(\max\{n+1,1+\lfloor n^2/4\rfloor\}\), attained by \(D\) and respectively by a balanced initial-source/final-target cut. The centralizer formulas give \(a_i=i\), \(b_j=n-j+1\) and \(L=n(n+1)/2\). Summing all centralizers, with zero, then simplifying the elementary sums over \(1\le i<j\le n\), gives the displayed cubic-times-linear formula for \(K(L_n)\).

## Verification
The standalone script `verify_path_semigroups.py` independently enumerates **every** directed path of each finite test multiquiver, explicitly computes concatenation, enumerates all commuting subsets, filters inclusion-maximal ones, and compares them to the cut classification and every individual centralizer formula. It checks all 75 simple DAGs on 1–4 labeled ordered vertices, four additional DAG/multiquiver examples, and the directed-line count and maximum-size expressions for \(1\le n\le6\). Run `python3 verify_path_semigroups.py` using Python 3.9+. It prints `PASS: 79 DAG instances; all maximal families and individual centralizers`. These finite checks corroborate but do not replace the preceding proof for all finite acyclic multiquivers.

## Relationship to prior work
Mazorchuk and Steinberg (2011), §8.1, explicitly define finite acyclic path semigroups and prove an effective-dimension theorem; that theorem does **not** provide commuting-family or centralizer classifications. Ma and March (2009), §2, characterize the triangular matrix-unit semigroups obtained from directed lines and suitable group-labeled variants, but do **not** count their maximal commutative subsemigroups. General maximal-commutative classifications for complete Brandt semigroups involve all source-target rectangles. Their unrestricted rectangular structure is related to the endpoint obstruction above, but it does not by itself provide the reachability-admissibility and path-multiplicity enumeration on arbitrary acyclic quivers, especially for distinct paths with identical endpoints. The exact source-to-target cut formula and its line specialization are the assertions assessed here.

## Limitations
The quiver is required to be finite and acyclic; cycles can create nonzero commuting products and invalidate the classification, and may produce infinite path semigroups. The theorem counts **embedded labeled** maximal commutative subsemigroups, not isomorphism classes under quiver automorphisms. The cited literature comparison is not an exhaustive proof of priority; an earlier equivalent enumeration in monomial semigroup theory could exist. The checker tests finitely many examples, not every finite quiver.

## References
- V. Mazorchuk and B. Steinberg, *Effective dimension of finite semigroups*, preprint first publicly posted 7 July 2011, arXiv:1107.1413, §8.1. https://arxiv.org/abs/1107.1413
- J. Ma and E. March, *Lattice-ordered triangular matrix algebras*, Journal of Algebra 321 (2009), 3659–3667; online 8 April 2009, doi:10.1016/j.jalgebra.2009.02.028, especially §2. https://doi.org/10.1016/j.jalgebra.2009.02.028
