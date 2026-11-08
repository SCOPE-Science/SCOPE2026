# Sharp two-grid phase staggering for causal exponential-derivative wavelet frames

## Finding
Fix a geometric scale ratio \(q>1\). Among all offsets \(0\leq\theta<1\) between two equal-gain geometric banks of the causal wavelet \(\psi_a(t)=a e^{-at}(1-at)\mathbf 1_{[0,\infty)}(t)\), the unique offset \(\theta=1/2\) simultaneously **maximizes the optimal lower semi-discrete frame bound** and **minimizes the optimal upper bound**. In particular it uniquely minimizes their ratio. This is an exact, nonasymptotic statement for every \(q>1\).

Put \(h=\log q\), \(L=h/2\), and define the absolutely convergent positive sums
\[
 A_*(q)=\frac14\sum_{j\in\mathbb Z}\operatorname{sech}^{2}((j+\tfrac12)L),\qquad
 B_*(q)=\frac14\sum_{j\in\mathbb Z}\operatorname{sech}^{2}(jL).
\]
These are exactly the optimally staggered sharp lower and upper bounds. If \(A(q,\theta)\), \(B(q,\theta)\) are the bounds at an arbitrary offset, then
\[
 A(q,\theta)\leq A_*(q),\quad B(q,\theta)\geq B_*(q),
\]
with *both inequalities strict* whenever \(\theta\ne1/2\) modulo one. For the optimal squared-bound condition number \(R_*(q)=B_*(q)/A_*(q)\),
\[
 R_*(q)\sim\frac{\sqrt q}{8}\quad(q\to\infty),\qquad
 R_*(q)-1\sim\frac{16\pi^2}{\log q}\exp\!\left(-\frac{2\pi^2}{\log q}\right)\quad(q\downarrow1).
\]
Thus half-step staggering reduces the sparse-scale conditioning growth from order \(q\) for a single grid to order \(\sqrt q\), while providing an explicitly exponentially near-tight two-bank frame at dense scales.

For an optional elliptic closed form, let \(k\in(0,1)\) be the unique modulus satisfying \(K(\sqrt{1-k^2})/K(k)=\pi/L\), where \(K\) and \(E\) denote complete elliptic integrals of first and second kind. Then
\[
 B_*(q)=\frac1{2L}-\frac{K(k)E(k)}{L^2}+\frac{K(k)^2}{L^2},\quad
 A_*(q)=\frac1{2L}-\frac{K(k)E(k)}{L^2}+\frac{K(k)^2(1-k^2)}{L^2}.
\]
The convergent hyperbolic sums above are preferable for numerical evaluation when \(q\) is close to one.

## Assumptions and scope
For every \(a>0\), let \(\psi_a(t)=a e^{-at}(1-at)\mathbf1_{[0,\infty)}(t)\). With the Fourier convention \(\widehat f(\omega)=\int_{\mathbb R}f(t)e^{-i\omega t}\,dt\), the two-bank analysis energy of \(f\in L^2(\mathbb R)\) is
\[
 \mathcal E_{q,\theta}(f)=\sum_{j\in\mathbb Z}\left(\|\psi_{q^j}*f\|_2^2+\|\psi_{q^{j+\theta}}*f\|_2^2\right).
\]
This is a *semi-discrete scale, continuously translated convolution frame*, not a discrete translation-lattice wavelet basis. The two channels count separately even at \(\theta=0\). The sharp constants \(A(q,\theta)\), \(B(q,\theta)\) are the best numbers in \(A\|f\|_2^2\leq\mathcal E_{q,\theta}(f)\leq B\|f\|_2^2\) simultaneously for all \(f\in L^2(\mathbb R)\). Frequencies \(\omega=0\) form a null set and do not affect the sharp essential infimum or supremum.

