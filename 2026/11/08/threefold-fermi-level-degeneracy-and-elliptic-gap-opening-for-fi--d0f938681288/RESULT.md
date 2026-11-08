# Threefold Fermi-level degeneracy and elliptic gap opening for first-Hermite localization

## Finding

For every integer \(N\ge1\), the first-Hermite short-time Fourier concentration operator on a disk of phase-space area \(N\) has a *three-dimensional* eigenspace precisely at its rank-\(N\) spectral cutoff. Its corresponding Hermite indices are \(N-1,N,N+1\). Every maximal-energy rank-\(N\) orthogonal subspace consists of all lower Hermite modes and an arbitrary line in this three-dimensional eigenspace.

An area-preserving elliptic deformation resolves that ambiguity at first order, with an exact positive splitting coefficient. For \(\tau>0\), the maximizing cutoff line tends to \(\mathbb C(h_{N-1}-h_{N+1})\), whereas for \(\tau<0\) it tends to \(\mathbb C(h_{N-1}+h_{N+1})\). Thus, an arbitrarily small aspect-ratio perturbation selects two distinct limiting maximizers, depending on its sign.

Let \(\mu_1(N,\tau)\ge\mu_2(N,\tau)\ge\cdots\) denote the eigenvalues, including multiplicities, of the operator defined below. Put
\[
 p_N=\frac{e^{-N}N^N}{N!},\qquad
 c_N=p_N\sqrt{\frac{N}{N+1}},\qquad
 \ell_N=\Pr\{\operatorname{Pois}(N)\ge N+1\}.
\]
Then, for each fixed \(N\), as \(\tau\to0\),
\[
\begin{aligned}
 \mu_N(N,\tau)&=\ell_N+c_N|\tau|+O_N(\tau^2),\\
 \mu_{N+1}(N,\tau)&=\ell_N+O_N(\tau^2),\\
 \mu_{N+2}(N,\tau)&=\ell_N-c_N|\tau|+O_N(\tau^2),\\
 \mu_N(N,\tau)-\mu_{N+1}(N,\tau)&=c_N|\tau|+O_N(\tau^2).
\end{aligned}
\]
The gap coefficient obeys \(c_N\sim(2\pi N)^{-1/2}\). For every fixed \(N\), the rank-\(N\) maximizing subspace is unique once \(0<|\tau|<\varepsilon_N\) for some \(\varepsilon_N>0\).

## Assumptions and scope

On \(L^2(\mathbb R)\) use the normalized Hermite functions \(h_j\) with \(h_0(t)=2^{1/4}e^{-\pi t^2}\) and \(h_1(t)=2\sqrt\pi\,t h_0(t)\), and define
\[
 V_{h_1}f(x,\xi)=\int_{\mathbb R}f(t)\overline{h_1(t-x)}e^{-2\pi i\xi t}\,dt.
\]
For an integer \(N\ge1\) and real \(\tau\), let
\[
 E_{N,\tau}=\{(x,\xi):\pi(e^{-2\tau}x^2+e^{2\tau}\xi^2)\le N\},\qquad
 H_{N,\tau}=V_{h_1}^*\mathbf1_{E_{N,\tau}}V_{h_1}.
\]
The ellipse has exact area \(N\); \(H_{N,\tau}\) is positive, compact and trace class, and its eigenvalues are nonnegative and repeated according to multiplicity. A rank-\(N\) subspace is *maximal-energy* when the sum of the captured STFT energies of an orthonormal basis is maximal, equivalently when its projection maximizes \(\operatorname{Tr}(P H_{N,\tau})\) among rank-\(N\) orthogonal projections. Limits of lines use Hilbert-space projective convergence. All perturbation statements fix \(N\) before letting \(\tau\to0\); there is no uniform joint-limit claim.

## Proof

