# Sharp coordinate-dominance concentration for holomorphic spherical polynomials

## Finding

For integers \(d\ge k\ge2\) and \(m\ge1\), let \(\mathcal H_{d,m}\) be the degree-exactly-\(m\) homogeneous holomorphic polynomials on \(S^{2d-1}\subset\mathbb C^d\), with probability-Haar inner product. Observe only the coordinate-dominance chamber
\[
\Omega_{d,k}=\{z\in S^{2d-1}: |z_1|>\max_{2\le j\le k}|z_j|\}.
\]
This is one of the \(k\) symmetric cells in the moment-map simplex of the first \(k\) coordinates. Write
\[
\Lambda_{k,m}=\sum_{j=0}^{k-1}(-1)^j\binom{k-1}{j}\frac1{(j+1)^{m+1}},\qquad
\mu_{k,m}=\frac{1-\Lambda_{k,m}}{k-1}.
\]
The sharp concentration inequality is
\[
\boxed{\mu_{k,m}\|f\|_2^2\le\int_{\Omega_{d,k}}|f(z)|^2\,d\sigma(z)\le\Lambda_{k,m}\|f\|_2^2\quad(f\in\mathcal H_{d,m}).}
\]
For \(m\ge1\), upper equality holds exactly for scalar multiples of \(z_1^m\), and lower equality holds exactly for the nonzero members of \(\operatorname{span}_{\mathbb C}\{z_2^m,\dots,z_k^m\}\). Thus the sharp squared singular-value condition number and its fixed-\(k\) degree asymptotic are
\[
\boxed{\kappa_{k,m}=\frac{(k-1)\Lambda_{k,m}}{1-\Lambda_{k,m}},\qquad
\lim_{m\to\infty}\frac{\kappa_{k,m}}{2^{m+1}}=1.}
\]
The two extreme eigenvalues, all equality cases, and the condition number are independent of the ambient complex dimension \(d\). In fact every eigenvalue is rational, and the full finite spectrum is given explicitly below. For \(m=0\), the sole eigenvalue is \(1/k\).

For example, at \(k=3,m=2\), the sharp upper and lower energy fractions are \(85/108\) and \(23/216\), so the exact squared condition number is \(170/23\). The upper eigenspace is one-dimensional, whereas the lower eigenspace has dimension two.

## Assumptions and scope

The measure \(\sigma\) on the complex unit sphere has total mass one. The boundaries \(|z_i|=|z_j|\) have measure zero. The degree \(m\) is exact, not a band cutoff; polynomials are holomorphic, not arbitrary real harmonic polynomials. For each multi-index \(\alpha\in\mathbb N_0^d\) with \(|\alpha|=m\), normalized monomials are
\[
e_\alpha(z)=\left(\frac{(d)_m}{\alpha!}\right)^{1/2}z^\alpha,
\quad(d)_m=d(d+1)\cdots(d+m-1).
\]
They form an orthonormal basis. Let \(T\) be the compression of multiplication by \(\mathbf1_{\Omega_{d,k}}\) to \(\mathcal H_{d,m}\). All \(e_\alpha\) are eigenvectors, with eigenvalue
\[
p(\alpha_1,\ldots,\alpha_k)=\int_0^\infty\frac{e^{-t}t^{\alpha_1}}{\alpha_1!}
\prod_{j=2}^{k}\left(1-e^{-t}\sum_{r=0}^{\alpha_j}\frac{t^r}{r!}\right)dt.
\]
This is the **complete spectrum as a multiset** when \(\alpha\) ranges over every composition \(|\alpha|=m\) of length \(d\); any coincident eigenvalues have their natural summed multiplicities. The value depends only on the first \(k\) exponents, not the remaining \(d-k\). It is exactly rational, with the finite-sum evaluation
\[
p(\alpha_1,\ldots,\alpha_k)=\sum_{A\subseteq\{2,\ldots,k\}}(-1)^{|A|}
\sum_{0\le r_j\le\alpha_j\ (j\in A)}
\frac{(\alpha_1+\sum_{j\in A}r_j)!}
{\alpha_1!\,(|A|+1)^{\alpha_1+\sum_{j\in A}r_j+1}\prod_{j\in A}r_j!}.
\]
The empty-set contribution is one. In particular all eigenvalues lie strictly between zero and one.

## Proof

**1. Diagonalization and probabilistic representation.** Independently rotating each complex coordinate preserves both \(\sigma\) and the chamber. Hence the monomials are mutually orthogonal even after restriction, which diagonalizes \(T\). The standard spherical moment is
\[
\int_{S^{2d-1}}|z^\alpha|^2d\sigma=\frac{\alpha!}{(d)_m}.
\]
Under the probability law with density \(|e_\alpha|^2\) relative to \(\sigma\), squared coordinate moduli follow \(\mathrm{Dirichlet}(\alpha_1+1,\ldots,\alpha_d+1)\). Write this Dirichlet vector as independent unit-rate gamma variables, of corresponding shapes, divided by their common sum. The chamber depends only on ordering, so normalization cancels. Conditioning on the first gamma variable gives the displayed integral. Expanding the other cumulative distributions and integrating each gamma monomial gives the finite rational sum.

**2. Strict placement of the degree.** Fix \(m\ge1\). Increasing the shape of the first gamma variable strictly increases the event that it exceeds all rivals, by coupling the higher integer-shape gamma with an additional independent unit exponential. Increasing the shape of any of the next \(k-1\) gamma variables strictly decreases that event. Shapes of all other coordinates do not enter it. Thus an upper maximizer must put every exponent unit into coordinate one, and a lower minimizer must put every exponent unit into the rival coordinates. The strict inequalities follow because every gamma density is positive on \((0,\infty)\).

