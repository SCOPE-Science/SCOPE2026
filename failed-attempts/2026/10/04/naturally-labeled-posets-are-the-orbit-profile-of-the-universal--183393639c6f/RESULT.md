# Naturally labeled posets are the orbit profile of the universal ordered poset
## Finding
Let \(U=(U,\prec,<)\) be the universal ordered poset, the Fraïssé limit of all finite posets equipped with a linear order extending the partial order, and let \(G=\operatorname{Aut}(U)\). Let \(s_n\) be OEIS A006455, the number of naturally labeled posets on \([n]\), equivalently partial orders \(\prec\) satisfying \(i\prec j\Rightarrow i<j\).

If \(a_n\) denotes the number of \(G\)-orbits on injective ordered \(n\)-tuples, then
\[
\boxed{a_n=n!\,s_n.}
\]
Equivalently,
\[
\boxed{a_n=\sum_{P\in\mathcal P_n} e(P),}
\]
where \(\mathcal P_n\) is the set of all labeled posets on \([n]\) and \(e(P)\) is the number of linear extensions of \(P\). Thus the injective orbit profile of this canonical homogeneous ordered structure is exactly the total linear-extension count over all labeled \(n\)-element posets.

The profile begins, from \(n=0\),
\[
1,\ 1,\ 4,\ 42,\ 960,\ 42840,\ 3473280,\ 485997120,\ 112915031040,\ldots.
\]

If \(b_n\) counts orbits on all ordered \(n\)-tuples, allowing repetitions, then equality patterns give the exact Stirling transform
\[
\boxed{b_n=\sum_{k=0}^{n}{n\brace k}\,k!\,s_k.}
\]
The first values are
\[
1,\ 1,\ 5,\ 55,\ 1241,\ 53551,\ 4182185,\ 565282495,\ 127493498921,\ldots.
\]

Finally, the classical Kleitman–Rothschild estimate for labeled posets implies
\[
\boxed{\lim_{n\to\infty}\frac{\log_2 a_n}{n^2}=\frac14.}
\]
Indeed, if \(p_n\) is the number of labeled \(n\)-element posets, then every poset has between one and \(n!\) linear extensions, so \(p_n\le a_n\le n!p_n\), and \(\log_2 p_n=n^2/4+o(n^2)\).

## Assumptions and scope
An ordered poset here means exactly a finite structure \((P,\prec,<)\) in which \((P,\prec)\) is a poset and \(<\) is a linear order extending \(\prec\), as in Kwiatkowska–Malicki. The universal ordered poset is the Fraïssé limit of this class. The claim concerns automorphism orbits of that limit, not conjugacy classes in its automorphism group.

The A006455 enumeration and the combinatorial identity connecting naturally labeled posets to total linear-extension counts are prior combinatorics. The contribution isolated here is their exact identification with the finite tuple-orbit profile of the universal ordered poset, together with the repeated-coordinate orbit transform and the resulting model-theoretic interpretation.

## Proof
Because \(U\) is ultrahomogeneous, two injective ordered tuples \((x_1,\ldots,x_n)\) and \((y_1,\ldots,y_n)\) lie in the same \(G\)-orbit exactly when the map \(x_i\mapsto y_i\) is an isomorphism between their induced finite ordered-poset structures. Therefore \(a_n\) is the number of ordered-poset structures on the labeled set \([n]\).

Choose first the linear order \(<\) on \([n]\). There are \(n!\) choices. Once \(<\) is chosen, relabel the points increasingly as \(1<\cdots<n\). The partial order \(\prec\) may then be any partial order contained in this linear order, and there are exactly \(s_n\) such relations. Hence \(a_n=n!s_n\).

The same objects can instead be counted by first choosing the labeled poset \(P\) and then choosing the distinguished linear extension \(<\), giving \(a_n=\sum_P e(P)\).

For an arbitrary ordered \(n\)-tuple, let its equality partition have \(k\) blocks. There are \({n\brace k}\) possible equality partitions. After canonically ordering the blocks by their least tuple position, the distinct values form an injective ordered \(k\)-tuple, contributing \(a_k\) orbit choices. Summing over \(k\) yields the Stirling transform.

## Verification
The companion verifier uses two independent finite enumerations. First, it enumerates every naturally labeled strict poset through six points by subsets of forward pairs and checks the A006455 row
\[
1,1,2,7,40,357,4824.
\]
Second, for each \(n\le5\), it independently enumerates every labeled poset by ternary pair orientations, counts all of its linear extensions by brute-force permutations, and verifies that the total equals \(n!s_n\). The labeled-poset counts recovered in this process are
\[
1,1,3,19,219,4231.
\]
It also computes the injective and all-tuple profiles and independently enumerates set partitions by restricted-growth strings to check the Stirling transform. The replay terminates with `VERIFY_OK`.

## Relationship to prior work
Kwiatkowska and Malicki define the universal ordered poset as the Fraïssé limit of all finite ordered posets and study large conjugacy classes of its automorphism group. Their full text does not state a finite tuple-orbit profile, and searches in that text found no occurrence of “profile,” “naturally labeled,” or “linear extension.”

OEIS A006455 is the classical sequence of naturally labeled posets, also described as upper-triangular Boolean idempotent matrices with diagonal ones. Its record also notes the prior identity that \(n!s_n/p_n\) is the average number of linear extensions of a labeled \(n\)-element poset. Bevan, Cheon, and Kitaev study naturally labelled posets and several avoidance subclasses. Brightwell, Prömel, and Steger study the average number of linear extensions and the number of suborders of a linear order.

The closest semantic-index result located for automorphism groups gives exact tuple-orbit profiles for reduct groups of the random poset. That result counts labeled posets themselves in the unreduced random-poset case, whereas the present ordered expansion counts a poset together with a chosen linear extension. Targeted searches for the universal ordered poset together with A006455, naturally labeled posets, linear extensions, orbit profiles, and oligomorphic profiles did not locate this identification.

## Limitations
The main formula is a short consequence of ultrahomogeneity plus a classical enumeration, so unindexed folklore priority remains a real possibility. No claim is made that A006455 or the total-linear-extension identity is new. The verification is exhaustive only in small arities and does not re-prove the classical asymptotic enumeration of finite posets.

## References
1. A. Kwiatkowska and M. Malicki, “Ordered structures and large conjugacy classes,” *Journal of Algebra* 557 (2020), 67–96. arXiv:1903.00936; DOI: 10.1016/j.jalgebra.2020.03.021.
2. OEIS Foundation, A006455, “Number of partial orders on \(\{1,2,\ldots,n\}\) that are contained in the usual linear order.”
3. D. Bevan, G.-S. Cheon, and S. Kitaev, “On naturally labelled posets and permutations avoiding 12-34,” arXiv:2311.08023.
4. G. Brightwell, H. J. Prömel, and A. Steger, “The average number of linear extensions of a partial order,” *Journal of Combinatorial Theory, Series A* 73 (1996), 193–206. DOI: 10.1016/S0097-3165(96)80001-X.
5. D. J. Kleitman and B. L. Rothschild, “Asymptotic enumeration of partial orders on a finite set,” *Transactions of the American Mathematical Society* 205 (1975), 205–220. DOI: 10.2307/1997200.
