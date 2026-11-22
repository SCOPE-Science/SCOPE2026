# Oscillatory boundary concentration and a sharp cutoff trichotomy in harmonic Bergman spaces

## Finding
Fix an integer \(d\ge2\), real \(\lambda>-1\), and \(0\le\gamma<\lambda+2\). Let \(b^2_\lambda(\mathbb B_d)\) be the complex Hilbert space of harmonic functions on the real unit ball with radial weight proportional to \((1-|x|^2)^\lambda\). For \(0<\varepsilon<1\), let \(T_\varepsilon\) be the bounded Toeplitz compression of
\[
\psi_\varepsilon(x)=\mathbf1_{\{|x|^2\le1-\varepsilon\}}(1-|x|^2)^{-\gamma}\exp\!\left(\frac{i}{1-|x|^2}\right).
\]
There is a unique compact normal operator \(T\) whose restriction to each harmonic homogeneous-degree subspace agrees with the limit of the corresponding coefficients of \(T_\varepsilon\). The following conclusions hold.

**(i) Spectral cancellation.** On the degree-\(k\) spherical-harmonic subspace \(\mathcal H_k\), the scalar eigenvalue \(\mu_k\) satisfies, with \(m=k+d/2\), \(\beta=\lambda-\gamma\),
\[
\mu_k=\frac{\displaystyle\int_0^1 t^{m-1}(1-t)^\beta e^{i/(1-t)}\,dt}{B(m,\lambda+1)}
=\frac{e^i\Gamma(m)U(m,-\beta,-i)}{B(m,\lambda+1)},
\]
where the first integral is an improper oscillatory integral and \(U\) denotes Tricomi's confluent hypergeometric function (boundary value from \(\operatorname{Re}z>0\)). As \(k\to\infty\),
\[
\boxed{\mu_k=\frac{\sqrt\pi}{\Gamma(\lambda+1)}k^{(2\lambda+2\gamma+1)/4}
\exp\!\left(-\sqrt{2k}+i\left[\sqrt{2k}+\frac12-\frac{\pi(2\lambda-2\gamma+1)}8\right]\right)(1+o(1)).}
\]
Consequently \(T\) belongs to every Schatten class \(S_p\), \(p>0\), despite the fact that the untruncated symbol is not in weighted \(L^1\) whenever \(\gamma\ge\lambda+1\). If \(N_T(s)\) counts singular values strictly exceeding \(s\), with multiplicities, then
\[
\boxed{N_T(s)\sim\frac{2^{2-d}}{(d-1)!}\bigl(\log(1/s)\bigr)^{2(d-1)}\quad(s\downarrow0).}
\]

**(ii) Sharp cutoff topology.** The degree-wise limit is approached by the canonical radial cutoffs in exactly three ways:
\[
\begin{array}{ll}
0\le\gamma<1:&\displaystyle \|T_\varepsilon-T\|\asymp_{d,\lambda,\gamma}\varepsilon^{1-\gamma}\longrightarrow0;\\[2pt]
\gamma=1:& T_\varepsilon\to T\ \text{strongly, but not in operator norm};\\[2pt]
1<\gamma<\lambda+2:&\displaystyle \|T_\varepsilon\|\longrightarrow\infty,
\ \text{although each fixed mode converges to }\mu_k.
\end{array}
\]
At \(\gamma=1\), the middle regime is present for every \(\lambda>-1\). More precisely, in every stated regime the sharp lower bound
\[
\liminf_{\varepsilon\downarrow0}\varepsilon^{\gamma-1}\|T_\varepsilon-T\|
\ \ge\ \frac{(\lambda+1)^{\lambda+1}e^{-(\lambda+1)}}{\Gamma(\lambda+1)}>0
\]
holds (in the third regime this is a statement about its diverging norm difference). If \(\gamma\ge\lambda+2\), the individual unregularized radial moments cease to converge in the ordinary improper sense, so no such coefficientwise definition is asserted.

## Assumptions and scope
Use the normalized measure \(dV_\lambda=C_{d,\lambda}(1-|x|^2)^\lambda\,dx\), where \(C_{d,\lambda}\) makes the ball mass one. The projection \(P_\lambda\) is the \(L^2(dV_\lambda)\)-orthogonal projection onto \(b^2_\lambda\), and \(T_\varepsilon=P_\lambda M_{\psi_\varepsilon}|_{b^2_\lambda}\). All convergence is as \(\varepsilon\downarrow0\). The complex symbol is intentional: replacing it by its real part creates eigenvalue cancellations and changes the singular-value counting problem. The diagonal limit \(T\) is a uniquely determined bounded *mode-extension*; when \(\gamma>1\) it is not claimed to arise as a strong cutoff limit or as an everywhere-defined multiplication-compression operator.

