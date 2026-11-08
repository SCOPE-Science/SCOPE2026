# Asymmetric critical synchronization and logarithmic relaxation in planar Ricker competition

## Finding
Fix arbitrary unequal competition strengths \(0<\alpha,\beta<1\) with \(\alpha\ne\beta\). Consider the positive-quadrant discrete map
\[
T_{\alpha,\beta}(x,y)=\bigl(xe^{2-x-\alpha y},\;ye^{2-y-\beta x}\bigr).
\]
Its unique positive equilibrium is
\[
E=(u,v),\qquad u=\frac{2(1-\alpha)}{1-\alpha\beta},\qquad
v=\frac{2(1-\beta)}{1-\alpha\beta}.
\]
Every strictly positive initial state converges to \(E\), and the normalized species synchronize at an exponential rate: for each trajectory there is \(0<\rho<1\) such that
\[
\left|\frac{x_n}{u}-\frac{y_n}{v}\right|=O(\rho^n).
\]
Here \(c=2(1-\alpha)(1-\beta)/(1-\alpha\beta)\). The transverse contraction has a sharp parameter distinction: if \(c\ne1\) and the logarithmic ratio never vanishes, its successive ratio tends to \(1-c\); on the resonance \(c=1\), equivalently \(1-2\alpha-2\beta+3\alpha\beta=0\), synchronization is supergeometric, meaning \(\lvert\log(x_n/u)-\log(y_n/v)\rvert=O(r^n)\) for **every** \(0<r<1\). There is an exact dichotomy. Either both normalized deviations converge to zero exponentially, or there are a common constant \(C\in\mathbb R\) and a sign \(\sigma\in\{-1,1\}\) such that, for both \(z_n=x_n/u-1\) and \(z_n=y_n/v-1\),
\[
\frac{1}{z_{2m}^2}=\frac83m+\frac85\log m+C+o(1),\qquad
\lim_{n\to\infty}(-1)^n\sqrt n\,z_n=\sigma\frac{\sqrt3}{2}.
\]
In the second case all the displayed inverse squares are defined for sufficiently large \(m\). In particular \(m z_{2m}^2\to3/8\). Both normalized species have the *same* inverse-square constant \(C\), not merely the same leading and logarithmic coefficients. The non-exponential alternative occurs, for example, for every sufficiently small nonequilibrium initial state on the invariant normalized diagonal \(x/u=y/v\).

## Assumptions and scope
The hypotheses require both competition coefficients strictly between zero and one and unequal; both intrinsic growth parameters are exactly \(2\), and initial states satisfy \(x_0,y_0>0\). Time \(n\) counts full applications of \(T_{\alpha,\beta}\). The constant in an \(O\)-term may depend on the fixed parameters and initial state. No uniformity is asserted as either coupling tends to an endpoint, and the theorem does not identify the complete set of exponentially convergent initial states.

## Proof
**1. Global attraction at the nonhyperbolic boundary.** Baigent, Hou, Elaydi, Balreira and Luís prove in Theorem 3.4 of the cited 2023 paper that every nonnegative orbit of \((xe^{r-x-\alpha y},ye^{s-y-\beta x})\) converges to some fixed point when \(\alpha,\beta>0\) and \(0<r,s\le2\). For the specified coefficients, the fixed points in the closed positive quadrant are the origin, \((2,0)\), \((0,2)\), and \(E\). A strictly positive orbit cannot converge to the origin, since then the ratio of each coordinate at consecutive times tends to \(e^2>1\). Nor can it converge to \((2,0)\), since its positive second coordinate would have successive ratio tending to \(e^{2(1-\beta)}>1\). The analogous first-coordinate argument excludes \((0,2)\). Consequently every positive orbit converges to \(E\), including at the neutral flip threshold.

**2. Exact transverse logarithmic contraction.** Write \(P_n=\log(x_n/u)\), \(Q_n=\log(y_n/v)\), and \(d_n=P_n-Q_n\). The equilibrium equations give
\[
c=u(1-\beta)=v(1-\alpha)=\frac{2(1-\alpha)(1-\beta)}{1-\alpha\beta}\in(0,2).
\]
Subtraction of the two logarithmic updates gives the *exact* identity
\[
d_{n+1}=\left(1-c\int_0^1e^{Q_n+t(P_n-Q_n)}\,dt\right)d_n.
\]
Since \(P_n,Q_n\to0\), the multiplier tends to \(1-c\in(-1,1)\). Thus \(|d_n|=O(\rho^n)\) for some \(\rho<1\). Whenever the ratio remains nonzero, its step multiplier tends to \(1-c\); when \(c=1\), the multiplier tends to zero, so \(|d_n|=O(r^n)\) for every \(r\in(0,1)\), including trajectories that synchronize exactly in finitely many steps. Smoothness of the exponential near the origin yields \(|x_n/u-y_n/v|=O(\rho^n)\). The normalized diagonal is invariant, because on it both normalized populations evolve by the same scalar Ricker map \(g(t)=te^{2(1-t)}\).

