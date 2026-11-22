# Radial-universal spectral collisions for angular quadratic Toeplitz operators

## Finding

The number of distinct eigenvalues of a finite-dimensional Toeplitz compression can change its order of growth when the symbol matrix has an exact arithmetic resonance. For the angular quadratic symbols considered here, the complete answer in three complex variables is independent of the radial weight and holds for **arbitrary complex matrices, including nonnormal ones**.

Let \(N_A(d)\) denote the number of distinct spectral values on homogeneous polynomials of degree \(d\), and let \(H_A(t)=\sum_{d\ge0}N_A(d)t^d\). Writing \(\lambda_1,\lambda_2,\lambda_3\) for the eigenvalues of \(A\) counted algebraically, the classification is:

- One distinct eigenvalue: \(H_A(t)=(1-t)^{-1}\), so \(N_A(d)=1\).
- Exactly two distinct eigenvalues: \(H_A(t)=(1-t)^{-2}\), so \(N_A(d)=d+1\).
- Three distinct eigenvalues with \(\mathbb Q\)-linearly independent gaps: \(H_A(t)=(1-t)^{-3}\), so \(N_A(d)=\binom{d+2}{2}\).
- Three distinct eigenvalues with rationally dependent gaps: uniquely choose an affine arithmetic normalization \(\{c,c+\eta p,c+\eta q\}\), where \(\eta\ne0\), \(0<p<q\), and \(\gcd(p,q)=1\). Then

\[
H_A(t)=\frac{1-t^q}{(1-t)^3},\qquad
N_A(d)=\binom{d+2}{2}-\mathbf1_{d\ge q}\binom{d-q+2}{2}.
\]

In the resonant case, the first equality between distinct occupation-index spectral values occurs **exactly at degree \(q\)**, and \(N_A(d)=qd+q(3-q)/2\) for every \(d\ge q\). In particular, the integer \(p\) does not affect the cardinality sequence once the primitive span \(q\) is fixed. Across all cases, \(N_A(d)\to\infty\) precisely when \(A\) has at least two distinct eigenvalues. A nonzero nilpotent matrix has only one spectral value on each homogeneous block, illustrating why nonscalarity is not enough.

## Assumptions and scope

Let \(\mu\) be a nonzero finite, \(U(3)\)-invariant, positive Borel measure on \(\mathbb C^3\), with \(\mu(\{0\})=0\) and \(0<\int\|z\|^{2d}\,d\mu(z)<\infty\) for every integer \(d\ge0\). Define \(\mathcal H_\mu\) as the closure of the holomorphic polynomials in \(L^2(\mu)\), and \(P\) as its orthogonal projection. For any \(A=(A_{ij})\in M_3(\mathbb C)\), put

\[
\varphi_A(z)=\frac{\sum_{i,j=1}^3 A_{ij}z_i\overline{z_j}}{\sum_{k=1}^3|z_k|^2},\qquad z\ne0,
\qquad T_A f=P(\varphi_A f).
\]

The bounded symbol has \(\|\varphi_A\|_\infty\le\|A\|\). The definition covers rotation-invariant weighted Bergman spaces on balls, holomorphic Hardy spaces on spheres, and Gaussian Fock spaces, as well as other radial measures with all positive moments. By scalar-rotation invariance, the degree-\(d\) homogeneous polynomial spaces \(\mathcal H_d\) are mutually orthogonal, have dimension \(\binom{d+2}{2}\), and reduce \(T_A\). The spectrum below is **the finite-block spectrum**, not the full operator spectrum or its essential spectrum. Neither \(A\) nor the symbol is required to be Hermitian.

Two complex numbers are \(\mathbb Q\)-linearly independent if no nontrivial rational linear combination vanishes. If the three eigenvalues are distinct and their two gaps are \(\mathbb Q\)-dependent, their locations lie on one affine real line with commensurable spacing, so the stated primitive integers \(p,q\) exist after choosing its extremal points as endpoints. They are unique up to reversing the line and changing \(p\) to \(q-p\); the span \(q\) is canonical.

