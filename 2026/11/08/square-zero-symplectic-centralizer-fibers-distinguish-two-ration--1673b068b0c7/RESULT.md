# Square-zero symplectic centralizer fibers distinguish two rational nilpotent orbits

## Finding

Let \(q\) be an odd prime power, \(k=\mathbb F_q\), and let \(S\) be any nonsingular symmetric \(4\times4\) matrix over \(k\). On \(k^8\) use the alternating form with matrix
\[
J=\begin{pmatrix}0&I_4\\-I_4&0\end{pmatrix},\qquad
N_S=\begin{pmatrix}0&S\\0&0\end{pmatrix}\in\mathfrak{sp}_8(k).
\]
Thus \(N_S^2=0\), \(\operatorname{rank}N_S=4\), and its geometric Jordan partition is \((2,2,2,2)\). Define
\[
H_{S,q}(z)=\sum_{\substack{X\in\mathfrak{sp}_8(k)\\X^2=0,\,[X,N_S]=0}}z^{\operatorname{rank}X}.
\]
Write \(\delta(S)=1\) when \(\det S\in(k^\times)^2\), and \(0\) otherwise. The exact polynomial is
\[
\boxed{\begin{aligned}
H_{S,q}(z)={}&1+(q^4-1)z
+q^2(q-1)(q^2+1)(q^2+q+1)z^2\\
&+q^2(q-1)^2(q+1)(q^2+1)(q^2+q+1)z^3\\
&+q^6\big((q-1)^2(q^2+q+1)+2\delta(S)(q^2-1)\big)z^4.
\end{aligned}}
\]
In particular,
\[
H_{S,q}(1)=\begin{cases}
q^{10},&\det S\text{ nonsquare},\\
q^{10}+2(q^2-1)q^6,&\det S\text{ square}.
\end{cases}
\]
For odd \(q\), the two congruence classes of nonsingular symmetric forms in dimension four give two distinct rational symplectic nilpotent orbits of the same geometric Jordan type. Their square-zero centralizer rank distributions disagree **only at maximal rank four**.

## Assumptions and scope

All matrices and ranks are over \(k\), an arbitrary finite field of odd cardinality \(q\). The symplectic Lie algebra consists of matrices \(X\) satisfying \(X^{\mathsf T}J+JX=0\). Matrices \(S\) are invertible and symmetric. The rank of a square-zero \(8\times8\) matrix is at most four. No assumption that \(q\) is prime rather than a prime power is used in the proof. The split/nonsplit terminology refers to the Witt class of the symmetric four-space with Gram matrix \(S^{-1}\); in dimension four its split class is equivalent to square determinant. Indeed, the image and kernel of every maximal-rank square-zero symplectic Lie element coincide and form a Lagrangian four-space: for any vectors \(x,y\), skew-adjointness gives \(\langle Nx,Ny\rangle=-\langle x,N^2y\rangle=0\). In a symplectic basis adapted to this Lagrangian the element has the displayed \(N_S\) form. The symplectic stabilizer of that Lagrangian changes the symmetric \(S\) by congruence, and all such congruences are realized. Finite fields of odd cardinality have exactly two classes of nonsingular symmetric four-forms, so these are exactly the two rational orbits. The distribution consequently depends only on the rational nilpotent orbit.

## Proof

**1. Centralizer and square-zero equations.** Write a general symplectic Lie element as
\[
X=\begin{pmatrix}A&B\\C&-A^{\mathsf T}\end{pmatrix},\qquad B=B^{\mathsf T},\ C=C^{\mathsf T}.
\]
Direct multiplication with \(N_S\) gives \([X,N_S]=0\) if and only if \(C=0\) and \(AS+SA^{\mathsf T}=0\), because \(S\) is invertible. Then
\[
X^2=0\quad\Longleftrightarrow\quad A^2=0,\quad AB=BA^{\mathsf T}.
\]
Consequently all solutions correspond bijectively to pairs \((A,B)\) with \(A\) skew-adjoint for the symmetric form \(S^{-1}\), \(A^2=0\), and \(B\) symmetric satisfying \(AB=BA^{\mathsf T}\).

