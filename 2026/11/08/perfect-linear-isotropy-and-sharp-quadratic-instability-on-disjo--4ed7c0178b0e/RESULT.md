# Perfect linear isotropy and sharp quadratic instability on disjoint coordinate caps

## Finding
For every integer \(d\ge3\) and every \(2^{-1/2}\le t<1\), let \(E_t=\{x\in S^{d-1}:\max_{1\le j\le d}|x_j|\ge t\}\). Let \(C_{k,t}\) be the spatial concentration operator on the *pure*, complex-valued degree-\(k\) spherical harmonics, using probability-normalized spherical measure: \(\langle C_{k,t}f,g\rangle=\int_{E_t}f\bar g\,d\sigma\). Define
\[
 c_d=\frac{\Gamma(d/2)}{\sqrt\pi\,\Gamma((d-1)/2)},\quad
 q_d(t)=c_d\int_t^1(1-u^2)^{(d-3)/2}\,du,\quad
 \mu_d(t)=2d\,q_d(t),
\]
and
\[
 B_d(t)=c_d\,t(1-t^2)^{(d-1)/2},\qquad T_d(t)=(d+4)t^2-3.
\]
The degree-one operator is exactly \(C_{1,t}=\mu_d(t)I\). The **complete** degree-two concentration spectrum is
\[
 \boxed{\lambda_D=\mu_d(t)+\frac{d^2}{d^2-1}B_d(t)T_d(t)}
 \quad\text{(multiplicity \(d-1\))},
\]
\[
 \boxed{\lambda_O=\mu_d(t)-\frac{2d}{d^2-1}B_d(t)T_d(t)}
 \quad\text{(multiplicity \(d(d-1)/2\))}.
\]
The \(\lambda_D\)-eigenspace consists precisely of trace-free diagonal quadratics \(\sum_j a_jx_j^2\) with \(\sum_j a_j=0\); the \(\lambda_O\)-eigenspace consists of off-diagonal quadratics \(\sum_{i<j}b_{ij}x_ix_j\). Both eigenvalues are in \((0,1)\), and \(\lambda_D>\lambda_O\) throughout the stated range.

Writing \(\delta=1-t^2\), the sharp spectral and restriction conditioning laws are
\[
 \boxed{\frac{\lambda_D}{\lambda_O}\sim\frac{d+1}{4\delta}},
 \qquad
 \boxed{\kappa_2(R_{2,t})\sim\frac{\sqrt{d+1}}{2\sqrt\delta}},
 \qquad\delta\downarrow0,
\]
where \(R_{2,t}\) is restriction from \(\mathcal H_2(S^{d-1})\) to \(L^2(E_t)\). In contrast the corresponding degree-one restriction always has relative condition number exactly one. Thus exact second-moment isotropy of a sampling region need not control higher-harmonic conditioning; this family is a sharp quantitative example.

## Assumptions and scope
The sphere has dimension \(d-1\) and carries probability-normalized rotation-invariant surface measure. The underlying harmonic Hilbert spaces use the whole-sphere \(L^2\) inner product and consist of restrictions of homogeneous harmonic polynomials of degree exactly one or exactly two; the theorem does not concern a cumulative degree band. The cap threshold \(t\) is at least \(1/\sqrt2\), so the \(2d\) caps about the signed coordinate axes are pairwise disjoint up to sets of surface measure zero. No equality-case assumption about coefficients is made, and all scalar coefficients may be complex. Conditioning means the ratio of the largest to smallest nonzero singular values (or, for the positive concentration operator, the ratio of its largest to smallest eigenvalues).

## Proof
**1. Geometric separation, first moments, and linear modes.** If two different coordinates simultaneously satisfy \(|x_i|\ge t\) and \(|x_j|\ge t\), then \(1\ge x_i^2+x_j^2\ge2t^2\ge1\). Equality can occur only on a lower-dimensional subset. Thus the indicator of \(E_t\) is, almost everywhere, the sum of indicators of the \(2d\) signed coordinate caps. The first coordinate \(U=x_1\) of a uniform point on the sphere has density \(c_d(1-u^2)^{(d-3)/2}\). Hence \(\sigma(E_t)=2dq_d(t)=\mu_d(t)\). Sign flips make the mixed moments \(\mathbb E[1_{E_t}x_ix_j]\) vanish for \(i\ne j\). Coordinate permutations and \(\sum_jx_j^2=1\) give \(\mathbb E[1_{E_t}x_i^2]=\mu_d(t)/d\). Since \(\{\sqrt d\,x_i\}_{i=1}^d\) is an orthonormal basis for \(\mathcal H_1\), the first claim follows.

