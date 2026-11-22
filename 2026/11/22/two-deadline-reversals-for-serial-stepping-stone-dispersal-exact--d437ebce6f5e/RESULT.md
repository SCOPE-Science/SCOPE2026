# Two-deadline reversals for serial stepping-stone dispersal: exact speed thresholds and stage asymptotics

## Finding

For all integers \(k\ge2\), every direct completion rate \(\gamma>0\), serial stage rate \(\lambda>0\), and independent eventual-success factors \(0<a<b\le1\), define
\[
P_D(T)=b(1-e^{-\gamma T}),\qquad
P_S(T)=a\left(1-e^{-\lambda T}\sum_{j=0}^{k-1}\frac{(\lambda T)^j}{j!}\right),\quad T>0.
\]
Put \(r=\lambda/\gamma\), \(q=b/a>1\), and
\[
G_k(u)=1-e^{-u}\sum_{j=0}^{k-1}\frac{u^j}{j!},\qquad
R_{k,r}(x)=\frac{G_k(rx)}{1-e^{-x}},\qquad
M_k(r)=\sup_{x>0}R_{k,r}(x).
\]
For each \(q>1\), exactly one \(r_c(k,q)>1\) solves \(M_k(r_c)=q\). If \(r<r_c\), then \(P_S(T)<P_D(T)\) for all \(T>0\). If \(r=r_c\), equality occurs at exactly one finite positive \(T\); otherwise the direct route is better. If \(r>r_c\), there are exactly two distinct finite positive crossing times \(T_-<T_+\), which are transversal, and \(P_S>P_D\) holds **only** for \(T_-<T<T_+\). No three or more preference reversals are possible. At criticality the equality is a strict tangency.

