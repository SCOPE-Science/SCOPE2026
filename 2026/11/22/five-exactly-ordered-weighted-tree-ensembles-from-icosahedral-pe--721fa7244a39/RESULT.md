# Five exactly ordered weighted-tree ensembles from icosahedral perfect matchings

## Finding
Let \(I\) be the 12-vertex icosahedral graph and let \(\mathcal M\) be its set of perfect matchings. For \(M\in\mathcal M\) and \(t>0\), assign conductance \(t\) to the six edges of \(M\) and conductance 1 to the other 24 edges. The weighted spanning-tree partition function is
\[
Z_M(t)=\sum_{T\text{ spanning tree of }I} t^{|T\cap M|}.
\]
Precisely five distinct polynomials occur among the 125 choices of \(M\). Writing \(P_j\) for the polynomial realized by exactly \(j\) matchings, they are
\[
\begin{aligned}
P_5(t)&=1536(t+2)^3(2t+3)^3,\\
P_{20}(t)&=6(t+2)(2t+3)(31t^2+114t+95)^2,\\
P_{60}(t)&=10(t+2)^2(31t^2+114t+95)(35t^2+122t+83),\\
P_{30}(t)&=64(t+2)^2(3t+7)(11t+19)(5t^2+16t+9),\\
P_{10}(t)&=384(t+2)^3(3t+2)(3t+7)^2.
\end{aligned}
\]
For **every** \(t>0\) other than \(t=1\), their strict global ranking is
\[
P_5(t)>P_{20}(t)>P_{60}(t)>P_{30}(t)>P_{10}(t).
\]
At \(t=1\), all five equal \(5{,}184{,}000\). Hence the same five matchings maximize the partition function whether the designated edges are weakened or strengthened. These five maximizers are exactly the five perfect matchings that admit no alternating four-cycle flip; the latter characterization was previously established independently and is not claimed as new. The ten minimizers are exactly the matchings of type \(P_{10}\).

## Assumptions and scope
Use vertices \(0,1,\ldots,11\); for \(i\in\mathbb Z/5\mathbb Z\), set \(u_i=1+i\) and \(v_i=6+i\). The thirty edges are
\[
\{0u_i,\ 11v_i,\ u_iu_{i+1},\ v_iv_{i+1},\ u_iv_i,\ u_iv_{i+1}: i\in\mathbb Z/5\mathbb Z\}.
\]
This defines the standard icosahedral graph (twelve vertices each of degree five). A perfect matching is a six-edge set meeting every vertex exactly once. The partition function uses **product** conductance weights, not the minimum sum of edge costs; a tree with \(a\) marked edges contributes \(t^a\). The variable is an arbitrary positive real, and a statement at \(t=0\) is only a polynomial limit, not part of the model assumptions.

## Proof
**Exhaustive matching classification.** Given a set of unmatched vertices, choose its least-labeled vertex and branch over each available neighbor, then recurse. Every perfect matching contains exactly one such edge, so recursion enumerates every matching exactly once. The first independent program lists precisely 125 distinct matchings. For each matching, construct the eleven-by-eleven grounded weighted Laplacian. By the weighted matrix-tree theorem, its determinant is \(Z_M(t)\). Because the marked matching contains six edges, this determinant is a polynomial of degree at most six in \(t\). Exact Bareiss determinants at \(t=0,1,2,3,4,5,6\), followed by rational Newton interpolation, therefore determine each full polynomial—not a numerical approximation or partial sampling. Checking the identity at \(t=7\) independently tests interpolation. The 125 polynomials coincide with exactly the five displayed factors and have multiplicities 5, 20, 60, 30, and 10.

**Uniform baseline and first moment.** At \(t=1\), the tree count is \(5{,}184{,}000\). By edge transitivity, each of the 30 edges belongs to the same fraction \((12-1)/30=11/30\) of uniform spanning trees. Therefore the derivative at one is \(6(11/30)\cdot5{,}184{,}000=11{,}404{,}800\), independent of the matching. Hence every difference between two class polynomials is divisible by \((t-1)^2\).

