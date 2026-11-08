# An exact conserved quantity and neutral oscillation annulus at critical collective-risk feedback

## Finding

In the well-mixed collective-risk cooperation–risk model with linear environmental feedback, the critical parameter \(u=(M-1)/(N-M)\) is an **integrable nonlinear-center threshold**. There is an explicit first integral on the entire open state square. Whenever the interior equilibrium is biologically admissible, it is surrounded by a continuum of regular, non-attracting periodic orbits. This distinguishes neutral closed orbits from an isolated stable limit cycle at the exactly tuned critical parameter.

For integers \(1<M<N\), write \(m=M-1\), \(n=N-M\), \(d=m+n=N-1\), and
\[
\Gamma(x)=\binom{d}{m}x^m(1-x)^n,\qquad
x_* = \frac{m}{d},\qquad
r_* = \frac{c}{b\Gamma(x_*)}.
\]
Take \(b,c,\varepsilon>0\), \(u=m/n\), and assume \(0<r_*<1\). Let
\[
s=\log\frac{r}{1-r},\quad s_*=\log\frac{r_*}{1-r_*},\quad
a=\frac{nc}{\varepsilon},\quad q=\frac{nb}{\varepsilon}.
\]
Then the function
\[
\boxed{\;H(x,r)=\frac{e^{-as}}{\Gamma(x)}
+q\int_{s_*}^{s}\frac{e^{-av}}{1+e^{-v}}\,dv\;}
\]
is constant on every solution in \((0,1)^2\). In particular the unique interior equilibrium \((x_*,r_*)\) is a nondegenerate local minimum; every sufficiently small positive energy level is one periodic trajectory, and these levels form an annulus.

The periods of the small cycles approach
\[
\boxed{\;T_*=2\pi\sqrt{\frac{d\varepsilon}{mc(1-r_*)}}\;}.
\]

## Assumptions and scope

The exact published System I is
\[
\varepsilon\dot{x}=x(1-x)[b r\Gamma(x)-c],\qquad
\dot r=r(1-r)[u(1-x)-x].
\]
Here \(x\) is the cooperator fraction, \(r\) is the disaster risk, and the group threshold obeys \(1<M<N\). The state domain is the open square \(0<x<1\), \(0<r<1\). All speeds and payoff parameters are positive. The feedback strength is exactly \(u=(M-1)/(N-M)\). The admissibility inequality \(0<c<b\Gamma(x_*)\) is necessary for the interior equilibrium and periodic annulus; the formula for the first integral itself still makes sense with an arbitrary fixed lower integration endpoint in place of \(s_*\), even without this inequality.

Claims concern only the linear-feedback model, not the distinct sigmoid-feedback system, off-critical feedback, stochastic finite populations, or trajectories on the boundary of the square.

## Proof

