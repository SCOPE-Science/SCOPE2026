# Quadratic foliation, stationary-shell laws, and a hyperchaos obstruction in a switching jerk flow

## Finding

Consider the four-dimensional autonomous piecewise-smooth system of Abou El Qassime, Nhaila and Bahatti,
\[
\dot x=y,\quad \dot y=z,\quad \dot z=-az-by+c(x-\sigma(x)),\quad \dot w=xy+yz,
\]
where \(a,b>0\), \(c\ne0\), and \(\sigma(x)=1\) for \(x\ge0\) and \(-1\) otherwise. For every absolutely continuous solution satisfying the equations almost everywhere, the quantity
\[
J=w-\frac{x^2+y^2}{2}
\]
is constant. The global polynomial coordinate transformation \((x,y,z,w)\mapsto(x,y,z,J)\) conjugates every solution branch to the three-dimensional switching jerk equation together with \(\dot J=0\). Consequently all orbits belong to invariant quadratic graphs.

For every compactly supported invariant probability \(\mu\) of a defined measurable solution flow, its stationary moments satisfy
\[
\boxed{\int z^2\,d\mu=b\int y^2\,d\mu,\qquad
 a\int y^2\,d\mu=c\int(|x|-x^2)\,d\mu.}
\]
If \(\mu\) is not supported on equilibria, the common transverse activity is strictly positive. In particular:

- For \(c<0\), \(\mu\{|x|>1\}>0\); no non-equilibrium compact stationary state remains entirely in \(|x|\le1\).
- For \(c>0\), \(\int x^2\,d\mu<1\), \(\int y^2\,d\mu<c/(4a)\) and \(\int z^2\,d\mu<bc/(4a)\).

For any nonconstant periodic orbit of period \(T>0\) whose contacts with \(x=0\) are finitely many isolated transverse crossings, the four-dimensional Floquet multipliers include two copies of \(1\), and the product of the other two is \(e^{-aT}<1\). In particular, the periodic orbit cannot possess two expanding nontrivial multipliers. More generally, at any non-equilibrium compact ergodic state with well-defined Oseledets exponents and the stated transverse-crossing and integrability assumptions, the Lyapunov spectrum includes two zeros and its remaining exponents sum to \(-a\); hence at most one exponent is positive. This is an exact obstruction to *regular compact-attractor hyperchaos* in the source's four-dimensional autonomous system, including its reported positive-damping parameter choices.

## Assumptions and scope

The sign convention at the switching plane is the printed one: \(\sigma(0)=1\). The theorem concerns absolutely continuous trajectories satisfying the right-hand side almost everywhere and measurable invariant probability measures where a solution flow is defined. There is no assertion of global uniqueness at every nongeneric initial condition on the discontinuity. The conservation and moment identities need no differentiability of the crossing map. For statements about a linearized return map, every switch must be isolated and transverse (\(y\ne0\) at \(x=0\)); the ergodic-exponent statement additionally assumes integrability of the logarithms of crossing saltation norms and tempered, nonvanishing flow-speed in the time direction. No Lyapunov obstruction is asserted for stationary point masses or pathologies lacking a regular variational cocycle.

## Proof

**First integral and reduction.** Every absolutely continuous solution has
\[
\frac{d}{dt}\left(w-\frac{x^2+y^2}{2}\right)
=xy+yz-xy-yz=0
\]
almost everywhere. In the new variable \(J\), the last equation becomes \(\dot J=0\). The inverse transformation is globally polynomial, \(w=J+(x^2+y^2)/2\); thus no local or small-parameter argument is used.

**Exact stationary identities.** Let \(L\) denote differentiation along the three-dimensional vector field on each smooth side. By the absolutely continuous chain rule, \(L|x|=\sigma(x)y\) almost everywhere in time, including an inessential set of transversal crossing times. Two pointwise coboundary identities hold almost everywhere:
\[
 z^2-by^2=
 L(yz)+aL(y^2/2)-cL(x^2/2)+cL|x|,
\]
\[
 ay^2+c(x^2-|x|)=
 L(xz)-L(y^2/2)+aL(xy)+bL(x^2/2).
\]
All these observables are bounded on the support of \(\mu\). Invariance makes the integral of every displayed \(L\)-coboundary zero (equivalently integrate in time and divide by duration), yielding both boxed identities. This applies to arbitrary compact stationary mixtures, not only periodic orbits.

