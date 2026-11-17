# Heat-diffusion reversal of the weakest Fourier shape mode on regular circle samples

## Finding
For each integer \(N\ge4\), the least-stable Fourier shape deformation of the equally weighted regular \(N\)-gon changes as the intrinsic heat scale increases: the first angular mode is uniquely weakest (up to complex conjugacy) at sufficiently fine heat scale, while the highest discrete angular mode is weakest at sufficiently coarse heat scale. All nonrotational curvatures are strictly positive in both regimes. The complete exact Hessian spectrum and its sharp fine-scale exponential prefactor are given below.

## Assumptions and scope
Work on \(\mathbb T=\mathbb R/(2\pi\mathbb Z)\) with normalized Haar measure \(d\theta/(2\pi)\), fixed integer \(N\ge4\), and \(t>0\). The intrinsic heat kernel is
\[
H_{2t}(x)=\sum_{n\in\mathbb Z}e^{-2tn^2}e^{inx}.
\]
For \(N\) equally weighted points with angles \(\theta_j\), define the heat-overlap energy
\[
E_t(\theta)=\frac1{N^2}\sum_{i,j=0}^{N-1}H_{2t}(\theta_i-\theta_j).
\]
The corresponding geometric effective sample size is \(G_t(\theta)=H_{2t}(0)/E_t(\theta)\), as given by the homogeneous-manifold heat-overlap normalization. At the regular configuration \(\theta_j^0=2\pi j/N\), perturb real angles by \(\theta_j^0+\varepsilon u_j\). A common shift of all \(u_j\) is a rotation and has identically zero curvature. Use the unnormalized finite Fourier transform \(\widehat u_k=\sum_{j=0}^{N-1}u_je^{-2\pi i kj/N}\).

## Proof
**Exact diagonal Hessian.** Let \(F_n(\theta)=N^{-1}\sum_j e^{in\theta_j}\). Positive Fourier coefficients give \(E_t=\sum_{n\in\mathbb Z}e^{-2tn^2}|F_n|^2\), with absolutely convergent derivatives for each fixed \(t>0\). At the regular configuration, \(F_n=1\) if \(N\mid n\) and \(F_n=0\) otherwise. For \(N\nmid n\), the quadratic Taylor term in \(|F_n|^2\) equals \(\varepsilon^2 n^2 |\widehat u_{-n\pmod N}|^2/N^2\). For \(N\mid n\), it equals \(-\varepsilon^2n^2(\overline{u^2}-\overline u^2)\), where Parseval gives \(\overline{u^2}-\overline u^2=N^{-2}\sum_{k=1}^{N-1}|\widehat u_k|^2\). Thus the linear variation vanishes and
\[
E_t(\theta^0+\varepsilon u)-E_t(\theta^0)
=\frac{\varepsilon^2}{N^2}\sum_{k=1}^{N-1}\bigl(S_k(t)-S_0(t)\bigr)|\widehat u_k|^2+O_{N,t,u}(\varepsilon^3),
\]
where \(S_k(t)=\sum_{\ell\in\mathbb Z}(N\ell+k)^2e^{-2t(N\ell+k)^2}\). The eigenvalues of the real Hessian in the usual Euclidean-angle normalization are \(2(S_k-S_0)/N\) for nonzero frequency \(k\), while rotation has eigenvalue zero. These are exact for every \(t>0\); no truncated sum is used as a proof.

**Fine-scale regime.** By Poisson summation applied to \(f_t(x)=x^2e^{-2tx^2}\), whose real Fourier transform is
\[
\widehat f_t(\xi)=\sqrt{\frac\pi{2t}}\left(\frac1{4t}-\frac{\xi^2}{16t^2}\right)e^{-\xi^2/(8t)},
\]
we have
\[
S_k-S_0=\frac1N\sum_{r\ne0}\widehat f_t(2\pi r/N)\bigl(e^{2\pi irk/N}-1\bigr).
\]
The two terms \(r=\pm1\) dominate uniformly over the finite set \(1\le k\le N-1\), and all \(|r|\ge2\) terms are exponentially smaller. Hence, for fixed \(N\), uniformly in those \(k\),
\[
S_k-S_0=\frac{\pi^2}{2N^3}\sqrt{\frac\pi2}\,t^{-5/2}e^{-\pi^2/(2N^2t)}\left(1-\cos\frac{2\pi k}N\right)\bigl(1+O_N(t)\bigr),\qquad t\downarrow0.
\]
Every leading factor is positive; \(1-\cos(2\pi k/N)\) has its strict minimum exactly at \(k=1,N-1\), proving the first regime and local nondegeneracy modulo rotations.

