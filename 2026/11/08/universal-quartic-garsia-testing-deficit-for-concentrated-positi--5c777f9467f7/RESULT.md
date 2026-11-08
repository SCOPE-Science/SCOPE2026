# Universal quartic Garsia-testing deficit for concentrated positive moment Hankel operators

## Finding
Let \(\nu\) be a Borel probability measure supported on \([0,R]\), where \(0<R<\infty\), and write \(m=\int s\,d\nu(s)\), \(q=\int s^2\,d\nu(s)\), \(V=q-m^2\). For \(0<\varepsilon<R^{-1}\), let the compact positive Hankel operator \(H_\varepsilon\) on complex Hardy \(H^2(\mathbb D)\) have matrix
\[
\langle H_\varepsilon e_j,e_i\rangle=\varepsilon^{i+j}\int_0^R s^{i+j}\,d\nu(s),\qquad i,j\ge0.
\]
With normalized Szegő kernels \(k_a(z)=\sqrt{1-|a|^2}/(1-\bar a z)\), put
\[
N_\varepsilon=\|H_\varepsilon\|,\qquad Q_\varepsilon=\sup_{a\in\mathbb D}\|H_\varepsilon k_a\|.
\]
Then, for every such probability measure,
\[
\boxed{\lim_{\varepsilon\downarrow0}\varepsilon^{-4}(N_\varepsilon-Q_\varepsilon)=\frac12 V^2.}
\]
If \(V>0\), the leading coefficient is strictly positive. A maximizing kernel can be chosen with real nonnegative parameter \(a_\varepsilon\), and any such maximizer satisfies \(a_\varepsilon=\varepsilon m+o(\varepsilon^2)\). If \(V=0\), the measure is a point mass and \(N_\varepsilon=Q_\varepsilon\) for every admissible \(\varepsilon\). In particular, the first universal nonzero loss of sharp kernel testing is quartic in the concentration scale, and depends only on the *variance squared*, not on higher moments.

## Assumptions and scope
The measure is fixed as \(\varepsilon\downarrow0\), positive, of mass one, and supported on a fixed bounded interval of nonnegative reals. We identify \(H^2(\mathbb D)\) with \(\ell^2(\mathbb N_0)\) through monomials \(e_j(z)=z^j\). The operator is the positive moment matrix induced by the pushforward of \(\nu\) under \(s\mapsto\varepsilon s\); composing with the canonical unitary from analytic to antianalytic Hardy coordinates gives the usual Hankel-operator interpretation. This is a small-concentration asymptotic, not a uniform remainder over all probability measures or a claim for noncompact operators.

## Proof
**Step 1: compact positive model.** Put \(v_t=(1,t,t^2,\ldots)\) for \(0\le t<1\). Then \(H_\varepsilon=\int v_{\varepsilon s}\otimes v_{\varepsilon s}\,d\nu(s)\), a positive trace-class operator with \(\operatorname{tr}H_\varepsilon=\int(1-\varepsilon^2s^2)^{-1}d\nu(s)\). Its matrix entries are nonnegative. Therefore replacing a complex kernel parameter by its modulus cannot decrease the test norm: \(\|H_\varepsilon k_a\|\le\|H_\varepsilon k_{|a|}\|\). Compactness and weak convergence of \(k_a\) to zero as \(|a|\uparrow1\) ensure an interior maximizer.

**Step 2: isolated top eigenvector.** As \(\varepsilon\to0\), \(H_\varepsilon\to e_0\otimes e_0\) in operator norm, analytically for \(|\varepsilon|R<1\). For small positive \(\varepsilon\), its largest eigenvalue \(\lambda_\varepsilon=N_\varepsilon\) is simple. Choose its unit eigenvector \(u_\varepsilon\) with positive zeroth coordinate. Analytic perturbation or direct coefficient equations yield, in \(\ell^2\),
\[
u_\varepsilon=e_0+\varepsilon m e_1+\varepsilon^2\left(qe_2-\frac{m^2}{2}e_0\right)+O(\varepsilon^3),\quad
\lambda_\varepsilon=1+\varepsilon^2m^2+O(\varepsilon^3).
\]
The rest of the positive spectrum is bounded by \(C\varepsilon^2\): by min--max it is at most the operator norm of the compression to \(e_0^\perp\), which is bounded by \(\int\sum_{j\ge1}(\varepsilon s)^{2j}d\nu(s)=O(\varepsilon^2)\).

