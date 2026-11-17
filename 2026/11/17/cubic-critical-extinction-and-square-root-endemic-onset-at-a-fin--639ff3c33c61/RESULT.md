# Cubic critical extinction and square-root endemic onset at a finite-round contagion degeneracy

## Finding

The discrete-round, two-stage contagion map defined below possesses a distinguished codimension-two invasion point. For every turnover ratio \(\nu>0\) and round length \(\tau>0\), the transition probability \(p=p_c(\nu,\tau)\) is uniquely specified by an elementary quadratic equation. The finite-round existence of this boundary and its ordinary (nondegenerate) branch direction are not claimed here as new. **The result concerns the previously unclassified equality case.** At the invasion contact intensity, the adopter-normalized center map is
\[
 a_{n+1}=a_n-Ca_n^3+O(a_n^4),\qquad C=C(\nu,\tau)>0,
\]
with the explicit coefficient below. Every sufficiently small physical initial state containing a positive fraction of adopters converges to extinction and has the sharp law
\[
 \lim_{n\to\infty}n a_n^2=\frac1{2C}.
\]
For contact intensity \(\rho=\rho_T(1+\eta)\), the unique sufficiently small **positive** endemic equilibrium appears precisely for \(\eta>0\), satisfies
\[
 a_*(\eta)=\sqrt{\frac{\kappa}{C}}\sqrt\eta+O(\eta),
\]
and is locally asymptotically stable. For sufficiently small \(\eta<0\), no nearby positive endemic equilibrium exists. All results are local in phase space and parameters, rather than claims of global extinction or absence of remote attractors.

## Assumptions and scope

The fractions \(z,a,w\) denote primed susceptibles, adopters, and recovered individuals, respectively. The naive susceptible fraction is \(s_0=1-z-a-w\), and the physical simplex is
\[
 \Delta=\{(z,a,w):z,a,w\ge0,\ z+a+w\le1\}.
\]
Fix arbitrary \(\nu>0\) and \(\tau>0\); take \(0<p<1\), contact ratio \(\rho>0\). Define
\[
\begin{gathered}
 m=\nu\tau,\quad e=e^{-m},\quad \delta=1-e,\quad
 \kappa=1-e^{-(1+\nu)\tau},\quad g=\frac1{1+\nu},\\
 B=\frac{\rho\kappa}{1+\nu},\quad
 P(a)=1-e^{-(m+Ba)},\quad q(a)=\frac{Ba}{m+Ba}P(a).
\end{gathered}
\]
The large-population map of Muñoz, Nuño, and Meacci [1] is exactly
\[
\begin{aligned}
 z'&=(1-p)(1-z-a-w)q(a)+z[1-P(a)],\\
 a'&=p(1-z-a-w)q(a)+zq(a)+(1-\kappa)a,\\
 w'&=ew+\kappa ga.
\end{aligned}
\]
It preserves \(\Delta\). Set
\[
 R=\frac{\delta-me}{\delta^2}>0,\quad
 Q(p)=1-(2+\delta R)p+\left(1-g-\frac\delta\kappa\right)p^2.
\]
Define \(p_c=p_c(\nu,\tau)\) as the unique root of \(Q(p)=0\) in \((0,1/2)\); this is the degenerate branch-direction boundary. At this \(p\), put
\[
 \rho_T=\frac{(1+\nu)m}{p_c\delta},\quad
 B_0=\frac{\kappa m}{p_c\delta},\quad
 c=1+\frac{\kappa g}{\delta}.
\]
The explicit, strictly positive coefficient is
\[
\boxed{
 C=\frac\kappa2\left[c^2+\frac{B_0^2e}{\delta^2}
  +\frac{B_0^2}{m^2}\left(\frac1{p_c^2}-1-(2-p_c)^2\right)\right]>0.
}
\]
All asymptotics in the contact perturbation \(\eta\to0\) hold at fixed \(\nu,\tau,p=p_c\). The recurrence and rate at \(\eta=0\) hold for sufficiently small initial states in \(\Delta\) with \(a_0>0\). No assertion concerns the finite-population absorbing Markov chain.

## Proof

