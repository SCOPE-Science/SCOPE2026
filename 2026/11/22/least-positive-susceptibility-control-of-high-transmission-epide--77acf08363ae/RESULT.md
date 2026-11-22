# Least-positive-susceptibility control of high-transmission epidemic peak time

## Finding
In a deterministic epidemic with persistent, finitely supported individual susceptibility, the last positive susceptibility class controls the leading time of the peak of **infectious prevalence**, not its final size or its incidence maximum. For transmission-to-recovery ratio \(R\to\infty\), the peak time has an explicit two-term logarithmic expansion and a singular dependence on whether a small susceptibility is positive or exactly zero.

Write \(p_0=\Pr(\Lambda=0)\), \(\lambda_*=\min\{\lambda>0:\Pr(\Lambda=\lambda)>0\}\), \(p_*=\Pr(\Lambda=\lambda_*)\), and \(G(u)=\mathbb E[e^{-u\Lambda}]\). Then
\[
R t_{{\rm peak}}(R)=\frac{{\log(Rs p_*\lambda_*)}}{{\lambda_*(1-sp_0)}}+C(F,s)+o(1),\qquad
C(F,s)=\int_0^\infty\left(\frac1{{i+s(1-G(u))}}-\frac1{{1-sp_0}}\right)du.
\]
In particular,
\[
\lim_{{R\to\infty}}\frac{{R t_{{\rm peak}}(R)}}{{\log R}}=\frac1{{\lambda_*(1-sp_0)}}.
\]
For the constant-mean family \(F_a=\frac12\delta_a+\frac12\delta_{{2-a}}\), the coefficient is \(1/a\) for \(0<a\le1\), but it is \(1/(2-s)\) at \(a=0\). In particular, a moderately heterogeneous population can have a *later* prevalence peak than both a homogeneous population and a population containing a genuinely completely immune half.

## Assumptions and scope
Fix initial conditions \(0<s<1\), \(i=1-s>0\), zero initial removals, unit recovery, and a fixed susceptibility distribution \(F=\sum_{{j=1}}^m p_j\delta_{{\lambda_j}}\), where \(m\ge1\), \(p_j>0\), \(\sum_jp_j=1\), and distinct \(\lambda_j\ge0\) include at least one positive value. Transmission rate \(R>0\) multiplies susceptibility uniformly. The per-capita susceptible mass at susceptibility \(\lambda_j\) evolves as \(S_j'(t)=-R\lambda_jS_j(t)I(t)\); the total infectious prevalence satisfies \(I'(t)=R I(t)\sum_j\lambda_jS_j(t)-I(t)\). A unique strict peak means the unique maximizer of \(I\) on nonnegative times; for the theorem, \(Rs\mathbb E\Lambda>1\), automatically true eventually.

All limits hold as \(R\to\infty\) with \(F,s\) fixed, not jointly in the small positive susceptibility. The family statement varies the law only after the fixed-law asymptotic is established.

