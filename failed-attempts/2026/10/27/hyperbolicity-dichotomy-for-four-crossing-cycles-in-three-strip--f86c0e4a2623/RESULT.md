# Hyperbolicity dichotomy for four-crossing cycles in three-strip Hamiltonian flows

## Finding
Consider a planar piecewise-affine Hamiltonian flow on the three regions separated by the vertical lines \(x=-1\) and \(x=1\), with transverse crossings and no sliding. Every primitive periodic orbit with exactly four transverse boundary crossings, in cyclic order right strip, middle strip, left strip, middle strip, satisfies the following alternative.

Let \(u_R\) and \(u_L\) be the means of its two ordinate values at \(x=1\) and \(x=-1\), respectively. Write \(a,b,\alpha\) for the coefficients of \(x,y,1\) in the middle strip's horizontal velocity, and set
\[
\Theta=2a+b(u_R-u_L).
\]
Its nontrivial Poincaré (transverse Floquet) multiplier is strictly less than one when \(\Theta>0\), strictly greater than one when \(\Theta<0\), and equal to one exactly when \(\Theta=0\). Moreover, the last case is not an isolated semistable cycle: it belongs to a local open annulus of four-crossing periodic orbits. Thus every isolated four-crossing periodic orbit is hyperbolic, with attracting/repelling type decided by this single geometric coefficient.

This result is a conditional stability theorem: it does not assert existence of such a cycle for arbitrary coefficients.

## Assumptions and scope
On each region \(i\in\{L,C,R\}\), the autonomous field is
\[
\dot x=a_i x+b_i y+\alpha_i,\qquad
\dot y=c_i x-a_i y+\beta_i,
\]
with real coefficients and Hamiltonian
\[
H_i(x,y)=\tfrac12 b_i y^2-\tfrac12 c_i x^2+a_i xy+\alpha_i y-\beta_i x.
\]
In keeping with the motivating class, one may require \(a_i^2+b_i c_i\ne0\) (isolated equilibrium in each affine subsystem), although the local multiplier argument itself does not use this extra restriction.

A four-crossing periodic orbit is a regular Filippov crossing orbit whose boundary contacts consist of exactly \(P_0=(1,y_0)\), \(P_1=(1,y_1)\), \(P_2=(-1,y_2)\), \(P_3=(-1,y_3)\), encountered in that order: \(P_0\to P_1\) through the right region, \(P_1\to P_2\) through the middle, \(P_2\to P_3\) through the left, and \(P_3\to P_0\) through the middle. At these contacts, both one-sided normal components have the crossing sign. No grazing, sliding, simultaneous corner events, or extra intermediate boundary intersections are allowed.

Define \(u_R=(y_0+y_1)/2\), \(u_L=(y_2+y_3)/2\), \(v_R=(y_0-y_1)/2\), and \(v_L=(y_3-y_2)/2\). Put \(a=a_C\), \(b=b_C\), \(\alpha=\alpha_C\), \(t_R=a+\alpha+b u_R\), and \(t_L=-a+\alpha+b u_L\). The transverse crossing inequalities give \(b v_R>0\), \(b v_L>0\), and
\[
t_R+bv_R>0,\quad t_R-bv_R<0,\quad t_L-bv_L<0,\quad t_L+bv_L>0.
\]
In particular, \(b,b_L,b_R\ne0\). The return multiplier is taken on the \(x=1\) section with ordinate as its local coordinate.

## Proof
First, restriction of each outer Hamiltonian to its own switching line is quadratic in the ordinate. Equality of outer Hamiltonian values at the two hits forces the reflections
\[
y_1=2u_R-y_0,\quad u_R=-\frac{a_R+\alpha_R}{b_R},\qquad
y_3=2u_L-y_2,\quad u_L=\frac{a_L-\alpha_L}{b_L}.
\]
The outer horizontal velocity reverses sign between the two corresponding contacts. If an outer quadratic coefficient were zero, equal energy at distinct contacts would force both normal velocities to be zero. Hence the denominators above are nonzero.

Set \(\Delta=H_C(1,u_R)-H_C(-1,u_L)\). Preservation of the central Hamiltonian on *both* middle-region flight arcs gives the two independent identities
\[
\Delta+t_Rv_R-t_Lv_L+\tfrac b2(v_R^2-v_L^2)=0,
\]
\[
\Delta-t_Rv_R+t_Lv_L+\tfrac b2(v_R^2-v_L^2)=0.
\]
Thus
\[
t_Rv_R=t_Lv_L,\qquad
\Delta+\tfrac b2(v_R^2-v_L^2)=0. \tag{1}
\]
The crossing order implies the four strict inequalities displayed in the assumptions. In particular \(v_R,v_L\) are nonzero and have the same sign.

