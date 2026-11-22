# Arithmetic rigidity and finite survival of generalized Aluthge \(m\)-isometric shifts

## Finding
Let \(P\in\mathbb R[x]\) satisfy \(P(0)=1\) and \(P(n)>0\) for every integer \(n\ge0\). On \(\ell^2(\mathbb N_0)\), define the positive unilateral weighted shift
\[
W_Pe_n=\sqrt{\frac{P(n+1)}{P(n)}}\,e_{n+1}.
\]
Fix \(0<\lambda<1\), let \(\Delta_\lambda(T)=|T|^\lambda U|T|^{1-\lambda}\) for the polar decomposition \(T=U|T|\), and write \(W^{(k)}=\Delta_\lambda^{\circ k}(W_P)\), \(k\ge1\). If \(P\) is nonconstant, the following conditions are equivalent:

1. \(W^{(k)}\) is an \(m\)-isometry for some finite integer \(m\ge1\).
2. \(\lambda=u/v\) is rational in lowest terms with \(0<u<v\), and there is a real polynomial \(Q\) satisfying \(Q(0)=1\), \(Q(n)>0\) for every integer \(n\ge0\), and
\[
P(x)=Q(x)^{v^k}.
\]

Whenever these conditions hold, \(W^{(k)}\) is a **strict** \((\deg P+1)\)-isometry and its normalized moment polynomial is exactly
\[
R_k(x)=\frac{\displaystyle\prod_{j=0}^k Q(x+j)^{b_{k,j}}}
{\displaystyle\prod_{j=0}^k Q(j)^{b_{k,j}}},\qquad
b_{k,j}=\binom kj(v-u)^{k-j}u^j.
\]
If \(P\equiv1\), every iterate is the unilateral isometry. Thus an irrational parameter destroys every nontrivial polynomial-moment isometry at the first iterate and at **every** later iterate. For rational \(u/v\), a nonconstant \(P\) can survive at most \(\lfloor\log_v(\deg P)\rfloor\) iterations. In particular, a strict \(m\)-isometric shift can survive \(k\) iterations only if \(v^k\mid(m-1)\), and for every such divisibility there are positive-weight examples realizing survival.

## Assumptions and scope
All polynomials and weights are real, with \(P(0)=1\) and positivity assumed only at **nonnegative integers**, not between them. The generalized Aluthge parameter lies strictly between zero and one. The assertion covers every nonnegative integer \(k\) for the moment identity and every positive integer \(k\) for the classification. All statements refer to scalar, injective unilateral weighted shifts on complex \(\ell^2(\mathbb N_0)\); no general-operator extension is asserted. We call an operator a strict \(m\)-isometry when it satisfies the \(m\)-isometry identity but not the \((m-1)\)-identity.

## Proof
**1. Moment formula.** The positive weights tend to one because \(P(n+1)/P(n)\to1\), so \(W_P\) is bounded and injective. For a positive unilateral shift with weights \(w_n\), the generalized Aluthge weights are \(w_n^{1-\lambda}w_{n+1}^{\lambda}\). Iterating this log-linear averaging and telescoping the products gives
\[
\beta_k(n):=\|(W^{(k)})^ne_0\|^2
=\prod_{j=0}^k\left(\frac{P(n+j)}{P(j)}\right)^{c_{k,j}},
\quad c_{k,j}=\binom kj(1-\lambda)^{k-j}\lambda^j.
\tag{1}
\]
A strictly positive unilateral shift is an \(m\)-isometry precisely when its normalized moments agree with a polynomial in \(n\) of degree at most \(m-1\): the \(m\)-th forward difference vanishes at each basis vector, equivalently at \(e_0\) and at every shifted starting point, using \(\beta_k(n+r)/\beta_k(r)\). If the sequence in (1) is a polynomial \(R(n)\), then \(\deg R=\deg P=:d\), since \(\beta_k(n)\sim Cn^d\) and \(\sum_jc_{k,j}=1\).

