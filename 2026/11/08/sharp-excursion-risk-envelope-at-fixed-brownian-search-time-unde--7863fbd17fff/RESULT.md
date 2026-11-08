# Sharp excursion-risk envelope at fixed Brownian search time under distributed resetting

## Finding

A Brownian searcher can have an exactly fixed mean time to reach its absorbing target and nevertheless have different probabilities of undertaking a large excursion. There is a **sharp, simultaneously valid stochastic envelope for every excursion threshold above the reset region**, with unique optimal reset-location laws and a complete attainable range.

**Theorem.** Let a particle with diffusivity \(D>0\) and generator \(D\partial_{xx}\) start from a specified \(x_0>0\) and be absorbed at \(0\). Independently of diffusion, rate-\(r>0\) Poisson events move it instantaneously to independently sampled locations \(Z\) with law \(\nu\) supported in a fixed interval \([a,b]\), where \(0<a<b\). Write \(T\) for absorption time and \(M=\sup_{0\le t\le T}X_t\), including both sides of resetting jumps. Define

\[
 k=\sqrt{r/D},\qquad s=\mathbb E_\nu[e^{-kZ}],\qquad u=\mathbb E_\nu[e^{kZ}],\qquad s_0=e^{-kx_0}.
\]

The mean search time is \(\mathbb E[T]=(1-s_0)/(rs)\). For **every** threshold \(m>\max\{x_0,b\}\), put \(t=e^{-km}\). The exact exceedance probability is

\[
 \boxed{\Pr_\nu(M\ge m)=\Phi_m(u;s)
 =\frac{t(1-s_0)(u+s/s_0)}{(1-t)(s+tu)}.}
\]

In particular, holding \(D,r,x_0,a,b\) and the mean search time fixed is equivalent to holding \(s\) fixed. Set

\[
 \ell=e^{-kb},\quad h=e^{-ka},\quad
 \theta=\frac{s-\ell}{h-\ell},\quad
 u_{\min}=\frac1s,\quad
 u_{\max}=\theta e^{ka}+(1-\theta)e^{kb}.
\]

For any feasible \(s\in[\ell,h]\), the exact set of attainable exceedance probabilities, simultaneously ordered for **all** thresholds above the support, is

\[
 \boxed{\Phi_m(u_{\min};s)\le\Pr_\nu(M\ge m)\le\Phi_m(u_{\max};s).}
\]

If \(\ell<s<h\), the lower endpoint is attained **only** by resetting at the effective single location \(z_*=-(\log s)/k\), and the upper endpoint **only** by resetting to \(a\) with probability \(\theta\) and to \(b\) with probability \(1-\theta\). Every value between the endpoints is attained. More strongly, all above-support maximum laws for fixed \(s\) form a one-parameter family indexed exactly by \(u\in[u_{\min},u_{\max}]\); one measurement of any \(\Pr(M\ge m)\) at a known admissible threshold uniquely identifies \(u\). At the boundary values \(s=\ell\) or \(s=h\), the only feasible reset law is the corresponding point mass and the endpoints coincide.

The same order holds in the rare-event coefficient:

\[
 \lim_{m\to\infty}e^{km}\Pr_\nu(M\ge m)
 =(1-s_0)\left(\frac us+\frac1{s_0}\right).
\]

## Assumptions and scope

The diffusion is ordinary one-dimensional driftless Brownian motion with variance \(2Dt\) between resets, on the positive half-line; the target is perfectly absorbing at zero. Resetting times are independent exponential holding times of rate \(r\). Each reset chooses a fresh spatial location according to the same probability measure \(\nu\), independently of all earlier history. The initial position \(x_0\) is fixed and need not be drawn from \(\nu\). There are no refractory periods or spatial dependence in resetting rates. Both reset endpoints are positive, and the excursion threshold must exceed both the initial position and every possible reset position; otherwise a reset jump could cross the threshold and the displayed formula need not apply.

The absorption time is finite almost surely: after every reset, the probability of reaching zero before the next reset is at least \(e^{-kb}>0\), and reset cycles are independent after drawing a fresh location. Its mean is finite by the renewal calculation below. Consequently \(M<\infty\) almost surely.

## Proof