**2. The contribution from \(A=0\).** In this case \(X=\begin{pmatrix}0&B\\0&0\end{pmatrix}\) and \(\operatorname{rank}X=\operatorname{rank}B\). A symmetric matrix of rank \(r\) is determined by its \((4-r)\)-dimensional radical and a nonsingular symmetric form on the quotient. Therefore its number is \({4\brack r}_q\,T_r(q)\), where \({4\brack r}_q\) is a Gaussian binomial coefficient and
\[
T_0(q)=1,\quad T_1(q)=q-1,\quad T_2(q)=q^2(q-1),\quad
T_3(q)=q^2(q-1)^2(q^2+q+1),\quad
T_4(q)=q^6(q-1)^2(q^2+q+1).
\]
These standard finite-field form counts follow by dividing \(|\operatorname{GL}_r(k)|\) by the orders of the two orthogonal stabilizers, then summing both discriminant classes. Substituting the Gaussian coefficients gives
\[
\begin{aligned}
F_q(z)={}&1+(q^4-1)z+q^2(q-1)(q^2+1)(q^2+q+1)z^2\\
&+q^2(q-1)^2(q+1)(q^2+1)(q^2+q+1)z^3\\
&+q^6(q-1)^2(q^2+q+1)z^4.
\end{aligned}
\]
The sum of these coefficients is \(q^{10}\), the number of symmetric \(4\times4\) matrices.

**3. Classification of nonzero \(A\).** Let \(H=S^{-1}\). The equation \(AS+SA^{\mathsf T}=0\) is exactly \(A^{\mathsf T}H+HA=0\). Thus \(HA\) is alternating, and \(\operatorname{rank}A\) must be even in odd characteristic. As \(A^2=0\) on a four-space, \(\operatorname{rank}A\le2\). Every nonzero such \(A\) therefore has rank two and \(U=\operatorname{im}A=\ker A\). For \(u=Ax\) and \(v=Ay\),
\[
\langle u,v\rangle_H=\langle Ax,Ay\rangle_H
=-\langle x,A^2y\rangle_H=0.
\]
So \(U\) is maximal totally isotropic for \(H\). A nonsplit four-space has Witt index one and admits no such \(U\), hence no nonzero \(A\). In a split four-space, the two reguli of the hyperbolic quadric give exactly \(2(q+1)\) totally isotropic planes. For each fixed \(U\), the skew-adjoint endomorphisms satisfying \(\operatorname{im}A=\ker A=U\) correspond to nonzero alternating maps \(V/U\to U\); because \(\dim U=2\), this is a one-dimensional space of alternating forms with \(q-1\) nonzero members. Therefore the exact number of nonzero admissible \(A\) is
\[
\begin{cases}2(q+1)(q-1)=2(q^2-1),&\det S\text{ square},\\0,&\det S\text{ nonsquare}.\end{cases}
\]

**4. Compatible blocks and their ranks.** Fix one nonzero \(A\). Choose a hyperbolic basis adapted to \(U\), so \(H=\begin{pmatrix}0&I_2\\I_2&0\end{pmatrix}\) and
\[
A=\begin{pmatrix}0&K\\0&0\end{pmatrix},\qquad
K=\begin{pmatrix}0&c\\-c&0\end{pmatrix},\quad c\ne0.
\]
Put \(D=BH\). The condition \(B=B^{\mathsf T}\) is equivalent to \(D\) being \(H\)-self-adjoint; the condition \(AB=BA^{\mathsf T}\) is equivalent to \(AD+DA=0\). Thus
\[
D=\begin{pmatrix}P&Q\\R&P^{\mathsf T}\end{pmatrix},\qquad Q=Q^{\mathsf T},\ R=R^{\mathsf T}.
\]
The equation \(AD+DA=0\) forces \(R=0\) and \(KP^{\mathsf T}+PK=0\), which for the invertible \(2\times2\) alternating \(K\) is exactly \(\operatorname{tr}P=0\). The parameters are therefore three free entries of \(P\) (trace zero) and three free entries of symmetric \(Q\), six total. Hence precisely \(q^6\) compatible \(B\) exist.

