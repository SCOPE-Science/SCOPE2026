# A sharp ambient-background delay bound for one-shot localization of a diffusing pollutant pulse

## Finding

For a single Gaussian diffusion pulse observed by three simultaneous, equally exposed independent Poisson counters at positions \(-a,0,a\), the locally information-optimal monitoring time for its cross-stream source position is **unique**, even when the source amplitude and a spatially uniform positive background are unknown nuisance parameters. The optimal time grows strictly as background increases. Its high-background limit is at most \(5/3\) times its zero-background limit, with sharp factor \(5/3\) when chemical loss vanishes. It is always earlier than the time at which the signal at either outer counter reaches its maximum.

Set \(h=a^2/(4D)\) and define, for \(\alpha>0\),
\[
T_\alpha=\frac{2h}{\alpha+\sqrt{\alpha^2+4\kappa h}}.
\]
For every positive source strength \(A\), background \(b\), diffusivity \(D\), spacing \(a\), and every loss rate \(\kappa\ge0\), the unique optimal time \(t_*(b)\) obeys
\[
\boxed{T_{5/2}<t_*(b)<T_{3/2},\qquad
1<\frac{T_{3/2}}{T_{5/2}}\le\frac53.}
\]
The upper factor is attained as an endpoint ratio exactly when \(\kappa=0\); the strict interior inequalities hold for each finite \(b>0\). Also \(t_*(b)\) is strictly increasing in \(b\), with endpoint limits \(T_{5/2}\) as \(b\downarrow0\) and \(T_{3/2}\) as \(b\to\infty\).

## Assumptions and scope

Fix \(a,D,A,b>0\) and \(\kappa\ge0\). Consider the one-dimensional instantaneous diffusion-and-first-order-loss kernel at source coordinate \(\theta\in\mathbb R\), observed once at age \(t>0\). At the three positions \(x\in\{-a,0,a\}\), independent counts have means
\[
\mu_x(t,\theta,A,b)=b+A t^{-1/2}\exp\!\left(-\kappa t-\frac{(x-\theta)^2}{4Dt}\right).
\]
All counters have the same prescribed exposure and calibration, absorbed into \(A\) and \(b\). The instantaneous-release time, diffusivity, spacing and loss rate are known; the unknown statistical parameters are \((\theta,A,b)\). The optimization is **local at nominal \(\theta=0\)**, using the efficient Fisher information for \(\theta\) after profiling the two unknown nuisance parameters. The same design time is applied to all three counters. This is not a comparison of arbitrary sensor placements, a multi-time observation schedule, or a global estimator risk.

Write \(h=a^2/(4D)\) and
\[
g(t)=A t^{-1/2}e^{-\kappa t-h/t},\qquad p(t)=\frac{g(t)}{b+g(t)}.
\]

## Proof

**1. Nuisance elimination.** At nominal \(\theta=0\), the two wing means are both \(b+g\), while the central mean is \(b+A t^{-1/2}e^{-\kappa t}\). The gradient of the Poisson means with respect to \(\theta\) is antisymmetric, with components \(-ag/(2Dt),0,ag/(2Dt)\). The gradients with respect to \(A\) and \(b\) are symmetric. Therefore the \(\theta\)-score is Fisher-orthogonal to both nuisance scores. The nuisance block is positive definite, because the central and wing signal responses to \(A\) differ strictly whenever \(a,t>0\). The Schur complement for \(\theta\) consequently equals the diagonal Fisher entry:
\[
\boxed{J(t)=\mathcal I_{\theta\mid A,b}(t)
=\frac{a^2}{2D^2t^2}\frac{g(t)^2}{b+g(t)}.}
\]
This identity uses the actual independent Poisson likelihood, not a Gaussian measurement approximation.

