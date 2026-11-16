# Exact Steinberg Fourier endpoint norms over finite unitary groups

## Finding
Let \(q\ge2\) be a prime power and \(n\ge1\). Write \(G=U_n(q)\) for the full isometry group of a nondegenerate Hermitian form on \(\mathbb F_{q^2}^n\), and \(\operatorname{St}_{n,q}\) for its irreducible complex Steinberg character, of degree \(D_{n,q}=q^{n(n-1)/2}\). Let \(P_{n,q}\) be the central Fourier projection on complex-valued functions on \(G\) onto the full Steinberg isotypic block of the regular representation. Its sharp endpoint norms coincide:
\[
\|P_{n,q}\|_{\ell^1\to\ell^1}=\|P_{n,q}\|_{\ell^\infty\to\ell^\infty}=D_{n,q}a_n(q).
\]
Here \(a_0(q)=1\) is a bookkeeping coefficient and, for all \(n\ge0\), the *exact* rational number \(a_n(q)\) is the coefficient of \(z^n\) in
\[
 H_q(z)=\prod_{d\ge1}\left(\sum_{m\ge0}\frac{z^{dm}}{\prod_{j=1}^m(q^{dj}-(-1)^{dj})}\right)^{N_d(q)},\qquad
 N_d(q)=\frac1d\sum_{e\mid d}\mu(d/e)(q^e-(-1)^e).
\]
Empty products equal one; the infinite product is interpreted as a formal series. In particular,
\[
 a_1(q)=1,\quad a_2(q)=\frac{q}{q+1},\quad
 a_3(q)=\frac{q(q-1)(q^2+q+1)}{(q+1)^2(q^2-q+1)}.
\]
The normalized sharp norm admits a positive, explicitly convergent infinite-product limit. For every fixed \(q\ge2\) and every real \(\rho\) with \(1<\rho<\sqrt q\),
\[
 a_n(q)=C_q+O_{q,\rho}(\rho^{-n}),
\]
where
\[
 C_q=\left(1+\frac1q\right)\prod_{d\ge1}\left[
 (1-q^{-d})\sum_{m\ge0}\frac1{\prod_{j=1}^m(q^{dj}-(-1)^{dj})}
 \right]^{N_d(q)}\in(0,\infty).
\]

## Assumptions and scope
The group is the **full finite unitary group**, not its special unitary subgroup; \(q\) is any prime power, including characteristic two. Frequencies refer to irreducible matrix coefficients in finite-group noncommutative Fourier analysis. The central Fourier idempotent is the convolution kernel \(K(g)=D_{n,q}\operatorname{St}_{n,q}(g^{-1})/|G|\); counting measure is used for \(\ell^1\), and its induced norm is unchanged by rescaling both source and target counting measures. The result concerns the full Steinberg isotypic block, not individual matrix coefficients or restriction operators.

## Proof
**1. Endpoint norm as a semisimple class sum.** For convolution on a finite group, the sharp \(\ell^1\)- and \(\ell^\infty\)-operator norms are both \(\sum_{g\in G}|K(g)|\), attained by a point mass and a phase-aligned test function respectively. The standard Steinberg character value theorem states that it vanishes outside semisimple elements and has \(|\operatorname{St}_{n,q}(g)|=|C_G(g)|_p\) at every semisimple element (\(p\) the defining characteristic). Each semisimple conjugacy class contributes \(|C_G(g)|_p/|C_G(g)|\) to \(a_n(q)=|G|^{-1}\sum_g|\operatorname{St}_{n,q}(g)|\).

**2. Classification of semisimple centralizers.** On nonzero eigenvalues over an algebraic closure, the unitary Frobenius acts by \(F(\lambda)=\lambda^{-q}\). Its exact period-\(d\) orbits number \(N_d(q)\) as displayed: \(F^e\) has exactly \(q^e-(-1)^e\) fixed nonzero eigenvalues, so Möbius inversion applies. A semisimple conjugacy class is specified by an arbitrary nonnegative multiplicity \(m\) for each such orbit, with total dimension \(n=\sum dm\). An orbit of odd length \(d\) yields a centralizer factor \(U_m(q^d)\); one of even length \(d\) yields \(\mathrm{GL}_m(q^d)\). The quotient of defining-characteristic parts by full orders of these factors is, in either case,
\[
 \frac{|C_d(m)|_p}{|C_d(m)|}=\left[\prod_{j=1}^{m}(q^{dj}-(-1)^{dj})\right]^{-1}.
\]
The formula uses the standard orders \(|U_m(Q)|=Q^{m(m-1)/2}\prod_{j=1}^m(Q^j-(-1)^j)\) for odd \(d\) and \(|\mathrm{GL}_m(Q)|=Q^{m(m-1)/2}\prod_{j=1}^m(Q^j-1)\) for even \(d\), with \(Q=q^d\). Summing products of these weights independently over eigenvalue orbits and multiplicities proves the coefficient formula. Expanding degrees up to three gives the three rational values displayed above.

