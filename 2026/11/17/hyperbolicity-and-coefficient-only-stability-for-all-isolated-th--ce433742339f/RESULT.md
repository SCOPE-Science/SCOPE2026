# Hyperbolicity and coefficient-only stability for all isolated three-zone Hamiltonian crossing cycles

## Finding

**Theorem.** Consider a planar piecewise-affine Hamiltonian vector field with three vertical zones bounded by the lines \(x=-1\) and \(x=1\), with vector field in zone \(i\in\{L,C,R\}\)
\[
(\dot x,\dot y)=(a_i x+b_i y+\alpha_i,\ c_i x-a_i y+\beta_i).
\]
Assume real coefficients and \(a_i^2+b_ic_i\ne0\) in each zone. Suppose a periodic orbit crosses both switching lines transversely, has exactly two crossing points on each, traverses all three open zones, and is isolated among nearby crossing periodic orbits. Put
\[
r=-\frac{a_R+\alpha_R}{b_R},\qquad
\ell=\frac{a_L-\alpha_L}{b_L},\qquad
A=b_Cr+a_C+\alpha_C,\qquad
B=b_C\ell-a_C+\alpha_C.
\]
Existence of the assumed orbit forces \(b_Lb_Cb_R\ne0\), and the following conclusions hold:

1. \(AB>0\), \(A\ne B\), and \(b_L,b_C,b_R\) have the same sign.
2. With the crossing points labeled \((1,r+t),(1,r-t),(-1,\ell-u),(-1,\ell+u)\), where \(t,u>0\), define
\[
Q=\frac{(A-b_Ct)(B+b_Cu)}{(B-b_Cu)(A+b_Ct)}.
\]
Then \(Q>0\) and the physical-forward-time transverse multiplier is exactly
\[
\boxed{\mu=Q^{\operatorname{sgn}(b_C)}.}
\]
3. The orbit is necessarily hyperbolic. It is attracting if and only if \(B<A\), and repelling if and only if \(B>A\). This sign criterion involves only affine coefficients, not the amplitudes or flight times. In particular, a nonhyperbolic *isolated transverse crossing* cycle cannot arise within this three-zone Hamiltonian family.

The claim applies uniformly to all center/saddle configurations of the three affine Hamiltonian subsystems. No existence theorem for a proposed set of coefficients is asserted here.

## Assumptions and scope

The discontinuities are understood with the standard crossing convention: at each of the four boundary points the normal velocity is nonzero on both adjacent sides and has matching sign, so that the piecewise flow passes uniquely into the next zone. Sliding, grazing, tangency and cycles lying within only one or two zones are excluded. Isolation refers to the usual Poincaré section in the four-crossing itinerary. The three linear subsystem matrices have trace zero and determinant \(-a_i^2-b_ic_i\ne0\); hence their equilibria are isolated centers or saddles. Switching-line points are not interpreted as stationary equilibria. Affine normalization sets the two parallel switching lines at \(\pm1\).

## Proof

**Step 1: outer reflections and the signs of the normal velocities.** The zone Hamiltonian is
\[
H_i(x,y)=\frac{b_i}{2}y^2+a_i xy-\frac{c_i}{2}x^2+\alpha_i y-\beta_i x,
\qquad (\partial_yH_i,-\partial_xH_i)=(\dot x,\dot y).
\]
At each of the two intersections of a periodic orbit with one switching line, the outer-zone normal velocity has opposite signs; otherwise that zone cannot be entered and later exited. Since \(\dot x\) is affine in the boundary ordinate, this forces \(b_L,b_R\ne0\). Energy conservation in the right outer excursion gives \(H_R(1,y_0)=H_R(1,y_1)\), so \(y_0+y_1=2r\); similarly the left excursion gives \(y_2+y_3=2\ell\). Label the upper/right point \(y_0=r+t\), lower/right \(y_1=r-t\), lower/left \(y_2=\ell-u\), upper/left \(y_3=\ell+u\), with \(t,u>0\). These outer half-returns are exact reflections and each has derivative \(-1\).