If \(\int y^2\,d\mu=0\), almost every stationary trajectory has \(y=0\) at almost every time and hence, by continuity, identically. The equations then force \(z=0\) and \(c(x-\sigma(x))=0\), so the state lies on an equilibrium line. Thus activity is strictly positive for every measure not supported on equilibria. For \(c<0\), the second identity forces the integral of \(x^2-|x|\) to be positive. Since this integrand is nonpositive for \(|x|\le1\), positive measure must lie outside that slab. For \(c>0\), \(r-r^2\le1/4\) for \(r=|x|\), with equality only at \(r=1/2\). Equality for an invariant measure would force \(x\) constant almost surely, hence an equilibrium measure, so the upper activity bound is strict. Also \(\int(r-r^2)\,d\mu>0\) implies \(\int r^2\,d\mu<1\): otherwise Cauchy–Schwarz gives \(\int r\,d\mu\le\sqrt{\int r^2\,d\mu}\le\int r^2\,d\mu\), a contradiction. Use the first identity for the \(z\)-bound.

**Variational determinant and Lyapunov obstruction.** Within either open half-space, the Jacobian of the three-dimensional base has constant trace \(-a\). At a transverse crossing, the saltation matrix is
\[
 S=I_3+\frac{(f^{\rm after}-f^{\rm before})e_1^{\mathsf T}}{y}.
\]
The jump vector has only a third component, whereas its normal component vanishes. The matrix determinant lemma therefore gives \(\det S=1\) for either crossing direction. Liouville's formula between crossings implies \(\det D\phi_T=e^{-aT}\) over any finite transverse itinerary. The full system is polynomially conjugate to \(\phi_T\times\operatorname{id}\); the extra identity direction contributes one unit multiplier. For a nonconstant periodic orbit, the autonomous time direction supplies a second unit multiplier, so the remaining two have product \(e^{-aT}\). Their moduli cannot both exceed one. For the specified regular ergodic state, the first-integral coordinate supplies a zero exponent, the nonvanishing autonomous time direction a second, and the determinant identity fixes the sum of the remaining two at \(-a<0\). Thus there can be at most one strictly positive exponent.

## Verification

The standalone `checker.py` verifies symbolically, with exact algebra rather than time-series data: conservation of \(J\); determinant-one global coordinate change; both local coboundary identities; smooth divergence \(-a\); and determinant-one crossing saltation. Reproduce with `python checker.py`, requiring Python and SymPy. The proof of stationary measure consequences and periodic Floquet structure is analytical and does not rely on simulations. The variational assertions do not infer general non-grazing behavior from a numerical orbit.

## Relationship to prior work

Abou El Qassime, Nhaila and Bahatti introduced the four-dimensional equations and reported a hyperchaotic regime for \((a,b,c)=(1/2,1,-1)\), mainly using simulated phase portraits, Lyapunov spectra and synchronization. The full accessible source paper (sections 2–6, equations and figures) was examined; it does not state this quadratic first integral, the two invariant-measure identities or the two-neutral-exponent obstruction. Their earlier 2023 paper concerns three-dimensional jerk examples; the accessible source description does not supply the four-dimensional claim. General saltation and cocycle methods are standard and are not asserted to be new. The new contribution is their exact joint application to this specific published system, including an all-parameter structural constraint and a sharp sign-dependent recurrent-shell implication.

## Limitations

A discontinuous right-hand side may require additional solution-selection conventions for initial data on the switching plane; no well-posedness theorem at all such points is claimed. The spectral conclusion excludes equilibria, grazing switchings, undefined variational cocycles and noncompact transient numerical trajectories. The invariant-measure laws do not establish existence of a non-equilibrium stationary measure. They do not invalidate every numerical observation in the source; they exclude the usual two-positive-exponent interpretation for compact, regular autonomous invariant dynamics. There may be unindexed equivalent studies. The article's earliest full-text online day was not located directly; the conference technical program places its presentation on 24 November 2023, while the publisher's other article in the same proceedings volume bears a later December date.

## References

1. A. Abou El Qassime, H. Nhaila, and L. Bahatti, *A new hyper-chaotic system with equilibrium lines: dynamic analysis and synchronization*, E3S Web of Conferences 469, 00051 (2023). https://doi.org/10.1051/e3sconf/202346900051
2. ICEGC 2023 Technical Program, Friday 24 November 2023, Session 18, listing the preceding work. https://www.iraset.org/icegc2023/files/ICEGC%272023%20Final%20Program.pdf
3. A. Abou El Qassime, H. Nhaila and L. Bahatti, *Determination of chaos in different jerk systems: dynamical study, circuit design*, IRASET 2023 conference paper (referenced in [1]).
