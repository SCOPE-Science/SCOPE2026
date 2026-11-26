# Uniform critical-window relaxation of periodized long-range Zeno walks

## Finding
For the periodized one-dimensional long-range jump generator defined below, the full nonzero spectral gap has a *uniform critical-window crossover*. Let \(p_N=3+z/\log N\), with fixed \(z\in\mathbb R\). For \(N\to\infty\), uniformly when \(z\) ranges over any fixed compact set \(K\subset\mathbb R\),
\[
\boxed{\operatorname{gap}(Q_{N,p_N})=\frac{4\pi^2\kappa\log N}{N^2}\left(\Phi(z)+O_K((\log N)^{-1})\right),\qquad
\Phi(z)=\begin{cases}(1-e^{-z})/z,&z\ne0,\\1,&z=0.\end{cases}}
\]
In particular, for the exactly marginal exponent \(p=3\), the first two finite-size terms are
\[
\boxed{\operatorname{gap}(Q_{N,3})=\frac{4\pi^2\kappa}{N^2}\left(\log N-\log(2\pi)+\frac32\right)+O(\kappa N^{-4}).}
\]
The gap occurs at Fourier wave numbers \(m=1,N-1\), for every \(N\ge3\) and every \(p>2\). The associated spectral relaxation time is the reciprocal of the gap; for a normalized squared population deviation the exponential decay time is its half. Thus the marginal spectral time is proportional to \(N^2/\log N\), not to \(N^2\log N\), for this explicitly periodized effective generator. The *newly assessed contribution* is the compact-uniform exponent-dependent crossover and its exact normalization, rather than the already-known existence of logarithmic acceleration at a fixed critical exponent.

## Assumptions and scope
Fix \(\kappa>0\), an integer \(N\ge3\), and \(p>2\). On \(\mathbb Z/N\mathbb Z\), define the continuous-time conservative Markov generator by
\[
(Q_{N,p}f)(j)=\kappa\sum_{r\in\mathbb Z\setminus\{0\}}\frac{f(j+r\bmod N)-f(j)}{|r|^p}.
\]
This **periodizes the infinite-lattice jump rates**, including every nonzero winding lift. The series converges absolutely. In the strong-dephasing limit of a Haken–Strobl chain with hopping proportional to \(J/r^\alpha\), its infinite-lattice effective rate has \(p=2\alpha\) and \(\kappa=2J^2/\gamma\); the *finite periodic-rate model itself* is precisely the mathematical object proved here. The generator is symmetric and has a unique uniform equilibrium; its spectral gap is the smallest positive eigenvalue of \(-Q_{N,p}\). We take \(p_N=3+z/\log N\) only for large enough \(N\) that \(p_N>2\). Constants implicit in \(O_K\) may depend on \(K\) but not on \(N,z\), or \(\kappa\).

## Proof
**1. Exact diagonalization.** Fourier characters \(f_m(j)=e^{2\pi i mj/N}\) diagonalize the translation-invariant matrix. The eigenvalue of \(-Q_{N,p}\) at \(m\) is
\[
\lambda_m=2\kappa\sum_{r=1}^{\infty}\frac{1-\cos(2\pi mr/N)}{r^p},\qquad 0\le m<N.
\]
The zero eigenvalue occurs only at \(m=0\), since the length-one jump rate is strictly positive. Set \(F_p(\theta)=\sum_{r\ge1}(1-\cos r\theta)/r^p\). For \(p>2\), termwise differentiation and the Laplace integral for \(r^{-(p-1)}\) yield
\[
F_p'(\theta)=\frac{\sin\theta}{\Gamma(p-1)}\int_0^\infty \frac{t^{p-2}e^{-t}}{1-2e^{-t}\cos\theta+e^{-2t}}\,dt>0
\]
for \(0<\theta<\pi\). Justification: first insert an Abel factor in the sine series, or integrate its positive geometrically summed kernel and apply dominated convergence. Since \(F_p(2\pi-\theta)=F_p(\theta)\), the smallest nonzero Fourier values are exactly \(m=1,N-1\).