**1. Exact circular spectrum.** In polar phase-space variables \(s=\pi(x^2+\xi^2)\), \(\theta=\arg(x+i\xi)\), the first-Hermite STFT of \(h_j\), after removal of a common unimodular phase, is
\[
 \Psi_j(s,\theta)=\frac{(j-s)s^{(j-1)/2}}{\sqrt{j!}}e^{-s/2}e^{i(j-1)\theta},\qquad j\ge0.
\]
For \(j=0\), this means \(\Psi_0=-\sqrt{s}e^{-s/2}e^{-i\theta}\); the displayed expression has its continuous interpretation for \(s>0\). These are the standard first-order complex Hermite functions; the normalization follows from \(dx\,d\xi=ds\,d\theta/(2\pi)\) and the STFT isometry. Rotational integration diagonalizes \(H_{N,0}\) in \(\{h_j\}\), with eigenvalues
\[
 \lambda_j(T)=\int_0^T\frac{(j-s)^2}{s}\frac{e^{-s}s^j}{j!}\,ds,\qquad T>0.
\]
The integral is nonsingular for every \(j\), including \(j=0\). Integration of powers against \(e^{-s}\), using \(p_j(T)=e^{-T}T^j/j!\), yields
\[
 \lambda_j(T)=\Pr\{\operatorname{Pois}(T)\ge j\}+(j-1-T)p_j(T).
\]
For \(j=0\) the probability is \(1\), so the same identity holds. Subtracting adjacent terms and using \(p_{j+1}(T)=Tp_j(T)/(j+1)\) gives the exact difference identity
\[
 \lambda_{j+1}(T)-\lambda_j(T)=\frac{(T-j)(j+1-T)}{j+1}p_j(T). \tag{1}
\]

**2. Exact Fermi degeneracy and its isolation.** At \(T=N\) the right side of (1) vanishes exactly for \(j=N-1,N\); it is strictly negative for all other nonnegative integers \(j\). Consequently,
\[
 \lambda_0(N)>\cdots>\lambda_{N-2}(N)>\lambda_{N-1}(N)=\lambda_N(N)=\lambda_{N+1}(N)>\lambda_{N+2}(N)>\cdots
\]
when \(N\ge2\), with the empty leading segment omitted for \(N=1\). The common value is \(\ell_N\), since the correction in the Poisson identity vanishes at \(j=N+1\). The adjacent positive spectral gaps are exactly
\[
 \lambda_{N-2}(N)-\ell_N=\frac{2p_N}{N}\quad(N\ge2),\qquad
 \ell_N-\lambda_{N+2}(N)=\frac{2N p_N}{(N+1)(N+2)}.
\]
Both are asymptotic to \(\sqrt{2/\pi}\,N^{-3/2}\). The compact-operator maximal trace principle now proves the characterization of all rank-\(N\) maximizers: include the \(N-1\) strictly superior modes and select exactly one dimension from the triple eigenspace.

**3. Elliptic shape derivative.** The polar upper integration boundary is
\[
 T_\tau(\theta)=\frac{N}{e^{-2\tau}\cos^2\theta+e^{2\tau}\sin^2\theta},\qquad
 T'_0(\theta)=2N\cos2\theta.
\]
The operator admits a trace-norm differentiable, indeed twice continuously differentiable, representation as the integral of the smooth rank-one STFT evaluation kernels over this moving radial boundary. Therefore its derivative matrix in the Hermite basis is obtained by differentiating the upper limit of the polar integrals. Angular orthogonality with \(\cos2\theta\) gives the exact selection rule
\[
 \left\langle H'_{N,0}h_j,h_k\right\rangle=
 \begin{cases}
 \displaystyle N e^{-N}\frac{(j-N)(k-N)N^{(j+k-2)/2}}{\sqrt{j!k!}},&|j-k|=2,\\
 0,&|j-k|\ne2.
 \end{cases} \tag{2}
\]
Here the displayed convention is the standard phase convention for \(h_j\) and the Fourier/STFT transform given above. Formula (2) follows since \(\frac1{2\pi}\int_0^{2\pi}(2N\cos2\theta)e^{i(j-k)\theta}d\theta=N\) when \(|j-k|=2\).

Let \(\mathcal E_N=\operatorname{span}\{h_{N-1},h_N,h_{N+1}\}\). Projecting (2) to \(\mathcal E_N\), in its displayed ordered basis, yields
\[
 P_{\mathcal E_N}H'_{N,0}P_{\mathcal E_N}
 =\begin{pmatrix}0&0&-c_N\\0&0&0\\-c_N&0&0\end{pmatrix},\qquad
 c_N=\frac{e^{-N}N^N}{N!}\sqrt{\frac N{N+1}}.
\]
Its three eigenvalues are \(+c_N,0,-c_N\); the eigenvector for \(+c_N\) is \((h_{N-1}-h_{N+1})/\sqrt2\), and for \(-c_N\) it is \((h_{N-1}+h_{N+1})/\sqrt2\).

