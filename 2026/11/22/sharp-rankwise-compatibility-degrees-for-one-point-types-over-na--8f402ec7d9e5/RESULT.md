# Sharp rankwise compatibility degrees for one-point types over named cycles

## Finding

In the countable homogeneous universal triangle-free graph \(H_3\), fix an induced cycle \(C_n\) with all its vertices individually named, where \(n\ge4\). A nonalgebraic complete singleton type is determined by its set \(S\) of named neighbors, which must be independent in \(C_n\). Let \(d(S)\) be the number of complete nonalgebraic singleton types \(T\) that can be realized together with \(S\) by **two distinct adjacent new vertices**. Unlike compatibility of positive formulas for one vertex, this asks that both full singleton types hold simultaneously for an adjacent pair.

For every \(1\le k\le\lfloor n/2\rfloor\), restrict to types with \(|S|=k\) and write \(r=n-2k\). With Fibonacci numbers \(F_0=0,F_1=1,F_{j+2}=F_{j+1}+F_j\), the sharp degree extrema are
\[
\begin{aligned}
 d_{\max}(n,k)&=2^{k-1}F_{n-2k+3},\\
 d_{\min}(n,k)&=\begin{cases}
 2^{k-r}3^r,&0\le r\le k,\\
 3^{k-1}F_{n-3k+4},&r>k.
 \end{cases}
\end{aligned}
\]
Every extremizer is classified by the cyclic gaps between successive members of \(S\): maximum gaps consist of \(k-1\) copies of \(2\) and one gap \(n-2k+2\); minimum gaps consist of \(k-r\) copies of \(2\) and \(r\) copies of \(3\) when \(r\le k\), and \(k-1\) copies of \(3\) and one gap \(n-3k+3\) when \(r>k\). A gap multiset denotes all cyclic placements and rotations of that multiset, not a preferred labeling.

The **numbers of pointwise-named types** attaining these extrema are exact:
\[
 N_{\max}(n,k)=\begin{cases}2,&n=2k,\\n,&n>2k,\end{cases}
\qquad
 N_{\min}(n,k)=\begin{cases}
 \frac{n}{k}\binom{k}{r},&0\le r\le k,\\n,&r>k.
\end{cases}
\]
For \(k=1\), both bounds equal \(F_{n+1}\), and all \(n\) types have the same degree. For \(k\ge2\), all degrees coincide for \(n=2k\) and \(n=2k+1\); the **first** degree variation is at \(n=2k+2\), where the only two degrees are \(9\cdot2^{k-2}\) and \(10\cdot2^{k-2}\), with multiplicities \(n(k-1)/2\) and \(n\), respectively. Degree variation persists for every larger permitted \(n\).

## Assumptions and scope

Graphs are simple, undirected and loopless. The old parameters are pointwise named and induce exactly \(C_n\), \(n\ge4\). New vertices are distinct from each other and from all parameters. The compatibility degree counts distinct complete singleton types for the *second* new vertex, not numbers of actual realizations in the countable graph, and the two new vertices are required to be adjacent. All independent old-neighbor sets of size \(k\) are included; no type at \(k=0\) is needed in the extremal theorem. The cyclic gap from an occupied vertex to the next occupied vertex is the number of **edges** traversed clockwise, so each gap is at least two, and the gaps sum to \(n\).

## Proof

**(1) Translation of adjacent extensions.** The age of \(H_3\) is the class of finite triangle-free graphs, and homogeneity/finite extension realize each allowed finite labelled diagram. A one-point old-neighbor set \(S\) is permitted exactly when \(S\) is independent. If two new vertices are adjacent and their old-neighbor sets are \(S,T\), the only additional possible triangles use their mutual edge and one old common neighbor. Thus the complete adjacent-pair diagram exists exactly when \(S\cap T=\varnothing\). Hence
\[
 d(S)=\#\{T\subseteq V(C_n)\setminus S:T\text{ is independent in }C_n\}=i(C_n-S),
\]
where \(i(G)\) counts independent vertex subsets, including the empty subset.

**(2) Exact cyclic-gap product.** Given \(S\ne\varnothing\), write its successive clockwise gaps as \(g_1,\ldots,g_k\), with \(g_i\ge2\) and \(\sum_i g_i=n\). Deleting \(S\) leaves the disjoint union of paths with \(g_i-1\) vertices. The recurrence \(i(P_m)=i(P_{m-1})+i(P_{m-2})\), with \(i(P_0)=1\), \(i(P_1)=2\), gives \(i(P_m)=F_{m+2}\). Thus
\[
 \boxed{d(S)=\prod_{i=1}^k F_{g_i+1}.}
\]
Conversely every ordered list of \(k\) integers at least two summing to \(n\) determines an independent \(k\)-set after choosing a starting vertex.

**(3) Three exact exchange identities.** For \(a,b\ge2\), Fibonacci addition gives
\[
 2F_{a+b-1}-F_{a+1}F_{b+1}=F_{a-2}F_{b-2}\ge0.
\]
It is strict exactly when \(a,b\ge3\). Replacing two gaps by \(2,a+b-2\) therefore strictly increases the product if both exceed two. Repeating proves that the maximum occurs exactly with all but at most one gap equal to two.

