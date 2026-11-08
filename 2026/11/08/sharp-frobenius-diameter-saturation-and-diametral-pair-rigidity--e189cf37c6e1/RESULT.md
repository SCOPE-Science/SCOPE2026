# Sharp Frobenius diameter saturation and diametral-pair rigidity of partial alternating-sign-matrix polytopes

## Finding

For all positive integers \(m,n\), put \(s=\min(m,n)\) and \(t=\max(m,n)\). The polytope \(\mathrm{PASM}(m,n)\) is the convex hull of the rectangular partial alternating-sign matrices in \(\mathbb R^{m\times n}\). Its Frobenius diameter satisfies

\[
\operatorname{diam}_F(\mathrm{PASM}(m,n))^2\le 2s(2s-1).
\]

**The sharp saturation and rigidity theorem** states that equality holds precisely when \(t\ge 2s\). In that regime, the number of unordered diameter-realizing vertex pairs is **exactly**

\[
\binom{t}{2s},
\]

and all such pairs are the explicitly defined staggered alternating-diamond pairs below, up to transposition and interchanging the endpoints. The bound is strict when \(t<2s\); no exact subthreshold diameter is asserted.

## Assumptions and scope

An \(m\times n\) partial alternating-sign matrix \(M=(M_{ij})\) has entries in \(\{-1,0,1\}\), and for every \(1\le i\le m\), \(1\le j\le n\), the initial row and column sums satisfy

\[
\sum_{k=1}^{j}M_{ik}\in\{0,1\},\qquad
\sum_{h=1}^{i}M_{hj}\in\{0,1\}.
\]

The Frobenius norm and the ambient Euclidean distance are identical:
\(\|M\|_F^2=\sum_{i,j}M_{ij}^2\). Every such matrix is a vertex of its convex hull, by Heuer–Striker, Proposition 4.3 [1]; no additional vertex types occur. The aspect ratio and all size parameters in this theorem are **integer**, with no lower restriction other than positivity.

For an explicit equality pair when \(m\le n\) and \(n\ge2m\), choose any \(2m\) columns
\(1\le c_1<\cdots<c_{2m}\le n\). For every row \(1\le i\le m\) and integer \(0\le h\le2i-2\), place

\[
A_{i,c_{m-i+1+h}}=(-1)^h,\qquad
B_{i,c_{m-i+2+h}}=(-1)^h,
\]

and set all unlisted entries of \(A,B\) to zero. This description applies in the first and last rows, including the case \(m=1\). For \(m>n\), transpose the corresponding \(n\times m\) construction.

## Proof

**1. A sharp universal quadratic bound.** By transpose symmetry assume \(m\le n\). For any partial alternating-sign matrix \(M\), write \(q_i\) for the number of negative entries in row \(i\), and \(\sigma_i\in\{0,1\}\) for its final row sum. Alternation of the binary horizontal partial sums implies the row has \(q_i+\sigma_i\) positive entries. Immediately above row \(i\), the binary column partial sums contain exactly \(\sum_{h<i}\sigma_h\le i-1\) ones. A negative entry in row \(i\) is possible only at one of these positions. Consequently

\[
q_i\le i-1,\qquad
\|M\|_F^2=\sum_{i=1}^{m}(2q_i+\sigma_i)\le m^2,
\]

and the total number of negative entries in \(M\) is at most \(m(m-1)/2\).

For two such matrices \(M,N\), every negative summand in their Frobenius inner product \(\langle M,N\rangle\) uses a negative entry from one of them, and each negative entry contributes at most once. Thus

\[
\langle M,N\rangle\ge-\bigl(q(M)+q(N)\bigr)\ge-m(m-1).
\]

It follows that

\[
\|M-N\|_F^2=\|M\|_F^2+\|N\|_F^2-2\langle M,N\rangle
\le2m^2+2m(m-1)=2m(2m-1).
\]

A convex combination cannot have greater distance than the greatest distance between generating vertices (apply the triangle inequality twice), hence this also bounds the entire polytope.

**2. Equality constraints.** If a pair attains the upper bound, equality in all estimates forces, for each row of each matrix,

\[
q_i=i-1,\qquad\sigma_i=1.
\]

In addition, **every** negative entry of \(M\) overlaps a positive entry of \(N\), and conversely, while no two positive entries overlap. In particular, a negative entry never coincides with a negative or a zero in the other matrix. Each row has \(i\) positives and \(i-1\) negatives, strictly alternating with positive endpoints.

**3. The bottom-row alternating word and the sharp aspect-ratio obstruction.** In the last row each matrix has \(m\) positive entries. The two positive supports are disjoint, so their union has precisely \(2m\) columns. All their negative entries occur at columns belonging to the other positive support. At each of these \(2m\) columns, the pair of row entries is one of \((1,0),(0,1),(1,-1),(-1,1)\). There are exactly two unmatched positives and \(2m-2\) opposite-sign overlaps.

Consider the running **sum of the two horizontal row prefixes**. Each individual prefix is binary, and the only increments in their sum are the two unmatched positives. Initially the sum is zero and finally it is two. An opposite-sign overlap is impossible when both prefixes are zero or when both are one; hence every overlap lies strictly between the two unmatched positives. Between those columns, exactly one prefix is one, and the overlapping signs must toggle which matrix has prefix one. Thus the \(2m\) selected columns, in increasing order, are necessarily the two one-position-staggered alternating words:

