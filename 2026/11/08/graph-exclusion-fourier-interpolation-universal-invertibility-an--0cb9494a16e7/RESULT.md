# Exact inverse zero patterns for graph-exclusion Fourier matrices

## Finding

Let \(G=(V,E)\) be a finite simple graph and \(A\) a finite abelian group of order \(q\ge2\), with a symmetric perfect bicharacter \(b\). Index the unnormalized matrix \(H_G(x,y)=\prod_{v\in V}b(x_v,y_v)\) by assignments whose nonidentity support is an independent set of \(G\). Then \(H_G\) is invertible. Write \(U=\operatorname{supp}(x)\cup\operatorname{supp}(y)\). Its inverse has the following exact zero patterns:

- For \(q\ge3\), \((H_G^{-1})(x,y)=0\) if and only if \(U\) is not independent. In particular, the submatrix on assignments with a fixed nonidentity label at exactly one vertex recovers the adjacency relation from its off-diagonal zeros.
- For \(q=2\) and the path \(P_n\), there are the forced zeros when \(U\) is not independent. For independent \(U\), \((H_G^{-1})(x,y)=0\) if and only if at least one component of \(P_n-N[U]\) has a number of vertices congruent to \(2\pmod 4\). At the pair of all-zero assignments, this condition is \(n\equiv2\pmod4\).

