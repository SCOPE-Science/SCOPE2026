# Exact heptagonal rotation and one-cycle integer energy shells in a two-season tropical Lyness map

## Finding

Let
\[
 T_a(x,y)=(y,\max\{a,y\}-x),\qquad
 F=T_1\circ T_0,
\]
where the first update uses threshold zero and the second uses threshold one. Equivalently,
\[
 F(x,y)=(z,\max\{1,z\}-y),\qquad z=\max\{0,y\}-x.
\]
The globally conserved function is
\[
 H(x,y)=\max\{x+1,0\}+\max\{y,1\}
       +\max\{x,y+1,1\}-x-y.
\]
For every real \(h>3\), the entire level \(H=h\) is a convex heptagon. In the counterclockwise orientation, its arclength in primitive lattice directions is \(5h-8\), and the restriction of \(F\) is conjugate, by this arclength coordinate, to the rigid circle rotation
\[
 \boxed{\rho(h)=\frac{3h-5}{5h-8}}.
\]
Consequently every point on \(H=h>3\) is periodic if and only if \(h\) is rational; if \(h\) is irrational, every orbit is dense in that heptagon. If \(h\) is rational, every orbit has least period equal to the denominator of \(\rho(h)\) in lowest terms.

On the **entire integer lattice**, the conclusion is stronger and completely arithmetic: for every integer \(k\ge3\), the \(5k-8\) points with \(H=k\) form **one** orbit, of least period exactly \(5k-8\). Thus every integer initial state is periodic from time zero, and each integer energy has precisely one temporal cycle. For \(k\ge4\), this transitivity follows from
\[
 5(3k-5)-3(5k-8)=-1.
\]
The exceptional flat central level \(H=3\) satisfies the same integer-period formula by a separate seven-point calculation, but is **not** claimed to be a circle of real states.

The heptagon encloses the exact area
\[
 A(h)=\frac{5h^2-16h+8}{2} \quad(h>3).
\]
With area action \(I=A/(2\pi)\), the exterior invariant foliation has strict twist
\[
 \frac{d\rho}{dI}=\frac{2\pi}{(5h-8)^3}>0.
\]

## Assumptions and scope

All maps act on \(\mathbb R^2\), with no positivity restriction on the tropical coordinates. The quantity \(h\) denotes the value of the stated exact first integral, not a time variable. The two-step map \(F\), rather than a single alternating individual step, is the object whose iteration periods are counted. Arclength is measured along each edge using its primitive integer direction: displacement by one primitive direction vector has length one. Counterclockwise turns are positive. The real-circle classification applies **only to \(h>3\)**; the integer statement includes \(k=3\), checked separately.

## Proof

**1. An exact first integral.** For positive real variables \(X,Y,a,b\), introduce the rational Lyness maps
\[
 L_a(X,Y)=\left(Y,\frac{a+Y}{X}\right)
\]
and the rational function
\[
 R_{b,a}(X,Y)=\frac{(bX+a)(aY+b)(aX+bY+ab)}{XY}.
\]
Direct substitution and cancellation give
\[
 R_{b,a}(L_bL_a(X,Y))=R_{b,a}(X,Y).
\]
For \(\varepsilon>0\), substitute \(a=1\), \(b=e^{1/\varepsilon}\), \(X=e^{x/\varepsilon}\), \(Y=e^{y/\varepsilon}\), and apply \(\varepsilon\log\) to the rational two-step dynamics and to \(R_{b,a}\). The identity
\[
 \varepsilon\log\!\left(\sum_{j=1}^m e^{c_j/\varepsilon}\right)
 \longrightarrow\max_j c_j
\]
converges uniformly on every compact set of the exponents. Therefore, taking \(\varepsilon\downarrow0\), the rational two-step map converges to \(F\), while \(\varepsilon\log R_{b,a}\) converges to \(H\). The exact rational invariance passes to the limit, proving \(H\circ F=H\) for every real input. This also follows from direct checking of the finitely many max-linear chambers.

