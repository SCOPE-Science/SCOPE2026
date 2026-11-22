# Extremal nilpotence forces two-step translations in parity-preserving fence inverse monoids

## Finding
For each integer \(n\ge3\), let \(M_n=IOF_n^{\mathrm{par}}\) be the inverse monoid of parity-preserving, strictly order-preserving, two-sided fence-preserving partial injections of the chain \([n]=\{1,\ldots,n\}\), including the empty map \(0\). For a nilpotent \(f\in M_n\), set \(\nu(f)=\min\{j\ge1:f^j=0\}\), and let
\[
E_n(z)=\sum_{\substack{f\in M_n\text{ nilpotent}\\ \nu(f)=\lceil n/2\rceil}}z^{|\operatorname{Dom}(f)|}.
\]
Then the sharp maximal index is
\[
\boxed{\max_{f\in M_n\text{ nilpotent}}\nu(f)=\lceil n/2\rceil},
\]
and its complete domain-rank spectrum is
\[
\boxed{E_{2m+1}(z)=2z^m(1+z)^{m-1}\quad(m\ge1),}
\]
\[
\boxed{E_{2m}(z)=4z^{m-1}(1+z)^{m-1}-2z^{2m-2}\quad(m\ge2).}
\]
Consequently, the number of maximum-index nilpotent maps is \(2^m\) for odd size \(2m+1\), and \(2^{m+1}-2\) for even size \(2m\).

More precisely, **every** maximum-index element is a restriction of one of the two partial translations \(\tau_{+}(x)=x+2\) and \(\tau_{-}(x)=x-2\). For each direction and each parity class having the maximum possible cardinality \(\lceil n/2\rceil\), all its points except the last in that direction must be in the domain. Every remaining available point of the opposite parity can independently be included or omitted. For even \(n\), the two parity choices for one direction share exactly one map, the complete two-step translation on its available domain; different directions never coincide in a nonempty map. Thus the maximum-index locus is assembled from Boolean cubes, with a one-vertex intersection of the two cubes per direction in even size.

## Assumptions and scope
The alternating fence is \(1\prec2\succ3\prec4\succ\cdots\), a poset of height two. Thus distinct elements are comparable in the fence exactly when they are adjacent integers. A partial injection is strictly chain-order-preserving when \(a<b\) among its domain elements implies \(f(a)<f(b)\); it preserves parity when \(f(a)\equiv a\pmod 2\). Both \(f\) and its partial inverse preserve the fence order. Equivalently, for consecutive elements of its increasing domain, a gap of one is mapped to a gap of one, and the two gaps have the same parity (Sareeto–Koppitz, Proposition 1 [1]). This is the usual monoid \(IOF_n^{\mathrm{par}}\), not the much larger monoid of all increasing partial injections. Composition is ordinary partial-function composition; \(0\) is the empty map. Domain rank is the number of source points, not the minimum number of monoid generators.

For \(n=1,2\), every nilpotent element is \(0\), with index one; the enumerating formulas above are stated only for \(n\ge3\).

## Proof
**1. Orbit monotonicity and index bound.** A partial injection on a finite set has a directed functional graph consisting of vertex-disjoint cycles and directed paths (isolated vertices allowed). It is nilpotent exactly when it has no directed cycle. Fix a nontrivial orbit \(x,f(x),\ldots,f^k(x)\) of a strictly increasing partial map. If \(x<f(x)\) then applying strict order preservation to the two domain points \(x,f(x)\), whenever the second iterate exists, gives \(f(x)<f^2(x)\); induction makes the entire orbit strictly increasing. The case \(x>f(x)\) makes it strictly decreasing. Every iterate stays in the parity class of its starting point, so an orbit uses at most \(\lceil n/2\rceil\) distinct vertices. If its largest directed path has \(L\) vertices, \(f^{L-1}\ne0\) and \(f^L=0\); hence \(\nu(f)\le\lceil n/2\rceil\). Both translations by two, restricted to a full increasing or decreasing parity path, attain the upper bound.

