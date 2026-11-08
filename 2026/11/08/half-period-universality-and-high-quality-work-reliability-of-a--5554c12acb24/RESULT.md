# Half-period universality and high-quality work reliability of a two-jump inertial trap

## Finding

A one-dimensional inertial Brownian particle is driven by a known constant positive force \(f\), and its harmonic-trap center is allowed **only two ordinary finite jumps**: from zero to a chosen constant \(a\) at the start, and back to zero at a chosen positive time \(h\). The initial position and velocity are both zero. For every underdamped choice of mass, stiffness and positive friction, **the first damped half-period is the unique globally optimal switching time** for both the mean extracted work and the probability of extracting work in a single realization, for *every fixed amplitude with negative mean work*. In particular, time optimality is independent of the chosen extracting amplitude and of bath temperature. This is a restricted-control statement, not an optimum over arbitrary trap-center trajectories.

Writing
\[
\alpha=\frac{\gamma}{2m},\qquad
\omega=\sqrt{\frac{k}{m}-\alpha^2},\qquad
h_\star=\frac{\pi}{\omega},\qquad q=e^{-\alpha h_\star},
\]
the globally mean-optimal amplitude is \(a_\star=-f/(2k)\). Its work is Gaussian with exact moments
\[
\boxed{\quad \mathbb E W_\star=-\frac{f^2}{4k}(1+q),\qquad
\operatorname{Var}(W_\star)=\frac{f^2\Theta}{4k}(1-q^2),\quad}
\]
where \(\Theta=k_B T>0\) is thermal energy. The exact probability of *failing* to extract work is
\[
\mathbb P(W_\star\ge0)
=\overline\Phi\!\left(\frac{f}{2\sqrt{k\Theta}}
\sqrt{\frac{1+q}{1-q}}\right).
\]
The Gaussian complementary CDF \(\overline\Phi(z)=\int_z^\infty e^{-u^2/2}\,du/\sqrt{2\pi}\).

At fixed \(m,k,f,\Theta\) as \(\gamma\downarrow0\), the two-jump mean work reaches the limiting, unconstrained ideal mean-work bound in the motivating model, while the single-trial failure probability has the sharp asymptotic
\[
\boxed{\quad
\mathbb P(W_\star\ge0)\sim
\frac{\sqrt{k\Theta\gamma/(2m\omega_0)}}{f}
\exp\!\left(-\frac{f^2m\omega_0}{2\pi k\Theta\gamma}\right),\qquad
\omega_0=\sqrt{k/m}.\quad}
\]
At the *same* protocol duration \(h_\star\), the ratio of the two-jump work variance to the work variance of the unrestricted **mean-optimal** protocol tends to the universal constant \(\pi^2/8\). This is a comparison of two specific work variances, not a universal minimum-variance bound.

## Assumptions and scope

Take \(m,k,\gamma,\Theta,f>0\) and \(0<\gamma<2\sqrt{mk}\). Starting at \(x(0^-)=\dot x(0^-)=0\), let
\[
m\ddot x(t)+\gamma\dot x(t)+k[x(t)-\lambda(t)]
=f+\sqrt{2\gamma\Theta}\,\xi(t),\qquad
\lambda(t)=\begin{cases}a,&0<t<h,\\0,&t<0\text{ or }t>h.\end{cases}
\]
The white noise \(\xi\) is standard and independent of the fixed initial data. The force \(f\) stays constant throughout the protocol. The trap jumps are instantaneous *finite position changes*, not Dirac-delta impulses or a finite-bandwidth implementation. By the jump convention for the potential \(V(x,\lambda)=k(x-\lambda)^2/2\), controller work is the sum of the two potential changes, \(W=k a[x(h)-x(0)]=ka x(h)\). Negative \(W\) means energy extracted by the trap controller; cost of generating \(f\), quench cost beyond work, and repetition/erasure costs are not included.

Mean extraction occurs exactly for \(-f/k<a<0\). For this interval the same globally optimal duration holds if a finite horizon \(H>0\) is imposed, with \(h=\min\{H,h_\star\}\). The optimization of probability is always **at fixed amplitude**; when amplitude itself is free, the supremum of success probability occurs in the small-amplitude limit rather than at the mean-optimal amplitude.

## Proof