## Proof

**1. Exact angular compression.** Write \(z=r\omega\) with \(\omega\) uniformly distributed on the unit sphere \(S^5\); the radial and angular measures separate by \(U(3)\)-invariance. For any \(\alpha=(\alpha_1,\alpha_2,\alpha_3)\in\mathbb N_0^3\) of total degree \(d\), the Dirichlet angular-moment identity is

\[
\int_{S^5}|\omega^\alpha|^2\,d\sigma(\omega)
=\frac{2\,\alpha_1!\alpha_2!\alpha_3!}{(d+2)!}.
\]

In the matrix element of \(T_{z_i\overline{z_j}/\|z\|^2}\), the radial moment is of degree \(2d\) both in numerator and denominator and therefore cancels. The displayed identity gives, for every monomial \(z^\alpha\),

\[
T_{z_i\overline{z_j}/\|z\|^2}z^\alpha
=\frac{z_i\partial_{z_j}z^\alpha+\delta_{ij}z^\alpha}{d+3}.
\]

This also holds when \(\alpha_j=0\), with the differentiation term zero. Summing over \(A_{ij}\) proves the **exact identity of operators** on \(\mathcal H_d\):

\[
(d+3)\,T_A|_{\mathcal H_d}
=\operatorname{tr}(A)I+\sum_{i,j=1}^3 A_{ij}z_i\partial_{z_j}.
\]

No approximation, large-degree limit, or radial-density assumption is used.

**2. General finite-block spectrum.** The differential part is the induced action of \(A\) on the symmetric degree-\(d\) tensor power of \(\mathbb C^3\). Triangularize \(A\) over \(\mathbb C\), using an invertible similarity, not necessarily a unitary one. Its induced action on the symmetric tensor power is triangular with diagonal entries \(\alpha_1\lambda_1+\alpha_2\lambda_2+\alpha_3\lambda_3\), indexed by \(\alpha_j\ge0\) and \(\sum\alpha_j=d\). Thus, as a *set* without multiplicities,

\[
\operatorname{sp}(T_A|_{\mathcal H_d})=
\left\{\frac{\operatorname{tr}A+\alpha_1\lambda_1+\alpha_2\lambda_2+\alpha_3\lambda_3}{d+3}:\ \alpha_j\in\mathbb N_0,\ \sum\alpha_j=d\right\}.
\]

This argument applies to Jordan matrices and other nonnormal matrices; nilpotent contributions may alter Jordan structure but never the displayed spectral set.

**3. Unresonant and lower-rank cases.** With one distinct \(\lambda\), the set has one point. With exactly two distinct values, the number of occupations assigned to the first eigenspace ranges over the \(d+1\) integers from \(0\) to \(d\), all giving distinct spectral values. For three distinct values, subtract the constant \(d\lambda_1\); the remaining affine parameter is \(\alpha_2(\lambda_2-\lambda_1)+\alpha_3(\lambda_3-\lambda_1)\). If the two gaps are \(\mathbb Q\)-independent, distinct pairs of nonnegative occupations yield distinct sums. Hence every one of the \(\binom{d+2}{2}\) triples contributes a different eigenvalue. Summing the corresponding sequences in \(d\) gives the first three generating series.

**4. Primitive arithmetic resonance.** In the remaining case, after the affine normalization the varying part of every eigenvalue is \(p\alpha_p+q\alpha_q\), with \(\alpha_0+\alpha_p+\alpha_q=d\). The exact relation

\[
q p=(q-p)\cdot0+p q
\]

shows that \(q\) copies of the middle level may be replaced by \(q-p\) copies of the lower level and \(p\) copies of the upper level, without changing the occupation total or its spectral value. Repeatedly apply this replacement until \(0\le\alpha_p<q\). It always terminates, and every occupation triple reduces to one in this range.

To prove uniqueness, if two reduced triples of the same total degree have equal weighted value, then

\[
p(\alpha_p-\beta_p)+q(\alpha_q-\beta_q)=0.
\]

