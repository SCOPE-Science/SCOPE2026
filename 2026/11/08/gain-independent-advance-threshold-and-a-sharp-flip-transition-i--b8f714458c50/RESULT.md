# Gain-independent advance threshold and a sharp flip transition in a sampled inhibitory neuron

## Finding

Consider a scalar neural-feedback equation with a fixed within-cell sampling phase. Its exact phase boundary separates unconditional exponential stabilization by a sufficiently advanced sample from a sharp gain-induced flip and a stable anti-periodic orbit. At the critical gain, convergence remains global but becomes algebraic.

More precisely, fix \(a>0\), \(g>0\), \(0\leq\theta\leq1\), and define
\[
\gamma(t)=\lfloor t\rfloor+\theta,\qquad
\dot x(t)=-a x(t)-g\tanh(x(\gamma(t)))\quad(t\in[k,k+1),\ k=0,1,\ldots).
\]
We require continuity at integers, and at \(\theta=1\) use the left limit at each right endpoint. Given any real initial value \(x(0)\), there exists a unique global continuous trajectory.

Put \(E=e^{-a}\), \(F=e^{-a\theta}\), \(\Delta=2F-1-E\), and
\[
\theta_*(a)=-\frac1a\log\frac{1+e^{-a}}2\in(0,1).
\]
If \(\theta\geq\theta_*(a)\), the zero solution is globally exponentially attractive for **every finite** \(g>0\). If \(0\leq\theta<\theta_*(a)\), define
\[
 g_c=\frac{a(1+E)}{\Delta}.
\]
For \(0<g<g_c\), zero is globally exponentially attractive. At \(g=g_c\), it is globally asymptotically attractive but not exponentially attractive. For every initial condition whose integer-time orbit does not hit zero in finitely many steps,
\[
|x(k)|\sim(2Kk)^{-1/2},\qquad
K=\frac{(g_c/a)(1-E)F^3}{3[1+(g_c/a)(1-F)]^4}>0.
\]
The finite-hitting exceptional initial conditions converge to zero even faster and must not be included in this asymptotic formula.

When \(g>g_c\), zero is unstable and there is exactly one **symmetric** nonzero integer-time two-cycle \(\{c,-c\}\), which is locally asymptotically stable. With \(C=\Delta/(1-E)>0\), its amplitude is characterized by
\[
\frac{\tanh(Cc)}{Cc}=\frac{g_c}{g},\qquad c>0.
\]
It corresponds to an actual continuous-time anti-periodic orbit satisfying \(x(t+1)=-x(t)\). Moreover,
\[
c=\frac1C\sqrt{\frac{3(g-g_c)}{g_c}}\,[1+O(g-g_c)]
\quad\text{as }g\downarrow g_c.
\]
There is no nonzero time-one-periodic solution for any parameters. The claim of uniqueness refers to **symmetric** two-cycles, not to all two-cycles or all attractors.

## Assumptions and scope

All parameters are constant and real. The nonlinearity is exactly \(\tanh\), the within-cell sample is \(k+\theta\), and there are no external drives or impulses. The statement concerns every \(k\geq0\), every finite \(g>0\), and all real initial states. The phase \(\theta\) is dimensionless because the mesh spacing is one. The primary classification is MSC2020 34K13.

The use of an advanced argument does not make the problem ill-posed: on each unit interval the unknown sample value solves a strictly monotone scalar equation. Attraction is claimed for all full trajectories precisely in the regimes where the mesh map is contractive; above the flip threshold, only local stability of the exhibited cycle is asserted.

## Proof