**2. All heptagonal boundaries.** Expanding the maxima and discarding dominated affine terms shows that \(H\) is the maximum of the eight affine expressions
\[
 x+1,\quad y+2,\quad3,\quad x-y+2,\quad3-y,\quad
 -x+y+1,\quad2-x,\quad2-x-y.
\]
In particular \(H\ge3\). For every \(h>3\), intersecting their sublevel half-planes gives a bounded convex polygon whose vertices, in counterclockwise order, are
\[
 \begin{aligned}
 P_0&=(1,3-h),&P_1&=(h-1,1),&P_2&=(h-1,h-2),\\
 P_3&=(-1,h-2),&P_4&=(2-h,1),&P_5&=(2-h,0),\\
 P_6&=(-1,3-h).&&
 \end{aligned}
\]
Successive edges have primitive directions \((1,1)\), \((0,1)\), \((-1,0)\), \((-1,-1)\), \((0,-1)\), \((1,-1)\), \((1,0)\). Their respective positive primitive arclengths are
\[
 h-2,\quad h-3,\quad h,\quad h-3,\quad1,\quad h-3,\quad2.
\]
The total is \(L(h)=5h-8\). Each listed vertex satisfies all the defining inequalities, and consecutive edges exhaust the seven active facets; the constant facet \(3\) is inactive when \(h>3\). Since \(H\ge3\), the level \(H=h>3\) is exactly this polygonal boundary, with no interior component. Its shoelace area is \(A(h)=(5h^2-16h+8)/2\).

**3. Rigid rotation rather than just a rotation number.** Each one-step map \(T_a\) is a continuous plane homeomorphism with inverse
\[
 T_a^{-1}(u,v)=(\max\{a,u\}-v,u).
\]
On each side of its switching line its linear part lies in \(\operatorname{SL}_2(\mathbb Z)\), so it preserves planar orientation and sends every primitive integer tangent vector to another primitive integer vector. The same holds for the composition \(F\) on each of its finitely many affine regions. As \(H\) is invariant, \(F\) restricts to an orientation-preserving homeomorphism of every invariant heptagon. Partitioning an edge at any switching points shows that it also preserves its local primitive arclength; hence it is a positively oriented isometry of the boundary circle of circumference \(L(h)\). Such an isometry must be a rigid translation in that arclength coordinate.

At the first vertex, \(F(P_0)=P_3\). The counterclockwise arclength from \(P_0\) to \(P_3\) is
\[
 \delta(h)=(h-2)+(h-3)+h=3h-5.
\]
Therefore the boundary action is translation by \(\delta(h)\) modulo \(L(h)\). The ratio \(\rho(h)=\delta(h)/L(h)\) lies in \((4/7,3/5)\) and has derivative \(1/(5h-8)^2>0\). Since a fractional-linear map with integer coefficients and nonzero determinant sends rational inputs precisely to rational outputs, \(\rho(h)\) is rational exactly when \(h\) is rational. This proves the real-orbit classification. Differentiating the area formula gives \(dI/dh=(5h-8)/(2\pi)\), yielding the twist formula.

**4. One cycle per integer energy.** For integer \(k\ge4\), the seven vertices have integer coordinates, all seven edge directions are primitive integer vectors, and an integer point satisfies \(H=k\) exactly when it lies on the boundary. Each edge contributes its integer primitive length in integer lattice points, counted with one endpoint excluded; the complete boundary therefore has \(L(k)=5k-8\) points. The rigid translation adds \(\delta(k)=3k-5\) to their integer arclength coordinates modulo \(L(k)\). Their greatest common divisor is one by the displayed Bézout identity, so they comprise one primitive orbit of length \(5k-8\).

