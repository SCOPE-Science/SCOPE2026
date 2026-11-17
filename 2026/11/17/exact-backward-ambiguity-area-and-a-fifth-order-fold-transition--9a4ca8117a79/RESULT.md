# Exact backward-ambiguity area and a fifth-order fold transition in a plankton map

## Finding

Consider the discrete phytoplankton–zooplankton map
\[
F_{r,\gamma}(x,y)=\bigl(x(2-x-y),\ y(1-r+\gamma x)\bigr)
\]
on the biologically nonnegative triangle
\[
\mathcal M=\{(x,y):0\le x\le1,\ 0\le y\le2-x\}.
\]
Fix \(0<r<1\) and \(\gamma>0\), and write \(A=1-r\). Let \(\mathcal B_{A,\gamma}\) be the set of target states \((u,v)\) with \(0<u<1\) and \(v>0\) that have **two distinct predecessors in the strict interior** of \(\mathcal M\). Then every such target has at most two predecessors in \(\mathcal M\), \(\mathcal B_{A,\gamma}\) is nonempty and open, and its exact planar Lebesgue area is
\[
\boxed{\operatorname{area}(\mathcal B_{A,\gamma})=
\begin{cases}
\dfrac{5A^2-5A\gamma+2\gamma^2}{30A},&0<\gamma\le A/2,\\[5pt]
\dfrac{A^2(A^2-10A\gamma+40\gamma^2)}{480\gamma^3},&\gamma\ge A/2.
\end{cases}}
\]
The formulas agree at the transition, giving area \(A/10\). For fixed \(A>0\), this area as a function of \(\gamma\) is \(C^4\) but not \(C^5\) across \(\gamma=A/2\): its fifth one-sided derivatives differ by \(64/A^4\). This is caused by a fold entering the interior of the source triangle from a different boundary stratum, **not** by a forward equilibrium bifurcation.

More precisely, for each \(0<u<1\) put \(s(u)=1-\sqrt{1-u}\) and
\[
h_u(x)=(2-x-u/x)(A+\gamma x),\qquad s(u)\le x\le1.
\]
There is a unique \(x_*(u)\in(s(u),1)\) maximizing \(h_u\). Set \(v_*(u)=h_u(x_*(u))\) and \(v_0(u)=(1-u)(A+\gamma)\). The exact ambiguity region is
\[
\boxed{\mathcal B_{A,\gamma}=\{(u,v):0<u<1,\ v_0(u)<v<v_*(u)\}.}
\]
For \(0<v<v_0(u)\), exactly one predecessor lies in the strict interior. At \(v=v_0(u)\), one predecessor is interior and the other lies on the edge \(x=1\); at \(v=v_*(u)\), one interior fold predecessor remains; at \(v>v_*(u)\) there is none. The full image has area \((A+\gamma)/2+\operatorname{area}(\mathcal B_{A,\gamma})\), so at the transition exactly \(2/17\) of its area has two strictly interior predecessors.

This entire fold phenomenon occurs inside the forward-invariant regime in which all strict-interior initial states converge to the prey-only equilibrium for \(0<\gamma<r<1\) whenever that regime meets \(\gamma=A/2\), equivalently \(r>1/3\). For example, \(r=1/2\), \(\gamma=1/3\) give two different interior states
\[
(1/2,1),\qquad (\sqrt3/2,\ 2-2\sqrt3/3)
\]
with the same image \((1/4,2/3)\); the ambiguity-area is exactly \(109/2560\).

## Assumptions and scope

All target multiplicities above count only antecedents in \(\mathcal M\) and concern \(0<u<1\), \(v>0\). The zero-prey target edge \(u=0\) is excluded from the fiber census because boundary degeneracies require separate treatment. The area concerns **target-space Lebesgue measure**, not the measure of the subset of source initial states. No assumption that \(F_{r,\gamma}(\mathcal M)\subseteq\mathcal M\) is needed for the area formula. In the biological parameter subregion \(0<\gamma\le r<1\), the triangle is forward invariant, as shown below. Throughout, area and derivatives are taken with \(r\), hence \(A\), held fixed.

## Proof

