# A rhombus-to-octagon transition in the orthogonal kernels of right rectangular pyramids

## Finding

For any \(a,b,h>0\), let the right rectangular pyramid \(P=P_{a,b,h}\subset\mathbb R^3\) have vertices \((\pm a,\pm b,0)\) and \((0,0,h)\). Following the standard all-face definition, its *orthogonal kernel* consists of interior points whose orthogonal projections onto the affine hulls of **every nonempty face** land in the corresponding relative interiors.

Write \(s=h^2\), \(L=\max\{a^2,b^2\}\), \(M=\min\{a^2,b^2\}\), and \(d=L-M\). The kernel is exactly the open set
\[
\begin{split}
\ker_\perp(P)=\{(x,y,z):\;&0<z<h,\\
&(s+b^2)|x|/a+b^2|y|/b<s(1-z/h),\\
&a^2|x|/a+(s+a^2)|y|/b<s(1-z/h)\}.
\end{split}
\]
Its closure is a pyramid with the original apex, and with a four-vertex rhombic base if \(s\le d\), or an eight-vertex base if \(s>d\). Its exact volume fraction is
\[
\boxed{\frac{\operatorname{Vol}_3(\ker_\perp(P))}{\operatorname{Vol}_3(P)}
=\frac{s^2}{2L(s+L)}-
\frac{s(s-d)_+^2}{2L(s+M)(s+L+M)},}\qquad (w)_+=\max\{w,0\}.
\]
If \(a\ne b\), this fraction is continuously differentiable, but not twice differentiable, as a function of \(s\) at \(s=d\); the first additional clipped-area contribution is \(d(s-d)^2/(4L^3)+O((s-d)^3)\).

At fixed base area \(4ab\) and fixed height \(h\), the volume fraction has a **unique maximum** at a square base:
\[
\boxed{\frac{\operatorname{Vol}_3(\ker_\perp(P_{a,b,h}))}{\operatorname{Vol}_3(P_{a,b,h})}
\le\frac{h^4}{(h^2+ab)(h^2+2ab)},}\qquad\text{equality exactly when }a=b.
\]
These statements include all positive sizes and both sides of the transition; no assumption about the pyramid being equifacial or circumscribed is made.

## Assumptions and scope

The Euclidean metric is fixed. The face projection is the ordinary perpendicular foot on \(\operatorname{aff}G\), and relative interior includes the strict inequalities on every face of dimension one or two; on a singleton vertex, projection automatically lands at that vertex. The kernel is open; face and apex boundary points in the displayed closure do not belong to it. Its volume equals the volume of its closure. The parameter \(s\) is the squared apex height, not height itself. The polygonal-face transition refers to the closure's base at \(z=0\).

## Proof

