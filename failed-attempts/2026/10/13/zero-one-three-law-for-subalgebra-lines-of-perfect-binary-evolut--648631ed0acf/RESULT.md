# Zero–one–three law for subalgebra lines of perfect binary evolution algebras in characteristic two

## Finding
For each power \(q=2^m\), \(m\ge 1\), fix a two-dimensional vector space over \(\mathbb F_q\) with an ordered basis \(e_1,e_2\). Give it an evolution-algebra product
\[
e_1e_2=0,\quad e_1^2=a e_1+c e_2,\quad e_2^2=b e_1+d e_2,
\qquad A=\begin{pmatrix}a&b\\c&d\end{pmatrix}\in\mathrm{GL}_2(\mathbb F_q).
\]
For each such **labeled structure matrix**, let \(r(A)\) be the number of nonzero one-dimensional subalgebras. Then \(r(A)\) is exactly one of \(0,1,3\), and the complete distribution is
\[
\#\{A:r(A)=0\}=\frac{q(q-1)^2(q+1)}3,\quad
\#\{A:r(A)=1\}=\frac{q(q-1)^2(q+1)}2,\quad
\#\{A:r(A)=3\}=\frac{q(q-1)^2(q+1)}6.
\]
Thus precisely one third of labeled perfect binary evolution-algebra structures over \(\mathbb F_q\) have no proper nonzero subalgebra, and exactly one half have a unique one. Each one-dimensional subalgebra contains exactly one nonzero idempotent; hence the same distribution counts nonzero idempotents. Equivalently, the complete subalgebra-dimension polynomial of such an algebra is \(1+r(A)T+T^2\).

## Assumptions and scope
The base field is \(\mathbb F_q\) with \(q\) a positive power of two. Products are commutative and need not be associative. The matrix \(A\) uses **columns** for the coordinate vectors of \(e_1^2\) and \(e_2^2\); its invertibility is equivalent to the perfectness condition \(E^2=E\). The distribution is over all \(|\mathrm{GL}_2(\mathbb F_q)|\) matrices in the fixed ordered natural basis, not uniformly over isomorphism classes. A subalgebra is a linear subspace closed under multiplication, including zero and the whole algebra.

## Proof
Write \(v=x e_1+y e_2\), and use \(v^{[2]}=(x^2,y^2)^{\mathsf T}\) for coordinatewise squaring. Then
\[
v^2=A v^{[2]}.
\]
Since \(A\) is invertible, \(v^2\ne0\) whenever \(v\ne0\). Consequently \(\mathbb F_qv\) is a subalgebra exactly when \(A v^{[2]}=\lambda v\) for some \(\lambda\in\mathbb F_q^\times\). In this case \(\lambda^{-1}v\) is an idempotent and is the unique nonzero idempotent on that line. Thus \(r(A)\) is the fixed-point count on \(\mathbf P^1(\mathbb F_q)\) of the projective permutation induced by \(v\mapsto A v^{[2]}\). This is a bijection because coordinatewise squaring is a field automorphism in characteristic two.

Suppose two distinct projective lines \(\mathbb F_qv_1,\mathbb F_qv_2\) are fixed. Choose independent vectors \(v_i\) on them and scalars \(\lambda_i\ne0\) satisfying \(A v_i^{[2]}=\lambda_i v_i\). Characteristic two gives, for every pair of scalars \(s,t\),
\[
A(sv_1+tv_2)^{[2]}=s^2\lambda_1v_1+t^2\lambda_2v_2.
\]
When \(st\ne0\), this vector spans \(sv_1+tv_2\) precisely when \(s\lambda_1=t\lambda_2\). There is exactly one such projective direction, namely \(\mathbb F_q(\lambda_2v_1+\lambda_1v_2)\). Therefore any two fixed lines force exactly one additional fixed line, and \(r(A)\in\{0,1,3\}\), including the boundary field \(\mathbb F_2\).

