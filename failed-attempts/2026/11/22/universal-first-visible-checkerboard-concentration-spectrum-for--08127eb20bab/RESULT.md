# Universal first-visible checkerboard concentration spectrum for rotationally invariant polynomial bands

## Finding

Let \(q\ge1\) and \(d\ge2q\) be integers. On \(\mathbb R^d\), consider the parity-checkerboard half-region
\[
\Omega_q=\left\{x:\prod_{j=1}^{2q}x_j>0\right\}.
\]
For every orthogonally invariant probability law with no atom at the origin and positive finite radial moment of order \(2q\), let \(V_L\subset L^2(\mu;\mathbb C)\) be the image of polynomials of total degree at most \(L\). Let \(T_{q,L}=P_{V_L}M_{\mathbf1_{\Omega_q}}|_{V_L}\) be its energy-concentration operator. Then
\[
T_{q,q-1}=\tfrac12I,
\]
and, at the first responsive band \(L=q\), the **entire spectrum**, including multiplicities, is
\[
\operatorname{spec}(T_{q,q})=
\left\{
\left(\frac{1+c_q}{2},\frac12\binom{2q}{q}\right),
\left(\frac12,\dim V_q-\binom{2q}{q}\right),
\left(\frac{1-c_q}{2},\frac12\binom{2q}{q}\right)
\right\},\qquad c_q=\left(\frac2\pi\right)^q.
\]
The ordered pairs designate (eigenvalue, multiplicity). Both noncentral multiplicities are positive; the middle multiplicity may be zero. In particular, the sharp squared recovery condition number on \(V_q\) is
\[
\kappa_q=\frac{1+(2/\pi)^q}{1-(2/\pi)^q},
\]
independent of ambient dimension and radial distribution. The two extreme eigenspaces are spanned by explicit balanced combinations of squarefree degree-\(q\) monomials indexed by complementary halves of the first \(2q\) coordinates.

This statement also applies separately to the pure degree-\(q\) spherical harmonics on \(S^{d-1}\); their spectrum has the same two noncentral eigenvalues and multiplicities, with middle multiplicity \(\dim\mathcal H_q(S^{d-1})-\binom{2q}{q}\).

## Assumptions and scope

Write \(X=RU\) in distribution, where \(U\) is Haar-uniform on \(S^{d-1}\), independent of the nonnegative radius \(R\), and \(\mathbb P(R=0)=0\). Require \(0<\mathbb E[R^{2q}]<\infty\); lower-degree moments are then finite. No radial density and no full-dimensional support are required. The Hilbert space is the image of the stated polynomials in \(L^2(\mu)\), rather than an unjustified formal monomial space. Boundaries of \(\Omega_q\) have zero \(\mu\)-measure. All operators and eigenvalues use the *probability-normalized* full-domain \(L^2\) inner product, and the restriction measure is \(\mu|_{\Omega_q}\), **not** the conditional measure \(2\mu|_{\Omega_q}\).

For surface probability measure on the sphere, \(V_q=\bigoplus_{j=0}^q\mathcal H_j\) and
\[
\dim V_q=\binom{d+q}{q}-\binom{d+q-2}{q-2},\qquad
\dim\mathcal H_q=\binom{d+q-1}{q}-\binom{d+q-3}{q-2},
\]
with binomial coefficients of negative lower index interpreted as zero. For any radial law with full-dimensional support (for example, a nondegenerate isotropic Gaussian), \(\dim V_q=\binom{d+q}{q}\).

## Proof

**(1) Character selection.** Reflections of any coordinate preserve \(\mu\). The commuting unitary coordinate reflections decompose \(V_q\) orthogonally into parity-character spaces indexed by sets \(S\subseteq\{1,\ldots,d\}\), with character \(\chi_S(\varepsilon)=\prod_{j\in S}\varepsilon_j\). A polynomial belonging to character \(S\) must have degree at least \(|S|\). The checkerboard sign function
\[
F(x)=\operatorname{sgn}\left(\prod_{j=1}^{2q}x_j\right)
\]
transforms under reflections by \(\chi_J\), where \(J=\{1,\ldots,2q\}\). Hence \(\langle f,Fg\rangle\) can be nonzero only if \(S\triangle T=J\) for parity sets \(S,T\) of \(f,g\). For polynomial degrees at most \(q-1\), this is impossible because \(|S\triangle T|\le|S|+|T|\le2q-2\). Therefore \(P_{V_{q-1}}M_F|_{V_{q-1}}=0\).

At degree \(q\), equality \(|J|=|S\triangle T|\le|S|+|T|\le2q\) forces \(|S|=|T|=q\), disjoint \(S,T\subseteq J\), and \(T=J\setminus S\). Every character space of this maximal cardinality in \(V_q\) is one-dimensional, spanned by the squarefree monomial \(m_S(x)=\prod_{i\in S}x_i\). There are exactly \(\binom{2q}{q}/2\) unordered complementary pairs. All remaining parity components are annihilated by the compressed sign operator.