**1. The distinguished parameter is well defined.** Since \(m>0\), \(e^m>1+m\) implies \(\delta-me>0\) and hence \(R>0\). Put \(t=(1+\nu)/\nu>1\). Strict concavity of \(x\mapsto1-e^{-x}\) gives \(\kappa=1-e^{-tm}<t(1-e^{-m})=t\delta\), whereas \(1-g=1/t\). Consequently
\[
 Q(0)=1>0,\qquad Q(1/2)=-\frac{\delta R}{2}
 +\frac{1/t-\delta/\kappa}{4}<0,
\]
while \(Q(1)=-g-\delta R-\delta/\kappa<0\). Because \(Q\) is quadratic, it has exactly one zero in \((0,1)\), which lies in \((0,1/2)\). At \(\rho=\rho_T\), the Jacobian of the map at the extinction state \(E_0=(0,0,0)\) has multipliers \(e,e,1\); the unit multiplier is simple.

**2. Exact scalar equilibrium reduction.** An equilibrium with adopter fraction \(a>0\) must have
\[
 w=\frac{\kappa g}{\delta}a,\qquad
 s_0=\frac{(1-ca)(m+Ba)}{m+(2-p)Ba},\qquad
 z=\frac{(1-p)Ba(1-ca)}{m+(2-p)Ba}.
\]
These identities follow directly from the \(w\)- and \(z\)-equilibrium equations. Inserting them into the adopter equation yields **exactly**
\[
 0=a[H_B(a)-\kappa],\quad
 H_B(a)=\frac{B[1-e^{-(m+Ba)}](Ba+pm)(1-ca)}
  {(m+Ba)[m+(2-p)Ba]}.
\]
This reduction is analytic near \(a=0\), and its nearby positive roots give physical equilibria because all fractions remain nonnegative for sufficiently small positive \(a\). At \(\rho=\rho_T\), one has \(B=B_0\) and \(H_{B_0}(0)=\kappa\). Differentiation gives
\[
 H'_{B_0}(0)=\frac{\kappa^2}{\delta p^2}Q(p).
\]
Thus this derivative vanishes at \(p=p_c\); the usual quadratic term in the center dynamics vanishes as well.

