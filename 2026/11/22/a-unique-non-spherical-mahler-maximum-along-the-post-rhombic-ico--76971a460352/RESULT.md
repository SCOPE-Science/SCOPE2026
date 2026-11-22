# A unique non-spherical Mahler maximum along the post-rhombic icosahedral hull

## Finding

Let \(I\subset\mathbb R^3\) be a regular icosahedron whose vertices lie on the Euclidean unit sphere, and let \(U\) be its twenty outward unit facet normals. For \(\tau>0\), set
\[
K_\tau=\operatorname{conv}(I\cup \tau U),\qquad
\mathcal M(\tau)=\operatorname{vol}_3(K_\tau)\operatorname{vol}_3(K_\tau^\circ).
\]
The bodies are centrally symmetric, so the origin is their Santaló point. Put
\[
h=\sqrt{\frac{5+2\sqrt5}{15}},\qquad
b=1-\frac1{\sqrt5},\qquad
\tau_0=\frac{1-b/2}{h},\qquad
B=\operatorname{vol}_3(I)\operatorname{vol}_3(I^\circ).
\]
**Theorem.** On the entire post-rhombic range \(\tau\ge\tau_0\), the exact volume-product law is
\[
\mathcal M(\tau)=
\begin{cases}
\displaystyle B\,\frac{1-3b s^3}{1-bs},&\tau_0\le\tau\le h^{-1},\quad s=\frac{1-h\tau}{b},\\[3pt]
B,&\tau\ge h^{-1}.
\end{cases}
\]
There is exactly one maximizer in that half-line, namely
\[
\tau_*=\frac{1-bs_*}{h}=1.00954708271666\ldots,
\qquad 1-9s_*^2+6bs_*^3=0,
\quad \frac13<s_*<\frac9{25}.
\]
The displayed cubic has exactly one root in \((0,1/2)\). The volume product is strictly increasing for \(\tau_0\le\tau\le\tau_*\), strictly decreasing for \(\tau_*\le\tau\le h^{-1}\), and constant thereafter. In particular \(\tau_*>1\): the unique maximum-volume configuration with thirty-two vertices on a common unit sphere, \(K_1\), does **not** maximize the affine-invariant volume product even within this one-parameter family. Quantitatively,
\[
\mathcal M(\tau_*)=16.2140188408924\ldots
>\mathcal M(1)=16.2080044346791\ldots.
\]
The inequality is strict by the exact derivative and the strict ordering \(\tau_*>1\); decimals are only for orientation.

## Assumptions and scope

All volumes are ordinary three-dimensional Euclidean volumes. The polar is taken at the origin, \(K^\circ=\{y:\langle x,y\rangle\le1\text{ for all }x\in K\}\). The theorem concerns only the specified complete icosahedral-orbit family and the parameter range \(\tau\ge\tau_0\), which starts at the coplanar-rhombus transition. It is not a global Mahler optimizer among all polyhedra or all thirty-two-vertex polyhedra.

For explicit normalization, let \(\varphi=(1+\sqrt5)/2\) and take the twelve unit vectors obtained by dividing
\[
(0,\pm1,\pm\varphi),\quad(\pm1,\pm\varphi,0),\quad(\pm\varphi,0,\pm1)
\]
by \(\sqrt{1+\varphi^2}\). The twenty outward unit normals to their triangular faces form \(U\); the supporting face planes are \(\langle u,x\rangle=h\). Two adjacent icosahedral vertices have scalar product \(1/\sqrt5\). Write \(A_5=2\sin(2\pi/5)\) for the area of the regular pentagon formed by the five neighboring vertices of one icosahedral vertex. Then
\[
\operatorname{vol}_3(I)=\frac43 A_5,
\quad\operatorname{vol}_3(I^\circ)=\frac{10(1-h^2)}{h^2}\sin\frac{2\pi}5,
\quad B=\frac{80}{3}\,\frac{1-h^2}{h^2}\sin^2\frac{2\pi}5.
\]

## Proof

