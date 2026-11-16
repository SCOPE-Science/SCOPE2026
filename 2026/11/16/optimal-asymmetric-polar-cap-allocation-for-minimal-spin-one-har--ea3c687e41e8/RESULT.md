# Optimal asymmetric polar-cap allocation for minimal spin-one harmonic observability

## Finding
Fix a total observation-area fraction \(h\in(0,1)\) of the unit sphere. Among unions of two nonoverlapping caps centered at the north and south poles, with respective full-sphere area fractions \(p,q\geq0\) and \(p+q=h\), let \(\mu(p,q)\) be the least fraction of squared \(L^2\)-energy captured from a unit vector in the complex three-dimensional spin-weight-one harmonic space of exact degree \(\ell=1\).

The **only** maximizers of \(\mu\) are the two asymmetric allocations \((p,q)=(p_*,q_*)\) and \((q_*,p_*)\), where
\[
 d_* = \frac{\sqrt{1+6h-3h^2}-1}{3},\qquad p_* =\frac{h+d_*}{2},\qquad q_* =\frac{h-d_*}{2}.
\]
The sharp worst-mode concentration is
\[
 \max_{p+q=h}\mu(p,q)
 = \frac{h^2(3-h)+3(1-h)d_*^2}{2}.
\]
At each optimizer the least concentration eigenvalue has multiplicity two. Equal-area allocation is strictly suboptimal at every \(0<h<1\), with value \(h^2(3-h)/2\). In the small-area regime, \(q_*=h^2+O(h^3)\), \(p_*=h-h^2+O(h^3)\), and the sharp optimal/equal-area worst-mode ratio tends to \(2\).

## Assumptions and scope
Use the standard complex spin-weight \(+1\) spherical harmonics \({}_1Y_{1m}\), \(m=-1,0,+1\), orthonormal in \(L^2(S^2,d\Omega)\). The space contains exactly this degree, not a degree band and not the direct sum of both spin chiralities. Each cap is defined by a polar angle: the north cap has \(0\leq\theta\leq\arccos(1-2p)\), and the south cap has \(\pi-\arccos(1-2q)\leq\theta\leq\pi\). Since \(h<1\), the caps are disjoint. Observation is squared-energy restriction to their union with no extra cap weighting. The optimization concerns the *least* of the three restriction eigenvalues, equivalently the greatest guaranteed retained energy over all unit vectors in the harmonic space. All inequalities and uniqueness assertions hold for every real \(h\in(0,1)\).

## Proof
Put \(u=(1-\cos\theta)/2\). The Wigner small-\(d\) formulas at \(\ell=1\), after azimuthal integration, give the normalized latitudinal energy densities for the three orders \(m=-1,0,+1\):
\[
 \rho_{-1}(u)=3(1-u)^2,\qquad \rho_0(u)=6u(1-u),\qquad \rho_{+1}(u)=3u^2,\qquad 0\leq u\leq1.
\]
In each case the integral over \([0,1]\) is \(1\). Orthogonality of the azimuthal factors makes the cap restriction operator diagonal in these orders. Integrating the densities over \([0,p]\cup[1-q,1]\) gives exactly
\[
 \begin{aligned}
 \lambda_{-1}&=3p-3p^2+p^3+q^3,\\
 \lambda_0&=3(p^2+q^2)-2(p^3+q^3),\\
 \lambda_{+1}&=p^3+3q-3q^2+q^3.
 \end{aligned}
\]
Thus \(\mu(p,q)=\min\{\lambda_{-1},\lambda_0,\lambda_{+1}\}\). Reflection through the equator interchanges \(p,q\) and \(m,-m\), so it is enough to optimize over \(p\geq q\), writing \(d=p-q\in[0,h]\). Direct subtraction yields
\[
 \lambda_{-1}-\lambda_{+1}=3d(1-h)\geq0.
\]
Consequently the smaller of the two extreme-order eigenvalues is \(\lambda_{+1}\). Substitution of \(p=(h+d)/2\) and \(q=(h-d)/2\) gives
\[
 \lambda_0=\frac{h^2(3-h)}2+\frac{3(1-h)}2d^2,
 \qquad
 \frac{d\lambda_0}{dd}=3(1-h)d,
 \qquad
 \frac{d\lambda_{+1}}{dd}=-\frac32(1-h)(1+d).
\]
The central eigenvalue increases strictly for \(d>0\), and the extreme eigenvalue decreases strictly throughout \([0,h]\). Their difference factors as
\[
 \lambda_0-\lambda_{+1}=\frac34(1-h)\bigl(3d^2+2d+h^2-2h\bigr).
\]
At \(d=0\) this difference is negative because \(h^2-2h<0\). At \(d=h\) it is positive, equal to \(3h^2(1-h)\). It has exactly one zero in \((0,h)\), namely \(d_*\) displayed above. Hence the pointwise minimum of the increasing \(\lambda_0\) and decreasing \(\lambda_{+1}\) is strictly increasing up to \(d_*\) and strictly decreasing afterwards. This proves global optimality and uniqueness for \(d\geq0\), and symmetry gives precisely two ordered allocations. At the maximizers, \(\lambda_0=\lambda_{+1}<\lambda_{-1}\), proving the two-dimensional least-observed eigenspace.

