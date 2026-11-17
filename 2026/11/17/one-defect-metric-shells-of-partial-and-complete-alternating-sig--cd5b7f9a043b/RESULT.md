# One-defect metric shells of partial and complete alternating-sign-matrix polytopes

## Finding

Let \(\mathcal R_{m,n}\) denote the polytope of real nonnegative \(m\times n\) matrices with every row and column sum at most one (the convex hull of partial-permutation matrices). For an \(m\times n\) partial alternating sign matrix \(A\) with exactly one negative entry, let \(a\) and \(b\) be the numbers of its positive entries in the row and column containing that entry. Then \(a,b\in\{1,2\}\), and
\[
\operatorname{dist}_F(A,\mathcal R_{m,n})^2=\frac{a+b}{2}.
\]
The unique closest point is obtained by setting the negative entry to zero and, for each of the two affected lines that has two positive entries, replacing both of those positive entries by \(1/2\); all other entries remain unchanged. This is a complete three-shell classification for one-negative partial alternating sign matrices: the squared distances are \(1\), \(3/2\), and \(2\).

Let \(\mathcal B_n\) be the Birkhoff polytope of nonnegative doubly stochastic \(n\times n\) matrices. For every complete alternating sign matrix \(A\) of order \(n\ge3\) with exactly one negative entry,
\[
\operatorname{dist}_F(A,\mathcal B_n)^2=2+\frac{2}{n+5}.
\]
There are exactly \(\binom{n}{3}^2(n-3)!\) such matrices. Every one has the same squared distance to \(\mathcal B_n\), although the nearest point differs with the combinatorial position of its defect. The additional full-row/full-column completion cost over the four-arm partial case is exactly \(2/(n+5)\). The projected matrix has positive entries linking the defect's two outer rows and columns with every one of the other \(n-3\) matched rows and columns.

## Assumptions and scope

A partial alternating sign matrix means a matrix with entries in \(\{-1,0,1\}\), each prefix sum along every row and column in \(\{0,1\}\). Its final row and column sums may be zero. A complete alternating sign matrix has final row and column sums one. Distances are ordinary ambient Frobenius distances, not combinatorial graph distances or distances between vertices alone. The statements concern **every** one-negative partial matrix for all \(m,n\ge2\) for which such a matrix exists, and **every** one-negative complete matrix for all \(n\ge3\). No claim is made about the farthest vertex of the entire alternating-sign-matrix polytope or about matrices with multiple negative entries.

## Proof

**1. Partial-matrix classification.** Let the unique negative entry occupy position \((r,c)\). Prefix-sum admissibility forces a positive entry earlier in its row and column. With no other negative entry, there can be at most one further positive entry later in either of those lines. Consequently the counts \(a,b\) both belong to \(\{1,2\}\), and every other row and column has at most one positive entry.

For any \(Y\in\mathcal R_{m,n}\), put \(\delta=Y_{rc}+1\ge1\). The squared contribution of the negative position to \(\|Y-A\|_F^2\) is \(\delta^2\). If the affected row has two positive entries, its total in \(A\) equals one. Since the corresponding row of \(Y\) is nonnegative and sums to at most one, the sum of the two positive-position changes is at most \(-\delta\). Cauchy–Schwarz therefore forces their squared changes to sum to at least \(\delta^2/2\). If that row has only one positive entry, no additional estimate is needed. The identical argument applies to a two-positive affected column; its positive positions are distinct from the row's positive positions. Thus
\[
\|Y-A\|_F^2\ge \delta^2\left(1+\frac{a-1}{2}+\frac{b-1}{2}\right)\ge\frac{a+b}{2}.
\]
Construct \(Y_*\) by setting the negative entry to zero; in each affected line with two positives replace them by \(1/2\); leave every other entry unchanged. The affected row and column then have total one. All other rows and columns have total zero, one-half, or one. Hence \(Y_*\in\mathcal R_{m,n}\), and direct subtraction gives \(\|Y_*-A\|_F^2=(a+b)/2\). Since the squared Frobenius objective is strictly convex, the projection is unique.

**2. Reduction of a complete matrix.** When all final row and column sums are one, both affected lines must contain exactly two positive entries. The remaining positive entries form a permutation matching on the other \(n-3\) rows and columns. Independently permuting rows and columns puts any such \(A\) in the form
\[
D\oplus I_{n-3},\qquad D=\begin{pmatrix}0&1&0\\1&-1&1\\0&1&0\end{pmatrix}.
\]
Row and column permutations preserve both Frobenius distance and the Birkhoff polytope, so this canonical form suffices.

**3. Explicit full projection.** Put \(s=n+5\). In the canonical coordinates define a symmetric \(n\times n\) matrix \(X\) by these exhaustive entry rules: the four \(3\times3\) corner entries indexed by \(\{1,3\}\times\{1,3\}\) equal \(2/s\); the four arms \((1,2),(2,1),(2,3),(3,2)\) equal \(1/2\); the center \((2,2)\) equals zero; for each \(j\ge4\), the diagonal entry \((j,j)\) equals \(1-1/s\), while its four cross entries \((1,j),(3,j),(j,1),(j,3)\) equal \(1/(2s)\). All other entries are zero.

