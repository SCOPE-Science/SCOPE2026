# High-connectivity tails of inversion-graph enumerators via path–triangle complements

## Finding

For an integer \(n\ge4\) and a permutation \(\pi\in S_n\), let \(G_\pi\) denote the inversion graph on the \(n\) positions, where \(i<j\) are adjacent exactly when \(\pi(i)>\pi(j)\). Write \(\kappa(G)\) for ordinary vertex connectivity, with value zero for disconnected graphs, and let
\[
K_n(x)=\sum_{\pi\in S_n}x^{\kappa(G_\pi)}.
\]
The following conditions are equivalent:

1. \(\kappa(G_\pi)\ge n-3\).
2. The complementary graph \(\overline{G_\pi}\) is a disjoint union of paths (isolated vertices permitted) and triangles.
3. The value-complement permutation \(\widehat\pi(i)=n+1-\pi(i)\) decomposes as a direct sum whose indecomposable components are either path permutations (increasing oscillations, including components of sizes one and two) or the size-three decreasing permutation \(321\).

Let \(N(\pi)=\binom n2-\operatorname{inv}(\pi)\), the number of noninversions. For \(n\le3\), put every permutation into the initial class, and for all \(n\ge4\) use the equivalent conditions above. The complete noninversion-refined enumerator of these permutations is
\[
\boxed{\sum_{n\ge0}z^n\!\sum_{\pi:\,\kappa(G_\pi)\ge n-3}q^{N(\pi)}
=\frac{1}{1-z-qz^2-(2q^2+q^3)z^3-\dfrac{2q^3z^4}{1-qz}}.}
\]
The condition for \(n\le3\) in this display means precisely the declared all-permutation initial class, not a negative-connectivity convention.

Writing \(a_n=[z^n](1-z)/(1-2z-2z^3+z^4)\), and \(F_0=0,F_1=1\) for Fibonacci numbers, we obtain for all \(n\ge4\):
\[
\boxed{[x^{n-1}]K_n(x)=1,\qquad
[x^{n-2}]K_n(x)=F_{n+1}-1,\qquad
[x^{n-3}]K_n(x)=a_n-F_{n+1}.}
\]
For \(n=4,5,6,7,8\), the last coefficient equals \(8,21,55,135,323\), respectively. The all-order scalar counts \(a_n\) coincide with the shifted OEIS A180965 sequence and are **not claimed as a previously unknown numerical sequence**.

## Assumptions and scope

All graphs are finite and simple. An induced graph on a vertex set is used when deleting vertices; \(\kappa(K_n)=n-1\). A path of order one is an isolated vertex; the term triangle means the complete graph on three vertices. The variable \(q\) counts noninversions of the *original* permutation, equivalently edges of its complementary inversion graph. The theorem counts permutations, not graph isomorphism types, and makes no claim for connectivity layers below \(n-3\).

## Proof

**1. Four-vertex connectivity test.** For every graph \(G\) on \(n\ge4\) vertices, \(\kappa(G)\ge n-3\) if and only if every induced four-vertex subgraph is connected. Indeed, a disconnected induced subgraph on four vertices gives a vertex cut of size \(n-4\). Conversely, if a deletion of at most \(n-4\) vertices disconnects the remaining graph, which has at least four vertices, selecting four vertices from at least two of its connected components yields a disconnected induced four-vertex subgraph.

**2. Complement obstructions.** Put \(H=\overline G\). A four-vertex induced subgraph of \(G\) is disconnected if and only if, across some partition into two nonempty blocks, all cross-edges lie in \(H\). Such a partition has type \(1+3\) or \(2+2\). Consequently, the four-vertex condition is equivalent to \(H\) containing neither \(K_{1,3}\) nor \(K_{2,2}\) as a (not necessarily induced) subgraph. The first prohibition says \(\Delta(H)\le2\). Thus every connected component of \(H\) is a path or cycle. The second prohibition excludes a four-cycle. Inversion graphs have no induced cycles of length at least five (the standard permutation-graph fact explicitly used in Albert–Brignall–Ruškuc–Vatter, §9, page 27). As a graph with maximum degree two cannot contain a cycle with a chord, the only possible cyclic component is a triangle. This proves equivalence of (1) and (2) for a permutation inversion graph.