**2. Rigidity of a maximal orbit.** Suppose \(\nu(f)=\lceil n/2\rceil=:L\). Some directed orbit has exactly \(L\) vertices, all in one parity class. Since this class has at most \(L\) points, the orbit visits **every** point of a class with precisely \(L\) points. Its strict monotonicity forces its consecutive values to be the full parity list, in increasing or decreasing order; therefore \(f(x)=x+2\) or \(f(x)=x-2\) on the \(L-1\) nonterminal orbit points. Reversing the chain and the direction exchanges the cases, so it suffices to analyze the forward direction.

**3. All remaining source points are forced to translate by two.** Write the mandatory source parity class in increasing order as \(a_1<a_2<\cdots<a_L\), where \(a_{j+1}=a_j+2\), and \(f(a_j)=a_{j+1}\) for \(j<L\). Any extra source \(b\) has the opposite parity: every point of the orbit parity class except the terminal point is already mandatory, and the terminal point cannot lie in the domain because its image would have to be greater than \(a_L\), outside the chain or incompatible with injectivity and the neighboring parity-chain images. More directly, for forward direction \(a_L\) is the last element of its parity class and either \(a_L=n\), or \(a_L=n-1\) while the larger integer has opposite parity; any same-parity image greater than \(a_L\) is impossible.

If \(a_j<b<a_{j+1}\) for some \(j<L-1\), order preservation gives \(a_{j+1}<f(b)<a_{j+2}\); there is only one integer in this interval, namely \(f(b)=b+2\). If \(b\) is the opposite-parity point immediately before the first mandatory source, then \(b,a_1\) are adjacent in the fence, so two-sided fence preservation forces their images to be adjacent. Since \(f(b)<a_2\) and parity is fixed, the only possibility is \(f(b)=a_2-1=b+2\). If \(b\) follows the final mandatory source \(a_{L-1}\), then it is the immediately succeeding opposite-parity point: the next same-parity point, if any, is the excluded terminal orbit vertex. Fence adjacency therefore forces \(f(b)=a_L+1=b+2\) when this lies in \([n]\). If it does not, there is no admissible image greater than \(a_L\) of the correct parity, except in the even-size odd-orbit case \(b=n\), where the only candidate is \(f(n)=n\); that fixed point is incompatible with nilpotence. Thus no point beyond the translation domain can be included. Every possible extra source consequently lies in \(D_+=\{1,\ldots,n-2\}\), with image forced to be \(b+2\).

Conversely, for any subset of the available opposite-parity sources in \(D_+\), adjoining those sources to the mandatory parity-path sources and restricting \(\tau_+\) produces a strictly increasing parity-preserving partial injection that preserves fence adjacency both ways. It contains the mandatory \(L\)-vertex orbit and thus has maximal nilpotency index. The same reasoning holds for \(\tau_-\). Because \(n\ge3\) gives \(L\ge2\), no nonempty maximum-index map can be a restriction of both \(\tau_+\) and \(\tau_-\).

**4. Counting the Boolean families and intersections.** For odd \(n=2m+1\), the sole parity class of size \(L=m+1\) consists of the odds. The forward mandatory sources are \(1,3,\ldots,2m-1\) (\(m\) sources), and the optional points are \(2,4,\ldots,2m-2\) (\(m-1\) sources). Thus the forward rank enumerator is \(z^m(1+z)^{m-1}\), with the same expression for the opposite direction and no overlap. This proves the odd formula.

For even \(n=2m\), both parity classes have size \(L=m\). Each direction and each mandatory parity choice supplies \(m-1\) compulsory and \(m-1\) optional sources, giving \(z^{m-1}(1+z)^{m-1}\). Within the same direction, the two choices intersect precisely when every point of \(D_+=[n-2]\) is present: both parity paths must be included, and that single map has domain rank \(2m-2\). Likewise for \(\tau_-\) with source domain \(\{3,\ldots,n\}\). By inclusion-exclusion over the four families, we subtract \(2z^{2m-2}\), proving the even formula. Substituting \(z=1\) yields the total counts.