**4. Perturbed cutoff.** Because \(\ell_N\) is isolated from the rest of the spectrum by the strictly positive gaps above and below, its three-dimensional spectral projection varies smoothly in a neighborhood of \(\tau=0\). Standard finite-multiplicity selfadjoint perturbation theory, or a direct three-dimensional reduction using that projection, gives three eigenvalue branches with first derivatives \(+c_N,0,-c_N\), each with remainder \(O_N(\tau^2)\). Sorting the branches for either sign of \(\tau\) proves the stated absolute-value asymptotics. Their strict first-order separation and persistence of the outer spectral gaps imply uniqueness of the top-rank-\(N\) subspace when \(0<|\tau|\) is sufficiently small. The corresponding cutoff eigenvector tends to the stated sign-dependent line. Stirling's formula yields \(c_N\sim(2\pi N)^{-1/2}\). This concludes the proof.

## Verification

The standalone file `hermite_ellipse_checks.py` reconstructs the complex Hermite STFT matrix by independent polar quadrature (angular trapezoidal integration and radial Gauss–Legendre integration), compares the circular matrix to the Poisson eigenvalue formula, verifies the exact adjacent-difference and plateau-gap identities, and checks the predicted elliptic derivative, three spectral branches, Fermi gap and limiting eigenvectors for \(N=1,2,3,4,5,7,10\). Execute `python hermite_ellipse_checks.py` with Python 3, NumPy and SciPy. The script reports `HERMITE_ELLIPSE_CHECKS_PASS 252` when all its assertions pass. Finite checks are numerical evidence only; the infinitely many integer cases and exact perturbation constants are proved analytically above.

## Relationship to prior work

Abreu, Gröchenig and Romero (arXiv:1704.03042; first publicly submitted April 10, 2017) establish the general circular-domain Hermite diagonalization and eigenvalue integral in their Proposition 4.1 and Lemma 4.2, and expressly note a two-eigenvalue crossing in Remark 4.3. Those radial formulas are used as prior input, not claimed new. Their inspected treatment of radial eigenvalues, finite Weyl–Heisenberg ensembles and their spectral truncations does not identify the **all-integer threefold rank cutoff and its exact gap**, nor the **elliptic shape-derivative splitting and sign-dependent selection** proved here. No inference from their general finite-ensemble existence results determines the elliptical splitting matrix.

Nicola and Tilli (arXiv:2106.03423, 2021) analyze concentration and extremizers for the *Gaussian-window* STFT under arbitrary regions; their Faber–Krahn theorem does not apply to the non-Gaussian first-Hermite window. Knutsen (2020) analyzes a *Gaussian-window*, radial-symbol Cantor-type localization problem. Oblak et al. (arXiv:2301.01726, 2023) study semiclassical anisotropic quantum Hall droplets in the *lowest Landau level*, and explicitly do not include higher Landau-level contributions. Those settings do not give the stated finite-\(N\) first excited Landau-level cutoff splitting. The standard degenerate perturbation principle is also prior mathematics; the particular exact shape derivative and Fermi-level degeneracy are the claims here.

## Limitations

The claim addresses only a normalized first-Hermite window, the disk of integer area, and the displayed area-preserving elliptic family. The asymptotics are for each fixed \(N\) and small ellipticity; they are not uniform in \(N\). No optimization over arbitrary shapes or windows, no finite sampling theorem, and no statement about physical many-body energy levels is given. The first-order splitting does not determine the complete finite-ellipticity spectrum. Although the primary comparisons found no equivalent complete statement, an earlier implicit equivalent calculation in polyanalytic Toeplitz, Landau-level or shape-perturbation literature cannot be excluded; independent verification has not been performed.

## References

- L. D. Abreu, K. Gröchenig and J. L. Romero, *Harmonic analysis in phase space and finite Weyl–Heisenberg ensembles*, arXiv:1704.03042 (first posted 2017-04-10); *Journal of Statistical Physics* 174 (2019), 1104–1136, https://doi.org/10.1007/s10955-019-02226-2. In particular, Section 4, Proposition 4.1, Lemma 4.2 and Remark 4.3.
- F. Nicola and P. Tilli, *The Faber–Krahn inequality for the Short-time Fourier transform*, arXiv:2106.03423 (2021), *Inventiones Mathematicae* 230 (2022), 1–30.
- H. Knutsen, *Daubechies’ Time–Frequency Localization Operator on Cantor Type Sets I*, *Journal of Fourier Analysis and Applications* 26, article 47 (2020), https://doi.org/10.1007/s00041-020-09751-9.
- B. Oblak, B. Lapierre, P. Moosavi, J.-M. Stéphan and B. Estienne, *Anisotropic Quantum Hall Droplets*, arXiv:2301.01726 (2023), *Physical Review X* 14, 011030 (2024).
