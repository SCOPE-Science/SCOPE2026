# Heterogeneous partition-matroid deep holes encode number partitioning

## Finding
Let the ground set be the disjoint union of \(m\ge2\) labelled blocks \(E_i\) of sizes \(q_i\ge2\), with integers \(1\le c_i<q_i\). Set \(N=\sum_iq_i\), \(R=\sum_ic_i\), and let \(M=\bigoplus_{i=1}^m U_{c_i,q_i}\) be their partition matroid. In standard orthonormal coordinates, its base polytope and the containing rank-\(R\) hypersimplex are
\[
P=\prod_{i=1}^m\Delta(c_i,q_i)\subseteq H=\Delta(R,N)=\{x\in[0,1]^N:\sum_jx_j=R\}.
\]
For every block define the rational function on integers \(0\le j\le q_i\):
\[
\phi_i(j)=
\begin{cases}
(c_i-j)^2/(q_i-j),&0\le j\le c_i,\\
(j-c_i)^2/j,&c_i\le j\le q_i.
\end{cases}
\]
Both formulas give zero at \(j=c_i\); their denominators are nonzero on their stated ranges. For any hypersimplex vertex \(\mathbf1_S\), writing \(j_i=|S\cap E_i|\), its exact squared distance to \(P\) is \(\sum_i\phi_i(j_i)\).

**Compression theorem.** Every hypersimplex vertex maximizing this squared distance has at most one block whose occupancy lies strictly between zero and its block size. In particular, the exact squared Hausdorff distance is the following finite combinatorial maximum, with no continuous optimization:
\[
\boxed{
 d_H(H,P)^2=
 \max_{\substack{A\subseteq[m],\ t\in[m]\setminus A\\0\le R-\sum_{i\in A}q_i\le q_t}}
 \left[
 \sum_{i\in A}\phi_i(q_i)
 +\phi_t\!\left(R-\sum_{i\in A}q_i\right)
 +\sum_{i\notin A\cup\{t\}}\phi_i(0)
 \right].
}
\]
Here a candidate labels the blocks in \(A\) as full, the blocks outside \(A\cup\{t\}\) as empty, and the one exceptional block \(t\) as having the displayed occupancy. The formula permits an exceptional occupancy at an endpoint, so it also includes the all-endpoint case. If different candidates attain the maximum, all corresponding hypersimplex vertices are maximizers.

**Arithmetic threshold theorem.** In the natural balanced-within-each-block subfamily
\[
q_i=2a_i,\qquad c_i=a_i,\qquad a_i\in\mathbb Z_{>0},\qquad R=\sum_i a_i,
\]
one has the universal sharp bound
\[
\boxed{d_H(H,P)^2\le R/2.}
\]
Equality holds **if and only if** the multiset \((a_1,\ldots,a_m)\) can be partitioned into two equal-sum submultisets. In the equality case, the *entire* continuous farthest-point locus in \(H\) consists precisely of the hypersimplex vertices that select all coordinates in the blocks of one equal-sum subcollection and none in the others: no nonvertex point is farthest.

Consequently, from the positive integers \(a_i\) given in binary, the decision problem of whether this implicitly specified Euclidean Hausdorff squared distance equals \(R/2\) is **weakly NP-complete**. This complexity statement concerns the succinct block-size encoding, not an explicitly expanded list of \(N=2R\) ambient coordinates.

## Assumptions and scope
All coordinates have their ordinary unweighted Euclidean norm; no affine renormalization or intrinsic metric rescaling is used. There are \(m\ge2\) blocks, and every block has both positive rank and positive corank. The Hausdorff distance is \(\sup_{x\in H}\inf_{y\in P}\|x-y\|_2\), since \(P\subseteq H\). Its square appears throughout the displayed formulas. The complexity statement takes only the integer block parameters as input, in binary, and considers exact rational arithmetic. It does not claim strong NP-hardness or polynomial-time hardness under an explicitly enumerated vertex/coordinate representation.

