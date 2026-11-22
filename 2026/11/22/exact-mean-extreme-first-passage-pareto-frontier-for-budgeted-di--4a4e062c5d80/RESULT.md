# Exact mean–extreme first-passage Pareto frontier for budgeted diffusion

## Finding

Consider a one-dimensional, zero-drift Itô diffusion on \([0,1]\), reflected at \(0\), absorbed at \(1\), and started at \(0\). For a spatial diffusivity \(D\) satisfying \(D(x)>0\) almost everywhere and \(\int_0^1 D(x)\,dx=1\), define the two design functionals
\[
M[D]=\int_0^1\frac{1-x}{D(x)}\,dx,\qquad
F[D]=\int_0^1\frac{dx}{\sqrt{D(x)}}.
\]
The domain consists of measurable profiles for which both integrals are finite. For a sufficiently regular strictly positive profile, \(M[D]\) is exactly the mean absorption time, and the expected earliest absorption among \(N\) independent copies satisfies
\[
\mathbb E[T_{(1),N}]\sim\frac{F[D]^2}{4\log N}\qquad(N\to\infty).
\]
Thus the Pareto-efficient designs for single-searcher mean time and the leading collective-first-arrival constant are precisely the Pareto-efficient designs for \((M,F)\).

**Complete frontier.** For every real \(r>1\), put
\[
h_r=r^4-r,\qquad d_r=\frac{3r}{2r^3+1},
\]
and let \(u_r(x)\in[1,r]\) be the unique root of
\[
u_r(x)^4-u_r(x)=h_r(1-x),\qquad 0\le x\le1.
\]
Then the **unique** nondominated profiles, up to equality almost everywhere, are exactly
\[
D_r(x)=d_r u_r(x)^2,\quad 1<r<\infty,
\]
together with the two limiting designs \(D_1(x)=1\) and \(D_\infty(x)=\tfrac32\sqrt{1-x}\). Their objective values are
\[
F_r=\frac{\frac43(r^3-1)-\log r}{h_r\sqrt{d_r}},\qquad
M_r=\frac{\frac13(2r^6-5r^3+3)+\log r}{d_r h_r^2}.
\]
As \(r\) increases from \(1\) to \(\infty\), \(M_r\) strictly decreases and \(F_r\) strictly increases, with endpoint pairs
\[
(M_1,F_1)=\left(\frac12,1\right),\qquad
(M_\infty,F_\infty)=\left(\frac49,\sqrt{\frac{32}{27}}\right).
\]
In particular, the unique mean-optimal diffusivity shortens the single-searcher mean by exactly \(1/9\), but **lengthens** the leading many-searcher first-arrival time by a factor of exactly \(32/27\) relative to homogeneous diffusion. Every intermediate nondominated tradeoff profile is explicit above.

## Assumptions and scope

The functional classification holds for all measurable \(D:(0,1)\to(0,\infty)\), interpreted up to null sets, with unit spatial mean and finite \(M[D]\) and \(F[D]\). The endpoint value \(D_\infty(1)=0\) refers to its continuous representative: it is positive almost everywhere, and its reflected-to-absorbed diffusion is well defined and has finite mean. For \(1\le r<\infty\), \(D_r\) is smooth and uniformly positive on \([0,1]\); the physical many-searcher asymptotics apply in the standard uniformly elliptic setting. The singular \(r=\infty\) endpoint is established separately in the proof.

For a spatially averaged diffusivity \(D_0>0\) on an interval of length \(L>0\), rescale \(x\mapsto x/L\) and multiply each displayed \(D_r\) by \(D_0\). The mean cost becomes \(L^2M_r/D_0\), while the earliest-arrival leading term becomes \(L^2F_r^2/(4D_0\log N)\).

## Proof

