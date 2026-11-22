# Characteristic-two involutions of multivariable cubic jet automorphism groups

## Finding
Let \(q=2^e\) for an integer \(e\ge1\), and let \(d\ge1\). For the local commutative algebra
\[
A_d=\mathbb F_q[x_1,\ldots,x_d]/(x_1,\ldots,x_d)^3,
\]
write \(G_d=\operatorname{Aut}_{\mathbb F_q}(A_d)\), \(D=\binom{d+1}{2}\), and \(\mathfrak m=(x_1,\ldots,x_d)\). For every \(g\in G_d\), let \(\overline g\) be its induced linear automorphism of \(\mathfrak m/\mathfrak m^2\). Define \(\mathcal I_{d,q}=\{g\in G_d:g^2=1\}\), so the identity is included.

**Theorem.** The complete distribution of \(\mathcal I_{d,q}\) by \(r=\operatorname{rank}(\overline g-I)\) is
\[
\boxed{\displaystyle
\#\{g\in\mathcal I_{d,q}:\operatorname{rank}(\overline g-I)=r\}
={d\brack r}_q{d-r\brack r}_q|\operatorname{GL}_r(q)|
q^{\,(d-r)D-(d-2r)r(d-r)}
}\tag{1}
\]
for each integer \(0\le r\le\lfloor d/2\rfloor\), and is zero otherwise. Here \({n\brack k}_q=\prod_{i=0}^{k-1}(q^{n-i}-1)/(q^{k-i}-1)\), and \(|\operatorname{GL}_0(q)|=1\). Summing (1) gives the exact number of automorphisms of order dividing two; subtract one to count automorphisms of order exactly two.

A characteristic-two concentration phenomenon follows: for fixed \(q\), as \(d\to\infty\),
\[
\boxed{\displaystyle
\Pr_{g\text{ uniform in }\mathcal I_{d,q}}(\overline g=I)
=1-O_q\!\left(q^{-d(d-3)/2}\right).}\tag{2}
\]
In fact the identity-linear involutions form an elementary abelian group of order \(q^{dD}\). Thus almost every involution has **trivial cotangent action but usually a nontrivial quadratic action**.

For example, the exact totals are \(88\) for \((d,q)=(2,2)\), \(5056\) for \((2,4)\), and \(283648\) for \((3,2)\).

## Assumptions and scope
Automorphisms are unital, \(\mathbb F_q\)-linear and fix the coefficient field pointwise. The algebra uses the ordinary symmetric polynomial quotient by all monomials of total degree at least three; it is **not** the tensor (noncommutative) cube-zero algebra or the divided-power algebra. The group law is substitution and truncation. Characteristic two is essential. No statement is made about automorphisms over arbitrary base rings, higher jet order, or full conjugacy-class classification.

## Proof
**1. Normal form and the involution equation.** Put \(V=\mathfrak m/\mathfrak m^2\) and \(W=\operatorname{Sym}^2(V)\), of dimensions \(d\) and \(D\). The standard monomial basis identifies \(A_d\cong\mathbb F_q1\oplus V\oplus W\), with \(VW=W^2=0\) and multiplication on \(V\) given by the symmetric product. Every algebra endomorphism has a unique normal form
\[
 g(v)=L(v)+Q(v),\qquad L\in\operatorname{End}(V),\quad Q\in\operatorname{Hom}(V,W),
\]
and it is an automorphism exactly when \(L\in\operatorname{GL}(V)\): its matrix in the three-step decomposition is block triangular with diagonal blocks \(1,L,\operatorname{Sym}^2L\), while the inverse of an invertible such map is obtained by solving the degree-one and degree-two equations. Its action on \(W\) is exactly \(\operatorname{Sym}^2L\). Accordingly,
\[
 g^2=1\quad\Longleftrightarrow\quad L^2=I\ \text{and}\ QL+(\operatorname{Sym}^2L)Q=0.\tag{3}
\]
For \(q\) even the second equation is \(QL=(\operatorname{Sym}^2L)Q\), so \(Q\) is an intertwiner of the \(C_2\)-modules \(V\) and \(W\) under \(L\) and \(\operatorname{Sym}^2L\).