## Proof
**1. Exact projection.** A partition-matroid basis selects exactly \(c_i\) elements in each \(E_i\), and its base polytope is the Cartesian product of the corresponding hypersimplices. Because the coordinate blocks are orthogonal, Euclidean projection onto \(P\) separates by block. For a binary vector with \(j\) ones in a block of size \(q\), rank \(c\):

If \(j\le c\), its projection retains value \(1\) on all selected coordinates and assigns \((c-j)/(q-j)\) to every unselected coordinate; the squared residual is \((c-j)^2/(q-j)\). If \(j\ge c\), its projection assigns \(c/j\) on the selected coordinates and zero elsewhere; the squared residual is \((j-c)^2/j\). In each case the candidate is in \(\Delta(c,q)\). The residual is zero on selected positions and nonpositive on unselected positions in the first case, or nonnegative on selected positions and zero on the others in the second; hence its linear support over \(\Delta(c,q)\) is attained at the proposed point. The characterization \((v-y)\cdot(z-y)\le0\) for every \(z\) in a convex set proves that this is its unique Euclidean projection. Orthogonality gives the asserted sum of the \(\phi_i\).

**2. Reduction to vertices.** The distance to any nonempty closed convex set is convex. Since \(H\) is the convex hull of its binary rank-\(R\) vertices, its maximum distance to \(P\) is attained at a vertex. Therefore its squared Hausdorff distance is the maximum of \(\sum_i\phi_i(j_i)\) over integers \(0\le j_i\le q_i\) satisfying \(\sum_i j_i=R\). All such occupancy tuples are realized by binary vertices.

**3. Strict occupancy compression.** Extend each \(\phi_i\) to its real domain \([0,q_i]\) by the same two formulas. On \((0,c_i)\) its second derivative is \(2(q_i-c_i)^2/(q_i-j)^3>0\); on \((c_i,q_i)\) its second derivative is \(2c_i^2/j^3>0\). The first derivatives from both sides equal zero at \(c_i\). Hence \(\phi_i\) is strictly convex on its entire interval. Suppose an integer maximizing occupancy tuple had two different strictly interior block occupancies \(j_i,j_l\). Both neighboring transfers \((j_i+1,j_l-1)\) and \((j_i-1,j_l+1)\) are feasible. Strict convexity of \(t\mapsto\phi_i(j_i+t)+\phi_l(j_l-t)\) implies that at least one transfer strictly increases the sum, a contradiction. Thus every maximizing tuple has all but at most one occupancy at its endpoints; enumerating precisely these tuples yields the compressed maximum formula.

**4. Sharp partition threshold.** Under \(q_i=2a_i\), \(c_i=a_i\), the two endpoint values of \(\phi_i\) both equal \(a_i/2\). Strict convexity gives \(\phi_i(j)<a_i/2\) for every interior \(j\). Summing shows that no hypersimplex vertex has distance squared above \(R/2\), and equality for a vertex requires each block to be entirely selected or entirely unselected. The total occupancy equals \(R\) exactly when the full blocks satisfy \(\sum_{i\in A}2a_i=\sum_i a_i\), which is exactly the equal-sum partition condition. Conversely each such partition produces a vertex at distance squared \(R/2\). This proves the bound and equivalence.

**5. All continuous equality cases.** For each equality vertex \(v\), let \(y_v\) be its nearest point and \(r_v=v-y_v\) its residual. In every block, \(r_v\) has all coordinates equal to \(+1/2\) for a full block or \(-1/2\) for an empty block. Distinct equality vertices therefore have distinct residual vectors of squared norm \(R/2\). For any convex combination \(x=\sum_v\lambda_vv\) of hypersimplex vertices, the point \(\sum_v\lambda_v y_v\) lies in \(P\), whence
\[
\operatorname{dist}(x,P)^2\le\left\|\sum_v\lambda_vr_v\right\|^2\le\sum_v\lambda_v\|r_v\|^2\le R/2.
\]
If any positive-weight vertex is not an equality vertex, the last inequality is strict. If two distinct equality vertices have positive weights, strict convexity of the squared norm makes the middle inequality strict because their residuals differ. Thus equality at \(x\) is possible only when \(x\) itself is one of the designated binary equality vertices.