**1. Functionals from the stochastic problem.** For any uniformly positive smooth \(D\), the backward mean-time equation is \(D(x)m''(x)=-1\), with \(m'(0)=0\) and \(m(1)=0\). Integrating twice gives \(m(0)=M[D]\). The one-dimensional diffusion metric has intrinsic length \(F[D]\). The short-time first-passage logarithmic exponent is \(-F[D]^2/(4t)\), and the extreme-first-passage moment theorem then yields \(\mathbb E[T_{(1),N}]\sim F[D]^2/(4\log N)\); this uses a fixed spatial profile as \(N\to\infty\), not a profile depending on \(N\).

**2. Unique weighted minimizers.** Both maps \(z\mapsto z^{-1}\) and \(z\mapsto z^{-1/2}\) are strictly convex on positive numbers. For each \(\lambda>0\), the strictly convex objective \(M[D]+\lambda F[D]\), restricted by \(\int D=1\), has at most one minimizer. A candidate satisfying
\[
\frac{1-x}{D(x)^2}+\frac{\lambda}{2D(x)^{3/2}}=\mu
\]
for some constant \(\mu\) is automatically its unique global minimizer: the pointwise supporting-line inequalities integrate, and their linear terms cancel because both competitors have unit mean.

Writing \(d=D(1)>0\) and \(u(x)=\sqrt{D(x)/d}\), the equation at \(x=1\) gives \(\mu=\lambda/(2d^{3/2})\). Subtracting at a general \(x\) gives
\[
1-x=\frac{\lambda\sqrt d}{2}\bigl(u(x)^4-u(x)\bigr).
\]
Set \(r=u(0)>1\) and \(h_r=r^4-r\). The relation at \(x=0\) yields \(\lambda=2/(\sqrt d\,h_r)\), and the normalization becomes
\[
1=\frac d{h_r}\int_1^r u^2(4u^3-1)\,du
=\frac d{h_r}\frac{2r^6-r^3-1}{3},
\]
so \(d=d_r=3r/(2r^3+1)\). Conversely, every such profile satisfies the exact multiplier equation and is therefore the unique minimizer of \(M+\lambda F\) for its \(\lambda\). The quantity \(d_rh_r^2=3r^3(r^3-1)^2/(2r^3+1)\) increases strictly from zero to infinity, so the associated \(\lambda_r=2/(\sqrt{d_r}h_r)\) decreases bijectively from infinity to zero.

**3. Exact curve and strict ordering.** The change of variables \(x=1-(u^4-u)/h_r\) gives
\[
F[D_r]=\frac1{h_r\sqrt{d_r}}\int_1^r\frac{4u^3-1}{u}\,du,
\]
and
\[
M[D_r]=\frac1{d_rh_r^2}\int_1^r\frac{(u^4-u)(4u^3-1)}{u^2}\,du.
\]
Elementary antiderivatives produce the formulas stated above, including their logarithms. The two endpoint limits follow by expansion at \(r=1\) and by scaling \(u_r(x)/r\to(1-x)^{1/4}\) as \(r\to\infty\). At \(r=1\) the strict Jensen inequality \(F[D]\ge1\) makes the homogeneous profile uniquely efficient; at \(r=\infty\), Cauchy–Schwarz gives
\[
M[D]\ge\frac{\bigl(\int_0^1\sqrt{1-x}\,dx\bigr)^2}{\int_0^1D(x)\,dx}=\frac49,
\]
with equality only for \(D(x)=\tfrac32\sqrt{1-x}\) almost everywhere. For two different positive multipliers, adding the two strict minimizing inequalities shows that the optimizer of the larger multiplier has strictly smaller \(F\) and strictly larger \(M\). This establishes the strict ordering.

**4. Exhaustion of all nondominated profiles.** No admissible \(D\) can have \(M[D]<4/9\). If \(M[D]\ge1/2\), the homogeneous profile has both no larger \(M\) and strictly smaller \(F\), except when \(D\) itself is homogeneous. Otherwise \(M[D]\in(4/9,1/2)\); by continuity and strict ordering, there exists exactly one \(r\in(1,\infty)\) with \(M[D_r]=M[D]\). The strict global minimization of \(M+\lambda_r F\) then forces \(F[D]\ge F[D_r]\), with equality only if \(D=D_r\) almost everywhere. Hence every off-frontier design is dominated, and every listed design is nondominated. The same conclusion holds for \(F^2\) since \(F>0\).

**5. Singular mean-optimal endpoint and collective-arrival constant.** For \(D_\infty(x)=c\sqrt{1-x}\), \(c=3/2\), let \(Y=1-X\) and \(U=Y^{3/2}\). On \((0,1)\), its generator becomes
\[
\mathcal G\varphi(u)=\frac{27}{8}u\varphi''(u)+\frac98\varphi'(u),
\]
with absorption at \(u=0\), reflection at \(u=1\), and start at \(u=1\). This is a time-scaled squared-Bessel diffusion of dimension \(2/3\), with accessible absorbing endpoint. Solving \(\mathcal G\varphi=s\varphi\), \(\varphi(0)=1\), \(\varphi'(1)=0\), gives the exact absorption-time Laplace transform
\[
\mathbb E[e^{-sT}]=\left[\Gamma(2/3)(8s/27)^{1/6}I_{-1/3}\!\left(2\sqrt{8s/27}\right)\right]^{-1},\quad s>0.
\]
The large-argument asymptotic of \(I_{-1/3}\) gives \(-\log\mathbb E[e^{-sT}]=\sqrt{32s/27}+O(\log s)\). The corresponding short-time exponential estimate is
\[
\lim_{t\downarrow0}t\log\mathbb P(T\le t)=-\frac{8}{27}.
\]
For completeness, it follows directly by Chernoff's upper bound and exponential tilting: under the tilted law proportional to \(e^{-sT}\), the mean is \(\sqrt{32/27}/(2\sqrt s)(1+o(1))\), with relative variance tending to zero; concentrating the tilt just below \(t\) yields the matching lower logarithmic bound. Since \(\mathbb ET=4/9<\infty\), the extreme-first-passage moment theorem applies and yields \(\mathbb ET_{(1),N}\sim (8/27)/\log N\), compared with \((1/4)/\log N\) for homogeneous diffusion. Their ratio is \(32/27\).

## Verification

A standalone standard-library Python checker, `CHECKER.py`, tests the exact normalized shape, \(M\) and \(F\) integral formulas, the multiplier stationarity equation, strict Pareto ordering, scalarized competitor inequalities, and rational endpoint identities at several independent parameter values. It passed 177 deterministic checks. The singular-endpoint Laplace formula was also independently compared against numerical integration of its backward ODE for several positive discounts. These finite computations check algebra and normalization; the analytical arguments above prove the continuous assertions.

## Relationship to prior work

Menon (2026) established the fixed-average diffusivity mean-first-passage optimizer, including the \(D_\infty\) profile and its \(8/9\) mean ratio, but did not optimize the joint mean/collective-arrival tradeoff. Lawley (2019/2020) established the universal extreme-first-passage law at a fixed diffusion profile and its geodesic dependence, but not the budget-constrained jointly efficient profiles. Dos Santos, Menon Jr., and Anteneodo (2022) studied full first-passage distributions and inverse-time search efficiency for space-dependent diffusion, not this two-objective complete frontier. The new claim is the *complete unique profile classification with exact parametric Pareto costs*, not those established single-objective or fixed-profile results.

## Limitations

The Pareto theorem concerns the first passage **mean** and the **leading large-population extreme-time coefficient**; it does not optimize finite-population mean completion times, finite-time quantiles, higher dimensions, or arbitrarily prescribed stochastic-calculus conventions. For merely measurable designs, \(M\) and \(F\) are well-defined mathematical functionals; the diffusion-process interpretation is asserted only for regular positive profiles and for the explicitly analyzed singular endpoint. No claim of uniformity in \(N\) while the profile parameter varies is made. Independent external validation and publication-priority assessment have not been performed.

## References

1. L. Menon, *Optimal heterogeneous diffusivity profiles for mean first-passage minimization*, arXiv:2611.17470v1 (first public 2026-11-12), https://arxiv.org/html/2611.17470v1.
2. S. D. Lawley, *Universal Formula for Extreme First Passage Statistics of Diffusion*, arXiv:1909.09883 (first public 2019-09-21); Phys. Rev. E **101**, 012413 (2020), https://arxiv.org/abs/1909.09883.
3. M. A. F. dos Santos, L. Menon Jr., and C. Anteneodo, *Efficiency of random search with space-dependent diffusivity*, arXiv:2206.14229 (first public 2022-06-28), https://arxiv.org/abs/2206.14229.
