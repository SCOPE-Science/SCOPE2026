# Fibonacci-cube components and a Poisson mobility law for involutions in the permutahedron

## Finding

Let \(G_n\), for \(n\ge1\), be the graph whose vertices are permutations \(\pi\in S_n\) satisfying \(\pi^2=\mathrm{id}\), where an edge is allowed when swapping values in exactly two neighboring **one-line positions** produces another involution. Define the Fibonacci numbers by \(F_0=0\), \(F_1=1\), and \(F_{m+2}=F_{m+1}+F_m\). The Fibonacci cube \(\Gamma_d\) is the induced graph on binary strings of length \(d\) without adjacent ones, adjacent at Hamming distance one, with \(\Gamma_0=K_1\).

For each matching \(M\) consisting entirely of nonconsecutive pairs \(\{i,j\}\subseteq[n]\), \(j-i\ge2\), remove its covered positions and let \(\ell_1,\ldots,\ell_r\) be the lengths of maximal nonempty consecutive runs in the residual ordered subset. There is exactly one component \(H_M\) with the nonconsecutive two-cycles \(M\), and
\[
H_M\cong\mathop{\square}_{a=1}^{r}\Gamma_{\ell_a-1},\qquad
|V(H_M)|=\prod_{a=1}^{r}F_{\ell_a+1},\qquad
\operatorname{diam}(H_M)=\sum_{a=1}^{r}(\ell_a-1).
\]
An empty product is one and an empty sum zero. If \(T(\pi)\) is the set of adjacent transpositions appearing in \(\pi\), then for vertices in one component the shortest-path distance is \(|T(\pi)\triangle T(\sigma)|\).

For \(n\ge1\), the unique largest component is \(H_\varnothing\cong\Gamma_{n-1}\), having \(F_{n+1}\) vertices. For \(n\ge3\), the unique second-largest component is indexed by \(M=\{\{1,n\}\}\) and has \(F_{n-1}\) vertices. Write \(I_0=I_1=1\), \(I_n=I_{n-1}+(n-1)I_{n-2}\). The number of components is
\[
C_n=\sum_{j=0}^{\lfloor n/2\rfloor}(-1)^j\binom{n-j}{j}I_{n-2j},
\]
and the total edge count for \(n\ge2\) is \(|E(G_n)|=(n-1)I_{n-2}\); there are no edges for \(n=1\).

For a uniformly sampled involution, its vertex degree converges in law to \(\operatorname{Poisson}(2)\), while \(C_n/I_n\to e^{-1}\) and the proportion of isolated vertices tends to \(e^{-2}\). Consequently the arithmetic mean of component sizes approaches \(e\), although the largest component has Fibonacci-exponential size.

## Assumptions and scope

The domain is the complete involution set (fixed points allowed) on the fixed **labelled linear order** \([n]\); adjacency exchanges positions \(i\) and \(i+1\), not arbitrary values or conjugation. The graph is undirected and simple. A matching here means a set of pairwise vertex-disjoint unordered pairs, and a *long* pair means a nonconsecutive pair. We make no claim about a cyclic order, token-sliding rules, or a single fixed-point-free class.

## Proof

**Local criterion.** Write \(s_i=(i\ i+1)\). Swapping positions of \(\pi\) is right composition \(\pi s_i\). Because both factors are involutions, \((\pi s_i)^2=\mathrm{id}\) is equivalent to \(\pi s_i=s_i\pi\). A permutation commutes with the transposition \(s_i\) precisely when it preserves the unordered two-element set \(\{i,i+1\}\). Since \(\pi\) is an involution, this means it either fixes both members or swaps those two members. Hence every allowed edge toggles exactly the short two-cycle \((i\ i+1)\), replacing it with two fixed points, or vice versa. Every long two-cycle is invariant under legal moves.

**Components.** Every involution is uniquely the product of its disjoint long two-cycles, short two-cycles, and fixed points. Fixing the long-cycle matching \(M\), the only choices are disjoint edges \(\{i,i+1\}\) whose ends are not in \(V(M)\). These choices form all matchings of the subgraph of the ordinary path induced on \([n]\setminus V(M)\). Encode each such edge by one binary coordinate. Matchings correspond exactly to binary coordinate strings with no two adjacent ones on each residual run, and a legal move toggles one coordinate. All choices are mutually connected because one can remove the coordinates of one matching and then add the new coordinates of another. Thus the full \(M\)-sector is one connected component and is the claimed Cartesian product. The same remove-then-add path has length \(|T(\pi)\triangle T(\sigma)|\), attaining the Hamming lower bound. For a residual run of length \(\ell\), there are \(F_{\ell+1}\) matchings; the Fibonacci-cube diameter is \(\ell-1\), attained by the two complementary alternating edge sets, hence the claimed product formulas.

**Extrema.** Inserting separators between disjoint residual path runs can only increase the number of matchings, so \(\prod_a F_{\ell_a+1}\le F_{r+1}\) when their lengths sum to \(r\); strict inequality occurs if \(r\ge2\) and a genuine separator splits a nontrivial choice. Nonempty \(M\) removes at least two positions, hence \(|V(H_M)|\le F_{n-1}\). Equality for \(n\ge3\) forces exactly one removed long pair, with all \(n-2\) residual positions consecutive, and therefore uniquely \(M=\{\{1,n\}\}\). The empty matching gives size \(F_{n+1}\), larger when \(n\ge3\); for \(n=1,2\) it is the only component.

