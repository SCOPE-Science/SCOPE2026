# Complete two-projector convolution in characteristic-two Hermitian matrix planes

## Finding
Let \(q=2^m\), \(m\ge 1\), \(F=\mathbb F_q\), \(K=\mathbb F_{q^2}\), and let \(\overline z=z^q\). In the additive group \(V=\{S\in M_2(K):S=\overline S^{\mathsf T}\}\), put
\[
\mathcal P=\{P\in V:P^2=P,\ \operatorname{rank}_K(P)=1\},\qquad
r(S)=\#\{(P,Q)\in\mathcal P^2:P+Q=S\}.
\]
Then \(|\mathcal P|=q(q-1)\). The *complete ordered two-projector convolution law* is as follows. If \(\operatorname{tr}(S)\ne0\), then \(r(S)=0\). Otherwise write uniquely
\[
S=\begin{pmatrix}s&w\\\overline w&s\end{pmatrix},\quad s\in F,\quad w\in K,\qquad h=N(w):=w\overline w\in F.
\]
The exact representation number is
\[
r(S)=\begin{cases}
q(q-1),&w=0\text{ and }s\in\{0,1\},\\
q,&w\ne0\text{ and }h\notin\{s^2,(s+1)^2\},\\
0,&\text{otherwise}.
\end{cases}
\]
In particular, for nonscalar trace-zero \(S\), representability is equivalent to *both* \(S\) and \(S+I_2\) being invertible. The scalar exceptions are \(S=0\) and \(S=I_2\).

The exact support size, complement in the trace-zero hyperplane, and additive energy are
\[
|\mathcal P+\mathcal P|=q^3-2q^2-q+4,\qquad
q^3-|\mathcal P+\mathcal P|=2q^2+q-4,
\]
\[
\sum_{S\in V}r(S)^2=q^2(q^3-5q+4).
\]
Equivalently, the nonzero convolution values consist of \(q(q-1)\) at precisely two matrices and \(q\) at precisely \((q-2)(q^2-1)\) others. There are no additional positive values. These conclusions include the degenerate case \(q=2\), where \(\mathcal P+\mathcal P=\{0,I_2\}\).

## Assumptions and scope
The extension \(K/F\) is quadratic with the standard Frobenius involution, and the Hermitian adjoint uses the standard coordinate form. Projectors are *self-adjoint* idempotents of rank one, not arbitrary rank-one matrices or non-self-adjoint idempotents. Addition and convolution are unnormalized, ordered, and taken in the additive group \(V\), which has \(q^4\) elements. The matrix trace is the ordinary trace over \(K\), landing in \(F\) for Hermitian matrices. All claims hold for every integer \(m\ge1\).

## Proof
**1. Parameterization and normalization.** A rank-one idempotent in dimension two has ordinary trace \(1\) and determinant \(0\). Conversely, any Hermitian two-by-two matrix with trace \(1\) and determinant \(0\) is idempotent by the Cayley–Hamilton relation, and necessarily has rank one. Therefore every projector is uniquely
\[
P(a,z)=\begin{pmatrix}a&z\\\overline z&1+a\end{pmatrix},\qquad
a\in F,\ z\in K,\qquad N(z)=a^2+a.
\]
For \(a\in\{0,1\}\), the norm equation has only \(z=0\). At the remaining \(q-2\) values, its nonzero right side has \(q+1\) preimages under \(N:K^\times\to F^\times\), since the norm homomorphism is surjective with kernel of order \(q+1\). Thus
\[
|\mathcal P|=2+(q-2)(q+1)=q(q-1).
\]
Every sum of two projectors has trace \(1+1=0\), and in characteristic two every trace-zero Hermitian matrix has the stated diagonal parameter \(s\).

**2. A trace equation for a pair.** For fixed \(S=\bigl(\begin{smallmatrix}s&w\\\overline w&s\end{smallmatrix}\bigr)\), an ordered pair \((P,Q)\) with \(P+Q=S\) is determined by \(P=P(a,z)\); its partner is \(Q=P(a+s,z+w)\). Writing the two determinant-zero conditions and subtracting them gives
\[
\operatorname{Tr}_{K/F}(z\overline w)=s^2+s+N(w)=:L,
\]
where \(\operatorname{Tr}_{K/F}(u)=u+\overline u\). This linear equation, together with \(a^2+a=N(z)\), is necessary and sufficient.

**3. Scalar targets.** When \(w=0\), the relative-trace equation is satisfied exactly when \(s^2+s=0\), i.e. \(s\in\{0,1\}\). Each of the \(q(q-1)\) projectors then yields a unique partner. These targets are \(0\) and \(I_2\). All other scalar trace-zero targets have no representations.

**4. Nonscalar targets and a complete Artin–Schreier fiber count.** Suppose \(w\ne0\), set \(h=N(w)\in F^\times\) and \(t=L/h\in F\). Choose \(\beta\in K\) with \(\operatorname{Tr}_{K/F}(\beta)=1\), possible since relative trace is onto. Put \(e=N(\beta)\in F\). The element \(\beta\notin F\) solves \(X^2+X+e=0\), which is irreducible over \(F\); hence the absolute trace \(\operatorname{Tr}_{F/\mathbb F_2}(e)=1\) by the Artin–Schreier criterion.

