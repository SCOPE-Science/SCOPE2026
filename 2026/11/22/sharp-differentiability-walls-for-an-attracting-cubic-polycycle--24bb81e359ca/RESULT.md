# Sharp differentiability walls for an attracting cubic polycycle

## Finding
Consider the cubic vector field in the plane
\[
\begin{aligned}
\dot x&=x-\big[(x^2+y^2)+\varepsilon(x^2-y^2)\big]x-2\omega xy^2,\\
\dot y&=y-\big[(x^2+y^2)+\varepsilon(x^2-y^2)\big]y+2\omega x^2y,
\end{aligned}
\tag{1}
\]
with fixed real parameters \(0<\varepsilon<1\) and \(\omega>0\). For every such pair, there is a unique globally attracting invariant topological circle \(S_{\varepsilon,\omega}\) surrounding the repelling origin. It is a four-connection heteroclinic polycycle, with saddles at the two nonzero horizontal-axis equilibria and sinks at the two nonzero vertical-axis equilibria. **Its topological phase portrait is unchanged as \(\omega\) varies, yet its geometric differentiability changes at two sharp walls:**
\[
\boxed{S_{\varepsilon,\omega}\text{ is a }C^1\text{ embedded circle}\ \Longleftrightarrow\ \omega<1-\varepsilon,}
\]
\[
\boxed{S_{\varepsilon,\omega}\text{ is a }C^2\text{ embedded circle}\ \Longleftrightarrow\ \omega<\frac{1-\varepsilon}{2}.}
\]
Both boundary inequalities are strict. At the first wall the two incoming arcs meet at an honest corner; at the second wall the curve is \(C^1\) but has an explicitly nonzero logarithmic second-derivative singularity.

More precisely, write \(r_*=1/\sqrt{1-\varepsilon}\), \(\kappa=(1-\varepsilon)/\omega\), and let \(r(\theta)\) be the unique positive radial graph of the circle. At a sink, put \(u=\theta-\pi/2\). For \(\kappa<2\),
\[
 r_*-r(\pi/2+u)\sim C_{\varepsilon,\omega}|u|^\kappa,
\quad C_{\varepsilon,\omega}=\frac{\varepsilon\,2^{\alpha-\beta-1}}{r_*}
\int_{-1}^{1}\frac{(1-s)^\beta(1+s)^{-\alpha}}{(1+\varepsilon s)^2}\,ds>0,
\quad \alpha=\frac{1-\varepsilon}{2\omega},\quad\beta=\frac{1+\varepsilon}{2\omega}.
\]
At \(\kappa=2\),
\[
\boxed{r_*-r(\pi/2+u)\sim\frac{2\varepsilon}{(1-\varepsilon)^{3/2}}\,u^2\log\frac1{|u|}.}
\]
For \(\kappa>2\),
\[
\boxed{r_*-r(\pi/2+u)\sim
\frac{\varepsilon\alpha}{(\alpha-1)(1-\varepsilon)^{3/2}}\,u^2,}
\]
with convergence of the second angular derivative as \(u\to0\). All these asymptotics also hold at the opposite sink with the same coefficients.

## Assumptions and scope
Parameters obey \(0<\varepsilon<1\) and \(\omega>0\), throughout. Differentiability means that the entire closed planar invariant Jordan curve admits a regular \(C^j\) embedded-circle structure with its inherited planar inclusion; it does not mean that each open heteroclinic arc individually has this regularity (all such arcs are analytic). The graph \(r(\theta)\) uses the standard Euclidean polar radius, the original coordinates of (1), and no time reparametrization. The origin is excluded from \(S_{\varepsilon,\omega}\). The value \(\varepsilon=0\) is deliberately excluded: it gives an exactly circular, smooth invariant set for every \(\omega>0\), so the strict positive-anisotropy hypothesis is essential. Statements concern the complete real plane, not just the positive quadrant.

## Proof
**1. Contraction and the four equilibrium connections.** Write \(r^2=x^2+y^2\). The cubic nonlinear part \(Q\) of (1) satisfies
\[
\langle (x,y),Q(x,y)\rangle=-r^4-\varepsilon r^2(x^2-y^2)\le-(1-\varepsilon)r^4<0\quad(r>0).
\]
In polar coordinates this gives the exact original-time equations
\[
\dot r=r\big[1-r^2(1+\varepsilon\cos2\theta)\big],\qquad
\dot\theta=\omega r^2\sin2\theta.\tag{2}
\]
The unstable origin and strict contraction satisfy the invariant-circle theorem [1]. Alternatively, the radial equation traps every nonzero orbit eventually between two fixed positive radii, while the angular equation has only the four invariant axial rays. The nonzero equilibria are
\[
(\pm(1+\varepsilon)^{-1/2},0),\qquad(0,\pm(1-\varepsilon)^{-1/2}).
\]
At the horizontal pair, the radial and angular eigenvalues are \(-2\) and \(2\omega/(1+\varepsilon)\), giving saddles; at the vertical pair they are \(-2\) and \(-2\omega/(1-\varepsilon)\), giving sinks. Within each open quadrant, \(\theta\) is strictly monotone towards its vertical boundary. The unique unstable branch of each horizontal saddle in each adjacent quadrant ends at that quadrant's vertical sink; the four branches close into the invariant Jordan curve, independently of \(\omega>0\). The standard invariant-circle theorem ensures uniqueness and global attraction as a set [1].

