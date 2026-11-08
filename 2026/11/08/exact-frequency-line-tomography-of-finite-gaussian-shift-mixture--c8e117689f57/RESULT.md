# Exact frequency-line tomography of finite Gaussian shift mixtures by pair-sum multiplicities

## Finding

For a finite sum of distinct real Gaussian translates, the precise number of parallel frequency lines necessary and sufficient to linearly reconstruct **all** coefficient products from its Gaussian-window Gabor spectrogram is a weighted additive-collision invariant of the translates. Let \(t_1<\cdots<t_m\) be distinct real numbers, and for each sum \(s\in\Sigma=\{t_j+t_k:1\le j\le k\le m\}\), let \(a_s\in\{0,1\}\) indicate whether \(s=2t_j\) for some \(j\), and let \(b_s\) count unordered pairs \(j<k\) satisfying \(t_j+t_k=s\). Put \(d_s=a_s+2b_s\).

For \(K\) frequency lines, the maximal real rank of all continuous-time intensity measurements, **viewed as a linear map on the real vector space of \(m\)-by-\(m\) Hermitian matrices**, is

\[
\boxed{\operatorname{rank}_{\rm generic}=\sum_{s\in\Sigma}\min\{K,d_s\}.}
\]

Generic means outside a proper real-analytic null set of frequency tuples. The **sharp minimal number of parallel frequency lines for complete Hermitian lifting** is therefore

\[
\boxed{K_{\min}=\max_{s\in\Sigma}(a_s+2b_s).}
\]

At or above this threshold, exactly \(m^2\) appropriately selected time-frequency intensity measurements linearly reconstruct the entire coefficient outer product; no fewer measurements can reconstruct every Hermitian matrix by a real-linear inverse. Once the outer product is reconstructed, each nonzero coefficient vector is determined up to a global unimodular factor. The lower bounds refer to **linear matrix lifting**, not to every possible nonlinear phase-retrieval algorithm.

For \(m\ge2\), \(K_{\min}=2\) **if and only if** all unordered pair sums \(t_j+t_k\), including diagonal sums, are distinct (the Sidon property). For these supports, two lines at \(\omega_0,\omega_1\) are individually sufficient precisely when

\[
\sin\bigl(\pi(\omega_1-\omega_0)(t_k-t_j)\bigr)\ne0
\quad\text{for every }j<k.
\]

There is an explicit optimal layout with \(m(m+1)/2\) arbitrary distinct time locations on the first frequency line and \(m(m-1)/2\) arbitrary distinct time locations on the second, each line using independently chosen time locations. A length-\(m\) arithmetic progression has \(K_{\min}=m\), so the optimal number of frequency lines is genuinely controlled by additive collisions and can range from two to the number of translates.

## Assumptions and scope

All shifts are distinct real numbers and fixed in advance; \(m\ge1\). Write \(g(t)=e^{-\pi t^2}\) and \(f_c(t)=\sum_{j=1}^m c_j g(t-t_j)\) for arbitrary complex coefficients \(c_j\). Adopt the (unnormalized-window) Gaussian short-time Fourier transform

\[
V_g f(x,\omega)=\int_{\mathbb R}f(t)\overline{g(t-x)}e^{-2\pi i\omega t}\,dt.
\]

The intensity is \(I_c(x,\omega)=|V_gf_c(x,\omega)|^2\). Its **Hermitian lifting** \(\mathcal L(H)(x,\omega)\), for arbitrary \(H=H^*\in\operatorname{Herm}(m)\), is the unique real-linear extension of the intensity under the replacement \(c_j\overline{c_k}\mapsto H_{jk}\). A line means a complete time scan \(x\in\mathbb R\) at one fixed real frequency; a finite measurement is one point on such a line. All statements are exact noiseless algebraic injectivity assertions; no uniform conditioning or optimal nonlinear sampling count is claimed.

## Proof

**1. Gaussian transform and exponential separation.** Completing the square gives, with the above normalization,

\[
V_g f_c(x,\omega)=\frac{e^{-\pi(x^2+\omega^2)/2}e^{-\pi i\omega x}}{\sqrt2}
\sum_{j=1}^m c_j e^{-\pi t_j^2/2}e^{\pi xt_j}e^{-\pi i\omega t_j}.
\]

