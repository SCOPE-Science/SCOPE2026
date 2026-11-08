# Sharp second-order zero–two saturation for polynomially tangential normal contractions

## Finding
Let \(\alpha>1\), \(\kappa>0\), \(\eta\in\mathbb R\), and \(0<\delta<1\). Let \(f:[0,\delta]\to[0,\infty)\) be continuous, with \(f(0)=0\), \(f(t)>0\) for \(0<t\le\delta\), and
\[
f(t)=\kappa t^\alpha+\eta t^{2\alpha-1}+o(t^{2\alpha-1})\qquad(t\downarrow0).
\]
On \(H=L^2([0,\delta],dt)\), let \(N\) be multiplication by \(\lambda(t)=\exp(-f(t)+it)\). Put \(\varepsilon_n=n^{1-\alpha}\) and \(D_n=\|I-N^n\|\). Then
\[
\boxed{2-D_n=\kappa\pi^\alpha\varepsilon_n+
\left[\eta\pi^{2\alpha-1}-\kappa^2\left(\frac{\pi^{2\alpha}}2+\alpha^2\pi^{2\alpha-2}\right)\right]\varepsilon_n^2+o(\varepsilon_n^2).}
\]
For every choice \(t_n\in[0,\delta]\) attaining \(D_n\),
\[
\boxed{nt_n=\pi-2\kappa\alpha\pi^{\alpha-1}\varepsilon_n+o(\varepsilon_n).}
\]
The same contraction satisfies the exact power-difference asymptotic
\[
\boxed{\lim_{n\to\infty}n^{-(1-1/\alpha)}\|nN^{n-1}(I-N)\|=(\kappa\alpha)^{-1/\alpha}e^{-1/\alpha}.}
\]
In particular, \(D_n<2\) for each finite \(n\), but \(D_n\to2\); and \(N\) is power bounded but not Ritt. The first two terms of the zero–two deficit distinguish the radial second jet \(\eta\) from a universal negative phase-optimization correction.

## Assumptions and scope
The Hilbert space is complex. Multiplication is defined with respect to Lebesgue measure on the compact interval \([0,\delta]\); continuity ensures that its operator norms equal the maxima of the corresponding scalar functions, not merely upper bounds by their essential suprema. The hypotheses allow arbitrary oscillations of \(f\) consistent with the displayed two-term little-\(o\) expansion; no differentiability or monotonicity of \(f\) is assumed. The asymptotics concern integer \(n\to\infty\) with fixed \(\alpha,\kappa,\eta,f,\delta\). The quantity \(D_n\) is the ordinary operator norm, and the last display concerns \(\|nN^{n-1}(I-N)\|\), not the unscaled difference.

## Proof
**Scalar reduction.** Since \(N\) is multiplication by a continuous function of modulus at most one, it is a normal contraction and
\[
D_n=\max_{0\le t\le\delta}|1-e^{-nf(t)+int}|,\qquad
\|nN^{n-1}(I-N)\|=\max_{0\le t\le\delta}n e^{-(n-1)f(t)}|1-e^{-f(t)+it}|.
\]
Also \(\sigma(N)=\{\lambda(t):0\le t\le\delta\}\), so \(\sigma(N)\cap\{|z|=1\}=\{1\}\). For a fixed \(n\), the strict inequality \(|1-\lambda(t)^n|<2\) holds at every \(t\), hence by compactness \(D_n<2\).

**Leading phase location.** Take \(t=\pi/n\), which lies in \([0,\delta]\) for large \(n\). Then \(|1-\lambda(t)^n|=1+\exp(-nf(\pi/n))\). In particular, \(D_n\to2\) and
\[
2-D_n\le\kappa\pi^\alpha\varepsilon_n+O(\varepsilon_n^2)+o(\varepsilon_n^2).
\]
Choose a maximizer \(t_n\). Writing \(x_n=nf(t_n)\), the fact that \(|1-e^{-x_n+int_n}|\to2\) forces \(x_n\to0\) and forces the phase \(nt_n\) to approach an odd multiple of \(\pi\) modulo \(2\pi\). Positivity of \(f\) away from zero gives \(t_n\to0\), and \(nt_n\ge\pi-o(1)\). Since
\[
2-D_n\ge1-e^{-x_n},
\]
the displayed candidate estimate implies \(x_n=O(\varepsilon_n)\). The asymptotic \(f(t)\sim\kappa t^\alpha\) now gives
\[
\liminf_{n\to\infty}\frac{2-D_n}{\varepsilon_n}\ge\kappa\pi^\alpha.
\]
Together with the candidate upper estimate this proves \((2-D_n)/\varepsilon_n\to\kappa\pi^\alpha\). It also forces \(nt_n\to\pi\), since all other positive odd multiples are strictly more costly in the radial term, and a phase tending to infinity is impossible at this leading cost.

**Second-order optimization.** Write \(u=nt-\pi\), and let \(u_n=nt_n-\pi=o(1)\). Uniformly in \(u=o(1)\) with \(\pi+u>0\),
\[
x=n f((\pi+u)/n)=\kappa(\pi+u)^\alpha\varepsilon_n+
\eta(\pi+u)^{2\alpha-1}\varepsilon_n^2+o(\varepsilon_n^2).
\]
The scalar deficiency is
\[
\Delta_n(u)=2-|1+e^{-x+iu}|.
\]
Its Taylor expansion near \((x,u)=(0,0)\) begins with
\[
\Delta_n(u)=x-\frac{x^2}{2}+\frac{u^2}{4}+
O(x^3+xu^2+u^4).
\]
Comparison with \(u=0\), together with the positivity of the quadratic phase penalty, first gives \(u_n=O(\varepsilon_n)\): specifically, for small \(u\), the difference from \(\Delta_n(0)\) is bounded below by \(c u^2-C\varepsilon_n|u|-C\varepsilon_n^2+o(\varepsilon_n^2)\), with fixed \(c,C>0\). Since \(\Delta_n(u_n)\le\Delta_n(0)\), the quadratic inequality yields the claim.

