# First spherical-cap collision and a three-to-six mode transition in triangular-prism random widths

## Finding
For a right equilateral triangular prism \(P_h\) of base circumradius one and height \(h>0\), let \(U\) have the rotation-invariant probability distribution on \(S^2\), and let \(W_h=\max_{x\in P_h}\langle U,x\rangle-\min_{x\in P_h}\langle U,x\rangle\). Define
\[
D=\sqrt{h^2+3},\quad q=\sqrt{\max\{3,h^2+9/4\}},\quad
N=\begin{cases}3,&0<h<\sqrt3/2,\\9,&h=\sqrt3/2,\\6,&h>\sqrt3/2.\end{cases}
\]
Then \(\operatorname{supp}(W_h)\) has right endpoint \(D\) and, exactly on the full terminal interval \(q\le t\le D\),
\[
\Pr(W_h>t)=6\left(1-\frac{t}{D}\right).
\]
The lower endpoint \(q\) of this linear terminal interval is optimal. More precisely, as \(t\uparrow q\) from below,
\[
\Pr(W_h>t)=6\left(1-\frac{t}{D}\right)-
\frac{4\sqrt2 N}{3\pi\sqrt q\sqrt{D^2-q^2}}(q-t)^{3/2}
+o\big((q-t)^{3/2}\big).
\]
The nonzero correction exhibits a sharp change of collision multiplicity from three to six, with nine simultaneous contacts at the critical aspect ratio \(h=\sqrt3/2\). This is a local terminal distribution theorem; no complete lower-width density is claimed.

## Assumptions and scope
The triangular base has vertices \(p_j=(\cos(2\pi j/3),\sin(2\pi j/3))\), for \(j=0,1,2\), and the prism is \(P_h=\operatorname{conv}\{(p_j,\pm h/2):j=0,1,2\}\). All six vertices are distinct because \(h>0\). Rotational probability is normalized surface area \(d\omega/(4\pi)\). The claim holds for every real \(h>0\), including the critical height. The threshold \(q\) is strictly less than \(D\) when \(h>0\).

## Proof
**1. Six diametral axes encode every width.** Let \(d_j=p_j-p_{j+1}\), with indices cyclic modulo three. Each has squared length \(3\), and \(d_i\cdot d_j=-3/2\) for distinct indices. Because every pair of base vertices is adjacent, the planar triangle width is \(\max_j|\langle d_j,u_{xy}\rangle|\). Minkowski additivity of directional width for the Cartesian product with a vertical interval gives
\[
W_h(u)=\max_j|\langle d_j,u_{xy}\rangle|+h|u_z|=
\max_{\substack{j=0,1,2\\s=\pm1}}|\langle(d_j,sh),u\rangle|.
\]
There are exactly six unoriented unit axes \(v_{j,s}=(d_j,sh)/D\). Hence \(W_h=D\max_{j,s}|\langle v_{j,s},U\rangle|\), and the support maximum is \(D\). For \(t\in(0,D)\), the event \(W_h>t\) is a union of twelve spherical caps of height \(t/D\), in six antipodal pairs.