**2. Complete quadratic decomposition.** A homogeneous quadratic is harmonic exactly when its symmetric coefficient matrix has trace zero. Decompose that matrix uniquely into a trace-free diagonal matrix and a symmetric zero-diagonal matrix. Accordingly,
\[
 \mathcal H_2=D\oplus O,\quad
 D=\operatorname{span}\{x_i^2-x_j^2\},\quad
 O=\operatorname{span}\{x_ix_j:i<j\}.
\]
The dimensions are \(d-1\) and \(d(d-1)/2\). Sign-flip invariance of \(E_t\) makes distinct off-diagonal characters orthogonal and makes \(D\) orthogonal to \(O\), under both whole-sphere and restricted inner products. Permutation invariance makes the restricted quadratic form on the trace-free diagonal subspace scalar (a matrix having a common diagonal entry and a common off-diagonal entry acts as a scalar on vectors of coordinate sum zero). Thus there are precisely two eigenvalues, including possible accidental coincidence; the explicit gap below excludes coincidence.

**3. Reduction to fourth moments.** Set \(a=\mathbb E[1_{E_t}x_1^4]\) and \(b=\mathbb E[1_{E_t}x_1^2x_2^2]\), for \(1\ne2\). Exact whole-sphere fourth moments are \(\mathbb E[x_1^4]=3/[d(d+2)]\) and \(\mathbb E[x_1^2x_2^2]=1/[d(d+2)]\). The Rayleigh quotients of \(x_1x_2\) and \(x_1^2-x_2^2\) are therefore
\[
 \lambda_O=d(d+2)b,\qquad \lambda_D=\frac{d(d+2)}2(a-b).
\]
The disjoint-cap representation gives one-dimensional formulas. Write \(I_j=\int_t^1u^jc_d(1-u^2)^{(d-3)/2}\,du\). Conditional on \(x_k=u\), the remaining coordinates are uniformly distributed on a sphere of radius \(\sqrt{1-u^2}\) in \(d-1\) dimensions; their second, fourth and mixed fourth moments are respectively \((1-u^2)/(d-1)\), \(3(1-u^2)^2/[(d-1)(d+1)]\), and \((1-u^2)^2/[(d-1)(d+1)]\). Summing the \(2d\) cap contributions gives
\[
 a=2\left[I_4+\frac3{d+1}(I_0-2I_2+I_4)\right],
\]
\[
 b=2\left[\frac2{d-1}(I_2-I_4)+\frac{d-2}{(d-1)(d+1)}(I_0-2I_2+I_4)\right].
\]
Integration by parts gives the exact recurrences
\[
 I_0=q_d(t),\quad
 I_2=\frac{I_0+B_d(t)}d,\quad
 I_4=\frac{3I_2+t^2B_d(t)}{d+2}.
\]
Substitution (without any asymptotic approximation) yields the two displayed eigenvalues. An equivalent direct certificate for the gap is the elementary derivative identity
\[
 \frac{d}{du}\!\left[u(1-u^2)^{(d-1)/2}\big((d+4)u^2-3\big)\right]
 =-(1-u^2)^{(d-3)/2}
 \left[(d+2)(d+4)u^4-6(d+2)u^2+3\right].
\]
In particular,
\[
 \boxed{\lambda_D-\lambda_O=\frac{d(d+2)}{d^2-1}B_d(t)T_d(t)>0},
\]
because \(t^2\ge1/2\) and \(T_d(t)\ge(d-2)/2>0\). Both eigenvalues lie strictly between zero and one: for every nonzero harmonic polynomial, its squared modulus has positive integral on each of the two nonempty open sets \(E_t\) and \(S^{d-1}\setminus E_t\), since a nonzero polynomial cannot vanish on a nonempty open portion of the sphere.

