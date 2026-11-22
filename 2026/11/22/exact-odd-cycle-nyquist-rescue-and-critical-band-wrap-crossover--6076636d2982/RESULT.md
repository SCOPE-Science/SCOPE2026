# Exact odd-cycle Nyquist rescue and critical band-wrap crossover for periodized sinc powers

## Finding

The periodized covariance of every integer power of a sampled sinc kernel has an exact all-size spectral classification. At the first circular band-wrap boundary, **even grids retain an exact Nyquist zero**, while **odd grids remain invertible** and have a sharp least eigenvalue of order \(N^{-(p-1)}\). An \(N^{-1}\)-scale bandwidth perturbation has a fully explicit, parity-dependent crossover profile.

Specifically, fix an integer \(p\ge2\), an integer \(N\ge2\), and \(0<a<\pi\). Set \(s_a(0)=1\) and \(s_a(j)=\sin(aj)/(aj)\) for every nonzero integer \(j\). Define the cyclic matrix
\[
K_{N,p,a}(r,s)=\sum_{\ell\in\mathbb Z}s_a(r-s+\ell N)^p,
\qquad r,s\in\mathbb Z/N\mathbb Z.
\]
This sum converges absolutely and defines a real symmetric positive-semidefinite circulant.

Let \(b_{p,a}\) be the probability density of the sum of \(p\) independent random variables uniformly distributed on \([-a,a]\). For \(k=0,\ldots,N-1\), its exact eigenvalues are
\[
\lambda_k=2\pi\sum_{j\in\mathbb Z}b_{p,a}\!\left(\frac{2\pi k}{N}+2\pi j\right).
\tag{1}
\]
The least eigenvalue always occurs at a frequency nearest \(\pi\), not necessarily uniquely.

Writing \(\alpha=pa\), the following statements hold.

**Exact rank below first wrap.** If \(0<\alpha\le\pi\),
\[
\operatorname{nullity} K_{N,p,a}
=N+1-2\left\lceil\frac{N\alpha}{2\pi}\right\rceil.
\tag{2}
\]
For arbitrary \(0<a<\pi\), the matrix is strictly positive definite exactly when
\[
\begin{cases}
\alpha>\pi, & N\text{ even},\\
\alpha>\pi(1-1/N),&N\text{ odd}.
\end{cases}
\tag{3}
\]
In particular, an odd cycle has a nonempty invertible window of bandwidths strictly below the continuum half-circle threshold.

**Exact critical eigenvalue.** At \(\alpha=\pi\), even \(N\) has precisely one zero eigenvalue. Every odd \(N\ge\max\{3,p\}\) has
\[
\lambda_{\min}(K_{N,p,\pi/p})
=\frac{p^p}{2^{p-1}(p-1)!\,N^{p-1}}.
\tag{4}
\]
This positive constant is an equality, not an asymptotic estimate.

**Exact near-critical crossover.** Put \(\varepsilon=pa-\pi\), and \(\delta_N=0\) for even \(N\), \(\delta_N=\pi/N\) for odd \(N\). If
\[
|\varepsilon|\le\pi/4,
\qquad |\varepsilon|+\delta_N\le2a,
\]
then, with \(u_+=\max\{u,0\}\),
\[
\lambda_{\min}(K_{N,p,a})
=\frac{2\pi}{(p-1)!(2a)^p}
\left[(\varepsilon+\delta_N)_+^{p-1}+(\varepsilon-\delta_N)_+^{p-1}\right].
\tag{5}
\]
For fixed \(t\in\mathbb R\), choose \(a_N=\pi(1+t/N)/p\); then (5) applies for all sufficiently large \(N\), and for \(\eta_N=0\) on even grids and \(\eta_N=1\) on odd grids,
\[
N^{p-1}\lambda_{\min}(K_{N,p,a_N})
=\frac{p^p}{2^{p-1}(p-1)!}
\left(1+\frac{t}{N}\right)^{-p}
\left[(t+\eta_N)_+^{p-1}+(t-\eta_N)_+^{p-1}\right].
\tag{6}
\]
Thus each parity subsequence has a distinct explicit limiting scaling profile.

