# A unique predator-abundance optimum under prey refuge and fear

## Finding

For the fear–refuge predator–prey system of Ramraj and Poornima (2026), the positive coexistence equilibrium's predator density has **exactly one** critical point as effective predation intensity varies, for **every** admissible positive choice of the other parameters. That point is a strict, nondegenerate global maximum. Thus decreasing exposed-prey predation by increasing proportional prey refuge can **strictly increase** equilibrium predator abundance when initial attack intensity is excessive, although equilibrium prey abundance always increases with refuge.

More precisely, put \(b=\beta(1-\delta)\), and let \(U>0\) solve \(a\alpha U^2+aU=r\). Define the predator invasion threshold \(b_0=m/(cU)\). For every \(b>b_0\) there is exactly one positive equilibrium \((u_b,v_b)\). The function \(b\mapsto u_b\) is strictly decreasing from \(U\) to zero, whereas \(b\mapsto v_b\) rises strictly from zero to a unique maximum at \(b=b_*\), and then decreases strictly to zero. Its peak is nondegenerate: \(v_b''|_{b=b_*}<0\). The maximizer is uniquely specified by the positive solutions of
\[
\frac{ru}{1+kv+\alpha u}-au^2-\frac{v(m+\eta v)}c=0,\qquad
\frac{r(1+kv)}{(1+kv+\alpha u)^2}=2au,
\]
followed by \(b_*=(m+\eta v)/(cu)\).

For any fixed nominal attack coefficient \(\beta>b_0\), the feasible coexistence refuge interval is \(0\le\delta<1-b_0/\beta\). If \(\beta>b_*\), the **unique** predator-density-maximizing refuge is \(\delta_*=1-b_*/\beta\in(0,1)\); if \(b_0<\beta\le b_*\), the predator-density maximum in that interval occurs at \(\delta=0\).

## Assumptions and scope

All parameters \(r,k,\alpha,a,\beta,m,\eta\) are strictly positive, \(0<c\le1\), and \(0\le\delta<1\). The autonomous continuous-time system is
\[
\dot u=u\left(\frac r{1+kv+\alpha u}-au-bv\right),\qquad
\dot v=v(cbu-m-\eta v),\qquad b=\beta(1-\delta).
\]
Here \(u>0\) is prey, \(v>0\) predator; \(\delta\) is the proportional prey refuge fraction. Each parameter is held fixed except \(b\) or, equivalently at fixed \(\beta\), \(\delta\). The claims concern **positive equilibrium densities**, not transient peaks, noisy ecological populations, optimal intervention policies, or changes to parameters other than the effective attack coefficient. No auxiliary sufficient boundedness condition involving \(b\) is needed for the equilibrium classification. For every fixed \(b>0\), positive trajectories are bounded by logistic comparisons \(\dot u\le u(r-au)\) and \(\dot v\le v(cbM-m-\eta v)\) after bounding prey by \(M\).

## Proof

**1. Existence, uniqueness and monotonicity of prey equilibrium.** Define the per-capita equilibrium functions
\[
F(u,v;b)=\frac r{1+kv+\alpha u}-au-bv,
\qquad G(u,v;b)=cbu-m-\eta v.
\]
For \(v=0\), \(F(U,0;b)=0\) has the sole positive solution \(U\) above. An interior equilibrium requires \(u>m/(cb)\). If \(b\le b_0\), this is incompatible with \(u<U\): \(F_u<0\), \(F_v<0\), so any positive equilibrium of \(F\) has \(u<U\). For \(b>b_0\), the predator nullcline \(v=(cbu-m)/\eta\) emerges from zero at \(u=m/(cb)<U\). On the interval \((m/(cb),U)\), the function \(F(u,(cbu-m)/\eta;b)\) is strictly decreasing, positive at the left endpoint and negative at the right. It has exactly one root \(u_b\), giving one \(v_b>0\).

The Jacobian of \((F,G)\) in \((u,v)\) is
\[
J=\begin{pmatrix}F_u&F_v\\cb&-\eta\end{pmatrix},\qquad
F_u=-\frac{r\alpha}{(1+kv+\alpha u)^2}-a<0,
\quad F_v=-\frac{rk}{(1+kv+\alpha u)^2}-b<0.
\]
Thus \(\det J=-\eta F_u-cbF_v>0\). Differentiating \(F=G=0\) with respect to \(b\) gives \(J(u_b',v_b')^\mathsf T=(v_b,-cu_b)^\mathsf T\), hence
\[
u_b'=\frac{-\eta v_b+cu_bF_v}{\det J}<0.
\]
As \(b\downarrow b_0\), uniqueness and the nullclines force \((u_b,v_b)\to(U,0)\). As \(b\to\infty\), the prey balance implies \(bv_b<r\), so \(v_b\to0\) and \(u_b=(m+\eta v_b)/(cb)\to0\). Consequently \(b\mapsto u_b\) is a strictly decreasing bijection from \((b_0,\infty)\) to \((0,U)\).

