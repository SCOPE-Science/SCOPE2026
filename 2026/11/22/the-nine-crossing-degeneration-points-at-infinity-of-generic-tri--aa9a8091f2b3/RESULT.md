# The nine crossing-degeneration points at infinity of generic triangle Lissajous sextics

## Finding
Fix \(c\in\mathbb C\setminus\{0,1,-1\}\). Let \(S_c\) be the closure in affine three-space of the image of the torus \(abd=\lambda\), with \(\lambda+\lambda^{-1}=2c\), under the coordinatewise half-trace map. Let \(X_c\subset\mathbb P^3\) be the **ordinary degree-six homogenization** of this integral affine surface. In coordinates \([X:Y:Z:W]\), the infinity hyperplane is \(W=0\).

The scheme-theoretic infinity section of \(X_c\) is
\[
X_c\cap\{W=0\}=2\{X=W=0\}+2\{Y=W=0\}+2\{Z=W=0\}
\]
as an effective Cartier divisor. Its support consists of three projective lines; every point of them is singular on \(X_c\).

The only points of the infinity section at which the analytic transverse type is not an **ordinary double crossing** are the following **nine distinct points**:
\[
[1:0:0:0],\quad[0:1:0:0],\quad[0:0:1:0],
\]
and
\[
[0:1:\pm1:0],\quad[1:0:\pm1:0],\quad[1:\pm1:0:0].
\]
At each of the nine the local complex-analytic hypersurface germ is equivalent to
\[
\{U^2-V^2T^2=0\}\subset(\mathbb C^3,0).
\]
This consists of two smooth surface branches whose intersection is two transverse smooth curves \(\{U=V=0\}\cup\{U=T=0\}\). Thus the nine are *intersections of double curves*, not Whitney pinch points. Everywhere else on the infinity lines the local germ consists of two smooth transverse analytic surface branches meeting along one line.

## Assumptions and scope
The base field is \(\mathbb C\), and \(c\ne0,\pm1\). The statement concerns the ordinary projective closure in \(\mathbb P^3\), not a toric compactification, a resolution, or the affine singularity classification. Local equivalence means analytic (hence completed formal) equivalence after multiplying the equation by a unit. No assertion is made about the global projective normalization or singularities away from infinity.

## Proof
Set \(x=X/W\), \(y=Y/W\), and \(z=Z/W\) in the affine chart. Elimination of the three half-trace equations and the product relation gives the following sextic, normalized by requiring coefficient \(4\) on \(x^2y^2z^2\):
\[
\begin{aligned}
F_c={}&c^4-4c^3xyz+4c^2(x^2y^2+x^2z^2+y^2z^2)\\
&-2c^2(x^2+y^2+z^2)-4cxyz(x^2+y^2+z^2)\\
&+8cxyz+x^4+y^4+z^4\\
&-2(x^2y^2+x^2z^2+y^2z^2)+4x^2y^2z^2.
\end{aligned}
\]
One can obtain this polynomial without elimination software: write \(x=\cos A\), \(y=\cos B\), \(z=\cos C\); then multiply the four factors corresponding to the four possible values of \(\cos(\pm A\pm B\pm C)\) up to simultaneous sign reversal. Explicitly, put \(p=xyz\), \(q_1=x\sin B\sin C\), \(q_2=y\sin A\sin C\), \(q_3=z\sin A\sin B\), multiply the four signed linear factors, and substitute \(\sin^2 A=1-x^2\), etc. This yields exactly \(F_c\). Its degree-six part is \(4x^2y^2z^2\). Thus the homogenization \(\Phi_c(X,Y,Z,W)\) satisfies \(\Phi_c(X,Y,Z,0)=4X^2Y^2Z^2\). The infinity section is the stated doubled triangle. Since the first normal derivatives in all four projective coordinates vanish there, every point of its support is singular.

At a point of the line \(X=W=0\) with \(Y,Z\ne0\), take the chart \(Y=1\), set \(t=Z\), \(u=X\), and \(w=W\). The quadratic normal form of \(\Phi_c\) in \((u,w)\), parametrized by \(t\), is
\[
Q_t=4t^2u^2-4ct(1+t^2)uw+
\big((1-t^2)^2+4c^2t^2\big)w^2.
\]
Its discriminant is precisely
\[
16t^2(c^2-1)(1-t^2)^2.
\]
Because \(c^2\ne1\), it is nonzero for \(t\notin\{0,1,-1\}\). At every such point the two normal directions split into two distinct complex lines. The analytic Weierstrass splitting/implicit-function theorem therefore factors the local equation into two smooth transverse branches. Cyclic permutation gives the same assertion on each of the three lines.