**Step 1: triangular facets.** For a point \(B=(x,y,z)\) in the interior of \(P\), set \(\tau=1-z/h>0\) and normalized coordinates \(u=|x|/a\), \(v=|y|/b\). The facets through the \(x\)-sides lie in planes \(\pm hx+az=ah\). Orthogonal projection of \(B\) onto such a plane has height \(z'\) satisfying
\[
1-z'/h=\frac{h^2\tau\pm ax}{h^2+a^2}.
\]
Because the projected \(y\)-coordinate equals \(y\), its foot lies in the relative interior of the corresponding triangular facet precisely when \((s+a^2)v\mp ax<s\tau\), for each sign. Requiring both signs gives \(a^2u+(s+a^2)v<s\tau\). Analogously, projection to the two facets through \(y=\pm b\) gives \((s+b^2)u+b^2v<s\tau\).

**Step 2: the other faces are automatic.** These two strict inequalities imply \(u<\tau\) and \(v<\tau\), so \(B\) is inside the original pyramid and projects into the base rectangle and all four of its edges. For the edge from a corner \((\epsilon a,\eta b,0)\) to the apex, direct projection gives edge parameter
\[
t_{\epsilon,\eta}=\frac{a^2+b^2-\epsilon ax-\eta by+hz}{s+a^2+b^2}.
\]
Its lower bound \(t_{\epsilon,\eta}>0\) follows from \(u<\tau\), \(v<\tau\), \(z>0\). Its upper bound follows from \(s\tau>a|x|+b|y|\), which follows from the first facet inequality if \(a^2\le s+b^2\), or from the second if \(b^2\le s+a^2\). At least one of these alternatives always holds. Thus every apex-edge foot is interior. Projections onto vertices are automatic. This proves both necessity and sufficiency of the two displayed inequalities, without relying on a generic-position assumption.

**Step 3: shape and volume.** At height \(z\), the admissible horizontal section is \(\tau\) times a fixed centrally symmetric polygon. Its normalized first quadrant has inequalities
\[
(s+b^2)u+b^2v<s,\qquad a^2u+(s+a^2)v<s,\qquad u,v\ge0.
\]
Consequently the closure has the original apex, and the fraction of the volume retained equals the fraction of the basal rectangular area retained, namely the first-quadrant \((u,v)\)-area.

By symmetry suppose \(a^2=L\ge M=b^2\). If \(s\le d=L-M\), the second line dominates: the quadrant is a triangle with axis intercepts \(s/L\) and \(s/(s+L)\), of area \(s^2/[2L(s+L)]\). If \(s>d\), the two lines meet in the first quadrant at
\[
(u_*,v_*)=\left(\frac{s+d}{s+L+M},\frac{s-d}{s+L+M}\right).
\]
The active axis intercepts are \(s/(s+M)\) and \(s/(s+L)\), and the quadrant is a four-vertex polygon of area
\[
\frac{s}{2(s+L+M)}\left(\frac{s-d}{s+M}+\frac{s+d}{s+L}\right).
\]
Algebraic subtraction from the triangular expression yields exactly the positive-part volume formula in the finding. The first regime produces four axis vertices in the full centrally symmetric base, and the second additionally produces four off-axis vertices. For \(a\ne b\), its volume correction first appears as \(d(s-d)^2/(4L^3)+O((s-d)^3)\), giving the claimed \(C^1\) but non-\(C^2\) transition.

**Step 4: fixed-area optimization.** Put \(p=ab>0\), \(r=s/p>0\), and \(q=L/p\ge1\). Since \(M/p=q^{-1}\), let \(t=q+q^{-1}\ge2\), with equality only for the square. In the rhombic regime \(r\le q-q^{-1}\), the fraction becomes \(r^2/[2q(r+q)]\), strictly decreasing in \(q\). In the octagonal regime the fraction is
\[
F(r,t)=\frac{r(2r^2+rt+4-t^2)}{2(r+t)(r^2+rt+1)}.
\]
A direct quotient differentiation gives
\[
\frac{\partial F}{\partial t}=-\frac{r\bigl(3t^2r^2+t^2+6tr^3+10tr+3r^4+9r^2+4\bigr)}{2(r+t)^2(r^2+rt+1)^2}<0.
\]
The regimes agree continuously at the change of active facet, and \(t\) increases strictly with \(q\) for \(q>1\). Hence the unique maximizing \(q\) is one. Substituting \(a=b=\sqrt p\) gives \(r^2/[(r+1)(r+2)]\), equal to the displayed square-base bound.

## Verification

The accompanying `VERIFY.py` requires only Python 3. It compares the two strict inequalities with **independently computed orthogonal feet onto all triangular facets and apex-to-corner edges** at 3,840 exact rational sample points across twelve rational parameter triples. It independently clips the first quadrant by its two linear halfplanes and evaluates exact shoelace areas, matching the stated volume fraction in all twelve cases; it also compares sixteen fixed-area deformations with their square baselines. A direct symbolic differentiation of the rational octagonal expression reproduces the strictly negative derivative shown above. These finite checks are diagnostics: the all-positive-parameter claims and phase transition rest on the preceding exact argument.

To reproduce from a folder containing this file and `VERIFY.py`, run `python3 VERIFY.py` and expect a line beginning `PASS:`.

## Relationship to prior work

Pavlík's *Thales's theorem in higher dimensions* (arXiv:2611.14277, Section 6) defines the all-face orthogonal kernel and characterizes orthogonally bipolar cutout tilings in dimension three using membership of that kernel. His companion *Face lattices of polytopes and bipolar polytopes* (arXiv:2611.13896) develops geometric and combinatorial cutout constructions. The formula, rectangular-pyramid phase transition, exact volume fraction and fixed-base-area extremum above are not supplied by those statements: the general criterion concerns admissibility, whereas the present theorem solves the explicit system for every right rectangular pyramid. Other known calculations of all-face kernels for cross-polytopes and parallelotopes concern different, not projectively equivalent face configurations and do not imply this result. This is a best-knowledge comparison, not a guarantee that equivalent older literature does not exist.

## Limitations

The result applies to centered-apex *right rectangular* pyramids, not arbitrary oblique pyramids, arbitrary quadrilateral bases, or arbitrary polytopes. The sharp square inequality compares kernel **fractions** at fixed rectangular base area and height; it is not a statement about other optimization criteria. The phase transition is at \(h^2=|a^2-b^2|\) and is only interior to the positive-height parameter domain if the base is nonsquare. No independent expert audit or global historical-priority certification is claimed.

## References

1. Jan Pavlík, *Thales's theorem in higher dimensions*, arXiv:2611.14277, initial public submission 10 November 2026, especially Definition 6.1 and Theorem 6.6. https://arxiv.org/html/2611.14277v2
2. Jan Pavlík, *Face lattices of polytopes and bipolar polytopes*, arXiv:2611.13896, initial public submission 10 November 2026, especially geometric cutout definitions and constructions. https://arxiv.org/abs/2611.13896
