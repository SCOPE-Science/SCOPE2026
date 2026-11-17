# A boundary eigenarc for the Hilbert–Schmidt spectrum of a Bergman completely positive map

## Finding

Let \(\Psi\) be the unital completely positive map of Panja associated with ordinary analytic Bergman space on the unit disk, restricted to the Hilbert–Schmidt ideal \(\mathcal S_2\). Its **entire point spectrum** is
\[
\boxed{\sigma_{\rm p}(\Psi|_{\mathcal S_2})
=\{\lambda\in\mathbb C:|2\lambda-1|<1\}\ \cup\
\{\lambda\in\mathbb C:|2\lambda-1|=1,\ \operatorname{Re}(2\lambda-1)<\tfrac12\}.}
\]
Every point eigenvalue has infinite geometric multiplicity. In particular, the circular boundary exhibits a genuine transition: the arc with \(\operatorname{Re}(2\lambda-1)<1/2\) consists of eigenvalues, while the complementary arc, including its two endpoints and \(\lambda=1\), does not. No assertion about the full or essential spectrum is made.

## Assumptions and scope

Use normalized area measure \(dA=\pi^{-1}dx\,dy\) on the disk. Ordinary Bergman space \(A^2\) has orthonormal basis \(e_j(z)=\sqrt{j+1}\,z^j\) and moments \(\omega_j=1/(j+1)\). Write \(S=M_z\), its Cauchy dual \(S'=S(S^*S)^{-1}\), and \(Q_j\) for the projection onto the closed span of \(e_j,e_{j+1},\ldots\). Thus \(\delta_j=\omega_j/\omega_{j+1}=(j+2)/(j+1)\) and \(\delta_0=2\). Define the normal unital completely positive map on bounded operators by
\[
\Psi(X)=\frac12\left(S'^*XS'+\sum_{j=1}^\infty(\delta_{j-1}-\delta_j)Q_jXQ_j\right).
\]
This is the map of Panja (2026, equation (4.10)); the sum converges in operator norm because the nonnegative scalar coefficients telescope. It restricts boundedly to \(\mathcal S_2\), as every summand acts boundedly on that ideal and the sum converges in its operator norm.

## Proof

Put \(E_{ij}=|e_i\rangle\langle e_j|\), \(i,j\ge0\). Since \(S'e_j=\sqrt{\delta_j}\,e_{j+1}\), direct substitution gives
\[
\Psi(E_{ij})=\frac{\min(i,j)}{2(\min(i,j)+1)}E_{ij}
+\mathbf1_{i,j\ge1}\frac{\sqrt{\delta_{i-1}\delta_{j-1}}}{2}E_{i-1,j-1}.
\tag{1}
\]
The Hilbert–Schmidt space is the orthogonal sum of the mutually invariant diagonal subspaces \(\mathcal H_d=\overline{\operatorname{span}}\{E_{n,n+d}:n\ge0\}\), \(d\ge0\), and their negative-diagonal analogues. Each is canonically \(\ell^2(\mathbb N_0)\). An eigenvector supported on \(\mathcal H_d\) with coefficients \((u_n)\) obeys
\[
(\lambda-a_n)u_n=b_{n+1,d}u_{n+1},\quad
 a_n=\frac{n}{2(n+1)},\quad
 b_{n+1,d}=\frac12\sqrt{\frac{n+2}{n+1}\frac{n+d+2}{n+d+1}}>0.
\tag{2}
\]
Thus the nonzero solution space on each diagonal is one-dimensional, determined by \(u_0\). Writing \(z=2\lambda-1\), iteration telescopes exactly to
\[
\boxed{u_n=u_0\sqrt{\frac{d+1}{(n+1)(n+d+1)}}
\prod_{j=1}^{n}\left(z+\frac1j\right),\quad n\ge0.}
\tag{3}
\]
This identity also handles \(z=0\) and all terminating products \(z=-1/j\) without gamma-function conventions.

If \(z\ne0\) and \(z\notin\{-1/j:j\ge1\}\), Euler's gamma-product identity and the gamma-ratio asymptotic yield
\[
u_n=u_0\sqrt{\frac{d+1}{(n+1)(n+d+1)}}
\frac{z^n\Gamma(n+1+z^{-1})}{\Gamma(1+z^{-1})\Gamma(n+1)},
\qquad
|u_n|\sim C_{z,d,u_0}|z|^n n^{\operatorname{Re}(z^{-1})-1},
\tag{4}
\]
where \(C_{z,d,u_0}>0\) when \(u_0\ne0\). For \(z=0\), formula (3) gives factorial decay. At \(z=-1/j\) the product terminates and gives a finitely supported eigenvector.

For \(|z|<1\), every diagonal solution belongs to \(\ell^2\), including the terminating exceptions. For \(|z|>1\), none does. On \(|z|=1\) with \(z=e^{i\theta}\), apart from the terminating case \(z=-1\) which is already square summable, the squared coefficients behave like \(n^{2(\cos\theta-1)}\); the series converges precisely when \(\cos\theta<1/2\). At equality it is harmonic and diverges. Hence the displayed point-spectrum set is exact on every diagonal.

Finally, any Hilbert–Schmidt eigenvector decomposes orthogonally into diagonal eigenvectors, since these subspaces reduce the coefficient calculation in (1). Conversely, for every admitted \(\lambda\), choosing \(u_0=1\) in (3) on each different nonnegative diagonal gives countably many mutually orthogonal nonzero eigenvectors. Therefore the point spectrum is exactly as claimed, and each eigenvalue has infinite geometric multiplicity.

## Verification

The algebra in (1) follows by applying the Kraus terms to a single matrix unit. In (2), all denominators are strictly positive, including the boundary index \(n=0\). The product (3) follows from telescoping \(\prod_{k=0}^{n-1}[(k+1)(k+d+1)/((k+2)(k+d+2))]^{1/2}\). The gamma-asymptotic step is used only away from terminating products, and the borderline exponent is treated as a divergent harmonic series. The accompanying standalone checker verifies the recurrence and finite product at rational and complex parameters and samples the limiting boundary exponents; these finite checks supplement rather than replace the proof.

## Relationship to prior work

Panja (2026) constructed \(\Psi\) and identified its bounded-operator fixed points as harmonic-symbol Toeplitz operators, also excluding nonzero compact fixed points. That gives the absence of the eigenvalue \(1\) on \(\mathcal S_2\), but does not specify the other point eigenvalues or the Hilbert–Schmidt boundary arc. General weighted-backward-shift theory motivates solving diagonal recurrences, but the exact coefficients and boundary threshold here come from Panja's specific map. No claim is made that the general recurrence technique is new.

## Limitations

The result addresses the ordinary (unweighted) analytic Bergman space and the Hilbert–Schmidt ideal only; it does not classify spectral points on \(\mathcal S_p\) for other \(p\), nor the whole spectrum, Fredholm essential spectrum, or the corresponding map for general admissible radial weights. The literature comparison is limited to the inspected sources and scholarly-index searches; an unindexed equivalent analysis remains possible. Independent review has not been performed.

## References

1. S. Panja, *Toeplitz operators with bounded harmonic symbols on weighted Bergman spaces are the fixed points of a normal unital completely positive map*, arXiv:2611.09731v1 (first posted 2026-11-06), especially equation (4.10), Lemma 4.4 and Theorem 4.5. https://arxiv.org/abs/2611.09731
2. A. Brown and P. R. Halmos, *Algebraic properties of Toeplitz operators*, J. Reine Angew. Math. 213 (1964), 89–102 (background for fixed-point characterization).