**1. Fixed-mean constraint.** Starting from any \(x>0\), let \(\tau_0\) be the first Brownian hitting time of zero in the absence of resets, and let \(R\) be independent exponential time of rate \(r\). Standard one-dimensional killed-diffusion boundary value theory, or solving \(Df''=rf\) with \(f(0)=1\) and \(f(\infty)=0\), gives \(\Pr(\tau_0<R)=\mathbb E e^{-r\tau_0}=e^{-kx}\). Also \(\mathbb E[\min(\tau_0,R)]=(1-e^{-kx})/r\). If \(H(x)\) denotes mean absorption time after starting at \(x\), first-cycle decomposition yields

\[
 H(x)=\frac{1-e^{-kx}}r+(1-e^{-kx})\,\mathbb E H(Z).
\]

Averaging this identity over \(\nu\) gives \(\mathbb E H(Z)=(1-s)/(rs)\); substitution yields \(H(x_0)=(1-s_0)/(rs)\), with no assumption on the density or number of atoms of \(\nu\).

**2. Exact threshold exit law.** Fix \(m>\max\{x_0,b\}\). Before the first of a hit on zero, a hit on \(m\), or a reset, define the respective probabilities starting at \(x\in(0,m)\) as \(A_x,B_x,C_x\). The killed boundary equations and endpoint conditions give

\[
 A_x=\frac{\sinh(k(m-x))}{\sinh(km)},\qquad
 B_x=\frac{\sinh(kx)}{\sinh(km)},\qquad
 C_x=1-A_x-B_x.
\]

Let \(Q(x)\) be the probability of hitting the upper threshold before final absorption at zero, with future resets active. Its first-cycle renewal identity is \(Q(x)=B_x+C_x\mathbb E Q(Z)\). Writing bars for averages over \(\nu\), one obtains

\[
 \mathbb E Q(Z)=\frac{\bar B}{\bar A+\bar B},\qquad
 Q(x_0)=B_{x_0}+C_{x_0}\frac{\bar B}{\bar A+\bar B}.
\]

This denominator is strictly positive because absorption before resetting has positive probability. In terms of \(t=e^{-km}\), \(s=\mathbb E e^{-kZ}\), and \(u=\mathbb E e^{kZ}\), the three elementary identities are

\[
 B_x=\frac{t(e^{kx}-e^{-kx})}{1-t^2},\qquad
 A_x+B_x=\frac{e^{-kx}+t e^{kx}}{1+t},
 \qquad
 \frac{\bar B}{\bar A+\bar B}=\frac{t(u-s)}{(1-t)(s+tu)}.
\]

Substitute these into the preceding renewal formula and cancel to get

\[
 Q(x_0)=\frac{t(1-s_0)(u+s/s_0)}{(1-t)(s+tu)}.
\]

As resetting never lands at or above \(m\), this equals \(\Pr(M\ge m)\). Boundary hitting at exactly \(m\) is equivalent to crossing for continuous Brownian excursions; the difference between strict and non-strict inequalities has probability zero for each fixed admissible \(m\).

**3. Exact stochastic envelope and equality.** At fixed \(s\), differentiation of the rational formula gives

\[
 \frac{\partial\Phi_m}{\partial u}
 =\frac{t(1-s_0)s(1-t/s_0)}{(1-t)(s+tu)^2}>0,
\]

since \(0<t<s_0<1\). Let \(Y=e^{-kZ}\). Then \(\ell\le Y\le h\), \(\mathbb EY=s\), and \(u=\mathbb E(1/Y)\). Strict convexity of \(y\mapsto1/y\) gives the Jensen bound \(u\ge1/s\), with equality only for \(Y=s\). The secant-line bound for the same strictly convex function on \([\ell,h]\) yields

\[
 \mathbb E\frac1Y\le
 \frac{s-\ell}{h-\ell}\frac1h+
 \frac{h-s}{h-\ell}\frac1\ell
 =u_{\max},
\]

with equality only if \(Y\) is supported at the endpoints (their weights being forced by its mean). Hence the unique lower and upper maximizing spatial reset laws are exactly those in the finding. For every \(v\in[u_{\min},u_{\max}]\), an appropriate mixture of these two extremal probability measures maintains \(\mathbb EY=s\) while having \(\mathbb E(1/Y)=v\). The map \(v\mapsto\Phi_m(v;s)\) is continuous and strictly increasing for each threshold, so the complete interval is attained, and the same two extremizers work simultaneously at every threshold.

**4. Identification and rare-tail boundary.** If a threshold probability \(P=\Pr(M\ge m)\) is measured and \(s\) is known from the MFPT, put \(J=P(1-t)/(t(1-s_0))\). Solving the exact rational equation yields

\[
 u=\frac{s(J-1/s_0)}{1-tJ},\qquad 1-tJ>0,
\]

