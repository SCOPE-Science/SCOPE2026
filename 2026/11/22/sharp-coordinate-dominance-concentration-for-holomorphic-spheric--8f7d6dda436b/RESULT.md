# Sharp coordinate-dominance concentration for holomorphic spherical polynomials

## Finding

Let \(d\ge k\ge2\) and let \(\mathcal H_{d,m}\) be the homogeneous holomorphic polynomials of degree \(m\) on the complex unit sphere, with probability Haar measure \(\sigma\). Set \(\Omega_{d,k}=\{z:|z_1|>\max_{2\le j\le k}|z_j|\}\). For \(m\ge1\), define
\[
\Lambda_{k,m}=\sum_{j=0}^{k-1}(-1)^j\binom{k-1}{j}(j+1)^{-(m+1)},\qquad
\mu_{k,m}=\frac{1-\Lambda_{k,m}}{k-1}.
\]
Then
\[
\mu_{k,m}\|f\|_2^2\le\int_{\Omega_{d,k}} |f|^2d\sigma\le\Lambda_{k,m}\|f\|_2^2
\quad(f\in\mathcal H_{d,m}).
\]
The upper equality space is \(\mathbb C z_1^m\); the lower equality space is \(\operatorname{span}_{\mathbb C}\{z_2^m,\ldots,z_k^m\}\). In particular the zero polynomial gives equality on both sides. Both bounds are sharp. The squared singular-value condition number of restriction is
\[
\kappa_{k,m}=\frac{(k-1)\Lambda_{k,m}}{1-\Lambda_{k,m}},\qquad
\lim_{m\to\infty}\frac{\kappa_{k,m}}{2^{m+1}}=1\quad\text{for fixed }k.
\]
The extreme eigenvalues and squared condition number do not depend on \(d\). For \(m=0\), the only eigenvalue is \(1/k\). As a positive-degree example, at \(k=3,m=2\) the sharp endpoints are \(23/216\) and \(85/108\), with squared condition number \(170/23\).

## Assumptions and scope

The subspace is exact degree, not a degree band. Coordinates after \(k\) are not constrained by the chamber. Ties in coordinate moduli have measure zero, and no real or nonholomorphic harmonic analogue is asserted. The degree asymptotic is not stated uniformly in \(k\).

## Full spectrum and proof

**Diagonalization.** Torus invariance of the measure and chamber makes distinct monomials orthogonal both on the whole sphere and on the chamber. For \(|\alpha|=m\) the normalized monomial is \(e_\alpha=((d)_m/\alpha!)^{1/2}z^\alpha\), where \((d)_m=d(d+1)\cdots(d+m-1)\). Indeed, squared coordinate moduli under Haar measure are uniform on the simplex, by normalizing independent complex Gaussian coordinates, and their Dirichlet moments give \(\int|z^\alpha|^2d\sigma=\alpha!/(d)_m\). Under the reweighted law \(|e_\alpha|^2d\sigma\), the squared moduli are Dirichlet with parameters \(1+\alpha_j\). Represent them by independent unit-rate gamma variables \(G_j\) of those shapes divided by their common sum. Normalization preserves ordering, so the compression eigenvalue is \(p(\alpha)=\Pr(G_1>\max_{2\le j\le k}G_j)\).

**Exact rational spectrum.** Conditional on \(G_1=t\),
\[
p(\alpha)=\int_0^\infty \frac{e^{-t}t^{\alpha_1}}{\alpha_1!}
\prod_{j=2}^{k}\left(1-e^{-t}\sum_{r=0}^{\alpha_j}\frac{t^r}{r!}\right)dt.
\]
Expanding and integrating gamma monomials gives
\[
p(\alpha)=\sum_{A\subseteq\{2,\ldots,k\}}(-1)^{|A|}
\sum_{0\le r_j\le\alpha_j\ (j\in A)}
\frac{(\alpha_1+\sum_{j\in A}r_j)!}{\alpha_1!(|A|+1)^{\alpha_1+\sum_{j\in A}r_j+1}\prod_{j\in A}r_j!},
\]
with empty-set summand one. These are all eigenvalues, counting repetitions as \(\alpha\) ranges over length-\(d\) compositions of \(m\). Each lies strictly between zero and one by positivity of the gamma densities.

