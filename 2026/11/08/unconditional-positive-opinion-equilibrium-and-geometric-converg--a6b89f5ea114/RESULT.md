# Unconditional positive-opinion equilibrium and geometric convergence in an adaptive leadership network

## Finding
For the positive-initial-opinion branch of the co-evolving opinion–leadership model of Alutto, Zino, Johansson and Fontan [1], one has an unconditional uniqueness and computation theorem. No small-disagreement or large-leadership-growth assumption is needed. More precisely, for all \(n\ge1\), every row-stochastic nonnegative \(W\), all \(\alpha,\beta>0\), and all strictly same-sign original opinions, the dynamically accessible opinion box contains exactly one equilibrium of the full coupled equations. It has an explicit globally convergent, two-sided stationary solver. In addition, the *fast-leadership reduced continuous-time equation* converges exponentially to that equilibrium throughout the box, with a parameter-explicit rate. These are one combined result about the same equilibrium, not a claim of global convergence of the finite-speed coupled equations.

## Assumptions and scope
Let \(W\in\mathbb R_{\ge0}^{n\times n}\) satisfy \(W\mathbf1=\mathbf1\); irreducibility, symmetry, and positive diagonal entries are not assumed. Set \(u_i=x_i(0)\in[-1,1]\), \(\alpha,\beta>0\), and let \(\rho=\alpha/\beta\). The source model [1, equation (1)] is
\[
\dot x_i=-(1-y_i)(x_i-(Wx)_i)-y_i(x_i-u_i),\qquad
\dot y_i=\alpha(1-y_i)x_i^2-\beta y_i(x_i-(Wx)_i)^2,
\]
with \(y_i\in[0,1]\). Assume either all \(u_i>0\) or all \(u_i<0\). Simultaneous sign reversal of \(x,u\) reduces both cases to \(u_i>0\). Henceforth put \(a=\min_i u_i>0\), \(b=\max_i u_i\le1\), and \(B=[a,b]^n\). The box \(B\times[0,1]^n\) is positively invariant: at \(x_i=a\) both terms in \(\dot x_i\) are nonnegative, at \(x_i=b\) both are nonpositive, and the leadership vector field points inward at \(y_i=0,1\).

Every equilibrium in this box has \(y_i>0\) and satisfies
\[
 y_i=\frac{\rho x_i^2}{\rho x_i^2+(x_i-(Wx)_i)^2},\qquad
 F_i(x):=\rho(x_i-u_i)+\frac{(x_i-(Wx)_i)^3}{x_i^2}=0.\tag{1}
\]
Conversely, every solution of \(F(x)=0\) in \(B\) supplies an equilibrium of the full coupled system through this formula.

