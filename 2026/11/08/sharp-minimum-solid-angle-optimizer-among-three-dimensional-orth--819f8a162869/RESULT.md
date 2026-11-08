# Sharp minimum-solid-angle optimizer among three-dimensional orthoschemes

## Finding
For a nondegenerate three-dimensional Euclidean orthoscheme, the minimum inward vertex solid angle is at most
\[
\Omega_\star=2\arctan\frac{\sqrt2}{5+3\sqrt3}
=0.2756427992162654\ldots\quad\text{steradians}.
\]
Equality holds exactly for the similarity class of a successive perpendicular-edge path with lengths \(1,\sqrt2,1\). The equality class is unique, including reversal of the path. In contrast, the equal-step path has minimum solid angle \(\pi/12\), which is strictly smaller. This is an exact maximin result for a natural class of tetrahedral mesh elements, not a universal tetrahedron inequality.

## Assumptions and scope
Let \(a,b,c>0\), and define the tetrahedron \(T(a,b,c)\) with ordered vertices
\[
v_0=(0,0,0),\quad v_1=(a,0,0),\quad v_2=(a,b,0),\quad v_3=(a,b,c).
\]
The successive path edges are mutually perpendicular, so every nondegenerate three-dimensional orthoscheme is congruent to such a model after possibly reflecting coordinate axes. A vertex solid angle \(\Omega_i\) is the spherical surface area cut out by the interior tangent cone at \(v_i\), measured in steradians (the whole sphere has area \(4\pi\)). The mesh-quality functional is \(Q(T)=\min_i\Omega_i\). Only positive lengths are permitted; no degenerate tetrahedron is included.

## Proof
Set \(D_a=\sqrt{a^2+b^2}\), \(D_c=\sqrt{c^2+b^2}\), and \(E=\sqrt{a^2+b^2+c^2}\). The elementary trihedral solid-angle formula for three noncoplanar rays \(u,v,w\) pointing into a convex tetrahedron is
\[
\tan\frac\Omega2=
\frac{|\det(u,v,w)|}
{\|u\|\|v\|\|w\|+(u\cdot v)\|w\|+(v\cdot w)\|u\|+(w\cdot u)\|v\|}.
\]
All denominators here are positive. At \(v_0\), the rays \((a,0,0),(a,b,0),(a,b,c)\) have determinant \(abc\), and the denominator factors as \(a(a+D_a)(D_a+E)\). At \(v_3\) reverse the path. Consequently
\[
\begin{aligned}
\tan(\Omega_0/2)&=\frac{bc}{(a+D_a)(D_a+E)},\\
\tan(\Omega_3/2)&=\frac{ba}{(c+D_c)(D_c+E)}.
\end{aligned}
\]
The other two vertex tangent cones are products of a planar wedge with a half-line, hence
\[
\Omega_1=\arctan(c/b),\qquad \Omega_2=\arctan(a/b).
\]
Fix \(b\) and \(a^2+c^2\), so \(E\) is fixed. As \(a\) increases and \(c\) decreases along the positive quarter-circle, \(bc/((a+D_a)(D_a+E))\) decreases strictly: its numerator decreases and both denominator factors increase. The expression with \(a,c\) exchanged increases strictly. At \(a=c\) they coincide, by symmetry. Thus their smaller value is uniquely maximized at \(a=c\). Since the smallest vertex solid angle is no larger than the smaller endpoint angle, we have for each fixed \(b\) and \(a^2+c^2\)
\[
Q(T(a,b,c))\le \min\{\Omega_0,\Omega_3\}\le \Omega_0(s,b,s),\qquad s=\sqrt{(a^2+c^2)/2},
\]
with strict second inequality when \(a\ne c\).

