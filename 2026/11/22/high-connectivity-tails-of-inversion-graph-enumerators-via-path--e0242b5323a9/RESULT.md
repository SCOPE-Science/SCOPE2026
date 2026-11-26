# High-connectivity tails of inversion-graph enumerators via path–triangle complements

## Finding

For a permutation \(\pi\in S_n\), let \(G_\pi\) be its inversion graph on positions, with \(i<j\) adjacent when \(\pi(i)>\pi(j)\), and set \(K_n(x)=\sum_{\pi\in S_n}x^{\kappa(G_\pi)}\), where \(\kappa\) denotes ordinary vertex connectivity. For \(n\ge4\), the following conditions are equivalent:

1. \(\kappa(G_\pi)\ge n-3\).
2. \(\overline{G_\pi}\) is a disjoint union of paths (allowing isolated vertices) and triangles.
3. The value complement \(\widehat\pi(i)=n+1-\pi(i)\) is a direct sum of increasing oscillations (including path blocks of sizes one and two) and copies of the triangle permutation \(321\).
4. \(\widehat\pi\) satisfies \(|\widehat\pi(i)-i|\le2\) for all \(i\) and avoids \(3412\).

Condition 4 is the permutation class already described in the comments of OEIS A180965 (with its index shifted by one). The unweighted sequence and that permutation interpretation are not claimed as new. The result connects that class to high vertex connectivity and gives a noninversion refinement in the original permutation. Write \(N(\pi)=\binom{n}{2}-\operatorname{inv}(\pi)\). Including every permutation for orders \(0\) through \(3\), the refined series is
\[
\sum_{n\ge0}z^n\sum_{\pi:\,\kappa(G_\pi)\ge n-3}q^{N(\pi)}
=\frac{1}{1-z-qz^2-(2q^2+q^3)z^3-2q^3z^4/(1-qz)}.
\]
The condition in this series for orders \(0\) through \(3\) is the declared initial class. For \(n\ge4\), putting \(a_n=[z^n](1-z)/(1-2z-2z^3+z^4)\), the top three coefficients are
\[
[x^{n-1}]K_n(x)=1,\qquad [x^{n-2}]K_n(x)=F_{n+1}-1,\qquad [x^{n-3}]K_n(x)=a_n-F_{n+1},
\]
where \(F_0=0,F_1=1\). For \(n=4,5,6,7,8\) the last coefficient is \(8,21,55,135,323\), respectively; the values through order seven occur in Verkama's table.

## Assumptions and scope

Graphs are finite and simple, with \(\kappa(K_n)=n-1\) and \(\kappa=0\) for disconnected graphs. This counts permutations, not isomorphism types of graphs. The variable \(q\) counts edges of the complementary inversion graph, and no classification for lower connectivity layers is claimed.

## Proof

**Four-vertex test.** For \(n\ge4\), a disconnected induced subgraph on four vertices exhibits a cut of size \(n-4\). Conversely a deletion of at most \(n-4\) vertices leaving a disconnected graph leaves at least four vertices; choose four of them meeting at least two components. Hence \(\kappa(G)\ge n-3\) holds exactly when every four-vertex induced subgraph is connected.

**Complement obstructions.** A disconnected induced subgraph on four vertices gives a partition of type \(1+3\) or \(2+2\) with all cross-edges in the complement. Thus the test excludes \(K_{1,3}\) and \(K_{2,2}\) as not necessarily induced subgraphs of \(\overline G\). The first exclusion implies maximum degree two, so all components are paths or cycles; the second excludes four-cycles. Now \(\overline{G_\pi}=G_{\widehat\pi}\). An inversion graph has no induced cycles of length at least five by [2]. Every cycle in a graph of maximum degree two is induced, so only triangles remain. The converse is immediate from the same obstructions. This proves 1–2.

**Direct sums and weights.** The components of an inversion graph are the blocks of its permutation's unique direct-sum decomposition; if an index between endpoints of an inversion belonged to another component, its value would have to be larger than the left value and smaller than the right value, which is impossible. Hence connected components occupy consecutive positions, with no cross inversions. By [2, 3], path components have one representative at each size one and two, and two increasing oscillations at every size at least three. A triangle has representative \(321\). A path of order \(j\) has \(j-1\) edges, and a triangle has three, so the series for the allowed components of \(\widehat\pi\) is
\[
B(z,q)=z+qz^2+(2q^2+q^3)z^3+\sum_{j\ge4}2q^{j-1}z^j.
\]
Ordered sequences of these blocks have series \(1/(1-B(z,q))\), including the empty sequence. This proves 2–3 and the weighted formula since \(\operatorname{inv}(\widehat\pi)=N(\pi)\). At orders at most three all permutations satisfy condition 2.

