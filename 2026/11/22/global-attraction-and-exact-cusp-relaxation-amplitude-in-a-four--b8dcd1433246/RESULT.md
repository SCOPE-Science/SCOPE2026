# Global attraction and exact cusp-relaxation amplitude in a four-compartment traffic flow

## Finding

Consider the four-mode traffic-compartment flow defined below. Its unique physical equilibrium is globally attracting, although its linearization has a simple zero eigenvalue. With the state ordered as \((S,C,B,T)\), all solutions in the physical simplex converge to
\[
E=\left(\frac1{12},\frac14,\frac14,\frac1{12}\right).
\]
There is a three-dimensional local strong-stable manifold of \(E\) on which convergence is exponential. Every other physical trajectory, apart from its global forward-preimage extension, has an eventual sign \(\sigma\in\{-1,+1\}\) and satisfies the **exact four-coordinate asymptotic**
\[
\boxed{\displaystyle
\lim_{t\to\infty}\sqrt t\left((S,C,B,T)(t)-E\right)
=\sigma\sqrt{\frac{53}{768}}
\left(-\frac13,1,1,-\frac13\right).}
\]
In particular the car-density relaxation coefficient is \(\sqrt{53/768}\), not the coefficient determined by the stationary scalar equation alone.

## Assumptions and scope

Time is continuous, \(t\ge0\). The population fractions \(S,C,B,T\) represent the fractions seeking a trip, using cars, using buses, and using trains. The residual nontravelling fraction is \(H=1-S-C-B-T\). The physical state space is
\[
\Omega=\{(S,C,B,T):S,C,B,T\ge0,\quad S+C+B+T\le1\}.
\]
The exact system is
\[
\begin{aligned}
\dot S&=-\frac{15}{4}S+\frac34(1-C-B-T),\\
\dot C&=S-\frac{C}{1+128C^3},\\
\dot B&=S-\frac{B}{1+128C^3},\\
\dot T&=S-T.
\end{aligned}
\]
This is the constant-demand multi-transit model of Valentine and Bizyaeva with all demand and free-flow parameters \(\alpha_C=\alpha_B=\alpha_T=\omega_C=\omega_B=\beta=1\), population return rate \(\gamma=3/4\), congestion exponent \(n=3\), and capacity \(k=128^{-1/3}\). The last two rates locate an exact triple-equilibrium cusp of the stationarity equation. The physical simplex is forward invariant by a direct inward-vector-field calculation. No seven-dimensional opinion dynamics, stochastic effects, or network heterogeneity is included.

Define the local strong-stable manifold \(W^{ss}_{\mathrm{loc}}(E)\) as the \(C^\infty\) invariant three-dimensional manifold tangent at \(E\) to the three negative-eigenvalue eigendirections. Its global physical basin extension consists of points whose forward trajectory eventually enters this local manifold. The signed asymptotic holds for every physical starting state outside this exceptional set; on the exceptional set the convergence is exponential.

## Proof

**1. Exact cusp and uniqueness.** Put
\[
g(c)=\frac1{1+128c^3},\qquad h(c)=cg(c),\qquad
F(c)=\frac92h(c)+\frac32c-\frac34.
\]
The equilibrium equations yield \(S=T=h(C)\), \(B=C\), and \(F(C)=0\). Direct factorization gives
\[
F(c)=\frac{3(4c-1)^3(4c+1)}{4(1+128c^3)},\qquad
F'(c)=\frac{6(1-64c^3)^2}{(1+128c^3)^2}.
\]
For \(c\ge0\), the unique root is \(c=1/4\). The threefold root is a cubic cusp: \(F(1/4)=F'(1/4)=F''(1/4)=0\), \(F'''(1/4)=192\). As \(h(1/4)=1/12\), the unique equilibrium is \(E\). Its residual population \(H=1/3\) is strictly positive.

