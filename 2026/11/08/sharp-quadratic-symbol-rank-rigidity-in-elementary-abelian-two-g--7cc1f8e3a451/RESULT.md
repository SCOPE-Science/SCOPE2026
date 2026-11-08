# Sharp quadratic-symbol rank rigidity in elementary abelian two-group algebras

## Finding
Let \(k\) be any field of characteristic \(2\), let \(n\geq 0\), and let \(A=k[(C_2)^n]\) with augmentation ideal \(J\). Choosing group generators gives an augmentation basis \(x_1,\ldots,x_n\) in which
\[
A\cong k[x_1,\ldots,x_n]/(x_1^2,\ldots,x_n^2)=\bigoplus_{j=0}^n A_j.
\]
Every \(a\in J^2\) has a uniquely determined degree-two term \(\omega\in A_2\) and higher term \(\eta\in\bigoplus_{j\geq3}A_j\). The alternating coefficient matrix of \(\omega=\sum_{i<j}b_{ij}x_ix_j\) is \(B=(b_{ij})\), with \(b_{ji}=b_{ij}\) and \(b_{ii}=0\). Put \(\operatorname{rank}B=2r\) and \(s=n-2r\).

**Sharp rigidity theorem.** If \(s\leq2\), *every* higher-order lift \(a=\omega+\eta\) has the same multiplication-operator rank:
\[
\operatorname{rank}_k(m_a)=2^{n-1}-2^{n-r-1}\qquad(r\geq1),
\]
with rank \(0\) when \(r=0\). Equivalently, the square-zero map \(m_a:u\mapsto au\) has precisely \(2^{n-1}-2^{n-r-1}\) size-two Jordan blocks and \(2^{n-r}\) size-one blocks. Thus its two-periodic homology \(\ker(m_a)/\operatorname{im}(m_a)\) has dimension \(2^{n-r}\). (The rank formula can uniformly be written as \((2^n-2^{n-r})/2\), including \(r=0\).)

This is a **sharp nullity threshold**: for *every* \(r\geq0\) and \(s\geq3\), there exist \(\omega\) of alternating rank \(2r\) and two lifts with distinct multiplication ranks. With variables \(u_i,v_i\) (\(1\leq i\leq r\)) and \(z_j\) (\(1\leq j\leq s\)), take
\[
\omega=\sum_{i=1}^r u_iv_i,\qquad
 a_0=\omega,\qquad a_1=\omega+z_1z_2z_3.
\]
Their ranks are, exactly,
\[
\operatorname{rank}(m_{a_0})=(2^n-2^{n-r})/2,
\quad\operatorname{rank}(m_{a_1})=\operatorname{rank}(m_{a_0})+2^{r+s-3}.
\]
In particular, for \(n=5\), the two elements \(x_1x_2\) and \(x_1x_2+x_3x_4x_5\) have the **same rank-two quadratic symbol** but multiplication ranks \(8\) and \(10\).

For finite \(k=\mathbb F_q\), \(q\) a power of \(2\), there are
\[
N_{n,r}(q)=\begin{bmatrix}n\\2r\end{bmatrix}_q\frac{|\mathrm{GL}_{2r}(\mathbb F_q)|}{|\mathrm{Sp}_{2r}(\mathbb F_q)|}
\]
quadratic symbols of alternating rank \(2r\), with the fraction interpreted as \(1\) at \(r=0\). Here the bracket is the Gaussian binomial coefficient. Thus for \(s\leq2\), exactly \(N_{n,r}(q)q^{\sum_{j=3}^n\binom nj}\) elements of \(J^2\) have that quadratic rank and the multiplication rank above.

A complete, low-dimensional consequence (not merely a count of homogeneous quadratics) is that **every** \(a\in J^2\) for \(n=4\) contributes to the generating polynomial
\[
\sum_{a\in J^2}T^{\operatorname{rank}_k(m_a)}=
1+(q-1)T+q(q^4-1)T^2
+q^5(q-1)(q^2+1)(q^2+q+1)T^4
+q^7(q-1)(q^3-1)T^6.
\]
Hence ranks \(3\) and \(5\) are impossible in this natural first complete rank census, although ranks \(0,1,2,4,6\) all occur.

