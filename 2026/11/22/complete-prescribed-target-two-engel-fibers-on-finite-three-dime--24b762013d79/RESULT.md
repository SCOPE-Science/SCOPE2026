# Complete prescribed-target two-Engel fibers on finite three-dimensional matrix Lie algebras

## Finding

Let \(q\) be any prime power, let \(L=\mathfrak{sl}_2(\mathbb F_q)\), and set
\[
\mathcal E:L\times L\longrightarrow L,\qquad \mathcal E(X,Y)=[X,[X,Y]],\quad [A,B]=AB-BA.
\]
For \(Z=\begin{psmallmatrix}a&b\\c&-a\end{psmallmatrix}\), put \(Q(Z)=a^2+bc=-\det Z\). When \(q\) is odd, let \(\chi\) be the quadratic character of \(\mathbb F_q\), extended by \(\chi(0)=0\). Then for every \(Z\in L\), the exact number \(N_q(Z)=|\mathcal E^{-1}(Z)|\) is
\[
N_q(Z)=\begin{cases}
2q^4-q^2,& Z=0,\\
2q^2(q-1),&Z\ne0,\ Q(Z)=0,\\
q(q-1)^2,&\chi(Q(Z))=1,\\
q(q^2-1),&\chi(Q(Z))=-1.
\end{cases}
\]
The respective target-stratum sizes are \(1\), \(q^2-1\), \(q(q^2-1)/2\), and \(q(q-1)^2/2\). In particular, all targets occur, and the total input mass mapping to the square and nonsquare nonzero \(Q\)-strata is exactly equal, namely \(q^2(q^2-1)(q-1)^2/2\) each.

For every even prime power \(q\), the map \(\mathcal E\) is identically zero; thus \(N_q(0)=q^6\), and \(N_q(Z)=0\) otherwise. The brackets are those of the full trace-zero matrix Lie algebra (which has a central line in characteristic two).

## Assumptions and scope

The statement includes all prime powers \(q\), not merely prime fields. All matrices \(X,Y,Z\) range over the three-dimensional vector space of trace-zero \(2\times2\) matrices, with no restrictions on nilpotency, invertibility, or nonzero entries. Fibers are ordered pairs. The nonzero-square/nonsquare separation is asserted only when \(q\) is odd. The object is the *second* Lie Engel polynomial, not the analogous word map in the matrix group.

## Proof

Suppose \(q\) is odd. For \(X,Y\in L\), the characteristic polynomial identity and trace-zero anticommutator identity are
\[
X^2=Q(X)I_2,\qquad XY+YX=\operatorname{tr}(XY)I_2.
\]
Writing \(B(X,Y)=\operatorname{tr}(XY)\), direct expansion yields
\[
\mathcal E(X,Y)=4Q(X)Y-2B(X,Y)X.\tag{1}
\]
The form \(B\) is nondegenerate in odd characteristic. If \(X=0\), the linear map \(Y\mapsto\mathcal E(X,Y)\) is zero and admits \(q^3\) possible \(Y\). If \(X\ne0\) and \(Q(X)=0\), equation (1) is a rank-one operator with image \(\langle X\rangle\) and with \(q^2\) preimages per image point. If \(Q(X)\ne0\), the map has kernel \(\langle X\rangle\), image the plane \(X^\perp=\{Z:B(X,Z)=0\}\), and exactly \(q\) preimages per image point: on \(X^\perp\), equation (1) acts as multiplication by the nonzero scalar \(4Q(X)\).

The ternary quadratic form \(Q(a,b,c)=a^2+bc\) has exactly \(q^2\) zeros, including the origin. For fixed nonzero \(t\in\mathbb F_q\), it takes the value \(t\) at exactly \(q(q+\chi(t))\) triples: fixing \(a\), the equation \(bc=t-a^2\) has \(q-1\) solutions when its right side is nonzero and \(2q-1\) when it vanishes. Therefore, there are \(q^2-1\) nonzero isotropic vectors and \(q^3-q^2\) nonisotropic vectors in \(L\).

For \(Z=0\), every \(X\) contributes its kernel size, so
\[
N_q(0)=q^3+(q^2-1)q^2+(q^3-q^2)q=2q^4-q^2.
\]
Now let \(Z\ne0\) be isotropic. Exactly the \(q-1\) nonzero vectors \(X\in\langle Z\rangle\) give rank-one images containing \(Z\). The plane \(Z^\perp\) has precisely \(q(q-1)\) nonisotropic elements. Indeed, conjugate \(Z\) to \(\begin{psmallmatrix}0&1\\0&0\end{psmallmatrix}\), so the perpendicular plane is \(c=0\) and the nonisotropy condition is \(a\ne0\). Consequently,
\[
N_q(Z)=(q-1)q^2+q(q-1)q=2q^2(q-1).
\]