**Exact totals.** Components are in bijection with involutions having no adjacent two-cycle, because each long matching is such an involution. Applying inclusion-exclusion to the \(n-1\) forbidden adjacent pairs, the number of ways to choose \(j\) mutually disjoint adjacent pairs is \(\binom{n-j}{j}\). Force these pairs and leave an arbitrary involution on the other \(n-2j\) positions to obtain \(C_n\). At a specified position pair, there are exactly \(I_{n-2}\) involutions in which the pair is a short two-cycle, and exactly \(I_{n-2}\) involutions in which both points are fixed; exactly those configurations allow the corresponding move. Summing their degrees over all \(n-1\) pairs and dividing by two gives \(|E(G_n)|\).

**Limiting law.** Let \(D_n\) be the number of legal adjacent swaps. For each neighboring pair, its event is the disjoint union of 'both fixed' and 'short two-cycle'. For \(r\) distinct *pairwise disjoint* position pairs, simultaneous occurrence has probability \(2^r I_{n-2r}/I_n\), and the number of ordered choices is \(r!\binom{n-r}{r}\). For overlapping selected pairs, group their positions into \(c<r\) consecutive edge clusters. Every cluster of at least two edges forces all covered positions to be fixed, and a singleton cluster allows precisely the two local states just mentioned. A configuration with \(r\) selected edges in \(c\) clusters therefore fixes local states on \(r+c\) distinct positions, with probability bounded by \(2^c I_{n-r-c}/I_n\); the number of ordered selections of any fixed cluster pattern is \(O(n^c)\). The needed fixed-\(s\) ratio \(I_{n-s}/I_n\sim n^{-s/2}\) has a self-contained proof: set \(R_m=I_m/I_{m-1}\). The recurrence gives \(R_m=1+(m-1)/R_{m-1}\), and induction starting at \(R_1=1\) proves \(\sqrt m\le R_m\le\sqrt m+1\). Indeed, if \(x=\sqrt{m-1}\), the inductive upper bound yields \(R_m\ge1+x^2/(x+1)=x+1/(x+1)\ge\sqrt{x^2+1}\); the inductive lower bound gives \(R_m\le1+x\le1+\sqrt m\). Multiplying the ratios \(1/R_m\) at \(m=n-s+1,\ldots,n\) proves the required estimate. Thus the disjoint-pair contribution to \(\mathbb E[(D_n)_r]\) tends to \(2^r\), and all overlaps contribute \(O(n^{-(r-c)/2})\to0\). All factorial moments match those of \(\operatorname{Poisson}(2)\), determining its distribution. The same calculation for the number of short two-cycles (just one choice per disjoint pair, no overlaps possible) yields a \(\operatorname{Poisson}(1)\) limit. The number of components equals the number of involutions with no short two-cycles, so \(C_n/I_n\to e^{-1}\). Since \(D_n=0\) precisely for isolated states, their fraction tends to \(e^{-2}\), by convergence in distribution at the integer threshold.

## Verification

Run `python3 check_invol.py` using Python 3 without external dependencies. The checker independently enumerates all self-inverse permutations for each \(1\le n\le9\), obtains edges by directly swapping positions and checking the involution condition, constructs every connected component by breadth-first search, and compares it with the long-cycle invariant and Fibonacci product counts. It also checks the exact component-count inclusion-exclusion, total edges, largest sizes, and, through \(n=8\), every shortest-path distance by independent breadth-first searches. Counts through \(n=9\): total involutions \(1,2,4,10,26,76,232,764,2620\); components \(1,1,2,5,13,37,112,363,1235\). The all-length and limiting claims are mathematical deductions above, not finite-experiment extrapolations.

## Relationship to prior work

Fibonacci cubes and their diametral path theory are established; the novelty claimed is **not** the count or diameter of a Fibonacci cube. Eğecioğlu, Saygı, and Saygı (2022) study those cubes as abstract graphs. Avis and Hoang (2022) analyze independent-set reconfiguration under token sliding, which preserves occupied-set cardinality; the present local operation instead adds/removes a short transposition while fixing all nonadjacent transpositions. The claimed new step is the precise *global* decomposition of the involution-induced permutahedron into all those products, with its exact component/edge enumeration and the Poisson mobility limit. The unrestricted adjacent-swap permutahedron is connected; restricting to involutions radically changes its geometry.

## Limitations

This is an all-length theorem for one prescribed move relation, not a theorem about arbitrary transpositions, conjugacy-class reconfiguration, or sorting algorithms on all permutations. Its limiting law is under the uniform distribution on all involutions. No independence verification or exhaustive historical-priority claim is made; an unindexed equivalent formulation could exist. The finite verifier establishes small-length consistency, not the infinite theorem. The elementary recurrence bounds on consecutive involution-number ratios give the asymptotic needed in the proof, without invoking an external analytic result.

## References

1. D. Avis and D. A. Hoang, *On Reconfiguration Graphs of Independent Sets under Token Sliding*, arXiv:2203.16861, first publicly posted 2022-03-31, https://arxiv.org/abs/2203.16861.
2. Ö. Eğecioğlu, E. Saygı and Z. Saygı, *Euler numbers and diametral paths in Fibonacci cubes, Lucas cubes and Alternate Lucas cubes*, arXiv:2210.13849, first publicly posted 2022-10-25, https://arxiv.org/abs/2210.13849.