Every row and column has sum one: each outer core row totals \(4/s+1/2+(n-3)/(2s)=1\), the middle core row totals one, and every external row totals \(1-1/s+1/s=1\). Therefore \(X\in\mathcal B_n\).

Define the potential vector \(h\in\mathbb R^n\) by
\[
h_1=h_3=-\frac1s,\qquad h_2=\frac12+\frac1s,\qquad h_j=\frac1{2s}\quad(4\le j\le n).
\]
A case-by-case evaluation of the entry rules gives
\[
X_{ij}=\max\{A_{ij}-h_i-h_j,0\}\quad\text{for every }i,j.
\]
For an arbitrary doubly stochastic \(Y\), at positive entries of \(X\) the relation \(X_{ij}-A_{ij}=-h_i-h_j\) holds, while at zero entries it gives \(X_{ij}-A_{ij}\ge-h_i-h_j\). Using \(Y_{ij}\ge0\), the row and column sum equalities and the Frobenius inner product,
\[
\langle X-A,Y-X\rangle\ge-\sum_{i,j}(h_i+h_j)(Y_{ij}-X_{ij})=0.
\]
Consequently
\[
\|Y-A\|_F^2-\|X-A\|_F^2=\|Y-X\|_F^2+2\langle X-A,Y-X\rangle\ge\|Y-X\|_F^2.
\]
This proves that \(X\) is the unique Euclidean projection, including the boundary case \(n=3\), where the external block is empty.

**4. Exact distance and shell count.** The squared differences contribute one from the central negative entry, one from four half-size arm changes, \(16/s^2\) from four core corners, \((n-3)/s^2\) from the external diagonals, and another \((n-3)/s^2\) from their four cross entries. Hence
\[
\|X-A\|_F^2=2+\frac{16+2(n-3)}{s^2}=2+\frac2{n+5}.
\]
For the enumeration choose the three rows containing the defect's positive and negative core positions, choose the three corresponding columns, and then assign a permutation matching on the remaining \(n-3\) rows and columns. The sorted order within each selected triple forces the alternating-sign core uniquely, so the count is \(\binom n3^2(n-3)!\), without overcounting.

## Verification

The included `scripts/verify_one_defect.py` uses exact rational arithmetic to check the full projection certificate for every order from three through fifty, thirty-six rectangular four-arm instances, and all one-negative partial alternating sign matrices in seven small rectangular sizes. Its independent transfer enumeration checks all complete alternating sign matrices of orders three, four, and five and their one-negative classifications. The optional `scripts/independent_qp.py` uses numerical constrained quadratic optimization to check seven complete-matrix orders and fourteen partial-matrix instances, independently of the displayed potential formula. Their successful actual execution outputs are recorded in `VERIFICATION.md`. These are finite cross-checks; the unrestricted assertions follow from the proof above.

## Relationship to prior work

Heuer and Striker introduced and studied partial alternating-sign-matrix polytopes and partial-permutation polytopes in the 2020 preprint arXiv:2012.09901, establishing the matrix and polytope descriptions used here. Striker's earlier standard alternating-sign-matrix polytope work (arXiv:0705.0998) establishes the relevant convex-hull context and Birkhoff inclusion. O'Brien and Quinlan (2022) investigate alternating sign matrices with one or more negative entries under multiplicative-order constraints, but not this metric projection. General bistochastic projection theory supplies the convex optimization framework, not the stated closed-form one-defect distance shells. The present result is a concrete pointwise Euclidean projection and exact metric-shell statement rather than a facet count, polytope diameter, or inradius.

## Limitations

The classification requires exactly one negative entry; for more negative entries the simple row/column defect certificates can interact. The result does not identify the global Hausdorff distance between the entire alternating-sign-matrix polytope and the Birkhoff polytope. Neither the small-order enumerations nor numerical quadratic programs certify historical priority. Earlier equivalent statements in the matrix-nearness literature remain possible; independent mathematical and bibliographic reviews have not been conducted.

## References

1. D. Heuer and J. Striker, *Partial permutation and alternating sign matrix polytopes*, arXiv:2012.09901 (first posted 2020-12-17); later *SIAM Journal on Discrete Mathematics* 36 (2022), 2863–2888. https://arxiv.org/abs/2012.09901
2. J. Striker, *The alternating sign matrix polytope*, arXiv:0705.0998 (2007); *Electronic Journal of Combinatorics* 16 (2009), R41. https://arxiv.org/abs/0705.0998
3. C. O'Brien and R. Quinlan, *Alternating sign matrices of finite multiplicative order*, *Linear Algebra and Its Applications* 651 (2022), 332–358. https://doi.org/10.1016/j.laa.2022.06.001