**2. Exact marginal constant.** Abel summation of the logarithmic Fourier series gives, for \(0<\theta<2\pi\),
\[
F_3''(\theta)=\sum_{r\ge1}\frac{\cos(r\theta)}r=-\log(2\sin(\theta/2)).
\]
As \(\theta\downarrow0\), the right-hand side is \(-\log\theta+O(\theta^2)\). Integrate twice using \(F_3(0)=F_3'(0)=0\), obtaining
\[
F_3(\theta)=\frac{\theta^2}{2}\log(1/\theta)+\frac{3\theta^2}{4}+O(\theta^4).
\]
The substitution \(\theta=2\pi/N\) into \(\lambda_1=2\kappa F_3(\theta)\) proves the explicit two-term marginal formula.

**3. Uniform window.** Write \(\varepsilon=z/\log N\) with \(z\in K\). For \(\theta=2\pi/N\), split the Fourier sum at \(r=N\). Using \(2(1-\cos u)=u^2+O(u^4)\) for \(r\le N\),
\[
\lambda_1=\kappa\theta^2\sum_{r\le N}r^{-1-\varepsilon}+E_N,
\qquad |E_N|\le C_K\kappa N^{-2}.
\]
Indeed the Taylor remainder is bounded by \(C\kappa\theta^4\sum_{r\le N}r^{1-\varepsilon}=O_K(\kappa N^{-2})\); the discarded tail is at most \(4\kappa\sum_{r>N}r^{-3-\varepsilon}=O_K(\kappa N^{-2})\). The integral test, uniformly for bounded \(z\), gives
\[
\sum_{r\le N}r^{-1-z/\log N}=\int_1^N t^{-1-z/\log N}\,dt+O_K(1)
=\log N\,\Phi(z)+O_K(1).
\]
Substituting \(\theta^2=4\pi^2/N^2\) proves the uniform crossover. Positivity of \(\Phi\) permits inversion for the corresponding spectral relaxation time.

## Verification
The accompanying standalone `gap_check.py` requires Python 3 and `mpmath`. It uses high-precision Hurwitz-zeta matrix entries and a polylogarithm Fourier symbol to test the Fourier eigenvector equations for twelve finite generators; it tests marginal finite-size constants and the approach to \(\Phi(z)\) for positive, negative, and zero \(z\). Execute `python gap_check.py` after extracting this file. It reports `PASS 125 independent Fourier/matrix/asymptotic checks`; these computations are finite corroboration, **not** the proof of the infinite-\(N\) assertion. Proof of every assertion is analytical as above.

## Relationship to prior work
Catalano et al. (2022 preprint; 2023 journal) derive the long-range Haken–Strobl strong-dephasing generator (their equations 5–7) and study its relaxation. Their equation 12 gives a marginal \(N^2\log N\) time factor, whereas the exactly specified rate-periodized generator here has the inverse \(N^2/\log N\) factor. This observation is model-qualified: their finite simulations use open boundaries, and no assertion about the exact open-boundary quantum Liouvillian follows from this theorem. Gonçalves and Scotta (2020) *already established* \(N^2/\log N\) as the correct marginal hydrodynamic time scale for a related boundary-driven long-jump exclusion process. Bernardin et al. (2020/2022) study noncritical heavy-tailed, open, reservoir-coupled processes. Neither inspected treatment presents the **fixed-\(z\) uniform moving-exponent function** \(\Phi(z)\) as the exact spectral-gap crossover for the rate-periodized ring. Classical logarithmically divergent truncated second moments are standard; the result's specificity is its uniform coupling of spectral modes, normalization, and the \(p_N-3\sim1/\log N\) scale.

## Limitations
The generator periodizes **rates**, not coherent amplitudes before squaring, and cannot be identified with every finite-ring Haken–Strobl model. Quantum finite-dephasing corrections, many-particle spectral sectors, open boundaries, and total-variation mixing times are not treated. For large but finite \(N\), the crossover approximation has relative error of order \(1/\log N\), and the exact marginal expansion should be used for accurate critical numerical comparison. The fixed critical time scaling was known before; originality of the moving-exponent spectral crossover remains subject to independent literature assessment, including possible implicit versions in general regularly varying jump-kernel theory.

## References
1. A. G. Catalano et al., *Anomalous diffusion in the Long-Range Haken-Strobl-Reineker model*, arXiv:2212.07744v1 (15 December 2022), https://arxiv.org/abs/2212.07744 ; full text https://arxiv.org/html/2212.07744v2 .
2. P. Gonçalves and S. Scotta, *Diffusive to super-diffusive behavior in boundary driven exclusion*, arXiv:2004.03978v1 (8 April 2020), https://arxiv.org/abs/2004.03978 .
3. C. Bernardin, P. Cardoso, P. Gonçalves, and S. Scotta, *Hydrodynamic limit for a boundary driven super-diffusive symmetric exclusion*, arXiv:2007.01621, https://arxiv.org/html/2007.01621v3 .