## Proof
**1. Mode decomposition and sharp existence range.** Homogeneous harmonic polynomials of distinct degree are orthogonal for any radial measure. The radial substitution \(t=|x|^2\) gives the quotient of beta moments above, with \(m=k+d/2\). Setting \(u=1-t\), the numerator near \(u=0\) has amplitude \(u^\beta(1-u)^{m-1}\) and phase \(e^{i/u}\). With \(v=1/u\), the tail is \(\int^\infty v^{-\beta-2}e^{iv}(1-v^{-1})^{m-1}\,dv\). Dirichlet's test, or one integration by parts, proves ordinary convergence exactly if \(\beta>-2\), equivalently \(\gamma<\lambda+2\). At the endpoint \(\beta=-2\), the oscillating boundary term has nonzero modulus; for more negative \(\beta\), it grows. The substitution \(v=t/(1-t)\) identifies the exact Tricomi \(U\) expression by its defining integral and Abel boundary value.

**2. Sharp high-degree asymptotics.** Write the numerator as \(I_m=\int_0^1u^\beta(1-u)^{m-1}e^{i/u}\,du\). Split at \(u=m^{-1/3}\). On the remaining real segment the factor \((1-u)^{m-1}\) is exponentially small in \(m^{2/3}\). On the first segment, rotate the contour locally through angle \(-\pi/4\); the essential exponential decays at the rotated origin, and the connecting arc is exponentially negligible. Set \(u=m^{-1/2}z\). In the saddle region,
\[
(m-1)\log(1-u)+i/u=\sqrt m(-z+i/z)-z^2/2+O(m^{-1/2}(1+|z|^3)).
\]
The phase \(-z+i/z\) has a nondegenerate saddle at \(z_0=e^{-i\pi/4}\), with saddle value \(-2e^{-i\pi/4}\). The smooth perturbation \(e^{-z^2/2}\) evaluates to \(e^{i/2}\) at that saddle. The model integral is exactly \(2(-i/m)^{(\beta+1)/2}K_{\beta+1}(2\sqrt{-im})\), whose large-argument expansion on the ray of argument \(-\pi/4\) yields
\[
I_m\sim\sqrt\pi\,(-i)^{(2\beta+1)/4}m^{-(2\beta+3)/4}
\exp\!\left(-2\sqrt{-im}+i/2\right).
\]
The contour argument is valid for \(\beta>-2\): the rotated origin contributes no surviving endpoint term, and the saddle has Gaussian decay. Finally \(B(m,\lambda+1)\sim\Gamma(\lambda+1)m^{-\lambda-1}\) and \(m=k+O(1)\), giving (i). This proof uses a genuine complex saddle; applying absolute-value Laplace estimates first would discard the decisive cancellation.

**3. Multiplicities and counting.** The dimension of \(\mathcal H_k\) for \(k\ge1\) is
\[
h_{k,d}=\binom{k+d-1}{d-1}-\binom{k+d-3}{d-1}
\sim\frac{2}{(d-2)!}k^{d-2},
\]
where a binomial coefficient with negative upper index is interpreted as zero. Thus \(\sum_{k\le K}h_{k,d}\sim2K^{d-1}/(d-1)!\). The preceding asymptotic makes \(|\mu_k|\) eventually strictly decreasing, and \(\log(1/|\mu_k|)\sim\sqrt{2k}\). Solving for \(K\) and summing dimensions proves the counting law. The stretched exponential beats every polynomial multiplicity, proving all Schatten inclusions.

**4. Exact cutoff trichotomy.** Let \(\mu_{k,\varepsilon}\) denote the truncated beta quotient and \(E_{m,\varepsilon}=\int_0^\varepsilon u^\beta(1-u)^{m-1}e^{i/u}\,du\). Since \(e^{i/u}=iu^2\,\frac{d}{du}e^{i/u}\), integration by parts gives
\[
|E_{m,\varepsilon}|\le C\left[\varepsilon^{\beta+2}(1-\varepsilon)^{m-1}
+\int_0^\varepsilon u^{\beta+1}(1-u)^{m-1}du
+m\int_0^\varepsilon u^{\beta+2}(1-u)^{m-2}du\right].
\]
For \(\gamma\le1\), split at \(m\varepsilon=1\), use \(B(m,\lambda+1)^{-1}\asymp m^{\lambda+1}\) and standard incomplete gamma bounds. The supremum over \(k\) is \(O(\varepsilon^{1-\gamma})\). In particular, \(\gamma<1\) yields norm convergence, while at \(\gamma=1\) there is a uniform operator bound; coefficientwise convergence on the dense direct sum of \(\mathcal H_k\) then yields strong convergence.

