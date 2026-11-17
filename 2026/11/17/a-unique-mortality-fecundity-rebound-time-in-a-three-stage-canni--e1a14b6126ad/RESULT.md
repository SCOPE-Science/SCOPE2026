# A unique mortality–fecundity rebound time in a three-stage cannibalistic population flow

## Finding

A positive three-stage age-structured cannibalism model has a nonempty sharp parameter region in which a small permanent increase of adult mortality **together with its stipulated equal increase of adult fertility** first decreases total population, then causes exactly one crossing of the old population level, and leaves total population strictly higher forever. The crossing is unique for the fully nonlinear flow, not merely in its linearization. An exact positive-convolution formula determines its small-shock limiting time.

Consider the dimensionless system, with parameters \(c,\kappa,m>0\),
\[
\dot x=-x-\kappa xz+y+(c+m)z,\qquad
\dot y=x-y,\qquad
\dot z=y-mz.
\tag{1}
\]
Here \(x,y,z\) are successive nonnegative life-stage populations. The dimensionless juvenile maturation rate and the middle-stage fecundity are both one. The adult death rate \(m\) is linked to adult fecundity \(c+m\), as in the special three-compartment model of Xia, Li and Chou. **This is a coupled parameter intervention, not a claim about increasing death rate while holding fertility fixed.**

The unique positive equilibrium is
\[
E_m=(P_m,P_m,Z_m),\qquad
P_m=\frac{m+c}{\kappa},\quad Z_m=\frac{m+c}{\kappa m},
\quad N_*(m)=\frac{(m+c)(2+m^{-1})}{\kappa}.
\tag{2}
\]
Start at \(E_m\) and, at time zero, replace \(m\) by \(m+\delta\) in **both** occurrences in (1), keeping \(c,\kappa\) fixed. Let \(N_\delta(t)=x_\delta(t)+y_\delta(t)+z_\delta(t)\) and let \(N_0=N_*(m)\).

**Theorem.** If
\[
\boxed{\sqrt{c/2}<m<\frac{1+\sqrt{1+4c}}2,}
\tag{3}
\]
then there exists \(\delta_0=\delta_0(c,\kappa,m)>0\) such that, for every \(0<\delta<\delta_0\), the shocked solution exists for all \(t\ge0\), remains strictly positive, and has a **unique** crossing time \(t_\delta>0\), with
\[
N_\delta(t)<N_0\quad(0<t<t_\delta),\qquad
N_\delta(t)>N_0\quad(t>t_\delta).
\tag{4}
\]
It converges exponentially to \(E_{m+\delta}\), for which \(N_*(m+\delta)>N_*(m)\). The crossing time tends to the unique positive solution \(t_*\) of
\[
\boxed{\frac{\int_0^{t_*}h(s)\,ds}{h(t_*)}
=\frac{m+c-m^2}{2m^2-c},}
\tag{5}
\]
where
\[
\begin{split}
p&=\tfrac12\bigl(3+c/m-\sqrt{5+2c/m+(c/m)^2}\bigr),\\
q&=\tfrac12\bigl(3+c/m+\sqrt{5+2c/m+(c/m)^2}\bigr),\\
h(t)&=\big(e^{-pt}\mathbf1_{t\ge0}*e^{-qt}\mathbf1_{t\ge0}*e^{-mt}\mathbf1_{t\ge0}\big)(t).
\end{split}
\tag{6}
\]
In particular, \(p,q,m>0\) and \(h(t)>0\) for \(t>0\).

The two strict boundaries in (3) have distinct meanings. The lower is the already known steady-state positive-response threshold \(2m^2>c\); the upper is the new short-time under-response threshold \(m^2-m-c<0\). For every \(c>0\), these boundaries leave a nonempty interval. At \(c=m=\kappa=1\), \(t_*\approx1.616150218\) in the dimensionless time variable.

## Assumptions and scope

The conclusion concerns the deterministic ODE (1), positive \(c,\kappa,m\), exactly the pre-shock equilibrium as initial data, and a sufficiently small positive permanent step in the linked adult-mortality/fertility parameter. The original model is a reduced special case of the multi-stage age-structured system, not a statement about its parent age-continuum PDE or arbitrary initial states. The strict inequalities (3) are essential to the sign-stable single-crossing proof. No crossing-count claim is made for large steps or parameters on either boundary.

## Proof