**2. Exact radial graph.** Set \(z=\cos2\theta\) and \(V(z)=r(\theta)^2\) along any such heteroclinic branch. Since \(\dot z=-2\omega r^2(1-z^2)\), equation (2) gives, for \(-1<z<1\),
\[
V'(z)=\frac{(1+\varepsilon z)V(z)-1}{\omega(1-z^2)}.\tag{3}
\]
The endpoint value at the horizontal saddle is \(V(1)=(1+\varepsilon)^{-1}\). Let
\[
\alpha=\frac{1-\varepsilon}{2\omega}>0,\quad
\beta=\frac{1+\varepsilon}{2\omega}>0,\quad
M(z)=(1-z)^\beta(1+z)^{-\alpha}.
\]
The integrating factor obeys \(M'/M=-(1+\varepsilon z)/(\omega(1-z^2))\), so \((MV)'=-M/(\omega(1-z^2))\). Of all solutions, there is exactly one bounded at \(z=1\) (a homogeneous perturbation diverges as \((1-z)^{-\beta}\)). It is explicitly
\[
\boxed{
V(z)=\frac{(1+z)^\alpha}{\omega(1-z)^\beta}
\int_z^1(1-s)^{\beta-1}(1+s)^{-\alpha-1}\,ds.}
\tag{4}
\]
The integral is strictly positive; endpoint integration proves \(V(1)=(1+\varepsilon)^{-1}\) and \(V(-1)=(1-\varepsilon)^{-1}\). Equation (4) defines the same even-in-each-axis radial graph on all four open quadrants. It is analytic there and at \(z=1\), including at the two saddles (the bounded ODE solution has a convergent Taylor expansion in \(1-z\)). Thus the only possible loss of differentiability occurs at \(z=-1\), the two sinks.