**Sharp all-parameter ordering.** Direct exact factorization of the four adjacent differences yields
\[
\begin{aligned}
P_5-P_{20}&=6(t-1)^2(t+2)(2t+3)(63t^2+226t+191),\\
P_{20}-P_{60}&=2(t-1)^2(t+2)(11t+25)(31t^2+114t+95),\\
P_{60}-P_{30}&=2(t-1)^2(t+2)^2(145t^2+814t+1121),\\
P_{30}-P_{10}&=64(t-1)^2(t+2)^2(t+3)(3t+7).
\end{aligned}
\]
Every factor other than \((t-1)^2\) is strictly positive for \(t>0\); the claimed strict ranking follows, with equality only at \(t=1\). Exhaustive pairwise symmetric-difference tests of all matchings show exactly five have no alternating four-cycle neighbor; they are exactly the \(P_5\) configurations. The already-known count and frozen-status fact are cited, not promoted to a new discovery.

**Independent transfer-current reconstruction.** The second independent program uses a separately encoded standard icosahedral adjacency list (and explicitly checks an isomorphism to the ring realization). It constructs the inverse \(L_0^{-1}\) of the unit-conductance grounded Laplacian over the rationals. If \(B_M\) is the eleven-by-six oriented incidence matrix of marked matching edges, the matrix determinant lemma gives
\[
Z_M(t)=5{,}184{,}000\det\bigl(I_6+(t-1)B_M^{\mathsf T}L_0^{-1}B_M\bigr).
\]
The two constructions use different matching-enumeration orders and different exact determinant methods. The transfer-current computation checks seven interpolation values plus \(t=8\) for each of the 125 matchings and reproduces all five polynomials and class sizes. Both independent finite exhaustive paths justify the asserted classifications.

## Verification
From the directory containing the two supplied, self-contained, standard-library Python 3 programs, run

```bash
python3 verify_laplacian.py
python3 verify_transfer_current.py
```

The first program outputs all five ascending coefficient vectors, checks the class sizes, common value and first derivative at one, and certifies each adjacent difference has positive coefficients after division by \((t-1)^2\). It also computes the alternating four-cycle flip degree of all matchings. The second computes 1,000 independent exact-rational transfer-current evaluations and checks a separate adjacency labeling and all five polynomial classes. Both were run against their actual included source files with their asserted checks passing. No finite run is substituted for an infinite numerical sampling argument: exact degree bounds and interpolation make the finite computation exhaustive for **every** real \(t>0\).

## Relationship to prior work
Kenyon, Propp and Wilson (1999) derive a weight-preserving spanning-tree/perfect-matching bijection for planar graphs, but the matchings live in an **auxiliary** graph, not the same graph whose original perfect matching specifies six conductance changes. Their general identity is background, not this icosahedral five-class optimization. Khosoussi and collaborators (2016) study maximizing weighted spanning-tree counts by graph design, including general matroid-constrained edge selection and relaxations, but do not supply the exact icosahedral marked-matching polynomials, class counts, or global order.

The earlier icosahedral perfect-matching flip classification already establishes there are 125 matchings and exactly five four-cycle-isolated matchings. Here those known five are identified, through new weighted-tree calculations, as the exact strict optimizers across every nontrivial positive rate contrast. A previously reported exact icosahedral uniform spanning-tree path-length census concerns the common specialization \(t=1\), which cannot determine the six marked-edge coefficients or the placement ordering. Generic determinant identities can of course be used to *compute* these polynomials but do not imply the specific five-class order without performing this comparison.

## Limitations
This theorem concerns the fixed twelve-vertex icosahedral graph, uniform off-matching conductances, and selecting precisely one entire perfect matching. It does not classify arbitrary six-edge subsets, variable individual edge weights, other regular polyhedral graphs, or random-time kinetic observables. Its proof is a complete finite exact classification with reproducible integer and rational algorithms, not a formally checked or independent external audit. No search can prove absolute publication priority; inaccessible or unindexed equivalent specialized work is a residual historical risk.

## References
1. R. Kenyon, J. Propp and D. Wilson, *Trees and Matchings*, arXiv:math/9903025 (first posted 1999-03-03), *Electronic Journal of Combinatorics* 7 (2000), #R25, https://arxiv.org/abs/math/9903025 and https://doi.org/10.37236/1503.
2. K. Khosoussi, G. S. Sukhatme, S. Huang and G. Dissanayake, *Maximizing the Weighted Number of Spanning Trees: Near-t-Optimal Graphs*, arXiv:1604.01116 (first posted 2016-04-05), https://arxiv.org/abs/1604.01116.
3. *Five frozen icosahedral matchings become the centers under six-cycle flips*, publicly indexed mathematical research (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-five-frozen-icosahedral-matchings-become-the-centers-under-six-c--98a001e14839.
