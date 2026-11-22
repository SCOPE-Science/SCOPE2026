# A dimension-free optimizer switch for tangential-gradient concentration of spherical quadrupoles

## Finding

Let \(d\ge3\), let \(\mathcal H_2(S^{d-1})\) be the complex exact-degree-two spherical-harmonic space, and set
\[
\Omega_t=\{x\in S^{d-1}:|x_d|\ge t\},\qquad 0<t<1.
\]
For nonzero \(f\in\mathcal H_2(S^{d-1})\), consider the *tangential-gradient energy fraction*
\[
\mathcal R_t(f)=\frac{\int_{\Omega_t}|\nabla_S f|^2\,d\sigma}{\int_{S^{d-1}}|\nabla_S f|^2\,d\sigma},
\]
where \(\sigma\) is normalized surface probability measure. The Hermitian concentration operator for this quotient has exactly three eigenvalue branches, including their possible coincidences:

| Sector | Dimension | Eigenvalue |
|---|---:|---|
| Zonal \(Z\) | \(1\) | \(\Lambda_Z(s)\) |
| Mixed \(M\) | \(d-1\) | \(\Lambda_M(s)\) |
| Transverse trace-free \(T\) | \((d-2)(d+1)/2\) | \(\Lambda_T(s)\) |

Here \(s=t^2\), \(a=1/2\), \(b=(d-1)/2\), and for \(j\in\{Z,M,T\}\),
\[
\Lambda_j(s)=\frac{1}{B(a,b)m_j}\int_s^1 u^{a-1}(1-u)^{b-1}q_j(u)\,du,
\]
where
\[
\begin{aligned}
q_Z(u)&=u(1-u),&m_Z&=\frac{d-1}{d(d+2)},\\
q_M(u)&=1+(d-6)u+4u^2,&m_M&=\frac{2(d-1)}{d+2},\\
q_T(u)&=(1-u)(d-1+2u),&m_T&=\frac{(d-1)(d+1)}{d+2}.
\end{aligned}
\]
All branches are strictly between zero and one. With
\[
W_d(s)=\frac{s^{1/2}(1-s)^{(d-1)/2}}{B(1/2,(d-1)/2)},
\]
the exact spectral gaps are
\[
\begin{aligned}
\Lambda_Z-\Lambda_M&=\frac{d+2}{d-1}W_d(s)(1-2s),\\
\Lambda_Z-\Lambda_T&=\frac{2(d+2)}{d+1}W_d(s)(1-s),\\
\Lambda_M-\Lambda_T&=\frac{d+2}{(d-1)(d+1)}W_d(s)(d-3+4s).
\end{aligned}
\]
Consequently the transverse sector \(T\) is *always strictly least concentrated*. The uniquely optimal branch is the zonal line for \(0<t<1/\sqrt2\) and the \((d-1)\)-dimensional mixed sector for \(1/\sqrt2<t<1\). Exactly at \(t=1/\sqrt2\), the maximum has multiplicity \(d\). Thus the switching aperture is independent of ambient dimension. The sharp *squared observation condition number* is
\[
\kappa_d(t)=\frac{\max\{\Lambda_Z(t^2),\Lambda_M(t^2)\}}{\Lambda_T(t^2)},
\qquad
\kappa_d(t)\sim\frac{d+1}{2(1-t^2)}\quad(t\uparrow1).
\]

## Assumptions and scope

The result concerns the complete complexification of the real harmonic space of homogeneous trace-free quadratic forms, not the scalar value concentration operator. There is no spectral truncation involving other harmonic degrees. The two opposite caps use the same polar axis, and the regional measurements are the full intrinsic tangent gradients with their Euclidean tangent-vector norm. Every assertion holds for each integer \(d\ge3\) and each real \(0<t<1\). At \(t=0\) all eigenvalues are one; at \(t=1\) all are zero, and a condition number is not defined. No finite-point sampling or noise model is claimed.