The central-zone normal velocities must also change sign between the two visits to \(x=1\), so \(b_C\ne0\) and \(|b_Ct|>|A|\). At \(x=-1\), likewise \(|b_Cu|>|B|\). At the right switch, the normal velocities at upper and lower visits have the signs of \(b_R\) and \(-b_R\) for the outer field and of \(b_C\) and \(-b_C\) for the central field. The crossing convention therefore requires \(\operatorname{sgn}(b_R)=\operatorname{sgn}(b_C)\). The same argument on the left gives \(\operatorname{sgn}(b_L)=\operatorname{sgn}(b_C)\).

**Step 2: two exact Hamiltonian matching equations.** Set \(D=H_C(1,r)-H_C(-1,\ell)\). The central arcs have equal Hamiltonian at their respective endpoints:
\[
H_C(1,r+t)=H_C(-1,\ell+u),\qquad
H_C(1,r-t)=H_C(-1,\ell-u).
\]
Subtracting and adding the equations gives, exactly,
\[
\boxed{At=Bu,\qquad 2D+b_C(t^2-u^2)=0.}\tag{1}
\]
Since \(t,u>0\), either \(A,B\) have the same nonzero sign, or both vanish. If \(A=B\ne0\), (1) implies \(u=t\) and \(D=0\), and nearby positive \(t\) solve both equations. If \(A=B=0\), the second equation of (1) defines a smooth one-dimensional curve through \((t,u)\), because its gradient \((2b_Ct,-2b_Cu)\) is nonzero. In both cases, the original transverse crossing itinerary persists under sufficiently small perturbations of crossing data, so these solutions give an annulus of nearby cycles, contradicting isolation. Thus \(AB>0\) and \(A\ne B\). In particular \(A^2\ne B^2\). Equation (1) also gives the optional amplitude determination
\[
t^2=-\frac{2DB^2}{b_C(B^2-A^2)},\qquad u=\frac{A}{B}t,
\]
whenever a genuine orbit exists; these algebraic identities alone are not claimed sufficient for realizing a physical orbit.

**Step 3: exact return derivative.** For an energy-preserving transverse flight of the central Hamiltonian between vertical sections, differentiation of \(H_C(x_{\mathrm{in}},y_{\mathrm{in}})=H_C(x_{\mathrm{out}},y_{\mathrm{out}})\) yields
\[
\frac{dy_{\mathrm{out}}}{dy_{\mathrm{in}}}
=\frac{\partial_yH_C(x_{\mathrm{in}},y_{\mathrm{in}})}{\partial_yH_C(x_{\mathrm{out}},y_{\mathrm{out}})}.
\]
For the central legs from \((1,r-t)\) to \((-1,\ell-u)\), and then from \((-1,\ell+u)\) to \((1,r+t)\), respectively, the derivatives are \((A-b_Ct)/(B-b_Cu)\) and \((B+b_Cu)/(A+b_Ct)\). Multiplying these and the two outer reflection derivatives gives \(Q\). The signs of all four normal velocities guarantee that the product is positive. When \(b_C>0\), the indicated order is forward in time and \(\mu=Q\). For \(b_C<0\), the forward flight follows the reverse order, so \(\mu=Q^{-1}\). The factor uses the actual crossing flow, including any switching saltation; it is not a smooth-divergence-only approximation.

**Step 4: nonunit multiplier and stability.** By direct algebra,
\[
Q-1=\frac{2b_C(Au-Bt)}{(B-b_Cu)(A+b_Ct)}.
\]
Because of the opposite central normal directions at the two right/left visits, the denominator is strictly negative. Using \(At=Bu\), we have \(Au-Bt=A(u^2-t^2)/u\) and \(A-B=A(u-t)/u\); these have the same sign since \(t+u>0\). Consequently,
\[
\operatorname{sgn}(Q-1)=\operatorname{sgn}(b_C)\operatorname{sgn}(B-A).
\]
Since \(\mu=Q\) if \(b_C>0\) and \(\mu=Q^{-1}\) if \(b_C<0\), it follows that
\[
\operatorname{sgn}(\mu-1)=\operatorname{sgn}(B-A).
\]
As \(A\ne B\), \(\mu\ne1\). As \(\mu>0\), this is exactly the asserted hyperbolicity and attraction/repulsion classification. \(\square\)