**2. Linear involutions.** In characteristic two, \(L^2=I\) is equivalent to \((L-I)^2=0\). Let \(r=\operatorname{rank}(L-I)\), and write \(s=d-2r\). Then \(r\) lies in the stated interval and \(L\) is conjugate to a direct sum of \(r\) two-dimensional unipotent Jordan blocks and \(s\) one-dimensional identity blocks. Conversely every such normal form squares to the identity. To count the matrices \(L\), choose the \(r\)-dimensional image \(U\) of \(L-I\), then choose a codimension-\(r\) kernel \(K\) containing \(U\), and finally choose an isomorphism \(V/K\to U\). These three independent choices give
\[
\#\{L:L^2=I,\ \operatorname{rank}(L-I)=r\}
={d\brack r}_q{d-r\brack r}_q|\operatorname{GL}_r(q)|.\tag{4}
\]

**3. Symmetric squares of modular two-blocks.** Over \(\mathbb F_q[C_2]\), let \(P\) denote the indecomposable two-dimensional regular module (a unipotent Jordan block), and let \(T\) denote the trivial one-dimensional module. Then \(V\cong P^r\oplus T^s\). In characteristic two, direct basis calculations show
\[
\operatorname{Sym}^2P\cong P\oplus T,
\qquad P\otimes P\cong P^2,
\qquad P\otimes T\cong P,
\]
while \(\operatorname{Sym}^2(T^s)\cong T^{\binom{s+1}{2}}\). Explicitly, if \(P\) has basis \(a,b\), with \(L(a)=a\) and \(L(b)=b+a\), then \(L-I\) maps \(ab\) and \(b^2\) to \(a^2\) and kills \(a^2\), so \(\operatorname{Sym}^2P\) has one two-block. On \(P\otimes P\), the map \(L-I\) has rank two, so it consists of two two-blocks. Taking symmetric squares of the direct sum now shows that the total number of \(P\) summands in \(W\) is
\[
 R=r+2\binom r2+rs=r(d-r).\tag{5}
\]
Because \(\dim W=D\), the remaining number of \(T\) summands is \(D-2R\).

**4. Count the quadratic lifts.** A \(C_2\)-linear map from \(P\cong\mathbb F_q[C_2]\) to \(W\) is uniquely determined by the image of a regular generator and therefore has \(D\) free coefficients. A \(C_2\)-linear map from \(T\) to \(W\) has image in the fixed subspace \(W^{C_2}\), whose dimension is \(R+(D-2R)=D-R\). Hence for each fixed linear involution \(L\), the solution space of (3) has dimension
\[
\dim\operatorname{Hom}_{\mathbb F_q[C_2]}(V,W)
=rD+s(D-R)=(d-r)D-(d-2r)r(d-r).\tag{6}
\]
There are exactly \(q\) to this exponent many quadratic lifts. Multiplication by the count (4) proves (1), with no assumption that a finite computational sample is exhaustive for unrestricted \(d\).

**5. Large-generator concentration.** The \(r=0\) term in (1) is \(q^{dD}\), and these are precisely the substitutions \(g(v)=v+Q(v)\). They form an elementary abelian group, since composition adds the quadratic parts. Define \(c_q=\prod_{j\ge1}(1-q^{-j})>0\). For \(0\le r\le d/2\), the Gaussian coefficient estimates and \(|\operatorname{GL}_r(q)|\le q^{r^2}\) give
\[
{d\brack r}_q{d-r\brack r}_q|\operatorname{GL}_r(q)|
\le c_q^{-2}q^{2r(d-r)}.
\]
The exponent in (6) is \(dD-rD-(d-2r)r(d-r)\), so for \(d\ge4\), the proportion of nonidentity-linear terms relative to the \(r=0\) count is bounded by
\[
\begin{aligned}
\frac{|\mathcal I_{d,q}|-q^{dD}}{q^{dD}}
&\le c_q^{-2}\sum_{r=1}^{\lfloor d/2\rfloor}
q^{2r(d-r)-rD-(d-2r)r(d-r)}\\
&\le c_q^{-2}\frac{q^{-d(d-3)/2}}{1-q^{-d(d-3)/2}}.
\end{aligned}
\]
This yields (2). The probability of the **identity automorphism itself** tends to zero since it is one element among at least \(q^{dD}\); thus the concentration is genuinely nonlinear, not concentration on the identity element.