**Step 1: exact polarity to vertex truncations.** Put \(a=h\tau\) and \(s=(1-a)/b\). By the facet representation of \(I\),
\[
 aK_\tau^\circ
=\{x:\langle u,x\rangle\le h\ (u\in U),\ 
\langle v,x\rangle\le a\ (v\in\operatorname{vert}I)\}
=I\cap\bigcap_{v\in\operatorname{vert}I}\{x:\langle v,x\rangle\le a\}=:T_s.
\]
For \(\tau_0\le\tau\le h^{-1}\), exactly \(0\le s\le1/2\). The plane \(\langle v,x\rangle=1-bs\) cuts each of the five edges emanating from vertex \(v\) at fraction \(s\) from that vertex; its five neighbors have scalar product \(1-b\) with \(v\). All other vertices lie farther inward. Since \(s\le1/2\), the twelve corner caps have pairwise disjoint interiors. Thus \(T_s\) is precisely the equal-edge-fraction vertex truncation of \(I\).

**Step 2: primal truncated volume.** Each original corner cap is a pyramid of height \(b\) above the regular pentagon of area \(A_5\). The cap at fraction \(s\) is its homothetic copy of factor \(s\), with volume \(bA_5s^3/3\). There are twelve. The classical icosahedral face-pyramid formula gives \(\operatorname{vol}_3(I)=\frac{20}{3}hA_\triangle=\frac43 A_5\), where \(A_\triangle=(\sqrt3/2)b\). The last identity follows by substituting the displayed value of \(h\) and the elementary pentagonal sine formula. Therefore
\[
\operatorname{vol}_3(T_s)=\frac43A_5-12\frac{bA_5s^3}{3}
=\operatorname{vol}_3(I)(1-3bs^3).
\]

**Step 3: polar truncated volume.** Since \(I^\circ=\operatorname{conv}\{u/h:u\in U\}\) is a regular dodecahedron circumscribed about the unit ball, its twelve congruent pentagonal facets each have area \(A_D=\operatorname{vol}_3(I^\circ)/4\). Polarity of the intersection above yields
\[
T_s^\circ=\operatorname{conv}\bigl(I^\circ\cup\{v/a:v\in\operatorname{vert}I\}\bigr),\qquad a=1-bs.
\]
For \(0<s\le1/2\), each new point \(v/a\) is beyond exactly the dodecahedral supporting plane \(\langle v,x\rangle=1\), but no other facet plane: the largest distinct-vertex scalar product is \(1-b<a\). Hence \(T_s^\circ\) is the union of \(I^\circ\) and twelve disjoint-outside-interior pyramids on its pentagonal facets. Their common outward height is \(a^{-1}-1\). Consequently
\[
\operatorname{vol}_3(T_s^\circ)=\operatorname{vol}_3(I^\circ)
+\frac{12}{3}A_D(a^{-1}-1)
=\frac{\operatorname{vol}_3(I^\circ)}a.
\]
This also holds at \(s=0\) by continuity. Since \(K_\tau=aT_s^\circ\), invariance of volume product under invertible homotheties proves the stated rational-cubic formula. When \(\tau\ge h^{-1}\), all twelve truncating constraints are redundant and \(K_\tau=\tau\operatorname{conv}(U)\), giving the constant second branch \(B\) by polarity and scaling.