## Assumptions and scope
The ground field has characteristic two; the finite-field enumeration requires \(q=2^e\) with integer \(e\geq1\). The group algebra is the full, commutative group algebra of an elementary abelian group of exponent two, and the multiplication maps act on its *whole* regular module. The claim concerns the fixed degree-two augmentation symbol and *arbitrary*, not necessarily homogeneous, terms of degree at least three. The symbol's alternating rank is invariant under invertible linear changes of augmentation generators. The dimension \(s\) is the radical/nullity of the associated alternating form. The theorem does not assert rigidity for \(s\geq3\), nor a complete spectrum for all such perturbations.

## Proof
**1. Algebra and square-zero differential.** For each chosen group generator \(g_i\), put \(x_i=g_i-1\). Since the group is abelian and the characteristic is two, \(x_i^2=0\); the distinct squarefree monomials form a basis. Every element of \(J\) has square zero by the Frobenius identity, so \(m_a^2=0\). For a square-zero map on a vector space of dimension \(2^n\), homology dimension equals \(2^n-2\operatorname{rank}(m_a)\).

**2. Homology of the quadratic principal part.** A change of degree-one basis puts any alternating \(\omega\) of rank \(2r\) into \(\sum_{i=1}^r u_iv_i\), leaving \(s\) unused generators. For a single pair, the complex \(k[ u,v]/(u^2,v^2)\), with differential multiplication by \(uv\), has an acyclic pair \(1\mapsto uv\) and homology spanned by the classes of \(u\) and \(v\), both in degree one. Since characteristic two removes tensor-product differential signs, repeated tensor-product cancellation gives
\[
H(A,m_\omega)\cong\bigotimes_{i=1}^r k\{[u_i],[v_i]\}\otimes k[z_1,\ldots,z_s]/(z_1^2,\ldots,z_s^2)
\]
as graded vector spaces. Its Hilbert polynomial is \((2t)^r(1+t)^s\), its dimension is \(2^{r+s}=2^{n-r}\), and its degrees are contained in the interval \([r,r+s]\). This proves the stated rank for \(\eta=0\).

**3. Finite cancellation lemma for all higher terms.** We give the linear-algebra reason the nonhomogeneous perturbations are controlled, rather than assuming invariance from finite experiments. Suppose a graded finite-dimensional vector space \(C\) has square-zero differential \(d_0\) raising degree exactly two. Choose graded complements \(C=B\oplus H\oplus L\), with \(B=\operatorname{im}d_0\), \(\ker d_0=B\oplus H\), and \(d_0:L\to B\) an isomorphism. Let \(d=d_0+\delta\), with \(d^2=0\) and \(\delta\) raising degree at least three. The block \(d_{BL}:L\to B\) is invertible: it is \(d_0|_L\) plus a strictly degree-raising perturbation after multiplying by its inverse, so its inverse is a finite geometric series. Elementary elimination of the matched \(L\to B\) pairs reduces \((C,d)\) to the complex on \(H\) with effective differential
\[
 d_H=d_{HH}-d_{HL}(d_{BL})^{-1}d_{BH}.
\]
This standard cancellation identity follows by replacing each \(h\in H\) by \(h-(d_{BL})^{-1}d_{BH}h\) and eliminating the resulting contractible pairs; it is a direct invertible basis elimination preserving homology. The direct block \(d_{HH}\) raises degree at least three; the second term raises degree at least four, since its two outer maps raise at least three and its inverse has lowest degree shift minus two. Therefore \(d_H\) strictly raises degree by at least three. If the homology representative space \(H\) is supported in at most three consecutive degrees, \(d_H=0\) and \(\dim H(C,d)=\dim H(C,d_0)\).

Apply this lemma with \(C=A\), \(d_0=m_\omega\) and \(\delta=m_\eta\). Because \(H(A,m_\omega)\) is supported in \([r,r+s]\), the condition \(s\leq2\) makes the effective differential vanish. The homology dimension and therefore the rank and Jordan type are rigid for every higher-order lift.

**4. Sharpness for each larger nullity.** Suppose \(s\geq3\) and put \(b=z_1z_2z_3\). The differential \(m_{\omega+b}\) on the tensor factors is the sum of multiplication by \(\omega\) and multiplication by \(b\). Tensor-product cancellation yields
\[
\dim H(A,m_{\omega+b})=\dim H(A_{2r},m_\omega)\cdot\dim H(A_s,m_b).
\]
Here \(\operatorname{rank}m_b=2^{s-3}\), because multiplication by \(b\) maps the \(2^{s-3}\) monomials avoiding \(z_1,z_2,z_3\) bijectively onto the monomials containing all three. Thus the second homology dimension is \(2^s-2^{s-2}=3\cdot2^{s-2}\), and the product is \(3\cdot2^{r+s-2}\). Substituting into \(\operatorname{rank}=(2^n-\dim H)/2\) gives the exact rank increase \(2^{r+s-3}\). This establishes sharpness even when \(\omega=0\).