**3. The cubic sign is strictly negative for all eligible rates.** Write \(L(a)=\log H_{B_0}(a)\). At \(p=p_c\), \(L'(0)=0\). Direct logarithmic differentiation gives
\[
 L''(0)=-c^2-\frac{B_0^2e}{\delta^2}
 +\frac{B_0^2}{m^2}\left[1+(2-p_c)^2-\frac1{p_c^2}\right].
\]
For \(0<p\le1/2\) the bracket is negative: indeed \(p^2[1+(2-p)^2]\) is increasing on this interval and equals \(13/16<1\) at \(p=1/2\). Therefore \(H''_{B_0}(0)=\kappa L''(0)=-2C<0\), with the stated formula and \(C>0\). This is a strict analytical sign proof, not an inference from sampled parameter values.

**4. The equilibrium curvature is the true center-manifold cubic.** At the critical contact ratio, the center eigendirection, normalized by adopter coordinate, is
\[
 (z,a,w)=\left(\frac{(1-p_c)\kappa}{p_c\delta},1,
 \frac{\kappa g}{\delta}\right)a+O(a^2).
\]
The adopter equation has no linear dependence on \(z,w\). Its quadratic coefficient is exactly \(H'_{B_0}(0)=0\). Hence on the analytic local center manifold \(a'=a+O(a^3)\). Its invariance equations for the two stable components agree through quadratic order with the stationary equations (since replacing \(a\) with \(a'\) changes their graphs only at cubic order). Therefore the stable-component center graphs agree through degree two with those in Step 2. Substitution into the adopter equation identifies the center cubic with \(H''_{B_0}(0)/2=-C\). This proves the asserted center normal form and, by center-manifold stability theory, local asymptotic stability at \(\eta=0\).

**5. Sharp critical extinction clock.** For any nonstationary positive center trajectory near zero,
\[
 a_{n+1}=a_n(1-Ca_n^2+O(a_n^3))
\]
implies
\[
 a_{n+1}^{-2}-a_n^{-2}=2C+O(a_n),
\]
so telescoping and Cesàro averaging yield \(a_n^{-2}/n\to2C\). The set \(a=0\) is an invariant, exponentially contracting two-dimensional manifold and is precisely the local strong-stable manifold of \(E_0\). Standard local stable foliation about the attracting center manifold gives exponentially close shadowing by a center trajectory. An initial physical state with \(a_0>0\) does not lie in \(a=0\), so its shadowing center trajectory is nonstationary and positive. The exponentially small difference does not affect the \(n a_n^2\) limit. The stated rate therefore holds for every sufficiently small physical state with positive adopter fraction.

**6. Square-root onset and local stability.** Let \(\eta=\rho/\rho_T-1\), so that \(B=B_0(1+\eta)\). Because \(H_B(0)=\kappa(1+\eta)\), Taylor expansion at the degeneracy gives
\[
 H_B(a)-\kappa=\kappa\eta-Ca^2+O(a^3+|\eta|a).
\]
A quadratic blow-up \(a=\sqrt\eta\,v\) followed by the implicit-function theorem gives one positive nearby root for all small \(\eta>0\) with \(v\to\sqrt{\kappa/C}\). For \(\eta<0\) there are no nearby positive roots, by strict negativity of the expansion in a sufficiently small neighborhood. On the endemic branch, \(H'_B(a_*)=-2Ca_*+O(\eta)<0\). Eliminating the two contracting stationary components as in Step 2, the Schur-complement formula for the Jacobian at multiplier one shows that the remaining near-unit multiplier lies below one; the other two remain strictly inside the unit circle. Thus the endemic equilibrium is locally attracting. All statements here are restricted to a sufficiently small neighborhood of the critical point.

## Verification

The standalone `CHECK.py` uses exact symbolic differentiation to validate the stationary elimination and Taylor identities. High-precision tests evaluate the universal sign and square-root scale for five distinct positive turnover/round pairs. Direct iterations independently check the critical inverse-square relaxation in two cases. Run `python CHECK.py` with SymPy and mpmath installed; the last line is `VERIFY_OK cubic_degeneracy=5 stationary_identity=3 critical_relaxation=2`. Numerical tests corroborate but do not replace the argument above.

For example, at \(\nu=1\), \(\tau=\log 2\), the critical probability is the unique positive root of
\[
 1-(3-\log 2)p-\frac{p^2}{6}=0,
\]
namely \(p_c=0.4207036521773739\ldots\), and \(C=16.00637197485935\ldots\). The predicted critical limit is \(1/(2C)=0.0312375596909364\ldots\).

## Relationship to prior work

Muñoz, Nuño, and Meacci [1], first publicly available November 5, 2026, derive this exact competing-risks map, its invasion multiplier, and a parametric representation of endemic equilibria. Their local bifurcation discussion does not classify the codimension-two zero-quadratic case. Katriel [2] analyzes the continuous-time two-stage model and its qualitative forward/backward bifurcation division at direct-adoption probability \(1/2\). These are different statements: the present result concerns the **finite-round equality locus**, proves its cubic coefficient has a strict universal sign, and supplies a sharp discrete-time extinction clock and the square-root branch amplitude. The ordinary nondegenerate finite-round forward/backward branch division is not part of the novelty claim.

## Limitations

The result is local for fixed positive \(\nu,\tau\). It neither proves global convergence nor rules out remote endemic states, periodic attractors, or chaos; it does not describe stochastic persistence or absorption times in finite populations. The bounds implicit in the local remainder are not uniform as \(\nu\) or \(\tau\) approach zero or infinity. Historical-priority assessment is based on the identified relevant literature and is not independent validation.

## References

[1] F. J. Muñoz, J. C. Nuño, and L. Meacci, *From elementary processes to chaos: a discrete-time two-stage contagion model and its continuous limit*, arXiv:2611.08353v1, first public November 5, 2026, https://arxiv.org/abs/2611.08353.

[2] G. Katriel, *The dynamics of two-stage contagion*, arXiv:1812.08867v2 (2018), https://arxiv.org/abs/1812.08867; published in *Chaos, Solitons & Fractals: X* 2 (2019), article 100010.