The large viability-ratio and stage-count laws are
\[
\lim_{q\to\infty}\frac{r_c(k,q)}q=\frac1{c_k},\qquad
c_k=\max_{u>0}\frac{G_k(u)}u,\qquad
\lim_{k\to\infty}k c_k=1.
\]
Here \(c_k\) has a unique maximizing argument \(u_k>k-1\), determined by \(u_k G_k'(u_k)=G_k(u_k)\). For fixed \(k,q\), as \(r\downarrow r_c\) from above, the dimensionless crossing separation obeys
\[
x_+(r)-x_-(r)=2\sqrt{\frac{2\,\partial_r R_{k,r_c}(x_c)}{-\partial_{xx}R_{k,r_c}(x_c)}}\sqrt{r-r_c}+O(r-r_c),
\]
where \(x_\pm=\gamma T_\pm\), and \(x_c\) uniquely maximizes \(R_{k,r_c}\). Every quantity under the square root is strictly positive.

## Assumptions and scope

The direct route has one exponential transit clock of rate \(\gamma\). The stepping-stone route has \(k\) **sequential and independent** exponential transit clocks, each rate \(\lambda\), and succeeds only after all stages. The respective independent terminal viability factors are \(a,b\); they are not inferred from empirical measurements. The target's opportunity expires at a fixed deadline \(T\). Arrival at exactly the deadline has probability zero. There is a single traveler, no reproduction on intermediate sites, and no feedback or competing arrivals. Success is the joint event of completion before the deadline and independent terminal viability. We compare direct and serial routes, not a population-optimal policy with switching or mixing.

## Proof

Scale the deadline by \(x=\gamma T\). The route comparison \(P_S/P_D=R_{k,r}(x)/q\) is exact because the Erlang stage-sum has CDF \(G_k\).

**1. Shape of the CDF quotient.** For \(r\le1\), the serial transit time is stochastically no smaller than its first stage, which is itself stochastically no smaller than an exponential time of rate \(\gamma\). Thus \(R_{k,r}(x)<1\) for all \(x>0\), and the direct route wins whenever \(q>1\).

For \(r>1\), set \(B(x)=1-e^{-x}\), \(A(x)=G_k(rx)\) and
\[
h(x)=\frac{A'(x)}{B'(x)}=\frac{r^k x^{k-1}e^{-(r-1)x}}{(k-1)!},\qquad
U(x)=B(x)h(x)-A(x).
\]
Then \(U'(x)=B(x)h'(x)\). The density ratio \(h\) strictly increases up to \((k-1)/(r-1)\) and strictly decreases thereafter. Since \(U(0+)=0\), \(U\) is positive up to that point; since \(U(\infty)=-1\), it crosses zero **once and strictly** on the decreasing branch. Finally
\[
R'_{k,r}(x)=\frac{e^{-x}}{B(x)^2}U(x),
\]
so \(R_{k,r}\) strictly increases then strictly decreases, with exactly one interior maximizer \(x_*(k,r)\). Its endpoints are \(R(0+)=0\) and \(R(\infty)=1\). Moreover, for all sufficiently large \(x\),
\[
A(x)-B(x)=e^{-x}-e^{-rx}\sum_{j=0}^{k-1}\frac{(rx)^j}{j!}>0
\]
because \(r>1\). Hence \(M_k(r)>1\), and the unique maximum is nondegenerate: at \(x_*\), \(U=0\), \(U'<0\), so \(R''(x_*)<0\). In particular the horizontal level \(q>1\) meets the quotient at zero, one tangent, or two transversal points according as \(q>M\), \(q=M\), or \(q<M\).

**2. Unique threshold in rate ratio.** At each fixed \(x>0\), \(G_k(rx)\) is strictly increasing in \(r\), and the unique finite maximizer shows \(M_k(r)\) is strictly increasing on \((1,\infty)\). As \(r\downarrow1\), uniform convergence on every compact \(x\)-interval and the tail bound \(R_{k,r}(x)\le(1-e^{-x})^{-1}\) imply \(M_k(r)\downarrow1\). As \(r\to\infty\), taking \(x=r^{-1/2}\) yields \(R_{k,r}(x)\sim\sqrt r\), so \(M_k(r)\to\infty\). Continuity of the unique maximum follows from its strict finite location and smooth defining equation (or compactness on bounded rate intervals). Thus the unique critical \(r_c(k,q)\) exists for every \(q>1\). The first classification follows.

**3. Critical square-root splitting.** Let \(x_c=x_*(k,r_c)\). The derivative \(\partial_rR(x_c,r_c)>0\) and curvature \(\partial_{xx}R(x_c,r_c)<0\), established above. Taylor expansion
\[
R(x,r)-q=\partial_r R(x_c,r_c)(r-r_c)+\tfrac12\partial_{xx}R(x_c,r_c)(x-x_c)^2+O((r-r_c)|x-x_c|+|x-x_c|^3+(r-r_c)^2)
\]
and the implicit-function theorem on each side of the nondegenerate peak give the displayed square-root coalescence formula. No other roots can exist by Step 1.

**4. Sharp speed and stage asymptotics.** Substitute \(u=rx\):
\[
\frac{M_k(r)}r=\sup_{u>0}\frac{G_k(u)}{r(1-e^{-u/r})}.
\]
For fixed positive \(u\), the displayed quotient tends to \(G_k(u)/u\). Moreover, \(1/[r(1-e^{-u/r})]\le1/u+1/r\). On \(u\ge H\), the normalized quotient is therefore at most \(1/H+1/r\). On \(0<u\le\varepsilon\), the bound \(G_k(u)\le u^k/k!\) and the same denominator inequality make it uniformly negligible as \(\varepsilon\downarrow0\) for \(r\ge1\). Hence compact convergence and the two tail controls yield \(M_k(r)/r\to c_k\), which, on setting \(M_k(r_c)=q\), proves \(r_c(k,q)/q\to1/c_k\) as \(q\to\infty\).

Write \(f_k(u)=G_k'(u)=e^{-u}u^{k-1}/(k-1)!\). The derivative of \(G_k(u)/u\) has numerator \(V(u)=u f_k(u)-G_k(u)\), with \(V'(u)=u f_k'(u)\). This is strictly positive on \((0,k-1)\), strictly negative afterwards, \(V(0+)=0\), and \(V(\infty)=-1\), proving a unique \(u_k>k-1\) and \(c_k=G_k(u_k)/u_k\le1/(k-1)\). On the other hand, for every fixed \(\varepsilon>0\), \(G_k(k(1+\varepsilon))\to1\) by the law of large numbers for a sum of \(k\) unit exponentials, so
\[
\liminf_{k\to\infty}kc_k\ge\frac1{1+\varepsilon}.
\]
Letting \(\varepsilon\downarrow0\) yields \(kc_k\to1\).

**5. Slower-mean yet finite-deadline advantage.** The direct route's mean transit time is \(1/\gamma\); the serial route's mean is \(k/\lambda\). For every \(1<r<k\), the latter mean is larger. But Step 1 gives \(M_k(r)>1\); choose any viability ratio \(1<q<M_k(r)\), e.g. take \(b=1\), \(a=1/q\). The direct route also has the higher eventual success \(b>a\), while the serial route wins on a nonempty bounded deadline interval. This proves the strict counterintuitive joint comparison.

## Verification

A reproducible standalone checker is supplied as `check.py` using only the Python standard library. It checks Erlang CDF summation against integration benchmarks, root structure at explicit numerical parameters, finite-difference derivatives and the predicted large-speed scaling over finite grids. It is supplementary to the proof above. The exact symbolic counterexample uses \(k=2\), \(\gamma=1\), \(\lambda=3/2\), \(a=999/1000\), \(b=1\): the serial route has mean transit \(4/3>1\), eventual success \(999/1000<1\), but at \(T=5\) its success advantage is
\[
\frac{999}{1000}\left[1-\left(1+\frac{15}{2}\right)e^{-15/2}\right]-(1-e^{-5})>\frac{1139}{1200000}>0.
\]
For a fully rational certificate, the exponential Taylor sum through order nine with a geometric upper bound for its remaining tail gives \(e^5<150\), and the Taylor sum through order sixteen gives \(e^{15/2}>1800\). Thus the displayed difference exceeds \(1/150-1/1000-(999/1000)(17/2)/1800=1139/1200000\). Both strict rational Taylor comparisons are replayed in `check.py`. At very small and arbitrarily large deadlines the difference is strictly negative by Step 1 and terminal factors, so there must be two crossings.

## Relationship to prior work

Szojka and Germain (2024) provide ecological motivation for transient persistence and dormant dispersal through unsuitable habitat. Saura, Bodin and Fortin (2013) establish the ecological value of multi-step connectivity and discuss time lag, but their generalized network comparison is not the present fixed-deadline Erlang-versus-exponential model. Pinelis's work on l'Hospital-type monotonicity rules gives a classical general tool for deriving a quotient's one-peak structure; the calculus principle itself is **not claimed to be novel**. The claimed additional model-specific content is the complete exact viability/rate frontier for any number of steps, the two finite-deadline preference reversals despite both inferior mean time and eventual survival, the threshold saddle-node law, and sharp large-viability-ratio and large-stage-count scalings. The completeness of historical literature coverage is not independently certified.

## Limitations

Stage completion is memoryless within each step; stage times are independent and identically distributed; each route has a constant independent eventual viability factor, not death continuously coupled to travel. The direct route has one exponential transit stage. The model ignores temporal stochasticity of the target's own availability, demographic multiplication at intermediate patches, spatial feedback, and individual heterogeneity. The finding does not claim a calibrated ecological design threshold or claim all serial routes are viable. For arbitrary non-exponential transit laws the one-peak guarantee may fail. Finite checks cannot establish the universal theorem, which rests on the analytic proof.

## References

1. Szojka, M. C., and Germain, R. M. (2024). *Dispersing across habitat boundaries: Uncovering the demographic fates of populations in unsuitable habitat*. Ecosphere 15, e4814. First publicly available March 24, 2024. https://doi.org/10.1002/ecs2.4814
2. Saura, S., Bodin, Ö., and Fortin, M.-J. (2014 volume; online 2013). *Stepping stones are crucial for species' long-distance dispersal and range expansion through habitat networks*. Journal of Applied Ecology 51, 171–182. First publicly available October 1, 2013. https://doi.org/10.1111/1365-2664.12179
3. Pinelis, I. *L'Hospital-Type Rules for Monotonicity: Include Them into Calculus Texts!* https://pages.mtu.edu/~ipinelis/lhosp/textbook.pdf (general monotonicity method; exact source-publication date not asserted).