## Assumptions and scope

The exponent \(p\) is an integer at least two; grid size \(N\) is at least two; and \(a\) is a real angular half-bandwidth strictly between zero and \(\pi\). The periodization, rather than ordinary finite Toeplitz truncation, is essential. The entries are sampled at integer spatial sites; the Fourier transform convention for (1) is \(\widehat{c}(\theta)=\sum_{j\in\mathbb Z}c(j)e^{-ij\theta}\). The density \(b_{p,a}\) integrates to one on the real line. Real and complex vectors have the same eigenvalues and positive-definiteness threshold. Equations (2)–(4) do not require the small-crossover assumptions of (5).

## Proof

1. **Fourier representation and normalization.** A centered uniform random variable \(U\) on \([-a,a]\) has characteristic function \(\mathbb E[e^{ijU}]=s_a(j)\) for every integer \(j\). For the independent sum \(S=U_1+\cdots+U_p\), \(s_a(j)^p=\mathbb E[e^{ijS}]=\int_{\mathbb R}e^{ijx}b_{p,a}(x)\,dx\). Because \(|s_a(j)^p|=O(|j|^{-p})\), its Fourier series converges absolutely. Periodizing the sequence in residues modulo \(N\), and applying the discrete Fourier transform, gives
\[
\lambda_k=\sum_{j\in\mathbb Z}s_a(j)^p e^{-2\pi ikj/N}
=2\pi\sum_{h\in\mathbb Z}b_{p,a}(2\pi k/N+2\pi h).
\]
The sign from the transform disappears because the density is even. In particular, all eigenvalues are nonnegative and the matrix is positive semidefinite.

2. **Where the minimum occurs.** The wrapped density \(B(\theta)=\sum_h b_{p,a}(\theta+2\pi h)\) is the circular \(p\)-fold convolution of normalized indicators of the centered arc \([-a,a]\). Every such arc indicator is even and nonincreasing as a function of circular distance from zero. The circular convolution of any two even, circularly nonincreasing, nonnegative functions is again even and circularly nonincreasing: by the layer-cake formula, each convolution is a positive mixture of overlaps of two centered arcs, and the overlap length is nonincreasing with the circular displacement in \([0,\pi]\). Induction gives this property for \(B\). The discrete angle closest to \(\pi\) therefore attains the minimum. Its distance from \(\pi\) is exactly \(\delta_N\).

3. **Zeros, rank and positive definiteness.** The real convolution density \(b_{p,a}\) is positive precisely in the open interval \((-pa,pa)\) and vanishes outside it, including its endpoints. If \(pa\le\pi\), periodization contributes at most one positive copy on the interior of \((-\pi,\pi)\). The nonzero eigenvalues correspond exactly to integer indices satisfying \(\min\{k,N-k\}<Npa/(2\pi)\). The number of those indices is \(2\lceil Npa/(2\pi)\rceil-1\); this proves (2), including the equality boundary. For larger \(pa\), the density's circular periodization is positive at every angle precisely if \(pa>\pi\). On the finite frequency grid, positivity already occurs once the open support reaches the angle nearest \(\pi\), namely \(\pi-\delta_N\). These conditions give (3), with strict inequalities because the density vanishes at each support endpoint.

4. **Exact outer B-spline edge.** If \(0\le u\le2a\), the event \(S\in[pa-u,pa]\) is determined by nonnegative deficits \(a-U_i\) with total at most \(u\). Since their upper restrictions \(a-U_i\le2a\) are then automatically satisfied, differentiation of the simplex-volume formula gives
\[
b_{p,a}(pa-u)=\frac{u^{p-1}}{(p-1)!(2a)^p},\qquad 0\le u\le2a.
\tag{7}
\]
By symmetry the corresponding lower-edge formula holds at \(-pa\).