Finally suppose \(Q(Z)\ne0\). There are no nonzero isotropic \(X\) with rank-one image containing \(Z\). Only the nonisotropic elements of \(Z^\perp\) contribute, each with \(q\) preimages. If \(Q(Z)\) is a square, the perpendicular binary plane is split, with exactly \((q-1)^2\) nonisotropic vectors: after scaling and conjugacy, take \(Z=\operatorname{diag}(u,-u)\), so \(Z^\perp\) is the off-diagonal plane and \(Q(X)=bc\). If \(Q(Z)\) is a nonsquare, this plane is anisotropic, with exactly \(q^2-1\) nonisotropic vectors: take \(Z=\begin{psmallmatrix}0&1\\t&0\end{psmallmatrix}\) for nonsquare \(t\), so in \(Z^\perp\) one has \(c=-tb\), whence \(Q(X)=a^2-tb^2\). Multiplication by \(q\) gives the remaining two fiber formulas.

The stratum sizes follow from the preceding count \(q(q+\chi(t))\), summed over \((q-1)/2\) nonzero squares and over \((q-1)/2\) nonsquares. Multiplying them by the corresponding fibers proves the equal-mass identity. Their total weighted sum is \(q^6\), confirming that the partition exhausts all ordered input pairs.

When \(q\) is even, every trace-zero \(2\times2\) matrix has equal diagonal entries. Its commutator with another such matrix is scalar, so \([L,L]\subseteq\mathbb F_q I_2\) is central. Thus every nested commutator of length three vanishes and \(\mathcal E\equiv0\), proving the remaining case.

## Verification

The attached standalone `verify_engel.py` enumerates all ordered pairs by direct \(2\times2\) matrix products and independently compares every prescribed-target fiber with the formula. It was run for \(q=2,3,4,5,7,9\), using explicit polynomial-field arithmetic for \(q=4,9\). Every assertion passed; representative odd-field statistics are: \(q=3\), fibers \((153,36,12,24)\), and \(q=5\), fibers \((1225,200,80,120)\), in the target-class order stated above. The code is finite corroboration; the algebraic argument above proves the claim for all prime powers.

## Relationship to prior work

Bandman, Gordeev, Kunyavskii and Plotkin treat qualitative image/surjectivity properties of Engel polynomials on simple Lie algebras (arXiv:1012.4106, particularly their Theorem 4.3 and Corollary 4.4). Kanel-Belov, Malev and Rowen classify possible images of low-dimensional Lie polynomials (arXiv:1506.06792); their primary classification is 17B01. The later Roy–Singh treatment (arXiv:2607.21171) studies Engel-map surjectivity and constructions of suitable nonempty fibers over trace-zero matrices and local rings; its Section 3 does not present the complete size of every finite-field prescribed-target fiber. All qualitative surjectivity claims and basic adjoint identities from these papers are prior work. The new, narrowly specified claim here is the full four-stratum finite-field fiber distribution, including the square/nonsquare contrast and its exact aggregate balance, alongside the characteristic-two collapse.

## Limitations

No independent audit or completeness claim about all prior literature is made. A broader unpublished finite-field Lie-word fiber theorem could subsume this calculation. The precise result addresses one cubic Lie polynomial on one fixed matrix size, not higher matrix sizes, higher Engel lengths, or group-valued Engel words. Enumeration of small fields is not presented as a proof for all fields.

## References

1. T. Bandman, N. Gordeev, B. Kunyavskii, E. Plotkin, *Equations in simple Lie algebras*, arXiv:1012.4106 (first public version 2010-12-18); J. Algebra 355 (2012), 67–79. https://arxiv.org/abs/1012.4106
2. A. Kanel-Belov, S. Malev, L. Rowen, *The images of Lie polynomials evaluated on matrices*, arXiv:1506.06792 (first public version 2015-06-22); Commun. Algebra 45 (2017), 4801–4808. https://arxiv.org/abs/1506.06792
3. A. Roy, A. Singh, *Surjectivity of Engel Maps over trace zero matrices in \(M_2(\mathcal O)\)*, arXiv:2607.21171 (2026). https://arxiv.org/abs/2607.21171