**5. Finite-field counts.** To count alternating symbols of rank \(2r\), first select their \(s\)-dimensional radical: \(\begin{bmatrix}n\\2r\end{bmatrix}_q\) choices. Then equip the \(2r\)-dimensional quotient with a nondegenerate alternating form; this is a single \(\mathrm{GL}_{2r}\)-orbit with stabilizer \(\mathrm{Sp}_{2r}\). The number of independent higher-degree coefficients is \(\sum_{j=3}^n\binom nj\). For \(n=4\), rank-two and rank-four alternating symbols number respectively \((q-1)(q^2+1)(q^2+q+1)\) and \(q^2(q-1)(q^3-1)\). For zero quadratic symbol, elements are cubic plus quartic. Of these, one is zero, \(q-1\) nonzero pure quartics have multiplication rank one, and the other \(q(q^4-1)\) elements have rank two (the nonzero cubic component maps the unit to itself and some degree-one monomial to a nonzero top-degree multiple). Multiplying the two nonzero quadratic-symbol counts by \(q^5\) gives the stated polynomial. Its evaluation at \(T=1\) is \(q^{11}=|J^2|\).

## Verification
The standalone `verify.py` uses squarefree bitmask multiplication and independent finite-field Gaussian elimination. It exhausts all \(2^{11}=2048\) elements of \(J^2\) for \(n=4\), \(q=2\), obtaining rank multiplicities \((0:1,1:1,2:30,4:1120,6:896)\). It also enumerates all \(4^6=4096\) homogeneous quadratic symbols for \(n=4\), \(q=4\), obtaining alternating rank multiplicities \((0:1,2:1071,4:3024)\). Deterministic samples over both fields test lifts for \(n=3,4,5,6\), and explicit sharpness examples are checked up to \(n=9\). The verifier prints `VERIFY_OK`. Neither sampling nor finite enumeration is offered as an infinite proof; the cancellation and tensor decompositions above establish the universal theorem.

## Relationship to prior work
Margolis, Sakurai and Stanojkovski (arXiv:2110.10025, first public 2021-10-19) obtain structural invariants and reductions in modular group algebras; their principal conclusions concern group bases rather than the Jordan rank of individual multiplication operators, and their methodology motivates looking for finer augmentation invariants. García-Lucas (arXiv:2209.15128, first public 2022-09-29) continues this modular group-algebra program via abelian factors and relative augmentation ideals, without asserting the present perturbation threshold. Crispin Quiñonez, Lundqvist and Nenashev (arXiv:1803.08918, first public 2018-03-23) study Hilbert series for generic *pairs* of homogeneous quadratic exterior-algebra forms over the complex numbers and recall known principal-ideal formulas in characteristic zero. These do not determine characteristic-two multiplication-operator homology for arbitrary higher-degree perturbations. Classical alternating-form normal forms, elementary complex cancellation, and finite-field orbit counts are used as standard ingredients, not claimed as new. The contribution assessed here is their sharp synthesis into a theorem about higher-order lifts, with an explicit nonrigidity boundary and a complete four-generator rank census.

## Limitations
The result requires characteristic two and elementary abelian groups of exponent two. For quadratic-symbol nullity at least three it proves nonrigidity and constructs a precise rank jump, but does not classify all possible higher-lift ranks. The finite-field count covers the rigid strata in arbitrary dimension and the full rank census at four generators, not all higher-dimensional nonrigid strata. Previously undiscovered stronger results on exterior-algebra deformations could potentially imply parts of the theorem. No independent mathematical validation is claimed.

## References
1. L. Margolis, T. Sakurai, M. Stanojkovski, *Abelian invariants and a reduction theorem for the modular isomorphism problem*, arXiv:2110.10025, first public 2021-10-19, https://arxiv.org/abs/2110.10025.
2. D. García-Lucas, *The modular isomorphism problem and abelian direct factors*, arXiv:2209.15128, first public 2022-09-29, https://arxiv.org/abs/2209.15128.
3. V. Crispin Quiñonez, S. Lundqvist, G. Nenashev, *On ideals generated by two generic quadratic forms in the exterior algebra*, arXiv:1803.08918, first public 2018-03-23, https://arxiv.org/abs/1803.08918.
