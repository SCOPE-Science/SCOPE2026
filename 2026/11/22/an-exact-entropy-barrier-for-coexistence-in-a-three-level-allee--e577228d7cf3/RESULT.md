# An exact entropy barrier for coexistence in a three-level Allee food chain

## Finding

Consider the three-species continuous-time food-chain system of Satar, Naji, and Haque [1]. Whenever its prey nullcline has **two distinct positive coexistence roots** \(u_-<u_+\), both exceeding the middle predator's mortality parameter \(a_2\), a particular relative-entropy functional has an **exact, sign-changing dissipation identity**. It supplies an explicit open subset of the attraction basin of the upper coexistence equilibrium, with a sharp threshold for that entropy-based half-space certificate. Moreover, any nonconstant positive periodic solution, if one exists, must cross the lower coexistence prey level \(u_-\) in both directions, while its mean prey level lies strictly between the two roots.

Write \(v_*=a_4/a_3\), \(w_*=u_+-a_2\), and, for \(x,z>0\),
\[
 h(x\mid z)=x-z-z\log(x/z),\qquad
 \mathcal H(u,v,w)=h(u\mid u_+)+h(v\mid v_*)+a_3^{-1}h(w\mid w_*).
\]
Then every positive initial condition with
\[
\boxed{\mathcal H(u(0),v(0),w(0))<B,
\quad B=h(u_-\mid u_+)>0}
\]
generates a global strictly positive solution converging to \((u_+,v_*,w_*)\). The number \(B\) is the **largest entropy-sublevel threshold that certifies containment in \(u>u_-\)**; it is not claimed to be the true boundary of the full attraction basin.

## Assumptions and scope

Let \(a_1,a_2,a_3,a_4,b_1,b_2\) be strictly positive, and define
\[
 F(u)=\frac{(1-a_1u)(u-b_1)}{u+b_2},\qquad u>0.
\]
The dynamics are
\[
 \dot u=u(F(u)-v),\qquad
 \dot v=v(u-w-a_2),\qquad
 \dot w=w(a_3v-a_4).
\]
Assume that the equation \(F(u)=a_4/a_3\) has **two distinct real roots**
\[
 0<a_2<u_-<u_+.
\]
Because the equilibrium predator coordinates are \(v_*=a_4/a_3>0\) and \(w_*=u_+-a_2>0\), this defines a strictly positive upper equilibrium \(E_+=(u_+,v_*,w_*)\). The lower point \(E_-=(u_-,v_*,u_--a_2)\) is also positive. This theorem applies to every such parameter sextuple, not merely the numerical example below. All convergence statements concern positive classical solutions and the continuous-time model, not stochastic ecological extinction or perturbations of its equations.

## Proof

**1. Exact cancellation.** The weighted entropy is nonnegative and equals zero only at \(E_+\). Since \(a_3v_*=a_4\) and \(w_*=u_+-a_2\), direct differentiation along any positive solution gives
\[
\begin{aligned}
\dot{\mathcal H}
&=(u-u_+)(F(u)-v)
 +(v-v_*)(u-w-a_2)
 +(w-w_*)(v-v_*)\\
&=(u-u_+)\bigl(F(u)-v_*\bigr).
\end{aligned}
\]
The two predator–prey transfers cancel exactly; this is a model-specific consequence of the trophic coefficients and the chosen weights.

**2. Two-root factorization.** Put \(D=(b_1+b_2)(1+a_1b_2)>0\). Polynomial division yields
\[
F(u)=1+a_1(b_1+b_2)-a_1u-\frac{D}{u+b_2}.
\]
For any positive \(s,u\),
\[
F(u)-F(s)=(u-s)\left(-a_1+\frac{D}{(u+b_2)(s+b_2)}\right).
\]
Since \(F(u_-)=F(u_+)\) and the roots are distinct,
\[
D=a_1(u_-+b_2)(u_++b_2).
\]
Substituting into the preceding derivative gives the exact identity
\[
\boxed{
 \dot{\mathcal H}=-\frac{a_1(u-u_+)^2(u-u_-)}{u+b_2}.
}
\]
In particular \(\dot{\mathcal H}\le0\) throughout \(u\ge u_-\), and it is strictly negative for \(u>u_-\), \(u\ne u_+\).

**3. Entropy barrier and global convergence.** The scalar function \(h(x\mid z)\) is nonnegative and proper on \(x>0\), diverging as \(x\downarrow0\) and \(x\to\infty\). It is strictly decreasing on \(0<x<z\). Consequently, if \(u\le u_-\), then
\[
\mathcal H(u,v,w)\ge h(u\mid u_+)\ge h(u_-\mid u_+)=B.
\]
Thus the open set \(\{\mathcal H<B\}\) lies entirely in \(u>u_-\). On that set \(\mathcal H\) cannot increase, so any solution starting there remains in the same strict sublevel for all positive time. Its closed initial-entropy sublevel is a compact subset of the positive octant, because all three scalar entropy terms are proper. Therefore the solution exists globally and remains strictly positive and bounded. LaSalle's invariance principle applies there. The only invariant trajectory within \(\dot{\mathcal H}=0\) and \(u>u_-\) has \(u\equiv u_+\). The first equation then forces \(v\equiv v_*\), and the second forces \(w\equiv w_*\). Hence every such solution converges to \(E_+\).

