# Integral Smith classification of primitive-position Ramanujan Gram matrices

## Finding

For an integer \(n\ge2\), put \(U_n=(\mathbb Z/n\mathbb Z)^\times\) and let
\[
c_n(t)=\sum_{d\mid\gcd(n,t)}d\,\mu(n/d),\qquad
G_n=\bigl(c_n(a-b)\bigr)_{a,b\in U_n}.
\]
The matrix \(G_n\) is the integral Gram matrix obtained by restricting the primitive-frequency Fourier frame to **primitive positions** as well. Write \(n=\prod_{p^e\parallel n}p^e\), and define
\[
R_n=\prod_{p^e\parallel n}
\begin{cases}
p-1,&e=1,\\
p^{e-2}(p-1)^2,&e\ge2.
\end{cases}
\]
For \(1\le j\le R_n\), set
\[
\boxed{d_j(n)=\prod_{p^e\parallel n}p^{\,e-1+\mathbf1_{\{j>R_n/(p-1)\}}}.}
\]
Then the complete **integral** Smith form is
\[
\boxed{\operatorname{SNF}_{\mathbb Z}G_n
=\operatorname{diag}\bigl(d_1(n),\ldots,d_{R_n}(n),
\underbrace{0,\ldots,0}_{\varphi(n)-R_n}\bigr).}
\]
In particular, \(d_j(n)\mid d_{j+1}(n)\), and
\[
\operatorname{coker}_{\mathbb Z}G_n\cong
\mathbb Z^{\varphi(n)-R_n}\oplus
\bigoplus_{j=1}^{R_n}\mathbb Z/d_j(n)\mathbb Z.
\]
The matrix \(G_n\) is nonsingular over \(\mathbb Q\) **exactly when \(n\) is squarefree**. In that case
\[
\det G_n=\prod_{p\mid n}p^{\varphi(n)(p-2)/(p-1)}>0.
\]
For arbitrary \(n\ge2\), the torsion order is
\[
\prod_{j=1}^{R_n}d_j(n)=
\frac{n^{R_n}}{\prod_{p\mid n}p^{R_n/(p-1)}},
\]
and its exponent is \(n/\gcd(n,2)\). At \(n=1\), the one-by-one matrix is \((1)\), with Smith factor \(1\).

## Assumptions and scope

The indexing set \(U_n\) consists of the residue classes relatively prime to \(n\); it is **not** the set of all residues, nor the set of divisors. The prime-power notation \(p^e\parallel n\) means an exact prime-power divisor. Here \(\mu\) is the Möbius function, \(\varphi\) Euler's totient and \(\mathbf1_{\{Q\}}\) the indicator of statement \(Q\). Smith equivalence uses unimodular matrices with integer entries; a complex Fourier diagonalization alone cannot establish it. The displayed zero factors denote free cokernel rank, not zero torsion. All prime products are over the distinct prime divisors of \(n\).

The description is relevant to primitive-position Fourier sampling because the vectors
\[
v_a=(\exp(2\pi i au/n))_{u\in U_n}
\]
have Hermitian Gram entries \(\langle v_a,v_b\rangle=c_n(a-b)\) up to the harmless convention for the inner-product order.

## Proof

**1. Local arithmetic structure.** The standard prime-power Ramanujan identity is
\[
c_{p^e}(t)=p^{e-1}\bigl(p\mathbf1_{\{p^e\mid t\}}-\mathbf1_{\{p^{e-1}\mid t\}}\bigr).
\]
For \(e=1\), every nonzero residue is a unit and every difference of distinct units is nonzero modulo \(p\). Thus the unit-indexed block is
\[
G_p=pI_{p-1}-J_{p-1},
\]
where \(J_q\) denotes the all-ones matrix of size \(q\). Its eigenvalues are \(1\) once and \(p\) with multiplicity \(p-2\); for an **integral** proof, subtract a fixed row from the others and use elementary row/column operations, or use the determinantal divisors of \(pI_{p-1}-J_{p-1}\): they are \(1,p,p^2,\ldots,p^{p-2}\). Consequently its Smith factors are one \(1\) and \(p-2\) copies of \(p\). This includes \(p=2\), giving the single factor \(1\).

For \(e\ge2\), the units modulo \(p^e\) split into exactly
\[
h=p^{e-2}(p-1)
\]
classes by their residue modulo \(p^{e-1}\), each with exactly \(p\) lifts. A difference from different classes is not divisible by \(p^{e-1}\), hence the corresponding Ramanujan entry is zero. Within each class the matrix is exactly
\[
p^{e-1}(pI_p-J_p).
\]
The matrix \(pI_p-J_p\) is the integral Laplacian of the complete graph, with Smith factors \(1\), then \(p\) repeated \(p-2\) times, then \(0\). For completeness, replace its final column by the sum of all columns to make that column zero. Subtract the final row from all previous rows. The remaining nonzero block consists of \(pI_{p-1}\) above the row \((-1,\ldots,-1)\). Every \(k\)-minor, for \(1\le k\le p-1\), is divisible by \(p^{k-1}\); selecting the final row, \(k-1\) distinct coordinate rows and appropriate columns gives a minor of absolute value \(p^{k-1}\). This proves the asserted local Smith form by determinantal divisors.

Therefore for \(e\ge2\), there are \(h\) local factors \(p^{e-1}\), \(h(p-2)\) local factors \(p^e\), and \(h\) zero factors. The local rational rank is \(h(p-1)=p^{e-2}(p-1)^2\). In the case \(e=1\), the rank is \(p-1\); in either case exactly a fraction \(1/(p-1)\) of the nonzero factors has \(p\)-valuation \(e-1\), and the others have valuation \(e\).