**1. Equilibrium and local stability.** Substituting \(y=x\) and \(z=x/m\) into (1) gives (2). The Jacobian at \(E_m\) is
\[
J=\begin{pmatrix}-(2+c/m)&1&0\\1&-1&0\\0&1&-m\end{pmatrix},
\tag{7}
\]
with characteristic polynomial
\[
\det(sI-J)=(s+m)\bigl(s^2+(3+c/m)s+1+c/m\bigr).
\tag{8}
\]
Its three roots are strictly negative, because the quadratic has two real negative roots \(-p,-q\) with \(p,q>0\). The positive equilibrium is therefore hyperbolically exponentially attracting, uniformly for parameters near any fixed \(m>0\). The shocked initial state \(E_m\) is \(O(\delta)\) from \(E_{m+\delta}\), so sufficiently small shocks stay in a positive attracting neighborhood for all future time and converge exponentially.

**2. Exact short- and long-time signs.** Summing the equations yields the parameter-independent identity
\[
\dot N=y+cz-\kappa xz.
\tag{9}
\]
At time zero, \(\dot N_\delta(0)=0\), while the shocked vector field has \(\dot x_\delta(0)=\delta Z_m\), \(\dot y_\delta(0)=0\), \(\dot z_\delta(0)=-\delta Z_m\). Differentiating (9) therefore gives the **exact**, finite-step identity
\[
\ddot N_\delta(0)=\delta Z_m\frac{m^2-m-c}{m}<0.
\tag{10}
\]
The equilibrium difference is also exact:
\[
N_*(m+\delta)-N_*(m)
=\frac{\delta}{\kappa}\left(2-\frac{c}{m(m+\delta)}\right)>0
\quad\text{under (3).}
\tag{11}
\]
Hence an initial dip and eventual rebound must occur. The remaining issue is proving there is exactly one crossing.

**3. Exact susceptibility.** Differentiate the shocked solution with respect to \(\delta\) at zero. The variational solution \(v\) satisfies \(\dot v=Jv+w\), \(v(0)=0\), with \(w=Z_m(1,0,-1)^T\). Set \(F(t)=(1,1,1)v(t)\). Direct inversion gives
\[
(1,1,1)(sI-J)^{-1}w
=\frac{Z_m}{m}\,
\frac{(m^2-m-c)s+(2m^2-c)}{(s+m)(s+p)(s+q)}.
\tag{12}
\]
Let \(A=m^2-m-c<0\), \(B=2m^2-c>0\), and \(H(t)=\int_0^t h(s)\,ds\). Inverting (12) and integrating once in time yields
\[
\boxed{F(t)=\frac{Z_m}{m}\bigl(Ah(t)+BH(t)\bigr).}
\tag{13}
\]
As \(t\downarrow0\), \(h(t)\sim t^2/2\), \(H(t)\sim t^3/6\), so \(F(t)<0\) initially. As \(t\to\infty\), \(h(t)\to0\), \(H(t)\to1/(m+c)\), and \(F(t)\to(2-c/m^2)/\kappa>0\).

