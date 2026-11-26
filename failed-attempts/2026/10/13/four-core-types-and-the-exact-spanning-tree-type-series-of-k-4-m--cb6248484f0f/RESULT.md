# Four core types and the exact spanning-tree-type series of \(K_{4,m}\)

## Finding

For every integer \(m\ge 5\), let \(I_{4,m}\) count unrooted, unlabelled abstract tree isomorphism types occurring as spanning trees of the complete bipartite graph \(K_{4,m}\). Write \(F(z)\) for the formal rational series

\[
\begin{aligned}
F(z)={}&\frac{z}{(1-z)(1-z^2)(1-z^3)(1-z^4)}\\
&+\frac{z^2}{2}\left(\frac{1}{(1-z)^4}+\frac{1}{(1-z)^2(1-z^2)}\right)\\
&+\frac{z^3}{(1-z)^2(1-z^2)(1-z^3)}\\
&+\frac{z^3}{2}\left(\frac{1}{(1-z)^4}+\frac{1}{(1-z^2)^2}\right).
\end{aligned}
\]

Then \(I_{4,m}=[z^m]F(z)\) for every \(m\ge5\), or equivalently

\[
\sum_{m\ge5}I_{4,m}z^m=F(z)-z-2z^2-7z^3-14z^4.
\]

The rational function also simplifies to

\[
F(z)=\frac{z(1+z+4z^2+5z^3+7z^4+5z^5+4z^6+z^7+z^8)}{(1-z)^4(1+z)^2(1+z^2)(1+z+z^2)}.
\]

For \(m=5,6,7,8,9,10\), the exact numbers are \(28,45,73,105,152,204\). The sequence is eventually quasipolynomial of degree three and period dividing twelve, with \(I_{4,m}=\frac{29}{144}m^3+O(m^2)\). More strongly, each tree type is uniquely obtained from one of four explicitly classified cores by attaching leaves to four hub vertices, modulo the core automorphism group.

## Assumptions and scope

Graphs are finite, simple and undirected. A spanning tree of \(K_{4,m}\) has the full \(4+m\) vertex set and exactly \(m+3\) edges, and two spanning trees count as the same type when they are isomorphic as **uncoloured, unrooted trees**, regardless of their vertex labels or their embeddings. Since \(m\ge5\), the bipartition classes of sizes \(4\) and \(m\) are distinguished under every tree isomorphism. Denote the four vertices in the small class by **hubs**. All series identities are identities of formal power series over the rationals. The coefficients of \(F\) at powers less than five are only formal core counts; no assertion about \(I_{4,m}\) is made there.

## Proof

**1. Core reduction.** Let \(T\) be any spanning tree and let \(B\) denote its class of size \(m\). Since \(T\) has \(m+3\) edges,

\[
\sum_{v\in B}(\deg_T(v)-1)=(m+3)-m=3.
\]

Exactly \(k\in\{1,2,3\}\) vertices of \(B\) therefore have degree at least two. Delete all degree-one vertices of \(B\), retaining every hub. The remaining graph, called the core, is a connected tree: a deleted pendant vertex cannot disconnect two surviving vertices, and each hub has an incident core edge because it must connect to the other hubs. It has four hubs and \(k\) degree-at-least-two vertices of \(B\). Every deleted vertex is attached to exactly one hub.

**2. Exactly four core types.** If \(k=1\), the sole nonleaf \(B\)-vertex has degree four, so the core is a four-armed subdividing-center star with a \(B\)-center (type A). If \(k=2\), the \(B\)-degrees are \(3,2\); the two nonleaf vertices must share precisely one hub to give a connected five-edge tree, and the degree-three vertex meets two additional hubs while the degree-two vertex meets the last hub (type B). If \(k=3\), every surviving \(B\)-vertex has degree two; suppressing all three produces an ordinary three-edge tree on the four hubs. Up to isomorphism it is either the star \(K_{1,3}\) (type C) or the path \(P_4\) (type D), with each edge subdivided exactly once. The four cases are disjoint by \(k\), and within \(k=3\) by the suppressed hub tree.

**3. Automorphism orbits.** The four respective actions on the hubs are \(S_4\), \(C_2\) (swapping the two degree-one branches of the degree-three nonleaf vertex), \(S_3\) (permuting the leaves of the suppressed star), and \(C_2\) (reversing the suppressed path). In type B, the degree-three and degree-two nonleaf vertices have different degrees, so no additional exchange is allowed. Each tree of core type \(j\) arises by attaching nonnegative numbers \((x_1,x_2,x_3,x_4)\) of new leaves to the four hubs, with \(x_1+x_2+x_3+x_4=m-k\). Since \(m>4\), every isomorphism preserves the smaller shore, the nonleaf vertices of the larger shore, and hence the core. Two such vectors yield isomorphic trees **if and only if** they lie in the same automorphism-group orbit; conversely all vectors produce a valid spanning tree.

