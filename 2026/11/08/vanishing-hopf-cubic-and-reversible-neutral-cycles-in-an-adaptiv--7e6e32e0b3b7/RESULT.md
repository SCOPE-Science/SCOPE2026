# Vanishing Hopf cubic and reversible neutral cycles in an adaptive collective-risk game

## Finding

Consider the exponential-feedback collective-risk replicator of Liu, Chen and Szolnoki [1], with the conventions and parameter domain below. At the natural critical cooperation threshold \(T=T_0=(M-1)/(N-1)\), the unique interior equilibrium has a pair of imaginary eigenvalues, but **its first Lyapunov coefficient is identically zero** for every admissible group size, cost, benefit, coupling rate and sigmoid steepness. Thus ordinary nondegenerate supercritical/subcritical Hopf conclusions do not follow at this point.

In the balanced-quota subfamily \(N=2m+1\), \(M=m+1\) (\(m\ge1\)) and \(T=T_0=1/2\), the full nonlinear field is reversible under \((x,r,t)\mapsto(1-x,r,-t)\). Its interior equilibrium is a genuine nonlinear center with an open annulus of distinct periodic trajectories. Indeed, **every periodic trajectory wholly contained in the open unit square belongs to a local continuum of periodic trajectories**, so no such orbit is an isolated attracting or repelling limit cycle. The periods of the small cycles tend to
\[
  P_0=2\pi\sqrt{\frac{8\varepsilon}{\beta c(1-\rho)}}.
\]

The universal cubic cancellation and the balanced center are two linked consequences of the critical binomial-response geometry; the first applies to every quota and the second to symmetric quota only.

## Assumptions and scope

Let \(N,M\) be integers \(1<M<N\), let \(b,c,\varepsilon,\beta>0\), and define
\[
 \Gamma(x)=\binom{N-1}{M-1}x^{M-1}(1-x)^{N-M}, \qquad
 T_0=\frac{M-1}{N-1},\qquad \rho=\frac{c}{b\Gamma(T_0)}.
\]
Assume \(0<\rho<1\), and set the feedback threshold **equal** to \(T=T_0\). Consider the smooth planar system on \((x,r)\in(0,1)^2\):
\[
 \dot x=\frac{x(1-x)}{\varepsilon}\,[b\Gamma(x)r-c],\qquad
 \dot r=-r(1-r)\tanh\!\left(\frac{\beta(x-T_0)}2\right).
\]
The only equilibrium in the open square is \(E=(T_0,\rho)\). If the additional balanced-quota assumption \(N=2m+1\), \(M=m+1\) holds, then \(T_0=1/2\). No assertion of global periodicity, of global attraction, or of the behavior for \(T\ne T_0\) is made.

## Proof