**3. Convergent normalization and exponential rate.** Put \(B_d(t)=\sum_{m\ge0}t^m/\prod_{j=1}^m(q^{dj}-(-1)^{dj})\). The fixed-point identity \(\sum_{d\mid k}dN_d(q)=q^k-(-1)^k\) gives the formal identity
\[
 \prod_{d\ge1}(1-q^{-d}z^d)^{-N_d(q)}
 =\exp\left(\sum_{k\ge1}\frac{(q^k-(-1)^k)(z/q)^k}{k}\right)=\frac{1+z/q}{1-z}.
\]
Consequently \(H_q(z)=(1+z/q)R_q(z)/(1-z)\), where
\[
 R_q(z)=\prod_{d\ge1}\left[(1-q^{-d}z^d)B_d(z^d)\right]^{N_d(q)}.
\]
For \(|z|\le\rho<\sqrt q\), the basic estimates \(N_d(q)\le q^d+1\), \(b_{d,1}=q^{-d}+O(q^{-2d})\), and \(0<b_{d,m}\le c\,q^{-dm(m+1)/2}\) uniformly in \(d,m\) imply \((1-q^{-d}z^d)B_d(z^d)-1=O_\rho(\rho^d q^{-2d}+\rho^{2d}q^{-2d})\) for large \(d\). The sum of the corresponding \(N_d(q)\)-weighted bounds converges since \(\rho<\sqrt q\); the remaining finitely many factors are analytic. Thus \(R_q\) is analytic in \(|z|<\sqrt q\). Each factor is strictly positive at \(z=1\), and the same estimates show \(R_q(1)\in(0,\infty)\). Subtracting the pole \(C_q/(1-z)\) from \(H_q\) leaves a function analytic in \(|z|<\sqrt q\). Cauchy's coefficient bound gives \(a_n(q)-C_q=O_{q,\rho}(\rho^{-n})\). No monotonicity is claimed.

## Verification
The complete standard-library program `CHECK.py` computes the rational coefficients by direct formal-series multiplication for \(q=2,3,4,5\), verifying the closed values through degree three. It independently enumerates all \(648\) elements of \(U_3(2)\) as Hermitian-orthonormal ordered bases over \(\mathbb F_4\), uses the action on its nine isotropic projective lines to calculate the Steinberg character (the reduced rank-one building character), and obtains the distribution \(\{-1:168,0:405,2:72,8:3\}\). Hence the directly enumerated norm is \(112/27\), matching \(8a_3(2)\). The program reports `UNITARY_STEINBERG_EXACT_CHECKS_PASS`. These finite cases check the normalization and centralizer weighting but do not establish the infinite-rank claim: that follows from the character theorem, orbit decomposition, and analytic estimates above.

## Relationship to prior work
The Steinberg character value theorem and classification of semisimple centralizers are classical and are used as inputs, not claimed as new. Hiss and Zalesski (2008) study *products* of Weil and Steinberg characters and restrictions, not this central idempotent endpoint norm. Møller (first preprint 2017, subsequently published) determines equivariant Euler characteristics of unitary buildings and sets out the same semisimple-class centralizers; his signed equivariant Euler-characteristic generating functions have different class weights from the absolute Steinberg averages here. A published determination of Steinberg Fourier endpoint norms for **general linear** groups concerns a different Frobenius family, and its equal-even-odd normalized law does not hold for the unitary values already at rank three: \(a_2(2)=2/3\) while \(a_3(2)=14/27\). The present proof evaluates the unitary absolute-character sum explicitly and gives a positive limiting Euler product with exponential convergence. This comparison does not assert exhaustive historical priority.

## Limitations
The theorem depends on standard external Steinberg-character and finite-unitary-centralizer results; these are not reproved. It does not supply sharp bounds uniform in the field size \(q\), nor norms for special unitary subgroups or other character blocks. The exact rational sequence is given by a coefficient product rather than a single elementary closed expression at arbitrary rank. A previous unindexed equivalent unitary specialization or a deduction from an uninspected general theorem remains a priority risk. Independent external mathematical validation has not been performed.

## References
- G. Hiss and A. Zalesski, *The Weil–Steinberg character of finite classical groups*, arXiv:0806.2567, first public version 2008-06-16, https://arxiv.org/abs/0806.2567.
- J. M. Møller, *Equivariant Euler characteristics of unitary buildings*, arXiv:1707.00850, first public version 2017-07-04, https://arxiv.org/abs/1707.00850.
- R. W. Carter, *Centralizers of semisimple elements in the finite classical groups*, Proc. London Math. Soc. 42 (1981), 1–41.
- *Exact Steinberg Fourier endpoint norms over finite general linear groups*, published mathematical research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-steinberg-fourier-endpoint-norms-over-finite-general-linea--a54c7ffd4a79.
