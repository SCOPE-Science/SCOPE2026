# A two-step Fourier recurrence for singular matrices over finite chain rings

## Finding
Let \(R\) be a commutative finite chain ring of nilpotency length \(m\ge1\), with maximal ideal \((\pi)\), \(\pi^m=0\ne\pi^{m-1}\), and residue field of order \(q\). Fix an additive character \(\psi\) whose kernel contains no nonzero ideal, and use \(\langle T,A\rangle=\sum_{i,j=1}^2T_{ij}A_{ij}\). For the determinant-zero set \(C_m=\{A\in M_2(R):\det A=0\}\), put
\[
 F_m(T)=\sum_{A\in C_m}\psi(\langle T,A\rangle).
\]
Each \(T\) has Smith form \(\operatorname{diag}(\pi^a,\pi^b)\), with \(0\le a\le b\le m\), where \(\pi^m=0\). Write \(F_m(a,b)\) for this Fourier coefficient. All coefficients depend only on \(m,q,a,b\), not on the characteristic or isomorphism type of the chain ring.

Here is a complete two-step recursion. Set \(F_0(0,0)=1\). At length one:
\[
 F_1(0,0)=-q,\qquad F_1(0,1)=q^2-q,\qquad F_1(1,1)=q^3+q^2-q.
\]
For \(m\ge2\), define \(U=q^{m-1}(q-1)\), \(H=q^{2m}-q^{2m-2}\), and
\[
 N_0=\begin{cases}q^aU,&a<m,\ b=m,\\H,&a=b=m,\\0,&\text{otherwise},\end{cases}
\qquad
 N_s=\begin{cases}0,&b\le m-2,\\q^{a+1}U,&a\le m-2<b,\\H,&a\ge m-1.\end{cases}
\]
Then
\[
 P_m(a,b)=\frac{q^{2m}N_0-q^{2m-2}N_s}{U},
 \qquad
 F_m(a,b)=P_m(a,b)+\mathbf1_{a\ge1}q^4F_{m-2}(\min(a-1,m-2),\min(b-1,m-2)).
\]
For \(m=2\), the recursive term invokes the defined length-zero case. The expression is always an integer. Together with the usual Smith-type class counts, it gives the exact complete Fourier-coefficient distribution for every nilpotency length.

The first case beyond length two has an especially simple evaluated form. For \(m=3\), with rows listed as \((a,b):F_3(a,b)\), the full table is
\[
\begin{array}{c|c@{\qquad}c|c}
(0,0)&0&(0,1)&0\\
(0,2)&-q^5&(0,3)&q^5(q-1)\\
(1,1)&-q^5&(1,2)&-q^5\\
(1,3)&q^7-q^5&(2,2)&-q^5\\
(2,3)&q^8-q^5&(3,3)&q^9+q^8-q^5
\end{array}.
\]
Thus the four negative Smith types are exactly \((0,2),(1,1),(1,2),(2,2)\), and the two zero types are exactly \((0,0),(0,1)\). Their total negative multiplicity is
\[
 Z_-(q)=q^{10}-q^8-q^5+q^4-q^2+q.
\]
For the Fourier projection retaining frequencies in \(C_3\), the sharp norms, with unnormalized counting \(\ell^1\) and \(\ell^\infty\), are equal and exactly
\[
 \|P_{C_3}\|_{1\to1}=\|P_{C_3}\|_{\infty\to\infty}
 =1+\frac{2q^5 Z_-(q)}{q^{12}}
 =2q^3-2q+1-\frac2{q^2}+\frac2{q^3}-\frac2{q^5}+\frac2{q^6}.
\]

## Assumptions and scope
The ring is arbitrary finite commutative principal local with exactly \(m+1\) ideals (a chain ring), with residue cardinality \(q\) a prime power. There is no assumption that \(R\) is a Galois ring: for instance, rings of the form \(\mathbb F_q[\varepsilon]/(\varepsilon^m)\) are included, as are \(\mathbb Z/p^m\mathbb Z\). A generating character exists because a finite chain ring is Frobenius; the resulting perfect additive pairing is used throughout. All valuations and Smith types refer to entries over \(R\), not to determinant rank over a field. The claimed sharp norm is only evaluated in closed form for \(m=3\), while the recurrence determines all lengths.

## Proof
**Invariance.** Invertible row/column operations preserve the condition \(\det A=0\) and transform Fourier frequencies contragrediently, hence \(F_m(T)\) depends only on the Smith type. The usual Smith normal form exists over a principal chain ring.

**Field base.** For \(m=1\), the rank-one nonzero matrices over \(\mathbb F_q\) have character sum \((q^{4-r}-2q^2+1)/(q-1)\) against a dual matrix of rank \(r\). Add the zero matrix to obtain the three displayed base values. The empty ring at length zero contributes one.