## Verification

A supplementary standard-library program `check_three_zone.py` verifies the algebraic Hamiltonian matching identities using exact rational coefficients in the CCC example of Pessoa–Ribeiro (2022, Example 4.1). It checks four Hamiltonian endpoint equalities in the quadratic field \(\mathbb{Q}(\sqrt{295865})\), the amplitude identity, and transversality inequalities. It computes \(\mu\approx7.163689825174\) for the example; reversing the sign of every vector field reverses time and gives \(\mu\approx0.139592866861\). Running `python3 check_three_zone.py` prints `THREE_ZONE_HAMILTONIAN_RATIONAL_CERTIFICATE_OK`. These exact algebraic tests and numerical multiplier evaluations illustrate, rather than establish by enumeration, the universal analytical theorem. For an independent dynamics check, numerical event integration of the four flight segments gives a finite-difference return derivative agreeing with the predicted multiplier to within approximately \(2\times10^{-6}\) in one test.

## Relationship to prior work

Pessoa and Ribeiro, arXiv:2106.04638 (first posted 2021-06-08), and its 2022 journal version, establish that at most one isolated crossing limit cycle exists for the specified three-zone Hamiltonian family and construct examples in the six center/saddle configurations. Their complete inspected paper does not state the exact return multiplier, the hyperbolicity exclusion or the parameter-only attraction criterion. The 2018 Llibre–Teixeira article establishes an existence/uniqueness statement for only-center subsystems. Carmona, Fernández-Sánchez and Novaes study two-zone sewing systems in arXiv:2207.14634, not this three-zone Hamiltonian setting. The general published theory of saltation and section maps is used as background and is not claimed as new; the claimed new fact is the consequence of the double reflection identity and the signs in (1). A broader 2025 three-zone study by Xiong and Du could not be inspected in full, so possible equivalent coverage remains a priority risk.

## Limitations

The statement concerns *isolated transverse four-crossing* periodic orbits only; it does not classify sliding cycles, grazing cycles, nonlinear perturbations, cycles not visiting all three zones, or existence for arbitrary coefficients. At coefficients producing an entire period annulus, the isolated-cycle hypothesis fails, and no claim of hyperbolicity is made. The full text of Xiong and Du (2025, J. Differential Equations 418, 496–535) was not accessible, so exhaustive publication priority has not been certified. No independent mathematical audit has been performed.

## References

1. C. Pessoa and R. Ribeiro, *Limit cycles of planar piecewise linear Hamiltonian differential systems with two or three zones*, Electronic Journal of Qualitative Theory of Differential Equations (2022), no. 27, 1–19, DOI: 10.14232/ejqtde.2022.1.27. Original preprint: arXiv:2106.04638, first posted 2021-06-08.
2. J. Llibre and M. Teixeira, *Piecewise linear differential systems with only centers can create limit cycles?*, Nonlinear Dynamics 91 (2018), 249–255, DOI: 10.1007/s11071-017-3866-6.
3. V. Carmona, F. Fernández-Sánchez and D. D. Novaes, *Uniqueness and stability of limit cycles in planar piecewise-linear sewing systems* (2022), arXiv:2207.14634.
4. L. Xiong and Z. Du, *The period annulus and limit cycles in a planar piecewise linear system defined in three zones separated by two parallel lines*, Journal of Differential Equations 418 (2025), 496–535, DOI: 10.1016/j.jde.2024.11.045 (abstract/bibliographic information only).
