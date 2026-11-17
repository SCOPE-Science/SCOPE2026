# A two-unit orientation gap in Euclidean diameters of zigzag Bruhat interval polytopes

## Finding
For every integer \(n\ge3\), let \(s_i\) be the adjacent transposition exchanging the **positions** \(i\) and \(i+1\) of a one-line permutation. Form the two bipartite (zigzag) Coxeter elements
\[
 c_{\rm O}=\bigl(\prod_{i\ {
m odd}}^{\nearrow}s_i\bigr)\bigl(\prod_{i\ {
m even}}^{\nearrow}s_i\bigr),\qquad
 c_{\rm E}=\bigl(\prod_{i\ {
m even}}^{\nearrow}s_i\bigr)\bigl(\prod_{i\ {
m odd}}^{\nearrow}s_i\bigr),
\]
where each product is ordered by increasing index. For \(c\in\{c_{\rm O},c_{\rm E}\}\), let
\[
 Q_{n,c}=\operatorname{conv}\{(w(1),\ldots,w(n)):e\le_{\rm Bruhat}w\le_{\rm Bruhat}c\}\subset\mathbb R^n.
\]
All diameters below are **extrinsic Euclidean** diameters in these unscaled standard coordinates, not 1-skeleton graph diameters.

**Theorem (both zigzag orientations, all orders).** The exact squared Euclidean diameters are
\[
 \operatorname{diam}_2(Q_{n,c_{\rm O}})^2=
 \begin{cases}9n-19,&n\text{ odd},\\9n-18,&n\text{ even},\end{cases}
 \qquad
 \operatorname{diam}_2(Q_{n,c_{\rm E}})^2=
 \begin{cases}9n-19,&n\text{ odd},\\9n-20,&n\text{ even}.\end{cases}
\]
To describe **every unordered diametral pair**, write the displayed word of \(c\) as its first parity-class batch \(A\), followed by its other parity-class batch \(B\). Retain *every* transposition of \(A\) in both permutations; independently partition the transpositions of \(B\) into complementary subsets, applying one subset in the first permutation and its complement in the second. These, and only these, are the diametral pairs. Consequently, the numbers of unordered diametral pairs are
\[
 N_{\rm O}(n)=2^{\lfloor(n-1)/2\rfloor-1},\qquad
 N_{\rm E}(n)=2^{\lceil(n-1)/2\rceil-1}.
\]
The parity-induced difference is sharp: for every even \(n\ge4\), the two squared diameters differ by exactly \(2\), despite both polytopes having \(2^{n-1}\) vertices. Since the commuting first and second swap batches reverse under group inversion, \(c_{\rm E}=c_{\rm O}^{-1}\): this is a precise example of Euclidean diameter changing under inversion of a Coxeter element in the ordinary permutation-vector realization. No nonvertex point can participate in a diametral pair.

## Assumptions and scope
The index \(n\) ranges over all integers at least \(3\). Distances use the standard \(\ell_2\) metric on the one-line permutation vectors; no rescaling, inversion, or quotient metric is implicit. Multiplication of the transpositions is performed left-to-right as operations on the current list of entries, equivalently right multiplication in one-line notation.

The subword property of Bruhat order says that the elements of \([e,c]\) are precisely the products of subwords of a reduced word for \(c\). Each of the \(n-1\) simple reflections occurs once in either displayed word. Every subword is reduced, and two different subsets cannot have the same Coxeter support. Hence the interval has exactly \(2^{n-1}\) distinct elements. Every permutation vector is an extreme point of the ordinary permutohedron (for instance, a coordinate-ordering linear functional uniquely exposes it), so every one of these elements remains an extreme point in the smaller convex hull. The affine dimension is \(n-1\), since it contains \(e\) and the individual adjacent transpositions.