## Verification
The accompanying pure-Python `checker.py` constructs multiplication and symmetric-square actions over \(\mathbb F_2\) and \(\mathbb F_4\). It exhausts every invertible linear part in dimensions one and two over both fields and dimension three over \(\mathbb F_2\), independently computes the nullity of (3), and compares the exact stratum counts. An additional **independent polynomial-composition implementation**, which does not use (3), checks all \(384\) two-generator cubic-jet automorphisms over \(\mathbb F_2\) and finds precisely \(88\) square-one maps. Reproducibly generated conjugates cover every admissible Jordan type in dimensions four, five and six. Run `python3 checker.py` from its extracted directory; the recorded successful output is in `CHECKS.txt`. These finite tests are consistency checks, not proofs of statements for arbitrary dimensions or fields.

## Relationship to prior work
Bardakov–Neshchadim–Sosnovsky (first posted 2010-07-16, arXiv:1007.2711) examine polynomial automorphism groups in characteristic zero and explicitly discuss the problem of elements of finite order, but do not count characteristic-two cubic-jet involutions. Fleischmann–Woodcock (2015, arXiv:1507.00227) analyze modular actions on commutative algebras in the trace-surjective setting; these are not the complete finite local-jet actions considered here. Bardakov–Neshchadim (2015, arXiv:1501.02626) concern nonlinearizability over the complex numbers, not modular finite-field counts.

The published result *A modular conjugacy obstruction and exact census of anti-involutions on free cube-zero algebras* counts **anti-automorphisms of a noncommutative tensor algebra**. Its flip-twisted tensor action and domain are not the commutative \(\operatorname{Sym}^2V\) module in (3), and its numerical formulas do not count the present objects. The published *Parity-switching involution classes in finite two-variable jet automorphism groups* applies to **odd** finite fields, whereas (1) treats all dimensions in characteristic two. *Idempotent derivations of cubic-truncated symmetric algebras* concerns \(D^2=D\) for derivations rather than square-one algebra automorphisms. The novelty assessed here is the precise all-dimension characteristic-two rank-stratified count and its asymptotic cotangent concentration, not the standard classification of linear unipotent involutions or the normal-form substitution formalism.

## Limitations
The theorem concerns the second-order, commutative local jet algebra over a finite field of characteristic two, not arbitrary singularities or higher truncations. It counts elements of order dividing two, not their full conjugacy classes, invariant subrings, or quotient-scheme geometry. Full historical priority is not certified: differently indexed results on modular jet groups or symmetric-square intertwiners could cover parts of the statement. No independent mathematical audit has been performed.

## References
1. V. G. Bardakov, M. V. Neshchadim, Y. V. Sosnovsky, *Groups of triangular automorphisms of a free associative algebra and a polynomial algebra*, arXiv:1007.2711, initial public preprint 2010-07-16, https://arxiv.org/abs/1007.2711 .
2. P. Fleischmann, C. Woodcock, *Modular group actions on algebras and p-local Galois extensions for finite groups*, arXiv:1507.00227, first posted 2015-07-01, https://arxiv.org/abs/1507.00227 .
3. V. G. Bardakov, M. V. Neshchadim, *Example of non-linearizable quasi-cyclic subgroup of automorphism group of polynomial algebra*, arXiv:1501.02626, first posted 2015-01-12, https://arxiv.org/abs/1501.02626 .
4. *A modular conjugacy obstruction and exact census of anti-involutions on free cube-zero algebras*, publicly available `RESULT.md`, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-a-modular-conjugacy-obstruction-and-exact-census-of-anti-involut--e842947e3cb4 .
5. *Parity-switching involution classes in finite two-variable jet automorphism groups*, publicly available `RESULT.md`, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-parity-switching-involution-classes-in-finite-two-variable-jet-a--391410cf76e4 .
6. *Idempotent derivations of cubic-truncated symmetric algebras over arbitrary fields*, publicly available `RESULT.md`, https://github.com/published-finding corpus/2026/tree/main/2026/10/12/SCOPE-idempotent-derivations-of-cubic-truncated-symmetric-algebras-ove--25d3e577a3dc .