The solutions of the relative-trace equation are precisely
\[
z=w(x+t\beta),\qquad x\in F.
\]
Indeed, \(\operatorname{Tr}_{K/F}(z\overline w)=h\operatorname{Tr}_{K/F}(x+t\beta)=ht=L\). For these candidates,
\[
N(z)=h\bigl(x^2+tx+t^2e\bigr).
\]
For a fixed \(z\), the equation \(a^2+a=N(z)\) has exactly two solutions \(a\in F\) if \(\operatorname{Tr}_{F/\mathbb F_2}(N(z))=0\), and none otherwise. If \(\sqrt h\) denotes the unique field square root of \(h\), trace invariance under squaring gives the exact affine \(\mathbb F_2\)-linear expression
\[
\operatorname{Tr}_{F/\mathbb F_2}(N(z))
=\operatorname{Tr}_{F/\mathbb F_2}\!\bigl((\sqrt h+ht)x+ht^2e\bigr).
\]
If \(\sqrt h+ht\ne0\), this nonzero linear functional on the \(m\)-dimensional \(\mathbb F_2\)-space \(F\) takes zero on exactly \(q/2\) values of \(x\). Each contributes two \(a\)'s, giving exactly \(q\) ordered pairs.

If \(\sqrt h+ht=0\), then \(t=h^{-1/2}\) and \(ht^2=1\); the displayed absolute trace is identically \(\operatorname{Tr}_{F/\mathbb F_2}(e)=1\), so no \(a\) exists. Finally, the exceptional condition is equivalent to
\[
L=\sqrt h\iff s^2+s+h=\sqrt h
\iff(s+\sqrt h)(s+\sqrt h+1)=0
\iff h\in\{s^2,(s+1)^2\}.
\]
This proves the complete fiber formula without any finite-enumeration assumption. For the equivalent determinant criterion, use \(\det S=s^2+N(w)\) and \(\det(S+I_2)=(s+1)^2+N(w)\).

**5. Exact support and energy.** Each nonzero norm \(h\in F^\times\) is realized by exactly \(q+1\) values of \(w\). For \(s=0\) or \(1\), precisely one forbidden norm lies in \(F^\times\); for every other \(s\), precisely two distinct forbidden norms do. Hence there are
\[
2(q-2)(q+1)+(q-2)(q-3)(q+1)=(q-2)(q^2-1)
\]
nonscalar targets with \(r(S)=q\), plus the two scalar targets of weight \(q(q-1)\). Summing their squared weights proves the energy formula:
\[
2q^2(q-1)^2+q^2(q-2)(q^2-1)=q^2(q^3-5q+4).
\]
The support/complement counts follow, completing the proof.

## Verification
The self-contained `checker.py` constructs \(\mathbb F_{q^2}\) via irreducible binary polynomials for \(q\in\{2,4,8,16\}\), builds **all** trace-one rank-one Hermitian projectors, enumerates **all ordered pairs**, and compares their target frequencies with the theorem for every trace-zero target. It also verifies the exact support and additive-energy identities. The observed triples \((q,|\mathcal P|,|\mathcal P+\mathcal P|)\) are \((2,2,2)\), \((4,12,32)\), \((8,56,380)\), and \((16,240,3572)\). The full-range theorem is mathematical, not inferred from this finite check.

## Relationship to prior work
The finite Hermitian-form literature supplies the geometric and harmonic framework. Fulton (1977), Theorem 5.1, counts matrices of prescribed rank solving \(XAX^*=B\); its condition does not fix the **two individual column norms**, as a projector pair decomposition \(S=uu^*+vv^*\) does. Thus its counts do not directly give \(r(S)\). Gow–Lavrauw–Sheekey–Vanhove (2012), Sections 3–4, study rank-distance sets and additive characters of full Hermitian rank classes; this does not impose the trace-one idempotent restriction. Orel–Kuzma (2009), Theorem 2.1, classifies additive rank-one nonincreasing maps, not the additive convolution of idempotents. The present characteristic-two two-projector support and complete fiber count is a more restrictive orbit computation than rank-only data. These comparisons are not a claim of exhaustive historical priority.

## Limitations
The statement concerns only dimension two, quadratic extensions, characteristic two, standard-adjoint self-adjoint idempotents, and unweighted ordered two-fold convolution. It does not classify higher-rank or non-self-adjoint projector sums, arbitrary convolution powers, or spectral extremizers. Standard algebraic prerequisites include norm surjectivity, Artin–Schreier solvability, and Cayley–Hamilton. Searches cannot establish absolute uniqueness of the formula, and an unlocated equivalent expression in the finite-unitary or representation-number literature remains a historical-priority risk. Independent audit is not claimed.

## References
1. J. D. Fulton, “Representations by Hermitian Forms in a Finite Field of Characteristic Two,” *Canadian Journal of Mathematics* 29 (1977), 169–179, DOI: 10.4153/CJM-1977-017-5, especially equation (1.3) and Theorem 5.1.
2. M. Orel and B. Kuzma, “Additive rank-one nonincreasing maps on Hermitian matrices over the field GF(4),” *Electronic Journal of Linear Algebra* 18 (2009), DOI: 10.13001/1081-3810.1326, especially Theorem 2.1.
3. R. Gow, M. Lavrauw, J. Sheekey, and F. Vanhove, “Constant rank-distance sets of hermitian matrices and partial spreads in hermitian polar spaces,” arXiv:1208.1903, first publicly posted 2012-08-09; especially Sections 3–4.
