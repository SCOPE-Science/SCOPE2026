# Dimension-free sharp phase-wedge concentration of holomorphic quadratic harmonics

## Finding

Let \(d\ge2\) be an integer and let \(\mathcal H_m^{\mathrm{hol}}(\mathbb C^d)\) be the complex space of homogeneous holomorphic polynomials of degree \(m\), equipped with the probability-surface-measure norm on \(S^{2d-1}\). For \(0<\theta<\pi\), define
\[
\Omega_\theta=\{z\in S^{2d-1}:\arg(z_1\overline z_2)\in(-\theta,\theta)\},
\quad \langle T_{d,m,\theta}p,q\rangle=\int_{\Omega_\theta}p\overline q\,d\sigma.
\]
Arguments at points with \(z_1z_2=0\) do not affect the integral.

**Theorem (all-degree block reduction and sharp quadratic spectrum).** Every degree-\(m\) concentration operator decomposes explicitly into phase-coupled blocks of size at most \(m+1\). Its largest and smallest eigenvalues equal those of the single two-coordinate block of size \(m+1\), irrespective of ambient complex dimension. In degree \(m=2\), set
\[
\delta=\theta/\pi,\quad a=\sin\theta/4,\quad
c=\sin(2\theta)/(4\pi),\quad
r=\sqrt{c^2/4+9\sin^2\theta/64}.
\]
The complete spectrum, with multiplicities, is
\[
\begin{array}{c|c}
\text{eigenvalue}&\text{multiplicity}\\\hline
\gamma_+=\delta+c/2+r&1\\
\gamma_-=\delta+c/2-r&1\\
\gamma_0=\delta-c&1\\
\alpha_+=\delta+a&d-2\\
\alpha_-=\delta-a&d-2\\
\delta&(d-2)(d-1)/2
\end{array}
\]
(with zero-multiplicity branches omitted). For all \(d\ge2\), the sharp observation bounds on \(\mathcal H_2^{\mathrm{hol}}\) are \(\gamma_-\|p\|_2^2\le\int_{\Omega_\theta}|p|^2d\sigma\le\gamma_+\|p\|_2^2\), and both equalities are attained. The sharp squared restriction condition number is \(\kappa(\theta)=\gamma_+/\gamma_-\), **independent of \(d\)**. Every eigenvalue is strictly between zero and one.

For \(d\ge3\) the six listed branches are mutually distinct except at the single angular threshold \(\theta=\pi/2\), where the five distinct eigenvalues and multiplicities are \(1/8\) (one), \(1/4\) (\(d-2\)), \(1/2\) (\(1+(d-2)(d-1)/2\)), \(3/4\) (\(d-2\)), and \(7/8\) (one). In particular, \(\kappa(\pi/2)=7\), with extremizing lines \(\mathbb C(z_1-z_2)^2\) and \(\mathbb C(z_1+z_2)^2\). For \(d=2\), the only eigenvalues are the three \(\gamma\)-branches.

At each fixed \(0<\theta<\pi\), as \(m\to\infty\), the largest eigenvalue tends to one and the smallest tends to zero, so the dimension-free *fixed-degree* bounds do not become a degree-uniform frame bound.

## Assumptions and scope

All degrees are exact, not cumulative; all polynomials are holomorphic, not arbitrary real spherical harmonics. The region is an arc restriction on the **relative phase** of two complex coordinates rather than a modulus cap. The sphere and all norms use normalized invariant probability measure. The symbol is defined almost everywhere. For each \(m\), all phase-wedge concentration matrices are finite-dimensional Hermitian matrices. The ambient dimension is an arbitrary integer \(d\ge2\); \(m\) is a nonnegative integer.