For a Hermitian matrix \(H\), consequently,

\[
2e^{\pi(x^2+\omega^2)}\mathcal L(H)(x,\omega)
=\sum_{j,k=1}^m H_{jk}e^{-\pi(t_j^2+t_k^2)/2}
 e^{\pi x(t_j+t_k)} e^{-\pi i\omega(t_j-t_k)}.
\]

Writing \(\delta_{jk}=t_k-t_j>0\) for \(j<k\), the coefficient of \(e^{\pi sx}\), for a fixed \(s\in\Sigma\), is

\[
C_s(\omega)=a_s e^{-\pi t_j^2}H_{jj}\ (\text{if }s=2t_j)
+2\!\sum_{\substack{j<k\\t_j+t_k=s}}e^{-\pi(t_j^2+t_k^2)/2}
\left[\Re H_{jk}\cos(\pi\omega\delta_{jk})-\Im H_{jk}\sin(\pi\omega\delta_{jk})\right].
\]

The diagonal term is omitted when \(a_s=0\). Distinct real exponentials \(e^{\pi sx}\) are linearly independent on \(\mathbb R\). Hence observing \(\mathcal L(H)(x,\omega)\) at all times at a specified frequency exactly determines \(C_s(\omega)\) for every \(s\). Moreover, the \(|\Sigma|\) coefficients are determined by their values at *any* \(|\Sigma|\) distinct times: the real-exponential evaluation matrix is strictly totally positive after ordering time nodes and exponents (or invertible by the elementary zero-count for exponential sums).

**2. Multiplicity blocks.** For a fixed sum \(s\), two different unordered pairs \(j<k\) cannot share the same positive difference \(\delta_{jk}\): their sum and difference would then determine the same pair. Thus the \(d_s\) functions

\[
1\quad(\text{if }a_s=1),\qquad
\cos(\pi\omega\delta_{jk}),\quad\sin(\pi\omega\delta_{jk})
\quad(j<k,\ t_j+t_k=s)
\]

are linearly independent as real analytic functions of \(\omega\), since their complex-exponential frequencies \(0,\pm\delta_{jk}\) are distinct. The associated real evaluation map at \(K\) frequencies has rank at most \(\min(K,d_s)\), and the bound is attained for at least one tuple because independent analytic functions admit a nonsingular evaluation minor. The relevant determinants are analytic and not identically zero, so simultaneous attainment over the finitely many sums holds for all frequency tuples outside a finite union of proper analytic zero sets. As the sum blocks involve disjoint entries of \(H\), their ranks add. This proves the generic-rank formula and the sharp line count. For **every** choice of \(K<K_{\min}\) frequencies, one block has a nonzero matrix kernel, ruling out full Hermitian linear lifting even with continuous time scans.

**3. Finite optimal matrix tomography.** If \(K\ge K_{\min}\) and a frequency tuple has full rank, taking \(|\Sigma|\) distinct times on each line separates the coefficient functions \(C_s\). The resulting finite measurement matrix has full real rank \(m^2=\sum_s d_s\). Select any \(m^2\) independent rows from these \(K|\Sigma|\) rows. They determine every Hermitian \(H\), hence in particular every rank-one \(cc^*\). Conversely each scalar intensity is one real-linear equation on the \(m^2\)-dimensional real vector space \(\operatorname{Herm}(m)\), so fewer than \(m^2\) measurements cannot linearly recover all such matrices.

**4. Sidon and progressions.** If all unordered sums are distinct, each diagonal block has size one and each off-diagonal block size two; thus \(K_{\min}=2\) when \(m\ge2\). Conversely, a repeated unordered sum necessarily involves at least two distinct unordered pairs (one possibly diagonal), making \(d_s\ge3\). For one off-diagonal block the two-line matrix, after removal of nonzero scaling factors, has rows \((\cos(\pi\omega_\ell\delta),\sin(\pi\omega_\ell\delta))\), whose determinant equals \(\sin(\pi(\omega_1-\omega_0)\delta)\). This proves the precise two-line resonance criterion.