## Proof
**1. A scalar order-preserving response.** For \(m,u\in[a,b]\) and \(t>0\), define
\[
 f(t;m,u)=\rho(t-u)+\frac{(t-m)^3}{t^2}.
\]
Its derivative is
\[
 \partial_t f=\rho+\frac{(t-m)^2(t+2m)}{t^3}>0.
\]
Since \(f(\min(m,u);m,u)\le0\le f(\max(m,u);m,u)\), there is exactly one root \(\varphi_u(m)\in[\min(m,u),\max(m,u)]\subseteq[a,b]\). Implicit differentiation shows \(\varphi_u'(m)=3(t-m)^2/[t^2\partial_t f]\ge0\). Set \(T_i(z)=\varphi_{u_i}((Wz)_i)\). Thus \(T:B\to B\) is continuous, increasing, and has precisely the zeros of (1) as fixed points.

**2. Uniform logarithmic contraction.** For the scalar root \(t=\varphi_u(m)\), define its logarithmic elasticity
\[
 e(m,u)=\frac{\partial\log\varphi_u(m)}{\partial\log m}
 =\frac{3m(t-m)^2}{\rho t^3+(t-m)^2(t+2m)}.
\]
The equilibrium identity \((t-m)^3=\rho t^2(u-t)\) gives
\[
 1-e(m,u)=\frac{\rho t^2u}{\rho t^3+(t-m)^2(t+2m)}
 \ge\frac{\rho a^3}{\rho b^3+3b(b-a)^2}=1-q>0.\tag{2}
\]
For logarithmic coordinates \(v_j=\log z_j\), the gradient of \(\log (Wz)_i\) is a nonnegative vector with sum one, even when \(W\) is reducible. Consequently every row sum of the Jacobian of \(v\mapsto\log T(e^v)\) is at most \(q\). The logarithmic cube is convex and complete, so Banach's theorem gives a unique fixed point \(z^*\in B\), and the log-supremum error of any stationary iteration shrinks by \(q^k\).

**3. Certified monotone enclosure.** Start \(L^{(0)}=a\mathbf1\), \(U^{(0)}=b\mathbf1\), and iterate \(L^{(k+1)}=T(L^{(k)})\), \(U^{(k+1)}=T(U^{(k)})\). The scalar root belongs between its two inputs, so \(L^{(0)}\le L^{(1)}\), \(U^{(1)}\le U^{(0)}\). Monotonicity of \(T\) yields
\[
 L^{(k)}\le z^*\le U^{(k)},\qquad
 0\le U_i^{(k)}-L_i^{(k)}\le bq^k\log(b/a).\tag{3}
\]
The last inequality uses logarithmic contraction and \(s-t\le s\log(s/t)\) for \(s\ge t>0\).

**4. Global convergence of the fast-leadership reduced flow.** The reduced equation [1, equation (8)], with leadership slaved to its instantaneous equilibrium, is
\[
 \dot z_i=-\frac{(z_i-(Wz)_i)^3+\rho z_i^2(z_i-u_i)}
 {\rho z_i^2+(z_i-(Wz)_i)^2}.\tag{4}
\]
The same inward-boundary argument makes \(B\) invariant. Put \(m_i=(Wz)_i\) and \(H_i(z)=(z_i-m_i)^3/z_i^2\). For \(R=\max_i(z_i/z_i^*)\ge1\), choose a maximizing coordinate \(i\). Then \(m_i\le R(Wz^*)_i\); since \(H_i\) decreases with its neighbor mean and obeys \(H_i(Rz^*)=RH_i(z^*)\),
\[
 F_i(z)\ge R F_i(z^*)+\rho(R-1)u_i=\rho(R-1)u_i.
\]
Similarly, at a minimizing ratio \(r=\min_i(z_i/z_i^*)\le1\), \(F_i(z)\le\rho(r-1)u_i\). Throughout \(B\),
\[
 \frac{z_i}{\rho z_i^2+(z_i-m_i)^2}
 \ge h:=\frac{a}{\rho b^2+(b-a)^2}.
\]
Using \(\dot{\log z_i}=-z_iF_i(z)/[\rho z_i^2+(z_i-m_i)^2]\), the upper and lower extreme logarithmic deviations have upper Dini derivatives at most \(-h\rho aE_+\) and \(-h\rho a(a/b)E_-\), respectively; here \(E_+=\max(0,\log R)\), \(E_-=\max(0,-\log r)\), and \(1-r\ge r(-\log r)\ge(a/b)E_-\). Therefore, with
\[
 c=\frac{\rho a^3}{b[\rho b^2+(b-a)^2]}>0,
\]
we have for every solution of (4) starting in \(B\)
\[
 \big\|\log(z(t)/z^*)\big\|_\infty
 \le e^{-ct}\big\|\log(z(0)/z^*)\big\|_\infty.\tag{5}
\]
In the constant-opinion case \(a=b\), the box is a singleton and all conclusions hold trivially with \(q=0\). Simultaneous sign reversal completes the theorem for negative initial opinions.

## Verification
The fully self-contained `CHECK.py` uses exact fractions to verify a nontrivial two-agent example, reconstructs the leadership equilibrium, runs both bracketing recurrences, compares the certified bound with each finite iterate, integrates the reduced flow numerically, and tests 105 additional random positive row-stochastic networks. Execute `python CHECK.py` with Python 3.10 or later; no external packages are required. These numerical checks are supplementary to the preceding proof.

For \(W=\left(\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\right)\), \(\rho=16\), and \(u=(55/72,1/8)\), the exact equilibrium is \(z^*=(3/4,1/4)\), \(y^*=(36/37,4/5)\). The sufficient fixed-point condition (3) in [1] is already greater than \(8\) at the largest permissible \(\varepsilon=1/4\), so it does not cover this example; (2)–(5) do. Here the certified logarithmic factor is approximately \(0.9961263840\) and the reduced-flow exponential rate is approximately \(0.00419812985\).

## Relationship to prior work
[1] introduces exactly the equations studied here and derives the equilibrium cubic and a *conditional* contraction criterion depending on a lower bound on \(\lvert x_i\rvert\). It also describes the fast-leadership reduction and gives the constant-initial-opinion corollary. The source conclusion explicitly identifies restricting opinions to a positive domain as a possible route to stronger guarantees. The new combined claim replaces the restrictive stationary criterion by one-sign data of arbitrary spread; it obtains a concrete logarithmic contraction, a certified two-sided solver, and a global exponential estimate for the fast-leadership reduced **flow**, not only for stationary iterates. Results on order-preserving and subhomogeneous maps, including [2], furnish broad conceptual tools but neither state the claimed model-specific sharp domain of applicability nor give (2)–(5). A different nonlinear Friedkin–Johnsen model with friction-inspired stubbornness is studied in [3]. General contraction principles themselves are standard and are not claimed as new.

## Limitations
The theorem concerns strictly same-sign initial opinions; it does not address mixed signs, zeros, or other equilibria outside the forward-invariant box. The stationary uniqueness conclusion holds for the original finite-speed coupled equations within this box; the **global exponential convergence** conclusion applies only to its fast-leadership reduced equation (4), not to arbitrary finite-speed leadership trajectories. The constants are explicit but conservative, and neither the logarithmic contraction factor nor the flow rate is asserted sharp. The argument assumes nonnegative row-stochastic influence weights and no exogenous noise or switching. No independent audit has been performed.

## References
[1] M. Alutto, L. Zino, K. H. Johansson, A. Fontan, *On a Co-evolving Opinion-Leadership Model in Social Networks*, arXiv:2603.24381v1 (first public 2026-03-25), https://arxiv.org/html/2603.24381v1 .

[2] B. Lins, *Convergence of iterates in nonlinear Perron-Frobenius theory*, arXiv:2207.14098 (2022), https://arxiv.org/abs/2207.14098 .

[3] D. N. Reynolds and F. Tudisco, *Unique Nash equilibrium of a nonlinear model of opinion dynamics on networks with friction-inspired stubbornness*, arXiv:2304.07556 (2023), https://arxiv.org/abs/2304.07556 .