**Coarse-scale regime.** It suffices to take \(1\le k\le \lfloor N/2\rfloor\), since \(S_{N-k}=S_k\). As \(t\to\infty\),
\[
S_k-S_0\sim c_{N,k}k^2e^{-2tk^2},\quad c_{N,k}=\begin{cases}2,&N\text{ even and }k=N/2,\\1,&\text{otherwise}.\end{cases}
\]
Indeed the shortest nonzero integer in the residue class \(k\bmod N\) is \(k\), with the stated multiplicity; the smallest nonzero integer in the zero class is \(N\), giving an exponentially negligible subtraction. The leading positive exponentials strictly order the classes by their representative \(k\), so the unique weakest class up to conjugacy is \(k=\lfloor N/2\rfloor\). This also proves nondegeneracy modulo rotations for all sufficiently large \(t\).

**Forced mode exchange.** For \(N\ge4\), the first and highest discrete Fourier modes are different. All spectral branches are continuous in \(t\), so their least-eigenvalue mode must change somewhere at a finite positive \(t\), with a tie of nonrotational curvatures. Finally \(G_t=H_{2t}(0)/E_t\), and at a stationary configuration its second variation has the opposite sign from that of \(E_t\). Thus the regular polygon is a strict local gESS maximum modulo common rotations in both scale regimes.

## Verification
The standalone `verification/check.py` reconstructs truncated Fourier energies, compares finite-difference and exact-alias Hessians for \(N=4,5,6,8,9,13\), checks representative small- and large-time soft-mode ordering, and exhibits a numerical change of ordering for the four-site case. In a local execution it reported 134 passed checks and a representative four-site crossing near \(t=0.340208834388\). The numerical root is illustration only; no uniqueness or rigorous decimal enclosure is asserted. The theorem for infinite sums follows from the analytic Poisson and Fourier arguments above.

## Relationship to prior work
K. You, *Heat-Kernel Entropy Profiles and Geometric Effective Sample Size for Weighted Measures on Manifolds* (2026), supplies the homogeneous-manifold overlap normalization and broad spectral entropy framework, but does not give the exact angle Hessian or the scale-dependent weakest Fourier deformation of equal circle samples. R. Coulangeon and A. Schürmann, *Local Energy Optimality of Periodic Sets* (2018), analyze Gaussian energy Hessians for variable Euclidean periodic configurations rather than fixed-circle heat effective sample size. L. Bétermin, *Minimal Soft Lattice Theta Functions* (2018), establishes lattice and translated-lattice energy optimality, not the finite-circle angular Fourier curvature crossover. These are mathematical comparisons, not claims of exhaustive priority.

## Limitations
The result is for equal weights, \(N\ge4\), and the intrinsic circle heat semigroup with angular Laplacian eigenvalues \(n^2\). It proves local optimality and soft-mode order for sufficiently small and sufficiently large positive times only; it does not prove global optimality, intermediate-time stability, monotone ordering, the number of transitions, or exact transition locations. Previously published theta-energy Hessian identities could imply special cases through non-obvious reformulations; this residual bibliographic risk remains.

## References
- K. You, *Heat-Kernel Entropy Profiles and Geometric Effective Sample Size for Weighted Measures on Manifolds*, arXiv:2607.06696v1, first available 2026-07-07, https://arxiv.org/abs/2607.06696.
- R. Coulangeon and A. Schürmann, *Local Energy Optimality of Periodic Sets*, arXiv:1802.02072v1, https://arxiv.org/abs/1802.02072.
- L. Bétermin, *Minimal Soft Lattice Theta Functions*, arXiv:1809.00473v1, https://arxiv.org/abs/1809.00473.