**Locating the upper and lower eigenspaces.** Adding a degree unit in a tested coordinate adds an independent unit-rate exponential to its gamma variable. This strictly increases \(p\) for coordinate one and strictly decreases \(p\) for a rival coordinate, as the event boundary can be crossed with positive probability by positivity of the densities. Unobserved coordinates do not affect \(p\). Moving units to coordinate one therefore gives the sole upper extremizing allocation; moving units from coordinate one or an unobserved coordinate to a rival proves every lower extremizer allocates all units among the rivals.

For \(t>0\) let \(F_a(t)=\Pr(\mathrm{Gamma}(a+1,1)\le t)=\Pr(\operatorname{Poisson}(t)\ge a+1)\). Put \(q_a=e^{-t}t^a/a!\). For \(a\ge1\),
\[
\frac{q_a}{F_{a-1}(t)}=\left[1+\sum_{j=1}^{\infty}\frac{t^j}{(a+1)(a+2)\cdots(a+j)}\right]^{-1}.
\]
The ratio on the left strictly increases with \(a\), so \(F_a/F_{a-1}=1-q_a/F_{a-1}\) strictly decreases. Therefore \(F_aF_b>F_0F_{a+b}\) for positive integers \(a,b\), by comparing the first \(a\) ratios with the \(a\) ratios starting after index \(b\). Merging two positive rival exponents onto just one of them strictly decreases the product of rival CDFs at every \(t>0\). Iteration proves that the only lower extremizing allocations are pure rival powers. Since the compression is diagonal in the monomial basis, the corresponding monomials span the full equality spaces displayed above.

**Endpoint formulas.** At the upper pure power, \(G_1\) has shape \(m+1\) and the rivals are unit exponentials. The winning probability is \(\mathbb E(1-e^{-G_1})^{k-1}\), equal to \(\Lambda_{k,m}\) by the binomial expansion and the gamma Laplace transform. At a lower pure power one rival has the shape \(m+1\), and the \(k-1\) exponentials are exchangeable. The probability that the gamma rival loses is \(1-\Lambda_{k,m}\), divided equally among the exponentials' winning events; this gives \(\mu_{k,m}\). The squared singular values are the compression eigenvalues, so their ratio gives \(\kappa_{k,m}\). For fixed \(k\),
\[
1-\Lambda_{k,m}=(k-1)2^{-(m+1)}+O_k(3^{-(m+1)}),
\]
which gives the stated limit. Degree zero gives the constant monomial and relative chamber area \(1/k\) by symmetry.

## Verification and prior work

The supplied `verify.py` (Python 3, `mpmath`) checks exact rational spectra in the small cases \(d=k\in\{2,3,4,5\}\), \(0\le m\le7\), including equality allocations. It also compares nine high-precision gamma-CDF quadratures with exact rational values. These finite checks are supplementary; the proof, including monotonic coupling and strict rival merging, covers every dimension and degree.

Torus-invariant Toeplitz diagonalization and moment-map geometry are established frameworks, not the claim here. The result is the all-degree sharp order-chamber optimization, its equality spaces and associated conditioning law. Coordinate-threshold union caps and product caps pose different optimization problems. The literature comparison is not a claim of absolute priority.

## References

- W. Bauer, R. Hagger and N. Vasilevski, *Algebras of Toeplitz operators on the n-dimensional unit ball*, arXiv:1808.10372, especially §3.
- R. Quiroga-Barranco, *Toeplitz operators, torus invariance and quasi-homogeneous symbols*, arXiv:2106.01980, Proposition 4.10 and equations (5.2)–(5.4).
- M. A. Morales-Ramos, R. Quiroga-Barranco and A. Sánchez-Nungaray, *Toeplitz operators, pseudo-homogeneous symbols and moment maps on the complex projective space*, arXiv:1608.08543.