**2. CRT and integer diagonalization.** For coprime positive integers \(u,v\), the Chinese remainder theorem identifies \(U_{uv}\) with \(U_u\times U_v\), and ordinary Ramanujan sums satisfy \(c_{uv}(t)=c_u(t)c_v(t)\). It follows that a simultaneous permutation of rows and columns gives
\[
G_{uv}\simeq G_u\otimes G_v.
\]
Tensoring the integral unimodular transformations that produce the local Smith diagonals yields an **integral diagonalization** of \(G_n\). Its number of nonzero entries is the product of the local nonzero counts, precisely \(R_n\); its remaining \(\varphi(n)-R_n\) entries are zero.

**3. Recover canonical invariant factors.** Fix \(p^e\parallel n\). Among the \(R_n\) nonzero entries of this tensor diagonal, exactly \(R_n/(p-1)\) have \(p\)-adic valuation \(e-1\), and all others have valuation \(e\). The integer \(R_n/(p-1)\) exists since the local rank is divisible by \(p-1\). For a diagonal integral matrix, the ordered valuations of its positive Smith factors are obtained by separately sorting the nonzero diagonal valuations at each prime, then combining the sorted lists pointwise. This follows from gcds of minors or localization at each prime. Applying this step to every prime dividing \(n\) gives exactly the displayed formula for \(d_j(n)\), and verifies \(d_j(n)\mid d_{j+1}(n)\).

**4. Consequences.** The rational rank is \(R_n\), so \(G_n\) is nonsingular precisely when every local rank equals the number of units, i.e. when all prime powers dividing \(n\) have exponent one. If \(n\) is squarefree, its determinant is positive (the Gram matrix is positive definite) and equals the product of its Smith factors; summing the exponents gives the displayed determinant. For arbitrary \(n\), summing prime exponents gives the torsion-order formula. Finally the largest invariant factor has exponent \(e\) at every odd prime and \(e-1\) at the prime two, so it equals \(n/\gcd(n,2)\). The cokernel formula is the integral Smith classification theorem.

## Verification

The accompanying `verify_primitive_ramanujan_smith.py` constructs \(G_n\) **directly from the divisor-sum definition** of Ramanujan sums, computes its exact integer Smith normal form using SymPy, and compares the entire factor list with the stated expression. The 39 tested moduli include every integer from \(1\) through \(30\) and \(32,36,40,45,48,49,50,60,72\); checks cover squarefree, prime powers, repeated small primes and mixed factors. The executed check produced `CHECK_OK 39 independent Smith forms`. To reproduce, install `sympy`, then run `python3 verify_primitive_ramanujan_smith.py`. The test is finite corroboration; the proof above establishes the unlimited claim.

## Relationship to prior work

Fowler, Garcia and Karaali (first arXiv posting January 5, 2012) give the prime-power Ramanujan evaluation, multiplicativity and Kronecker-product constructions for **divisor-indexed supercharacter tables**. Those identities are used here, not claimed as new. Schlage-Puchta (2021) studies a **divisor-indexed determinant**. The published complete Smith classification of the **full residue-indexed** difference circulant \((c_n(a-b))_{a,b\in\mathbb Z/n\mathbb Z}\) gives rank \(\varphi(n)\) for every modulus; it does not determine the Smith invariants of its primitive-position principal submatrix. In particular, the latter has smaller rank at every nonsquarefree modulus, while remaining nonsingular for squarefree moduli. Other published divisor-indexed Ramanujan Smith and Gram classifications have different indexing sets, matrix sizes, and local blocks. The distinction is the restriction to units simultaneously on both axes, not just replacing a parameter in a known formula.

## Limitations

This classification is specific to primitive-position restrictions of the standard Ramanujan convolution Gram matrix; it does not treat arbitrary subsets of residues, arbitrary Fourier masks, or generalized Ramanujan sums over other finite rings. The classical local Ramanujan identities and integer Smith normal form of complete-graph Laplacians are established inputs. A broader general theorem that implies this unit-indexed specialization may exist in unindexed literature; absence from the checked sources cannot prove worldwide priority. The statement does not infer uniqueness of its integral classification from a complex spectral computation.

## References

1. C. F. Fowler, S. R. Garcia and G. Karaali, *Ramanujan sums as supercharacters*, initial arXiv version posted 2012-01-05, arXiv:1201.1060. https://arxiv.org/abs/1201.1060
2. J.-C. Schlage-Puchta, *A determinant involving Ramanujan sums and So's conjecture*, Archiv der Mathematik 117 (2021), 379–384, DOI:10.1007/s00013-021-01643-8. https://doi.org/10.1007/s00013-021-01643-8
3. *Complete Smith form of Ramanujan-sum convolution circulants*, published result (2026). https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-complete-smith-form-of-ramanujan-sum-convolution-circulants--0bffd4ff77aa
4. *Smith normal form of the reduced divisor-indexed Ramanujan matrix for every modulus*, published result (2026). https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-smith-normal-form-of-the-reduced-divisor-indexed-ramanujan-matri--3189e6142132
5. *Smith invariant factors of the divisor-indexed Ramanujan Gram matrix*, published result (2026). https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-smith-invariant-factors-of-the-divisor-indexed-ramanujan-gram-ma--1831f22124b8