**1. Exact biological fibers.** Fix \(0<u<1\). From \(u=x(2-x-y)\), any predecessor in \(\mathcal M\) has \(x>0\), \(y=2-x-u/x\), and \(y\ge0\) precisely when \(u\le x(2-x)\). On \(0<x\le1\), this gives exactly \(s(u)\le x\le1\). The second coordinate of the image is consequently \(v=h_u(x)\). Direct differentiation gives
\[
h_u'(x)=2\gamma-A-2\gamma x+\frac{Au}{x^2},\qquad
h_u''(x)=-2\gamma-\frac{2Au}{x^3}<0.
\]
At the endpoints,
\[
h_u'(s(u))=2(1-s(u))\left(\gamma+\frac A{s(u)}\right)>0,
\qquad h_u'(1)=A(u-1)<0.
\]
The unique maximum occurs in the open interval, and strict monotonicity on each side gives the stated zero-, one-, and two-predecessor classification. In particular \(h_u(s(u))=0\), \(h_u(1)=v_0(u)\), and \(v_*(u)>v_0(u)>0\). Thus the open double-fiber region is exactly the set asserted.

**2. The critical curve and its boundary transition.** The Jacobian determinant is
\[
\det DF_{r,\gamma}(x,y)=2(1-x)(A+\gamma x)-Ay.
\]
On the fiber \(u=\mathrm{constant}\), its value is \(x h_u'(x)\), so every fiber maximum is a nondegenerate fold because \(h_u''(x_*(u))<0\) and the first-coordinate derivative with respect to \(y\) is \(-x\ne0\). The critical arc can be parametrized by its prey coordinate \(t\):
\[
y_c(t)=\frac{2(1-t)(A+\gamma t)}A,
\quad
u_c(t)=t^2\left(1-\frac{2\gamma}{A}+\frac{2\gamma t}{A}\right),
\quad
v_c(t)=\frac{2(1-t)(A+\gamma t)^2}{A}.
\]
The source restriction \(0\le y_c(t)\le2-t\) holds exactly when
\[
t_0\le t\le1,\qquad
 t_0=\max\left\{0,1-\frac A{2\gamma}\right\}.
\]
The derivative \(u_c'(t)=t[2(1-2\gamma/A)+6\gamma t/A]\) is positive for \(t>t_0\), and \(u_c(t_0)=0\), \(u_c(1)=1\). Thus \(t\mapsto u_c(t)\) parametrizes all interior folds exactly once. The lower end of the critical arc sits at \((0,2)\) when \(\gamma\le A/2\); above that parameter it moves onto the oblique source edge at \((t_0,2-t_0)\). Both cases have the same endpoint in target prey coordinate \(u=0\), but different fold geometry.

**3. Area without implicit roots.** The double-covered output area is the vertical integral
\[
\operatorname{area}(\mathcal B_{A,\gamma})=
\int_0^1[v_*(u)-v_0(u)]\,du.
\]
Substitute \(u=u_c(t)\), \(v_*(u)=v_c(t)\). Elementary polynomial algebra gives
\[
\bigl[v_c(t)-(1-u_c(t))(A+\gamma)\bigr]u_c'(t)
=\frac{2t(t-1)^2(A+2\gamma t-\gamma)(A+3\gamma t-2\gamma)}A.
\]
Integrating from \(t_0\) to \(1\) produces, when \(\gamma\le A/2\) and \(t_0=0\),
\[
\frac{5A^2-5A\gamma+2\gamma^2}{30A}.
\]
When \(\gamma\ge A/2\) and \(t_0=1-A/(2\gamma)\), it produces
\[
\frac{A^2(A^2-10A\gamma+40\gamma^2)}{480\gamma^3}.
\]
Their algebraic difference (first expression minus second, interpreted as analytic expressions) is exactly
\[
\frac{(2\gamma-A)^5}{480A\gamma^3}.
\]
Consequently all derivatives through order four match at \(\gamma=A/2\), but the fifth derivatives are respectively \(0\) and \(-64/A^4\). The image over \(0<u<1\) is exactly \(0\le v\le v_*(u)\), so the total image area is \(\int_0^1v_*(u)\,du\). Subtracting the ambiguity area leaves \(\int_0^1 v_0(u)\,du=(A+\gamma)/2\). At \(\gamma=A/2\) the double-fiber proportion is \((A/10)/(3A/4+A/10)=2/17\).

**4. Ecological invariance and a rational/algebraic witness.** When \(0<\gamma\le r<1\), both map components are nonnegative on \(\mathcal M\), and \(u\le x(2-x)\le1\). Moreover
\[
u+v=x(2-x)+y[A+(\gamma-1)x].
\]
If the coefficient of \(y\) is nonpositive, this is at most \(x(2-x)\le1\). If positive, it is at most \((2-x)(A+\gamma x)\le2\), because \(A+\gamma x\le1-r+rx\le1\). Hence \(F_{r,\gamma}(\mathcal M)\subseteq\mathcal M\). The displayed two states at \(r=1/2,\gamma=1/3\) each lie in the strict interior and direct substitution yields the identical target \((1/4,2/3)\). The area formula evaluates to \(109/2560\), proving ambiguity despite forward invariance. The original paper establishes convergence to the prey-only equilibrium for strict-interior initial states in the stricter regime \(0<\gamma<r\); that forward property is not used to derive the backward formulas.

## Verification

Run `python check.py` with Python 3 and SymPy. The standalone checker symbolically reconstructs the Jacobian, fiber derivatives, fold parametrization, both exact integrals, the fifth-derivative discontinuity, the universal critical ratio, and both algebraic predecessors. It also verifies the exact area values \(83/1500\) at \((A,\gamma)=(1/2,1/5)\) and \(109/2560\) at \((A,\gamma)=(1/2,1/3)\). These are finite symbolic checks of identities; the universal fiber-count and area assertions follow from the analytical concavity and change-of-variables proof above.

## Relationship to prior work

The motivating linear-response plankton paper [1], first public on May 15, 2025, gives this discrete model, an invariant biological triangle, fixed-point stability and Neimark–Sacker bifurcation. Its inspected full text does not formulate a backward-fiber census, fold-region area, or fifth-order area transition. The 2019 study [2] gives an exact two-preimage region for the **different** map \((x,y)\mapsto(\mu x(1-x-y),\beta xy)\), on a different source simplex. In particular the predator equation in [2] collapses the full edge \(x=0\) immediately, unlike the contraction \(y\mapsto Ay\) on that edge when \(0<r<1\). Its linear image-fiber formula does not imply the present positive-mortality area law. The established general theory of critical curves and noninvertible planar maps [3] motivates fold counting, but supplies neither the exact formulas nor the parameter-space differentiability transition for this map. A later plankton paper [4] concerns different Holling functional responses and does not supply an implication for the linear-response fibers.

## Limitations

The result classifies one-step inverse ambiguity in the specified triangle, not all real-plane inverse images, and does not classify multiple-step inverse trees or attraction basins. The area is a target-space geometric invariant, not a probability of recovery without a specified target distribution. For \(\gamma>r\), the source triangle need not be forward invariant, although its one-step image geometry remains correct. The boundary target \(u=0\) is not included in the two-fiber assertion. Historical-priority comparisons cannot prove absolute novelty; independent verification remains to be undertaken.

## References

[1] S. K. Shoyimardonov, *Stability and Bifurcation Analysis of a Phytoplankton-Zooplankton Model with Linear Functional Responses*, arXiv:2505.09968v1 (first posted 2025-05-15), https://arxiv.org/html/2505.09968v1 .

[2] B. Vidiella, J. T. Lázaro, L. Alsedà and J. Sardanyés, *On Dynamics and Invariant Sets in Predator-Prey Maps*, IntechOpen (2019), DOI:10.5772/intechopen.89572, https://www.intechopen.com/chapters/70218 .

[3] J. P. England, B. Krauskopf and H. M. Osinga, *Bifurcations of Stable Sets in Noninvertible Planar Maps*, International Journal of Bifurcation and Chaos 15 (2005), 891–904, DOI:10.1142/S0218127405012466 .

[4] S. K. Shoyimardonov, *Discrete Dynamics of a Phytoplankton-Zooplankton Model with Toxin-Mediated Interactions*, arXiv:2508.07942v1 (2025), https://arxiv.org/abs/2508.07942 .