For \(a,b\ge3\), a second addition identity gives
\[
 F_{a+1}F_{b+1}-3F_{a+b-2}=F_{a-3}F_{b-3}\ge0,
\]
strict if both gaps exceed three. Replacing two gaps by \(3,a+b-3\) decreases the product in that case. Finally, for \(b\ge3\),
\[
 2F_{b+1}-3F_b=F_{b-3},
\]
strict when \(b\ge4\); replacing \(2,b\) by \(3,b-1\) decreases the product whenever \(b\ge4\). All replacements preserve the sum and the lower bound two. They terminate because, respectively, the numbers of gaps exceeding the target small value strictly decrease, or the sum of deviations from three strictly decreases. Consequently, a minimum with \(n<3k\) has only gaps two or three; a minimum with \(n\ge3k\) has no twos and at most one gap exceeding three. The gap classifications and displayed extreme products follow by fixing the sum.

**(4) Exact extremal multiplicities.** For any prescribed ordered cyclic gap list \((g_1,\ldots,g_k)\) and any starting old vertex, one obtains an independent \(k\)-set. Each set is counted exactly \(k\) times in all \(n\) starting choices. At the maximum, all gaps are two when \(n=2k\), giving \(n/k=2\) types; otherwise the exceptional large gap has \(k\) placements in the ordered gap word, giving \(n\) types. At the minimum for \(r\le k\), the ordered word contains \(r\) threes in \(\binom kr\) placements, giving \(n\binom kr/k\) types; when \(r>k\), there is one exceptional gap exceeding three, giving \(n\) types. These are exact labelled-set counts despite possible periodic gap words.

**(5) First nonuniform degree.** If \(n=2k\) or \(n=2k+1\), all feasible gap lists have the same multiset. At \(n=2k+2\), feasible gap lists have either two threes and the other gaps two, or one four and the others two. Their products are respectively \(9\cdot 2^{k-2}\) and \(10\cdot2^{k-2}\), and the preceding multiplicities give the stated counts. For any larger \(n\), at least two gap lists have at least two entries exceeding two, and the strict maximum exchange identity proves different degrees.

## Verification

The accompanying self-contained program `verify.py` independently enumerates every independent old-neighbor type and each disjoint independent compatible partner for every \(4\le n\le16\), rather than using the Fibonacci-gap formula for that direct count. It compares the resulting 5,754 nonempty types with the gap formula, and checks both extreme values and their exact multiplicities for all available \(k\). Separately it verifies all three Fibonacci exchange identities across 2,850 integer instances. See `verification_output.txt`. The exhaustive checks do not substitute for the unrestricted proof above.

## Relationship to prior work

The universal homogeneous triangle-free graph and its finite-extension criterion are classical; Conant's 2014 treatment of Henson graphs, especially its graph-theoretic finite-diagram formulation, provides the initiating model-theoretic setting. The general identity counting higher-arity Henson types by independent sets of Cartesian products, published in the indicated published-finding corpus result, implies the **unrefined** adjacent-pair count after summing over all first-neighbor types; it does not recover the fixed-rank compatibility-degree extrema or their multiplicities. The earlier cycle join-compatibility calculation concerns merging *positive requirements for one new vertex*, whereas this theorem concerns two different adjacent new vertices and enforces both complete types.

The Merrifield–Simmons index, the path Fibonacci recurrence, and two-factor Fibonacci product extremality are prior mathematics. De Ita Luna and collaborators (2024) study Fibonacci products and independent-set extrema when paths are joined to polygonal chains by cutting edges. Their studied families and invariants do not give the present simultaneous classification for every rank \(k\) of adjacent-pair type compatibility over a fixed old cycle, including the exact number of extremizers and sharp first nonuniformity. These prior ingredients are explicitly not claimed as new; the new object is the complete fixed-rank extremal compatibility profile.

## Limitations

The theorem applies to labelled singleton types over induced cycles in the triangle-free homogeneous graph. It does not treat arbitrary triangle-free old bases, weights, higher tuple arity, or the number of realizations of each type. It uses classical two-factor Fibonacci inequalities, so claims of novelty are for the all-rank exact extremal characterization and multiplicities, not for those identities. No independent mathematical audit or definitive historical-priority certification has been performed.

## References

1. G. Conant, "Forking and dividing in Henson graphs", first submitted 2014-01-08, arXiv:1401.1570. https://arxiv.org/abs/1401.1570
2. G. De Ita Luna, P. Bello López, M. Contreras González, J. R. Marcial Romero, "Extremal graphs for the number of independent sets on polygonal chains joined by cutting edges", *International Journal of Combinatorial Optimization Problems and Informatics* 15(2) (2024), 173–184. https://www.ijcopi.org/ojs/article/download/448/267/1490
3. "Higher-arity Henson type enumeration and exact-counting hardness", published mathematical finding (2026). https://github.com/published-finding corpus/2026/blob/main/2026/10/25/SCOPE-higher-arity-henson-type-enumeration-and-exact-counting-hardness--141a441755d6/RESULT.md
4. E. W. Weisstein, "Independence Polynomial", MathWorld, a compilation of standard independence-polynomial formulas. https://mathworld.wolfram.com/IndependencePolynomial.html
