# Three sharp period-edge regimes in a continuous two-zone quadratic center

## Finding
Consider the following two-zone specialization of a quadratic system with the invariant straight line \(y=1\):
\[
\dot x=-y+c(y)y^2,\qquad \dot y=x(1-y),
\qquad
c(y)=\begin{cases}k,&y\geq0,\\h,&y<0.\end{cases}
\]
For every fixed \(h\geq0\) and \(k\geq0\), restrict the flow to the invariant half-plane \(\Omega=\{(x,y):y<1\}\). The field is continuous and continuously differentiable across \(y=0\). The origin is a center. Its maximal period annulus and its **original-time** periods exhibit the following exhaustive parameter transition:

1. **\(0\leq k<1\) (global center):** every point of \(\Omega\setminus\{(0,0)\}\) lies on a periodic orbit. Writing \(E>0\) for the conserved energy, its least period obeys
   \[
   T(E)\sim\frac{2\sqrt{2}}{1-k}\sqrt E\quad(E\to\infty).
   \]
2. **\(k=1\) (infinite-position energy barrier):** the maximal period annulus is exactly the connected region \(0<E<1/2\) around the origin. Its periods obey
   \[
   T(E)\sim\frac{\pi\sqrt2}{\sqrt{1/2-E}}
   \quad(E\uparrow1/2).
   \]
   At the critical energy \(E=1/2\), each forward branch escaping toward \(y=1\) satisfies
   \[
   \lim_{t\to\infty}t^2(1-y(t))=2,\qquad
   \lim_{t\to\infty}t x(t)=2.
   \]
3. **\(k>1\) (finite saddle separatrix):** the origin's maximal period annulus is the connected bounded component of \(0<E<E_*(k)\), where
   \[
   E_*(k)=1-\frac{1}{2k}+(k-1)\log\!\left(1-\frac1k\right)>0.
   \]
   Its outer boundary is a homoclinic loop to the saddle \((x,y)=(0,1/k)\); the least period satisfies
   \[
   T(E)=\sqrt{\frac{k}{k-1}}\log\!\frac1{E_*(k)-E}+O(1)
   \quad(E\uparrow E_*(k)).
   \]

All three leading period coefficients, the critical energy, and the critical escape coefficients are independent of the lower-zone coefficient \(h\). The small-orbit period tends to \(2\pi\) in every case.

## Assumptions and scope
The two coefficients are fixed real numbers \(h,k\geq0\); initial data have \(y<1\); time has the normalization displayed above. There is no restriction on the sign or magnitude of \(x\), and the differential equation is globally defined in \(\Omega\). The function \(c(y)\) at the switching line may be set to either coefficient since its contribution is multiplied by \(y^2\). The asymptotic variable \(E\) is exactly the mechanical energy defined below, not an orbit amplitude. The period annulus always refers to its connected component containing the origin; at \(k>1\), the open energy sublevel has a separate exterior component and that component is not part of the annulus. No statement concerns the half-plane \(y\geq1\).