On a Hamiltonian flight between two transverse vertical sections, differentiation of the conserved energy yields \(dy_{\mathrm{out}}/dy_{\mathrm{in}}=H_y(\mathrm{in})/H_y(\mathrm{out})\). The two outer reflections have derivative \(-1\) each. Multiplying the derivatives of the four flights gives the actual Poincaré multiplier (including the effect of crossing the discontinuity):
\[
\mu=\frac{(t_R-bv_R)(t_L+bv_L)}{(t_L-bv_L)(t_R+bv_R)} >0. \tag{2}
\]
Using \(t_Rv_R=t_Lv_L\), the difference simplifies exactly to
\[
\mu-1=\frac{2b(t_R-t_L)(v_R+v_L)}{(t_L-bv_L)(t_R+bv_R)}. \tag{3}
\]
Its denominator is strictly negative and \(b(v_R+v_L)>0\). Since \(t_R-t_L=\Theta\), the sign of \(\mu-1\) is the *opposite* of the sign of \(\Theta\), and \(\mu=1\) precisely when \(\Theta=0\).

It remains to exclude isolated nonhyperbolic orbits. If \(\Theta=0\), write \(t_R=t_L=t\). When \(t\ne0\), (1) forces \(v_R=v_L\) and \(\Delta=0\), so any sufficiently small common change of \(v_R\) and \(v_L\) preserves both matching-energy equations. When \(t=0\), (1) leaves the one equation \(\Delta+\frac b2(v_R^2-v_L^2)=0\), which defines a smooth one-dimensional family near the given point because its derivative in \(v_R\) is \(b v_R\ne0\). In either case the four local flight maps are smooth by transversality, and the already realized four-flight itinerary persists under small changes. Accordingly these algebraic solution curves correspond to genuine nearby periodic trajectories, forming a local period annulus. Such an orbit is not an isolated limit cycle.

When \(\Theta\ne0\), (3) gives a positive multiplier different from one; its one-dimensional Poincaré fixed point is hyperbolic. The above sign classifies its local stability. This proves the alternative.

## Verification
An independent exact-rational fixture checker, included as `checker.py`, verifies all boundary-energy matching identities, the strict crossing signs, the return-multiplier identity, neutrality criterion and attraction/repulsion sign in 588 algebraic fixtures with both signs of the middle horizontal-velocity coefficient. It also evaluates a four-crossing example given in the motivating source and the reciprocal multiplier under reversing the vector field.

In the published four-crossing example with \(a=0\), \(b=2\), \(\alpha=2/3\), \(u_R=0\), and \(u_L=5/16\), one has \(\Theta=-5/8\), and the computed multiplier is about \(7.16368982517\), hence repelling. This is a consistency witness, not a proof of the universal statement. The proof above supplies the universal quantifiers.

## Relationship to prior work
Pessoa and Ribeiro (arXiv:2106.04638, first posted June 8, 2021) established that a discontinuous three-zone piecewise-affine Hamiltonian system with center/saddle subsystems has at most one crossing limit cycle, and constructed examples. Their primary question was existence and number of isolated cycles, not the above complete local hyperbolicity/period-annulus dichotomy or the explicit geometric stability sign.

Llibre and Valls (Symmetry 13, 1128, 2021) treated configurations of Hamiltonian saddles and cycle counts. Carmona, Fernández-Sánchez, and Novaes (arXiv:2207.14634) studied the crossing-cycle methodology for two-zone systems, not the three-zone classification here. Later papers on cyclicity from three-zone period annuli treat perturbations and Melnikov zeros, which are not a theorem about the unperturbed orbit's transverse multiplier.

## Limitations
The result addresses only regular four-crossing orbits that visit both outer strips. It does not classify trajectories with sliding, grazing, another crossing itinerary, or equilibria. A neutral orbit belongs to a *local* annulus; nothing global about that annulus's maximal extent is claimed. The orientation signs refer to the specified ordering of crossings; time reversal inverts the multiplier and swaps stability. No independent human validation or historical-priority certification is claimed. A plausible 2022 source on three-zone mixed centers and saddles was only accessible through its abstract, so overlap beyond the inspected material remains a residual literature risk.

## References
1. C. Pessoa and R. Ribeiro, *Limit Cycles from Planar Piecewise Linear Hamiltonian Differential Systems with Two or Three Zones*, arXiv:2106.04638 (first posted 2021-06-08), later Electronic Journal of Qualitative Theory of Differential Equations 2022, Paper 27. https://arxiv.org/abs/2106.04638
2. J. Llibre and C. Valls, *Limit Cycles of Planar Piecewise Differential Systems with Linear Hamiltonian Saddles*, Symmetry 13 (2021), 1128, https://doi.org/10.3390/sym13071128
3. V. Carmona, F. Fernández-Sánchez, and D. D. Novaes, *Uniqueness and stability of limit cycles in planar piecewise linear differential systems without sliding region*, arXiv:2207.14634 (two-zone comparison). https://arxiv.org/abs/2207.14634
4. C. Pessoa and R. Ribeiro, *Limit Cycles Bifurcating from a Periodic Annulus in Discontinuous Planar Piecewise Linear Hamiltonian Differential System with Three Zones*, arXiv:2109.10311, https://arxiv.org/abs/2109.10311
