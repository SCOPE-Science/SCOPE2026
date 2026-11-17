# Critical physical-time laws and a logarithmic ripple in monomial sewed-focus dynamics

## Finding

For a natural two-exponent family of nonanalytic planar crossing flows, the critical ratio of the exponents is exactly one. Below it, positive crossing radii converge to a nonzero attracting cycle; at it, there is a continuum of closed orbits; above it, initial crossing radii below one spiral into a sewed singularity in finite *physical* time. The collapse time has two sharp, distinct asymptotic laws:

**Exponent-coalescence law.** Fix \(0<a<1\), let \(\kappa\downarrow1\), and write \(h=\log\kappa\) and \(L=-\log a\). Then
\[
T_\kappa(a)=\frac{2E_1(L)}h+\frac{aL}{6}h+O_a(h^3),
\qquad E_1(L)=\int_L^\infty\frac{e^{-u}}u\,du.
\]
In particular the entire constant-order term cancels; the coefficient of \(h\) is explicit.

**Cycle-boundary law.** For fixed \(\kappa>1\), define the uniformly absolutely convergent function
\[
P_\kappa(\theta)=\sum_{j\le0}\left(e^{-\kappa^{j-\theta}}-1\right)
+\sum_{j\ge1}e^{-\kappa^{j-\theta}}-\theta.
\]
It is real analytic, nonconstant and one-periodic. As \(a\uparrow1\), writing \(L=-\log a\) and \(u=\log(1/L)/\log\kappa\),
\[
T_\kappa(a)=\frac{2\log(1/L)}{\log\kappa}
+1+2P_\kappa(\{u\})+O_\kappa(L).
\]
Thus the collapse delay diverges logarithmically with an intrinsically nonconstant logarithmic-scale ripple. The Fourier coefficients of its derivative have the exact form
\[
\widehat{P_\kappa'}(m)=\Gamma\!\left(1+\frac{2\pi i m}{\log\kappa}\right),\qquad m\in\mathbb Z\setminus\{0\}.
\]
These statements quantify physical time along a family of trajectories; they do not claim a new general classification of all piecewise-smooth singularities.

## Assumptions and scope

For real \(p,q>3\), put \(\kappa=q/p\) and consider the vector field on the two open half-planes divided by the switching line \(y=0\):
\[
\begin{aligned}
 y>0:&\quad \dot x=1,\qquad
 \dot y=\begin{cases}q(-x)^{q-1},&x<0,\\-px^{p-1},&x\ge0;\end{cases}\\
 y<0:&\quad \dot x=-1,\qquad
 \dot y=\begin{cases}p(-x)^{p-1},&x<0,\\-qx^{q-1},&x\ge0.\end{cases}
\end{aligned}
\]
Each half-plane field is \(C^2\) in \(x\) (with a continuous second derivative at \(x=0\)); both vertical components have sign opposite to \(x\) on \(y=0\) away from the origin, so all nonzero switching intersections are transverse and the crossing trajectory is unambiguous. At the singular origin no continuation past the accumulation time is asserted.

Start on the negative switching section at \((-a,0)\), \(a>0\), entering the upper half-plane, and let \(a_r\) be the radius of the \(r\)-th subsequent intersection, alternating in sign. We consider the crossing itinerary and its physical elapsed time (not an arbitrary parametrization). The stable-cycle and critical statements concern these section-started trajectories. The two asymptotics concern respectively fixed \(a\in(0,1)\) with \(\kappa\downarrow1^+\), and fixed \(\kappa>1\) with \(a\uparrow1^-\); they are not claimed uniformly in a simultaneous double limit.

## Proof

**Exact return law.** On the upper half-flight, the integral of the positive vertical field from \(-a\) to \(0\) is \(a^q\). On the positive part of this flight the downward integral is \(b^p\). The first positive switching intersection therefore occurs at \(b=a^{q/p}=a^\kappa\). The lower flight is symmetric in the same power matching, giving the next negative intersection radius \(b^\kappa\). Consequently
\[
a_r=a^{\kappa^r},\quad R(a)=a^{\kappa^2},\quad R'(1)=\kappa^2.
\]
Each half-flight takes time \(a_{r-1}+a_r\), because the horizontal speed has modulus one. Hence for \(\kappa>1\) and \(0<a<1\),
\[
T_\kappa(a)=a+2\sum_{r=1}^\infty a^{\kappa^r}<\infty.
\]
The radii decay superexponentially in \(r\), and the maximal vertical excursion during each half-flight is a positive power of its starting radius, hence also tends to zero. Thus the trajectory tends to \((0,0)\) at this finite time. The sum converges by comparing its tail with a geometric sequence after the powers are smaller than a fixed number below one. If \(\kappa=1\), each section radius is fixed, giving closed orbits with physical period \(4a\). If \(0<\kappa<1\), every \(a>0\) has \(a^{\kappa^r}\to1\), and the unique nonzero section cycle at \(a=1\) is attracting with multiplier \(\kappa^2\). For \(\kappa>1\), it is repelling and radii above one diverge; since half-flight times then grow without bound, this divergence is not a finite-time escape. No other nonzero periodic crossing itineraries exist because the power return has no other positive fixed points. A periodic trajectory cannot remain strictly within one half-plane, where \(\dot x\) is constant and nonzero.

**Exponent-coalescence asymptotic.** Define \(\phi(t)=\exp(-L e^t)\), so \(\sum_{r\ge1} a^{\kappa^r}=\sum_{r\ge1}\phi(rh)\). The substitution \(u=Le^t\) gives \(\int_0^\infty\phi(t)\,dt=E_1(L)\). For each fixed \(L>0\), the smooth function \(\phi\) and all its derivatives are integrable. The half-line Euler--Maclaurin expansion gives
\[
\sum_{r=1}^\infty\phi(rh)=\frac{E_1(L)}h-\frac{\phi(0)}2-\frac h{12}\phi'(0)+O_L(h^3).
\]
Since \(\phi(0)=a\) and \(\phi'(0)=-aL\), substitution in \(T_\kappa(a)=a+2\sum\phi(rh)\) cancels the constant term and yields exactly the claimed \(aLh/6\) correction. The next coefficient, not required for the principal claim, is \(a(-L^3+3L^2-L)h^3/360\), confirming the stated remainder order.

**Boundary log-periodicity and nonconstancy.** Fix \(\kappa>1\) and write \(u=\log_\kappa(1/L)=N+\theta\), \(N=\lfloor u\rfloor\), \(0\le\theta<1\). Shifting the index \(j=r-N\) in the series gives
\[
\sum_{r\ge1} e^{-L\kappa^r}=N+F_\kappa(\theta)+O_\kappa(L),\qquad
F_\kappa(\theta)=P_\kappa(\theta)+\theta.
\]
Indeed the omitted terms in the negative tail differ from their limiting value one by at most \(\sum_{j\le-N}\kappa^{j-\theta}\le C_\kappa L\). Positive tails decay superexponentially. The relation \(F_\kappa(\theta+1)=F_\kappa(\theta)+1\) proves periodicity of \(P_\kappa\), and \(a=1+O(L)\) proves the formula for \(T_\kappa\).

Termwise differentiation is valid locally uniformly, and with \(h=\log\kappa\),
\[
F_\kappa'(\theta)=h\sum_{j\in\mathbb Z}\kappa^{j-\theta}e^{-\kappa^{j-\theta}}.
\]
For each integer \(m\), unfold the period-one integral using \(x=j-\theta\), then substitute \(v=e^{hx}\):
\[
\int_0^1 F_\kappa'(\theta)e^{-2\pi i m\theta}\,d\theta
=\int_0^\infty e^{-v}v^{2\pi i m/h}\,dv
=\Gamma\left(1+\frac{2\pi i m}h\right).
\]
For nonzero \(m\), the Fourier coefficient of \(P_\kappa'=F_\kappa'-1\) is the same. Euler's Gamma function has no zeros, so \(P_\kappa\) is genuinely nonconstant for *every* \(\kappa>1\). The uniform convergence of the differentiated series on compact complex strips near the real axis also gives real analyticity. This completes the proof.

## Verification

The accompanying standalone Python file `verify.py` checks exact rational matching identities for the \(p=4,q=8\) specialization, the center return, multiple independently evaluated branch matches, the small-\(h\) Euler--Maclaurin correction, the discrete-scale periodicity, and fixed-\(\kappa\) near-cycle asymptotics. Run from a Python 3 standard-library installation with `python3 verify.py`. The expected final lines are `SEWED_FOCUS_EXACT_BRANCH_IDENTITIES_OK 29` and `SEWED_FOCUS_CRITICAL_E1_AND_LOGPERIODIC_CHECK_OK`. Finite numerical checks are corroboration, not proof of infinite parameter ranges, analytic nonconstancy, or mathematical originality.

## Relationship to prior work

Glendinning, Hogan, Homer, Jeffrey and Szalai introduced the explicit asymmetric monomial sewed-focus mechanism in their open-access 2023 paper (Theorem 3 and equations (13)--(15)); they already proved finite-time approach for one exponent ratio \(\kappa=2\) and allowed other smoothness orders. Thus the recurrence and existence of finite-time collapse are **prior results in substance**, not new claims. Their proof does not determine the sharp \(\kappa\downarrow1\) physical-time scale, its cancellation of constant order, or the explicit nonconstant logarithmic boundary ripple for arbitrary ratios. The present result derives these quantitative properties for the specified normalized two-power family.

Ordinary Euler--Maclaurin summation and Mellin/Fourier periodization are established tools; no originality is claimed for those methods. What is asserted is their exact application to the two singular physical-time limits of this sewed-focus flow. Searches can miss equivalent treatments of lacunary series or supplementary material; independent novelty verification is still needed.

## Limitations

The results are exact for the stated piecewise power-law vector field, section-started crossing trajectories and parameter regimes. They do not establish an all-parameter classification of arbitrary sewed foci, do not prescribe passage through the singular origin after finite-time accumulation, and do not cover a simultaneous uniform limit of \(\kappa\downarrow1\) and \(a\uparrow1\). The ripple may be numerically minute for some ratios, but is analytically nonzero. Nonzero periodic orbit uniqueness is a statement about the specified section map; no external independent audit has been performed.

## References

1. P. Glendinning, S. J. Hogan, M. Homer, M. R. Jeffrey and R. Szalai, *Uncountably Many Cases of Filippov's Sewed Focus*, Journal of Nonlinear Science 33, article 52 (first published 5 May 2023), DOI: 10.1007/s00332-023-09910-4. Open full text: https://link.springer.com/article/10.1007/s00332-023-09910-4 ; open author preprint: https://arxiv.org/html/2306.09743v1 (posted 16 June 2023).
2. A. F. Filippov, *Differential Equations with Discontinuous Righthand Sides*, Kluwer, 1988, especially the discussion of type-3 singularities, as cited and summarized in reference 1.
3. Classical Euler--Maclaurin summation and the Mellin integral for Euler's Gamma function, used here with derivations supplied in the proof above.
