# Exact ternary central-section law and a unique pentagon-optimal aspect ratio for triangular prisms

## Finding

Let \(H>0\) and let \(T_H\subset\mathbb R^3\) be the right prism whose two bases are equilateral triangles of side length \(1\), centered above one another at heights \(\pm H/2\), with their common horizontal circumradius \(R=1/\sqrt3\). Choose an unoriented plane through the prism center with the rotationally invariant (Haar) distribution on the space of such planes. Almost surely its intersection with \(T_H\) is a polygon with exactly three, four, or five vertices. Write \(p_j(H)\) for the probability of exactly \(j\) vertices and put
\[
q(H)=\frac{2}{\sqrt{4+3H^2}},\qquad
A=\arcsin\!\left(\frac q2\right),\quad
B=\arcsin\!\left(\frac{\sqrt3q}{2}\right),\quad
C=\arcsin(q).
\]
Then the complete probability law is
\[
\boxed{p_3(H)=1-\frac6\pi A,\quad
p_4(H)=\frac6\pi(2A+C-2B),\quad
p_5(H)=\frac6\pi(2B-A-C).}
\]
All three probabilities lie strictly between zero and one for every \(H>0\). In particular, the equilateral-sided-and-height prism \(H=1\) has \(p_5(1)=0.3490843216265\ldots\).

There is a **unique** prism height maximizing the probability of a pentagonal central section. To specify it exactly, let \(q_*\in(0,1)\) be the unique root of
\[
\frac{\sqrt3}{\sqrt{1-3q^2/4}}-\frac1{2\sqrt{1-q^2/4}}-\frac1{\sqrt{1-q^2}}=0.
\]
Then
\[
\boxed{H_*=\frac2{\sqrt3}\sqrt{q_*^{-2}-1}=0.613688176745\ldots,\qquad
p_5(H_*)=0.385155805674\ldots.}
\]
The maximum is strict; the pentagon probability tends to zero at both the vanishing-height and infinite-height limits.

## Assumptions and scope

The prism is nondegenerate, right, and has equilateral bases; changing overall scale does not change its section-type probabilities. The plane must pass through the centroid and has *uniform orientation*, not a randomly translated intercept. The orientation is represented by a uniform unit normal \(U\in S^2\) with \(U\) and \(-U\) identified. Degenerate planes passing through a vertex have probability zero. The count means actual vertices of the planar convex section, not vertices of a projected silhouette.

## Proof

**1. Reducing to two scalar parameters.** Place the base vertices at
\[
a_i=R(\cos(2\pi i/3),\sin(2\pi i/3)),\quad i=0,1,2,
\]
so the six prism vertices are \((a_i,\pm H/2)\). Express the normal as
\[
U=(\sqrt{1-t^2}\cos\phi,\sqrt{1-t^2}\sin\phi,\sigma t),
\]
where \(0<t<1\), \(\sigma\in\{-1,1\}\), and \(\phi\in[0,2\pi)\). For a uniform normal, \(t=|U_3|\) is uniform on \([0,1]\) and independent of uniform \(\phi\). Replacing \(U\) by \(-U\) does not change the section, so we may take \(\sigma=1\). Set
\[
z_i=R\sqrt{1-t^2}\cos(\phi-2\pi i/3),\qquad c=Ht/2.
\]
The signs of the scalar products of \(U\) with the six vertices are precisely the signs of \(z_i+c\) and \(z_i-c\).

**2. Which polygon appears.** Since \(z_0+z_1+z_2=0\), for almost every azimuth one of the three \(z_i\) has the sign opposite to the other two. Their absolute values, written in increasing order, are \(b<a<a+b\). The section vertices are in one-to-one correspondence with the prism edges whose endpoints have different signs (the plane is transversal to all edges and vertices almost surely). Counting the three horizontal edges in each base and the three vertical edges gives the following exhaustive four regimes:
\[
\begin{array}{c|cccc}
\text{range of }c&0<c<b&b<c<a&a<c<a+b&c>a+b\\\hline
\text{number of section vertices}&4&5&4&3.
\end{array}
\]
In particular, a central hexagon cannot occur. Each listed regime has positive spherical measure for \(H>0\).