**1. Critical linearization.** Put \(A(x)=x(1-x)/\varepsilon\), \(F(x,r)=A(x)[b\Gamma(x)r-c]\), and \(G(x,r)=-r(1-r)\tanh(\beta(x-T_0)/2)\). Let \(a=F_r(E)=b A(T_0)\Gamma(T_0)>0\) and \(d=G_x(E)=-\beta\rho(1-\rho)/2<0\). Because \(\Gamma'(T_0)=0\), the Jacobian is \(\bigl(\begin{smallmatrix}0&a\\d&0\end{smallmatrix}\bigr)\). Hence its eigenvalues are \(\pm i\omega\) with \(\omega^2=-ad>0\).

**2. Exact cubic cancellation.** Take canonical real coordinates \(X=x-T_0\), \(Y=-a(r-\rho)/\omega\). Then \(\dot X=-\omega Y+f(X,Y)\), \(\dot Y=\omega X+g(X,Y)\), with \(f,g=O(X^2+Y^2)\). The standard planar first-Lyapunov formula in these normalized coordinates (radial cubic coefficient per unit original time) is
\[
\begin{split}
16\ell_1={}&f_{XXX}+f_{XYY}+g_{XXY}+g_{YYY}\\
&+\omega^{-1}\{f_{XY}(f_{XX}+f_{YY})-g_{XY}(g_{XX}+g_{YY})-f_{XX}g_{XX}+f_{YY}g_{YY}\},
\end{split}
\]
with all derivatives evaluated at the origin. The affine-in-\(r\) form of \(F\) gives \(F_{rr}=0\); oddness of the sigmoid at \(T_0\) gives \(G_{xx}(E)=G_{xxr}(E)=0\). Thus this formula simplifies to
\[
 16\ell_1=F_{xxx}(E)-\frac{F_{xr}(E)F_{xx}(E)}{a}
 =b\rho\,[A(T_0)\Gamma'''(T_0)+2A'(T_0)\Gamma''(T_0)].
\]
To evaluate it, write \(n=N-1\), \(p=M-1\), \(Q(x)=x(1-x)\), so \(T_0=p/n\) and
\[
  \frac{\Gamma'(x)}{\Gamma(x)}=\frac{p-nx}{Q(x)}.
\]
Exact differentiation at \(T_0\), where the numerator vanishes, gives
\[
 \Gamma''(T_0)=-\frac{n\Gamma(T_0)}{Q(T_0)},\qquad
 \Gamma'''(T_0)=\frac{2nQ'(T_0)\Gamma(T_0)}{Q(T_0)^2}.
\]
Since \(A=Q/\varepsilon\), the terms in the bracket cancel **identically** and \(\ell_1=0\). No truncated numerical series or special parameter choice enters this identity. Different positive conventions for normal-form amplitude or time multiply \(\ell_1\) by a nonzero factor and therefore preserve its vanishing.

**3. Exact reversibility in the balanced subfamily.** If \(N=2m+1\), \(M=m+1\), then \(\Gamma(x)=\binom{2m}{m}[x(1-x)]^m\) is even about \(x=1/2\). For \(S(x,r)=(1-x,r)\), one has \(F(Sz)=F(z)\), \(G(Sz)=-G(z)\), and hence \(V(Sz)=-DS\,V(z)\) for \(V=(F,G)\). Consequently the local flow satisfies \(S\phi_t=\phi_{-t}S\). The fixed-point line of \(S\) is \(L=\{x=1/2\}\), and the unique interior equilibrium is \(E=(1/2,\rho)\).

**4. The center, periods and nonisolation.** At \(E\), the linear flow is an elliptic rotation. For every sufficiently small \(\delta>0\), the solution from \((1/2,\rho+\delta)\in L\) makes a half-turn and crosses \(L\) again transversely at some \((1/2,r_-)\), with \(r_-<\rho\). This follows from continuous dependence and the implicit function theorem applied to the transverse second crossing of the linearized half-turn; it holds uniformly for small \(\delta\). The reversibility identity, together with both endpoints of the half-orbit belonging to \(L\), forces the reflected half-orbit to return exactly to its initial point. Uniqueness prevents earlier self-intersections; hence each is a periodic orbit, and a continuum of different such orbits surrounds \(E\). Smooth rescaling near the linear center gives the period limit \(2\pi/\omega\), where, because \(T_0=1/2\),
\[
\omega^2=\frac{\beta c(1-\rho)}{8\varepsilon}.
\]
For the nonisolation statement, let \(\mathcal C\) be **any** periodic trajectory contained in the open square. Its Jordan interior contains at least one equilibrium (the planar index of a periodic orbit is \(+1\)); since \(E\) is the sole interior equilibrium, \(E\) lies inside \(\mathcal C\). Therefore \(\mathcal C\) crosses the symmetry line \(L\) on both sides of \(E\). All such crossings are transverse: \(F(1/2,r)=\frac{1}{4\varepsilon}[b\Gamma(1/2)r-c]\) vanishes only at \(r=\rho\), and \(E\notin\mathcal C\). Take one crossing \(z_+\in L\) and the next distinct crossing \(z_-\in L\). Nearby initial conditions \(z\in L\) have nearby transverse second crossings, by continuous dependence. Each nearby orbit therefore closes by the same reversibility argument. Thus \(\mathcal C\) is not isolated; in particular it cannot be an isolated hyperbolic limit cycle.

## Verification

The standalone file `verify.py` uses exact symbolic differentiation for six asymmetric and symmetric binomial quotas. In each case it checks the identity \(F_{xxx}-F_{xr}F_{xx}/F_r=0\), the binomial second/third derivative formulas, and the reversible symmetry where applicable. Independently, high-accuracy ODE integration tests three balanced initial conditions and checks the reflected half-return geometry. Running `python verify.py` (with SymPy and SciPy installed) produces `VERIFY_OK`. The symbolic samples and numerical trajectories are **diagnostic**; the general proof is the derivative and reversibility argument above.

## Relationship to prior work

Liu, Chen and Szolnoki [1] introduced both linear and sigmoid feedback; their System II (Equation 7 and Appendix 2) supplies the exact starting equations. Appendix 2 identifies imaginary eigenvalues at \(T=T_0\), then reports a tiny numerical negative first Lyapunov coefficient and a nondegenerate supercritical-Hopf interpretation. The exact coefficient cancellation shown here addresses that unresolved critical normal-form sign. The balanced-quota reversor additionally proves a full annulus of nonisolated cycles, rather than an isolated attracting cycle. Those authors' established equilibrium and oscillation observations are not claimed as new.

The existing conserved-quantity theorem for *linear* feedback [2] addresses \(\dot r=r(1-r)[u(1-x)-x]\); a nonlinear sigmoid cannot be replaced by that equation without changing the dynamics. Its center theorem for the linear model does not, by itself, imply the exact cancellation for all asymmetric sigmoid quotas or the reversible center for the balanced sigmoid system. Earlier eco-evolutionary feedback oscillations, exemplified by Weitz et al. [3], use different payoff and environment equations and do not determine these coefficients.

## Limitations

Vanishing \(\ell_1\) for asymmetric quotas does **not** determine whether a higher-order weak focus, generalized Hopf mechanism, or another nonlinear phenomenon occurs. The reversibility and center classification require balanced quota and the exact critical threshold; neither is proved for \(T\ne T_0\). No general conclusion about trajectories outside the period annuli is asserted. The absence of a matching result in searched repositories is not a proof of publication priority; unindexed equivalent analyses are a residual risk. The result is a deterministic planar-system statement, not a claim about finite-population stochastic games.

## References

[1] L. Liu, X. Chen, and A. Szolnoki, “Coevolutionary dynamics via adaptive feedback in collective-risk social dilemma game,” *eLife* 12, e82954 (2023). DOI: https://doi.org/10.7554/eLife.82954; public preprint first posted 2022-12-20, DOI: https://doi.org/10.1101/2022.12.19.520980. Relevant material: Equation 7, System II, Appendix 2.

[2] “An exact conserved quantity and neutral oscillation annulus at critical collective-risk feedback,” existing research record `ad472b80-a16a-460b-939a-57a6c2ed1bc9` (linear-feedback model; overlap comparison only).

[3] J. S. Weitz et al., “An oscillating tragedy of the commons in replicator dynamics with game-environment feedback,” *PNAS* 113, E7518–E7525 (2016). DOI: https://doi.org/10.1073/pnas.1604096113.
