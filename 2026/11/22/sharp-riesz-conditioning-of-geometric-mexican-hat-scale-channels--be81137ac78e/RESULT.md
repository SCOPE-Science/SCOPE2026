# Sharp Riesz conditioning of geometric Mexican-hat scale channels in every dimension

## Finding

Fix an integer \(d\ge1\) and \(h>0\). Write the Euclidean heat kernel as
\[
H_t(x)=(4\pi t)^{-d/2}\exp(-|x|^2/(4t)),\qquad x\in\mathbb R^d,\quad t>0,
\]
and let \(\psi_t=\Delta H_t\), \(\phi_j=\psi_{e^{jh}}/\|\psi_{e^{jh}}\|_2\) for every integer \(j\). Put \(\nu=(d+4)/2\). **The normalized unshifted Mexican-hat/LoG channels form a Riesz sequence for every logarithmic spacing** \(h>0\), with exactly the following optimal *squared* bounds:
\[
A_d(h)=1+2\sum_{k=1}^\infty(-1)^k\operatorname{sech}^{\nu}(kh/2),\qquad
B_d(h)=1+2\sum_{k=1}^\infty\operatorname{sech}^{\nu}(kh/2).
\]
Both are strictly positive and finite; neither can be improved uniformly for finitely supported coefficient sequences. In particular the unique frequency maximizing the Gram symbol is \(0\), and its unique minimizing frequency is \(\pi\), modulo \(2\pi\), for **every** \(d\ge1\) and \(h>0\).

The exact Gram symbol has an alternative, strictly positive periodized-Gamma representation:
\[
F_{\nu,h}(\theta)=\sum_{k\in\mathbb Z}\operatorname{sech}^{\nu}(kh/2)e^{ik\theta}
=\frac{2^\nu}{h\Gamma(\nu)}\sum_{m\in\mathbb Z}
\left|\Gamma\!\left(\frac\nu2+i\frac{\theta+2\pi m}{h}\right)\right|^2.
\]
For fixed \(h\), raising the dimension strictly increases \(A_d(h)\) and strictly decreases \(B_d(h)\). For fixed \(d\), as \(h\downarrow0\),
\[
\begin{aligned}
A_d(h)&\sim\frac{2^{\nu+2}\pi^\nu}{\Gamma(\nu)}h^{-\nu}e^{-\pi^2/h},\\
B_d(h)&\sim\frac{2^\nu\Gamma(\nu/2)^2}{\Gamma(\nu)}h^{-1},\\
\frac{B_d(h)}{A_d(h)}&\sim
\boxed{\frac{\Gamma(\nu/2)^2}{4\pi^\nu}\,h^{\nu-1}e^{\pi^2/h}}.
\end{aligned}
\]
The ratio is the sharp Gram-condition number, or equivalently the sharp ratio of squared synthesis bounds. For \(d=2\), its asymptotic coefficient is \(1/(16\pi^2)\) multiplying \(h^2e^{\pi^2/h}\). The same bounds are sharp when scales are indexed only by the nonnegative integers.

## Assumptions and scope

Everything takes place in \(L^2(\mathbb R^d,dx)\) with its usual inner product, no translations and a single scale center. \(d\) is a positive integer, \(h\) an arbitrary positive real, and \(\Delta\) the usual spatial Laplacian. The Fourier transform uses \(\widehat f(\xi)=\int_{\mathbb R^d}f(x)e^{-ix\cdot\xi}\,dx\), with inverse Plancherel weight \((2\pi)^{-d}\). The Riesz inequalities are
\[
A_d(h)\sum_j|c_j|^2\le \left\|\sum_jc_j\phi_j\right\|_2^2\le B_d(h)\sum_j|c_j|^2
\]
for every finitely supported complex coefficient sequence. Strict monotonicity in dimension compares fixed \(h\) and any two integers \(1\le d_1<d_2\). Dense-scale asymptotics hold for each fixed dimension as \(h\downarrow0\), with no joint limit in \(d\). No assertion of completeness or a full translation–dilation frame is made.

## Proof

**1. The exact scale Gram kernel.** Since \(\widehat{\psi_t}(\xi)=-|\xi|^2e^{-t|\xi|^2}\), polar integration and Plancherel give
\[
\langle\psi_t,\psi_s\rangle
=\frac{|\mathbb S^{d-1}|\Gamma(\nu)}{2(2\pi)^d(t+s)^\nu},
\qquad \nu=\frac d2+2.
\]
Dividing by the norms at \(t\) and \(s\), using the same formula at \(t=s\), yields exactly
\[
\frac{\langle\psi_t,\psi_s\rangle}{\|\psi_t\|_2\|\psi_s\|_2}
=\left(\frac{2\sqrt{ts}}{t+s}\right)^\nu
=\operatorname{sech}^{\nu}\!\left(\frac{\log t-\log s}{2}\right).
\]
Hence the full Gram operator is bilateral Toeplitz convolution with entries \(g_{j-k}=\operatorname{sech}^{\nu}((j-k)h/2)\). They decay exponentially for fixed \(h\), so its symbol \(F_{\nu,h}\) is real-analytic, even and continuous.