## Proof
**1. Two-coordinate bound.** Fix an integer \(t\) and four binary indicators \(a,b,A,B\). Consider a coordinate pair immediately before the second layer of disjoint adjacent swaps, first having entries
\[
 u=(t-a,t+1+b),\qquad v=(t-A,t+1+B).
\]
Each is then either left unchanged or reversed. When the two final reversal choices agree, the squared distance on this coordinate pair is \((a-A)^2+(b-B)^2\le2\). When they disagree, after interchanging the two points if necessary, the squared distance is
\[
 (1+a+B)^2+(1+b+A)^2\le18.
\]
Equality \(18\) holds **if and only if** \(a=b=A=B=1\) and the two reversal choices disagree. If at least one of \(a\ne A\) and \(b\ne B\) occurs, the squared distance is at most \(13\): in the disagreeing case one of the two squared summands is at most \(4\), while the other is at most \(9\). If one of the neighboring first-layer indicators is identically \(0\) in both permutations, the corresponding bound is instead \(8\), with equality exactly when the other neighboring indicator equals \(1\) in both permutations and the reversal choices disagree. In that boundary case a discrepancy in the remaining first-layer indicator lowers the pair's bound to \(5\). These are elementary integer inequalities, not experimental assertions.

**2. Odd transpositions first, odd \(n\).** Put \(n=2m+1\). Write \(a_j\in\{0,1\}\) for whether first-layer swap \(s_{2j-1}\) is used, and \(b_j\) for whether second-layer swap \(s_{2j}\) is used (\(1\le j\le m\)); write capitals for the second permutation. After the first layer, the entries at positions \(2j,2j+1\) are \((2j-a_j,2j+1+a_{j+1})\), defining \(a_{m+1}=0\). The entry at position \(1\) is \(1+a_1\). The full squared distance is the sum of the singleton contribution \((a_1-A_1)^2\), of \(m-1\) inner-pair contributions bounded by \(18\), and of the last boundary pair bounded by \(8\). The singleton can never increase the resulting bound: if \(a_1\ne A_1\), the first inner-pair contribution drops from at most \(18\) to at most \(13\) (or, when \(m=1\), the only boundary-pair contribution drops from at most \(8\) to at most \(5\)). Hence
\[
 \|p-q\|_2^2\le18(m-1)+8=9n-19.
\]
Equality forces every inner pair to attain \(18\), the last pair to attain \(8\), and \(a_1=A_1\). Thus every first-layer indicator in both permutations is \(1\), and all \(m\) second-layer indicators are complementary. Conversely these choices attain the bound.

**3. Odd transpositions first, even \(n\).** Put \(n=2m\), where \(m\ge2\). The first-layer swaps are \(s_{2j-1}\) for \(1\le j\le m\) and the second-layer swaps are \(s_{2j}\) for \(1\le j<m\). The endpoints, at positions \(1\) and \(2m\), contribute respectively \((a_1-A_1)^2\) and \((a_m-A_m)^2\), while each of the \(m-1\) interior pairs has contribution at most \(18\). Any nonzero endpoint contribution forces its adjacent interior pair to lose at least \(5\), more than compensating even if both endpoint indicators differ and \(m=2\). Therefore
\[
 \|p-q\|_2^2\le18(m-1)=9n-18.
\]
Equality holds precisely when every first-layer indicator is \(1\) in both permutations and the \(m-1\) second-layer indicators are complementary.

**4. Even transpositions first, even \(n\).** Put \(n=2m\) and let first-layer indicators \(a_1,\ldots,a_{m-1}\) correspond to \(s_2,s_4,\ldots,s_{2m-2}\). Define the boundary values \(a_0=a_m=0\). The second-layer swaps are \(s_{2j-1}\) for \(1\le j\le m\). Just before them, positions \((2j-1,2j)\) contain \((2j-1-a_{j-1},2j+a_j)\). Thus the first and last pairs have squared-distance bounds \(8\), and the intervening \(m-2\) pairs have bounds \(18\). It follows that
\[
 \|p-q\|_2^2\le 16+18(m-2)=9n-20.
\]
All bounds are met simultaneously if and only if every first-layer indicator is \(1\) in both permutations and the \(m\) second-layer indicators are complementary.

**5. Even transpositions first, odd \(n\).** Put \(n=2m+1\). First-layer swaps \(s_{2j}\) have indicators \(a_1,\ldots,a_m\), with \(a_0=0\). Second-layer swaps \(s_{2j-1}\) produce coordinate pairs \((2j-1,2j)\) for \(1\le j\le m\). The first pair contributes at most \(8\), and the remaining \(m-1\) pairs each at most \(18\); the last unpaired coordinate is \(2m+1-a_m\). If \(a_m\ne A_m\), the last paired block drops by at least \(5\) (or the first boundary pair by at least \(3\) if \(m=1\)), absorbing the possible singleton contribution of \(1\). Thus
\[
 \|p-q\|_2^2\le8+18(m-1)=9n-19.
\]
Equality occurs precisely for all first-layer indicators equal to \(1\) in both permutations and complementary choices of all \(m\) second-layer swaps.