**3. A scalar perturbation exponentially small in actual discrete time.** Put \(t_n=x_n/u\), \(s_n=y_n/v\). Using \(u+\alpha v=2\),
\[
t_{n+1}=g(t_n)\exp\bigl(\alpha v(t_n-s_n)\bigr)
=g(t_n)+O(\rho^n).
\]
With \(a_m=t_{2m}-1\), this implies
\[
a_{m+1}=F(a_m)+O(\theta^m),\qquad
F(w)=g(g(1+w))-1,\quad \theta=\rho^2\in(0,1).
\]
Here \(a_m\to0\), \(F(0)=0\), and \(F'(0)=1\).

**4. Elementary exponential shadowing near a unit multiplier.** We spell out the needed local lemma rather than treating the nonautonomous error as negligible without proof. Suppose \(a_m\to0\), \(F\) is a \(C^2\) local diffeomorphism around zero with \(F(0)=0\), \(F'(0)=1\), and \(a_{m+1}-F(a_m)=O(\theta^m)\), \(0<\theta<1\). Choose \(\eta\in(\theta,1)\), then a small neighborhood on which the inverse of \(F\) has Lipschitz bound \(L\) satisfying \(L\eta<1\). For sufficiently large \(N\), the operator on weighted sequences
\[
(\mathcal Ke)_m=F^{-1}(a_{m+1}+e_{m+1})-a_m,
\quad m\ge N,
\]
is a contraction in the norm \(\sup_{m\ge N}|e_m|\eta^{-m}\), on a suitably chosen ball. Its inhomogeneous term is \(O(\theta^m)\), and its Lipschitz constant is at most \(L\eta<1\); the ball can be chosen so that every argument remains inside the inverse's domain. The unique fixed point \(e_m=O(\eta^m)\) yields an exact orbit \(b_m=a_m+e_m\), \(b_{m+1}=F(b_m)\). If this orbit vanishes once it vanishes forever in the local inverse domain, and \(a_m=O(\eta^m)\). Otherwise \(b_m\) is eventually nonzero and has constant sign. This lemma also covers the resonant case in which the *transverse* eigenvalue equals zero: it assumes no inverse of the original planar map.

**5. Exact critical clock.** Taylor expansion of the explicit scalar function gives
\[
F(w)=w-\frac43w^3+\frac8{15}w^5+\frac49w^6+O(w^7).
\]
For a nonzero exact orbit \(b_m\to0\), this implies \(b_{m+1}/b_m=1-\frac43b_m^2+O(b_m^4)\), so the sign stabilizes and \(|b_m|\) decreases. Set \(Z_m=b_m^{-2}\). Direct reciprocal expansion gives
\[
Z_{m+1}-Z_m=\frac83+\frac{64}{15Z_m}+O(Z_m^{-3/2}).
\]
First \(Z_m/m\to8/3\) by averaging the increments, which tend to \(8/3\). This implies \(1/Z_m=O(1/m)\), so summing the recurrence first gives \(Z_m=(8/3)m+O(\log m)\). Consequently \(1/Z_m=3/(8m)+O(\log(m)/m^2)\). Subtracting \((8/3)m+(8/5)\log m\) from \(Z_m\), the consecutive differences of the residual are \(O(m^{-3/2}+\log(m)m^{-2})\), which is summable; therefore the residual converges to a finite constant \(C\). Since \(a_m-b_m=O(\eta^m)\) and \(|b_m|\asymp m^{-1/2}\), the inverse squares of \(a_m\) and \(b_m\) differ by \(O(m^{3/2}\eta^m)=o(1)\). The normalized second coordinate differs from the first by \(O(\rho^{2m})\), so its inverse square has the same \(C\). Finally \(g'(1)=-1\), and the one-step error is exponential; the odd-time deviations have the opposite asymptotic sign, giving the stated full-clock signed limits. If the shadowed orbit is zero, the same estimates and the one-step update give exponential convergence of both coordinates.

## Verification
The companion `verification.py` uses exact symbolic series and exact rational equilibrium identities, followed by long high-precision orbits for three distinct unequal coupling pairs (including one with zero transverse linear multiplier). It checks the coefficient \(-4/3\) of the cubic term, \(8/15\) of the quintic, the \(8/3\) drift, the \(8/5\) logarithmic law, and transverse synchronization. Finite numerical trajectories are only consistency checks; the all-parameter conclusion is established above through the published global convergence theorem and elementary analytic arguments.

## Relationship to prior work
Baigent *et al.* (2023), Theorem 3.4, prove convergence of the entire parameter family to fixed points for growth parameters up to and including two, but do not supply the parameter-independent critical relaxation clock or the exact logarithmic difference contraction. A preceding result for the *symmetric* subfamily \(\alpha=\beta\) proves an analogous leading/logarithmic clock by exploiting exchange symmetry; that result is **not** claimed anew here. The present theorem concerns genuinely unequal coefficients and unequal equilibrium populations. The identity with \(c=2(1-\alpha)(1-\beta)/(1-\alpha\beta)\) and the exponential-shadowing argument ensure that the asymmetric transverse mode, including the zero-eigenvalue case, cannot alter either constant in the critical law. Work on row-regular synchronous Ricker maps gives Floquet spectra of existing cycles, but not the global nonequilibrium orbitwise asymptotics here.

## Limitations
No universal rate for the exponentially convergent exceptional states is claimed. The theorem does not identify their global geometry or prove an invariant foliation. It does not extend to strong competition, unequal intrinsic growth parameters, stochastic perturbations, or a parameter-uniform limit as \(\alpha\) or \(\beta\) tends to an endpoint. Any equivalent theorem not indexed by the consulted literature and mathematical databases remains a publication-priority risk. The proof uses the published convergence theorem as an explicit external premise; it does not reprove that theorem from scratch.

## References
1. S. Baigent, Z. Hou, S. Elaydi, E. C. Balreira, R. Luís, *A global picture for the planar Ricker map: convergence to fixed points and identification of the stable/unstable manifolds*, Journal of Difference Equations and Applications **29** (2023), 575–591, https://doi.org/10.1080/10236198.2023.2222855 (first online 2023-06-26). Theorem 3.4 and the boundary remarks on pages 7–11.
2. H. N. Yeganeh and S. Baigent, *Convexity of non-compact carrying simplices in logarithmic coordinates*, Journal of Difference Equations and Applications **30** (2024), 1671–1691, https://doi.org/10.1080/10236198.2024.2369215 (distinct invariant-set questions and subcritical growth bounds).