Put \(N=|\mathrm{GL}_2(\mathbb F_q)|=q(q-1)^2(q+1)\). Fix any projective line \(\ell=\mathbb F_qv\). As \(v^{[2]}\ne0\), the number of invertible matrices sending \(v^{[2]}\) to a nonzero vector of \(\ell\) is \((q-1)(q^2-q)=q(q-1)^2\): choose the image of this vector and then the image of an independent complement outside \(\ell\). There are \(q+1\) choices of \(\ell\), hence
\[
\sum_{A\in\mathrm{GL}_2(\mathbb F_q)}r(A)=N.
\]
Fix two distinct lines \(\ell_1,\ell_2\). Their coordinatewise squares remain linearly independent, as the determinant of the squared coordinates is the square of the original determinant. There are exactly \((q-1)^2\) invertible matrices fixing both lines: independently choose a nonzero target vector on each target line. Counting unordered pairs yields
\[
\sum_A\binom{r(A)}2=\binom{q+1}2(q-1)^2=\frac N2.
\]
Writing \(n_j=\#\{A:r(A)=j\}\), these equations give \(n_1+3n_3=N\), \(3n_3=N/2\), and \(n_0+n_1+n_3=N\). Solving gives \(n_3=N/6\), \(n_1=N/2\), and \(n_0=N/3\), as claimed.

## Verification
The standalone `checker.py` enumerates every invertible \(2\times2\) matrix over explicit polynomial-basis models of \(\mathbb F_2,\mathbb F_4,\mathbb F_8,\mathbb F_{16}\), tests closure of every rational projective line, and compares with all three theoretical counts. It prints `VERIFY_OK` after the four exhaustive finite tests. These computations are checks of instances only; the proof above establishes the formula for every even prime power. For \(q=2\), the distribution is \((n_0,n_1,n_3)=(2,3,1)\). A matrix with no proper nonzero subalgebra is \(\begin{pmatrix}0&1\\1&1\end{pmatrix}\), since over \(\mathbb F_2\) the squaring map is the identity and this matrix has no rational eigenline.

## Relationship to prior work
Cabrera Casado, Martín Barquero and Martín González classify two-dimensional perfect evolution algebras over domains, including fields, but do not give this distribution of one-dimensional subalgebras among labeled structure matrices [1]. Wei and Zou enumerate isomorphism classes of perfect evolution algebras over finite fields, a different equivalence-class count [2]. The general semilinear Frobenius normal-form theory of Dempwolff, Fisher and Herman describes the operator underlying the fixed-line equation but its projective corollaries do not calculate the present distribution over \(A\in\mathrm{GL}_2(\mathbb F_q)\) [3]. García-Martínez and Pérez-Rodríguez describe the subalgebra–idempotent correspondence and existence over the complex field; their setting does not give the present finite-characteristic-two statistics [4].

## Limitations
The claim is confined to finite fields of characteristic two and two-dimensional **perfect** evolution algebras. It does not enumerate isomorphism classes with a specified number of subalgebras, nor treat singular structure matrices, higher-dimensional algebras, or odd-characteristic distributions. Classical results on projective semilinear maps could provide equivalent formulations; independently checking the broader literature remains desirable. No independent external validation has been performed.

## References
[1] Y. Cabrera Casado, D. Martín Barquero, C. Martín González, *Two dimensional perfect evolution algebras over domains*, arXiv:2204.08410v1 (18 April 2022); J. Algebraic Combin. 58 (2023), 569–587, DOI 10.1007/s10801-022-01196-1.

[2] Y. Wei and Y. M. Zou, *Isomorphism Classes of Idempotent Evolution Algebras*, arXiv:2310.12368v1 (18 October 2023), especially Section 4 and Theorem 4.1.

[3] U. Dempwolff, J. C. Fisher, A. Herman, *Semilinear transformations over finite fields are Frobenius maps*, Glasgow Math. J. 42 (2000), 289–295, DOI 10.1017/S0017089500020164.

[4] X. García-Martínez, A. Pérez-Rodríguez, *A note on complete evolution algebras*, Arch. Math. 126 (2026), 597–604, DOI 10.1007/s00013-026-02251-0, Section 3.1.
