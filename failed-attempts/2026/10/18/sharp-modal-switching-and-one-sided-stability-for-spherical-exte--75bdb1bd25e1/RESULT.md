# Sharp modal switching and one-sided stability for spherical extension on balls

## Finding

Let \(d\geq2\) be an integer, \(R>0\), and let \(d\sigma\) denote ordinary (unnormalized) surface measure on \(\mathbb S^{d-1}\). For \(f\in L^2(\mathbb S^{d-1},d\sigma)\), set
\[
\mathcal E_R f(x)=\int_{\mathbb S^{d-1}}e^{-ix\cdot\omega}f(\omega)\,d\sigma(\omega),\qquad |x|<R.
\]
Write \(\nu=d/2-1\), \(J_\mu\) for the Bessel function of the first kind, and
\[
T_k(R)=\int_0^R rJ_{\nu+k}(r)^2\,dr,\qquad k=0,1,2,\ldots.
\]
The exact sharp squared operator norm is
\[
\|\mathcal E_R\|_{L^2(\mathbb S^{d-1})\to L^2(B_R)}^2=(2\pi)^d\max\{T_0(R),T_1(R)\}.
\]
Define \(u(R)=R J_\nu(R)J_{\nu+1}(R)\). The complete extremizer space \(\mathcal H_{\mathrm{top}}(R)\), consisting of all equality cases together with zero, is the following orthogonal sum of spherical-harmonic subspaces \(\mathcal H_k^d\):
\[
\begin{array}{c|c}
\text{condition}&\mathcal H_{\mathrm{top}}(R)\\\hline
u(R)>0&\mathcal H_0^d\\
u(R)<0&\mathcal H_1^d\\
J_\nu(R)=0&\mathcal H_0^d\oplus\mathcal H_1^d\\
J_{\nu+1}(R)=0&\mathcal H_0^d\oplus\mathcal H_1^d\oplus\mathcal H_2^d
\end{array}
\]
The two Bessel functions never vanish simultaneously at positive \(R\); consequently these cases are mutually exclusive and exhaustive. The double-mode and triple-mode radii have top-eigenspace dimensions \(d+1\) and \(d(d+3)/2\), respectively.

More strongly, let \(\Pi_R\) be the orthogonal projector onto \(\mathcal H_{\mathrm{top}}(R)\) and put \(M(R)=\max\{T_0(R),T_1(R)\}\). Then
\[
(2\pi)^dM(R)\|f\|_2^2-\|\mathcal E_Rf\|_2^2
\ge (2\pi)^d G(R)\|f-\Pi_Rf\|_2^2,
\]
where \(G(R)>0\) is **the sharp constant**, explicitly
\[
G(R)=\begin{cases}
\min\{u(R),2(\nu+1)J_{\nu+1}(R)^2\},&u(R)>0,\\
\min\{-u(R),2(\nu+2)J_{\nu+2}(R)^2\},&u(R)<0,\\
\min\{2(\nu+1)J_{\nu+1}(R)^2,2(\nu+2)J_{\nu+2}(R)^2\},&J_\nu(R)=0,\\
\min\{2(\nu+2)J_{\nu+2}(R)^2,2(\nu+3)J_{\nu+3}(R)^2\},&J_{\nu+1}(R)=0.
\end{cases}
\]

There is a qualitative asymmetry in the sharp stability gap at triple collisions. At any positive zero \(z\) of \(J_{\nu+1}\), the normalized gap satisfies
\[
G(z+\delta)=2(\nu+1)J_\nu(z)^2\delta^2+O_{d,z}(\delta^3)
\quad(\delta\downarrow0),
\]
\[
G(z-\delta)=zJ_\nu(z)^2\delta+O_{d,z}(\delta^2)
\quad(\delta\downarrow0).
\]
At every positive zero \(y\) of \(J_\nu\), instead,
\[
G(y\pm\delta)=yJ_{\nu+1}(y)^2\delta+O_{d,y}(\delta^2)
\quad(\delta\downarrow0).
\]
Thus every triple collision has a quadratic gap onset on its high-radius side but only linear onset on its low-radius side.

## Assumptions and scope