For the reverse bound, take integers \(k_\varepsilon\) such that \(m_\varepsilon=k_\varepsilon+d/2\sim(\lambda+1)/\varepsilon\). Two integrations by parts (on the oscillatory tail, with \(m_\varepsilon\varepsilon\) bounded away from zero and infinity) give
\[
E_{m_\varepsilon,\varepsilon}=i\varepsilon^{\beta+2}(1-\varepsilon)^{m_\varepsilon-1}e^{i/\varepsilon}(1+O(\varepsilon)).
\]
The beta normalization therefore gives
\[
|\mu_{k_\varepsilon}-\mu_{k_\varepsilon,\varepsilon}|\sim
\frac{(\lambda+1)^{\lambda+1}e^{-(\lambda+1)}}{\Gamma(\lambda+1)}\varepsilon^{1-\gamma}.
\]
This proves the lower bound, the sharp norm rate for \(\gamma<1\), failure of norm convergence at \(\gamma=1\), and divergence of the cutoff norms for \(\gamma>1\) because \(\|T\|<\infty\). If a family of bounded operators converges strongly on the whole Hilbert space, the uniform boundedness principle forces bounded operator norms; hence strong convergence is impossible in the third regime.

## Verification
The accompanying `CHECK.py` evaluates the exact Tricomi representation, tests the complex saddle coefficient on multiple weights and exponents, checks harmonic-degree multiplicity identities, and compares finite cutoffs with the endpoint formula. Tests supply diagnostics only; they do not replace the analytic contour deformation, the uniform incomplete-gamma estimate, or the infinite-dimensional uniform boundedness argument.

## Relationship to prior work
Hagger–Liu–Taskinen–Virtanen, arXiv:2011.04699 (9 November 2020), proves general sufficient oscillatory-average criteria for bounded and compact harmonic Bergman Toeplitz operators, and illustrates unbounded radial symbols; those general existence phenomena are credited and **not** claimed as new here. The present statement isolates a specific singular chirp, resolves its full complex spectral asymptotic, its multiplicity-sensitive singular-value counting, and the sharp distinction between norm, strong-only, and coefficientwise-only radial truncation. Rozenblum, arXiv:1012.3528 (2010), treats spectral cancellation for bounded, predominantly compactly supported radial symbols and supplies earlier motivation for logarithmic spectral counting. Related public indexed work on the bounded cosine boundary chirp studies signed analytic Bergman eigenvalue counting; it covers the bounded oscillatory spectral phenomenon but not, in its available summary, the singular-amplitude cutoff trichotomy proved here.

## Limitations
The primary claim is about **complex radial phase** and ordinary cutoff limits in the harmonic Hilbert space. It does not claim a canonical Toeplitz multiplication domain for \(\gamma>1\). The cutoff thresholds do not imply the same topology for a different regularization; the nonintegrable range is \(\gamma\ge\lambda+1\) only. The exact complex-eigenvalue asymptotic is for fixed \(d,\lambda,\gamma\) and large degree, not uniform in changing parameters. Full historical priority in oscillatory Toeplitz spectral literature remains subject to independent review.

## References
- R. Hagger, C. Liu, J. Taskinen, J. A. Virtanen, *Toeplitz operators on the unit ball with locally integrable symbols*, arXiv:2011.04699, first posted 9 November 2020; Integral Equations and Operator Theory 94 (2022), article 17. https://arxiv.org/abs/2011.04699
- G. Rozenblum, *On lower eigenvalue bounds for Toeplitz operators with radial symbols in Bergman spaces*, arXiv:1012.3528, first posted 16 December 2010; J. Spectral Theory 1 (2011), 299–325. https://arxiv.org/abs/1012.3528
- NIST Digital Library of Mathematical Functions, Chapter 13 (Tricomi functions) and Chapter 10 (modified Bessel \(K\) asymptotics). https://dlmf.nist.gov/13 and https://dlmf.nist.gov/10