**3. Concentrating degree into a single rival.** For every \(t>0\) define
\[
F_a(t)=\Pr\{\mathrm{Gamma}(a+1,1)\le t\}
=\Pr\{\mathrm{Poisson}(t)\ge a+1\},\qquad a\in\mathbb N_0.
\]
This sequence is strictly log-concave in its integer index. Indeed, write \(q_a=e^{-t}t^a/a!\), so
\[
\frac{q_a}{F_{a-1}(t)}=
\left[1+\sum_{j=1}^\infty\frac{t^j}{(a+1)(a+2)\cdots(a+j)}\right]^{-1}
\quad(a\ge1).
\]
The right side is strictly increasing with \(a\), and thus \(F_a(t)/F_{a-1}(t)=1-q_a/F_{a-1}(t)\) is strictly decreasing. Strict log-concavity implies for integers \(a,b>0\)
\[
F_a(t)F_b(t)>F_0(t)F_{a+b}(t).
\]
In the conditional integral for the chamber, replacing two nonzero rival exponents by their sum on one rival and zero on the other strictly reduces the integrand for every positive \(t\). Iterating proves that the only lower-extremizing monomials are the pure powers \(z_j^m\), \(2\le j\le k\). The Gram operator is diagonal, so its entire lower eigenspace is their linear span.

**4. Exact sharp endpoints and asymptotic.** For the upper pure-power monomial the selected gamma variable has shape \(m+1\), and the other \(k-1\) variables are independent exponentials. Therefore
\[
\Lambda_{k,m}=\mathbb E(1-e^{-G})^{k-1}
=\sum_{j=0}^{k-1}(-1)^j\binom{k-1}{j}(j+1)^{-(m+1)}.
\]
For the lower pure-power monomial, exactly one rival has gamma shape \(m+1\), while the selected variable and the other \(k-2\) rivals are exchangeable exponentials. Conditional on the event that their maximum exceeds the gamma rival, each of the \(k-1\) exponentials is equally likely to be the maximum. The complement probability that the gamma beats all exponentials is \(\Lambda_{k,m}\); thus \(\mu_{k,m}=(1-\Lambda_{k,m})/(k-1)\). This gives every sharp equality case and the ratio formula.

For fixed \(k\), inclusion-exclusion yields
\[
1-\Lambda_{k,m}=(k-1)2^{-(m+1)}+O_k(3^{-(m+1)}),
\]
whence \(\kappa_{k,m}/2^{m+1}\to1\). The degree-zero case is the constant monomial and the chamber has relative Haar mass \(1/k\) by symmetry.

## Verification

The attached `verify.py` computes eigenvalues in exact rational arithmetic from the inclusion-exclusion formula and exhaustively checks all exponent allocations for \(2\le k\le5\) and \(0\le m\le7\), including all equality cases. It also compares nine independent 65-digit gamma-CDF quadratures to rational eigenvalues, with error below \(10^{-50}\). The computations are finite diagnostic checks; the infinite-parameter theorem follows from the preceding analytic proof, especially strict log-concavity of Poisson tails.

Run with Python 3 and `mpmath`: `python verify.py`.

## Relationship to prior work

The general torus-invariant Toeplitz formalism, monomial diagonalization and moment-map geometry are established in the work of Morales-Ramos–Quiroga-Barranco–Sánchez-Nungaray (2016), Bauer–Hagger–Vasilevski (2018), and Quiroga-Barranco (2021). Those broad operator frameworks are not claimed as new. The contribution here is the explicit **all-degree sharp minimum and maximum**, complete extremizer classification, exact stability ratio, and its dimension- and fixed-chamber-size universal exponential law for the specified coordinate-order chamber. They require an ordering argument for all integer gamma-shape allocations, not merely a generic integral representation.

Prior studied holomorphic union caps and product caps concern different observation sets: their coordinate thresholds or products cannot, for a fixed threshold, describe the moving coordinate-order chamber. Their sharp eigenvalue claims therefore neither state nor imply this theorem without an additional independent optimization argument.

## Limitations

Only the exact-degree holomorphic subspace is considered. The claim does not address arbitrary nonholomorphic spherical harmonics, arbitrary coordinate-order unions, all-degree Hardy bands, unequal coordinate thresholds, or the full infinite-dimensional Toeplitz operator. The fixed-\(k\) asymptotic is not asserted uniform when \(k\) grows with degree. Generic torus-invariant symbol formulas predate this result; global historical originality remains subject to specialist source discovery and independent audit.

## References

1. W. Bauer, R. Hagger, N. Vasilevski, *Algebras of Toeplitz operators on the \(n\)-dimensional unit ball*, arXiv:1808.10372v1, first posted 2018-08-30, especially Sections 1–3.
2. R. Quiroga-Barranco, *Toeplitz operators, \(\mathbb T^m\)-invariance and quasi-homogeneous symbols*, arXiv:2106.01980v1, first posted 2021-06-03, especially Sections 4 and 7.
3. M. A. Morales-Ramos, R. Quiroga-Barranco, A. Sánchez-Nungaray, *Toeplitz operators, pseudo-homogeneous symbols and moment maps on the complex projective space*, arXiv:1608.08543v1, first posted 2016-08-30, especially Sections 2–5.