## Proof
**(1) Exact mechanical equivalence and conservation.** Set \(q=-\log(1-y)\) on \(\Omega\). Then \(\dot q=x\), and
\[
\ddot q=-(1-e^{-q})+c(q)(1-e^{-q})^2=-V'(q),
\qquad c(q)=\begin{cases}k,&q\geq0,\\h,&q<0.\end{cases}
\]
The potential, normalized by \(V(0)=0\), is \(V(q)=U_k(q)\) for \(q\geq0\) and \(V(q)=U_h(q)\) for \(q<0\), where
\[
U_c(q)=(1-c)q+(1-2c)(e^{-q}-1)+\frac c2(e^{-2q}-1).
\]
Direct differentiation gives \(U_c'(q)=(1-e^{-q})[1-c(1-e^{-q})]\), \(U_c''(0)=1\), and conservation of \(H=\tfrac12 x^2+V(q)\). Both \(U_c(0)\) and \(U_c'(0)\) vanish, hence \(V\) is \(C^2\) at the switch. If \(q<0\), then \(1-e^{-q}<0\) and \(U_h'(q)<0\) for all \(h\geq0\). Thus \(V(q)\to+\infty\) as \(q\to-\infty\), giving one left turning point for any \(E>0\). Near the origin \(V(q)=q^2/2+O(|q|^3)\), establishing a linear center and the small-orbit period limit.

**(2) Exact right-side potential topology.** On \(q>0\), put \(z=1-e^{-q}\in(0,1)\). Then \(V'(q)=z(1-kz)\).
For \(k<1\), the potential is strictly increasing and \(U_k(q)=(1-k)q+O(1)\to\infty\). Every positive energy level has exactly two turning points, hence is a simple periodic oval; no other positive-energy components occur.
For \(k=1\), \(U_1(q)=\frac12(1-e^{-q})^2\) increases to \(1/2\) without attaining its supremum at finite \(q\). Therefore the periodic annulus has exactly \(0<E<1/2\). For \(k>1\), the unique positive critical point lies at \(q_s=\log(k/(k-1))\), and it is a strict maximum, since \(U_k''(q_s)=-(k-1)/k\). Its energy is \(U_k(q_s)=E_*(k)\). Each energy below this height has one bounded center component; at the height the inner component closes into a saddle homoclinic loop. The exterior branch does not create further periodic ovals.

**(3) Period quadrature and the high-energy regime.** Denote the left and right turning points on the center oval by \(q_-<0<q_+\). The least period in the original time is
\[
T(E)=\sqrt2\int_{q_-}^{q_+}\frac{dq}{\sqrt{E-V(q)}}
=T_-(E)+T_+(E),
\quad
T_\pm=\sqrt2\int_{\text{corresponding half}}\frac{dq}{\sqrt{E-V(q)}}.
\]
For \(k<1\), the right turning point satisfies \(q_+=E/(1-k)+O(1)\). Scaling \(q=Es/(1-k)\) in the upper integral and splitting off a fixed-width interval near each endpoint gives
\(T_+(E)\sim2\sqrt{2E}/(1-k)\). On the negative side, \(|q_-|=O(\log E)\); exponential growth of \(V(-r)\) and a square-root turning-point bound yield \(T_-(E)=O((\log E)/\sqrt E)\). This proves the first period asymptotic, including independence from \(h\).

**(4) The infinite-position barrier.** At \(k=1\), write \(\delta=1/2-E>0\) and \(z=e^{-q}\), so
\[
T_+(E)=\sqrt2\int_{z_*(\delta)}^1
\frac{dz}{z\sqrt{z-z^2/2-\delta}},
\qquad z_*(\delta)=1-\sqrt{1-2\delta}=\delta+O(\delta^2).
\]
On a fixed small interval \(z\in[z_*,\eta]\), comparison with the exactly integrable kernel \(1/[z\sqrt{z-\delta}]\), followed by \(z=\delta(1+s^2)\), gives \(\sqrt\delta\,T_+(E)\to\pi\sqrt2\); the complementary interval contributes only \(O(1)\). The lower half-period stays bounded as \(E\uparrow1/2\), since its negative turning point remains regular. At the critical energy, the forward outgoing motion obeys
\[
\dot q=\sqrt{2e^{-q}-e^{-2q}},\qquad
\frac{d}{dt}e^{q/2}=\frac12\sqrt{2-e^{-q}}\longrightarrow\frac1{\sqrt2}.
\]
Hence \(e^{q/2}/t\to1/\sqrt2\), which yields \(t^2(1-y(t))\to2\) and \(t x(t)\to2\). Such a trajectory takes infinite time to reach \(y=1\).

**(5) The finite-saddle logarithm.** At \(k>1\), put \(\lambda=\sqrt{(k-1)/k}\). As \(q\uparrow q_s\),
\[
U_k(q)=E_*(k)-\frac{\lambda^2}{2}(q_s-q)^2+O((q_s-q)^3).
\]
If \(\delta=E_*(k)-E\), the positive turning point satisfies \(q_s-q_+=\sqrt{2\delta}/\lambda+O(\delta)\). The singular portion of the positive half-period is therefore
\[
\sqrt2\int^{q_+}\frac{dq}{\sqrt{\lambda^2(q_s-q)^2/2-\delta}}
=\frac1\lambda\log\frac1\delta+O(1).
\]
Analyticity of the potential and the nondegenerate saddle control the error uniformly after subtracting this singular model. Again the negative half-period is bounded and cannot modify the coefficient.

**(6) Exhaustiveness and completeness inside the stated domain.** Mechanical energy prevents finite-time escape toward \(q=-\infty\). Toward \(q=+\infty\), the bounded-energy velocity satisfies \(|\dot q|=O(1)\) at \(k=1\) and \(|\dot q|=O(\sqrt{1+q})\) at \(k>1\), so finite-time escape is impossible. Uniqueness of the mechanical flow and the one-dimensional potential graph exclude other periodic components. These arguments justify the maximal annulus assertions without relying on finite trajectory sampling.

## Verification
Run \`python checker.py\` in an environment with SymPy and mpmath. The standalone script verifies exact symbolic differentiation, mechanical conservation, the saddle position, barrier height and curvature, the critical potential identity, and three finite-precision positive-period quadratures spanning the regimes. Those finite examples are consistency tests, not proofs of the quantified claims. The analytic arguments in Steps (1)–(6) prove the global statements and asymptotic coefficients.

## Relationship to prior work
Da Cruz and Torregrosa (arXiv:2204.00085, first publicly posted March 31, 2022) introduce the piecewise quadratic family with invariant line and classify the local center condition; their Theorem 1.4 includes the reversible subfamily with zero mixed quadratic coefficients. The *global* maximal annulus transition and the three leading original-time period-edge laws above are separate claims and are not consequences of merely knowing the local center condition.

Marín and Villadelprat (arXiv:2203.12966, 2022) analyze outer-boundary critical periods of **smooth** reversible Loud quadratic centers, including asymptotic expansions around their polycycles. Their results provide relevant context for the smooth specialization \(h=k\), but do not state an all-\(h\) piecewise classification or the three-regime leading coefficient formula of this theorem.

Rezende, Santos and Torregrosa (Research in the Mathematical Sciences, 2026, DOI 10.1007/s40687-026-00606-1) analyze local critical periods and weak isochronous centers in piecewise reversible quadratic systems. Their main theorems concern local period-constant bifurcations, rather than the global transition at \(k=1\) derived here. Smooth-system energy-barrier asymptotics are classical; no priority is claimed for those principles themselves.

## Limitations
The theorem is confined to the displayed continuous two-zone subclass, nonnegative coefficients, and \(y<1\). It does not classify all parameter choices or all centers in the broader piecewise quadratic family, other components of the full phase plane, or perturbation-induced limit cycles. No monotonicity of \(T(E)\) away from the stated asymptotic regimes is asserted. Published equivalences beyond the inspected literature could affect publication priority, and independent mathematical audit has not been performed.

## References
- L. P. C. da Cruz and J. Torregrosa, *Bifurcation of limit cycles in piecewise quadratic differential systems with an invariant straight line*, arXiv:2204.00085 (first version March 31, 2022), https://arxiv.org/pdf/2204.00085.
- D. Marín and J. Villadelprat, *The criticality of reversible quadratic centers at the outer boundary of its period annulus*, arXiv:2203.12966 (first version March 24, 2022), https://arxiv.org/pdf/2203.12966.
- A. C. Rezende, M. A. S. Santos and J. Torregrosa, *Period function of planar piecewise reversible quadratic systems*, Research in the Mathematical Sciences 13, article 25 (2026), https://doi.org/10.1007/s40687-026-00606-1.
