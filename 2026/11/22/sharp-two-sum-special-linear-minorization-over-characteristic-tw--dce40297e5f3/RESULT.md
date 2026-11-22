# Sharp two-sum special-linear minorization over characteristic-two chain rings

## Finding
Let \(R\) be any finite commutative chain ring of **characteristic two**, of length \(k\geq1\), with maximal ideal \((\pi)\) and residue field \(\mathbb F_q\), where \(q=2^m\) and \(m\geq1\). For \(A\in M_2(R)\), define
\[
N_R(A)=\#\{(U,V)\in\operatorname{SL}_2(R)^2:U+V=A\}.
\]
Then every target occurs, and the **sharp uniform minimum** is
\[
\min_{A\in M_2(R)}N_R(A)=q^{2k-1}(q-1).
\]
Precisely the following targets attain this minimum:

1. \(\operatorname{rank}(\overline A)=1\), or
2. \(\overline A\) is invertible and \(\operatorname{Tr}_{\mathbb F_q/\mathbb F_2}((\det\overline A)^{-1})=1\).

Here bars denote residue reduction. In particular, the number of minimum-fiber targets is
\[
q^{4(k-1)}\left((q-1)(q+1)^2+\frac{q^2(q^2-1)}2\right).
\]
If \(U,V\) are independent uniform elements of \(\operatorname{SL}_2(R)\), their sum distribution \(\mu\) therefore obeys the sharp pointwise minorization
\[
\mu(A)\ \geq\ \frac{q^3}{(q-1)(q+1)^2}\cdot\frac1{|M_2(R)|}
\]
for every \(A\). The factor is **independent of the ring length**.

## Assumptions and scope
The ring is finite, commutative, local principal with a chain of ideals \(R\supsetneq(\pi)\supsetneq\cdots\supsetneq(\pi^{k-1})\supsetneq0\), and \(2=0\) in \(R\). The residue field has \(q\) elements and each successive ideal quotient has \(q\) elements. This includes \(\mathbb F_q[t]/(t^k)\) for every binary prime power \(q\) and every \(k\geq1\). Determinant is the ordinary determinant in the commutative ring; matrix addition is componentwise. For \(A=0\), put its valuation equal to \(k\); for \(A\ne0\), let \(s\in\{0,\dots,k-1\}\) be the minimum valuation of its entries.

## Proof
**1. A trace constraint.** For arbitrary \(2\)-by-\(2\) matrices over a commutative ring, \(\det(X-Y)=\det X+\det Y-\operatorname{tr}(\operatorname{adj}(X)Y)\). Fix \(U\in\operatorname{SL}_2(R)\), so \(\operatorname{adj}(U)=U^{-1}\). The condition \(A-U\in\operatorname{SL}_2(R)\) is equivalent to
\[
\operatorname{tr}(U^{-1}A)=\det A.
\]
(The sign of \(U\) does not matter in characteristic two.) Thus \(N_R(A)\) counts the solutions of this equation in \(\operatorname{SL}_2(R)\).

**2. Primitive rank-one targets.** Suppose \(s=0\) and \(\operatorname{rank}(\overline A)=1\). Over \(\mathbb F_q\), row-column operations with determinant one reduce \(\overline A\) to \(\operatorname{diag}(1,0)\) without affecting the size of the trace fiber. The condition on \(W=U^{-1}\) becomes \(W_{11}=0\), with \(\det W=1\), leaving \(q(q-1)\) choices. At every residue solution, the trace equation restricts nontrivially to the three-dimensional tangent space of \(\operatorname{SL}_2\): its differential would vanish only if \(\overline W\overline A\) were scalar, impossible for a rank-one nonzero matrix. Consequently each residue solution lifts to exactly \(q^2\) solutions at each of the \(k-1\) successive levels. Therefore
\[
N_R(A)=q(q-1)q^{2(k-1)}=q^{2k-1}(q-1).
\]
The same smooth-lifting argument applies to a primitive matrix of residue rank one with any prescribed compatible trace right-hand side.

**3. Invertible targets.** Suppose \(s=0\) and \(\overline A\) is invertible. Write \(\delta=\det A\in R^\times\) and \(C=U^{-1}A\), a bijective substitution between the desired solutions and matrices satisfying \(\det C=\delta\), \(\operatorname{tr}C=\delta\). Their residue characteristic polynomial is \(z^2+\overline\delta z+\overline\delta\), separable because \(\overline\delta\ne0\). Its roots are in \(\mathbb F_q\) precisely when \(\operatorname{Tr}_{\mathbb F_q/\mathbb F_2}(\overline\delta^{-1})=0\): substitute \(z=\overline\delta y\), giving \(y^2+y=\overline\delta^{-1}\). A split-distinct characteristic polynomial has \(q(q+1)\) matrices, whereas an irreducible quadratic has \(q(q-1)\). The two conditions \(\det C=\delta\) and \(\operatorname{tr}C=\delta\) have independent differentials at every residue solution: dependence would force \(C\) scalar, contrary to its nonzero residue trace in characteristic two. Each residue solution therefore has exactly \(q^{2(k-1)}\) lifts. Hence
\[
N_R(A)=q^{2k-1}\begin{cases}q+1,&\operatorname{Tr}(\overline\delta^{-1})=0,\\q-1,&\operatorname{Tr}(\overline\delta^{-1})=1.\end{cases}
\]