**4. Sharp narrow-cap asymptotics.** Put \(\alpha=(d-1)/2\) and \(\delta=1-t^2\). The change of variables \(v=1-u^2\) gives
\[
 q_d(t)=\frac{c_d}{2}\int_0^\delta v^{\alpha-1}(1-v)^{-1/2}\,dv
 =\frac{c_d}{d-1}\delta^\alpha\left[1+\frac{d-1}{2(d+1)}\delta+O_d(\delta^2)\right].
\]
Also \(B_d(t)=c_d\delta^\alpha(1-\delta/2+O(\delta^2))\) and \(T_d(t)=d+1-(d+4)\delta\). The leading terms cancel in the formula for \(\lambda_O\) but not in that for \(\lambda_D\). Keeping the next term gives
\[
 \lambda_D=\frac{d(d+2)c_d}{d-1}\delta^\alpha\big[1+O_d(\delta)\big],\qquad
 \lambda_O=\frac{4d(d+2)c_d}{(d-1)(d+1)}\delta^{\alpha+1}\big[1+O_d(\delta)\big].
\]
Division proves the exact spectral coefficient \((d+1)/4\); the restriction singular values are square roots of the positive concentration eigenvalues, proving the other coefficient. All error terms are for fixed integer \(d\) as \(t\uparrow1\), not uniform in growing dimension.

## Verification
The standalone `check_axis_caps.py` proves algebraic identities symbolically, independently constructs quadratic restriction Gram matrices by integrating conditional coordinate moments, compares generalized eigenvalues across five ambient dimensions and five thresholds, checks the asymptotic constant at three small cap scales using high-precision incomplete-beta integrals, and additionally tests unrestricted spherical Monte Carlo integration in dimension three. Run with Python and the dependencies in `requirements.txt` by invoking `python check_axis_caps.py`; the observed result for this package is `AXIS_CAPS_SPECTRUM_CHECKS_PASS 490`. These finite computations are corroborative; the proof above supplies the all-parameter result.

## Relationship to prior work
The scalar spherical Slepian concentration framework is classical, and its finite concentration matrix for a general region is not new [1]. Michel, Plattner, and Seibert [2] study spherical Slepian constructions and commuting operators for polar caps, principally in the sphere of three-dimensional space. Snowball and Olver [3] construct orthogonal polynomial techniques for single spherical cap PDE domains. Zandieh, Han, and Avron [4] give general spherical harmonic reconstruction guarantees from uniformly distributed sample locations. The present theorem does **not** claim those general frameworks, cap constructions, or recovery guarantees. It resolves a different, rigid continuous observation geometry: the union of all disjoint signed coordinate caps, in arbitrary ambient dimension, revealing a sharp difference between linear and quadratic harmonic conditioning. A general Slepian matrix formula permits setting up this eigenproblem but does not alone state the explicit two-level spectrum, positive gap, or precise narrow-cap coefficient. Historical priority for these explicit specialized formulas remains subject to further checking.

## Limitations
The disjoint-cap threshold \(t\ge1/\sqrt2\) is essential to the simple moment sum; the overlap regime is not classified here. Only the individual harmonic degrees one and two, and fixed ambient dimensions \(d\ge3\), are covered. Perfect **relative** conditioning of the linear restriction does not imply a fixed absolute singular-value lower bound as cap area shrinks. The sharp quadratic instability describes continuous noiseless restriction, not a finite randomized sampling matrix or a minimax rate for a noise model. The numerical checker is not a formal proof or independent audit.

## References
[1] F. J. Simons, F. A. Dahlen, M. A. Wieczorek, *Spatiospectral concentration on a sphere*, SIAM Review 48 (2006), 504–536, arXiv:math/0408424, https://arxiv.org/abs/math/0408424.

[2] V. Michel, A. Plattner, K. Seibert, *A unified approach to scalar, vector, and tensor Slepian functions on the sphere and their construction by a commuting operator*, first public arXiv submission 2021-03-26, arXiv:2103.14650, https://arxiv.org/abs/2103.14650.

[3] B. Snowball, S. Olver, *Sparse spectral methods for partial differential equations on spherical caps*, first public arXiv submission 2020-12-21, arXiv:2012.11493, https://arxiv.org/html/2012.11493v1.

[4] A. Zandieh, I. Han, H. Avron, *Near optimal reconstruction of spherical harmonic expansions*, first public arXiv submission 2022-02-25, arXiv:2202.12995, https://arxiv.org/html/2202.12995v1.