**2. Gamma periodization and strictly monotone symbol.** The standard beta substitution \(u=e^x\) establishes, without relying on frame theory,
\[
\int_{\mathbb R}\operatorname{sech}^\nu(x/2)e^{-iyx}\,dx
=\frac{2^\nu}{\Gamma(\nu)}\Gamma\!\left(\frac\nu2+iy\right)\Gamma\!\left(\frac\nu2-iy\right).
\]
Fourier periodization/Poisson summation (valid since the function and transform decay exponentially) gives the Gamma formula in the finding. Every summand is positive and their sum converges uniformly; thus \(F_{\nu,h}(\theta)>0\) at every frequency.

It remains essential to locate the true minimum rather than assume it is \(\pi\). Write \(a=\nu/2>0\). The Euler–Weierstrass Gamma product gives
\[
\frac{|\Gamma(a+iy)|^2}{\Gamma(a)^2}
=\prod_{n=0}^\infty \left(1+\frac{y^2}{(a+n)^2}\right)^{-1}.
\]
Let \(X_n\) be independent exponentials of respective rates \((a+n)^2\), and \(S=\sum_{n=0}^\infty X_n\). Then \(S>0\) almost surely and \(\mathbb E S=\sum_{n\ge0}(a+n)^{-2}<\infty\). Laplace transforms of finite partial sums and dominated convergence imply
\[
|\Gamma(a+iy)|^2=\Gamma(a)^2\,\mathbb E\,e^{-Sy^2}.
\]
Consequently \(F_{\nu,h}\) is a strictly positive mixture of wrapped Gaussian functions
\[
P_b(\theta)=\sum_{m\in\mathbb Z}\exp\!\left[-b(\theta+2\pi m)^2\right],
\qquad b=S/h^2>0.
\]
For **every** \(b>0\), Poisson summation gives
\[
P_b(\theta)=\frac1{2\pi}\sqrt{\frac\pi b}\,\vartheta_3\!\left(\frac\theta2,e^{-1/(4b)}\right).
\]
The Jacobi triple product writes the theta function, for \(0<q<1\), as
\[
\vartheta_3(\theta/2,q)=\prod_{n=1}^\infty(1-q^{2n})
\big(1+2q^{2n-1}\cos\theta+q^{4n-2}\big).
\]
Each positive angle-dependent factor is strictly decreasing on \((0,\pi)\); differentiating its logarithm yields a negative term \(-2q^{2n-1}\sin\theta/(1+2q^{2n-1}\cos\theta+q^{4n-2})\). Uniform convergence on compact angle intervals justifies the conclusion. Therefore each \(P_b\), and hence their positive mixture \(F_{\nu,h}\), is **strictly decreasing** from \(0\) to \(\pi\). Periodicity and evenness imply the asserted unique spectral extrema.

**3. Exact and sharp Riesz bounds.** For finite coefficients let \(C(\theta)=\sum_j c_je^{ij\theta}\). The Gram identity gives
\[
\left\|\sum_jc_j\phi_j\right\|_2^2
=\frac1{2\pi}\int_{-\pi}^{\pi}F_{\nu,h}(\theta)|C(\theta)|^2\,d\theta.
\]
Positivity and the strict extrema from Step 2 give the inequalities. To see sharpness, use normalized Dirichlet polynomials supported on \(0\le j<N\), with arbitrary frequency modulation: their squared moduli are Fejér kernels converging weakly to the point mass at the specified frequency. This argument works both for \(j\in\mathbb Z\) and \(j\ge0\). Substituting \(0\) and \(\pi\) into the Fourier series yields the stated alternating and ordinary sums.

**4. Strict dimension improvement.** For \(\delta>0\), write \(g_{\nu+\delta}(k)=g_\nu(k)g_\delta(k)\). Multiplication of Fourier coefficients is circular convolution of symbols:
\[
F_{\nu+\delta,h}(\theta)=\frac1{2\pi}\int_{-\pi}^\pi F_{\nu,h}(\theta-u)F_{\delta,h}(u)\,du.
\]
Here \(F_{\delta,h}(u)>0\) everywhere and \((2\pi)^{-1}\int F_{\delta,h}=g_\delta(0)=1\); hence it is a full-support probability density. Since \(F_{\nu,h}\) is not constant, averaging strictly raises its minimum and strictly lowers its maximum. Increasing dimension raises \(\nu\), proving both strict claims.