The equal-cap value follows by setting \(d=0\). Its strict deficiency is \(3(1-h)d_*^2/2>0\). Finally, the Taylor expansion of the positive root gives \(d_*=h-2h^2+O(h^3)\), so \(q_*=h^2+O(h^3)\), while the optimized retained fraction is \(3h^2+O(h^3)\) versus \(3h^2/2+O(h^3)\) for the symmetric design. This proves the factor-two asymptotic.

## Verification
The accompanying standalone `check.py` reproduces the exact symbolic factorizations and derivatives in SymPy, verifies the root identity and asymptotic factor, compares all three polynomial eigenvalues with independently integrated spin-one Wigner angular densities for 150 deterministic pseudorandom admissible designs, and checks optimality and mode multiplicities at 199 area fractions. A separate discretized comparison on 20,099 feasible cap splits supplements, but does not replace, the analytical global proof. Run `python check.py` with Python 3, SymPy and SciPy. All stated tests were executed and passed. The proof does not rely on finite numerical experiments.

## Relationship to prior work
The spin-weighted spherical-harmonic concentration operator and its spherical-cap kernel are established in the work of Michel, Plattner, and Seibert (2021), especially their Sections 3.1–3.3; the Wigner/spin-harmonic framework and cap construction are already available in Seibert's 2018 thesis. Plattner and Simons (2013) discuss vector spherical Slepian concentration in arbitrary spatial regions. The present statement instead optimizes the **least spectral concentration** over unequal antipodal cap *areas* at fixed total area, giving a unique symmetry-breaking pair and sharp quantitative advantage. None of the portions of those primary works inspected gave this allocation theorem. The general operator definition by itself does not supply the global two-parameter extrema.

## Limitations
This result concerns only one spin chirality at the minimal harmonic degree \(\ell=1\), axis-aligned antipodal caps, and squared-energy maximin design. No assertion is made about optimality among arbitrary measurable regions, unconstrained cap centers, mixtures of spin weights or higher bandlimits. It does not establish historical priority against inaccessible or unindexed sources; the exact optimization may be rediscovered independently. No external independent mathematical audit has been performed.

## References
- V. Michel, A. Plattner and K. Seibert, *A Unified Approach to Scalar, Vector, and Tensor Slepian Functions on the Sphere and Their Construction by a Commuting Operator*, arXiv:2103.14650v1, first posted 26 March 2021; Sections 2.3 and 3.1–3.3. https://arxiv.org/abs/2103.14650
- K. Seibert, *Spin-Weighted Spherical Harmonics and Their Application for the Construction of Tensor Slepian Functions on the Spherical Cap*, University of Siegen, 2018; Chapters 3 and 8. https://noah.nrw/ubsihs/download/pdf/3558688
- A. Plattner and F. J. Simons, *Spatiospectral Concentration of Vector Fields on a Sphere*, arXiv:1306.3201, first posted 13 June 2013. https://arxiv.org/abs/1306.3201