Finally, every resulting \(X\) has rank four, independently of \(B\). Projection of \(\operatorname{im}X\) onto its second four-dimensional summand equals \(\operatorname{im}A^{\mathsf T}\), of dimension two. Its kernel equals \(\operatorname{im}A+B\ker A^{\mathsf T}\). From \(AB=BA^{\mathsf T}\) we have \(B\ker A^{\mathsf T}\subseteq\ker A=\operatorname{im}A\); hence this kernel has dimension two. Therefore \(\operatorname{rank}X=2+2=4\).

Combining the \(A=0\) polynomial with the \(2(q^2-1)q^6\) extra rank-four solutions in the split case proves the claimed formula, including the rank-specific difference and both total counts. \(\square\)

## Verification

Run `python3 verification/verify.py` using ordinary Python. The accompanying `verification/output.txt` records one actual replay. The checker independently enumerates all skew-adjoint \(A\) for the two determinant classes over \(\mathbb F_3\), \(\mathbb F_5\), and \(\mathbb F_7\), checking that the only nonzero square-zero cases have rank two, with exactly \(2(q^2-1)\) cases in the split class and none in the nonsplit class. It explicitly solves \(AB-BA^{\mathsf T}=0\) as a linear system and confirms the six-dimensional solution space. For \(q=3\) it exhausts all \(q^6\) compatible symmetric blocks for every nonzero \(A\), constructs the actual \(8\times8\) matrices, and verifies square zero and rank four. A second exhaustive enumeration computes the ranks of all \(3^{10}\) symmetric \(4\times4\) matrices. Polynomial total-count checks for \(q=3,5,7,9\) are arithmetic consistency checks only; the checker does not enumerate matrices over the extension field \(\mathbb F_9\). The proof, not the computations, covers all odd prime powers.

## Relationship to prior work

Oksana Yakimova's 2008 preprint investigates nilpotent centralizers in classical Lie algebras and their structural phenomena; its algebraic centralizer results motivate the fixed centralizer. It does not provide a finite-field count of commuting square-zero elements by rank or distinguish these rational-orbit fiber distributions. Samuel Reid's 2014 work discusses nilpotent orbit varieties for classical groups rather than the present finite-field point counts. Britnell and Wildon's 2010 study concerns existence of commuting representatives of general linear matrix classes. Fulman and Guralnick's 2016 preprint (subsequent to the archive cutoff) develops generating functions counting aggregate commuting pairs and aggregate commuting nilpotent pairs in symplectic Lie algebras; those results do not directly determine this fixed-orbit, square-zero, rank-refined distribution. Standard orthogonal-group form counts and the classical two-regulus geometry are used as known lemmas, not claimed as new. Compared with an existing general-linear centralizer rank count, the present restriction to the symplectic Lie algebra introduces a genuine split/nonsplit rational-orbit dependence, which is not a specialization of the unrestricted general-linear formula without further work.

## Limitations

The result is for odd-characteristic finite fields and dimension eight, with the fixed nilpotent element of maximal square-zero rank. It does not determine characteristic-two behavior, arbitrary symplectic dimensions, other fixed nilpotent Jordan partitions, or simultaneous conjugacy classes of pairs. These formulas have computational checks but no independent mathematical validation. A more general currently unidentified orbit-incidence formula might imply this calculation; historical priority is not certified.

## References

1. O. Yakimova, *Surprising properties of centralisers in classical Lie algebras*, arXiv:0803.0285, first posted 2008-03-03. https://arxiv.org/abs/0803.0285
2. S. Reid, *General Linear and Symplectic Nilpotent Orbit Varieties*, arXiv:1403.3112, first posted 2014-03-12. https://arxiv.org/abs/1403.3112
3. J. R. Britnell and M. Wildon, *On types and classes of commuting matrices over finite fields*, arXiv:1001.0811, first posted 2010-01-06. https://arxiv.org/abs/1001.0811
4. J. Fulman and R. Guralnick, *Enumeration of Commuting Pairs in Lie Algebras over Finite Fields*, arXiv:1611.05499, first posted 2016-11-16. https://arxiv.org/abs/1611.05499