5. **The crossover.** The minimizing grid angle is \(\pi-\delta_N\). With \(pa=\pi+\varepsilon\), its distances inside the two neighboring support copies are \(\varepsilon+\delta_N\) and \(\varepsilon-\delta_N\). Under the assumptions in (5), each positive distance lies in \([0,2a]\); \(|\varepsilon|\le\pi/4\) excludes all more distant periodic images. Applying (7) to these zero, one or two possible contributions establishes (5). If \(pa=\pi\), then an even grid has exactly one zero at \(\pi\), while an odd grid has \(\varepsilon=0\) and \(\delta_N=\pi/N\); for \(N\ge p\), the bound \(\delta_N\le2a\) holds. Substitution into (5) gives (4). Finally, inserting \(a_N=\pi(1+t/N)/p\), \(\varepsilon=\pi t/N\) and \(\delta_N=\pi\eta_N/N\) into (5) yields (6) algebraically. This also proves all quantifiers concerning sufficiently large \(N\).

## Verification

The standalone `sinc_circle_check.py` reconstructs the wrapped B-spline Fourier symbol in exact rational arithmetic for rational angular parameters normalized by \(\pi\). It checks 3,627 complete spectra for \(2\le p\le10\), \(2\le N\le32\), and thirteen bandwidth ratios; 2,232 independent rank/nullity comparisons; 2,142 exact crossover comparisons in the range of (5); and 21 critical odd-cycle gap identities. All passed. These finite calculations check algebraic normalizations and boundary indices but are **not** the infinite proof, which is given above.

To reproduce: run `python sinc_circle_check.py` using Python 3's standard library. No optional dependencies or external files are needed.

## Relationship to prior work

Pillai's November 2026 paper, *Spectral Regimes of Truncated sinc-Power and Pulse-Train Kernels*, analyzes finite **Toeplitz truncations** and the Szegő-quantile edge exponent for sinc-power symbols, explicitly treating the no-aliasing regime. Its source-side B-spline edge exponent motivates the present question, but its Toeplitz eigenvalues do not equal samples of the symbol and do not give exact cyclic rank or parity-dependent Nyquist eigenvalues. In contrast, the present matrices are the **periodizations** of a sampled power kernel, so DFT diagonalization is exact and the first band-wrap boundary has an arithmetic finite-grid effect.

The B-spline density formula and circulant diagonalization are classical; the contribution here is their combined all-grid exact rank/invertibility classification and sharply scaled finite-bandwidth crossover for this specific family. Related spline collocation spectra concern different sample operators and do not assert this theorem.

## Limitations

The theorem does not apply to a principal \(N\times N\) Toeplitz block of the same infinite kernel, noninteger sinc powers, irregular grids, or the unsampled continuous convolution operator. The complete eigenvalue formula (1) is valid at every bandwidth in scope, but (5) is a near-first-wrap identity and is not claimed beyond its explicit parameter conditions. The literature comparison does not establish absolute uniqueness: older equivalent cyclic-covariance calculations may exist and require an independent bibliographic review. No independent mathematical audit has been performed.

## References

- U. Pillai, *Spectral Regimes of Truncated sinc-Power and Pulse-Train Kernels: Edge Exponents, Per-Edge Plunges, and the Landau–Widom Limit*, arXiv:2611.08401v1, first public 2026-11-05, https://arxiv.org/abs/2611.08401.
- R. M. Gray, *Toeplitz and Circulant Matrices: A Review*, Foundations and Trends in Communications and Information Theory, 2006; Fourier diagonalization of circulants and Toeplitz/circulant distinctions.
- M. Novakovíc, S. Singer and S. Singer, *Estimates for the spectral condition number of cardinal B-spline collocation matrices*, 2010; comparative B-spline collocation rather than the present sinc-power periodized covariance.
