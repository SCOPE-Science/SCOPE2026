# Characteristic-two Rota–Baxter orbit profiles on split square-zero local algebras

## Finding

Let \(q=2^s\) with integer \(s\ge1\), let \(V=\mathbf F_q^n\) with \(n\ge1\), and let \(A=\mathbf F_q\oplus V\) be the commutative unital algebra whose multiplication is
\[
 (a,v)(b,w)=(ab,aw+bv).
\]
Every weight-zero Rota–Baxter operator \(P:A\to A\) has a *unique* description
\[
 P(a+v)=a u+T(v),\qquad u\in V,\quad T\in\operatorname{End}_{\mathbf F_q}(V),\quad T^2=0.
\]
Conversely, all such pairs \((u,T)\) define weight-zero Rota–Baxter operators. There is **no** condition that \(T(u)=0\) in characteristic two.

Put \(H_{n,r}(q)={n\brack r}_q{n-r\brack r}_q|\mathrm{GL}_r(\mathbf F_q)|\), where the brackets denote Gaussian binomial coefficients and \(|\mathrm{GL}_0(\mathbf F_q)|=1\). For every integer \(0\le r\le\lfloor n/2\rfloor\), exactly \(H_{n,r}(q)\) endomorphisms \(T\) satisfy \(T^2=0\) and \(\operatorname{rank}T=r\). Hence the total number of weight-zero Rota–Baxter operators is
\[
 \boxed{N_n(q)=q^n\sum_{r=0}^{\lfloor n/2\rfloor}{n\brack r}_q{n-r\brack r}_q|\mathrm{GL}_r(\mathbf F_q)|.}
\]

More precisely, algebra-automorphism conjugacy has exactly the following strata at each rank \(r\) of \(T\). Every nonempty line of the table is **one conjugacy class**, and the final column gives the exact size of that class among all operators.

| Type of \(u\) | Existence | Class size |
|---|---|---|
| \(u=0\) | every \(r\) | \(H_{n,r}(q)\) |
| \(u\in\operatorname{im}T\setminus\{0\}\) | \(r>0\) | \(H_{n,r}(q)(q^r-1)\) |
| \(u\in\ker T\setminus\operatorname{im}T\) | \(n>2r\) | \(H_{n,r}(q)(q^{n-r}-q^r)\) |
| \(u\notin\ker T\) | \(r>0\) | \(H_{n,r}(q)(q^n-q^{n-r})\) |

In particular, the number of conjugacy classes is \(4m+1\) if \(n=2m\ge2\), and \(4m+2\) if \(n=2m+1\ge1\). Every such operator satisfies \(P^3=0\), and \(P^2\ne0\) holds **exactly** for the fourth type in the table. For \(n\ge2\) the nilpotency bound three is sharp; the exact number of operators of nilpotency index three is
\[
 \boxed{\sum_{r=1}^{\lfloor n/2\rfloor}H_{n,r}(q)\bigl(q^n-q^{n-r}\bigr).}
\]
For \(n=1\), all operators are square-zero. For example, for \((q,n)=(2,2)\) there are exactly \(16\) operators in five automorphism-conjugacy classes of respective sizes \(1,3,3,3,6\); precisely six have nilpotency index three.

## Assumptions and scope

The field \(\mathbf F_q\) is an arbitrary finite field of characteristic two, including nonprime fields. The algebra has one unit and an \(n\)-dimensional square-zero ideal, so \(A\cong\mathbf F_q[x_1,\ldots,x_n]/(x_1,\ldots,x_n)^2\). All maps and automorphisms are \(\mathbf F_q\)-linear, and conjugacy means \(P\sim\alpha P\alpha^{-1}\) for an \(\mathbf F_q\)-algebra automorphism \(\alpha\) of \(A\). A weight-zero Rota–Baxter operator obeys
\[
 P(x)P(y)=P\bigl(P(x)y+xP(y)\bigr)\qquad(x,y\in A).
\]
No normalization by nonzero scalar multiplication of operators is performed. When the table gives zero elements for a putative type, that type is omitted entirely.

## Proof

**1. Classification of maps.** For \(v\in V\), write \(P(v)=f(v)1+T(v)\), with \(f:V\to\mathbf F_q\) linear and \(T:V\to V\) linear. Apply the defining identity to \((v,v)\). Comparison of scalar parts gives \(f(v)^2=2f(v)^2\), hence \(f(v)=0\) in a field. Thus \(P(V)\subseteq V\) in every characteristic. Now write \(P(1)=a1+u\). The identity for \((1,1)\) yields \(a^2=2a^2\) on scalar parts, so \(a=0\), and yields \(2T(u)=0\) on radical parts. Applying the identity to \((1,v)\) gives \(T^2(v)=0\) for every \(v\in V\): the left side is zero, the right is \(P(P(v))=T^2(v)\). In characteristic two, \(2T(u)=0\) imposes no additional condition. Conversely, if \(P(a+v)=a u+T(v)\) with \(T^2=0\), then both sides vanish: the product of the two values of \(P\) lies in \(V^2=0\), and
\[
 P\bigl(P(a+v)(b+w)+(a+v)P(b+w)\bigr)
 =P\bigl(b(au+T(v))+a(bu+T(w))\bigr)=T^2(bv+aw)=0,
\]
where the two \(ab u\) terms cancel in characteristic two. Therefore the classification is necessary and sufficient.

**2. Number of square-zero maps.** If \(T^2=0\) and \(\operatorname{rank}T=r\), then \(U=\operatorname{im}T\) has dimension \(r\) and \(K=\ker T\) has dimension \(n-r\), with \(U\subseteq K\). Choose \(U\) in \({n\brack r}_q\) ways and \(K\supseteq U\) in \({n-r\brack r}_q\) ways. For the chosen flag, \(T\) is equivalent to a linear isomorphism \(V/K\to U\), having \(|\mathrm{GL}_r(\mathbf F_q)|\) possibilities. These choices are bijective. Each \(T\) admits \(q^n\) choices for \(u\), proving the count.