Let \(B^{(k)}\), \(k\ge0\), be the explicitly dimension-free matrix indexed by \(a,b\in\{0,\ldots,k\}\):
\[
B^{(k)}_{ab}=\frac{\Gamma(1+(a+b)/2)\Gamma(1+k-(a+b)/2)}{\sqrt{a!(k-a)!b!(k-b)!}}F_{a-b}(\theta),
\quad F_j(\theta)=\begin{cases}\theta/\pi,&j=0,\\ \sin(j\theta)/(\pi j),&j\ne0.\end{cases}
\]
For \(d\ge3\), the full operator is the direct sum of \(B^{(k)}\) with multiplicity \(\binom{d+m-k-3}{m-k}\), for \(k=0,\ldots,m\), with coincident numerical eigenvalues combined. For \(d=2\), it consists only of \(B^{(m)}\). In all cases,
\[
\lambda_{\min}(T_{d,m,\theta})=\lambda_{\min}(B^{(m)}),\qquad
\lambda_{\max}(T_{d,m,\theta})=\lambda_{\max}(B^{(m)}).
\]

## Proof

**Phase and Dirichlet decomposition.** For a normalized homogeneous monomial \(e_\alpha=\sqrt{(d)_m/\alpha!}\,z^\alpha\), with \((d)_m=d(d+1)\cdots(d+m-1)\), the squared moduli of coordinates have Dirichlet distribution with parameters \(1+\alpha_j\). Only relative phase \(\phi_1-\phi_2\) enters the mask. Independent phases of coordinates three through \(d\), and the common phase of coordinates one and two, force a nonzero matrix element only for exponent pairs of the form \((a,k-a,\beta)\) and \((b,k-b,\beta)\), with fixed spectator multiindex \(\beta\) and fixed \(k=m-|\beta|\). The phase integral is \(F_{a-b}(\theta)\). Performing the Dirichlet moment integrals, the factors involving the spectator multiindex and ambient dimension cancel against monomial normalization, giving exactly \(B^{(k)}\) above. Counting spectator multiindices gives the asserted multiplicities.

**Extremal reduction across degrees.** Work on the unit sphere in \(\mathbb C^2\) with the same relative-phase mask. For any degree-\(k\) polynomial \(p\), the identity \(|z_1|^2+|z_2|^2=1\) implies both
\[
\|z_1p\|_2^2+\|z_2p\|_2^2=\|p\|_2^2,
\qquad \int_{\Omega_\theta}(|z_1p|^2+|z_2p|^2)d\sigma=\int_{\Omega_\theta}|p|^2d\sigma.
\]
Thus the Rayleigh quotient of \(p\) is a convex combination of those of its two degree-\(k+1\) multiples; hence \(\lambda_{\min}(B^{(k+1)})\le\lambda_{\min}(B^{(k)})\) and \(\lambda_{\max}(B^{(k+1)})\ge\lambda_{\max}(B^{(k)})\). Since the block with \(k=m\) is present with multiplicity one and all other blocks have \(k<m\), it supplies both global spectral endpoints.

**Quadratic evaluation.** Direct substitution in the matrix-entry formula yields, in the ordered normalized monomial basis \(z_2^2,z_1z_2,z_1^2\),
\[
B^{(2)}=\begin{pmatrix}
\delta&t&c\\ t&\delta&t\\c&t&\delta
\end{pmatrix},\qquad t=3\sin\theta/(8\sqrt2).
\]
The antisymmetric outer-coordinate vector is an eigenvector of eigenvalue \(\gamma_0=\delta-c\); the complementary symmetric two-dimensional block has eigenvalues \(\gamma_\pm=\delta+c/2\pm\sqrt{c^2/4+2t^2}\). Meanwhile \(B^{(1)}\) has eigenvalues \(\delta\pm\sin\theta/4\), and \(B^{(0)}=(\delta)\). The block multiplicity formula completes the exact spectrum. Since \(|c|\le\sin\theta/(2\pi)\), \(r\ge3\sin\theta/8\), and \(3/8-1/(4\pi)>1/4\), it follows strictly that \(\gamma_+>\alpha_+>\gamma_0>\alpha_->\gamma_-\); the central level \(\delta\) lies between \(\alpha_+\) and \(\alpha_-\), crossing \(\gamma_0\) only when \(c=0\), i.e. \(\theta=\pi/2\). The first and last inequalities identify sharp global spectral edges. For any nonzero holomorphic polynomial the positive-measure restriction integral is nonzero on both the phase wedge and its complementary open set: real-analytic continuation on the sphere excludes vanishing on either open set. Compactness of each finite-dimensional unit sphere then gives strict spectral bounds inside \((0,1)\). At the half-phase aperture, \(c=0\) and \(r=3/8\), giving the five-level assertion and the extremizers.

