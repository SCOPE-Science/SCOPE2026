# Exact all-size stability of alternately jittered periodic cubic-spline collocation

## Finding
For every even integer \(N=2m\ge4\), sampling the integer-knot periodic cardinal cubic B-spline basis at alternating sites \(t_{2k}=2k+\delta\) and \(t_{2k+1}=2k+1-\delta\), with \(0\le\delta\le1/2\), has a complete two-band singular-value spectrum. With \(a,b,c,e\) defined below, the singular values, including multiplicity, are
\[
\sigma_{r,\pm}=\sqrt{a^2+e^2+2ae\cos(2\pi r/m)}\ \pm\sqrt{b^2+c^2+2bc\cos(2\pi r/m)},\quad r=0,\ldots,m-1.
\]
Both signs give nonnegative values on this parameter range. For every \(0\le\delta<1/2\), the largest singular value is exactly \(1\) and the smallest is exactly
\[
\gamma(\delta)=\frac{(1-2\delta)(1+2\delta-2\delta^2)}3=\frac{1-6\delta^2+4\delta^3}{3}>0.
\]
Both extremal singular values are simple, supported on the spatially constant and alternating coefficient vectors, respectively. Consequently the sharp Euclidean collocation condition number is \(1/\gamma(\delta)\), independently of \(N\). It grows strictly from \(3\) at \(\delta=0\) and satisfies \(\kappa_2\sim(1/2-\delta)^{-1}\) as \(\delta\uparrow1/2\). At \(\delta=1/2\), all lower-band singular values vanish and the collocation matrix has rank precisely \(N/2\).

## Assumptions and scope
Define the compactly supported centered cardinal cubic B-spline
\[
\beta(x)=\begin{cases}
(4-6|x|^2+3|x|^3)/6,&0\le|x|\le1,\\
(2-|x|)^3/6,&1<|x|\le2,\\
0,&|x|>2.
\end{cases}
\]
For integers \(N=2m\ge4\), set \(B_j(x)=\sum_{h\in\mathbb Z}\beta(x-j+hN)\), for \(0\le j<N\). The sum is finite at each point. Form the square collocation operator \(A_{ij}=B_j(t_i)\) with periodic indices, \(0\le i,j<N\), where \(t_{2k}=2k+\delta\), \(t_{2k+1}=2k+1-\delta\), for \(0\le k<m\). All singular values and condition numbers refer to the unweighted Euclidean norms of coefficient and sample vectors. Only real \(0\le\delta\le1/2\) and even \(N\) are asserted. Put
\[
\begin{aligned}
a&=(4-6\delta^2+3\delta^3)/6, & e&=\delta^3/6,\\
b&=(4-6(1-\delta)^2+3(1-\delta)^3)/6, &c&=(1-\delta)^3/6.
\end{aligned}
\]
These are nonnegative and obey \(a+b+c+e=1\).

## Proof
**Step 1 (exact sampled stencil).** For any coefficient sequence \(u_j\), write \(E_k=u_{2k}\), \(O_k=u_{2k+1}\), with the cell index read cyclically modulo \(m\). Evaluation of the four nonzero translates of the centered cubic B-spline gives
\[
 (Au)_{2k}=aE_k+eE_{k+1}+bO_k+cO_{k-1},\qquad
 (Au)_{2k+1}=aO_k+eO_{k-1}+bE_k+cE_{k+1}.
\]
The formulas remain valid at \(N=4\) because the periodization adds coincident translates exactly as the cyclic indexing does.

**Step 2 (complete spectrum).** Apply the unitary discrete Fourier transform in the \(m\)-cell variable. On the frequency \(z_r=\exp(2\pi i r/m)\), the resulting \(2\times2\) matrix is
\[
 M_r=\begin{pmatrix}a+ez_r&b+c z_r^{-1}\\b+cz_r&a+ez_r^{-1}\end{pmatrix}.
\]
For any complex \(u,v\), the singular values of \(\begin{psmallmatrix}u&v\\\bar v&\bar u\end{psmallmatrix}\) are \(|u|+|v|\) and \(\bigl||u|-|v|\bigr|\); this follows by direct computation of its squared singular values \((|u|\pm|v|)^2\). Thus the claimed formulas follow once \(|u|\ge|v|\) is proved. This step includes all multiplicities and uses no large-dimension approximation.

