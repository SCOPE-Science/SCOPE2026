# Finite-round shift of the forward–backward contagion threshold and critical algebraic relaxation

## Finding

For the exact large-population, discrete-round two-stage contagion map of Muñoz, Nuño and Meacci [1], the nonlinear adoption-free threshold has a *unique finite-round critical direct-adoption probability* \(p_*(\nu,\tau)\) strictly below \(1/2\). Above this value, the invasion threshold has a locally attracting endemic branch on the supercritical side; below it, the small positive endemic branch lies on the subcritical side and is a saddle. At the exact invasion threshold, when \(p>p_*\), every sufficiently small physical initial state containing a positive fraction of adopters has the sharp critical law
\[
\lim_{n\to\infty}n a_n=-\frac1Q,\qquad
\lim_{n\to\infty}\frac{z_n}{a_n}=\alpha,\qquad
\lim_{n\to\infty}\frac{w_n}{a_n}=\omega.
\]
All parameters and constants are explicit below. The continuous-round limit satisfies \(p_*\to1/2\), agreeing with the known continuous-time division [2]. The finite-round shift and the coefficient \(Q\) are conclusions about the deterministic map, not about indefinite survival of its finite-population Markov-chain counterpart.

## Assumptions and scope

Fix positive \(\nu=\mu/\gamma\), \(\tau=\gamma\tau_{\rm physical}\), and \(p\in(0,1)\). The contact-to-cessation ratio \(\rho=\beta/\gamma>0\) is a parameter. Use the state variables \(z=s_1\) (primed susceptible), \(a\) (adopter), \(w=r\) (recovered), with naive susceptible \(s_0=1-z-a-w\). The physical simplex is \(z,a,w\ge0\) and \(z+a+w\le1\). Put
\[
 m=\nu\tau,\quad E=e^{-m},\quad u=1-E,\quad
 \lambda=e^{-(1+\nu)\tau},\quad v=1-\lambda,\quad
 L=\frac{\rho v}{1+\nu},\quad
 P(a)=1-e^{-(La+m)},\quad B(a)=\frac{La}{La+m}P(a).
\]
The smooth map, including its continuous extension at \(a=0\), is
\[
 \begin{split}
 z'&=(1-p)(1-z-a-w)B(a)+z[1-P(a)],\\
 a'&=p(1-z-a-w)B(a)+zB(a)+\lambda a,\\
 w'&=Ew+\frac{v}{1+\nu}a.
 \end{split}
\]
It is the exact deterministic large-population limit of the competing-risks round process of [1], not a forward Euler discretization. The adoption-free equilibrium is \((z,a,w)=(0,0,0)\). Its nonhyperbolic invasion surface is
\[
 \rho=\rho_T(p,\nu,\tau):=\frac{(1+\nu)m}{p u},
\]
where the eigenvalues are \(E,E,1\). Statements about the sign of the quadratic coefficient below assume \(p\ne p_*\); the point \(p=p_*\) is not classified.

At the invasion surface write
\[
 \alpha=\frac{(1-p)v}{p u},\qquad
 \omega=\frac{v}{(1+\nu)u},\qquad
 A=u\left(\frac{\nu}{1+\nu}-\frac{u}{v}\right),\qquad
 B_0=-3+(m+3)e^{-m},
\]
\[
 D(p)=u+B_0p+Ap^2,\qquad
 Q=\frac{v^2D(p)}{p^2u^2},\qquad
 p_*=\frac{-2u}{B_0-\sqrt{B_0^2-4Au}}.
\]
The square root is positive, and the given expression denotes the unique positive root of \(D\).

## Proof