**1. The exact two-jump work law.** Put
\[
g(t)=e^{-\alpha t}\left(\cos(\omega t)+\frac\alpha\omega\sin(\omega t)\right),\qquad
b(t)=e^{-\alpha t}\frac{\sin(\omega t)}{\omega},\qquad K(t)=1-g(t).
\]
These are the two entries in the first row of the fundamental matrix for the homogeneous phase-space dynamics. Since \(m\ddot g+\gamma\dot g+kg=0\), \(g(0)=1\), \(\dot g(0)=0\), the mean endpoint is \(\mathbb E x(h)=(a+f/k)K(h)\). The oscillator's equilibrium covariance is \(C_\infty=\operatorname{diag}(\Theta/k,\Theta/m)\). Since the initial phase-space state is deterministic, the covariance at time \(h\) is \(C_\infty-e^{Bh}C_\infty e^{B^{\mathsf T}h}\), where \(B=\left(\begin{smallmatrix}0&1\\-k/m&-\gamma/m\end{smallmatrix}\right)\). Hence
\[
\operatorname{Var}[x(h)]
=\frac\Theta k\left[1-g(h)^2-\frac km b(h)^2\right]
=\frac{2\gamma\Theta}{m^2}\int_0^h b(s)^2\,ds>0.
\]
The last equality also follows from the stochastic convolution. In particular, \(W=ka x(h)\) is Gaussian, with
\[
\mathbb E W=ka(a+f/k)K(h),\qquad
\operatorname{Var}(W)=k^2a^2\operatorname{Var}[x(h)].
\]
For every \(h>0\), \(K(h)>0\) by stability of the positive-friction oscillator. The mean work is strictly convex in \(a\), giving its unique minimizing value \(a_\star=-f/(2k)\), independently of duration.

**2. Global mean-optimal duration.** Differentiate: \(K'(h)=(k/m)b(h)\). Thus \(K\) increases strictly until \(h_\star=\pi/\omega\), and its subsequent successive extrema at \(n\pi/\omega\) are controlled by the strictly decaying envelope \(e^{-\alpha n\pi/\omega}\). At the first odd extremum \(g(h_\star)=-q\), the function \(K\) attains its unique global maximum \(1+q\). Because \(ka(a+f/k)<0\) precisely for \(-f/k<a<0\), that \(h_\star\) uniquely minimizes mean work throughout the extraction interval. With a horizon the optimizer is \(\min\{H,h_\star\}\).

**3. Global success-optimal duration (a log-concave impulse-response lemma).** For fixed \(-f/k<a<0\), the event \(W<0\) is \(x(h)>0\), and
\[
\mathbb P(W<0)=\Phi\!\left((a+f/k)\frac{K(h)}{\sqrt{\operatorname{Var}[x(h)]}}\right).
\]
The strictly increasing transformation \(\Phi\) reduces the duration problem to maximizing
\[
\frac{\int_0^h b(s)\,ds}{\sqrt{\int_0^h b(s)^2\,ds}},
\]
using \(K=(k/m)\int b\). On \((0,h_\star)\), \(b>0\) and it is strictly log-concave because
\[
\frac{d^2}{dh^2}\log b(h)=-\omega^2\csc^2(\omega h)<0.
\]
Write \(F(h)=\int_0^h b\), \(G(h)=\int_0^h b^2\), \(H_0(h)=2G(h)-b(h)F(h)\). A derivative calculation gives
\(H_0'(h)=b(h)^2-b'(h)F(h)\). After the unique mode of \(b\), one has \(b'\le0\) and therefore \(H_0'>0\). Before that mode, \(b'>0\). Set \(R(h)=b(h)^2/b'(h)-F(h)\). Strict log-concavity implies
\[
R'(h)=b(h)\left[1-\frac{b(h)b''(h)}{b'(h)^2}\right]>0,
\]
and \(R(0+)=0\), so \(F(h)<b(h)^2/b'(h)\) and again \(H_0'(h)>0\). Since \(H_0(0+)=0\), one has \(H_0(h)>0\) for the whole first half-period. Consequently,
\[
\frac{d}{dh}\frac{F(h)^2}{G(h)}
=\frac{b(h)F(h)}{G(h)^2}\left[2G(h)-b(h)F(h)\right]>0
\]
throughout \(0<h<h_\star\). After \(h_\star\), \(K(h)<K(h_\star)\) strictly, while \(\operatorname{Var}[x(h)]>\operatorname{Var}[x(h_\star)]\) because it is the integral of a nonzero square. Thus no later time matches the normalized displacement at the first half-period. This proves unique global success-time optimality for **each** extraction-generating \(a\), including but not limited to the mean-optimal amplitude.

**4. Half-period distribution and ideal benchmark.** Since \(b(h_\star)=0\), \(g(h_\star)=-q\), the variance identity becomes \(\operatorname{Var}[x(h_\star)]=(\Theta/k)(1-q^2)\). Substituting \(a_\star=-f/(2k)\) into the Gaussian work law yields the moments and failure probability in the Finding section.

