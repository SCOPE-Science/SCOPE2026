# A sharp finite-critical-point gap on the Grassmannian ED discriminant

## Finding
Let \(1\le k\le n-1\), and let
\[
\Sigma\subset \operatorname{Sym}^2(\mathbb C^n)
\]
be the Euclidean-distance discriminant for optimization on the projection Grassmannian \(\operatorname{pGr}(k,n)\). If \(Q\in\Sigma\) has a finite critical set, then
\[
\#\operatorname{Crit}(Q)
\le
M_{n,k}
:=
\binom{n-2}{k}+\binom{n-2}{k-2}
=
\binom{n}{k}-2\binom{n-2}{k-1}.
\]
The bound is sharp for every \(n\ge2\) and every \(1\le k\le n-1\).

Consequently there is a forbidden finite interval on the discriminant:
\[
M_{n,k}
<
\#\operatorname{Crit}(Q)
<
\binom{n}{k}
\]
never occurs. The generic off-discriminant count is \(\binom{n}{k}\), while a finite discriminant count must drop by at least
\[
2\binom{n-2}{k-1}.
\]

For real symmetric \(Q\in\Sigma\), the critical set is infinite, so every finite discriminant example is genuinely complex.

## Assumptions and scope
The optimization problem is the one studied by Friedman--Hoşten--Rosana:
\[
\operatorname{maximize}\ \operatorname{trace}(PQ)
\quad\text{subject to}\quad
P\in\operatorname{pGr}(k,n),
\]
with \(1\le k\le n-1\) and complex symmetric data \(Q\). The count is set-theoretic, matching their Theorem 3.5, which distinguishes finite from infinite critical sets. No claim is made about multiplicities in a nonreduced critical scheme.

The source proves that the ED discriminant is the characteristic-polynomial discriminant and that, when the critical set is finite, its cardinality is the coefficient of \(x^k\) in a product determined by Jordan-block sizes.

## Proof
Write the Jordan-block sizes of \(Q\) as a partition
\[
\lambda=(s_1,\ldots,s_r),\qquad s_1+\cdots+s_r=n.
\]
Friedman--Hoşten--Rosana prove that whenever the critical set is finite,
\[
\#\operatorname{Crit}(Q)
=
[x^k]\prod_{j=1}^r(1+x^{s_j}).
\]
Because \(Q\in\Sigma\), the characteristic polynomial has a repeated root. If all Jordan blocks had size \(1\), then \(Q\) would be diagonalizable with a repeated eigenvalue, and the source proves that the critical set is infinite. Therefore every finite discriminant datum has at least one block of size at least \(2\).

Now refine the partition without destroying one nontrivial part. Replacing a part \(a+b\) by two positive parts \(a,b\) changes the corresponding factor by
\[
(1+x^a)(1+x^b)-(1+x^{a+b})=x^a+x^b,
\]
which has coefficientwise nonnegative coefficients. Hence such a refinement can only increase every coefficient.

Choose one block of size at least \(2\), refine it to \(2\) together with size-one blocks, and refine every other block completely into size-one blocks. The resulting partition is
\[
(2,1^{n-2}).
\]
Coefficientwise monotonicity therefore gives
\[
[x^k]\prod_{j=1}^r(1+x^{s_j})
\le
[x^k](1+x^2)(1+x)^{n-2}
=
\binom{n-2}{k}+\binom{n-2}{k-2}.
\]
Using Pascal's identity twice,
\[
\binom{n}{k}
=
\binom{n-2}{k}
+2\binom{n-2}{k-1}
+\binom{n-2}{k-2},
\]
which gives the stated gap.

Sharpness is realized explicitly. Let
\[
N=
\begin{pmatrix}
i&1\\
1&-i
\end{pmatrix}.
\]
Then \(N=N^\mathsf T\), \(N\ne0\), and \(N^2=0\), so \(N\) has one Jordan block of size \(2\) with eigenvalue \(0\). For \(n>2\), choose pairwise distinct nonzero scalars \(\lambda_3,\ldots,\lambda_n\), and set
\[
Q=N\oplus\operatorname{diag}(\lambda_3,\ldots,\lambda_n).
\]
Each distinct eigenvalue contributes exactly one Jordan block. Thus the source's finiteness criterion is automatically satisfied, and its counting formula gives
\[
\#\operatorname{Crit}(Q)
=
[x^k](1+x^2)(1+x)^{n-2}
=
M_{n,k}.
\]
For \(n=2\), the same matrix \(N\) gives the sharp value \(M_{2,1}=0\).

Finally, every real symmetric matrix is diagonalizable. If it lies on the discriminant, it has a repeated eigenvalue, and the source's diagonalizable case gives infinitely many critical points.

## Verification
The accompanying `verify.py` checks the nilpotent symmetric witness exactly, verifies the binomial gap identity, enumerates all integer partitions through \(n=18\) to confirm the coefficient maximum, and checks the coefficientwise refinement step used in the proof. It ends with `VERIFY_OK`.

The enumeration is only a stress test; the proof above is infinite and does not depend on the finite range.

## Relationship to prior work
Friedman--Hoşten--Rosana identify the ED discriminant of \(\operatorname{pGr}(k,n)\) and give a complete Jordan-block criterion and coefficient formula for finite critical sets. They do not state the sharp largest finite count on the discriminant, the exact gap from the generic ED degree, or the resulting forbidden finite interval.

Lai--Lim--Ye determine the generic ED degree of the Grassmann manifold and give stationary points for distinct-eigenvalue real data. They explicitly note that repeated eigenvalues in the real symmetric setting yield infinitely many stationary points, but they do not treat defective complex symmetric data or the sharp finite discriminant boundary.

Breiding--Kozhasov--Lerario study the real repeated-eigenvalue discriminant as a geometric object and compute its codimension-two real geometry. Their problem is distance to the discriminant itself, rather than distance optimization on the Grassmannian with a discriminant data matrix, so it does not imply the bound above.

## Limitations
The finite-count bound is set-theoretic and uses the source's Theorem 3.5; it does not determine local multiplicities of a critical scheme. The sharp witness is complex symmetric, not real symmetric. The result concerns the whole projection Grassmannian rather than arbitrary Grassmannian subvarieties.

Originality searches cannot exclude an unindexed equivalent corollary, but no implication-equivalent statement was found in the initiating full text, the inspected generic ED-degree paper, the inspected real-discriminant geometry paper, targeted web searches, or the published-finding database.

## References
1. Hannah Friedman, Serkan Hoşten, Andrea Rosana, *Euclidean Distance Optimization Within the Grassmannian*, arXiv:2610.02018v1, 1 October 2026.
2. Zehua Lai, Lek-Heng Lim, Ke Ye, *Euclidean distance degree in manifold optimization*, arXiv:2502.10336; SIAM Journal on Optimization 35 (2025).
3. Paul Breiding, Khazhgali Kozhasov, Antonio Lerario, *On the Geometry of the Set of Symmetric Matrices with Repeated Eigenvalues*, Arnold Mathematical Journal 4 (2018), 423--443, DOI 10.1007/s40598-018-0095-0.