**1. Linearization and center directions.** Let \(c=B'(0)\). Direct differentiation of the incidence function gives
\[
 c=\frac{Lu}{m},\qquad
 d=\frac{B''(0)}2=\frac{L^2[(m+1)e^{-m}-1]}{m^2}.
\]
At \(\rho=\rho_T\), \(pc=v\), so the adopter eigenvalue is \(\lambda+pc=1\), and the other two multipliers are \(E\). With adopter component normalized to one, the center eigenvector is \((\alpha,1,\omega)\). The analytic center manifold therefore has
\(z=\alpha a+O(a^2)\), \(w=\omega a+O(a^2)\).

**2. Exact quadratic coefficient.** Substituting these first-order graph expansions into the adopter equation gives the scalar center map
\[
 a'=a+Qa^2+O(a^3),\qquad
 Q=pd+c\alpha(1-p)-pc(1+\omega).
\]
The derivative of the center graph at zero is sufficient at quadratic order because the adopter coordinate has no linear dependence on \(z,w\) at the origin. Inserting \(L=vm/(pu)\), \(pc=v\) and the formulas for \(\alpha,\omega\) simplifies exactly to \(Q=v^2D(p)/(p^2u^2)\). The symbolic identity, as well as the Taylor coefficients, is checked in `check.py`.

**3. Exactly one finite-round sign change.** Since \(t\mapsto(1-e^{-t})/t\) is strictly decreasing for positive \(t\),
\[
 \frac uv>\frac{\nu}{1+\nu},\quad\text{hence } A<0.
\]
Also \(B_0<0\) for \(m>0\), because \((m+3)e^{-m}\) strictly decreases from \(3\). Thus \(D'(p)=B_0+2Ap<0\) on \(p\ge0\). We have \(D(0)=u>0\) and
\[
 D(1/2)=\frac{(m+1)e^{-m}-1}{2}+\frac A4<0.
\]
Consequently exactly one positive root exists, it lies in \((0,1/2)\), and \(Q>0\) for \(0<p<p_*\), \(Q<0\) for \(p_*<p<1\). Since \(u\sim\nu\tau\), \(B_0\sim-2\nu\tau\), \(A=O(\tau^2)\) as \(\tau\downarrow0\) with \(\nu\) fixed, \(p_*\to1/2\).

**4. Direction and stability of the endemic branch.** Vary \(\rho=\rho_T(1+\delta)\), holding \(p,\nu,\tau\) fixed. The eigenvalue in the adopter direction is \(1+v\delta\), and a parameter-dependent center reduction is
\[
 a'=(1+v\delta)a+Qa^2+O(a^3+|\delta|a^2).
\]
For \(Q\ne0\), factoring \(a\) from the fixed-point equation and applying the implicit-function theorem yields the unique small nonzero branch
\[
 a_*(\delta)=-\frac vQ\delta+O(\delta^2),\qquad
 z_*(\delta)=\alpha a_*(\delta)+O(\delta^2),\qquad
 w_*(\delta)=\omega a_*(\delta)+O(\delta^2).
\]
The branch lies in the physical simplex exactly for sufficiently small \(\delta\) of sign opposite \(Q\). Its center multiplier is \(1-v\delta+O(\delta^2)\), while its two transverse multipliers converge to \(E<1\). Hence it is locally attracting for \(Q<0,\delta>0\), and is a saddle with one expanding direction for \(Q>0,\delta<0\). The extinction equilibrium is linearly stable when \(\delta<0\) and unstable when \(\delta>0\).

**5. Parabolic critical relaxation.** At \(\delta=0\), \(Q<0\), the restricted scalar center map is attracting from \(a>0\). The stable transverse directions contract geometrically. The invariant plane \(a=0\) is precisely the local two-dimensional strong-stable manifold of the extinction equilibrium: its exact dynamics is \(z'=Ez\), \(w'=Ew\). Every sufficiently close physical state with \(a_0>0\) lies outside this exceptional plane, remains in the simplex, and converges to the equilibrium. Its center coordinate has \(a_{n+1}=a_n+Qa_n^2+O(a_n^3)\) up to exponentially small transverse corrections, so taking reciprocal differences gives \(a_n^{-1}/n\to-Q\). The stable foliation makes \(z_n-\alpha a_n=o(a_n)\) and \(w_n-\omega a_n=o(a_n)\). This proves the displayed universal limits.

For \(Q>0\), the positive center-manifold germ instead moves away from extinction, proving its instability relative to the simplex at the invasion threshold.

## Verification

The accompanying `check.py` is standalone Python 3 with SymPy and mpmath. It differentiates the exact incidence function symbolically, verifies the closed coefficient identity, checks uniqueness and sign numerically at four parameter pairs, and cross-checks two 180,000-step critical trajectories and small endemic-branch fixed points. Its recorded completion string is `VERIFY_OK exact_center_taylor=2 exact_normal_form_identity=1 unique_transition_examples=4 critical_decay_examples=2 bifurcating_endemic_branches=2`.

The symbolic equalities support the analytic algebra; numerical trajectories do not prove asymptotic statements, and the proof above supplies their infinite-iteration justification.
For illustration, at \(\nu=1/2\) and \(\tau=2\), the separating probability is \(p_*\approx0.39242287372442264\), strictly below the continuous-time one-half boundary.

## Relationship to prior work

The map, the exact invasion surface, and the eigenvalues are from [1], especially its Definition 1 and Proposition 4. Those are **not** claimed as new. The present contribution is the finite-round nonlinear division \(p_*(\nu,\tau)\), direction and local stability of the branch at that surface, and the exact \(1/n\) critical adopter density. Katriel [2] proves forward/backward distinctions in the continuous-time limiting model, including its threshold at \(p=1/2\); this is not a finite-round theorem. Heidecke and Barbarossa [3] establish direction changes for a related continuous-time model with a different replenishment mechanism and equations. The general center-manifold and transcritical tools are standard; the exact model-specific coefficient and its global-in-\(p\) sign structure are the substantive calculation.

## Limitations

Only local phase-space statements near extinction and the first small endemic branch are proved. The degenerate locus \(p=p_*\), global endemic attractors, chaotic windows, and stochastic finite-population survival are outside scope. All conclusions assume fixed \(\nu>0\), strictly positive finite \(\tau\), and \(0<p<1\). Historical priority is provisional pending broader human literature review; the supplied checker is not independent mathematical certification.

## References

[1] F. J. Muñoz, J. C. Nuño, L. Meacci, *From elementary processes to chaos: a discrete-time two-stage contagion model and its continuous limit*, arXiv:2611.08353v1 (first posted 2026-11-05), https://arxiv.org/abs/2611.08353 . Full arXiv HTML Sections 3–8 and original PDF Definition 1 / Proposition 4 examined.

[2] G. Katriel, *The dynamics of two-stage contagion*, arXiv:1812.08867 (2018 preprint; subsequently published), https://arxiv.org/abs/1812.08867 . Especially Proposition 2 and the forward/backward discussion.

[3] J. Heidecke and M. V. Barbarossa, *When ideas go viral—complex bifurcations in a two-stage transmission model*, arXiv:2011.08792, https://arxiv.org/abs/2011.08792 . Especially Theorems 2.3–2.4.