**4. Burnside counts.** In type A, unordered four-tuples give \(z/\prod_{j=1}^{4}(1-z^j)\). In type B, the identity has fixed-vector series \((1-z)^{-4}\), and the one nontrivial permutation fixes series \((1-z)^{-2}(1-z^2)^{-1}\); applying Burnside and multiplying by \(z^2\) gives the second term of \(F\). In type C, the central hub has unrestricted leaves while the other three hubs form an unordered triple; this gives \(z^3/((1-z)^2(1-z^2)(1-z^3))\). In type D, the identity fixes \((1-z)^{-4}\), whereas path reversal fixes \((1-z^2)^{-2}\); Burnside gives the final term. Thus every tree is counted once and the displayed generating function follows exactly. The coefficients at degrees one to four are \(1,2,7,14\), giving the restricted series identity. Ordinary rational-function algebra yields the simplified form.

**5. Degree and leading coefficient.** All poles of \(F\) are at roots of unity of orders dividing twelve. The pole at \(z=1\) has order four, and its coefficient from the four types is \(1/24+1/2+1/6+1/2=29/24\) times \((1-z)^{-4}\); the resulting leading term is \((29/24)/3!=29/144\). Other poles have lower order, so \(I_{4,m}=29m^3/144+O(m^2)\). Root-of-unity partial fractions give the stated eventual quasipolynomiality and period bound.

## Verification

Run `python3 verify_k4_tree_types.py` with Python 3 and its standard library. The program enumerates **every** pair of bipartite Prüfer words for \(K_{4,5}\) and \(K_{4,6}\): respectively \(4^4 5^3=32{,}000\) and \(4^5 6^3=221{,}184\) labelled spanning trees. It decodes these words independently, canonicalizes each unrooted tree by its center decomposition, and finds exactly \(28\) and \(45\) abstract types. It also constructs all four families from explicit small cores and verifies disjointness and equality with the independently generated type sets. A separate formal-power-series convolution checks the four Burnside summands against the orbit formulas through degree forty. Expected recorded output is in `verify_k4_tree_types.out`. These finite computations check arithmetic and finite cases; the proof above establishes the statement for every integer \(m\ge5\).

## Relationship to prior work

Johnson and Nochumson [1] study precisely the number of non-isomorphic spanning-tree types of complete bipartite graphs and obtain general partition-based lower and upper bounds, but not an exact series for \(K_{4,m}\). Yan and Zhang [2, §5.1] give the bounded-core construction and the asymptotic leading constant for \(K_{d,n-d}\). Specializing their coefficient to four hubs yields \(29/144\), already known and not a new claim. Their argument discards repeated leaf multiplicities into an error term; it does not calculate the exact automorphism orbits. The new statement is the four-core isomorphism classification and its all-order exact Burnside series. General Pólya-type enumerations of bicoloured unlabelled trees may provide an alternative derivation, but no identical specialized expression was located in the inspected sources. Earlier work on equicolourable trees [3] concerns equal part sizes and does not cover the unequal shores here.

## Limitations

The theorem addresses only the shore sizes \((4,m)\) with \(m\ge5\), not the balanced case \(K_{4,4}\), arbitrary \(K_{d,m}\), or additional restrictions on spanning-tree degree sequences. It counts abstract types, **not** labelled spanning trees, which have the separately known count \(4^{m-1}m^3\). No independence or external validation is claimed. A general bicoloured-tree enumeration in uninspected literature could conceivably subsume this specialization.

## References

1. P. Johnson and S. Nochumson, *Counting Isomorphism Classes of Spanning Trees of Complete Bipartite Graphs*, arXiv:2602.06867, first public 2026-02-06. https://arxiv.org/html/2602.06867v2
2. Z. Yan and L.-M. Zhang, *An extremal theorem for non-isomorphic spanning trees*, arXiv:2609.30201v1, first public 2026-09-24, particularly Proposition 5.1 and §5.1. https://arxiv.org/html/2609.30201v1
3. N. Pippenger, *Enumeration of Equicolourable Trees*, SIAM J. Discrete Math. **14** (2001), 93–111, DOI:10.1137/S0895480100368463 (comparison by the public abstract).
