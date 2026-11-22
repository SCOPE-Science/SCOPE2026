# A nine-by-nine support face defeats full-affine bistochastic projection stability

## Finding
Let \(\mathcal B_9\) be the convex set of real \(9\times9\) nonnegative matrices with all row and column sums equal to one. Write \(\Pi\) for nearest-point projection onto \(\mathcal B_9\) in Frobenius distance, and measure perturbations by \(\|X\|_{\max}=\max_{i,j}|X_{ij}|\). Then
\[
\operatorname{Lip}_{\max}(\Pi)\ \ge\ \frac{13394263}{4220481}\ >\ \frac{256}{81}\ =\ \operatorname{Lip}_{\max}(\Pi_{\rm aff}),
\]
where \(\Pi_{\rm aff}\) is orthogonal projection onto the unrestricted affine space of matrices with unit row and column sums. The strict inequality is witnessed by two distinct explicit matrices whose projections lie on one proper face of \(\mathcal B_9\). Consequently the full-support affine Jacobian does not give the global coordinatewise perturbation bound even at matrix order nine.

## Assumptions and scope
All matrices are real and indexed from one to nine. The matrix norm \(\|\cdot\|_{\max}\) is the largest absolute *entry*, not the induced matrix infinity norm. For any map \(F\), its global Lipschitz coefficient is the supremum of \(\|F(X)-F(Y)\|_{\max}/\|X-Y\|_{\max}\) over distinct inputs.

Define an edge support \(E\) in the nine-by-nine grid by the permitted columns in each successive row:

```
row 1: 1 2 4 6
row 2: 2 5 8 9
row 3: 2 3 5 6 7 9
row 4: 3 4 6 7 8
row 5: 1 2 8 9
row 6: 1 2 5 8
row 7: 2 4 6 7 9
row 8: 4 9
row 9: 1 3 5 7
```

These 38 entries are the support of the relative interior of a nonempty bistochastic face. A complete seven-permutation support cover, with each row giving the successive column positions of the nonzero entries in a permutation matrix, is

```
1 2 3 4 8 5 6 9 7
2 5 6 3 9 8 7 4 1
6 8 5 7 1 2 4 9 3
4 5 7 6 8 1 2 9 3
6 9 3 8 2 1 7 4 5
6 5 2 3 1 8 9 4 7
1 2 9 3 8 5 6 4 7
```

## Proof
First consider the affine projection with no nonnegativity conditions. Its linear part is the two-sided centering map \(H\mapsto CHC\), where \(C=I-J/9\) and \(J\) is the all-ones matrix. Every absolute row sum of its coefficient matrix is \((2-2/9)^2=256/81\), proving the quoted full-affine norm.

For the proper face with support \(E\), index its 38 coordinates in row-major order. Form the signed vertex-edge incidence matrix \(B\) of the bipartite support graph, retaining all nine row vertices and only the first eight column vertices. Thus the edge \((i,j)\) has a \(+1\) in row vertex \(i\), a \(-1\) in column vertex \(j\) if \(j\le8\), and no other nonzero incidence entries. The \(17\times17\) matrix \(BB^{\mathsf T}\) is nonsingular. The orthogonal tangent projector on supported entries is therefore
\[
Q=I_{38}-B^{\mathsf T}(BB^{\mathsf T})^{-1}B.
\]
An exact rational elimination gives the absolute row sum corresponding to support edge \((4,8)\):
\[
\sum_{f\in E}|Q_{(4,8),f}|=\frac{13394263}{4220481},
\qquad
\frac{13394263}{4220481}-\frac{256}{81}=\frac{1497389}{113952987}>0.
\]
These are rational identities, not numerical approximations. The file `verify.py` independently reconstructs the incidence matrix and elimination and checks each identity using exact fractions.

For finite-input realization, let \(X_0\) be the mean of the seven permutation matrices listed above; every entry of \(X_0\) on \(E\) is strictly positive, and every entry outside \(E\) vanishes. Set \(N_{ij}=1\) for entries outside \(E\) and \(N_{ij}=0\) on \(E\), and define \(G_0=X_0-N\). The normal-cone inequality gives \(\Pi(G_0)=X_0\).

Let \(H\) equal the entrywise sign of the target row of \(Q\) on \(E\), and zero outside \(E\). Set \(\varepsilon=10^{-6}\), \(G_1=G_0+\varepsilon H\), and \(X_1=X_0+\varepsilon QH\), with \(QH\) extended by zero off \(E\). Exact rational tests in `verify.py` show that \(X_1\) is bistochastic, is strictly positive on the same support, and has strictly positive dual normal slacks off the support. Indeed, solving \((BB^{\mathsf T})u=BH_E\) gives row-column multipliers; the off-support normal slacks are \(1+\varepsilon b_{ij}^{\mathsf T}u>0\), where \(b_{ij}\) is the truncated signed incidence column for any grid position. The KKT conditions thus give \(\Pi(G_1)=X_1\).

The two inputs differ by maximum entry \(\varepsilon\), while the output difference at position \((4,8)\) is precisely \(\varepsilon\cdot13394263/4220481\). This proves the claimed global lower bound and its strict comparison with full-affine stability.

## Verification
Run `python verify.py` with Python 3; it uses only the standard-library `fractions` module. It checks support coverage by seven permutation matrices, the nonsingular exact incidence solve, the rational tangent-row norm and strict excess, all row and column sums of the second projected matrix, strict positivity on the support, and strict off-support dual slacks for the two finite inputs. These finite exact algebraic checks substantiate the particular witness; no exhaustive face classification is claimed.

## Relationship to prior work
Li, Sun and Toh (2017) give a generalized-Jacobian construction for Frobenius projection onto the Birkhoff polytope. Its incidence/active-constraint principle underlies the argument, but the specific nine-by-nine witness and its strict maximum-entry comparison are not stated in the inspected primary text. Publicly indexed mathematical records previously exhibited a three-block support with a strict obstruction at order twelve and reported exact full-affine sharpness at orders two, three and four. This finding supplies a strictly smaller explicit obstruction at order nine. The linked records were available as searchable descriptions but their full texts were not accessible during the comparison; this is a priority limitation, not a claim that the documents were exhaustively excluded.

## Limitations
The rational number is an attained *lower bound* on the global order-nine Lipschitz coefficient, not its exact global value. The smallest dimension at which a proper support face beats the full-affine norm is not determined; nothing is asserted for orders five through eight. The construction does not establish uniqueness or optimality of its support and does not classify higher matrix orders.

## References
- X. Li, D. Sun, K.-C. Toh, *On the efficient computation of a generalized Jacobian of the projector over the Birkhoff polytope* (first public version February 20, 2017), https://arxiv.org/abs/1702.05934.
- *A three-block face forces sharp coordinatewise instability in bistochastic least-squares projection*, public mathematical record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-a-three-block-face-forces-sharp-coordinatewise-instability-in-bi--0b9d63c07c36.
- *Small-order endpoint stability and a regular-face obstruction for Euclidean Birkhoff projection*, public mathematical record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-small-order-endpoint-stability-and-a-regular-face-obstruction-fo--94c6886725b7.
