# Fourteen habitat sites are the sharp onset of twice-reversing gateway containment priorities

## Finding

Consider an invasible habitat network that is a finite rooted directed out-tree, with the origin \(o\) possessing exactly two outgoing edges (the two *gateways*), and all edges directed away from \(o\). The origin is occupied initially. Each unblocked directed edge independently transmits colonization with a common probability \(p\in(0,1)\), and colonization thereafter propagates along open directed paths. One may perfectly and permanently close exactly one gateway edge before propagation. The objective is to minimize the expected final number of occupied sites, with one unit of consequence per site.

**Sharp theorem.** If the total number of vertices is at most \(13\), the identity of a strictly preferable gateway closure cannot switch twice as \(p\) increases from zero to one. For \(14\) vertices, there exists a network on which the preferred closure switches *exactly twice*. The sharp first size is therefore \(14\), within this fixed-source, two-gateway, equal-consequence model.

An explicit witness has the source vertex \(0\) and directed edges

```
0->1, 1->2, 2->3, 2->4, 2->5, 2->6,
0->7, 7->8, 7->9, 8->10, 10->11, 11->12, 11->13
```

Its first gateway leads to \(6\) sites, with the depth profile \((1,1,4)\); the second leads to \(7\) sites, with depth profile \((1,2,1,1,2)\). The expected occupation reductions from closing these gateways are

\[
G_A(p)=p+p^2+4p^3,\qquad
G_B(p)=p+2p^2+p^3+p^4+2p^5.
\]

Their exact difference is

\[
G_A(p)-G_B(p)=-p^2(2p-1)(p^2+p-1).
\]

Consequently gateway \(B\) is uniquely preferable to close on \(0<p<1/2\) and on \((\sqrt5-1)/2<p<1\); gateway \(A\) is uniquely preferable to close on \(1/2<p<(\sqrt5-1)/2\). Both closures tie exactly at \(p=1/2\) and \(p=(\sqrt5-1)/2\). Thus a policy can revert to its original favored gateway as transmission becomes more reliable, without any change in habitat values, edges, intervention costs, or invasion origin.

## Assumptions and scope

The network is a finite simple directed tree rooted at a known initial source; only its two *outgoing root edges* are eligible for removal, and exactly one of them is removed. The two downstream rooted branches are nonempty and may have arbitrary positive integer branching. Edges independently succeed with the same \(p\). Colonization is irreversible and follows all successful outgoing edges; there are no additional introductions, feedback, edge heterogeneity, density dependence, or costs other than expected occupied-site count. Total size includes the source. A *reversal* is a strict change of which action has the smaller expected occupied count at a parameter inside \((0,1)\); an everywhere tie or an isolated tangency is not a reversal. No uniqueness of the smallest witness is claimed.

## Proof

**1. Exact gateway benefits.** For either branch \(i\in\{A,B\}\), let \(b_{i,k}\) denote the number of sites at distance \(k\ge1\) from the original source. Each such vertex is reached if and only if every edge on its unique length-\(k\) path succeeds, an event of probability \(p^k\). Linearity of expectation, with no assertion of independence among site-occupation indicators, gives

\[
G_i(p)=\sum_{k\ge1}b_{i,k}p^k.
\]

All sites downstream of a removed gateway are inaccessible, so \(G_i\) is precisely the expected number of occupied sites prevented by removing that gateway relative to no removal. The expected total occupation after one removal equals the unprotected expectation minus \(G_i\). Therefore the strictly better gateway to close is precisely the one with larger \(G_i(p)\).

**2. Exhaustive class of feasible profiles.** For a branch with \(m\ge1\) sites, the first depth contains its sole gateway-adjacent vertex: \(b_1=1\). All subsequent depth levels up to its greatest depth are nonempty, and their widths are arbitrary positive integers summing to \(m-1\). Conversely, every vector \((1,b_2,\ldots,b_L)\) of this form is realized by a rooted out-tree: attach all sites of depth \(k+1\) to any one site of depth \(k\). For \(m=1\), only \((1)\) occurs. Thus the list of possible profiles is in bijection with all ordered positive-integer compositions of \(m-1\). The two branches are disjoint and have sizes totaling \(n-1\) if the whole network has \(n\) vertices. A finite comparison of profiles therefore covers *every* admissible directed tree, not just a selection of topologies.

**3. An exact exclusion certificate through \(13\) vertices.** Let \(P(p)\) be the difference of the two gateway-benefit polynomials. If it is identically zero, the two closures tie throughout and cannot reverse. Otherwise cancel its initial power of \(p\), and write the remaining polynomial \(C(p)=\sum_{i=0}^{d}c_i p^i\) with nonzero constant and leading coefficients. Map \(p=t/(1+t)\) bijectively from \((0,\infty)\) onto \((0,1)\). Then

\[
Q(t)=(1+t)^d C\!\left(\frac{t}{1+t}\right)
=\sum_{j=0}^{d}B_jt^j,\quad
B_j=\sum_{i=0}^{j}c_i\binom{d-i}{j-i}.
\]

Every \(B_j\) is an exact integer. By Descartes' rule, the number of positive real zeros of \(Q\), counted with multiplicity, cannot exceed the number of sign variations among its nonzero coefficients. Therefore at most one sign variation is a rigorous certificate that the original gateway ranking has at most one interior crossing.