**Step 3: test manifold and minimizing parameter.** At the natural candidate \(a=\varepsilon m\), the normalized kernel expands as
\[
k_{\varepsilon m}=e_0+\varepsilon m e_1+\varepsilon^2\left(m^2e_2-\frac{m^2}{2}e_0\right)+O(\varepsilon^3).
\]
Hence the squared distance of this kernel from \(u_\varepsilon\) is \(\varepsilon^4 V^2+o(\varepsilon^4)\). For any real kernel parameter \(a\), write \(d(a)^2=1-|\langle k_a,u_\varepsilon\rangle|^2\). Spectral decomposition, with the nonleading spectrum \(O(\varepsilon^2)\), gives whenever \(d(a)=O(\varepsilon^2)\),
\[
\lambda_\varepsilon-\|H_\varepsilon k_a\|=\tfrac12d(a)^2+o(\varepsilon^4).
\]
Testing at \(\varepsilon m\) shows \(N_\varepsilon-Q_\varepsilon=O(\varepsilon^4)\). The spectral gap then forces every maximizing real \(a_\varepsilon\) to obey \(d(a_\varepsilon)=O(\varepsilon^2)\), hence \(a_\varepsilon=\varepsilon m+O(\varepsilon^2)\). Write \(a_\varepsilon=\varepsilon m+b_\varepsilon\varepsilon^2\), where \(b_\varepsilon\) is bounded. The first three kernel coordinates and the expansion of \(u_\varepsilon\) give, uniformly for bounded \(b_\varepsilon\),
\[
d(a_\varepsilon)^2=\varepsilon^4\left(V^2+b_\varepsilon^2\right)+o(\varepsilon^4).
\]
The comparison with \(a=\varepsilon m\) forces \(b_\varepsilon\to0\) and produces the displayed sharp limit.

**Step 4: zero-variance boundary.** If \(V=0\), positivity implies \(\nu=\delta_m\). Then \(H_\varepsilon=v_{\varepsilon m}\otimes v_{\varepsilon m}\) and \(k_{\varepsilon m}\) exactly norms this rank-one operator, so the difference vanishes identically.

## Verification
`verify.py` is a standalone standard-library finite-section diagnostic. It computes the top eigenvalue by positive power iteration, maximizes the kernel norm on a real interval using golden-section search, and checks the predicted coefficients for \(\nu=(\delta_0+\delta_1)/2\) and for uniform measure on \([0,1]\). Its 20 assertions passed. The exact expected constants are \(1/32\) and \(1/288\), respectively. Numerical finite sections are not an infinite-dimensional proof; the preceding perturbation and spectral-gap argument is the proof.

## Relationship to prior work
Dyakonov, *The strong reproducing kernel thesis for Hankel operators and the Garsia norm* (2026, arXiv:2609.33242, **version 3**), including its addendum, already identifies every compact Hankel operator satisfying exact strong kernel testing. In particular, *qualitative failure* for nontrivial positive moment mixtures is covered by that more general classification and is not claimed here as new. Chatzifountas, Girela and Peláez, *A generalized Hilbert matrix acting on Hardy spaces* (arXiv:1309.6125), establish the positive moment-Hankel framework and qualitative compactness and Schatten criteria. The statement here instead determines a sharp, universal **fourth-order quantitative defect**, with an explicit coefficient across all compactly supported positive probability measures. Existing finite-rank strong-kernel classifications and one-symbol Hilbert-matrix norm gaps do not themselves imply this local variance-squared asymptotic.

## Limitations
The result does not cover arbitrary nonpositive measures, concentrations around points other than zero, or noncompact families with support reaching the unit circle. No uniform error estimate over all probability measures is asserted. The quantitative novelty comparison is best-knowledge and may be affected by an older general stability theorem for norming vector manifolds; independent mathematical review and publication-priority confirmation have not been performed.

## References
1. K. M. Dyakonov, *The strong reproducing kernel thesis for Hankel operators and the Garsia norm*, arXiv:2609.33242v3 (2026), https://arxiv.org/abs/2609.33242.
2. C. Chatzifountas, D. Girela and J. Á. Peláez, *A generalized Hilbert matrix acting on Hardy spaces*, arXiv:1309.6125 (2013), https://arxiv.org/abs/1309.6125.
3. O. F. Brevig and K. Seip, *Maximal norm Hankel operators*, *J. Math. Anal. Appl.* 529 (2024), 127221; arXiv:2301.07937.