**4. Nonprimitive targets.** Suppose \(1\le s<k\), write \(A=\pi^s B\) with \(B\) primitive, and set \(\ell=k-s\). Dividing the trace constraint by \(\pi^s\), in the quotient ring \(R/(\pi^\ell)\), gives
\[
\operatorname{tr}(WB)=\pi^s\det B\pmod{\pi^\ell},\qquad W\in\operatorname{SL}_2(R/(\pi^\ell)).
\]
The reduction map from \(\operatorname{SL}_2(R)\) to this group is surjective, with kernel size \(q^{3s}\), as follows from elementary smooth lifting of the determinant-one equation. If \(\overline B\) has rank one, all \(q(q-1)\) residue trace-zero solutions are smooth and lift through \(\ell-1\) levels with \(q^2\) choices per level. Thus
\[
N_R(A)=q^{2k+s-1}(q-1)>q^{2k-1}(q-1).
\]
If \(\overline B\) is invertible, the residue equation is \(\operatorname{tr}(\overline W\overline B)=0\). Its \(q^2\) determinant-one solutions include precisely one scalar matrix \(\overline W\overline B\), because every element of \(\mathbb F_q\) has a unique square root. The other \(q^2-1\) solutions are non-scalar and smooth, and alone contribute
\[
N_R(A)\ge(q^2-1)q^{2(k-s-1)+3s}=(q^2-1)q^{2k+s-2}
>q^{2k-1}(q-1).
\]
For \(A=0\), \(N_R(0)=|\operatorname{SL}_2(R)|=q^{3k-2}(q^2-1)\), also strictly larger. Thus the equality list is exhaustive.

**5. Count of minimizers and sharp mixing.** There are \((q-1)(q+1)^2\) rank-one \(2\)-by-\(2\) matrices over the residue field. Each specified nonzero determinant has \(q(q^2-1)\) invertible matrices; exactly \(q/2\) nonzero determinant values have absolute trace of their reciprocal equal to one. Each residue matrix has \(q^{4(k-1)}\) lifts. This gives the stated minimizer count. Finally \(|\operatorname{SL}_2(R)|=q^{3k-2}(q^2-1)\) and \(|M_2(R)|=q^{4k}\). Dividing the minimum by the square of the group order and comparing to the uniform additive probability gives the asserted \(q^3/((q-1)(q+1)^2)\); equality at the classified targets shows optimality.

## Verification
The accompanying standalone `verify.py` uses polynomial-bit arithmetic for \(\mathbb F_2[t]/(t^k)\) and explicit polynomial-field arithmetic for \(\mathbb F_4\). It exhaustively enumerates all ordered pairs in \(\operatorname{SL}_2(R)^2\) and all target matrices for \((q,k)=(2,1),(2,2),(2,3),(4,1)\); no statistical sampling is used in those four finite checks. It verifies exact sharp fibers, equality classification, the lower bounds in the divisible full-rank strata, and the minimizer counts. Five additional selected targets in the nonreduced \(\mathbb F_4[t]/(t^2)\) case are checked by separately enumerating all determinant-one first summands, including both invertible absolute-trace strata and a divisible rank-one target. The recorded output ends in `VERIFY_DUAL_OK`. The infinite-family statement rests on the proof above, **not** on the finite enumeration.

## Relationship to prior work
Mináč, Nguyen and Tân (first posted July 1, 2026) motivate two-sum questions for finite rings and normalized units; their matrix-normalization discussion is over fields. Karabulut (2017/2018) establishes the finite-field two-sum existence property for special-linear matrices. Luo and Ji (2025) give a general finite-field representation-count formula; finite-field fiber counts are accordingly **not** claimed as new here. A closely related public 2026 result establishes a sharp two-sum minorization for determinant-one matrices over **odd prime-power residue rings**; the numerical minorization constant is not claimed to be unprecedented. The asserted contribution is the characteristic-two **nonreduced chain-ring** minimum and its precise equality locus, including every even residue-field size and every length. The ring-length-independent minimizer density is a further exact refinement. Prior results for matrices with a field coefficient or odd residue characteristic do not imply these equal-characteristic-two lifts without additional argument.

## Limitations
This theorem concerns \(2\)-by-\(2\) special-linear matrices over *commutative chain rings of characteristic two*. It does not cover arbitrary noncommutative local rings, mixed-characteristic rings with even residue field, or higher matrix dimensions. The complete values of \(N_R(A)\) for all nonprimitive invertible-leading strata are not computed here; a strict lower bound suffices to prove the claimed sharp minimum. Prior-art searches cannot establish historical uniqueness, and some relevant full texts are only available in part. No independent mathematical audit has been performed.

## References
1. J. Mináč, T. T. Nguyen, N. D. Tân, *Sums of units in finite rings and applications to Cayley graphs*, arXiv:2607.00404v1 (first public posting 2026-07-01), https://arxiv.org/html/2607.00404v1.
2. Y. Demiroğlu Karabulut, *Cayley Digraphs of Matrix Rings over Finite Fields*, arXiv:1710.08872v1 (2017), https://arxiv.org/html/1710.08872v1.
3. Y. Luo and Q. Ji, *On the sum of matrices of special linear group over finite field*, AIMS Mathematics 10 (2025), 3642–3651, https://doi.org/10.3934/math.2025168.
4. *Exact two-sum convolution and depth-uniform minorization for special-linear matrices over odd prime-power rings*, publicly indexed 2026 research record (odd residue characteristic), scientific comparison described above.