Since \(\gcd(p,q)=1\), the difference \(\alpha_p-\beta_p\) is divisible by \(q\). But both lie between \(0\) and \(q-1\), forcing equality; then the upper and lower occupations agree as well. Therefore the reduced triples are in bijection with the distinct spectral values, and their number is

\[
N_A(d)=\sum_{j=0}^{\min(d,q-1)}(d-j+1)
=\binom{d+2}{2}-\mathbf1_{d\ge q}\binom{d-q+2}{2}.
\]

The generating series follows by subtraction of the shifted triangular-number sequence. Before degree \(q\) every triple is already reduced, so no collision is possible. At degree \(q\), the two different triples in the displayed relation collide. The closed linear formula for \(d\ge q\) follows by expanding the binomial coefficients. This proves all cases and their growth statements.

## Verification

The standalone `check.py` uses exact rational arithmetic and symbolic matrices. It checks the spherical Dirichlet moment ratios, the normalized operator formula for nonnormal test matrices, spectral count identities for every coprime \(1\le p<q\le20\) through degree \(2q+2\), and selected Jordan and repeated-eigenvalue examples. The current package run passed **4,499** finite assertions. This is supplementary consistency evidence only; it neither enumerates all parameter choices nor proves the infinite theorem, which is established analytically above. Run it with `python check.py` after extracting the complete record.

## Relationship to prior work

Bauer and Rodriguez Rodriguez (2022), Section 3.6 and their second concluding open problem, specifically identify growth of the cardinalities of homogeneous finite-block Toeplitz spectra as relevant to the Gelfand theory and radicals of associated Banach algebras. Their paper develops the general finite-block framework, not the arithmetic collision classification for the present angular quadratic family. Quiroga-Barranco (2021) derives monomial action formulas for much broader torus-invariant and quasi-homogeneous symbols on Bergman balls. Morales-Ramos, Quiroga-Barranco, and Sánchez-Nungaray (2016) explain the projective moment-map setting; the three-level occupation and monomial-curve arithmetic behind the present proof are classical structures, not claimed as newly invented machinery.

The specific contribution is a full, radially universal, exact **four-case spectral-cardinality/Hilbert-series classification** for this three-variable class, including nonnormal matrices, the first collision index and the rational-resonance growth transition. This treats a natural special family relevant to the cited open question; **it does not solve the open problem in general**.

## Limitations

The theorem is for degree-block spectra in three complex coordinates and angular symbols quadratic in the coordinates. It does not classify arbitrary generalized pseudo-homogeneous symbols, infinite-dimensional spectrum, Gelfand radicals, or spectral multiplicities beyond identifying the distinct-value set. The result depends on full unitary invariance of the measure; mere torus invariance does not generally cancel radial moments in the same manner. Standard representation-theoretic and toric equivalents may occur in literature under different terminology; the novelty comparison cannot exclude unindexed prior statements. The computations are finite supplemental checks rather than independent verification.

## References

1. W. Bauer and M. A. Rodriguez Rodriguez, *Commutative Toeplitz Algebras and Their Gelfand Theory: Old and New Results*, Complex Analysis and Operator Theory **16**, article 77 (2022), published 30 June 2022; https://doi.org/10.1007/s11785-022-01248-1 . See §§3.3, 3.6 and concluding Problem 2.
2. R. Quiroga-Barranco, *Toeplitz operators, \(\mathbb T^m\)-invariance and quasi-homogeneous symbols*, arXiv:2106.01980, first public 3 June 2021; https://arxiv.org/abs/2106.01980 .
3. M. A. Morales-Ramos, R. Quiroga-Barranco, and A. Sánchez-Nungaray, *Toeplitz operators, pseudo-homogeneous symbols and moment maps on the complex projective space*, arXiv:1608.08543, first public 30 August 2016; https://arxiv.org/abs/1608.08543 .
4. *On Convergence of Toeplitz Quantization of the Sphere*, Mathematics **12**, 3565 (2024); https://www.mdpi.com/2227-7390/12/22/3565 .