## Proof
**1. Exact Fourier reduction.** Direct integration gives \(\widehat{\psi_a}(\omega)=ia\omega/(a+i\omega)^2\), whence, for \(\omega\ne0\),
\[
 |\widehat{\psi_a}(\omega)|^2=\frac{a^2\omega^2}{(a^2+\omega^2)^2}=\frac14\operatorname{sech}^2(\log|\omega|-\log a).
\]
Put \(P_h(t)=\frac14\sum_{j\in\mathbb Z}\operatorname{sech}^2(t-jh)\). The frame multiplier is \(P_h(t)+P_h(t-\theta h)\), where \(t=\log|\omega|\). This positive continuous \(h\)-periodic function is bounded above and away from zero, and Plancherel yields its exact minimum and maximum as the frame bounds. These extrema are sharp by concentrating Fourier energy near any selected nonzero frequency.

**2. A strict periodic-unimodality lemma.** For every \(s>0\), \(P_s\) is even and \(s\)-periodic, with a unique maximum modulo \(s\) at \(t=0\), a unique minimum modulo \(s\) at \(t=s/2\), and strictly decreases on \((0,s/2)\). Here is an analytic proof (not a finite sampling argument). Fourier transformation and Poisson summation give the absolutely convergent series
\[
 P_s(t)=\frac1{2s}+\frac{\pi^2}{s^2}\sum_{n=1}^{\infty}\frac{n\cos(2\pi nt/s)}{\sinh(\pi^2n/s)}.
\]
For the unique \(k\in(0,1)\) with \(K(\sqrt{1-k^2})/K(k)=\pi/s\), the standard Fourier expansion of the Jacobi elliptic \(\operatorname{dn}^2\) (NIST DLMF 22.11.13, using \(\operatorname{dn}^2=1-k^2\operatorname{sn}^2\)) gives the exact identity
\[
 P_s(t)=\frac1{2s}-\frac{K(k)E(k)}{s^2}+\frac{K(k)^2}{s^2}\operatorname{dn}^2\!\left(\frac{2K(k)t}{s},k\right).
\]
Since \(\partial_u\operatorname{dn}^2(u,k)=-2k^2\operatorname{sn}(u,k)\operatorname{cn}(u,k)\operatorname{dn}(u,k)<0\) for \(0<u<K(k)\), the asserted strict monotonicity follows. Existence and uniqueness of \(k\) follow from the standard continuous strict decrease of \(K(\sqrt{1-k^2})/K(k)\) from infinity to zero.

**3. Unique simultaneous optimum.** By reflection, it suffices to take \(0\leq\theta\leq1/2\). For \(\theta=1/2\), merging the two scale grids gives \(P_h(t)+P_h(t-h/2)=P_{h/2}(t)\). Step 2 therefore gives \(A_*=P_{h/2}(h/4)=2P_h(h/4)\), and \(B_*=P_{h/2}(0)=P_h(0)+P_h(h/2)\). For \(0\leq\theta<1/2\), evaluate the frame multiplier at the midpoint of the *longer* circular scale gap, \(t=(1+\theta)h/2\). Evenness and periodicity give there the value \(2P_h((1-\theta)h/2)\), which is strictly less than \(2P_h(h/4)=A_*\). Thus \(A(q,\theta)<A_*\). At \(t=0\) the multiplier has value \(P_h(0)+P_h(\theta h)>P_h(0)+P_h(h/2)=B_*\), so \(B(q,\theta)>B_*\). Reflection treats \(1/2<\theta<1\). These strict inequalities prove simultaneous extremality and the unique condition-ratio optimum.

**4. Sharp scale-spacing limits.** Write \(L=(\log q)/2\). As \(L\to\infty\), the two nearest terms in the lower sum and the central term in the upper sum give \(A_*=2e^{-L}(1+O(e^{-L}))\), \(B_*=\tfrac14(1+O(e^{-2L}))\); geometrically dominated tails justify the errors. Therefore \(R_*\sim e^L/8=\sqrt q/8\). As \(L\downarrow0\), Poisson summation from Step 2 gives uniformly
\[
 P_L(t)=\frac1{2L}+\frac{\pi^2}{L^2\sinh(\pi^2/L)}\cos(2\pi t/L)+O\!\left(\frac{e^{-2\pi^2/L}}{L^2}\right).
\]
Evaluating at the proved maximum and minimum yields
\[
 R_*-1\sim\frac{4\pi^2}{L\sinh(\pi^2/L)}\sim\frac{8\pi^2}{L}e^{-\pi^2/L}
 =\frac{16\pi^2}{\log q}\exp(-2\pi^2/\log q).
\]
This completes the claims.