**4. The one-crossing convolution lemma.** Each function \(e^{-at}\mathbf1_{t\ge0}\), \(a>0\), is log-concave on the real line (with zero extension). Convolution preserves log-concavity, so \(h\) is log-concave on \((0,\infty)\). It is positive and real analytic there. If \((\log h)'\) were constant on any nonempty interval, analyticity would force \(h\) to be exponential throughout \((0,\infty)\), contradicting \(h(t)\sim t^2/2\). Thus \((\log h)'\) is strictly decreasing. For \(R(t)=H(t)/h(t)\), write
\[
R(t)=\int_0^t\frac{h(t-u)}{h(t)}\,du.
\tag{14}
\]
The integrand is strictly increasing with \(t\) for each fixed \(u\in(0,t)\), since its logarithmic derivative is \((\log h)'(t-u)-(\log h)'(t)>0\). Moreover, extending the integration interval adds a positive contribution. Hence \(R\) is strictly increasing; its limits are \(0\) at zero and \(+\infty\) at infinity. Formula (13) is \(F(t)=(Z_m/m)h(t)[A+BR(t)]\), so it has exactly one positive zero, is strictly negative before and strictly positive afterward. The zero is transverse because \(R'(t_*)>0\). Equation (5) follows.

**5. Persistence for the nonlinear shock.** Let \(F_\delta(t)=[N_\delta(t)-N_0]/\delta\). Smooth parameter dependence gives \(F_\delta\to F\) with one time derivative on every compact interval. Exponential attraction, uniform for small \(\delta\), yields \(\|X_\delta(t)-E_{m+\delta}\|\le C\delta e^{-\gamma t}\). Thus \(F_\delta(t)\) lies within \(Ce^{-\gamma t}\) of the positive equilibrium slope \([N_*(m+\delta)-N_0]/\delta\), uniformly for all small \(\delta\). This excludes late crossings. Near zero, (10) and locally uniform smooth third derivatives imply \(F_\delta(t)<0\) on one fixed short interval. On intermediate compact intervals away from \(t_*\), the strict sign of \(F\) persists; near \(t_*\), the transverse derivative persists. Consequently \(F_\delta\) has exactly one positive zero, and the zero converges to \(t_*\). This proves the theorem.

## Verification

The accompanying `verify.py` uses only the Python standard library. It checks exact-rational equilibrium/Jacobian and short-/long-time identities, the rational resolvent identity at several points, and high-accuracy deterministic numerical trajectories for representative small shocks. It also reconstructs the positive convolution for \(m=c=\kappa=1\) and brackets the unique limiting crossing. The analytic convexity argument and persistence step—not finite sampling—establish the infinitely many parameter/trajectory assertions.

For reproducibility, run `python3 verify.py`. All calculations are in the dimensionless time of (1).

## Relationship to prior work

Xia, Li and Chou (arXiv:2303.00864, first publicly posted 2023-03-01) introduce the age-structured cannibalism model. Their 2023 version 1, Appendix D.3, and revised 2024 version 2, Appendix F.3 (equations 95–97), specialize to the three-stage equations (1) before fixing the middle-stage fertility and maturation parameters both to one. The preprint explicitly supplies (2) and the derivative underlying the **lower** threshold in (3); neither that equilibrium result nor a local stability statement gives the dynamic sign-reversal window, the single-crossing property for actual nonlinear shocked trajectories, or the exact convolution crossing-time limit (5). Those are the claims assessed here. The later Physica D article (2024, DOI 10.1016/j.physd.2024.134339) is the journal version; its searchable excerpts and available abstract do not settle whether its inaccessible complete text contains related material.

Sorenson and Cortez (Theoretical Ecology, DOI 10.1007/s12080-020-00488-1) analyze an n-stage competition model and equilibrium hydra mechanisms, but their reproduction/maturation architecture differs and their primary conclusions concern equilibrium sensitivities. Cortez and Abrams (Ecology, DOI 10.1890/15-0648.1) similarly establish general equilibrium hydra restrictions. Neither work's accessible statements imply (4)–(5). A general totally-positive convolution or monotone-response theorem could conceptually subsume the log-concavity lemma; its applicability to the full nonlinear single-crossing statement has not been ruled out exhaustively.

## Limitations

The fecundity–mortality coupling is part of the source's constructed example and should not be interpreted as an intervention on mortality alone. The theorem is local in the shock magnitude and initial state (the old equilibrium). Its limiting crossing time is given implicitly, not in elementary form for general parameters. The result does not establish global attraction from arbitrary population states, single crossing for large shocks, or analogous behavior in the parent age-structured PDE. Possible equivalent formulations in unindexed work and the uninspected journal full text remain priority risks. Self-review is not an independent audit.

## References

1. M. Xia, X. Li and T. Chou, *Population overcompensation, transients, and oscillations in age-structured Lotka–Volterra models*, arXiv:2303.00864v1 (2023-03-01), https://arxiv.org/abs/2303.00864v1. Revised as *Overcompensation of transient and permanent death rate increases in age-structured models with cannibalistic interactions*, arXiv:2303.00864v2 (2024-03-15), https://arxiv.org/html/2303.00864v2, and Physica D 470 (2024), 134339, https://doi.org/10.1016/j.physd.2024.134339.
2. D. K. Sorenson and M. H. Cortez, *How intra-stage and inter-stage competition affect overcompensation in density and hydra effects in single-species, stage-structured models*, Theoretical Ecology 14 (2021), 23–39, https://doi.org/10.1007/s12080-020-00488-1.
3. M. H. Cortez and P. A. Abrams, *Hydra effects in stable communities and their implications for system dynamics*, Ecology 97 (2016), 1135–1145, https://doi.org/10.1890/15-0648.1.