**2. First contact and its multiplicity.** For two axes, the closest relevant signed cap centres have inner product \(|v\cdot v'|\). Directly from the base-edge identities, the 15 distinct axis pairs have inner-product absolute values
\[
\frac{|3-h^2|}{D^2}\quad (3\text{ pairs}),\qquad
\frac{h^2+3/2}{D^2}\quad (6\text{ pairs}),\qquad
\frac{|h^2-3/2|}{D^2}\quad (6\text{ pairs}).
\]
The largest of these is \(m=\max\{3-h^2,h^2+3/2\}/D^2\), since \(|3-h^2|\le\max\{3-h^2,h^2+3/2\}\) and the last class is smaller. Equal-radius caps around two unit centres at angular separation \(\arccos m\) first intersect at cap height \(c_*^2=(1+m)/2\). Therefore the first contact width is \(q=Dc_*=\sqrt{\max\{3,h^2+9/4\}}\). The numbers of touching unoriented axis pairs are respectively \(N=3,9,6\) as stated; the nine-pair graph at equality is bipartite, so it has no triangle. Since each single pair of antipodal caps has probability \(1-t/D\), and all twelve caps are disjoint for \(t\ge q\) up to measure-zero contact, the exact tail is \(6(1-t/D)\) there.

**3. Lens asymptotics and strict optimality of the threshold.** Fix \(h>0\), and let \(t=q-\varepsilon\), where \(\varepsilon>0\) decreases to zero. By compactness and the finite separation gap among non-nearest pairs, only the \(N\) nearest unoriented pairs can overlap. Each of them has two antipodally related cap intersections. At \(h=\sqrt3/2\), their contact graph has no triangle, so even at the critical aspect ratio there are no triple intersections sufficiently close to the first contact. For the two centres at separation \(\alpha=2\arccos(q/D)\), the caps have geodesic radius \(r=\arccos(t/D)\). At the first tangency \(r_0=\alpha/2\), tangent-plane coordinates \((x,y)\) yield the two cap boundary inequalities
\[
\pm x+\frac{\cot r_0}{2}y^2\le r-r_0+O\big((|x|+|y|)^3\big).
\]
The lens area is consequently
\[
L(t)=\frac83\sqrt{2\tan r_0}\,(r-r_0)^{3/2}+o\big((r-r_0)^{3/2}\big)
=\frac{8\sqrt2}{3\sqrt q\sqrt{D^2-q^2}}\,\varepsilon^{3/2}+o(\varepsilon^{3/2}).
\]
There are exactly \(2N\) such lens intersections on the sphere. Inclusion–exclusion with normalized spherical area gives
\[
\Pr(W_h>q-\varepsilon)=6\left(1-\frac{q-\varepsilon}{D}\right)-\frac{2N}{4\pi}L(q-\varepsilon),
\]
for all sufficiently small positive \(\varepsilon\). The stated coefficient follows. It is strictly positive for every \(h>0\), so the terminal linear law fails immediately below \(q\) and its interval is sharp.

## Verification
The standalone standard-library Python program `verify.py` checks the edge-pair Gram identities and three-to-nine-to-six contact counts, evaluates the exact terminal law against deterministic spherical-direction integration, and compares the exact spherical-lens formula with the asserted \(3/2\) coefficient. The analytic argument above, not numerical sampling, proves the universal claim. Numerical comparisons test only selected positive heights.

## Relationship to prior work
Omri Abas, *Random Width and Brightness: Polyhedral Density Theory, Reconstruction, and Gaussian Identifiability* (first public 2026-08-10, arXiv:2609.26202), gives a general spherical co-area framework for arbitrary polytope widths and, in its prism section, the width decomposition into base width and axial contribution. These general tools are prior work. Its explicit special-body treatments concern the tetrahedron, the truncated octahedron, and the rhombic dodecahedron, not this height-dependent collision calculation. Other published first-overlap calculations for regular simplices and type-D root polytopes establish cap-method precedents, but involve different axis configurations. Here the distinct contribution is the *triangular-prism* sharp contact height, aspect-ratio switch of the contact graph, and exact three-case cusp coefficient.

## Limitations
The claim covers only right prisms over a regular triangular base and only the terminal tail and its first collision. It does not determine the complete width distribution below \(q\), does not classify oblique prisms, and has no uniform error bound as \(h\to0\) or \(h\to\infty\). Literature comparison is evidence of noncoverage, not a proof of historical priority. Independent external validation has not been performed.

## References
1. O. Abas, *Random Width and Brightness: Polyhedral Density Theory, Reconstruction, and Gaussian Identifiability*, arXiv:2609.26202 (public 2026-08-10), https://arxiv.org/abs/2609.26202.
2. *Two sharp spherical-cap transitions in regular simplex projection widths*, published 2026, for comparison with general first-cap-overlap methods.
3. *First spherical-cap overlap law for type-D root-polytope widths*, published 2026, for comparison with other regular-polytope instances.