**6. Complexity.** The classical PARTITION language on binary-encoded positive integers \(a_1,\ldots,a_m\) asks whether some submultiset sums to half the total. Map the input to the succinct block parameters \((q_i,c_i)=(2a_i,a_i)\). The map has polynomial binary description length. By Step 4 the resulting Hausdorff threshold equality holds exactly for yes-instances of PARTITION. A witnessing submultiset proves membership in NP, giving NP-completeness of this restricted decision language. The standard pseudo-polynomial subset-sum dynamic program applies, explaining the word *weakly*. No conclusion is drawn about an input that explicitly lists all \(N\) coordinates of the resulting polytope.

## Verification
Run `python3 hetero_checker.py` using Python 3 and no external packages. The script enumerates binary vertices and uses exact rational arithmetic, independently checks every proposed projection with a supporting-normal inequality, compares each exhaustive maximum with the compressed-candidate maximum, and tests the PARTITION equivalence on a finite collection of numerical inputs. The observed deterministic output is:

```
HETEROGENEOUS_COMPRESSION_PASS configurations=122 exact_vertices=38606 maximal_vertices=819
PARTITION_THRESHOLD_PASS instances=1360 yes_instances=591
```

All infinite-dimensional claims and the complexity reduction follow from the proof above, not from these finite tests. The finite checker is deliberately small enough to rerun on ordinary hardware.

## Relationship to prior work
Lasoń and Michałek, *Gorenstein matroids*, arXiv:2005.08359 (first public May 17, 2020), §2.2, Lemma 2.4, explicitly identify a direct-sum matroid base polytope as a Cartesian product. Aprile et al., *Slack matrices, \(k\)-products, and 2-level polytopes*, arXiv:2106.12829 (June 24, 2021), §4, investigate the product structure through slack matrices and recognition. Pineda-Villavicencio and Schröter, *Reconstructibility of matroid polytopes*, arXiv:2010.10227 (October 20, 2020), discuss combinatorial reconstruction and hypersimplex facial structure. These supply context and known product representations, not the heterogeneous Euclidean Hausdorff compression theorem or its exact PARTITION threshold.

The previously recorded equal-block result *An arithmetic deep-face resonance in balanced partition-matroid polytopes* determines the Euclidean extrema for identical block sizes and identical ranks. The present arbitrary heterogeneous result genuinely includes independent \(q_i,c_i\), and its binary-encoded decision threshold detects arbitrary numerical subsets; the fixed-equal-block formula does not imply the hardness claim. Other known appearances of PARTITION in polytope geometry concern different objects and metrics and are not treated as evidence of uniqueness.

## Limitations
Originality is assessed against the literature and accessible mathematical records actually compared; undiscovered equivalent presentations could alter priority. The exact compressed maximum may still require exponential enumeration of subset choices under binary encoding. No hardness assertion is made for explicitly expanded coordinates, and no quantitative approximation-hardness statement is proved. The theorem does not classify every nonvertex farthest point in the general unequal-rank, unequal-size case; it classifies all continuous farthest points only for the specified equality-threshold subfamily. Independent validation has not been performed.

## References
1. M. Lasoń and M. Michałek, *Gorenstein matroids* (formerly *On algebraic properties of matroid polytopes*), arXiv:2005.08359, first version May 17, 2020. https://arxiv.org/abs/2005.08359
2. M. Aprile, M. Conforti, Y. Faenza, S. Fiorini, T. Huynh and M. Macchia, *Slack matrices, \(k\)-products, and 2-level polytopes*, arXiv:2106.12829, June 24, 2021. https://arxiv.org/abs/2106.12829
3. G. Pineda-Villavicencio and B. Schröter, *Reconstructibility of matroid polytopes*, arXiv:2010.10227, October 20, 2020. https://arxiv.org/abs/2010.10227
4. The classical PARTITION decision problem and its standard weak NP-completeness and pseudo-polynomial subset-sum algorithm; see M. Garey and D. Johnson, *Computers and Intractability*, 1979, problem SP12.
