# A sharp phase-aperture transition for globally bounded two-tone Fourier extrapolation

## Finding

Consider two nonzero complex Fourier amplitudes with a prescribed maximal relative phase angle. Although arbitrary two-tone sums can have unbounded extrapolation amplification as the exterior evaluation point moves to infinity, bounding the phase difference strictly below a half-turn yields a **uniform, sharp exterior constant independent of both frequencies and observation distance**. Its optimizer undergoes an exact transition between an attained finite-frequency-gap branch and an unattained near-collision branch.

For real \(T>0\), distinct \(\lambda_1,\lambda_2\in\mathbb R\), and nonzero \(a,b\in\mathbb C\), set
\[
f(t)=a e^{i\lambda_1t}+b e^{i\lambda_2t},\qquad
\|f\|_{T}^{2}=\frac1{2T}\int_{-T}^{T}|f(t)|^{2}\,dt.
\]
Write \(\theta=\operatorname{Arg}(b\overline a)\in[-\pi,\pi]\), the principal relative phase, and fix an aperture \(0\le\varphi<\pi\) with \(|\theta|\le\varphi\). Let \(d_*\in(\pi,3\pi/2)\) be the unique solution of \(\tan d_*=d_*\), and put
\[
\rho=\frac1{\sqrt{1+d_*^2}}=0.2172336282112216574\ldots,
\qquad \varphi_*=\arccos(-\rho)=1.7897758492705223\ldots.
\]
Then the **exact uniform constant**, in squared-norm normalization, is
\[
\boxed{\quad
\sup_{\substack{T>0,\,\lambda_1\ne\lambda_2,\,a b\ne0,\\
|\operatorname{Arg}(b\overline a)|\le\varphi,\,|t|\ge T}}
\frac{|f(t)|^2}{\|f\|_T^2}
= \mathcal K(\varphi):=
\begin{cases}
\displaystyle \frac{2}{1-\rho},&0\le\varphi\le\varphi_*,\\[3pt]
\displaystyle \frac{2}{1+\cos\varphi},&\varphi_*<\varphi<\pi.
\end{cases}\quad}
\]
The same formula holds if \(T\) is fixed rather than optimized.

For \(0\le\varphi\le\varphi_*\), the maximum is **attained**: take equal positive amplitudes, frequency separation \(|\lambda_2-\lambda_1|=d_*/T\), and \(t=2\pi T/d_*>T\). For \(\varphi_*<\varphi<\pi\), the supremum is **not attained** by distinct frequencies: it is approached as their gap tends to zero with equal amplitude moduli and extremal relative phase \(\theta=\pm\varphi\), while the aligned exterior evaluation point tends to infinity. At \(\varphi=\pi\), no finite uniform-in-exterior-point constant exists. In particular, for phase-coherent positive coefficients the sharp constant is \(\mathcal K(0)=2.5550407785526074\ldots\), and as \(\varphi\uparrow\pi\), \(\mathcal K(\varphi)\sim4/(\pi-\varphi)^2\).

## Assumptions and scope

The frequencies are arbitrary **real**, distinct and may be arbitrarily close; amplitudes are both nonzero and complex, with no restriction on their moduli beyond the relative argument aperture. The observation interval is centered and has normalized Lebesgue energy. The predicted time is any real \(t\) outside that interval, with no finite bound on \(|t|\). The relative phase is measured at the center of the observation window, so a common time shift changes the admissibility condition. Global phase rotation, common carrier modulation, scaling of both amplitudes, and positive time rescaling preserve the quotient. Statements concern the squared amplification quotient, not its square root.

## Proof

**1. Exact Gram energy.** Scaling time by \(T\), writing \(u=|a|>0\), \(v=|b|>0\), \(d=T|\lambda_2-\lambda_1|>0\), and \(s(d)=\sin(d)/d\), direct integration gives
\[
\|f\|_T^2=u^2+v^2+2uv\,s(d)\cos\theta.
\]
Since \(|s(d)|<1\), the denominator is strictly positive. At every time, the triangle inequality gives \(|f(t)|\le u+v\). Conversely, for each fixed gap and \(\theta\), infinitely many exterior times have the two exponentials exactly in phase: choose an integer \(m\) of sufficiently large magnitude such that \((\lambda_2-\lambda_1)t+\theta=2\pi m\). Thus
\[
\sup_{|t|\ge T}\frac{|f(t)|^2}{\|f\|_T^2}
=\frac{(u+v)^2}{u^2+v^2+2uv\,s(d)\cos\theta}.
\]

**2. Optimization over amplitude ratio.** With \(h=s(d)\cos\theta\in(-1,1)\), the exact identity
\[
\frac{u^2+v^2+2huv}{(u+v)^2}
=\frac{1+h}{2}+\frac{1-h}{2}\left(\frac{u-v}{u+v}\right)^2
\]
shows that the supremum over positive \(u,v\) is \(2/(1+h)\), with equality **if and only if \(u=v\)**. The complete problem therefore reduces to minimizing \(s(d)\cos\theta\) over \(d>0\) and \(|\theta|\le\varphi\).