**5. Sharp dense-scale asymptotics.** The Gamma formula at \(\theta=0\) has the single nearest periodization index \(m=0\), so for fixed \(\nu\),
\[
B_d(h)=\frac{2^\nu\Gamma(\nu/2)^2}{h\Gamma(\nu)}(1+o(1)).
\]
At \(\theta=\pi\), exactly two nearest indices, \(m=0,-1\), dominate. Stirling's fixed-real-part formula
\[
|\Gamma(a+iy)|^2=2\pi |y|^{2a-1}e^{-\pi|y|}(1+O_a(|y|^{-1}))
\]
at \(|y|=\pi/h\) gives
\[
A_d(h)\sim\frac{2^\nu}{h\Gamma(\nu)}\cdot 2\cdot 2\pi
\left(\frac\pi h\right)^{\nu-1}e^{-\pi^2/h},
\]
which equals the displayed \(A_d\) law. Terms with \(|\theta+2\pi m|\ge3\pi\) are exponentially negligible relative to the nearest pair, uniformly for small \(h\). Division gives the condition-number coefficient. Finally \(\operatorname{sech}(kh/2)\to0\) uniformly summably over \(k\ge1\) as \(h\to\infty\), so \(A_d(h),B_d(h)\to1\).

## Verification

The accompanying standalone `CHECK.py` recomputes the kernel coefficients and the Gamma periodization, independently checks spectral endpoints and strict sampled monotonicity, verifies dimension monotonicity at fixed spacing, and tests the analytic asymptotic constants without using cancellation-prone alternating sums at small spacing. The script uses Python, NumPy and SciPy and prints its actual successful test count. Run `python CHECK.py` from the directory containing the files. **Finite tests do not prove** positivity for a continuum of frequencies, uniqueness of the extrema, or any infinite-dimensional limit: these follow from Steps 2–5.

## Relationship to prior work

Fukuda, Kinoshita and Yoshino (first publicly available online 18 May 2017), Section 4, explicitly work with the Mexican-hat wavelet and calculate its Fourier representation and continuous wavelet transform. Their scope is Gelfand–Shilov continuity, not the all-dimensional normalized scale-only Gram spectrum or sharp dense-scale Riesz conditioning developed here. Antezana, Carando and Scotti (arXiv version 1, 14 October 2021) analyze Riesz conditions for **integer** dilation families using Dirichlet series; their function space and dilation model do not identify the present logarithmically spaced Euclidean heat derivatives or their Gamma periodization.

Earlier work by Bui and Laugesen on Mexican-hat frequency-scale frames concerns full translated/dilated analysis frames, not this exact unshifted coefficient-conditioned sequence; only its abstract and an author talk were accessible for this comparison, so implicit overlap remains a historical risk. A published result on **causal differences of exponential smoothing channels** also yields a Mellin–Toeplitz symbol and an exponentially bad small-spacing condition number, but its overlap sequence, Gamma factors, leading power and constants differ. In particular it does not imply the strict all-dimensional LoG mode-extremum and dimension-monotonicity statements. The classical beta/Gamma, Jacobi product and Fourier–Toeplitz tools are openly credited; the new mathematical content claimed is their exact combination and sharp constants for this concrete motivated family, not the individual general-purpose identities.

## Limitations

The functions are all centered at the spatial origin; a Riesz sequence of dilates is **not** a complete wavelet frame for all signals, and the bounds are not the frame bounds of a translated filter bank. The condition number refers to coefficient synthesis on the closed span of these channels, not the condition number of a numerical discretization. The two-sided infinite sequence and the one-sided sequence have the same optimal uniform bounds, but finite truncations generally have different eigenvalues. The dimension-asymptotic regime is not studied. The published literature comparison cannot establish absolute historical priority, especially where classical Mellin and theta identities might be incorporated indirectly into frame theory.

## References

1. N. Fukuda, T. Kinoshita and K. Yoshino, *Wavelet transforms on Gelfand–Shilov spaces and concrete examples*, Journal of Inequalities and Applications 2017, article 119. First public online 18 May 2017. https://doi.org/10.1186/s13660-017-1393-0 (full text, especially §4 and Remark 4.1).
2. J. Antezana, D. Carando and M. Scotti, *Splitting the Riesz basis condition for systems of dilated functions through Dirichlet series*, arXiv:2110.07659, first public version 14 October 2021. https://arxiv.org/abs/2110.07659 (especially §§1–2 and 4–5).
3. H. Q. Bui and R. S. Laugesen, *Frequency-scale frames and the solution of the Mexican hat problem*, Constructive Approximation 33 (2011), 163–189, https://doi.org/10.1007/s00365-010-9098-3 (abstract accessible; full text not inspected).
4. *Sharp dense-scale conditioning of causal exponential-difference dilates*, publicly accessible 2026 mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-sharp-dense-scale-conditioning-of-causal-exponential-difference--665865eb3d5b (full result and proof read for scientific overlap comparison).
5. Classical Euler–Weierstrass Gamma product, Poisson summation, Jacobi triple product and Stirling expansion, applied explicitly in the proof.