**3. Integrating the exact probabilities.** By the dihedral and antipodal symmetries of the base, every azimuth-dependent integral reduces to twelve identical sectors \(0<\phi<\pi/6\). Within this sector the three horizontal absolute-value magnitudes (before multiplying by \(\sqrt{1-t^2}\)) are
\[
R\cos(\phi+\pi/3),\qquad R\cos(\phi-\pi/3),\qquad R\cos\phi
\]
in increasing order. For any \(m\ge0\), the inequality
\[
Ht/2>Rm\sqrt{1-t^2}
\]
is equivalent to \(t>g_H(m)\), where
\[
g_H(m)=\frac{2Rm}{\sqrt{H^2+4R^2m^2}}.
\]
Because \(t\) is uniform and independent of \(\phi\), the regime table yields
\[
p_3=1-\frac6\pi\int_0^{\pi/6}g_H(\cos\phi)\,d\phi,
\]
\[
p_5=\frac6\pi\int_0^{\pi/6}
\big[g_H(\cos(\phi-\pi/3))-g_H(\cos(\phi+\pi/3))\big]d\phi.
\]
For all angles occurring here, the antiderivative is
\[
\int g_H(\cos\theta)\,d\theta
=\arcsin\!\left(\frac{2R}{\sqrt{H^2+4R^2}}\sin\theta\right).
\]
Since \(2R/\sqrt{H^2+4R^2}=q(H)\), evaluation at the limits gives the stated formulas for \(p_3\) and \(p_5\). The remaining probability \(p_4=1-p_3-p_5\) gives the stated expression. All identities are exact for every \(H>0\).

**4. Unique optimum.** Since \(q(H)\) decreases strictly from \(1\) to \(0\), maximize
\[
W(q)=2\arcsin(\sqrt3q/2)-\arcsin(q/2)-\arcsin(q),\qquad0<q<1.
\]
After dividing the derivative \(W'(q)\) by the positive factor \(1/\sqrt{1-q^2}\) and setting \(x=q^2\), its sign becomes that of
\[
G(x)=\sqrt3\sqrt{\frac{1-x}{1-3x/4}}
-\frac12\sqrt{\frac{1-x}{1-x/4}}-1.
\]
Now \(G(0)=\sqrt3-3/2>0\), \(\lim_{x\uparrow1}G(x)=-1\), and direct differentiation gives
\[
G'(x)=\frac{-2\sqrt3(1-3x/4)^{-3/2}+3(1-x/4)^{-3/2}}{16\sqrt{1-x}}<0.
\]
The strict inequality holds because \(2\sqrt3>3\) and \(1-3x/4\le1-x/4\). Therefore \(G\) crosses zero exactly once; \(W\) increases and then decreases as a function of \(q\). This yields the unique \(q_*\) and the unique \(H_*\). Finally \(W(0)=W(1)=0\) and \(W(q)>0\) for \(0<q<1\), establishing the strict maximum and endpoint limits.

## Verification

The standalone file `verify_prism.py` supplies independent checks of the edge-sign combinatorics and spherical integrals. Its exact-algebraic branch checks use rationals plus \(\sqrt3\) and perform more than 40,000 assertions across finite sets of nondegenerate plane orientations and six rational prism heights. An independent numerical quadrature of both probability integrals agrees with the closed formulas for eleven prism heights, and a bracketed derivative root check confirms the displayed optimal-height bounds. The script prints the number of successful assertions.

To reproduce, place `verify_prism.py` in a directory with Python, NumPy-free standard libraries, and SciPy installed, and run `python verify_prism.py`. The computation does not establish a theorem for all heights or orientations; the analytic proof above does so. No Monte Carlo data are needed to infer the formulas.

## Relationship to prior work

A 2026 study of random widths and brightness of three-dimensional polytopes develops exact spherical distributions for directional observables. The present calculation instead concerns the **combinatorial type of a central planar section** of a continuously varying triangular-prism family. Earlier stereological work studies random sections of prisms, including size/shape and angular distributions, principally with randomly placed sampling planes; those observations motivate asking for a closed Haar law conditioned to pass through the center. The joint three-/four-/five-gon probability formulas and unique pentagon-optimal aspect ratio are the specific new claims assessed here, not the familiar possibility of these polygonal section types.

## Limitations

The result does not describe translated or non-central plane sections, non-equilateral bases, random polygonal silhouettes, or section angle/area distributions. A plausible earlier paper on triangular-prism section-angle distributions was accessible only at its abstract, as was a 1995 prism-stereology study; therefore a historically equivalent full-text calculation remains a priority risk. An independent subject-matter audit has not been performed.

## References

- O. Abas, *Random Width and Brightness: Polyhedral Density Theory, Reconstruction, and Gaussian Identifiability*, first public version 2026-08-10, arXiv:2609.26202, https://arxiv.org/abs/2609.26202 (abstract verified; the paper concerns width and brightness).
- E. P. Konstantinova and L. N. Shchur, *Algorithm for density of angle distribution in random sections of polyhedron*, *Expert Systems with Applications* **235** (2024), 121195, DOI:10.1016/j.eswa.2023.121195; earlier public SSRN abstract DOI:10.2139/ssrn.4485810 (abstract verified; full text unavailable).
- J. Ohser and F. Mücklich, *Stereology for some classes of polyhedrons*, *Advances in Applied Probability* **27** (1995), 384–396, DOI:10.2307/1427832 (abstract verified; full text unavailable).