In coordinates \(y=(x_1,\ldots,x_{d-1})\) and \(z=x_d\), the three mutually inequivalent irreducible \(O(d-1)\)-types are
\[
Z=\operatorname{span}\{z^2-1/d\},\quad
M=\{z\,v\cdot y:v\in\mathbb C^{d-1}\},\quad
T=\{y^{\mathsf T}By:B^{\mathsf T}=B,\ \operatorname{tr}B=0\}.
\]
The last trace is over the transverse \((d-1)\)-dimensional block. These types exhaust \(\mathcal H_2\) by a dimension count. Their irreducibility and inequivalence also hold for \(d=3\), where transverse and mixed modes have angular frequencies two and one, respectively.

## Proof

**(1) Block decomposition.** Rotations of the first \(d-1\) coordinates preserve \(\Omega_t\), surface measure, the tangent-gradient metric, and the global Dirichlet inner product. The regional self-adjoint concentration form therefore commutes with \(O(d-1)\). Orthogonality of the three irreducible types makes each an eigenspace. The eigenvalues equal the regional/global gradient-energy fractions of any nonzero representative of each type. This argument works over the real space and hence its complexification.

**(2) Conditional quadratic gradient energies.** Write \(u=z^2\). For a homogeneous quadratic \(f(x)=x^{\mathsf T}Ax\), with symmetric matrix \(A\), the sphere gradient is
\[
\nabla_Sf(x)=2\big(Ax-f(x)x\big),\qquad
|\nabla_Sf|^2=4\big(|Ax|^2-|f(x)|^2\big)
\]
for real representatives; polarization gives the Hermitian version. Conditional on \(u\), \(y/\sqrt{1-u}\) is uniform on \(S^{d-2}\). Its second and fourth moments are
\[
\mathbb E(y_i^2\mid u)=\frac{1-u}{d-1},\quad
\mathbb E((y_i^2-y_j^2)^2\mid u)=\frac{4(1-u)^2}{(d-1)(d+1)}.
\]
For representatives \(f_Z=z^2-1/d\), \(f_M=zy_1\), and \(f_T=y_1^2-y_2^2\), a direct calculation yields
\[
\begin{aligned}
\mathbb E(|\nabla_Sf_Z|^2\mid u)&=4q_Z(u),\\
\mathbb E(|\nabla_Sf_M|^2\mid u)&=\frac{q_M(u)}{d-1},\\
\mathbb E(|\nabla_Sf_T|^2\mid u)&=\frac{8q_T(u)}{(d-1)(d+1)}.
\end{aligned}
\]
The distribution of \(u=z^2\) is \(\mathrm{Beta}(a,b)\). Its first two moments are \(\mathbb E u=1/d\) and \(\mathbb E u^2=3/[d(d+2)]\); inserting them into the three polynomials yields the stated \(m_j=\mathbb E q_j(u)\). Common positive prefactors cancel in each regional/global quotient, proving all three integral formulas.

**(3) Exact ordering without numerical root-finding.** For any polynomial \(P(u)=A+Bu\), differentiation gives
\[
\frac{d}{du}\big[u^a(1-u)^bP(u)\big]
=u^{a-1}(1-u)^{b-1}\left(aA+[(a+1)B-(a+b)A]u-(a+b+1)Bu^2\right).
\]
The normalized polynomial differences \(q_i/m_i-q_j/m_j\) match the bracket on the right with \(P(u)\) equal to the negative of the corresponding linear factor in the claimed gap formula. Integrating from \(s\) to one, where the boundary term vanishes, gives exactly the three displayed spectral differences. For \(0<s<1\), \(W_d(s)>0\); the second and third differences are strictly positive because \(d-3+4s>0\) for every \(d\ge3\). The first has the unique interior zero \(s=1/2\), and changes sign there. The claimed eigenspaces and multiplicities follow.

