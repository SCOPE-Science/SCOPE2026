# Log-periodic physical-time relaxation in a homogeneous cubic Lyapunov counterexample

## Finding
Consider the two-parameter homogeneous cubic planar vector-field family introduced by Liu and Fitzsimmons (2026):
\[
\begin{aligned}
\dot x&=-a(x^2+y^2)x+b(x^2-y^2)x-(x^2+y^2)y,\\
\dot y&=-a(x^2+y^2)y+b(x^2-y^2)y+(x^2+y^2)x,
\end{aligned}
\]
where \(a>0\) and \(b\in\mathbb R\). Let \(r(t)=\sqrt{x(t)^2+y(t)^2}\) for a nonzero solution, in the original physical time. There is an **explicit positive smooth periodic profile** \(\Phi_{a,b}\) with period \(2\pi a\) such that
\[
\boxed{\;t r(t)^2=\Phi_{a,b}(\log t+\log C)+O_{a,b,x(0),y(0)}(t^{-1})\;}\qquad(t\to\infty),
\]
where \(C>0\) is specified below. The profile is constant if and only if \(b=0\); in that case it equals \(1/(2a)\). For each \(b\ne0\), the set of subsequential limits of \(t r(t)^2\) is precisely the nondegenerate closed interval \([\min\Phi_{a,b},\max\Phi_{a,b}]\). Thus a globally asymptotically stable cubic system can have order-\(t^{-1/2}\) radial decay with **no limiting multiplicative radial prefactor**.

There is also a canonical initial-state-independent logarithmic occupation law: for every bounded continuous \(g:[0,\infty)\to\mathbb R\),
\[
\lim_{T\to\infty}\frac1{\log T}\int_1^T g(t r(t)^2)\,\frac{dt}{t}
=\frac1{2\pi a}\int_0^{2\pi a}g(\Phi_{a,b}(s))\,ds.
\]
For \(b\ne0\) the right-hand law is non-Dirac; for \(b=0\) it is the point mass at \(1/(2a)\). The coefficient \(C\) is initial-state dependent, but the profile, limit interval, and logarithmic occupation law are universal for each fixed parameter pair.

## Assumptions and scope
The vector field is defined on all of \(\mathbb R^2\). Fix finite real parameters \(a>0\) and \(b\in\mathbb R\). All assertions concern any initial state \((x_0,y_0)\ne(0,0)\) and its unique global forward solution. Choose any continuous lift \(\theta_0\in\mathbb R\) of the starting polar angle. Write
\[
\begin{aligned}
G(\theta)&=\int_0^\infty e^{-2av-b\sin(2(\theta-v))}\,dv
=\frac{\int_0^\pi e^{-2av-b\sin(2(\theta-v))}\,dv}{1-e^{-2\pi a}},\\
I(\theta)&=e^{2a\theta}G(\theta),\qquad
F(\theta)=e^{b\sin2\theta}G(\theta),\\
\Phi_{a,b}(s)&=F\!\left(I^{-1}(e^s)\right),\qquad
C=r_0^2 e^{-b\sin(2\theta_0)+2a\theta_0},\quad I_0=I(\theta_0).
\end{aligned}
\]
The inverse exists globally because \(I:\mathbb R\to(0,\infty)\) is strictly increasing and onto. Angles differing by \(2\pi\) merely shift \(\log C\) by a multiple of the stated profile period; all observables are independent of the angle lift. No uniformity in \(a,b\) or in initial conditions is asserted.