**4. Exact sharpness of the sublevel certificate.** On the plane \(u=u_-\),
\[
\min_{v,w>0}\mathcal H(u_-,v,w)
=h(u_-\mid u_+)=B,
\]
attained at \((v,w)=(v_*,w_*)\). For every \(C>B\), choosing \(u<u_-\) sufficiently close to \(u_-\) and \((v,w)=(v_*,w_*)\) gives \(\mathcal H<C\). Thus no larger **complete entropy sublevel** lies wholly in the half-space \(u>u_-\). This statement concerns the optimality of the stated certificate, not optimality among all invariant sets or the actual basin boundary.

**5. Restriction on any positive periodic coexistence orbit.** Along a positive periodic solution the integral of \(\dot{\mathcal H}\) over one period is zero. If the entire solution had \(u\ge u_-\) or \(u\le u_-\), the sign identity would force \(\dot{\mathcal H}\equiv0\). Continuity would then make \(u\) identically one of the two roots; the equations force the entire state to be a constant equilibrium. Hence every nonconstant positive periodic solution must satisfy
\[
\min_t u(t)<u_-<\max_t u(t).
\]
In addition, integrating the three logarithmic derivatives over one period \(T\) gives
\[
\langle v\rangle=v_*,\quad
\langle u\rangle-\langle w\rangle=a_2,\quad
\langle F(u)\rangle=v_*,\qquad
\langle f\rangle=T^{-1}\int_0^T f(t)\,dt.
\]
Since \(F''(u)=-2D/(u+b_2)^3<0\), strict Jensen inequality gives \(F(\langle u\rangle)>v_*\) for a nonconstant orbit. The superlevel set \(\{u>0:F(u)>v_*\}\) is precisely \((u_-,u_+)\); therefore
\[
\boxed{u_-<\langle u\rangle<u_+.}
\]
These are **necessary** conditions for such a periodic orbit; its existence is not asserted.

## Verification

All identities and example values can be independently reproduced with the standalone `VERIFY.py` included with this result. The program uses exact symbolic arithmetic for the functional identity, root relation, and strict concavity; it also checks one model-calibrated trajectory numerically. The analytic proof above, not the numerical integration, establishes the statement for all admissible parameters.

For the strictly positive parameter values
\[
(a_1,a_2,a_3,a_4,b_1,b_2)
=\left(\tfrac1{10},\tfrac1{10},\tfrac14,\tfrac3{20},\tfrac15,\tfrac15\right),
\]
the roots and upper equilibrium are exactly
\[
 u_-=1,\quad u_+=\tfrac{16}{5},\quad
 E_+=\left(\tfrac{16}{5},\tfrac35,\tfrac{31}{10}\right).
\]
The barrier is
\[
 B=-\tfrac{11}{5}+\tfrac{16}{5}\log\tfrac{16}{5}
 \approx1.5220825914.
\]
The nonlocal initial state \((2,3/5,31/10)\) has
\[
 \mathcal H=-\tfrac65+\tfrac{16}{5}\log\tfrac85
 \approx0.3040116136<B,
\]
so the **theorem** guarantees convergence to \(E_+\), independently of the numerical trajectory.

## Relationship to prior work

Satar, Naji and Haque [1] introduce precisely this system, derive the positive-equilibrium quadratic and the local-stability criterion for its upper branch (their Theorem 4), and exhibit bistability numerically. Those results are essential foundations, but they do not provide the exact entropy cancellation, maximal complete entropy-sublevel barrier, rigorous nonlocal basin subset, or periodic-crossing statement proved here. The comparison is of mathematical implications: a local Hurwitz criterion plus numerical basins does not yield the quantified global-initial-data statement.

Debnath, Ghosh and Sarkar [2] analyze a different strong-Allee trophic chain with Holling-II and Crowley–Martin predation and a nonlinear top-predator reproduction law. Its model-specific local/global conclusions cannot be directly specialized to the present bilinear trophic cancellations. The general Volterra/relative-entropy Lyapunov technique is classical and is not asserted to be new; the contribution here is its exact **two-root factorization and quantified sharp entropy capture region** for [1]. Related structural Volterra–Lyapunov global stability theory [3] concerns a linear Lotka–Volterra interaction-matrix setting, rather than this nonmonotone rational Allee prey-growth function.

## Limitations

The certified region is a **strict subset** of the true attraction basin; no exact full-basin separatrix or necessary-and-sufficient survival criterion is claimed. Its threshold is sharp only for entire sublevel sets of the particular relative entropy and their containment in \(u>u_-\). The periodic-orbit restrictions are conditional, and do not prove the existence or nonexistence of cycles. The proof assumes two distinct positive prey-nullcline intersections both above \(a_2\), excluding fold equality and parameter regimes with no strictly positive lower coexistence state. Biological stochasticity, environmental variation, spatial diffusion and empirical predictive validity are outside scope.

## References

[1] H. A. Satar, R. K. Naji and M. Haque, *A food chain model with Allee effect: Analysis on the behaviors of equilibria*, AIMS Mathematics **10** (2025), 12598–12618, DOI: https://doi.org/10.3934/math.2025568 (publisher first public date 2025-05-29; Eq. (2), Eq. (4), Theorem 4, numerical section).

[2] S. Debnath, U. Ghosh and S. Sarkar, *Global dynamics of a tritrophic food chain model subject to the Allee effects in the prey population with sexually reproductive generalized-type top predator*, Computational and Mathematical Methods **2** (2020), e1079, DOI: https://doi.org/10.1002/cmm4.1079.

[3] P. Almaraz, P. Kalita, J. A. Langa and F. Soler–Toscano, *Structural stability of invasion graphs for Lotka–Volterra systems*, Journal of Mathematical Biology **88** (2024), article 64, DOI: https://doi.org/10.1007/s00285-024-02087-8.