**Exact class overlap with A180965.** For a permutation \(\sigma\), let \(l_i\) count larger values strictly to the left of \(i\), and \(r_i\) smaller values strictly to the right. The degree is \(l_i+r_i\), and counting smaller values gives \(\sigma(i)-i=r_i-l_i\). Thus maximum degree at most two implies displacement at most two. Conversely, under the displacement bound, if \(l_i,r_i\) are both positive, a larger value to the left is at most \(i+1\) and a smaller value to the right is at least \(i-1\); consequently \(\sigma(i)=i\). The only possible left and right locations of these inversions are then \(i-1\) and \(i+1\), respectively. If just one side contributes, the degree is the absolute displacement. In all cases the degree is at most two.

The only four-point permutation whose inversion graph is a four-cycle is \(3412\): its first value must be 3 by degree two, the value 4 must be second to have two later smaller values, and the last two entries must be increasing. Thus under the degree bound avoidance of \(3412\) is exactly the absence of a four-cycle. This proves 2–4, using again the absence of longer induced cycles. Moreover, if \(a<b<c<d\) occur in the order \(c,d,a,b\) at positions \(i_1<i_2<i_3<i_4\), the displacement bound implies \(c\le i_1+2\) and \(b\ge i_4-2\). Since \(c>b\), one has \(i_4-i_1\le3\), forcing contiguous positions and the four consecutive values from \(i_1\) to \(i_1+3\) by the same bound. This also explains the description in [4] as swapping two consecutive pairs. Accordingly the unweighted A180965 overlap is class-level, not inferred from numerical equality.

**Connectivity coefficients.** At \(q=1\) the formula reduces to \((1-z)/(1-2z-2z^3+z^4)\). The same deletion argument with three vertices instead of four shows that \(\kappa(G)\ge n-2\) is equivalent to the complement having maximum degree one, since a disconnected triple yields a vertex with two complement neighbors and conversely. The complementary permutation is then a direct sum of singleton and size-two path blocks, with count \([z^n](1-z-z^2)^{-1}=F_{n+1}\). Only the decreasing permutation has the complete graph. Taking differences of the cumulative counts proves the three formulas.

## Verification

The supplied standard-library script `verify_inversion_connectivity.py` compares the path–triangle condition with connectivity by exhaustive vertex deletion through order seven and with the four-vertex test at order eight. It also checks the noninversion-refined coefficient counts. These finite tests supplement, not replace, the all-order proofs, including the displacement-pattern identification above.

## Relationship to prior work and limitations

Verkama [1, §6 and Table 1] defines \(K_n(x)\) and tabulates it through order seven. The path-oscillation classification and prohibition of longer induced cycles are known [2, 3]. Morales's 2013 interpretation in [4] gives the exact same unweighted complementary permutation class in displacement-pattern language, and [4] gives the shifted scalar generating function. The contribution here is the relation of this class to the high-connectivity tail and its noninversion-refined enumeration. There is no claim of a new unweighted permutation class, a new sequence, or a direct bijection to tatami tilings. Bounded prior-source comparisons do not establish publication priority.

## References

1. E. Verkama, *Permutation patterns and higher connectivity in inversion graphs*, arXiv:2611.17237v1, §6 and Table 1. https://arxiv.org/html/2611.17237v1
2. M. Albert, R. Brignall, N. Ruškuc and V. Vatter, *Rationality for subclasses of 321-avoiding permutations*, arXiv:1602.00672, §9. https://arxiv.org/pdf/1602.00672
3. M. Albert, V. Jelínek and M. Opler, *Two examples of Wilf-collapse*, arXiv:1912.07713, discussion of increasing oscillations. https://arxiv.org/pdf/1912.07713
4. OEIS Foundation, A180965, *Number of tatami tilings of a 2 X n grid (with monomers allowed)*, COMMENTS (Jean M. Morales, June 2, 2013) and FORMULA. https://oeis.org/A180965