It follows that, uniformly for \(|u|\le C\varepsilon_n\) with each fixed \(C\),
\[
\begin{aligned}
\Delta_n(u)={}&\kappa\pi^\alpha\varepsilon_n+
\left(\eta\pi^{2\alpha-1}-\frac{\kappa^2\pi^{2\alpha}}2\right)\varepsilon_n^2\\
&+\kappa\alpha\pi^{\alpha-1}\varepsilon_n u+\frac{u^2}4+o(\varepsilon_n^2)\\
={}&\kappa\pi^\alpha\varepsilon_n+
\left[\eta\pi^{2\alpha-1}-\kappa^2\left(\frac{\pi^{2\alpha}}2+\alpha^2\pi^{2\alpha-2}\right)\right]\varepsilon_n^2\\
&+\frac14\left(u+2\kappa\alpha\pi^{\alpha-1}\varepsilon_n\right)^2+o(\varepsilon_n^2).
\end{aligned}
\]
The trial value \(u=-2\kappa\alpha\pi^{\alpha-1}\varepsilon_n\) proves the matching upper bound for the minimum; applying the same square completion to an arbitrary maximizer gives the phase location \(u_n=-2\kappa\alpha\pi^{\alpha-1}\varepsilon_n+o(\varepsilon_n)\) and the claimed two-term deficiency law.

**Power-difference limit.** Since \(f(t)=o(t)\) and \(|1-e^{-f(t)+it}|/t\to1\), put \(t=x n^{-1/\alpha}\). For \(x\) in any fixed compact subset of \([0,\infty)\),
\[
n^{-(1-1/\alpha)}n e^{-(n-1)f(t)}|1-e^{-f(t)+it}|\longrightarrow x e^{-\kappa x^\alpha}
\]
uniformly. To justify taking maxima, choose \(t_0>0\) so that \(f(t)\ge\kappa t^\alpha/2\) and \(|1-e^{-f(t)+it}|\le2t\) for \(0<t<t_0\). For sufficiently large \(n\), the rescaled expression there is at most \(2x\exp(-\kappa x^\alpha/4)\), which tends to zero uniformly as \(x\to\infty\). On \([t_0,\delta]\), strict positivity of \(f\) gives exponential decay. Thus the maximum converges to \(\max_{x\ge0}x e^{-\kappa x^\alpha}\). Its unique positive maximizer is \(x=(\kappa\alpha)^{-1/\alpha}\), giving the stated constant. Finally, this unbounded normalized power difference when \(\alpha>1\) shows directly that the power-bounded contraction \(N\) is not Ritt.

## Verification
The exact scalar reductions and Taylor calculations are analytical. For finite corroboration, run `python checks/cusp_checker.py` with the dependency in `checks/requirements.txt`. The script evaluates high-precision local maximizing phases for three pairs of power-law jets, compares the inferred second-order coefficient and phase drift, and tests the scaled power-difference constant for two exponents. A successful run prints `TANGENTIAL_CUSP_FINITE_CORROBORATION_OK 8`. Numerical tests do not establish the global maximum or the infinite limit; these are proved above.

## Relationship to prior work
Borichev, Gomilko and Tomilov (arXiv:2607.10507, Section 6, especially Proposition 6.4 and Lemma 6.5) show that tangential spectral approach can saturate a norm-gap test and obstruct Ritt behavior. Their statements do not determine the finite-power saturation deficit, its second-order coefficient, or the drift of maximizing phase. Ng and Seifert (arXiv:2002.06236, Theorem 5.2) obtain general resolvent-based two-sided rate estimates for quasi-multiplication operators (including normal ones), but these estimates do not give the present two-term zero–two norm expansion or the exact leading constant for the scaled power difference. The classical Katznelson–Tzafriri theorem governs qualitative decay of the unscaled power difference. These antecedents motivate the pair of sharp quantitative diagnostics here. The originality assessment is necessarily subject to earlier formulations under different spectral-cusp terminology.

## Limitations
The theorem concerns a normal multiplication operator with an entire continuous spectrum curve parametrized by its argument. It does not assert the same constants for sparse diagonal spectra, arbitrary nonnormal operators, or general spectral sets containing additional curves. The second-order coefficient requires the stated two-term radial jet; a mere first-order asymptotic gives only the leading zero–two coefficient and the power-difference limit. Numerical corroboration is finite and independent mathematical audit has not been performed.

## References
1. A. Borichev, A. Gomilko, Yu. Tomilov, *Beurling--Kato theory, Hardy--Sobolev calculus and Ritt operators*, arXiv:2607.10507v1, first publicly posted 2026-07-11. https://arxiv.org/abs/2607.10507
2. A. C. S. Ng, D. Seifert, *Optimal rates of decay in the Katznelson–Tzafriri theorem for operators on Hilbert spaces*, arXiv:2002.06236, Journal of Functional Analysis 279 (2020), article 108799. https://arxiv.org/abs/2002.06236
3. D. Seifert, *Rates of decay in the classical Katznelson–Tzafriri theorem*, arXiv:1410.1297, Journal d'Analyse Mathématique 130 (2016), 329–354. https://arxiv.org/abs/1410.1297
4. Y. Katznelson, L. Tzafriri, *On power bounded operators*, Journal of Functional Analysis 68 (1986), 313–328. https://doi.org/10.1016/0022-1236(86)90101-1