**3. Sum-indecomposable blocks.** Value-complementation sends inversions to noninversions, so \(H=G_{\widehat\pi}\). Connected components of the inversion graph correspond, in left-to-right order, to the unique direct-sum decomposition of its permutation. For a size-one component there is one permutation; for a size-two path there is one; for every size \(j\ge3\) path there are exactly two increasing oscillations (see the explicit constructions in the cited Albert papers). The only additional allowed connected component is the size-three triangle, represented uniquely by \(321\). Every path component on \(j\) vertices contributes \(j-1\) inversions of \(\widehat\pi\), and a triangle contributes three. The indecomposable-component series is therefore
\[
B(z,q)=z+qz^2+(2q^2+q^3)z^3+\sum_{j\ge4}2q^{j-1}z^j
=z+qz^2+(2q^2+q^3)z^3+\frac{2q^3z^4}{1-qz}.
\]
Unique ordered concatenation implies the enumerator is \(\sum_{r\ge0}B(z,q)^r=1/(1-B(z,q))\), with no quotient by graph automorphisms. This proves the bivariate formula.

**4. The top three connectivity coefficients.** At \(q=1\) we obtain \(1/(1-B(z,1))=(1-z)/(1-2z-2z^3+z^4)\). Next, \(\kappa(G)\ge n-2\) is equivalent to every three-vertex induced subgraph of \(G\) being connected. In its complement this is equivalent to maximum degree at most one, namely a matching plus isolated vertices. The corresponding direct-sum blocks have lengths one and two, each with one permutation, so their count is \([z^n](1-z-z^2)^{-1}=F_{n+1}\). Finally, \(\kappa(G)=n-1\) occurs only for \(G=K_n\), hence only for the decreasing permutation. Subtracting cumulative counts yields the three coefficient formulas.

## Verification

Run `python3 verify_inversion_connectivity.py` with the Python standard library. The checker independently builds every inversion graph for all permutations of orders \(4\) through \(8\); for orders at most seven it obtains exact vertex connectivity by exhaustive deletion of vertex subsets. At order eight it directly checks every four-vertex induced subgraph. It compares both sides of the path–triangle characterization, the scalar counts, the first three connectivity coefficients when exact connectivity is computed, and every coefficient of the independently constructed noninversion-refined polynomial. All checks returned `VERIFY_OK`. The infinite-range theorem follows from the four-vertex obstruction and sum-decomposition proof, not from finite testing.

## Relationship to prior work

Verkama, *Permutation patterns and higher connectivity in inversion graphs* (arXiv:2611.17237v1, §6), defines \(K_n(x)\) and tabulates its coefficients through order seven, without the all-order high-connectivity classification or noninversion-refined generating function. Albert–Brignall–Ruškuc–Vatter (§9 of arXiv:1602.00672) and Albert–Jelínek–Opler (arXiv:1912.07713, p. 8) establish the path-permutation and oscillation facts used as inputs, not the vertex-connectivity statement. OEIS A180965 gives, with an index shift, the same **unweighted sequence** \(a_n\), originally under tatami tilings and another permutation interpretation. The known scalar recurrence is acknowledged; no numerical-sequence novelty is asserted on that basis. Searches under complement graphs, path–triangle components, pattern avoidance, and the upper connectivity coefficients yielded no prior complete covering statement. This does not prove historical uniqueness.

## Limitations

The structural classification and generating-function formula apply at the threshold \(n-3\) for \(n\ge4\). They do not determine intermediate or low vertex-connectivity coefficients, nor do they give a direct bijection to tatami tilings. A matching numerical sequence is not automatically an equivalence of the underlying combinatorial objects. Possible unindexed equivalent enumerations or pattern-class identities remain a priority risk. No independent mathematical audit has been performed.

## References

- E. Verkama, *Permutation patterns and higher connectivity in inversion graphs*, arXiv:2611.17237v1 (first public 2026-11-12), §6 and Table 1. https://arxiv.org/html/2611.17237v1
- M. Albert, R. Brignall, N. Ruškuc and V. Vatter, *Rationality For Subclasses of 321-Avoiding Permutations*, arXiv:1602.00672, §9, p. 27. https://arxiv.org/pdf/1602.00672
- M. Albert, V. Jelínek and M. Opler, *Two examples of Wilf-collapse*, arXiv:1912.07713, p. 8, discussion of increasing oscillations. https://arxiv.org/pdf/1912.07713
- OEIS Foundation, A180965, *Number of tatami tilings of a 2 X n grid (with monomers allowed)*; sequence, formula, and 2013 permutation interpretation. https://oeis.org/A180965