**3. Global minimum of sinc.** On \((0,\pi]\), \(s\ge0\). On \((\pi,2\pi)\), \(s<0\), with derivative \(s'(d)=(d\cos d-\sin d)/d^2\). Its unique zero is the unique solution \(d_*\in(\pi,3\pi/2)\) of \(\tan d=d\). Indeed \(\tan d-d\) is strictly increasing there (derivative \(\tan^2d>0\) away from \(\pi\)), from a negative value to infinity, and on \((3\pi/2,2\pi)\) the derivative of \(s\) is positive. Moreover for \(d\ge2\pi\), \(s(d)\ge-1/(2\pi)>-2/(3\pi)=s(3\pi/2)\ge s(d_*)\). Hence \(d_*\) is the **unique global minimizer** on \((0,\infty)\). At this point \(\sin d_*=d_*\cos d_*\), giving \(s(d_*)=\cos d_*=-1/\sqrt{1+d_*^2}=-\rho\). Also \(s(d)<1\) for every \(d>0\), with limit \(s(d)\to1\) as \(d\downarrow0\).

**4. Sharp aperture transition.** For any admissible \(\theta\), set \(c=\cos\theta\in[\cos\varphi,1]\). If \(c\ge0\), then \(s(d)c\ge-\rho\). If \(c<0\), since \(s(d)\le1\) and \(c\ge\cos\varphi\), we have \(s(d)c\ge c\ge\cos\varphi\). Consequently
\[
\inf_{d>0,\,|\theta|\le\varphi}s(d)\cos\theta
=\min\{-\rho,\cos\varphi\}.
\]
The value \(-\rho\) is attained by \(d=d_*\), \(\theta=0\); the value \(\cos\varphi\), when smaller, is a strict infimum approached by \(d\downarrow0\), \(|\theta|=\varphi\), since \(s(d)<1\) and \(\cos\varphi<0\). Substitution into step 2 yields the stated piecewise \(\mathcal K\), with crossover at \(\varphi_*\).

**5. Equality and singular boundary.** In the finite-gap regime \(\varphi\le\varphi_*\), choose \(u=v\), \(\theta=0\), and \(d=d_*\). The exterior point \(t=2\pi T/d_*\) aligns both tones, and \(2\pi/d_*>1\), so equality is achieved. When \(\varphi>\varphi_*\), equality would require \(s(d)=1\) at a positive gap, impossible, proving nonattainment. To approach the constant, use \(\theta=\varphi\), equal amplitude moduli, \(d\downarrow0\), and choose \(t=T(2\pi-\varphi)/d\) (which eventually exceeds \(T\)) so the two terms align. At \(\varphi=\pi\), the same construction with phase \(\pi\) has energy \(2(1-s(d))\to0\) while the aligned peak remains \(4\), so amplification diverges. Finally \(1+\cos\varphi\sim(\pi-\varphi)^2/2\), establishing the stated blow-up.

## Verification

The proof consists of exact integration, a two-variable square-completion identity, the elementary global-minimum analysis of \(\sin d/d\), and explicit exact extremizing witnesses. No numerical sampling or source computation is needed for the universal inequality. The standalone Python 3 standard-library program `CHECK.py` solves the stationary equation by bisection, checks the formulas and witness numerically, and compares representative sampled quotients with the analytic sharp curve. Run `python CHECK.py`; a successful run prints `PHASE_APERTURE_CHECKS_PASSED`. Its finite tests are supplementary and do not establish the continuum theorem.

## Relationship to prior work

Ruizhe Zhang's 2026 paper [1] develops extrapolation and leverage bounds for arbitrary sparse Fourier sums without frequency separation. Its principal statements depend on the exterior point and allow unrestricted complex phases; they do not state a global exterior-uniform, phase-aperture sharp law. Two publicly available sharp two-frequency results [2,3] prove exact **fixed-exterior-point** point-evaluation factors for unrestricted coefficients, including the fixed-frequency-gap formula \((1-s(d)\cos(dt/T))/(1-s(d)^2)\). Those statements maximize over all coefficient phases at a specified time. They do not imply the phase-restricted result by specialization: the optimizer for their unrestricted point evaluation can violate the phase aperture, and the order of optimization (phase restriction followed by all exterior times and gaps) changes the extremal regime. The present finding is the explicit uniform-in-time coefficient-cone classification, including a finite-gap/near-collision attainment transition.

## Limitations

This is a sharp theorem only for two frequencies and a **phase constraint referenced to the center of a symmetric observation interval**. It does not imply a uniform bound for differences of two separately phase-restricted signals, for three or more frequencies, or for arbitrary moving observation centers. Its result is deterministic, not a statistical recovery or noise-robust phase-estimation guarantee. The exact criterion is elementary and some of its ingredients follow from classical Gram methods; an unlocated older coefficient-cone theorem could supersede the presentation.

## References

[1] R. Zhang, *Optimal Extrapolation Bounds for Sparse Fourier Sums*, arXiv:2607.10501 (first publicly posted July 11, 2026), Theorem 1.1 and Section 5.3. https://arxiv.org/abs/2607.10501

[2] *Sharp exterior leverage for two arbitrary Fourier frequencies*, publicly available mathematical research note (November 2026), especially its fixed-gap evaluation formula. https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-sharp-exterior-leverage-for-two-arbitrary-fourier-frequencies--a88bbfc8602c

[3] *Sharp two-frequency exterior Fourier leverage and the quadratic collision defect*, publicly available mathematical research note (November 2026), especially its fixed-gap evaluation theorem. https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-sharp-two-frequency-exterior-fourier-leverage-and-the-quadratic--517d41b07a68