**Primitive matrices.** If \(\overline A\) has rank one modulo \(\pi\) and \(\det A=0\), a unit-pivot elimination expresses \(A=uv^{\mathsf T}\) with both vectors primitive (at least one unit coordinate). Every such matrix has exactly \(U=|R^\times|\) representations of this form, by \((u,v)\sim(tu,t^{-1}v)\). Fix primitive \(u\) and sum over primitive \(v\). Orthogonality of generating characters gives
\[
 \sum_{v\text{ primitive}}\psi(v^{\mathsf T}T^{\mathsf T}u)
 =q^{2m}\mathbf1_{T^{\mathsf T}u=0}
 -q^{2m-2}\mathbf1_{T^{\mathsf T}u\in(\pi^{m-1}R)^2}.
\]
For diagonal Smith type \((a,b)\), the two numbers of primitive \(u\) satisfying these conditions are precisely \(N_0\) and \(N_s\) displayed above. Indeed, \(\operatorname{ann}(\pi^a)=\pi^{m-a}R\) has \(q^a\) elements, and the preimage of \(\pi^{m-1}R\) under multiplication by \(\pi^a\) has \(q^{\min(a+1,m)}\) elements. Subtract the pairs with both coordinates nonunits. Dividing the summed character identity by \(U\) yields \(P_m\).

**Nonprimitive matrices.** Every remaining determinant-zero matrix is \(A=\pi B\), where \(B\) is a matrix over the quotient of length \(m-1\) satisfying \(\det B=0\pmod{\pi^{m-2}}\). Each \(B\) modulo \(\pi^{m-2}\) has \(q^4\) lifts. Summing the character over the lift fiber vanishes unless \(T\) is divisible by \(\pi\). When \(T=\pi S\), that sum is \(q^4\) times the length-\(m-2\) Fourier coefficient at the image of \(S\), which has Smith valuations \(\min(a-1,m-2)\) and \(\min(b-1,m-2)\). This establishes the recursion for every \(m\ge2\), and induction proves the complete spectrum statement.

**Length three and its norm.** Substituting the field and length-zero bases twice gives the ten Smith values in the table. Denote \(R_1=(q-1)(q+1)^2\), the number of rank-one matrices over \(\mathbb F_q\), and \(R_2=q(q-1)(q^2-1)\), the number of invertible \(2\)-by-\(2\) matrices. The four negative types have multiplicities, respectively,
\[
 R_1(q-1)q^6,\quad q^4R_2,\quad R_1(q-1)q^3,\quad R_2.
\]
Their sum is \(Z_-(q)\) as displayed. All negative coefficients equal \(-q^5\); every other coefficient is nonnegative. Fourier inversion gives \(\sum_TF_3(T)=|M_2(R)|=q^{12}\), because the zero matrix belongs to \(C_3\). Therefore \(\sum_T|F_3(T)|=q^{12}+2q^5Z_-(q)\). Convolution by the normalized inverse transform of \(\mathbf1_{C_3}\) is exactly the Fourier projection. Its \(\ell^1\) and \(\ell^\infty\) operator norms equal the \(\ell^1\)-mass of the convolution kernel, proving the sharp formula. Both norms are attained by a point mass or a suitable bounded phase vector.

## Verification
The accompanying `CHECK.py` builds the determinant-zero indicator independently, performs four-dimensional finite cyclic Fourier transforms for \(R=\mathbb Z/p^m\mathbb Z\) with \((p,m)=(2,1),(2,2),(2,3),(3,1),(3,2),(3,3)\), and compares **every** Fourier coefficient against the Smith-recursive formula. It additionally uses an exact integer Walsh--Hadamard transform for the distinct equal-characteristic rings \(\mathbb F_2[\varepsilon]/(\varepsilon^m)\), for \(m=2,3\). This corroborates ring-type independence at the smallest nonlinear level. The checker requires Python 3 and NumPy, and also tests the exact length-three negative multiplicity and norm. Finite tests do not replace the induction proof.

## Relationship to prior work
The 2016 preprint by Choosuwan, Jitman and Udomkavanich determines the number of matrices of any prescribed determinant over finite principal ideal rings, including \(\#C_m\), but does not evaluate the additive Fourier transform at nonzero matrix frequencies. Cao's 2011 paper studies a different orbital association scheme on right-invertible rectangular matrices. Watanabe's July 2026 paper determines the complete Smith-type eigenmatrix over \(\operatorname{GR}(p^2,r)\), **so the length-two Galois-ring specialization is already implied by that stronger work and is not claimed new**. The contribution assessed here is the characteristic-independent, arbitrary-nilpotency two-step formula and the first length-three explicit sign and endpoint-norm law. No general all-length determinant-zero Fourier recursion was identified in the checked sources; this is not a claim of exhaustive historical priority.

## Limitations
No explicit simplified endpoint norm is claimed for every length \(m\), although the recurrence computes each coefficient. The four type-class multiplicities in the length-three proof are exact; no assertion is made about larger matrix sizes. The full existing literature on higher-length translation schemes was not exhaustively accessible, leaving a risk of stronger prior formulas. No independent mathematical audit has been performed.

## References
- Y. Cao, “Association Schemes and Directed Graphs Determined by Orbitals of General Linear Groups Over Finite Chain Rings,” *Communications in Algebra* **39** (2011), 220–236, DOI 10.1080/00927870903390652; online 20 January 2011.
- P. Choosuwan, S. Jitman, P. Udomkavanich, “Determinants of Matrices over Commutative Finite Principal Ideal Rings,” arXiv:1605.06826v1, 22 May 2016, particularly Section 3.
- Y. Watanabe, “Bivariate Affine \(q\)-Krawtchouk Polynomials and Association Schemes over Galois Rings,” arXiv:2607.21913v1, 24 July 2026, particularly Theorem 4.2 and Example 4.3.