## Proof
**1. Exact physical-time quadrature.** The polar equations are \(\dot r=r^3(-a+b\cos2\theta)\) and \(\dot\theta=r^2>0\). As long as \(r>0\),
\[
\frac{d}{d\theta}\log r^2=-2a+2b\cos2\theta,
\qquad r^2 e^{-b\sin2\theta+2a\theta}=C.
\]
Consequently \(dt/d\theta=C^{-1}e^{2a\theta-b\sin2\theta}\). Differentiation under the integral defining \(I\), or the fundamental theorem of calculus, gives \(I'(\theta)=e^{2a\theta-b\sin2\theta}>0\), and therefore
\[
I(\theta(t))=I_0+Ct,
\qquad r(t)^2=C e^{-2a\theta(t)+b\sin2\theta(t)}.
\]
The bounded positive \(\pi\)-periodic function \(G\) satisfies \(e^{-|b|}/(2a)\le G\le e^{|b|}/(2a)\). Hence \(I(\theta)\) increases from zero to infinity as \(\theta\) ranges over \(\mathbb R\), which also proves the formulas describe the full forward solution. The same bound shows \(r\to0\) as \(t\to\infty\), while \(r(t)>0\) at finite times.

**2. Renormalized periodic profile.** Since \(G(\theta+\pi)=G(\theta)\), one has \(I(\theta+\pi)=e^{2\pi a}I(\theta)\) and \(F(\theta+\pi)=F(\theta)\). Thus \(\Phi_{a,b}\) is smooth, strictly positive, and periodic in \(s\) with period \(2\pi a\). Direct substitution yields the **exact** identity for every \(t>0\):
\[
 t r(t)^2=\left(1-\frac{I_0}{I_0+Ct}\right)
\Phi_{a,b}(\log(I_0+Ct)).
\]
As \(t\to\infty\), the factor is \(1+O(t^{-1})\) and the argument is \(\log t+\log C+O(t^{-1})\). Every periodic smooth function has bounded derivative, giving the displayed uniform-in-time \(O(t^{-1})\) estimate along each orbit.

**3. Nonconstancy and full limit interval.** The function \(F\) obeys, by direct differentiation,
\[
F'(\theta)=\left(2b\cos2\theta-2a\right)F(\theta)+1.
\]
If \(F\) is constant, then \(b=0\) because \(F>0\) and \(\cos2\theta\) varies. Conversely, when \(b=0\), the quadrature gives \(F\equiv1/(2a)\). Since \(I^{-1}\circ\exp\) is a surjection onto \(\mathbb R\), \(\Phi\) is nonconstant exactly when \(F\) is. The leading argument \(\log t+\log C\) runs through every period infinitely often as \(t\to\infty\); by the uniform \(O(t^{-1})\) remainder, every profile value occurs as a subsequential limit and no other value does. The continuous image of one period is exactly the interval between its minimum and maximum.

**4. Logarithmic occupation law.** Substitute \(u=\log t\) in the time average. The asymptotic estimate shows that \(g(e^u r(e^u)^2)-g(\Phi(u+\log C))\to0\) as \(u\to\infty\); on the bounded range of the arguments, continuity of \(g\) is uniform. Cesàro averaging makes its contribution vanish. The mean of the periodic function \(u\mapsto g(\Phi(u+\log C))\) equals its mean over any period, independently of \(C\). If \(b\ne0\), a nonconstant continuous \(\Phi\) has a pushforward of uniform circular measure with non-singleton support, proving the law is not a Dirac mass.

## Verification
The standalone `check.py` uses exact symbolic polynomial identities to confirm the polar radial and angular equations, and high-precision quadrature to check \(I(\theta+\pi)/I(\theta)=e^{2\pi a}\), \(F(\theta+\pi)=F(\theta)\), the exact time-radius formula, and both \(b=0\) and \(b\ne0\) cases. Execute `python3 check.py` with Python packages `sympy` and `mpmath`. It returned `CHECK_OK` with 35 internal checks. Finite numerical checks do not prove the infinite-time asymptotics; those follow entirely from the exact quadrature and periodic-function argument above.

## Relationship to prior work
Liu and Fitzsimmons (arXiv:2607.16171v1, July 17, 2026) established global asymptotic stability, an explicit nonpolynomial Lyapunov function, and obstruction to polynomial or analytic Lyapunov functions. Their Section IV-D introduced precisely this two-parameter cubic family and its polar equations; none of those qualitative facts or equations is claimed as new. The earlier work proves absence of homogeneous polynomial Lyapunov functions only for a specified subregion (including \(a=1,b=5\)); the quantitative theorem here holds throughout \(a>0\), including systems outside that obstruction region. The present statement quantifies **original-physical-time, orbit-level radial relaxation**: a generally nonconvergent normalized amplitude with an explicit universal periodic profile, a complete interval of accumulation values, and a phase-independent logarithmic occupation law.

A related published result, *Exact angular return and physical-time Floquet rigidity for contracting homogeneous star-node cycles* (published-finding corpus record `2026/10/11/SCOPE-exact-angular-return-and-physical-time-floquet-rigidity-for-cont--7c00337eaa41`), concerns \(\dot z=\lambda z+Q(z)\) with \(\lambda>0\) and an attracting nonzero-radius cycle. Its exact angular affine return and cycle Floquet calculation do not state or imply the present explicit \(\lambda=0\) original-time logarithmic relaxation profile. Another comparison, *Global algebraic relaxation and renormalized logarithmic phase at a cubic Liénard weak focus* (record `2026/10/11/SCOPE-global-algebraic-relaxation-and-renormalized-logarithmic-phase-a--33495a7a3125`), proves a **constant** normalized radial limit in a different, nonhomogeneous system; it does not cover the nonconstant logarithmic profile here. Known general homogeneous-flow reductions and discrete scale invariance are acknowledged. No absolute publication priority is claimed.

## Limitations
The claimed profile is specific to the two-parameter homogeneous cubic family and does not cover perturbations, nonconstant angular-speed factors, or other dimensions. It uses Euclidean radius and original physical time; changing the observable can change its normalization. The period \(2\pi a\) is guaranteed but not claimed minimal. The proof gives no elementary closed forms for its extrema. The result concerns physical-time quantitative dynamics, not the previously proved Lyapunov nonexistence, and an equivalent classical calculation in the older homogeneous-focus literature remains a legitimate bibliographic risk. Independent verification has not been performed.

## References
1. J. Liu and M. Fitzsimmons, *A Globally Asymptotically Stable Planar Homogeneous Polynomial Vector Field With No Polynomial Lyapunov Function*, arXiv:2607.16171v1, first public July 17, 2026. Full text at https://arxiv.org/abs/2607.16171; Sections III-A and IV-D.
2. *Exact angular return and physical-time Floquet rigidity for contracting homogeneous star-node cycles*, published research record at https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-angular-return-and-physical-time-floquet-rigidity-for-cont--7c00337eaa41; RESULT.md read for comparison.
3. *Global algebraic relaxation and renormalized logarithmic phase at a cubic Liénard weak focus*, published research record at https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-global-algebraic-relaxation-and-renormalized-logarithmic-phase-a--33495a7a3125; RESULT.md read for comparison.