\[
(1,-1,1,-1,\ldots,1,0),\qquad
(0,1,-1,1,\ldots,-1,1),
\]

or the reversed assignment of these two words. In particular, \(n\ge2m\) is **necessary** for equality.

**4. Backward-row rigidity.** In an equality matrix, let \(P_i(M)\) be the set of its \(i\) positive-entry columns in row \(i\). Because the first \(i-1\) row sums all equal one, precisely \(i-1\) column partial sums just above row \(i\) are one. The \(i-1\) negative entries of row \(i\) exhaust exactly those positions. They therefore coincide with \(P_{i-1}(M)\). Equivalently, \(P_{i-1}(M)\) consists of the unique negative entry strictly between each pair of successive positives from \(P_i(M)\). The same holds for \(N\).

The equality-overlap constraints give \(P_{i-1}(M)\subset P_i(N)\) and \(P_{i-1}(N)\subset P_i(M)\). As proved in step 3, the bottom positives occur in strictly alternating column order. Hence in every gap between successive positives of \(P_m(M)\) there is precisely one positive of \(P_m(N)\). The unique possible negative at that gap is this positive, and conversely. Therefore row \(m-1\) is uniquely determined and has exactly the proposed staggered pattern. Inductively the same argument uniquely determines every earlier row. This proves that **no other equality pairs exist**.

**5. Existence and counting.** For any selection \(c_1<\cdots<c_{2m}\), the matrices defined above have alternating horizontal partial sums. Their vertical partial sums are also binary: after row \(i\), the columns carrying a vertical one are exactly the \(i\) positive positions of that row, and these are discharged by negative entries in row \(i+1\). Thus both matrices are valid. Their squared distance, row by row, is

\[
\sum_{i=1}^{m}\bigl(2\cdot4(i-1)+2\bigr)
=\sum_{i=1}^{m}(8i-6)=2m(2m-1).
\]

There is exactly one **unordered** pair per increasing \(2m\)-column selection: swapping its endpoints exchanges the two possible stagger directions. Conversely, the bottom-row positive-support union recovers the selected columns uniquely from each diameter pair. Therefore the count is \(\binom{n}{2m}\). Transposition gives the stated result for all \(m,n\).

Because the squared Euclidean distance is strictly convex separately in each endpoint, a maximizing pair of arbitrary points of the polytope must consist of vertices; thus the classification covers every diameter-realizing pair.

## Verification

The standalone checker `verify_pasm_diameter.py` independently constructs all admissible matrices from binary column-prefix states in small sizes, checks both types of prefix constraints, and exhaustively computes the maximum squared vertex distance and the number of maximizing pairs in specified cases. It confirms the threshold in all tested sizes through three rows and six columns. In particular, the maximizing-pair multiplicities at size \((2,4),(2,5),(2,6),(3,6)\) are \(1,5,15,1\), respectively. It also verifies 1,626 explicit alternating-diamond constructions across sizes through seven rows, and their transposes. All checks use integer arithmetic. Run with `python verify_pasm_diameter.py` using a standard Python interpreter. These finite checks are supplementary; the five-step proof above is all-dimensional.

## Relationship to prior work

Heuer and Striker [1] introduced \(\mathrm{PASM}(m,n)\), established its exact vertices, inequalities, face lattice, and facet numbers, and studied its projection to partial permutohedra. The diameter theorem here uses their object and vertex result but does not follow from the facial or projection results: the projection is not a Frobenius isometry. Heuer, Solhjem, and Striker [2] analyze particular faces as order and flow polytopes, not the full ambient diameter. Behrend and collaborators [3] investigate partial permutohedra themselves (their faces and enumerative invariants). The checked materials do not state the aspect-ratio threshold or classification of the Frobenius-extremal signed-matrix pairs. Historical priority remains provisional, especially under alternative sign-restricted-matrix terminology.

## Limitations

The theorem does **not** give the exact diameter when \(t<2s\): it proves that the universal upper bound is strict there. It applies only to the standard ambient Frobenius metric and ordinary partial alternating-sign matrices, not arbitrary affine realizations or higher-spin variants. Exhaustive computations cover only finite small parameters. No independent mathematical audit has been performed.

## References

[1] D. Heuer and J. Striker, *Partial permutation and alternating sign matrix polytopes*, arXiv:2012.09901, initially public December 17, 2020; later SIAM J. Discrete Math. 36 (2022), 2863–2888. https://arxiv.org/abs/2012.09901

[2] D. Heuer, S. Solhjem, and J. Striker, *On nu faces of partial alternating sign matrix polytopes*, arXiv:2403.02204, initially public March 4, 2024. https://arxiv.org/abs/2403.02204

[3] R. E. Behrend, F. Castillo, A. Chavez, A. Diaz-Lopez, L. Escobar, P. E. Harris, and E. Insko, *Partial permutohedra*, arXiv:2207.14253, initially public July 28, 2022. https://arxiv.org/abs/2207.14253