**Step 4: sharp optimization.** Write \(F(s)=(1-3bs^3)/(1-bs)\). Direct differentiation gives
\[
F'(s)=\frac{b(1-9s^2+6bs^3)}{(1-bs)^2}.
\]
The cubic \(q(s)=1-9s^2+6bs^3\) is strictly decreasing on \(0<s\le1/2\), because \(q'(s)=-18s(1-bs)<0\). Moreover \(q(0)=1\) and \(q(1/2)=(-5+3b)/4<0\). Thus there is exactly one root \(s_*\in(0,1/2)\), giving a strict and unique maximum of \(F\). Because \(s\) decreases strictly as \(\tau\) increases, the asserted increase/decrease/plateau follows.

For the nontrivial position relative to the spherical volume maximizer, \(q(1/3)=2b/9>0\), whereas \(q(9/25)<0\): substitute the exact value of \(b\), or use \(b<4/7\). Thus \(1/3<s_*<9/25\). Moreover
\[
\left(1-\frac9{25}b\right)^2-h^2
=\frac{958-386\sqrt5}{9375}>0,
\]
and both square-root comparison sides are positive. Therefore \(h<1-9b/25<1-bs_*\), proving \(\tau_*>1\) without numerical estimates. Equality is impossible away from the unique root and the constant tail is strictly lower because \(F(s_*)>F(0)=1\). This completes the proof.

## Verification

Run `python check.py` with Python 3 and its standard library. It gives exact rational sign and bracket certificates using squared integer bounds for \(\sqrt5\), and displays decimal values of \(s_*\), \(\tau_*\), \(\mathcal M(\tau_*)\) and \(\mathcal M(1)\). The analytic proof above establishes the continuous-in-parameter theorem; a finite numerical test alone would not.

For an independent optional floating-point geometry check, the analysis compared convex-hull and halfspace-intersection volumes at \(\tau=0.95,1,1.009,1.1,1.25,1/h,1.3\) using the twelve explicit vertices and twenty computed face normals. Every comparison agreed with the displayed formula within \(2\times10^{-14}\). These tests are corroborative, not a replacement for the volume and optimizer derivations.

## Relationship to prior work

Hoehner (2026, arXiv:2611.10777v1) proves that the unit-sphere convex hull of the twelve unit icosahedral vertices and twenty unit face normals, namely \(K_1\), has globally maximal **ordinary volume** among inscribed three-polytopes with at most thirty-two vertices; the configuration's volume maximality within its type was known earlier from Wimmer. This result concerns an entirely different affine-invariant objective and proves the optimum occurs at \(\tau_*>1\), where the face-normal vertices are not all on the same sphere as the icosahedral vertices.

An earlier recorded result (opaque identifier `608997a4-e0fb-4c28-9c19-6f53c3e999b4`) establishes exact Mahler-product formulas and strict growth for \(h\le\tau\le1\). It does **not** imply the post-unit maximum, decrease thereafter or the global post-rhombic classification given here; the newly proved regime is \(\tau>1\). The present theorem independently derives its entire displayed formula from truncated-icosahedron and polar-pyramid decompositions.

Barthe and Fradelizi's reflection-symmetry inequality yields a **lower** volume-product bound for bodies with icosahedral symmetry; it does not select the maximizer in this parameter family. Alexander, Fradelizi and Zvavitch study volume-product maximization with vertex-count constraints but do not, in the material accessed, identify this radial parameter. Ordinary truncated-icosahedron volume tables do not give the simultaneous dual volume or the maximizing cubic.

## Limitations

This is an exact statement for one specified icosahedrally symmetric one-parameter family; it neither claims a global Mahler maximum for thirty-two-vertex bodies nor extends the monotonicity of the previously studied pre-unit branch. The gain over \(K_1\), while strictly proved, is numerically small. Full-text comparison with every historical treatment of the truncated icosahedron is not guaranteed: some plausible primary-source sections could not be retrieved during the comparison. Independent mathematical audit has not occurred.

## References

- Steven Hoehner, *On maximum volume polytopes inscribed in the sphere*, arXiv:2611.10777v1 (first public 2026-11-07), especially Theorem on thirty-two vertices and Section 7. https://arxiv.org/abs/2611.10777
- Franck Barthe and Matthieu Fradelizi, *The volume product of convex bodies with many hyperplane symmetries*, American Journal of Mathematics 135 (2013), 311–347. https://perso.math.u-pem.fr/fradelizi.matthieu/pdf/symmetries.pdf
- Matthew Alexander, Matthieu Fradelizi and Artem Zvavitch, *Polytopes of Maximal Volume Product*, arXiv:1708.07914 (2017). https://arxiv.org/abs/1708.07914
- Eric Weisstein, *Pentakis Dodecahedron*, MathWorld, geometric background on the dual truncated-icosahedral combinatorics. https://mathworld.wolfram.com/PentakisDodecahedron.html