All statements hold for every integer dimension \(d\ge2\), every finite \(R>0\), and arbitrary complex-valued input \(f\in L^2(\mathbb S^{d-1},d\sigma)\). The ball is centered at the origin, and the Fourier kernel has phase \(e^{-ix\cdot\omega}\) (not a \(2\pi\)-rescaled phase). Eigenvalues, norms, and stability constants depend on this normalization. The inequalities refer to the full infinite-dimensional spherical input space, not a degree-truncated subspace. The sharp inequality uses the **distance to the entire top eigenspace**, including all tied modes at transition radii.

## Proof

**1. Exact diagonalization.** Let \(P_k\) be the orthogonal projection onto \(\mathcal H_k^d\). The classical spherical Fourier–Bessel formula gives, for \(Y_k\in\mathcal H_k^d\) and polar coordinates \(x=r\theta\),
\[
\mathcal E_RY_k(r\theta)=(2\pi)^{d/2}(-i)^k r^{-\nu}J_{\nu+k}(r)Y_k(\theta).
\]
Angular orthogonality and polar integration show for every finite spherical-harmonic expansion that
\[
\|\mathcal E_R f\|_{L^2(B_R)}^2=(2\pi)^d\sum_{k\ge0}T_k(R)\|P_kf\|_2^2.
\]
Since \(\|\mathcal E_Rf\|_2\le |B_R|^{1/2}\sigma(\mathbb S^{d-1})^{1/2}\|f\|_2\), boundedness and density extend this identity to every input. In particular the normal operator is a direct sum of scalar eigenvalues \((2\pi)^dT_k(R)\), and \(T_k(R)\to0\) as \(k\to\infty\) at fixed \(R\) by the elementary Bessel series.

**2. Two exact difference identities.** For any real \(\mu\ge0\), the standard recurrences
\[
J_\mu'(r)=\frac\mu rJ_\mu(r)-J_{\mu+1}(r),\qquad
J_{\mu+1}'(r)=J_\mu(r)-\frac{\mu+1}rJ_{\mu+1}(r)
\]
produce
\[
\frac{d}{dr}\bigl(rJ_\mu(r)J_{\mu+1}(r)\bigr)
=r\bigl(J_\mu(r)^2-J_{\mu+1}(r)^2\bigr).
\]
The boundary term at zero vanishes for \(\mu\ge0\), so
\[
T_k(R)-T_{k+1}(R)=RJ_{\nu+k}(R)J_{\nu+k+1}(R).
\tag{1}
\]
Adding (1) for adjacent degrees and using
\(J_\mu(R)+J_{\mu+2}(R)=2(\mu+1)J_{\mu+1}(R)/R\) gives
\[
T_k(R)-T_{k+2}(R)=2(\nu+k+1)J_{\nu+k+1}(R)^2\ge0.
\tag{2}
\]
Thus both subsequences \(T_0\ge T_2\ge T_4\ge\cdots\) and \(T_1\ge T_3\ge T_5\ge\cdots\) are nonincreasing. Together with (1) at \(k=0\), this proves the exact norm and identifies which of degrees zero and one is largest.

**3. All equality cases.** A zero of \(J_\mu\) cannot also be a zero of \(J_{\mu+1}\), for the first recurrence would make \(J_\mu\) and its derivative vanish at an ordinary point of Bessel's differential equation. If \(u>0\), the only maximal mode is \(k=0\); if \(u<0\), it is \(k=1\). If \(J_\nu(R)=0\), (1) ties degrees zero and one, while (2) at \(k=0\) and \(k=1\) makes degrees two and three strictly lower, respectively. If \(J_{\nu+1}(R)=0\), (1) and (2) tie degrees zero, one, and two. The recurrence then gives \(J_{\nu+2}(R)=-J_\nu(R)\ne0\) and \(J_{\nu+3}(R)=2(\nu+2)J_{\nu+2}(R)/R\ne0\); (2) at \(k=1,2\) makes degrees three and four strictly lower. No further maximal modes are possible by the parity chains. Standard harmonic dimension formulas yield the displayed dimensions.

**4. Sharp positive gap.** The spectral deficit is the sum of \((2\pi)^d(M-T_k)\|P_kf\|_2^2\). By the two parity chains, the largest **nonmaximal** eigenvalue is \(\max(T_1,T_2)\) when degree zero alone is maximal; \(\max(T_0,T_3)\) when degree one alone is maximal; \(\max(T_2,T_3)\) for the zero/one tie; and \(\max(T_3,T_4)\) for the zero/one/two tie. Substitution of (1)–(2) gives each displayed formula for \(G(R)\). Strict positivity follows from the noncoincidence of consecutive Bessel zeros and the explicit relations in Step 3. Sharpness follows by choosing a nonzero harmonic vector of the nonmaximal degree that realizes the smaller gap.