The unrestricted distributional-protocol calculation of Yao--Bao--Hou [1, Eq. (10), Eq. (16)] specializes to the same initial and endpoint trap centers \(\lambda_i=\lambda_f=0\), initial position zero, and constant force \(f\), giving
\[
\mathbb E W_{\mathrm{ideal}}(h)=-\frac{f^2 h}{2(2\gamma+kh)},\qquad
\operatorname{Var}(W_{\mathrm{ideal}}(h))
=\frac{2\gamma\Theta f^2h}{(2\gamma+kh)^2}.
\]
These formulas are **literature benchmarks**, not claimed as newly proved universal bounds. At \(h=h_\star\), the exact restricted-to-ideal ratios are
\[
\frac{|\mathbb E W_\star|}{|\mathbb E W_{\mathrm{ideal}}(h_\star)|}
=\frac{1+q}{2}\left(1+\frac{2\gamma}{kh_\star}\right),\qquad
\frac{\operatorname{Var}(W_\star)}{\operatorname{Var}(W_{\mathrm{ideal}}(h_\star))}
=\frac{(1-q^2)(2\gamma+kh_\star)^2}{8k\gamma h_\star}.
\]
As \(\gamma\downarrow0\), \(h_\star\to\pi/\omega_0\), \(q=1-\gamma\pi/(2m\omega_0)+O(\gamma^2)\), and these ratios tend respectively to \(1\) and \(\pi^2/8\). This comparison keeps the actual protocol time equal on both sides.

**5. Rare non-extraction asymptotics.** The Gaussian failure argument is
\(z_\gamma=[f/(2\sqrt{k\Theta})]\sqrt{\coth(\gamma\pi/(4m\omega))}\).
As \(\gamma\downarrow0\),
\[
\frac{z_\gamma^2}{2}
=\frac{f^2m\omega_0}{2\pi k\Theta\gamma}+O(\gamma),\qquad
\frac1{\sqrt{2\pi}z_\gamma}
\sim\frac{\sqrt{k\Theta\gamma/(2m\omega_0)}}{f}.
\]
Mills' asymptotic \(\overline\Phi(z)\sim e^{-z^2/2}/(\sqrt{2\pi}z)\) proves the stated sharp failure equivalent. This is a small-friction theorem for the specified initial state, not a claim about repeated-engine reliability with uncontrolled initial conditions.

## Verification

The accompanying `verify_pulse.py` checks the quadratic optimization symbolically; independently evaluates fundamental-matrix entries by matrix exponentiation; compares stochastic-convolution covariance with its closed form for multiple positive underdamped parameter sets; checks half-period work moments and Gaussian success probabilities; numerically probes both sides of the unique peak; and tests the high-quality mean, variance-ratio, and exponential failure asymptotics. The program ran to completion with 421 passing checks. The strict continuum time optimization and singular asymptotic equivalence follow from the analytical arguments above, not from the finite numerical grid.

## Relationship to prior work

Yao, Bao and Hou [1] establish the exact mass-independent minimum-mean-work value and variance for unconstrained (including distributional-impulse) underdamped moving traps. Their full original HTML exposition and appendices specify the ideal protocol, and explicitly identify realistic actuator limitations as a direction for further study; they do not provide the present fixed two-jump class's global switching-time and sign-probability classification. Our comparison uses their results as inputs and never claims their ideal optimum as new. Schüttler and collaborators [2] derive passive and active-trap optimal-work and measurement-feedback formulas in the overdamped setting, including work statistics; their full article does not supply this inertial single-pulse first-half-period result. Gomez-Marin, Schmiedl and Seifert [3] establish singular boundary operations in underdamped ideal control, not the specified driven two-jump reliability optimum. The damped-oscillator step response and Gaussian covariance formula themselves are standard; the contribution is the **joint sharp global time-optimum for expected work and sign reliability in the constrained pulse family**, together with an exact near-ideal work/variance comparison and sharp rare-failure law.

## Limitations

The trap protocol has two instantaneous position jumps and therefore is **not** finite-bandwidth control. It contains no Dirac impulse but still requires arbitrarily rapid quench actuation. Initial position/velocity are deterministic zero, the active force is a known constant, and friction is positive but underdamped. The result does not cover an unknown active force, AOUP forcing noise, stationary initial data, measurement error, continuous-time feedback, a finite actuator slew-rate, or the energetic cost of preparing the initial state/drive. The comparison with the ideal variance is not a general minimum-variance claim. The literature comparisons establish a best-knowledge noncoverage assessment, not publication-priority or independent certification.

## References

[1] Kangcan Yao, Ruicheng Bao and Zhonghuai Hou, *Finite-time minimum-work protocols for underdamped traps driven by active forces*, arXiv:2610.38653v1, first publicly posted 2026-10-28. https://arxiv.org/html/2610.38653v1 .

[2] Janik Schüttler, Rosalba Garcia-Millan, Michael E. Cates and Sarah A. M. Loos, *Active particles in moving traps: minimum work protocols and information efficiency of work extraction*, arXiv:2501.18613v2. https://arxiv.org/html/2501.18613 .

[3] Alex Gomez-Marin, Tim Schmiedl and Udo Seifert, *Optimal protocols for minimal work processes in underdamped stochastic thermodynamics*, Journal of Chemical Physics 129, 024114 (2008), DOI:10.1063/1.2948948; arXiv:0803.0269. https://pubmed.ncbi.nlm.nih.gov/18624523/ .