## Verification
Execute `python CHECK.py` with Python 3 and mpmath. It verifies Fourier transforms by quadrature, the Poisson and elliptic formulas, direct scale-grid energy sums, strict staggering comparisons on sampled grids, and approach to the two asymptotic regimes. The code is corroborative: the proof of global extrema, universal \(q\), all offsets, and asymptotic limits is analytical in the preceding section.

## Relationship to prior work
Pedersen, Lindeberg and Gerstoft (arXiv:2609.17201, first public September 15, 2026) provide the motivating analysis of time-causal difference-of-exponentials (DoE), difference-of-limit-kernels (DoT) and related bandpass banks. Their full text, specifically Sections 3–5 and equations (12), (21)–(23), (26)–(31), computes sharp **finite-bank** frequency-domain bounds including a low-pass residual and scale-spacing tradeoffs. The DoE generator is a *finite difference of two truncated exponentials*, whereas the current \(\psi_a\) is a normalized logarithmic-scale derivative of one truncated exponential. Neither the two simultaneous offset geometric banks over all integer levels nor an offset-maximin theorem and the present exact elliptic/boundary constants occur in those results. The finite-bank single-lattice statements do not imply the two-bank phase optimizer.

The companion arXiv:2605.09770, Sections II-B and III-B–C, treats finite DoE/DoT scale-bank reconstruction, encoding and channel frame geometry, not an offset-optimization over the stated differentiable exponential family. Lindeberg (2026) considers derivatives of infinite-cascade time-causal limit kernels, not the present one-exponential differentiated kernel. Standard Calderón/Plancherel frame-multiplier reductions, Poisson summation and the Jacobi elliptic formula (DLMF 22.11.13) are classical, and are not claimed as new.

Hardin, Kendall and Saff (2013, Theorem 1) prove an equally-spaced maximin-polarization result for strictly convex nonincreasing *geodesic potential kernels*. It does not apply to the present \(P_h\), which is strictly concave near its maximum: the elliptic identity in Step 2 gives \(P_h''(0)<0\). Moreover that theorem is for the lower extremum, not the simultaneous sharp upper/lower wavelet bounds and sparse/dense asymptotics. This distinction and possible unidentified general two-point potential results are retained as originality risks.

## Limitations
The analysis uses **all** integer scales and continuous translation energy on \(L^2(\mathbb R)\). Finite filter banks, sampled translations, truncation, and noise quantization require separate edge/alias corrections. The ratio refers to squared frame bounds, not the Euclidean condition number of a finite matrix. Although the full text of the closest source arXiv:2609.17201 was inspected, an equivalent calculation in older special-function or frame-optimization literature may remain unindexed; publication priority is not independently certified. No independent scientific validation has been performed.

## References
- J. E. Pedersen, T. Lindeberg and P. Gerstoft, *Frame bounds and bandwidth tiling for time-causal bandpass wavelets*, arXiv:2609.17201 (first posted 2026-09-15). https://arxiv.org/abs/2609.17201
- J. E. Pedersen, T. Lindeberg and P. Gerstoft, *Encoding and Decoding Temporal Signals with Spiking Bandpass Wavelets*, arXiv:2605.09770 (first posted 2026-05-10). https://arxiv.t3mt.com/html/2605.09770v2
- T. Lindeberg, *Time-causal and time-recursive wavelets*, Frontiers in Signal Processing (2026), DOI:10.3389/frsip.2026.1786202. https://www.frontiersin.app/articles/frsip-2026-1786202
- I. Daubechies, *Ten Lectures on Wavelets*, SIAM (1992), Chapter 3 (general frame bounds; background reference).
- D. P. Hardin, A. P. Kendall and E. B. Saff, *Polarization optimality of equally spaced points on the circle for discrete potentials*, Discrete Comput. Geom. 50 (2013), 236–243; arXiv:1208.5261. https://arxiv.org/html/1208.5261v3
- NIST Digital Library of Mathematical Functions, Section 22.11, Eq. 22.11.13 (Fourier series for Jacobi elliptic squares). https://dlmf.nist.gov/22.11