**1. Exact reduction.** Introduce the logit risk coordinate \(s=\log(r/(1-r))\), so \(r=\sigma(s)=(1+e^{-s})^{-1}\). At the critical feedback value,
\[
\dot s=u(1-x)-x=\frac{m-dx}{n}.
\]
Since \(\Gamma'(x)/\Gamma(x)=m/x-n/(1-x)=(m-dx)/(x(1-x))\), the cooperation equation yields
\[
\frac{d}{dt}\log\Gamma(x)=\frac{m-dx}{\varepsilon}[b r\Gamma(x)-c].
\]
Consequently, with \(Y(x)=1/\Gamma(x)\),
\[
\dot Y=\frac n\varepsilon[cY-br]\dot s=(aY-q\sigma(s))\dot s.
\]
Multiplying by \(e^{-as}\) gives
\[
\frac{d}{dt}(e^{-as}Y)=-q e^{-as}\sigma(s)\dot s.
\]
The displayed \(H\) has the opposite integral derivative; hence \(\dot H=0\) identically throughout the open square. This does not depend on a perturbation expansion or numerical approximation.

**2. Critical point and its positive Hessian.** The derivative of \(H\) in the coordinates \((x,s)\) is
\[
H_x=e^{-as}Y'(x),\qquad H_s=e^{-as}[-aY(x)+q\sigma(s)].
\]
The positive function \(\Gamma\) has its unique maximum at \(x_*=m/d\), so \(Y'(x_*)=0\), and \(H_s(x_*,s_*)=0\) is equivalent to \(br_*\Gamma(x_*)=c\). This is the sole interior critical point. The cross-derivative vanishes there, while
\[
H_{xx}(x_*,s_*)=
\frac{e^{-as_*}}{\Gamma(x_*)}
\left(\frac m{x_*^2}+\frac n{(1-x_*)^2}\right)>0,
\]
and
\[
H_{ss}(x_*,s_*)=e^{-as_*}q r_*(1-r_*)>0.
\]
Thus the Hessian is positive definite. The logit is a smooth local diffeomorphism, so the center statement transfers to \((x,r)\) coordinates.

**3. Nonlinear center and periodic annulus.** By the Morse lemma, sufficiently small levels \(H=H(x_*,r_*)+h\), \(h>0\), are smooth simple closed curves strictly inside the state square. The only interior equilibrium is \((x_*,r_*)\), so the vector field never vanishes on such a level; conservation makes the nonzero vector field tangent to the curve. Therefore it circulates periodically and every such level is a distinct periodic orbit. Since nearby levels are also invariant, no such periodic orbit is asymptotically attracting or an isolated limit cycle. The nonlinear center is Lyapunov stable but not asymptotically stable.

**4. Small-cycle clock.** At the interior equilibrium, the Jacobian has trace zero and off-diagonal entries
\[
F_r=\frac{x_*(1-x_*)b\Gamma(x_*)}{\varepsilon}>0,
\quad G_x=-\frac d n r_*(1-r_*)<0.
\]
The diagonal entries vanish. Hence the eigenvalues are \(\pm i\omega\), where
\[
\omega^2=-F_rG_x=\frac{mc}{d\varepsilon}(1-r_*)>0.
\]
The standard small-oscillation limit for smooth nondegenerate centers gives \(T(h)\to 2\pi/\omega\), proving the stated formula.

## Verification

The accompanying standalone `verify.py` checks the exact derivative identity symbolically for every integer pair \(1\le m,n\le5\), the equilibrium Jacobian frequency identity, and the positive curvature formula (\(75\) symbolic assertions). It also integrates the source's numerical case \(N=6\), \(M=3\), \(b=1\), \(c=0.1\), \(\varepsilon=0.1\), \(u=2/3\), for which \(x_*=2/5\), \(r_*=125/432\). With stringent numerical tolerances, the computed integral drifts by less than \(10^{-9}\) over the tested interval; integration is a consistency check only. The proof above, not the finite test, establishes conservation and the full annulus.

Reproduce with `python verify.py` (requires `sympy`, `scipy`, and `numpy`).

## Relationship to prior work

Liu, Chen, and Szolnoki introduce precisely these two differential equations as System I (their equation (5)), locate the purely imaginary spectral threshold at \(u=(M-1)/(N-M)\), and exhibit oscillatory phase portraits. Their Appendix 1 reports a numerical first Lyapunov coefficient approximately \(-1.4\times10^{-8}\) and interprets the threshold through a supercritical Hopf scenario. The exact first integral and resulting nonisolated local periodic annulus give a mathematically stronger, model-specific characterization of the *critical* flow. This does not refute oscillatory dynamics away from the exact critical value and does not assert the entire open square consists of cycles.

Weitz and collaborators (2016) established general feedback-evolving games with oscillatory tragedy-of-commons dynamics in two-player environments; their model is not the binomial threshold-risk payoff or the exact conserved quantity above. Zhang, Yang, Han, and Xia (2025) study another threshold-public-goods risk-feedback framework and manifold control. The accessible abstract does not establish an equivalent conserved integral; its complete publisher text was unavailable for comparison, which remains a priority risk. The claimed novelty is consequently best-knowledge, not an assertion of universal uniqueness.

## Limitations

The first integral is defined on the open square and may diverge near its boundary. The theorem proves a local annulus near the interior equilibrium, not global foliation, exact finite-amplitude periods, or a complete classification of all boundary basins. It requires the critical linear feedback and an admissible interior equilibrium; results at noncritical feedback, for exponential feedback, or with demographic noise are not claimed. No independent external validation has been performed. Other equivalent conserved-coordinate descriptions may exist in unindexed works or inaccessible full texts.

## References

1. Liu, L., Chen, X., and Szolnoki, A. *Coevolutionary dynamics via adaptive feedback in collective-risk social dilemma game*. Preprint first posted 2022-12-20, bioRxiv DOI: https://doi.org/10.1101/2022.12.19.520980. eLife **12**, e82954 (2023), https://doi.org/10.7554/eLife.82954; author-preprint full text https://arxiv.org/abs/2305.00253, especially System I and Appendix 1.
2. Weitz, J. S., Eksin, C., Paarporn, K., Brown, S. P., and Ratcliff, W. C. *An oscillating tragedy of the commons in replicator dynamics with game-environment feedback*. PNAS **113** (2016), E7518–E7525. https://doi.org/10.1073/pnas.1604096113.
3. Zhang, Z., Yang, C., Han, W., and Xia, C. *Co-evolutionary dynamics of threshold PGGs with collective-risk environment feedback*. Physica A **658** (2025), 130275. https://doi.org/10.1016/j.physa.2024.130275 (abstract reviewed; publisher full text not accessible).