where positivity follows from \(t<s_0\). Thus a single above-support threshold probability identifies the second exponential moment \(u\), while no such measurement can in general identify the full reset law. Finally, multiplying the exact formula by \(1/t=e^{km}\) and taking \(t\downarrow0\) gives the stated rare-excursion coefficient. This limit is at fixed physical parameters and fixed compact reset support; no simultaneous high-reset-rate limit is claimed.

## Verification

Run `python3 checker.py` from this directory. The standalone script uses the standard library only and reproduces the theorem's closed form independently from the competing-event probabilities \(A_x,B_x,C_x\). It compares both formulas over random reset laws and thresholds, probes the full fixed-mean interpolation, checks the inverse-moment reconstruction, verifies a high-threshold limit and uses independently sampled exact killed-cycle outcomes for a Monte Carlo diagnostic. The replay passed 8,276 counted assertions.

For a concrete comparison take \(D=r=1\), \(a=1\), \(b=3\), \(x_0=2\) and \(s=(e^{-1}+e^{-3})/2\). The deterministic location is \(z_*=1.56621916951697\ldots\); the upper extremizer is an equal mixture at \(1\) and \(3\). Both have mean absorption time \(4.14045510959032\ldots\). At threshold \(m=4\), their respective exceedance probabilities are \(0.34445347398706\ldots\) and exactly \(1/2\). The exact value \(1/2\) in the latter case also follows from reflection symmetry about the initial position \(2\) of the reset sites and the two absorbing boundaries \(0\) and \(4\).

## Relationship to prior work

Evans and Majumdar introduced distributed spatial resetting and computed mean absorption times (arXiv:1107.4225). Julián-Salgado, Dagdug and Boyer analyzed two reset locations and discontinuous transitions in the optimal *reset rate* (arXiv:2311.11897). Méndez, Flaquer-Galmés and Campos analyzed first-passage-time distributions under random reset locations and discussed equivalent resetting points (arXiv:2401.01125). Guo, Yan and Chen solved first-passage maximum statistics for resetting to one fixed position (arXiv:2306.15929). These are important premises and do not supply the all-threshold, fixed-MFPT excursion envelope over an arbitrary compactly supported reset-location law.

A separate available result on the *same search model* establishes fixed-MFPT envelopes for the **Laplace transform and variance of absorption time**, with some matching extremal reset measures. That result does not logically imply this theorem: the path maximum is not determined by its absorption-time Laplace bounds, and the requisite upper-absorbing-boundary renewal calculation is distinct. The overlap in model and extremizers is disclosed, not treated as proof of novelty. General convex-order techniques and killed Markov-process formulas may yield this statement as a corollary in broader unindexed literature; publication priority is therefore subject to independent verification.

## Limitations

The statement concerns the *maximum attained before absorption*, not the maximum at a fixed observation time or a stationary resetting process. It orders exceedance probabilities only for thresholds strictly above every allowed reset location and the initial point. The support bounds \(a,b\), reset rate \(r\), diffusivity \(D\) and initial position \(x_0\) are fixed; changing them can change the design ordering. The finite-threshold and rare-threshold bounds are exact within this scope, but do not establish ordering of the full path law, all lower-threshold maxima or first-passage-time distributions. The proof uses memoryless resetting and fresh iid reset locations. No independent review or priority certification has been carried out.

## References

1. M. R. Evans and S. N. Majumdar, *Diffusion with Optimal Resetting*, arXiv:1107.4225, v1 first public July 21, 2011. https://arxiv.org/abs/1107.4225
2. W. Guo, H. Yan and H. Chen, *Extremal statistics for a resetting Brownian motion before its first-passage time*, arXiv:2306.15929, v1 June 28, 2023. https://arxiv.org/abs/2306.15929
3. P. Julián-Salgado, L. Dagdug and D. Boyer, *Diffusion with two resetting points*, arXiv:2311.11897, v1 November 20, 2023. https://arxiv.org/abs/2311.11897
4. V. Méndez, R. Flaquer-Galmés and D. Campos, *First-passage time of a Brownian searcher with stochastic resetting to random positions*, arXiv:2401.01125, v1 January 2, 2024. https://arxiv.org/abs/2401.01125
5. K. Dȩbicki, E. Hashorva and Z. Michna, *Distributional and Extremal Behaviour of Brownian Motion with Exponential Resetting*, published August 19, 2026. https://doi.org/10.1007/s11009-026-10316-4