**3. An exact positive defect coefficient.** Compare \(V\) with the instantaneous radial nullcline \(E(z)=(1+\varepsilon z)^{-1}\) and put \(h(z)=V(z)-E(z)\). Equation (3) gives
\[
h'(z)=\left[\frac\beta{1-z}+\frac\alpha{1+z}\right]h(z)+\frac{\varepsilon}{(1+\varepsilon z)^2},\qquad h(1)=0.
\]
Variation of constants, without an unknown matching constant, yields the exact identity
\[
\boxed{
h(z)=-\varepsilon\frac{(1+z)^\alpha}{(1-z)^\beta}
\int_z^1\frac{(1-s)^\beta(1+s)^{-\alpha}}{(1+\varepsilon s)^2}\,ds<0.}
\tag{5}
\]
In particular \(V'(z)<0\); the graph increases from the horizontal saddle radius to the vertical sink radius. Positivity of the integrand makes the leading singular coefficient nonzero, precluding accidental smoothing.

**4. Exact sink asymptotics and differentiability.** Near \(z=-1\), set \(t=1+z\) and \(q=1-\varepsilon\). The integrand in (5), after substituting \(v=1+s\), is
\[
\frac{\varepsilon(2-v)^\beta v^{-\alpha}}{(q+\varepsilon v)^2}
=\frac{\varepsilon2^\beta}{q^2}v^{-\alpha}(1+O(v)).\tag{6}
\]
If \(0<\alpha<1\), the full integral in (5) converges to a strictly positive finite integral \(J\), giving \(h(-1+t)\sim-\varepsilon2^{-\beta}Jt^\alpha\). The analytic nullcline difference \(E(-1+t)-E(-1)=O(t)\) is smaller because \(\alpha<1\). Since \(t=2\sin^2u=2u^2+O(u^4)\), and \(r=\sqrt V\), the stated \(C_{\varepsilon,\omega}|u|^{2\alpha}\) law follows.

At \(\alpha=1\), the same integral diverges as \(\varepsilon2^\beta q^{-2}\log(1/t)\). Thus
\[
 h(-1+t)\sim-\frac\varepsilon{q^2}t\log\frac1t,
\quad r_*-r(\pi/2+u)\sim\frac{2\varepsilon}{q^{3/2}}u^2\log\frac1{|u|}.
\]
If \(\alpha>1\), the integral diverges as \(\varepsilon2^\beta/[q^2(\alpha-1)]\,t^{1-\alpha}\), yielding
\[
h(-1+t)=-\frac{\varepsilon}{q^2(\alpha-1)}t+o(t),
\quad V(-1)-V(-1+t)=\frac{\varepsilon\alpha}{q^2(\alpha-1)}t+o(t).
\]
The claimed quadratic radial coefficient follows. The exact integral (5), differentiated in \(t>0\), gives the same leading differentiated expansions: for \(\alpha<1\), terms of order \(t^\alpha\) contribute \(O(t^{\alpha-j})\) at differentiation order \(j\), apart from smoother terms; at \(\alpha=1\), the corresponding terms are \(t\log(1/t)\); for \(\alpha>1\), the remainder after the linear term is \(O(t^{\min(\alpha,2)}(1+|\log t|))\), with the same derivative estimates. This includes the integer-index logarithmic resonances. The chain rule with \(t=2\sin^2u\) proves continuous first derivatives at \(u=0\) exactly when \(2\alpha>1\), and continuous second derivatives exactly when \(2\alpha>2\). For \(2\alpha=1\), the two one-sided first derivatives differ; for \(2\alpha=2\), the logarithmic second derivative diverges. For \(2\alpha<1\), the two meeting arcs form a nonregular inward cusp, not a \(C^1\) embedded curve. These are intrinsic properties of the planar curve: near either sink, \(x=-r_*u+o(u)\), so the singular radial powers transfer to the ordinary Cartesian graph \(y=y(x)\) with the same exponent. At either saddle, analyticity was already proved. This completes both sharp if-and-only-if criteria.

## Verification
The standalone `star_node_cusp_verify.py` uses symbolic identities to verify the exact radial/angular reduction, the integrating-factor decomposition, and the quadratic coefficient. High-precision quadrature checks one-sided asymptotic ratios at fixed \(\varepsilon=1/2\) for four parameter values spanning a cusp, corner, logarithmic wall and twice-differentiable regime. Run `python3 star_node_cusp_verify.py` with SymPy and mpmath installed; it prints `STAR_NODE_CUSP_VERIFY_OK` when its checks succeed. Finite quadrature and symbolic spot checks are diagnostic, **not** a substitute for the asymptotic proof in Sections 3–4. The exact integral (5) is the analytic certificate for the nonzero leading coefficient and the derivative limits.

## Relationship to prior work
Alarcón–Castro–Labouriau [1] establish the existence and topological classification of invariant circles and polycycles for contracting homogeneous planar star-node flows, including cubic examples. The present theorem uses their global attracting-circle result without claiming it anew. In contrast, it gives an explicit radial graph, positive singular amplitude, and **necessary and sufficient geometric \(C^1\)/\(C^2\) conditions** in a strictly contracting cubic subfamily that remains in one topological phase. Llibre–Zhang [2] give star-shapedness and a different quintic example with a square invariant circle; a square example does not determine either sharp threshold in (1). The previously published exact angular-return and physical-time Floquet theorem [3] explicitly assumes an angular factor that never vanishes, while here \(\dot\theta\) vanishes on the four axes and no nonconstant periodic orbit occurs. The published quartic depinning-cusp paper [4] analyzes near-critical rotation, original-time periods, and occupation distributions, not the differentiability of a pinned invariant polycycle. General competitive Lotka–Volterra carrying-simplex geometry [5] studies curvature and convexity after restricting to a positive quadrant, not the regularity of a four-quadrant closed curve at its reflected nodes. The use of local eigenvalue ratios is standard background; their **sharp, globally matched, noncancelling** singularity and derivative thresholds for this complete invariant set are the stated contribution.

## Limitations
The theorem fixes \(0<\varepsilon<1\); no statement on the circle's smoothness at \(\varepsilon=0\) follows by substitution into singular-coefficient formulas (the graph is exactly smooth there). Only \(C^1\) and \(C^2\) boundaries, their leading coefficients and the four-connection topology are classified; no claim is made about a complete hierarchy of higher differentiability, analytic regularity or nonhomogeneous perturbations. The statement is a self-reviewed mathematical result, without independent mathematical validation or a claim of exhaustive publication priority. Historical work on separatrix regularity and competitive carrying simplices could contain an equivalent reformulation despite the inspected comparisons.

## References
1. B. Alarcón, S. B. S. D. Castro, I. S. Labouriau, *Global planar dynamics with a star node and contracting nonlinearity*, arXiv:2307.16020v1 (first publicly posted 29 July 2023), https://arxiv.org/abs/2307.16020; *Research in the Mathematical Sciences* 11 (2024), article 21, https://doi.org/10.1007/s40687-024-00427-0.
2. J. Llibre, X. Zhang, *On the Invariant Sphere Theorem*, *Aequationes mathematicae* 100 (2026), article 55, https://doi.org/10.1007/s00010-026-01298-2.
3. *Exact angular return and physical-time Floquet rigidity for contracting homogeneous star-node cycles*, publicly available RESULT.md, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-angular-return-and-physical-time-floquet-rigidity-for-cont--7c00337eaa41.
4. *A quartic depinning cusp and a resolved physical-time occupation law for a contracting cubic star-node flow*, publicly available RESULT.md, https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-a-quartic-depinning-cusp-and-a-resolved-physical-time-occupation--ca713ddee5f9.
5. S. Baigent, *Convexity-preserving flows of totally competitive planar Lotka–Volterra equations and the geometry of the carrying simplex*, *Proceedings of the Edinburgh Mathematical Society* 55 (2012), 53–63, https://doi.org/10.1017/S0013091510000684. Abstract and publisher metadata inspected; comparison limited by incomplete full text.