**6. Pair counts and continuous extremizers.** Each first-layer choice is forced. If the second layer contains \(b\) disjoint swaps, choosing an arbitrary subset for the first permutation forces the complement for the second; swapping the two permutations identifies exactly two of the \(2^b\) choices. Hence there are \(2^{b-1}\) *unordered* pairs, yielding both stated enumerations.

Finally, for fixed \(y\), the function \(x\mapsto\|x-y\|_2^2\) is strictly convex. An interior point of a nontrivial segment in either polytope cannot maximize this function because its value is strictly below the corresponding convex combination of endpoint values. Thus both entries of any diametral pair must be vertices, so the vertex classification is complete. This finishes the proof for every allowed \(n\).

## Verification
The standalone `check.py` can be executed with Python 3 using no additional packages. It verifies the complete two-coordinate inequalities on all binary cases; enumerates every vertex and all unordered vertex pairs for both orientations for every \(3\le n\le10\), matching not only the diameter but the *exact set* of predicted pairs; and tests larger orders through \(n=201\), including explicit sharpness witnesses. Expected output:

```text
ZIGZAG_BRUHAT_DIAMETER_PASS local_cases=80 exhaustive_n=3..10 orientations=2 vertex_pairs=348500 random_pairs=4800
```

This finite verification is supplementary: the all-order claim and equality classification follow from the coordinate-pair proof above. The tests do not establish that every unindexed source has been searched.

## Relationship to prior work
Bruhat interval polytopes in the ordinary one-line convention were introduced and systematically studied by Tsukerman and Williams; their Theorem 4.24 gives the **combinatorial graph diameter** \(\ell(v)-\ell(u)\), proved by counting 1-skeleton paths, and is not a statement about the extrinsic Euclidean distance between coordinate vectors. In particular, it yields \(n-1\) for every \(Q_{n,c}\) here, independently of which zigzag orientation is chosen. Gaetz established lattice and simplicity-related properties of the 1-skeleton in 2022/2023, using the inverse-permutation vector convention; these are not Euclidean diameter formulas for the ordinary convention fixed here. Knutson, Sanchez and Sherman-Bennett used Coxeter elements to index permutahedral subdivisions and identified zigzag elements in their extremal subdivision census; their 2025 extended abstract does not give the above Euclidean diameter or diametral-pair classification.

The key new metric distinction is that the squared Euclidean diameter is orientation-sensitive for even \(n\), even between inverse Coxeter elements, although both intervals have the same number of vertices and the same combinatorial graph diameter. The exact diametral graph is a matching on a distinguished subset of vertices, in a polytope with exponentially many vertices. Searches of accessible mathematical literature and research records found no stronger known statement implying these formulas; this is not a guarantee of historical priority.

## Limitations
Only the two *alternating* Coxeter orientations are covered, not arbitrary Coxeter elements or general Bruhat intervals. We do not claim a classification of their face lattices, and do not infer combinatorial equivalence from their equal vertex counts. Euclidean results are coordinate-convention dependent: replacing each \(w\) by \(w^{-1}\) is not generally a Euclidean isometry of the vertex set. The cited 2014 article and 2025 subdivision study are background and novelty comparisons; the dated 2022 literature lead is Gaetz's preprint. Historical priority remains provisional. There has been no independent audit.

## References
1. C. Gaetz, *One-skeleton posets of Bruhat interval polytopes*, arXiv:2208.13826 (first posted 2022-08-29), *Advances in Mathematics* **430** (2023), 109216. https://arxiv.org/html/2208.13826v3
2. E. Tsukerman and L. Williams, *Bruhat Interval Polytopes*, arXiv:1406.5202 (first posted 2014-06-19), *Advances in Mathematics* **285** (2015), 766–810; particularly Section 4.4 and Theorem 4.24. https://arxiv.org/abs/1406.5202
3. A. Knutson, M. Sanchez and M. Sherman-Bennett, *Permutahedral subdivisions and class formulas from Coxeter elements*, *Séminaire Lotharingien de Combinatoire* **93B** (2025), article 8; particularly Definitions 2.1 and 2.3 and Examples 2.17. https://www.mat.univie.ac.at/~slc/wpapers/FPSAC2025/8.pdf