**2. Uniqueness.** Put \(z=\log t\) and \(L(z)=\log g(e^z)=\log A-z/2-\kappa e^z-he^{-z}\). Then
\[
L'(z)=-\tfrac12-\kappa e^z+he^{-z},\qquad
L''(z)=-\kappa e^z-he^{-z}<0.
\]
Write \(p=e^L/(b+e^L)\). Differentiating the logarithm of the efficient information gives
\[
\frac{d}{dz}\log J(e^z)=-2+(2-p)L',
\]
\[
\frac{d^2}{dz^2}\log J(e^z)
=(2-p)L''-p(1-p)(L')^2<0.
\]
Thus \(J\) is *strictly log-concave in log time*. Moreover \(J(t)\to0\) at both \(t\downarrow0\) and \(t\to\infty\), including when \(\kappa=0\). Hence exactly one global maximizer exists. Its equation is
\[
\boxed{(2-p(t_*))\left(\frac h{t_*}-\kappa t_*-\frac12\right)=2.}
\]

**3. Sharp background limits and strict monotonicity.** At the optimum \(0<p<1\); therefore
\[
1<\frac{2}{2-p}<2,
\]
so \(3/2<h/t_*-\kappa t_*<5/2\). The function \(h/t-\kappa t\) decreases strictly on positive times. Its level-\(\alpha\) solution is precisely \(T_\alpha\), yielding \(T_{5/2}<t_*<T_{3/2}\). Let \(F(z,b)=-2+(2-p(e^z,b))L'(z)\). At its unique root \(L'>0\). Since \(\partial_b p=-g/(b+g)^2<0\), we have \(\partial_b F>0\); meanwhile \(\partial_z F<0\) by step 2. Implicit differentiation proves \(dt_*/db>0\). Taking \(b\downarrow0\) and \(b\to\infty\) in the root equation gives respectively \(p\to1\) and \(p\to0\), and the stated endpoint times.

**4. Sharp \(5/3\) factor.** Write \(r=T_{3/2}/T_{5/2}>1\) and \(u=T_{5/2}>0\). The defining quadratic identities \(h=(5/2)u+\kappa u^2=(3/2)ru+\kappa r^2u^2\) imply
\[
\frac{5-3r}{2}=\kappa u(r^2-1)\ge0.
\]
Consequently \(r\le5/3\), with equality if and only if \(\kappa=0\). Finally the wing mean signal \(g(t)\) reaches its maximum when \(L'=0\), whereas \(L'(\log t_*)>0\), so the information-optimal observation is strictly earlier than the signal peak.

**5. Exact illustrative instance.** With \(a=2,D=A=1,\kappa=0\), choose \(b=e^{-2}/\sqrt2\). At \(t=1/2\), \(g=\sqrt2e^{-2}=2b\), hence \(p=2/3\) and \(L'=3/2\), exactly solving the stationarity equation. Therefore \(t_*=1/2\), between the sharp background endpoints \(T_{5/2}=2/5\) and \(T_{3/2}=2/3\). The wing signal itself peaks at \(t=2\). All conclusions about uniqueness and global optimality follow from the preceding proof, not numerical testing.

## Verification

Run `python3 verify.py`. It evaluates the full three-parameter Poisson Fisher matrix by independent summation, checks orthogonality and its nuisance Schur complement numerically, checks the exact instance, tests the analytic stationarity condition, and samples randomly selected positive physical parameters to test bracketing, concavity and monotonic behavior. The numerical tests are diagnostics only; the proof covers the complete stated parameter domain.

## Relationship to prior work

The source-apportionment study of Chrapkiewicz et al. (public preprint of 18 January 2024, published May 2024) develops concentration inversion and a network-topology strategy for selecting river-sampling *locations*; it specifically identifies temporal sampling as an avenue for further work. It does not supply this one-shot transient Poisson timing theorem. Newman et al. (arXiv:2408.01298, 2 August 2024) jointly infer atmospheric Gaussian-plume source parameters and background by Bayesian MCMC, but study continuous-emission models and do not derive the present efficient-information timing rule. Pomareda et al. (2017) explicitly include chemical background in mobile plume localization, with a concentration likelihood and spatial exploration algorithm rather than the transient Poisson c-optimal observation age.

A published mathematical research result titled *A strict separation between joint-parameter and location-only optimal Gaussian-plume transects* examines the same type of three-counter nuisance orthogonality, but optimizes **sensor spacing at fixed plume width and exposure**, not elapsed time under diffusive broadening \(\sigma^2\propto t\), a decaying source height and fixed ambient background. Its fixed-width scalar spacing result does not imply either the present optimal-time equation or the sharp \(5/3\) background-delay bound. This comparison is an implication check, not a claim that nuisance-orthogonality itself is new.

## Limitations

The theorem is an idealized **local c-optimal Fisher-information** result. It presupposes a single perfectly Gaussian transversal pulse, known diffusion and first-order-loss constants and release age, fixed spatially uniform independent Poisson background, and synchronized short sensor exposures. Real flow advection, turbulent fluctuations, cross-sensor dependence, unknown transport parameters, temporal release uncertainty and calibration drift are outside scope. Its strict \(5/3\) guarantee concerns the ratios of the two **limiting optimal times**, not a bound on absolute time shifts or field error. Classical Cramér–Rao information is not a finite-sample accuracy guarantee. Historical originality is provisional against unlocated specialized design theory.

## References

1. Chrapkiewicz, K., Lipp, A. G., Barron, L. P., Barnes, R., and Roberts, G. G., *Apportioning sources of chemicals of emerging concern along an urban river with inverse modelling*, public preprint 18 January 2024, DOI: https://doi.org/10.31223/X52T22; published 2024, DOI: https://doi.org/10.1016/j.scitotenv.2024.172827 .
2. Newman, T., Nemeth, C., Jones, M., and Jonathan, P., *Probabilistic Inversion Modeling of Gas Emissions: A Gradient-Based MCMC Estimation of Gaussian Plume Parameters*, arXiv posted 2 August 2024, https://arxiv.org/abs/2408.01298 .
3. Pomareda, V. et al., *Chemical Source Localization Fusing Concentration Information in the Presence of Chemical Background Noise*, Sensors 17 (2017) 904, DOI: https://doi.org/10.3390/s17040904 .
4. *A strict separation between joint-parameter and location-only optimal Gaussian-plume transects*, published published-finding corpus mathematical research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-a-strict-separation-between-joint-parameter-and-location-only-op--79a14601ec93 .