**(2) Moment normalization.** Each \(m_S\) has squared norm \(\sigma_q^2=\mathbb E[R^{2q}]\,\mathbb E[\prod_{i\in S}U_i^2]>0\). Orthogonal invariance gives the explicit uniform-sphere moments
\[
\mathbb E\prod_{i\in S}U_i^2
=\frac{\Gamma(d/2)}{2^q\Gamma(d/2+q)},\qquad
\mathbb E\prod_{i\in J}|U_i|
=\frac{\Gamma(d/2)}{\pi^q\Gamma(d/2+q)}.
\]
They follow from the Dirichlet law of squared uniform-sphere coordinates (or independent normal coordinates divided by their Euclidean norm). Set \(e_S=m_S/\sigma_q\). For the complementary pair \(S,T=J\setminus S\),
\[
\langle e_S,Fe_T\rangle
=\frac{\mathbb E[R^{2q}]\,\mathbb E\prod_{i\in J}|U_i|}{\sigma_q^2}
=\left(\frac2\pi\right)^q=c_q.
\]
The diagonal compressed sign entries are zero by parity; there are no other nonzero entries. Each pair therefore contributes the block \(\begin{pmatrix}0&c_q\\c_q&0\end{pmatrix}\), with eigenvectors \((e_S+e_T)/\sqrt2\) and \((e_S-e_T)/\sqrt2\). Since \(\mathbf1_{\Omega_q}=(1+F)/2\) almost everywhere, translating the sign spectrum by \(1/2\) and scaling by \(1/2\) proves the full assertion. Moreover \(0<c_q<1\), so these are exactly the three possible distinct levels whenever the middle multiplicity is nonzero.

**(3) Pure harmonics.** Every squarefree \(m_S\) is homogeneous and harmonic, since its Laplacian vanishes identically. Thus the entire noncentral block occurs inside \(\mathcal H_q\). All remaining pure harmonics are orthogonal to these blocks and remain at half energy, yielding the stated pure-harmonic version. The proof applies for every integer \(q\ge1\) and \(d\ge2q\), without asymptotics or numerical extrapolation.

## Verification

The accompanying `check_checkerboard.py` constructs the *full monomial moment Gram matrix* on the sphere rather than assuming the claimed parity-block basis. The monomials form a quotient basis under \(\sum_i x_i^2=1\). Its generalized eigenvalues agree with the predicted centered spectrum for \((q,d)=(1,2),(1,4),(2,4),(2,5),(3,6),(3,7)\), with largest absolute discrepancy \(2.3\times10^{-16}\) in double precision. Run using `python check_checkerboard.py` with NumPy and SciPy installed. These tests are finite checks of normalization and the full small-dimensional spectrum; the all-parameter theorem is proved analytically above.

For \(q=2\), the exact noncentral concentration eigenvalues are \(1/2\pm2/\pi^2\), each of multiplicity three, in every \(d\ge4\). For \(q=3\), they are \(1/2\pm4/\pi^3\), each of multiplicity ten, in every \(d\ge6\). At bandwidth below \(q\), the same checkerboard geometry is spectrally invisible to every polynomial in the band.

## Relationship to prior work

The sphere concentration problem and its matrix formulation are classical. Michel–Plattner–Seibert (first public arXiv version 26 March 2021) develops unified scalar/vector/tensor Slepian constructions, with emphasis on spherical caps. Bates–Khalid–Kennedy develops computational approaches for arbitrary spherical regions. Their inspected constructions motivate the exact question here but do not state the compressed coordinate-sign character blocks or the dimension- and radial-law-independent eigenvalue shifts.

The elementary reflection-character selection argument differs from existing hemisphere parity-pairing and Boolean-cube sampling results: the latter do not by themselves compute the precise first responsive band and its \((2/\pi)^q\) shift for continuous rotationally invariant measures. This is a comparison of inspected statements, not a claim that all historical literature has been exhaustively searched.

## Limitations

The result concerns polynomial bands only through the *first* responsive level \(q\). At higher bands the parity-character blocks grow and no formula is asserted. It does not concern arbitrary anisotropic measures, tilted checkerboard boundaries, discrete cube-vertex sampling or conditional-measure normalization. Independent mathematical validation and exhaustive historical-priority certification have not been performed. A previously unindexed equivalent statement is possible.

## References

- V. Michel, A. Plattner, K. Seibert, “A Unified Approach to Scalar, Vector, and Tensor Slepian Functions on the Sphere and Their Construction by a Commuting Operator,” arXiv:2103.14650v1, first public 2021-03-26. https://arxiv.org/abs/2103.14650
- A. P. Bates, Z. Khalid, R. A. Kennedy, “Efficient Computation of Slepian Functions for Arbitrary Regions on the Sphere,” arXiv:1608.05479, 2016. https://arxiv.org/abs/1608.05479
- F. J. Simons, F. A. Dahlen, M. A. Wieczorek, “Spatiospectral Concentration on a Sphere,” SIAM Review 48 (2006), 504–536. https://arxiv.org/abs/math/0408424