## Verification
Run `python verify.py` using standard Python 3 from this package. The verifier exhaustively enumerates all increasing pairs of equally sized subsets of \([n]\), tests their parity and both directions of fence adjacency directly, and computes least zero powers by iterating each partial map. For every \(3\le n\le10\), it compares the complete observed set of extremizers with an independently constructed union of translation-restriction families, and compares exact domain-rank frequencies to the closed formulas. It also cross-checks total monoid cardinalities against independently established initial terms: \(10,22,52,120,286,678,1628,3912\). The final successful output is `FENCE_EXTREMAL_NILPOTENCE_VERIFIED n=3..10`. These finite computations corroborate but do not prove the all-size theorem, which follows from the preceding orbit and adjacency arguments.

For illustration, the maximum-index counts in sizes \(n=3,4,5,6,7,8,9,10\) are respectively \(2,6,4,14,8,30,16,62\). A parity-preserving order/fence map need not itself be a translation: on \([7]\), the partial map \(1\mapsto3,\ 3\mapsto7\) is admissible but is not an isometry and has nilpotency index three rather than the maximum four. Hence translation rigidity here is a property of the **extremal locus**, not an ambient hypothesis.

## Relationship to prior work
Sareeto and Koppitz [1] introduced the precise domain/image gap characterization of this monoid and determined its minimum generating-set rank \(3n-6\) for \(n\ge4\); the present proof uses their fence and parity conditions but concerns nilpotency index, not generating sets. Their later presentation [2] and maximal-ideal-subsemigroup classification [3] address different invariants. A previously published algebraic generating function counts **all** elements of this monoid [4], and is credited for the independent finite cardinality comparison; counting all elements without a nilpotency-index filtration does not imply the rigidity and extremal rank formulas.

Related results [5,6] classify nilpotency profiles of **partial isometries** or maximal-rank-relative-index nilpotents of **partial contractions**. Neither establishes that the global maximum-index locus of the larger parity/fence monoid is contained in the two-step translations; that newly proved rigidity is the essential bridge to the Boolean-family census. A search for equivalent formulations, more general dominating results, tabulations and aliases did not identify a prior theorem containing that bridge. However, a search failure is not proof of priority, and there remains risk of an older formulation using different monoid terminology or a general statement that implicitly subsumes the result.

## Limitations
The result applies to the exact two-sided fence-preserving, parity-preserving, increasing partial-injection monoid and only to the **largest nilpotency index**, not all nilpotent elements, all indices, or all partial injections. The polynomial variable records domain rank, not semigroup generating rank. Only the \(n\ge3\) family is claimed; the zero element is not a maximum-index extremizer in those sizes. The proof establishes an exact infinite-family theorem, whereas the executable's finite enumeration runs only through size ten. Independent mathematical auditing has not been performed; publication priority is conditional on available literature and may change with additional sources.

## References
[1] A. Sareeto and J. Koppitz, *The rank of the semigroup of order-, fence-, and parity-preserving partial injections on a finite set*, arXiv:2208.03202, first public 5 August 2022, especially Proposition 1. https://arxiv.org/abs/2208.03202

[2] A. Sareeto and J. Koppitz, *A presentation for a submonoid of the symmetric inverse monoid*, arXiv:2310.15809, first public 24 October 2023. https://arxiv.org/html/2310.15809v1

[3] A. Sareeto and J. Koppitz, *The maximal subsemigroups of the ideals on a monoid of partial injections*, arXiv:2403.06957, first public 11 March 2024. https://arxiv.org/abs/2403.06957

[4] *Algebraic cardinality series and sharp growth of parity-preserving fence inverse monoids*, published mathematical result, 2026. https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-algebraic-cardinality-series-and-sharp-growth-of-parity-preservi--cd10259c2cbb

[5] *Nilpotency-height rank profiles and a lattice extreme law for order-preserving partial isometries*, published mathematical result, 2026. https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-nilpotency-height-rank-profiles-and-a-lattice-extreme-law-for-or--3383014bbd25

[6] *Extremal nilpotency in order-preserving partial contractions is governed by integer partitions*, published mathematical result, 2026. https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-extremal-nilpotency-in-order-preserving-partial-contractions-is--cbbee36cc90b