**2. Equality of analytic germs.** For sufficiently large positive real \(x\), define \(F(x)\) by replacing \(n\) with \(x\) on the right of (1), with positive real powers. Factoring the leading term of \(P(x+j)\) shows that \(z^dF(1/z)\) is holomorphic in a disk about \(z=0\). The same holds for \(z^dR(1/z)\). Agreement at every sufficiently large integer yields equality of the two analytic germs by the identity theorem. Consequently,
\[
\frac{R'(x)}{R(x)}
=\sum_{j=0}^kc_{k,j}\frac{P'(x+j)}{P(x+j)}
\tag{2}
\]
as an identity of rational functions, not merely a relation at sampled integers.

**3. Arithmetic of root multiplicities.** Partition the complex roots of \(P\) into finite sets of integer-translation orbits. Fix an orbit with representative \(\alpha\) and let \(a_h\ge0\) be the multiplicity of the root \(\alpha+h\) in \(P\), where \(h\in\mathbb Z\) and only finitely many \(a_h\) are nonzero. By (2), the multiplicity \(r_h\) in \(R\) is
\[
r_h=\sum_{j=0}^kc_{k,j}a_{h+j}\in\mathbb Z_{\ge0}.
\tag{3}
\]
Write \(M=\sum_ha_h>0\). Since \(\sum_jjc_{k,j}=k\lambda\), (3) implies
\[
\sum_hh(a_h-r_h)=k\lambda M\in\mathbb Z.
\]
Thus \(\lambda\) is rational. Write it in lowest terms as \(u/v\). Multiplying (3) by \(v^k\), the coefficient of \(a_h\) is \((v-u)^k\), coprime to \(v^k\). Starting at the **largest** \(h\) for which \(a_h\ne0\) and inducting downward, integrality of all \(r_h\) forces \(v^k\mid a_h\) for every \(h\). This holds in every root orbit. Reality and normalization then give a unique real polynomial \(Q\) with \(Q(0)=1\) and \(P=Q^{v^k}\).

**4. Integer-sign obstruction.** If \(v\) is odd, then \(Q(n)^{v^k}=P(n)>0\) forces \(Q(n)>0\) for each integer \(n\ge0\). If \(v\) is even, the integers \(u\), \(v-u\), and hence \(b_{k,0}=(v-u)^k\), are odd, while \(\sum_jb_{k,j}=v^k\) is even. The polynomial in (1), determined by its positive asymptotic branch, must have the sign of \(\prod_jQ(n+j)^{b_{k,j}}\), which is positive for all sufficiently large integers. Suppose \(Q(n)\) changes sign on the nonnegative integers. Let \(N\) be the last integer whose sign differs from the eventual sign. At \(n=N\), the product has the opposite sign from its eventual positive sign because \(b_{k,0}\) is odd and all later factors have eventual sign. This contradicts \(\beta_k(N)>0\). Hence the sign of \(Q(n)\) is constant; \(Q(0)=1\) makes it positive everywhere on the integer domain.

**5. Converse and order.** If \(P=Q^{v^k}\) with \(Q(n)>0\) as stated, each exponent \(v^kc_{k,j}=b_{k,j}\) in (1) is an integer. The resulting moment is exactly \(R_k\), a positive polynomial of degree \(\deg P\). The forward-difference criterion proves strict \((\deg P+1)\)-isometry. Since a nonconstant \(P\) with \(P=Q^{v^k}\) has degree at least \(v^k\), the stated finite-iteration bound follows. If \(v^k\mid(m-1)\), take \(P(x)=(x+1)^{m-1}\) for sharp existence.

## Verification
The standalone file `check_examples.py` uses exact symbolic arithmetic and reproduces examples at parameters \(1/2\), \(1/3\), \(2/3\), and \(2/5\), through three iterates. It verifies the moment polynomials, finite-difference identities, an integer-sign counterexample, and modular multiplicity illustrations; its recorded result is `EXACT_CHECKS_OK 191`. These checks are supplementary: the universal classification depends on the root-multiplicity and analytic-germ arguments above.

For instance, with \(P(x)=(x+1)^2\) and \(\lambda=1/2\), both \(W_P\) and its first transform are strict \(3\)-isometries, with transformed moment \((n+1)(n+2)/2\), but the second transform is no finite-order \(m\)-isometry. With \(P(x)=(x+1)^4\), the second-transform moment is \((n+1)(n+2)^2(n+3)/12\). The positivity condition on \(Q\) cannot be dropped: \(P(x)=(2x-1)^2\) has positive integer moments and is a perfect square, but at \(\lambda=1/2\) its first-transform moments agree with \(4n^2-1\) for every \(n\ge1\) while their value at \(n=0\) is \(1\), not \(-1\).

## Relationship to prior work
Chabbabi and Ostermann (2022) established Aluthge and mean-transform counterexamples for \(m\)-isometries and proved that a weighted shift which is itself a \(2\)-isometry cannot have a \(2\)-isometric ordinary Aluthge transform unless it is an isometry. Their final question asks about higher orders and generalized transforms. The classification above settles the scalar positive weighted-shift case for **all** finite orders, all interior generalized parameters, and arbitrarily many iterates; it also supplies nontrivial simultaneous \(3\)-isometric examples. The polynomial-moment characterization of weighted-shift \(m\)-isometries was established earlier by Abdullah and Le and is an explicit input, not claimed as new. Buchała (2024) generalizes such characterizations to operator-weighted shifts; the theorem here concerns arithmetic conditions under scalar Aluthge iteration, not that broader representation problem.

## Limitations
The theorem does not classify arbitrary operator-weighted or non-shift \(m\)-isometries, the mean transform, or Aluthge endpoints \(\lambda=0,1\). Its integer-sign condition is necessary: even perfect-power moment polynomials may fail after an interior transform. Distinct-source historical equivalents not indexed by the searches remain possible. No independent mathematical audit is asserted.

## References
1. F. Chabbabi and M. Ostermann, *The Aluthge and the mean transforms of \(m\)-isometries*, arXiv:2203.15658v1 (first posted 29 March 2022), https://arxiv.org/abs/2203.15658.
2. B. Abdullah and T. Le, *The structure of \(m\)-isometric weighted shift operators*, author-hosted full text, https://www.math.utoledo.edu/~tle20/Data/Structure2016.pdf.
3. M. Buchała, *\(m\)-isometric weighted shifts with operator weights*, arXiv:2407.17233v1 (first posted 24 July 2024), https://arxiv.org/abs/2407.17233.
4. G. R. Exner, *Aluthge transforms and \(n\)-contractivity of weighted shifts*, *Journal of Operator Theory* 61 (2009), https://jot.theta.ro/jot/archive/2009-061-002/2009-061-002-012.pdf.