The accompanying standard-library program `check_gate_reversals.py` visits every ordered positive composition for both branch sizes summing to at most \(12\); it counts each unordered pair of *distinct* depth profiles once and computes the displayed exact integer coefficients. The numbers of comparisons for total network sizes \(n=3,4,5,6,7,8,9,10,11,12,13\) are, respectively,

\[
0,\;1,\;2,\;6,\;13,\;32,\;70,\;160,\;348,\;768,\;1656,
\]

which sum to \(3056\). Every single difference has zero or one transformed-coefficient sign variation; none has two. The checker independently cross-verifies the composition generator by a recursive generator, asserts all eleven per-size comparison totals, and terminates with `VERIFY_OK`. For \(n\le2\) the stated two nonempty gateways cannot exist. This is an exhaustive finite integer calculation with a proved complete parametrization, not a finite grid of transmission probabilities.

**4. Exact sharpness witness.** The listed \(13\) directed edges form a rooted tree on \(14\) vertices. Its two level-width vectors are verified directly from the graph in the accompanying checker. Substituting those widths into step 1 yields

\[
\Delta(p)=G_A(p)-G_B(p)=-p^2(2p-1)(p^2+p-1).
\]

In \((0,1)\), its only roots are the simple zeros \(p=1/2\) and \(p=(\sqrt5-1)/2\); the factor \(p^2\) vanishes only at the excluded endpoint. The signs are negative, positive, negative in the successive open intervals. Hence both are strict reversals, and the exclusion result in step 3 proves minimality.

## Verification

Run `python3 check_gate_reversals.py` in the directory containing this document, using only Python 3 standard-library facilities. Expected terminal output is:

```
NO_TWO_REVERSALS_ON_AT_MOST_13_VERTICES 3056
WITNESS_SIZE 14
VERIFY_OK
```

This exact checker cross-verifies two composition generators; visits all profile pairs for each network size; checks the sign-variation certificate with integer binomial coefficients; rebuilds the witness profiles from its full directed edge list; and checks exact rational comparison signs in all three intervals. It does not rely upon an empirical probability grid, software-generated floating-point roots, a simulation, or any unenumerated tree shapes.

## Relationship to prior work

Carter and colleagues (2024) motivate spatial prioritization of invasive-species control while jointly accounting for established impacts and future dispersal. Their spatial planning and distribution models do not claim an exact finite rooted-tree cutoff for transmissibility-driven two-switch containment rankings. The 2012 link-quarantine work of Enns, Mounzer and Brandeau studies undirected-network partitioning and the number of nodes still *at risk*, rather than expected occupation under a varying independent edge-transmission probability.

Khorramzadeh, Youssef, Eubank and Mowlaei (2015) already show that reliability-polynomial rankings and edge importance can vary with reliability, including multiple potential intersections; the general fact that intervention priorities can reverse, the reliability-polynomial approach, and the appearance of the golden-ratio reciprocal are not claimed as novel here. Published finite-tree results on optimal *uniform-random-seed* edge removal and on *fixed-seed outbreak-size variance* also establish parameter-dependent rankings, but neither proves or implies the present exactly two-eligible-gateway, *fixed-origin expected-size*, sharp \(14\)-site result. A published rooted-phylogeny result establishes two crossings for expected surviving diversity with leaf-extinction probability; its different feasible coefficient profiles and objective do not imply the present threshold. The distinct contribution claimed here is the sharply minimal two-gateway containment structure with exact intervention intervals.

## Limitations

This is an abstract, equal-site-value, single-origin, two-gateway, homogeneous independent-dispersal model; it is not a calibrated prediction of any particular invasive species, disease or landscape. It does not classify all trees of size \(14\), networks with more than two eligible closure sites, root nodes with additional unprotected outgoing edges, multiple initial sources, non-tree paths, unequal site values, or repeated introductions. The exact integer census establishes minimality only for this specified class; it neither certifies novelty across unpublished literature nor implies that a site in a real habitat network changes priority at these same probabilities. Independent external audit has not been performed.

## References

1. S. Carter, C. Mills, Z. Hao, R. Mott, C. E. Hauser, M. White, J. Sharples, J. Taylor and J. L. Moore, "Spatial prioritization for widespread invasive species control: Trade-offs between current impact and future spread," *Ecological Applications* **34** (2024), e2982; first published 2024-06-03, https://doi.org/10.1002/eap.2982 .
2. E. A. Enns, J. J. Mounzer and M. L. Brandeau, "Optimal link removal for epidemic mitigation: a two-way partitioning approach," *Mathematical Biosciences* **235** (2012), 138–147, https://doi.org/10.1016/j.mbs.2011.11.006 .
3. Y. Khorramzadeh, M. Youssef, S. Eubank and S. Mowlaei, "Analyzing network reliability using structural motifs," *Physical Review E* **91** (2015), 042814; arXiv:1403.7074, https://arxiv.org/html/1403.7074v2 .
4. "First transmissibility-sensitive optimal edge cuts in tree epidemics," published finite-tree mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/10/13/SCOPE-first-transmissibility-sensitive-optimal-edge-cuts-in-tree-epide--8974612ce954 .
5. "Seven vertices are sharp for two outbreak-variance ranking reversals on trees," published finite-tree mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-seven-vertices-are-sharp-for-two-outbreak-variance-ranking-rever--8b64466bf53a .
6. "Eleven leaves are sharp for two reversals in expected future phylogenetic diversity," published phylogenetic mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-eleven-leaves-are-sharp-for-two-reversals-in-expected-future-phy--0dffbe31b8d3 .