**(4) Polar stability asymptotics.** Put \(\varepsilon=1-s\). The beta density near \(u=1\) is asymptotic to \((1-u)^{b-1}/B(a,b)\). The mixed energy polynomial satisfies \(q_M(1)=d-1\), whereas the transverse energy polynomial obeys \(q_T(u)\sim(d+1)(1-u)\). Consequently
\[
\Lambda_M(s)\sim\frac{d+2}{2bB(a,b)}\varepsilon^b,\qquad
\Lambda_T(s)\sim\frac{d+2}{(d-1)(b+1)B(a,b)}\varepsilon^{b+1}.
\]
The mixed branch is the unique maximal type for all sufficiently small \(\varepsilon>0\), so division gives \(\kappa_d(t)\sim(d+1)/(2\varepsilon)\) for fixed \(d\). All claims now follow. \(\square\)

## Verification

The accompanying standalone `verify.py` reconstructs the three beta moments and each differential gap identity symbolically for an indeterminate dimension parameter, then evaluates 125 normalized beta integrals across dimensions \(3,4,5,7,12\) and five cap thresholds. It independently constructs the five-dimensional quadratic-harmonic gradient Gram operator on \(S^2\) from ambient symmetric matrices and integrates its entries on a Gauss–Legendre/periodic angular grid at five distinct apertures, including the crossing. Its eigenvalues match the analytic three-branch prediction within \(5\times10^{-12}\) in the tested cases. Four separate thin-cap checks confirm the leading condition-number coefficient. Run `python verify.py` with Python, NumPy, SciPy, and SymPy. These numerical tests corroborate but do not replace the parameter-uniform symbolic proof.

## Relationship to prior work

Michel, Plattner, and Seibert (arXiv:2103.14650, first posted March 26, 2021) develop a broad spin-weighted scalar/vector/tensor Slepian construction and commuting operators on the two-sphere. Plattner and Simons (arXiv:1306.3201) give a general vector spherical concentration framework, while Jahn and Bokor (arXiv:1302.5261) reduce the tangential vector-cap eigenproblem to scalar ones on \(S^2\). These works motivate the present derivative-energy operator and supply general background, but the inspected texts do not state the sharp all-dimensional three-branch *gradient-restricted quadratic* spectrum, the universal threshold \(t=1/\sqrt2\), or its asymptotic conditioning coefficient.

The classical scalar-amplitude Slepian quadrupole problem is not equivalent to the present gradient-energy problem: the latter weights each point by a different quadratic form in the harmonic coefficients, and can reverse the ordering of zonal and mixed modes. Generic vector Slepian block matrices do not by themselves specify the evaluated spectral ordering in every dimension. This is an explicit specialization with new sharp comparisons, not a claim of inventing vector Slepian operators.

## Limitations

The theorem is proved only for exact-degree-two harmonic gradients on antipodal, axis-aligned polar caps. It does not classify arbitrary harmonic degrees, asymmetric pairs of caps, Hessian observations, or the stability of discrete point sampling. An explicit formula of similar effect might exist in older specialist literature or be hidden as an unworked consequence of published vector-concentration matrices; priority beyond the inspected sources is not independently certified. The sharp condition-number asymptotic assumes fixed dimension while the cap shrinks. Independent external audit has not been performed.

## References

1. V. Michel, A. Plattner, K. Seibert, *A Unified Approach to Scalar, Vector, and Tensor Slepian Functions on the Sphere and Their Construction by a Commuting Operator*, arXiv:2103.14650v1, March 26, 2021. https://arxiv.org/abs/2103.14650
2. A. Plattner, F. J. Simons, *Spatiospectral concentration of vector fields on a sphere*, arXiv:1306.3201v1, June 13, 2013. https://arxiv.org/abs/1306.3201
3. K. Jahn, N. Bokor, *Revisiting the concentration problem of vector fields within a spherical cap: a commuting differential operator solution*, arXiv:1302.5261v1, February 21, 2013. https://arxiv.org/abs/1302.5261
4. F. J. Simons, F. A. Dahlen, M. A. Wieczorek, *Spatiospectral concentration on a sphere*, arXiv:math/0408424, August 31, 2004. https://arxiv.org/abs/math/0408424