**Loss of degree-uniform stability.** On the two-coordinate unit sphere, \(\|(z_1\pm z_2)^m\|_2^2=2^m/(m+1)\). For \(p_+=(z_1+z_2)^m\), on the wedge complement \(|z_1+z_2|^2\le1+\max(\cos\theta,0)\), so
\[
1-\lambda_{\max}(B^{(m)})\le(m+1)\big[(1+\max(\cos\theta,0))/2\big]^m.
\]
For \(p_-=(z_1-z_2)^m\), on the wedge \(|z_1-z_2|^2\le1+\max(-\cos\theta,0)\), so
\[
\lambda_{\min}(B^{(m)})\le(m+1)\big[(1+\max(-\cos\theta,0))/2\big]^m.
\]
Both geometric bases are strictly below one for each fixed interior angle, proving the final claim. These estimates are not asserted sharp.

## Verification

Run `python verify.py` using Python 3, NumPy, SciPy and SymPy. This standalone program reconstructs block entries from independent numerical sphere-coordinate beta integrals, checks the exact gamma-moment identity, diagonalizes the degree-two blocks, checks their analytic formulas and multiplicities, verifies the cubic characteristic polynomial symbolically and tests monotonic spectral edges for degrees zero through six. Its recorded run passed 42 separate direct quadratures with maximum absolute discrepancy below \(2.7\times10^{-14}\), and multiplicity checks for ambient dimensions two through eight. These finite tests support but do **not** prove the stated universal identities; the analytic arguments above do.

## Relationship to prior work

Quiroga-Barranco (2021, arXiv:2106.01980, Sections 1 and 7) treats general torus-invariant and quasi-homogeneous Toeplitz symbols by representation-theoretic blocks and matrix integrals on weighted Bergman balls. Generic monomial-block methods are **not claimed as new** here: the phase-wedge mask has a relative-phase symmetry and the contribution is the explicit normalized Hardy-sphere phase-wedge matrix, the full quadratic eigenvalues and degeneracy, the dimension-independent sharp endpoints and condition number, and the all-degree extremal comparison with a precise degree-instability limit. Pau and Perälä (2018, arXiv:1805.04339) study Hardy-ball Toeplitz-type boundedness and related properties, not this evaluated finite-degree wedge spectrum. Michel, Plattner and Seibert (2021, arXiv:2103.14650) develop general Slepian constructions on the real sphere, in contrast to the holomorphic relative-phase geometry here. Earlier quasi-homogeneous Toeplitz models, such as García and Vasilevski (2015), further motivate caution: a differently stated or implicit exact evaluation may exist. The novelty assessment is not a claim that generic Toeplitz integral formulas could never be specialized to this example.

## Limitations

The sharp explicit multi-branch spectrum is evaluated only for exact holomorphic degree two, although the structural matrix and extremal reduction hold at all degrees. The high-degree estimates are nonsharp. No result is claimed for arbitrary real spherical harmonics, masks involving more than two relative phases, or general measurable phase masks. Literature priority remains subject to unindexed equivalent calculations in Toeplitz and harmonic-analysis work; numerical checks are finite and no independent mathematical audit has been performed.

## References

1. R. Quiroga-Barranco, *Toeplitz operators, \(\mathbb T^m\)-invariance and quasi-homogeneous symbols*, arXiv:2106.01980, first posted 2021-06-03, https://arxiv.org/abs/2106.01980.
2. J. Pau and A. Perälä, *A Toeplitz type operator on Hardy spaces in the unit ball*, arXiv:1805.04339, first posted 2018-05-11, https://arxiv.org/abs/1805.04339.
3. V. Michel, A. Plattner and M. Seibert, *A Unified Approach to Scalar, Vector, and Tensor Slepian Functions on the Sphere and Their Construction by a Commuting Operator*, arXiv:2103.14650, first posted 2021-03-26, https://arxiv.org/abs/2103.14650.
4. E. García and N. Vasilevski, *Toeplitz operators on the Weighted Bergman Space over the Two-Dimensional Unit Ball*, 2015, DOI 10.1155/2015/306168.