**Step 3 (strict spectral ordering and endpoints).** Put \(t=\cos(2\pi r/m)\), \(U(t)=\sqrt{a^2+e^2+2ae t}\), \(V(t)=\sqrt{b^2+c^2+2bc t}\). Direct polynomial factorization yields
\[
 a+e-b-c=\gamma(\delta),\quad
 bc-ae=\frac{(1-2\delta)(3\delta^4-6\delta^3+\delta^2+2\delta+1)}{36}.
\]
The second factor is positive for \(0\le\delta\le1/2\): since \(6\delta^3\le3\delta^2\), it is at least \(1+2\delta-2\delta^2+3\delta^4>0\). For \(\delta<1/2\), both \(\gamma>0\) and \(bc>ae\). Hence \(U(t)^2-V(t)^2\) is decreasing in \(t\in[-1,1]\), with a strictly positive minimum at \(t=1\), where it equals \((a+e)^2-(b+c)^2\). Thus \(U(t)>V(t)\) throughout this interval. Moreover \(U(t)\le a+e\), \(V(t)\le b+c\), so the upper singular value is at most \(a+b+c+e=1\), with equality only at \(t=1\). For the lower singular value, \(U-V\) is strictly decreasing as \(t\) grows: where derivatives are defined, \(U'=ae/U<bc/V=V'\) (the cases with \(V=0\) follow by continuity). It attains its unique minimum \((a+e)-(b+c)=\gamma\) at \(t=1\). On the discrete set \(t=\cos(2\pi r/m)\), the value \(t=1\) occurs only at \(r=0\). The two singular vectors there are the constant and checkerboard vectors, respectively, and both extremes are simple.

**Step 4 (monotonicity and collision).** The derivative \(\gamma'(\delta)=4\delta(\delta-1)\) is negative for \(0<\delta<1/2\). At \(\delta=1/2\), \(a=b=23/48\) and \(c=e=1/48\), so \(U(t)=V(t)\). Each frequency block then has one zero singular value and one strictly positive singular value, because \(a>e\) makes \(U(t)\ge a-e>0\). Therefore \(\operatorname{rank}A=m\). Finally \(\gamma(1/2-\varepsilon)=\varepsilon+O(\varepsilon^2)\) establishes the sharp divergence constant.

## Verification
The standalone script `check_spectrum.py` directly builds periodized cubic-spline collocation matrices without reusing the proposed Fourier block formula to generate matrix entries. For every even \(N\in\{4,6,\ldots,64\}\) and each of nine displacements \(\delta\in\{0,0.03125,0.1,0.2,0.24,0.3,0.4,0.49,0.5\}\), it compares all numerically computed singular values with the block formulas, checks the sharp maximum, minimum when noncolliding, and rank at the collision. It completed 1085 direct assertions. Execute `python check_spectrum.py` with NumPy installed. These finite checks support but do not establish the all-size proof.

## Relationship to prior work
Yu and Townsend (2022, arXiv:2202.04722) investigate stability of perturbed trigonometric interpolation and quadrature at uneven nodes. Their trigonometric polynomial sampling space differs from the cubic B-spline coefficient space here. Fageot, Aziznejad, Unser and Uhlmann (2020) analyze Hermite-spline support and approximation, including cubic-spline background, but do not provide this alternating-point cyclic collocation spectrum in the inspected text. Novaković, Singer and Singer (2010), *Estimates for the spectral condition number of cardinal B-spline collocation matrices*, https://hrcak.srce.hr/en/61876. Its accessible abstract concerns cardinal collocation at knot averages and numerical/estimated uniform-mesh conditioning; the linked primary PDF could not be fetched. It is a plausible older source, but the abstract does not claim the present two-periodic point-jitter singular spectrum. Classical cardinal-spline interpolation has much broader background; a logically equivalent formulation within older spline filter or Floquet theory remains a historical-priority risk. Published results about alternating-knot **linear** spline projections and cubic-spline **Gabor Zak transforms** concern different operators and do not directly state this coefficient-to-point-sample Euclidean spectrum.

## Limitations
The theorem is restricted to an even number of coefficients, two-periodic alternating jitter, and the centered cardinal cubic B-spline. It is a coefficient-to-sample \(\ell^2\) condition-number theorem, not a statement about optimal \(L^\infty\) interpolation constants, arbitrary independently perturbed nodes, all spline orders, or Gabor frame bounds. No claim of absolute historical priority or independent audit is made. The analytic proof is valid at every stated \(N\) regardless of finite numerical sample size.

## References
- A. Yu and A. Townsend, *On the stability of unevenly spaced samples for interpolation and quadrature*, arXiv:2202.04722 (first public version 2022-02-09), https://arxiv.org/abs/2202.04722.
- J. Fageot, S. Aziznejad, M. Unser, and V. Uhlmann, *Support and approximation properties of Hermite splines*, 2020 open-access article, https://pmc.ncbi.nlm.nih.gov/articles/PMC6919321/.
- V. Novaković, S. Singer and S. Singer, *Estimates for the spectral condition number of cardinal B-spline collocation matrices*, Mathematical Communications 15 (2010), 503–519, https://hrcak.srce.hr/en/61876 (abstract read; primary PDF inaccessible).
- I. J. Schoenberg, *Cardinal Spline Interpolation*, SIAM, 1973 (background literature; not exhaustively inspected for equivalent statements).