## Proof
**Step 1: exact pressure coordinate and uniqueness.** Let \(A(t)=R\int_0^t I(v)\,dv\). Then \(S_j(t)=s p_j e^{-\lambda_j A(t)}\), so \(S(t)=sG(A(t))\). Since recovered mass is \(A(t)/R\), conservation gives
\[
I(t)=H_R(A(t)),\quad H_R(u)=i+s(1-G(u))-u/R,\quad \dot A(t)=RH_R(A(t)).
\]
The derivative of infectious prevalence is \(I'(t)=RI(t)[sL(A(t))-1/R]\), where \(L(u)=-G'(u)=\sum_jp_j\lambda_j e^{-\lambda_ju}\) is continuous and strictly decreasing from \(\mathbb E\Lambda>0\) to zero. If \(Rs\mathbb E\Lambda>1\), the equation \(sL(A_R)=1/R\) has exactly one solution \(A_R>0\). For \(0\le u\le A_R\), \(H_R'(u)=sL(u)-1/R\ge0\), and hence \(H_R(u)\ge i>0\). The trajectory passes through \(A_R\) once; before it prevalence strictly rises, afterward strictly falls, because \(A(t)\) is strictly increasing as long as infection is positive. Thus
\[
R t_{{\rm peak}}(R)=\int_0^{{A_R}}\frac{{du}}{{H_R(u)}}.
\]
**Step 2: location of the peak.** Let \(\lambda_*\) be the least positive support point and \(p_*\) its mass. Factor the exact peak equation as
\[
\frac1R=sp_*\lambda_*e^{-\lambda_*A_R}\left[1+\sum_{{\lambda_j>\lambda_*}}\frac{{p_j\lambda_j}}{{p_*\lambda_*}}e^{-(\lambda_j-\lambda_*)A_R}\right].
\]
As \(R\to\infty\), strict monotonicity of \(L\) implies \(A_R\to\infty\); the bracket tends to one, so
\[
A_R=\frac{{\log(Rsp_*\lambda_*)}}{{\lambda_*}}+o(1),\quad A_R=O(\log R).
\]
This also covers the single-positive-class case (empty sum).

**Step 3: uniform error and constant term.** Put \(H_0(u)=i+s(1-G(u))\). On \([0,A_R]\), both \(H_R,H_0\ge i\) and \(H_0-H_R=u/R\). Hence
\[
0\le\int_0^{{A_R}}\left(\frac1{{H_R(u)}}-\frac1{{H_0(u)}}\right)du\le\frac{{A_R^2}}{{2Ri^2}}=o(1).
\]
Set \(H_\infty=i+s(1-p_0)=1-sp_0>0\). Since \(G(u)-p_0=\sum_{{\lambda_j>0}}p_je^{-\lambda_ju}=O(e^{-\lambda_*u})\),
\[
\frac1{{H_0(u)}}-\frac1{{H_\infty}}=\frac{{s(G(u)-p_0)}}{{H_0(u)H_\infty}}=O(e^{-\lambda_*u}).
\]
The difference is nonnegative and integrable on \([0,\infty)\). Splitting the integral into its constant limit plus this integrable remainder and inserting the \(A_R\) asymptotic gives the displayed expansion, including an actual finite constant \(C(F,s)\).

**Step 4: the natural mean-preserving two-class singularity.** For \(F_a=(\delta_a+\delta_{{2-a}})/2\), the mean is exactly one. If \(0<a<1\), \(p_0=0\), \(\lambda_*=a\), \(p_*=1/2\), so the coefficient is \(1/a\). If \(a=1\), both atoms coalesce at one, \(p_*=1\), and the coefficient is one. If \(a=0\), the zero-rate half is genuinely immune, \(p_0=1/2\), \(\lambda_*=2\), so the coefficient becomes \(1/[2(1-s/2)]=1/(2-s)\). As \(R\to\infty\), the coefficients are strictly ordered at \(a=1/2\), \(a=1\), \(a=0\) as \(2>1>1/(2-s)\). Thus this finite strict peak-time ordering holds for all sufficiently large \(R\). At each fixed sufficiently large \(R\), \(A_R(a)\) is the unique root of a strictly decreasing continuous function, depends continuously on \(a\in[0,1]\), and \(H_R\ge i\) up to the root, so the peak-time integral is continuous in \(a\). It exceeds both endpoint values at \(a=1/2\); therefore its maximum on \([0,1]\) is attained at least once in \((0,1)\). Finally the two iterated normalized-peak limits are \(\lim_{{a\downarrow0}}1/a=+\infty\) and \(1/(2-s)\), respectively. The latter follows fixed-\(R\) continuity before taking \(R\to\infty\). This completes the proof.

## Verification
The identities in Steps 1–3 are exact for all finite-support laws under the stated assumptions. The supplied `check_peak.py` numerically solves the *exact* pressure equation and quadrature for selected test cases and compares them with the asymptotic constant. These finite checks are diagnostics, not proof of the asymptotic or uniqueness; the algebraic bounds above establish those claims.

Run `python check_peak.py` with Python 3 and `mpmath` installed. No simulation of a finite stochastic population is needed, and no finite set of numerical tests is used to infer the general theorem.

## Relationship to prior work
Izyumtseva, KhudaBukhsh, Gomes and Rempala (2026, arXiv:2608.22122) rigorously derive the mixed-Sellke fluid limit, Laplace-transform susceptible law, selection identity, reproduction-number threshold, and final size. The pressure-coordinate equation in Step 1 is a specialization of their deterministic-limit representation. Their peak-time illustrations do not establish the fixed-law high-transmission two-term logarithmic expansion or the singular mean-preserving two-atom boundary. Earlier host-susceptibility literature establishes heterogeneous final-size and growth consequences, and literature on heterogeneous infectiousness/susceptibility investigates peak timing in different models. The present result isolates **infectious-prevalence peak time**, explicitly distinct from peak *incidence* and finite-population outbreak distributions. No exhaustive historical uniqueness is claimed.

## Limitations
Results are deterministic large-population consequences with a positive initial infected fraction and *finite* susceptibility support, homogeneous infectivity and recovery. The \(o(1)\) constant is not uniform in \(a\downarrow0\). The theorem does not assert monotone peak timing for all finite \(R\), a unique maximizing \(a\), or stochastic finite-population peak times. Historical priority beyond inspected sources and independent verification remain open.

## References
- O. Izyumtseva, W. R. KhudaBukhsh, M. G. M. Gomes, and G. A. Rempala, *From Individual-Based Stochastic Epidemics to Heterogeneous SIR Equations*, arXiv:2608.22122 (first public 2026-08-22), https://arxiv.org/html/2608.22122v1 .
- *Infections are not alike: The effects of covariation between individual susceptibility and transmissibility on epidemic dynamics*, Journal of Theoretical Biology, 2025, https://doi.org/10.1016/j.jtbi.2025.112211 .