For \(k=3\), the integer solutions of \(H=3\) are precisely
\[
 (-1,0),\ (-1,1),\ (0,0),\ (0,1),\ (1,0),\ (1,1),\ (2,1).
\]
They form the explicit single seven-cycle
\[
 (0,0)\mapsto(0,1)\mapsto(1,0)\mapsto(-1,1)
 \mapsto(2,1)\mapsto(-1,0)\mapsto(1,1)\mapsto(0,0).
\]
Every integer point has integer energy \(H\ge3\), completing the classification of all lattice orbits.

## Verification

Run `python verify_tropical_lyness.py` with SymPy installed from the directory containing this document. The checker reproduces the rational invariance and twist identities symbolically; verifies the seven-edge geometry and the arclength shift at 441 rational boundary sample points; independently enumerates the complete integer boundary and direct orbits on every shell from \(k=3\) through \(k=200\); and checks the central seven-cycle. Its expected final line is `VERIFY_OK`; the actual output is in `verification_output.txt`. These finite controls are not used as proofs for real irrational levels or arbitrarily large integer shells: those follow from steps 1–4 above.

## Relationship to prior work

Cima, Gasull and Mañosa (first publicly posted 2009-12-26, arXiv:0912.5031) analyze the positive **rational** two-season Lyness recurrence and its conserved rational curves. Their invariant underlies the tropicalization in step 1, but their elliptic-oval rotation theory does not supply the explicit alternating-threshold heptagon translation, lattice shell count or Bézout transitivity. De Angelis (2004, Sections 2–4) solves the **autonomous**, one-threshold Lyness max map; its circle conjugacies do not apply by direct substitution to the composition with distinct thresholds. Takahashi and Iwao (2007) study an integrable autonomous piecewise-linear QRT map and give a return-rotation construction for that different normalization.

The published result *Exact action-twist and Pareto rotation spectrum of a max-plus QRT map* uses \(G(x,y)=(y,\max\{0,y+1\}-x)\), with exterior octagonal rather than heptagonal levels and a different rotation law \((c-1)/(5c-3)\). It does not imply the two-season map's integer transitivity or the displayed rotation formula. These comparisons concern mathematical implications, not just title or notation similarity.

## Limitations

The theorem fixes thresholds in the order zero then one, with the **two-step** stroboscopic update. It does not classify arbitrary alternating thresholds, perturbations, or the continuous dynamics inside the flat central level \(H=3\). The exact integer classification includes this central level only through its seven integer points. The main priority risk is earlier literature on nonautonomous *max-type* Lyness recurrences, especially Grove, Kent and Ladas's 1998 work on boundedness and persistence, whose full text could not be inspected; accessible bibliographic evidence does not establish that it treats the exact rotation and primitive lattice-shell census. A negative database search is not a proof of uniqueness. No independent scientific audit has been performed.

## References

1. A. Cima, A. Gasull and V. Mañosa, *On two and three periodic Lyness difference equations*, arXiv:0912.5031, first posted 2009-12-26, https://arxiv.org/abs/0912.5031.
2. V. De Angelis, *Dynamics of the Lyness Max Map*, *Journal of Difference Equations and Applications* 10 (2004), 187–200, https://doi.org/10.1080/1023619031000148803. Author-hosted full PDF: https://vdeangel.xula.edu/Publications/Lynnes.pdf.
3. D. Takahashi and M. Iwao, *Geometrical Dynamics of an Integrable Piecewise-Linear Mapping* (2007), https://hakotama.jp/laboratory/works/public/2005-NATO-Science-Series.pdf.
4. *Exact action-twist and Pareto rotation spectrum of a max-plus QRT map*, published mathematical result (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-exact-action-twist-and-pareto-rotation-spectrum-of-a-max-plus-qr--08992945e4c5.
5. E. A. Grove, C. M. Kent and G. Ladas, *Boundedness and Persistence of the Nonautonomous Lyness and Max Equations*, *Journal of Difference Equations and Applications* (1998). Complete text not inspected.