For the stated optimal Sidon layout, the first \(m(m+1)/2=|\Sigma|\) time measurements recover all first-line sum coefficients by exponential interpolation. Every diagonal entry is now known, and each off-diagonal pair has one known linear projection. Using these known projections, subtract the known part of the second-line intensity; what remains has one unknown coordinate per off-diagonal pair, at \(m(m-1)/2\) pairwise distinct exponential rates. An invertible exponential interpolation matrix at arbitrary distinct second-line times recovers those remaining coordinates. The resonance criterion guarantees that none of their coefficients vanishes. This uses exactly \(m^2\) samples.

If \(t_j=a+(j-1)h\) with \(h>0\), the central sum \(2a+(m-1)h\) receives \(m\) ordered pairs and hence \(d_s=m\). No sum can receive more than \(m\) ordered pairs, so \(K_{\min}=m\). For \(m=1\) there is only one diagonal coordinate and \(K_{\min}=1\). This completes all cases.

## Verification

The accompanying self-contained SymPy checker, `verify_gaussian_scans.py`, constructs exact real lifting matrices after invertible column rescalings. For shifts \(\{0,1,3\}\), the two-line layout with frequencies \(0,1/4\), six time nodes on the first line and three on the second has a nonzero exact \(9\)-by-\(9\) determinant. For the nonsidon progression \(\{0,1,2\}\), two frequency scans produce rank eight on the nine-dimensional Hermitian space, and three frequency scans produce full rank nine. All entries are algebraic and all ranks are exact (no floating-point thresholds). Run `python verify_gaussian_scans.py` from the extracted package. The computer checks test finite examples only; the analytic independence and block arguments above prove the theorem for arbitrary distinct real shifts.

## Relationship to prior work

Grohs and Liehr, *Stable Gabor phase retrieval in Gaussian shift-invariant spaces via biorthogonality* (public arXiv posting September 6, 2021), establish reconstruction and stability from semidiscrete parallel-line configurations with **continuous frequency** and a lattice of time positions. Their full work provides the close Gaussian shift-invariant model and Gabor normalization but does not give the present exact minimal number of fixed frequency scans, additive-sum block-rank classification, or \(m^2\)-point optimal Hermitian linear tomography for arbitrary finite shift sets.

Wellershoff, *Sampling at twice the Nyquist rate in two frequency bins guarantees uniqueness in Gabor phase retrieval* (public arXiv posting June 8, 2022), proves two-frequency nonlinear phase retrieval for **bandlimited** functions using a time sampling lattice. Finite sums of translated Gaussians have noncompact Fourier support, so its bandlimiting hypotheses do not apply. Its nonlinear uniqueness statement is also logically different from complete linear Hermitian-lift recovery.

Gröchenig, *Phase-retrieval in shift-invariant spaces with Gaussian generator* (2019), studies time-domain phaseless samples rather than minimal-frequency Gabor lift tomography. The pair-sum multiplicity classification is not claimed by these cited results. Similar matrix-lifting rank formulas for finite cyclic Gabor frames concern different finite-group measurement models and do not imply this real-line Gaussian rank formula without an additional reduction. No claim of exhaustive worldwide priority is made.

## Limitations

All frequencies and shifts are exact, with no noise robustness guarantee. Generic full rank need not imply uniform good conditioning; near-resonant Sidon line spacings can be very ill-conditioned. The lower bounds on frequency-line number and sample count govern real-linear Hermitian matrix tomography, **not the generally smaller rank-one set under nonlinear phase retrieval**. The optimal Sidon two-line layout requires its displayed nonresonance condition. Continuous time scans are an intermediate mathematical device; exact finite designs are proved. A further unknown general theorem about Gaussian spectrogram finite-dimensional lifting could subsume the statement; this remains a historical-priority risk.

## References

1. P. Grohs and L. Liehr, *Stable Gabor phase retrieval in Gaussian shift-invariant spaces via biorthogonality*, arXiv:2109.02494 (first public 2021-09-06), *Constructive Approximation* 59 (2024), 61–111, DOI:10.1007/s00365-023-09629-1.
2. M. Wellershoff, *Sampling at twice the Nyquist rate in two frequency bins guarantees uniqueness in Gabor phase retrieval*, arXiv:2206.03946 (first public 2022-06-08), *Journal of Fourier Analysis and Applications* 29 (2023), article 7.
3. K. Gröchenig, *Phase-retrieval in shift-invariant spaces with Gaussian generator*, arXiv:1911.11050 (2019). 