Put \(a=c=s>0\), and let \(t=b/s>0\). The endpoint half-angle tangent becomes
\[
F(t)=\frac{t}{(1+\sqrt{1+t^2})(\sqrt{1+t^2}+\sqrt{2+t^2})}.
\]
Direct differentiation and simplification, using \(\frac d{dt}\log(\sqrt{1+t^2}+\sqrt{2+t^2})=t/(\sqrt{1+t^2}\sqrt{2+t^2})\), yields the **exact** identity
\[
\frac{F'(t)}{F(t)}
=\frac{\sqrt{t^2+2}-t^2}{t\sqrt{t^2+1}\sqrt{t^2+2}}.
\]
The denominator is positive. Its numerator changes sign only at \(t^4=t^2+2\), namely at \(t=\sqrt2\), from positive to negative. Thus \(F\) has a unique global maximum at that point, with
\[
F(\sqrt2)=\frac{\sqrt2}{(1+\sqrt3)(\sqrt3+2)}
=\frac{\sqrt2}{5+3\sqrt3}.
\]
Hence the endpoint minimum never exceeds \(\Omega_\star=2\arctan F(\sqrt2)\), and equality requires \(a=c\), \(b/a=\sqrt2\).

It remains to show the bound is attained for the *smallest of all four angles*, rather than only for the two endpoints. At \(a=c=1,b=\sqrt2\), the middle angles equal \(\arctan(1/\sqrt2)\). Their half-angle tangent is \(1/(\sqrt2+\sqrt3)\), strictly larger than \(F(\sqrt2)=\sqrt2/(5+3\sqrt3)\). Therefore \(\Omega_1=\Omega_2>\Omega_0=\Omega_3=\Omega_\star\), giving attainment and uniqueness. For \(a=b=c=1\), the endpoint half-angle tangent is \((\sqrt2-1)(\sqrt3-\sqrt2)=\tan(\pi/24)\), so \(\Omega_0=\Omega_3=\pi/12<\Omega_\star\).

## Verification
The accompanying `verify.py` uses the determinant-based trihedral formula independently from the factored endpoint formulas and evaluates all four vertex angles. With a deterministic seed it checks \(20{,}000\) independently sampled positive triples spanning several orders of magnitude against the derived bound, then checks the one-parameter derivative identity and the maximum at another \(1{,}000\) parameters. The run finishes with `ORTHOSCHEME_MAXIMIN_OK 21000`. The analytic monotonicity argument and exact derivative sign establish the continuum theorem; finite checks alone would not.

## Relationship to prior work
Licht's October 2026 paper treats the minimum solid angle as a simplex shape measure and gives general comparison inequalities; the proposed result computes the sharp restricted-orthoscheme maximum rather than a comparison exponent. Akopyan and Karasev give a general upper bound for the minimum solid angle of arbitrary tetrahedra, attained by the regular tetrahedron, which is not an orthoscheme. Mesh-bisection literature studies angle quality and similarity types but the inspected accessible primary material did not identify the particular orthoscheme maximin constant. Earlier solid-angle formulas and standard right-tetrahedron properties are classical and not claimed as innovations.

## Limitations
Only three-dimensional nondegenerate Euclidean orthoschemes are classified. The conclusion does not extend without proof to arbitrary tetrahedra, higher-dimensional orthoschemes, or alternative shape measures. The trihedral angle identity is a standard ingredient. Historical priority is provisional: specialist literature on orthoschemes or mesh optimization could contain an equivalent extremum not located by the targeted comparisons. Independent mathematical audit and independent priority verification have not been performed.

## References
- Martin W. Licht, *On solid angles and simplex shape measures*, arXiv:2610.05883v1, first posted 2026-10-05, https://arxiv.org/abs/2610.05883.
- Arseniy Akopyan and Roman Karasev, *Bounding minimal solid angles of polytopes*, arXiv:1505.05263, https://arxiv.org/abs/1505.05263.
- Anwei Liu and Barry Joe, *Quality Local Refinement of Tetrahedral Meshes Based on Bisection*, SIAM Journal on Scientific Computing 16 (1995), https://doi.org/10.1137/0916074.