**2. The unique predator maximum.** Eliminate \(b\) from the two equilibrium equations using \(b=(m+\eta v)/(cu)\). Multiplying the prey equation by \(u\) produces the smooth curve \(f(u,v)=0\), where
\[
f(u,v)=\frac{ru}{1+kv+\alpha u}-au^2-\frac{v(m+\eta v)}c.
\]
For every \(u\in(0,U)\), \(f(u,0)>0\), \(f(u,v)\to-\infty\) as \(v\to\infty\), and
\[
f_v=-\frac{rku}{(1+kv+\alpha u)^2}-\frac{m+2\eta v}c<0.
\]
There is exactly one \(v=h(u)>0\) solving \(f(u,h(u))=0\), smoothly depending on \(u\). The endpoint limits are \(h(u)\to0\) as \(u\downarrow0\) and as \(u\uparrow U\). Therefore \(h\) attains a positive interior maximum. At every critical point \(h'(u)=0\), one has \(f_u=0\), and
\[
f_{uu}=-\frac{2r\alpha(1+kv)}{(1+kv+\alpha u)^3}-2a<0,\qquad
h''(u)=-\frac{f_{uu}}{f_v}<0.
\]
So **every** critical point is a strict local maximum. There cannot be two such critical points: between two strict maxima a smooth function must have an interior minimum, which would give a critical point with \(h''\ge0\), impossible. Thus there is precisely one critical point \(u_*\), the unique strict global maximum. Moreover \(h'>0\) before it and \(h'<0\) after it, since these signs hold near the endpoints and there are no other zeroes. Because \(u_b\) strictly decreases as \(b\) increases, the predator density \(v_b=h(u_b)\) increases strictly for \(b_0<b<b_*\) and decreases strictly for \(b>b_*\). At \(b_*\), the chain rule gives \(v_b''=h''(u_*)(u_b')^2<0\). The stationarity equations displayed under Finding follow from \(f=f_u=0\).

**3. Refuge classification.** At fixed \(\beta\), \(b=\beta(1-\delta)\) decreases strictly with \(\delta\). The stated unique maximizer, or the zero-refuge boundary maximizer when \(\beta\le b_*\), follows by restricting the strict unimodal curve to \(b\in(b_0,\beta]\).

**4. Exact witness.** Choose
\[
(r,k,\alpha,a,c,m,\eta)=(25,1,3,1,1,1,3).
\]
At \((u_*,v_*,b_*)=(1,1,4)\), both equilibrium equations hold exactly: \(25/5-1-4=0\) and \(4-1-3=0\); also \(f_u=25(1+1)/5^2-2=0\). The theorem makes this the **unique global maximum** \(v_*=1\). Here \(U=(\sqrt{301}-1)/6\), \(b_0=(\sqrt{301}+1)/50\), and for nominal \(\beta=8\) the unique optimal refuge is \(\delta_*=1/2\). At this equilibrium, \(f_{uu}=-22/5\), \(f_v=-8\), \(h''=-11/20\), \(u_b'=-1/4\), so \(v_b''=-11/320<0\). These rational identities can be checked without numerical integration.

## Verification

The standalone `checker.py` uses SymPy to verify the exact example, all derivatives at the optimum, the positive Jacobian determinant and the strict-curvature identity. A supplementary numerical sweep checks root existence and the predicted direction of the hump; it is **not** used as an infinite proof. Reproduce with `python checker.py` (requires Python, SymPy and SciPy). The general result is proved in the preceding analytical steps, independent of software.

## Relationship to prior work

Ramraj and Poornima (2026) define precisely this model and characterize equilibria and local stability. Their Figure 3 reports monotone predator-density changes over *selected* attack-rate/refuge ranges; their displayed calculations do not give a universal global optimum or the exactly-one-critical-point theorem. Independent indexed results on the same equations establish global stability and critical invasion decay, not this parameter-optimization statement. These claims are distinct: knowing which equilibrium attracts trajectories at a fixed parameter does not establish how that equilibrium ranks across parameters.

The overexploitation mechanism and **intermediate-attack predator-abundance peaks are long-established ecological knowledge**, notably Holt and Hochberg (2001, Figure 2.2) for a logistic-prey, linear-response model and Barbier, Wojcik and Loreau (2021) for other predation density dependencies. **Neither the hump's existence nor the qualitative ecological paradox is claimed as new.** The finding here is the sharp, model-specific universal uniqueness, nondegeneracy and refuge-optimum classification under simultaneous rational fear, prey crowding, quadratic prey mortality and predator interference. Those broader works do not state this conclusion for this model. Historical-priority uncertainty remains possible; no independent literature audit is claimed.

## Limitations

The theorem addresses positive stationary solutions for this particular autonomous two-species model, not stochastic persistence, transient response, harvesting, or global population management. The optimal refuge has no claimed welfare significance and only maximizes predator density *within the model*. The original 2026 source's extra sufficient boundedness hypothesis is not required for the arguments, because elementary logistic comparisons bound trajectories for each fixed attack coefficient. The claim is not a general theorem for arbitrary functional responses or arbitrary refuge rules. The older literature already contains qualitative and example-level attack-rate hump mechanisms, and a fuller historical survey could uncover stronger prior theorems.

## References

1. G. Ramraj and T. Poornima (2026). “Fear-driven predator–prey dynamics with prey refuge: analytical framework and physics-informed neural network approach.” *Frontiers in Artificial Intelligence* 9, 1868693, published 10 August 2026. https://doi.org/10.3389/frai.2026.1868693
2. R. D. Holt and M. E. Hochberg (2001). “Indirect Interactions, Community Modules and Biological Control: a Theoretical Perspective.” In *Evaluating Indirect Ecological Effects of Biological Control*, especially Figure 2.2. https://people.clas.ufl.edu/rdholt/files/106.pdf
3. M. Barbier, L. Wojcik and M. Loreau (2021). “A macro-ecological approach to predation density-dependence.” *Oikos* 130, 553–570. https://doi.org/10.1111/oik.08043
4. “A systematic study of autonomous and nonautonomous predator–prey models for the combined effects of fear, refuge, cooperation and harvesting” (2022). https://pmc.ncbi.nlm.nih.gov/articles/PMC9217126/