**5. One-sided transition.** At a zero \(z>0\) of \(J_{\nu+1}\), the recurrence implies \(J_{\nu+1}'(z)=J_\nu(z)\ne0\); hence
\(u(z+\delta)=zJ_\nu(z)^2\delta+O_{d,z}(\delta^2)\).
For positive \(\delta\), degree zero wins and the even-parity competitor degree two has gap
\(2(\nu+1)J_{\nu+1}(z+\delta)^2
=2(\nu+1)J_\nu(z)^2\delta^2+O_{d,z}(\delta^3)\), smaller than the linearly separating odd competitor. For negative \(\delta\), degree one wins and its distance to degree zero is \(-u\), while its distance to degree three stays bounded away from zero. This yields the two different orders. At a zero \(y>0\) of \(J_\nu\), the recurrence gives \(J_\nu'(y)=-J_{\nu+1}(y)\), whence \(u(y+\delta)=-yJ_{\nu+1}(y)^2\delta+O(\delta^2)\). At that radius the competitors of degree zero or one in their own parity chains remain separated; the gap is therefore linear from either side. This proves the claimed expansions.

## Verification

The included `verification_check.py` independently integrates \(T_k(R)\) using 50-digit arithmetic and checks (1), (2), and global modal rankings over six dimensions, six radii, and thirteen degrees, performing 756 integral-identity and top-mode comparisons. It additionally checks first zeros of \(J_\nu\) and \(J_{\nu+1}\) in four dimensions and the predicted two- or three-way collisions. Output: `VERIFY_OK 756 integral identities/top modal comparisons`. This finite stress test is supplementary; the proof for all dimensions, radii, and modes is analytic.

## Relationship to prior work

Classical spherical Fourier–Bessel diagonalization and the Bessel recurrences are prior mathematical identities, not novelty claims. Oliveira e Silva and Wróbel (arXiv:2412.03942, first public 2024-12-05) treat dimension-free restriction and Bessel estimates on the whole space, rather than this sharp finite-ball \(L^2\) spectrum and transition stability. Carneiro, Oliveira e Silva, and Sousa (arXiv:1710.10365) determine mixed-norm extension properties for integrable all-space exponents above \(2d/(d-1)\). Ciccone and Sousa (doi:10.1007/s00041-025-10201-7) also analyze global, untruncated higher-exponent norms. Barceló, Bennett, and Carbery (doi:10.1017/S1446788708000694) address radial weighted localization estimates up to geometric constants and do not state the precise unweighted ball-normal-operator spectrum. The claimed contribution is the *combined exact all-radius modal/equality classification, complete sharp positive spectral gap, and asymmetric collision law*, not the underlying standard Bessel identities.

## Limitations

The ball must be centered and unweighted; replacing it by a nonradial aperture destroys this diagonal argument. The theorem is quadratic and does not address the general \(L^q\) restriction extremizer problem. Classical formulas make the computation relatively short, and an equivalent local-spectrum classification in older special-function or acoustic literature cannot be excluded without comprehensive human historical review. No independent scientific audit has been performed. The finite numerical tests do not certify the statements for untested cases.

## References

- D. Oliveira e Silva and B. Wróbel, *Dimension-free Fourier restriction inequalities*, arXiv:2412.03942 (initial version 2024-12-05), https://arxiv.org/html/2412.03942v2.
- E. Carneiro, D. Oliveira e Silva, and M. Sousa, *Sharp mixed norm spherical restriction*, arXiv:1710.10365, https://arxiv.org/abs/1710.10365.
- V. Ciccone and M. Sousa, *Global and local maximizers for some Fourier extension estimates on the sphere*, Journal of Fourier Analysis and Applications (2025), doi:10.1007/s00041-025-10201-7, https://link.springer.com/article/10.1007/s00041-025-10201-7.
- J. A. Barceló, J. M. Bennett, and A. Carbery, *A note on localised weighted inequalities for the extension operator*, Journal of the Australian Mathematical Society (2008), doi:10.1017/S1446788708000694.
- NIST Digital Library of Mathematical Functions, Chapter 10 (Bessel functions and recurrences), https://dlmf.nist.gov/10.