Next take the point \([0:1:1:0]\); other sign choices and permutations are equivalent by the same coordinate calculation. In the chart \(Y=1\) set \(Z=1+t\), \(X=cw+u\), \(W=w\). Direct expansion of the degree-six homogenization has quadratic part \(4u^2\), and its degree-four term after removing the nondegenerate \(u\)-direction by the holomorphic splitting lemma has leading part
\[
4(1-c^2)t^2w^2.
\]
The local singular locus contains both lines \(u=w=0\) (at infinity) and \(u=t=0\) (the closure of the affine singular line \(X=cW,\ Y=Z\)). Apply the holomorphic splitting lemma to obtain \(\Phi_c=\text{unit}\cdot(U^2+h(t,w))\). In the resulting coordinates those two curves remain critical and mapped to \(U=0\); hence \(h\) and its derivatives vanish identically on both coordinate axes, giving \(h\in(t^2)\cap(w^2)=(t^2w^2)\). The calculated nonzero degree-four coefficient implies \(h=t^2w^2\cdot\text{unit}\). An analytic square-root change of one coordinate gives \(U^2-V^2T^2=0\). At \([0:1:-1:0]\), replace \(Z\) by \(-Z\) and \(X\) by \(-X\) in the corresponding sign convention; all calculations are identical. Symmetry covers the six nonvertex points.

Finally, at \([1:0:0:0]\) use \(X=1\), with local coordinates \((y,z,w)=(Y,Z,W)\). The lowest weighted terms of the local equation, giving weight one to \(y,z\) and weight two to \(w\), are
\[
w^2-4cyzw+4y^2z^2.
\]
The quadratic term \(w^2\) permits analytic splitting in \(w\). Since the local singular locus contains the axes \(y=w=0\) and \(z=w=0\), the reduced residual function in \((y,z)\) is divisible by \(y^2z^2\). Completing the square in the displayed weighted-leading form shows its initial coefficient is \(4(1-c^2)\ne0\). Thus the germ is again \(U^2-V^2T^2=0\). By symmetry this applies to the other two vertices.

The quadratic discriminant test covers all remaining points of all three lines, so the nine identified points exhaust the exceptional types at infinity.

## Verification
The standalone checker `verify.py` reconstructs the sextic, computes its homogeneous pieces, confirms the discriminant of the transverse quadratic, verifies all six affine singular lines symbolically, and computes the critical degree-four residual at a nonvertex crossing point. The two vertex identities follow by cyclic permutations and the local weighted expansion. The analytical splitting lemma and divisibility argument, not finite sample tests, prove the all-complex-parameter assertion. Execute `python verify.py` with SymPy.

## Relationship to prior work
Mascarin–Telen (2025/2026) introduced the Lissajous varieties; Mascarin (2026, arXiv:2611.15725, first public 2026-11-11) analyzes their **affine** equations and singular sets, and prints the zero-phase triangle sextic. The previously studied generic-phase affine sextic has six affine double lines and a separate finite singularity stratification; that does not determine the singularities arising from ordinary degree-six projective homogenization. The present statement supplies precisely this missing infinity divisor and its nine exceptional analytic crossings. It is not a rephrasing of the affine singularity census: none of the three infinity lines lies in the affine chart. Searches for equivalent projective-boundary descriptions were inconclusive rather than exhaustive; the earlier Mascarin–Telen full text could not be inspected in this round, though its abstract and its treatment as an affine variety were examined.

## Limitations
The restriction \(c\ne0,\pm1\) is essential to the quadratic discriminant and residual-unit arguments. In particular, at \(c=0\) the line-crossing strata change; no claim is made there. The asserted local germs are complex analytic; they need not split over an arbitrary smaller field. This analysis does not compute the global normalization, conductor, or projective Chern numbers. Independent mathematical review has not been performed.

## References
1. F. M. Mascarin, *Intersections, Equations, and Singularities of Lissajous Varieties*, arXiv:2611.15725v1 (2026-11-11), https://arxiv.org/html/2611.15725v1, especially §§1, 3–5.
2. F. M. Mascarin and S. Telen, *Lissajous Varieties*, arXiv:2509.06844 (2025-09-08), https://arxiv.org/abs/2509.06844.
3. M. Laurent, F. M. Mascarin and S. Telen, *The Algebraic Boundary of Graph Elliptopes*, arXiv:2605.02484 (2026-05-04), https://arxiv.org/abs/2605.02484.