Write \(h=g/a\) and \(x_k=x(k)\). Variation of constants on the interval \([k,k+1]\) gives, for \(0\leq s\leq1\),
\[
x(k+s)=e^{-as}x_k-h(1-e^{-as})\tanh(u_k),\qquad u_k=x(k+\theta).
\]
Therefore
\[
 u_k+h(1-F)\tanh(u_k)=F x_k,\qquad
 x_{k+1}=P(x_k)=E x_k-h(1-E)\tanh(u_k).\tag{1}
\]
Since the derivative of the left side of the first equation is \(1+h(1-F)\operatorname{sech}^2u>0\), it maps the line bijectively to itself. Thus (1) defines a unique global trajectory and an odd smooth mesh map \(P\). Also \(u_k\) has the same sign as \(x_k\), and \(|u_k|\leq F|x_k|\).

Implicit differentiation gives
\[
P'(x)=E-\frac{h(1-E)F\operatorname{sech}^2u(x)}{1+h(1-F)\operatorname{sech}^2u(x)}.\tag{2}
\]
The ratio on the right is strictly increasing in \(\operatorname{sech}^2u\), while this squared secant is strictly decreasing with \(|x|\). Hence \(P'(x)\) is strictly increasing with \(|x|\) away from zero, and
\[
M:=P'(0)=E-\frac{h(1-E)F}{1+h(1-F)}\leq P'(x)<E<1,\qquad
1+M=\frac{1+E-h\Delta}{1+h(1-F)}.\tag{3}
\]
If \(\Delta\leq0\), then \(M>-1\) for every finite \(h>0\). If \(\Delta>0\), then \(M>-1\) exactly when \(h<(1+E)/\Delta\). In either case \(\sup_{x\in\mathbb R}|P'(x)|=\max\{|M|,E\}<1\), so the mean-value theorem makes \(P\) a global contraction. The explicit interpolation in (1) gives \(|x(k+s)|\leq(1+h)|x_k|\); hence contraction at mesh times implies global exponential attraction in continuous time. The equivalence \(\Delta\leq0\iff\theta\geq\theta_*(a)\) follows by solving \(2e^{-a\theta}\leq1+e^{-a}\). The threshold lies in \((0,1)\) because \(e^{-a}<(1+e^{-a})/2<1\).

For every positive \(x\), equation (1) has \(u(x)>0\), so \(P(x)=E x-h(1-E)\tanh(u(x))<x\), proving that zero is the only fixed point by oddness.

At \(h=h_c=(1+E)/\Delta\), equation (3) gives \(M=-1\). Strict monotonicity of the derivative away from zero yields \(-1<P'(x)<1\) for \(x\ne0\). Integration from zero then gives \(-|x|<P(x)<|x|\) for \(x>0\), with the symmetric statement for negative \(x\). Thus \(|P(x)|<|x|\) for all \(x\ne0\), and every integer orbit converges to zero (either eventually zero or strictly decreasing in modulus). The nonzero differential at the fixed point has modulus one, excluding exponential attraction uniformly on a neighborhood.

The first nonvanishing correction is obtained by solving the implicit equation to third order. With \(b=h(1-F)\),
\[
u(x)=\frac{F}{1+b}x+\frac{bF^3}{3(1+b)^4}x^3+O(x^5),\qquad
\tanh u(x)=\frac{F}{1+b}x-\frac{F^3}{3(1+b)^4}x^3+O(x^5).
\]
Consequently \(P(x)=-x+Kx^3+O(x^5)\) with \(K\) as specified. Any orbit not hitting zero eventually alternates sign; its positive magnitude obeys \(z_{k+1}=z_k-Kz_k^3+O(z_k^5)\). Therefore \(z_{k+1}^{-2}-z_k^{-2}=2K+O(z_k^2)\to2K\), and Cesàro summation gives \(kz_k^2\to1/(2K)\). Isolated preimages of zero are a necessary exception, since the odd map can cross zero again away from the origin.

If \(h>h_c\), then \(P'(0)<-1\), proving linear instability. Suppose \(P(c)=-c\) with \(c>0\). The endpoint equation and implicit equation (1) imply, respectively, \(h(1-E)\tanh u=(1+E)c\) and \(u=Cc\). Thus the cycle equation is
\[
\frac{\tanh(Cc)}{Cc}=\frac{h_c}{h}.
\]
The function \(z\mapsto\tanh z/z\) is strictly decreasing from one to zero on \((0,\infty)\): its derivative has numerator \(z\operatorname{sech}^2z-\tanh z<0\), since the opposite difference has derivative \(2z\operatorname{sech}^2z\tanh z>0\) and vanishes at zero. This proves existence and uniqueness of \(c\). Further, \(\operatorname{sech}^2(Cc)<\tanh(Cc)/(Cc)=h_c/h\). Substitution in (2)-(3), using the strict monotonicity of \(P'\) with decreasing squared secant, yields \(-1<P'(c)<E<1\). Oddness gives the same derivative at \(-c\); the second iterate has multiplier \(P'(c)^2<1\), so the two-cycle is locally attracting. The within-cell formula then extends it to a full anti-periodic continuous-time solution. Finally \(\tanh z/z=1-z^2/3+O(z^4)\) yields the stated square-root onset of \(c\).

## Verification

The standalone file `verify.py` implements the implicit sample solve by bracketing and binary search and tests the threshold, implicit derivative, oddness, contraction, existence and stability of the two-cycle, and critical algebraic relaxation. With standard Python 3 it prints `VERIFY_OK parameter_checks=339 critical_algebraic_cases=3`. These finite tests are complementary to, not a substitute for, the analytic proof. Reproduce by running `python verify.py` from a directory containing the embedded file.

## Relationship to prior work

Torres Naranjo and Castillo Apolonio (arXiv:2610.36560, initially public October 27, 2026) study Hopfield-type neural networks with generalized piecewise constant arguments; their full text gives sufficient Lipschitz/Gronwall criteria for periodic attraction, including a nonimpulsive case and a two-neuron `tanh` example. The present result concerns a natural scalar autonomous inhibitory specialization but derives its **exact** all-gain phase boundary, a sharp supercritical flip, and the critical convergence law, none of which follows from those sufficient conditions.

Earlier Akhmet–Aruğaslan–Yilmaz (2010), Akhmet–Aruğaslan Çinçin–Cengiz (2018), and Chiu (2026) study neural networks with similar generalized arguments and sufficient stability criteria. Their available abstracts do not assert this precise nonlinear transition. Full-text access to some of these potential historical antecedents was unsuccessful, so priority is not exhaustively certified.

## Limitations

The classification concerns one inhibitory cell with a single within-mesh sampled nonlinearity, not arbitrary neural-network dimensions, variable coefficients, external forces, or impulses. Above the threshold the theorem gives exactly one **symmetric** attracting 2-cycle; it does not classify all possible periodic orbits or basins at large gain. The critical inverse-square law excludes the finite-hitting set. Historical priority remains subject to examination of inaccessible full texts; no independent scientific audit has been performed.

## References

1. R. Torres Naranjo and S. Castillo Apolonio, *Periodic Solutions and Exponential Attractivity in Hopfield-Type Neural Networks with Generalized Piecewise Constant Arguments: Impulsive and Nonimpulsive Cases*, arXiv:2610.36560 (first submitted 2026-10-27), https://arxiv.org/abs/2610.36560 .
2. M. U. Akhmet, D. Aruğaslan and E. Yilmaz, *Stability analysis of recurrent neural networks with piecewise constant argument of generalized type*, Neural Networks **23** (2010), 805–811, https://doi.org/10.1016/j.neunet.2010.05.006 .
3. M. Akhmet, D. Aruğaslan Çinçin and N. Cengiz, *Exponential stability of periodic solutions of recurrent neural networks with functional dependence on piecewise constant argument*, Turkish Journal of Mathematics **42** (2018), 272–292, https://doi.org/10.3906/mat-1606-138 .
4. K.-S. Chiu, *New existence and exponential stability results for periodic solutions in recurrent neural networks with generalized piecewise constant delay via coincidence degree theory*, Mathematical Modelling and Analysis **31** (2026), 476–498, https://doi.org/10.3846/mma.2026.25296 .