The common calculation is an exact entry formula. Let \(N[U]\) be the union of \(U\) and its neighbors, and \(I_J(t)=\sum_{S\text{ independent in }J}t^{|S|}\), including the empty set. Then
\[
(H_G^{-1})(x,y)=
\begin{cases}
0, & U\text{ not independent},\\
q^{-|U|}\overline{H_G(x,y)}\,I_{G-N[U]}(-(q-1)/q), & U\text{ independent}.
\end{cases}
\tag{1}
\]
Thus for a compatible support pair, zero or nonzero is determined by a residual independence polynomial, not by the individual labels. For comparison, the same block factorization gives \(|\det H_G|=q^{(q/2)I_G'(q-1)}\).

## Assumptions and scope

The graph is undirected and may have empty vertex set. Identity coordinates are written \(0\). Perfect means \(a\mapsto b(a,\cdot)\) identifies \(A\) with its character group, and symmetric means \(b(a,c)=b(c,a)\). Such a bicharacter exists for every finite abelian group by cyclic decomposition. The binary path law uses the unique perfect bicharacter \((-1)^{ac}\) on the group of order two. No classification of binary cancellations for arbitrary graphs beyond (1) is asserted.

## Proof

**Block calculation.** Let \(B\) be the nonzero-label submatrix of the one-coordinate table \(W\), let \(J\) be the all-ones matrix of size \(q-1\), and put \(K=B-J\). Character orthogonality and symmetry give \(W^{-1}=q^{-1}\overline W\). Since \(K\) is the Schur complement of the upper-left entry \(1\), \(K^{-1}=q^{-1}\overline B\). Subtracting the first row of \(W\) from all the others gives \(\det W=\det K\); all singular values of \(W\) are \(\sqrt q\), so \(|\det K|=q^{q/2}\).

Order assignments by coordinate restriction: \(z\preceq x\) means that every nonzero coordinate of \(z\) agrees with \(x\). For allowed assignments define \(Z(x,z)=\mathbf1_{z\preceq x}\). It is unitriangular in an order by support size. Let \(D\) be block diagonal by independent supports, with block \(K^{\otimes |S|}\) for support \(S\), and empty block value \(1\). Expanding
\[
H_G(x,y)=\prod_{v\in V}\bigl(1+\mathbf1_{x_v\ne0,y_v\ne0}[b(x_v,y_v)-1]\bigr)
\]
by subsets of the intersection of the two supports yields \(H_G=ZDZ^{\mathsf T}\): all subsets in this expansion are allowed. The blocks are invertible. Each nonempty support of size \(k\) contributes \(|\det K|^{k(q-1)^{k-1}}\); their product is the determinant formula, since these exponents sum to \(I_G'(q-1)\).

Every interval in the assignment order is Boolean, hence \(Z^{-1}(x,z)=(-1)^{|\operatorname{supp}(x)|-|\operatorname{supp}(z)|}\mathbf1_{z\preceq x}\). In \(Z^{-\mathsf T}D^{-1}Z^{-1}\), only blocks with common support containing \(U\) can contribute. Per coordinate at which both labels are prescribed, the inverse block contributes \(q^{-1}\overline{b(x_v,y_v)}\). Where one label is prescribed and one is free, the character sum over nonzero labels is \(-1\); the one Möbius sign cancels it to give \(q^{-1}\). At every additional coordinate, the double sum over nonzero labels gives \(-(q-1)\), and two signs give no change, for a contribution \(-(q-1)/q\). When \(U\) is independent, extensions of it are exactly \(U\) together with an independent subset of \(G-N[U]\). Summing over these subsets proves (1). If \(U\) is not independent, no support block can contain it. This also covers the empty graph, for which the matrix and inverse are both \([1]\).

**Classifying cancellations.** The reduced numerator of \(-(q-1)/q\) is \(-(q-1)\), and \(I_J\) has integer coefficients and constant coefficient \(1\). For \(q\ge3\) the rational-root theorem forbids cancellation for every residual graph. For \(q=2\), on a path of \(m\) vertices the value \(F_m=I_{P_m}(-1/2)\) satisfies \(F_0=1\), \(F_1=1/2\), and \(F_m=F_{m-1}-F_{m-2}/2\), by deciding whether to select the last vertex. Its roots as a recurrence are \((1\pm i)/2\), giving
\[
F_m=2^{-m/2}\sin((m+2)\pi/4).
\]
This vanishes precisely at \(m\equiv2\pmod4\). The residual graph of a path is a disjoint union of paths; its independence polynomial is the product of their independence polynomials. With \(U=\varnothing\), the residual graph is the original path. This proves both zero descriptions.

## Verification

The proof is unrestricted. The accompanying `path_fourier_checker.py` is a finite exact-arithmetic check of matrix times proposed inverse (symmetry gives the other order) for binary paths of lengths 2–8, ternary paths of lengths 2–5, and cyclic-quaternary paths of lengths 2–4. It checks binary determinant magnitudes for lengths 2–6. It also tests the zero classification entry by entry: for compatible unions in the binary cases it checks the lengths of residual path runs, and for compatible unions in the nonbinary cases it checks nonvanishing. Incompatible unions are checked separately. The script uses only the Python standard library and is run as `python3 path_fourier_checker.py`.

## Relationship to prior work and limitations

The same support-poset zeta factorization and local character sums appear in the finite-group Fourier Hamming-ball inverse [1]. There the allowed extensions are determined only by cardinality and give truncated binomial sums. The block calculation above adapts that method to graph-constrained extensions; it is not a claim of a new factorization method or a priority assertion based on catalogue dates. The focus is the exact support and cancellation laws for graph exclusions: the result fixes the entire zero pattern in the nonbinary case and identifies a label-independent additional zero mechanism on binary paths. For example, a compatible union on a long path can have an inverse zero because of a two-vertex uncovered run, even when other runs do not vanish. The univariate independence-polynomial recurrence itself is standard. Classical meet-matrix methods also yield the binary zeta factorization by writing the kernel as \((-1)^{|x\cap y|}\); the graph/link and alphabet-specific zero descriptions are the point here. Knill's simplicial counting matrix [2] has a different kernel, and the Fourier-Kronecker submatrix rank results of Delvaux–Van Barel are potential related context whose full coverage was not settled. No general spectral conditioning bound is given.

## References

1. *Universal inverse and sharp conditioning of finite Fourier Hamming balls*, [Resultary 3b7e4e36808a](https://github.com/Resultary/2026/tree/main/2026/11/8/SCOPE-universal-inverse-and-sharp-conditioning-of-finite-fourier-hammi--3b7e4e36808a), Proof §§1–3.
2. O. Knill, *The counting matrix of a simplicial complex*, [arXiv:1907.09092v1](https://arxiv.org/abs/1907.09092v1), Theorem 1.
3. V. E. Levit and E. Mandrescu, *On the independence polynomial of an antiregular graph*, [arXiv:1007.0880](https://arxiv.org/abs/1007.0880), Introduction and Proposition 1.1.
4. S. Delvaux and M. Van Barel, *Rank-deficient submatrices of Kronecker products of Fourier matrices*, Linear Algebra Appl. 426 (2007), 349–367, DOI:10.1016/j.laa.2007.05.009.