**3. Complete orbit classification.** The Jacobson radical \(V\) is characteristic, so an algebra automorphism fixes \(1\) and acts as an arbitrary \(g\in\mathrm{GL}(V)\) on \(V\). Conjugation carries \((u,T)\) to \((gu,gTg^{-1})\). Square-zero maps of rank \(r\) are all similar (their Jordan form consists of \(r\) blocks of size two and \(n-2r\) zero blocks). Fix \(T\) and choose a vector-space decomposition \(V=U\oplus F\oplus W\) with \(U=\operatorname{im}T\), \(F\stackrel{T}{\longrightarrow}U\) an isomorphism and \(\ker T=U\oplus W\). In matched bases, \(T(e,f,w)=(f,0,0)\). Its invertible centralizer consists exactly of block matrices
\[
 g=\begin{pmatrix}A&B&C\\0&A&0\\0&D&E\end{pmatrix},
 \qquad A\in\mathrm{GL}_r(\mathbf F_q),\quad E\in\mathrm{GL}_{n-2r}(\mathbf F_q),
\]
with \(B,C,D\) arbitrary of compatible sizes. Thus \(g(e,f,w)=(Ae+Bf+Cw,Af,Df+Ew)\). If \(f\ne0\), choices of \(A,B,D\) make all such vectors conjugate. If \(f=0\) and \(w\ne0\), the blocks \(E,C\) make all such vectors conjugate. If \(f=w=0\) and \(e\ne0\), \(A\) is transitive; the zero vector is fixed. These are precisely the four table types. The numbers of respective vectors are \(1\), \(q^r-1\), \(q^{n-r}-q^r\), and \(q^n-q^{n-r}\). Multiplying each by the number \(H_{n,r}(q)\) of conjugate maps \(T\) gives all orbit sizes. Summing the possible types over ranks yields the stated class counts.

**4. Nilpotency threshold.** Directly, \(P^2(a+v)=aT(u)\) and \(P^3=0\). Thus \(P^2\ne0\) iff \(u\notin\ker T\). There are \(q^n-q^{n-r}\) such vectors for each rank-\(r\) map, and the resulting sum follows. For \(n\ge2\), take independent \(e,f\in V\), let \(T(f)=e\), and set \(u=f\) (with \(T\) zero on all other basis elements); then \(P^2(1)=e\ne0\), proving sharpness.

## Verification

The accompanying `rb_squarezero_checker.py` independently enumerates **all** \(\mathbf F_q\)-linear endomorphisms of \(A\) for \((q,n)=(2,1),(3,1),(2,2),(3,2),(2,3)\), tests the defining Rota–Baxter relation on all pairs of algebra basis vectors, and compares with the predicted block-form characterization in the corresponding characteristic. For each pair it also enumerates all algebra automorphisms and their conjugacy orbits, confirming the sizes. The output is `CHECKER_OK`; in particular it confirms the predicted five class sizes \((1,3,3,3,6)\) at \((q,n)=(2,2)\) and six classes totaling \(176\) at \((q,n)=(2,3)\). The odd-characteristic cases serve as boundary controls rather than instances of the characteristic-two theorem. Exhaustive tests for finitely many dimensions and prime fields cannot replace the general proof, which applies to every even prime power.

## Relationship to prior work

Gubarev, *Rota–Baxter operators on unital algebras* (arXiv:1805.00723, first submitted 2018-05-02), establishes general nilpotence results in characteristic zero and motivates the nilpotency index as an invariant. Farooq, *Rota Baxter Operators on Truncated Polynomial Algebras* (arXiv:2605.15670, 2026), treats **the same algebra** over fields of **characteristic zero**, proving the square-zero condition on the operator; in characteristic two, the present family has an additional nilpotency-index-three stratum not admitted by that theorem. The finite-field cardinality and precise automorphism-orbit-size formulas are not stated there. Zheng, Guo and Rosenkranz, *Classification of Rota-Baxter operators on semigroup algebras of order two and three* (2019), concern small-dimensional semigroup algebras and work under characteristic-zero assumptions, without providing all-dimensional characteristic-two counts. A publicly indexed result on weight-zero operators over the four-dimensional exterior algebra over \(\mathbf F_2\) concerns a different multiplication algebra with nonzero radical-square and does not imply the formulas here.

## Limitations

Only **weight zero** and **split square-zero local algebras** are treated. The automorphism group is the algebra automorphism group \(\mathrm{GL}(V)\), not the full general linear group on \(A\), nor scalar multiples of operators. The characteristic-zero normal form from prior work is not claimed as new. The exact finite-field enumeration and positive-characteristic comparison have been checked against the cited literature and targeted searches but have not received independent external mathematical review; differently indexed equivalent results may exist. Computational checks cover only \(q\in\{2,3\}\) and small dimensions; the theorem for all \(q=2^s\) follows from the proof, not from extrapolation.

## References

1. V. Gubarev, *Rota-Baxter operators on unital algebras*, arXiv:1805.00723, first version 2018-05-02, https://arxiv.org/abs/1805.00723.
2. A. Farooq, *Rota Baxter Operators on Truncated Polynomial Algebras*, arXiv:2605.15670, 2026-05-15, https://arxiv.org/abs/2605.15670.
3. S. Zheng, L. Guo and M. Rosenkranz, *Classification of Rota-Baxter operators on semigroup algebras of order two and three*, Communications in Algebra 47 (2019), 3094–3116, https://pmc.ncbi.nlm.nih.gov/articles/PMC7083595/.