**2. Global Lyapunov function.** Introduce the dynamically natural departure variables
\[
v=S-h(C),\qquad z=B-C,\qquad y=T-h(C),
\]
and write \(c=C\). The exact transformed differential equations are
\[
\begin{aligned}
\dot c&=v,\\
\dot v&=-\left(\frac{15}{4}+h'(c)\right)v-F(c)-\frac34(z+y),\\
\dot z&=-g(c)z,\\
\dot y&=(1-h'(c))v-y.
\end{aligned}
\]
Since \(F\) changes sign only at \(1/4\) and points away from neither side, the primitive
\[
U(c)=\int_{1/4}^c F(s)\,ds
\]
is nonnegative and vanishes only at \(c=1/4\). Let
\[
V=U(c)+\frac12v^2+\frac38y^2+32z^2.
\]
Substitution, without approximation, yields
\[
\dot V=-\left(\frac{15}{4}+h'\right)v^2-\frac34 y^2-64gz^2
-\frac34h'vy-\frac34vz.
\]
On \(0\le c\le1\), the elementary bounds \(-1/3\le h'(c)\le1\) and \(g(c)\ge1/129\) hold. Young's inequality therefore implies
\[
\dot V\le-\frac83v^2-\frac38y^2-\frac{125}{1032}z^2.
\]
The compact simplex \(\Omega\) is positively invariant, so LaSalle's argument applies. The only invariant subset of \(v=y=z=0\) has \(F(c)=0\), hence consists of \(E\) alone. Therefore every physical trajectory converges to \(E\).

**3. Exact critical center coefficient.** In the order \((S,C,B,T)\), the equilibrium Jacobian has characteristic polynomial
\[
\chi_E(\lambda)=\frac{\lambda(3\lambda+1)
(12\lambda^2+53\lambda+53)}{36}.
\]
The eigenvalues consist of one simple zero and three strictly negative real numbers, namely \(-1/3\) and \((-53\pm\sqrt{265})/24\). A zero-eigenvalue tangent vector is
\[
q=\left(-\frac13,1,1,-\frac13\right).
\]
Write \(u=c-1/4\). From the factored equation, \(F(c)=32u^3+O(u^4)\). At the equilibrium \(h'(1/4)=-1/3\), \(h''(1/4)=0\), and \(g(1/4)=1/3\). Thus the local center manifold can be expressed as
\[
v=a u^3+O(u^4),\qquad y=b u^3+O(u^4),\qquad z=0
\]
for a smooth choice of center manifold. The absence of lower-order terms follows from the invariance equations and the invertibility of the transverse linear operator. Matching the cubic terms in the equations for \(v\) and \(y\) gives
\[
0=-\frac{41}{12}a-32-\frac34b,
\qquad b=\frac43a,
\qquad a=-\frac{384}{53}.
\]
It follows that the center coordinate obeys
\[
\dot u=-\frac{384}{53}u^3+O(u^4).
\]
On either nonzero center branch the sign cannot change, and differentiation of \(u^{-2}\) gives
\[
\frac{d}{dt}\frac1{u(t)^2}=\frac{768}{53}+O(u(t));
\]
so \(\sqrt t\,u(t)\to\sigma\sqrt{53/768}\). The exponential tracking property of the normally contracting directions transfers this result from the center manifold to every trajectory not on the local strong-stable manifold. The state reconstruction \((S,C,B,T)-E=q u+O(u^2)\) gives the stated four-component limit. On the strong-stable manifold, all components converge exponentially. Global attraction ensures that each physical trajectory eventually lies in the domain of these local alternatives.

## Verification

The standalone `checker.py` reproduces the exact rational factorization, derivative identity, cusp derivatives, full Jacobian characteristic polynomial, transformed-equation identities, Lyapunov derivative and cubic center coefficient. It also integrates two physical initial conditions with opposite signs to verify finite-time approach to the exact limit. The integration is supplementary evidence only; the infinite-time theorem follows from the analytic proof.

## Relationship to prior work

Valentine and Bizyaeva, *Effect of car-centric social norms on traffic congestion in a compartmental model of transit mode utilization*, arXiv:2611.13265 (first posted 9 November 2026), introduced the constant-demand four-dimensional model, obtained its stationary equation, studied hysteresis, and proved global convergence under a sufficient Lyapunov condition. The model and these qualitative results are prior work. The present contribution concerns the **degenerate equality case** and gives the exact global signed relaxation law and its four-dimensional, non-scalar amplitude. General center-manifold theory explains the cubic-root mechanism but does not itself evaluate the critical coefficient or establish global attraction for these physical equations. Related discrete entropic congestion maps and other cusp flows have distinct evolution laws and do not directly give this result.

## Limitations

The statement is a fully specified balanced-rate, constant-demand cusp case, not a general parameter classification. It does not establish dynamics for the seven-dimensional opinion-feedback extension, parameter robustness away from the cusp, or stochastic traffic response. The strong-stable exception is defined dynamically, not by an explicit global algebraic equation. Numerical integration does not replace the proof. Independent external validation and exhaustive historical priority verification have not been performed.

## References

- A. Valentine and A. Bizyaeva, *Effect of car-centric social norms on traffic congestion in a compartmental model of transit mode utilization*, arXiv:2611.13265, v1 posted 9 November 2026, https://arxiv.org/abs/2611.13265 ; full-text v2 https://arxiv.org/html/2611.13265v2 .
- J. Carr, *Applications of Centre Manifold Theory*, Springer, 1981 (standard local center-manifold and stable-foliation methods).
- H. K. Khalil, *Nonlinear Systems*, Prentice Hall, 1996 (Lyapunov and LaSalle convergence methods).
