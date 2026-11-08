# A three-phase conditional face-count law for random central sections of the cube

## Finding

Let \(Q=[-1/2,1/2]^3\) be the unit-edge Euclidean cube. Let \(U\) be uniformly distributed on the unit sphere \(S^2\), and let \(N\) count the vertices of the central planar section \(Q\cap U^\perp\). Let \(W\) be the width of \(Q\) in the same normal direction (the length of its orthogonal projection onto the line spanned by \(U\)). Almost surely \(N\in\{4,6\}\). Define, for \(1<s<\sqrt3\),
\[
q(s)=\frac{s}{\sqrt{6-2s^2}},\qquad
\alpha(s)=\arccos\!\left(\frac{q(s)}2\right)
\quad\text{when }\sqrt2\le s\le\sqrt{8/3}.
\]
The **joint distribution** of \((W,N)\) is absolutely continuous in its first variable, with subdensities \(f_j(s)=\frac{d}{ds}\Pr\{W\le s,N=j\}\) given, away from the endpoints, by
\[
f_4(s)=\begin{cases}
\displaystyle \frac4{\sqrt3}\left[1-\frac3\pi\arccos q(s)\right],&1<s<\sqrt2,\\[2mm]
\displaystyle\frac{12}{\pi\sqrt3}\alpha(s),&\sqrt2<s<\sqrt{8/3},\\[2mm]
0,&\text{otherwise},
\end{cases}
\]
\[
f_6(s)=\begin{cases}
0,&s\le\sqrt2,\\[1mm]
\displaystyle \frac4{\sqrt3}\left[1-\frac3\pi\alpha(s)\right],&\sqrt2<s<\sqrt{8/3},\\[2mm]
\displaystyle\frac4{\sqrt3},&\sqrt{8/3}<s<\sqrt3,\\[2mm]
0,&s\ge\sqrt3.
\end{cases}
\]
In particular, a version of the conditional probability for almost every admissible width is
\[
\Pr(N=4\mid W=s)=
\begin{cases}
1,&1<s<\sqrt2,\\[1mm]
\displaystyle\frac3\pi\arccos\!\left(\frac{s}{2\sqrt{6-2s^2}}\right),&\sqrt2<s<\sqrt{8/3},\\[2mm]
0,&\sqrt{8/3}<s<\sqrt3.
\end{cases}
\]
This conditional probability decreases strictly through the intermediate interval, from one to zero. Thus **small-width cuts are necessarily quadrilateral, large-width cuts are necessarily hexagonal, and the intermediate widths have an explicit continuously varying mixture**. The marginal quadrilateral probability, already implied by the known average vertex count, is recovered as
\[
\Pr(N=4)=3-\frac{12}{\pi}\arctan\frac1{\sqrt2}
\approx0.649040687816356.
\]

## Assumptions and scope

The width and section use the **same** Haar-uniform normal \(U\); they are not sampled independently. The cube's edge length is exactly one. Planes pass through the center; uniformly translated or offset planes obey different laws. The section vertex count is combinatorial, not an assertion that its four or six sides have equal lengths. Directions satisfying a coordinate-zero condition or an exact triangle-equality condition form spherical-measure-zero sets, so values of conditional probabilities at individual transition widths do not affect the distribution.

For \(1<s<\sqrt3\), the function \(q\) is real and increasing; the arccosine expressions are used only in the intervals where their arguments lie in \([-1,1]\). The density is zero outside \([1,\sqrt3]\). The displayed subdensities are nonnegative and sum to the known directional-width density.

## Proof

**1. Geometric criterion for the section type.** Write \(u_i=|U_i|\), which are strictly positive almost surely, and \(s=u_1+u_2+u_3\). The cube's width is \(W=s\), since its support function is \(h_Q(U)=s/2\). A central plane meets the relative interior of both faces \(x_i=\pm1/2\) exactly when \(u_i<u_j+u_k\): on the face \(x_i=1/2\), the other coordinates can cancel \(u_i/2\) exactly when their possible signed sum reaches that magnitude. A generic central cube section has four or six sides. Thus \(N=6\) exactly when the three positive \(u_i\) obey all strict triangle inequalities, and \(N=4\) exactly when \(\max_i u_i>s/2\). The equality surfaces have measure zero.

**2. Width circles and their area element.** By coordinate-sign symmetry it suffices to use the positive spherical octant, of area \(\pi/2\). Put \(e=(1,1,1)/\sqrt3\), and let \(v_1,v_2\) be any orthonormal basis of \(e^\perp\). On \(u_1+u_2+u_3=s\) one has
\[
u(s,\phi)=\frac{s}{3}(1,1,1)
+\sqrt{1-\frac{s^2}{3}}
(\cos\phi\,v_1+\sin\phi\,v_2).
\]
This is a small circle on \(S^2\), for which the spherical area element is \(d\sigma=ds\,d\phi/\sqrt3\). Indeed \(s=\sqrt3\cos\theta\) and \(d\sigma=\sin\theta\,d\theta\,d\phi\). Accordingly the probability subdensity equals the *angular length of the corresponding subset of this circle* multiplied by \(2/(\pi\sqrt3)\).

The coordinates are, for three angles \(\phi_i\) spaced by \(2\pi/3\),
\[
u_i(s,\phi)=\frac{s}{3}+\frac{\sqrt{6-2s^2}}{3}\cos(\phi-\phi_i).
\]
Hence \(u_i>0\) exactly when \(\cos(\phi-\phi_i)>-q(s)\). The range \(1<s<\sqrt2\) corresponds to \(1/2<q(s)<1\). There each prohibited arc \(u_i<0\) has angular length \(2\arccos q(s)\). Two prohibited arcs cannot overlap: otherwise the remaining positive coordinate would exceed \(s>1\), contrary to \(u_i\le1\). The total angular length in the octant is therefore \(2\pi-6\arccos q(s)\). For \(s\ge\sqrt2\), the minimum coordinate along the entire small circle is \((s-\sqrt{6-2s^2})/3\ge0\), so its total admissible angular length is \(2\pi\).

**3. Why hexagons start only at \(\sqrt2\).** Under the strict triangle inequalities, \(\max_i u_i<s/2\). Therefore \(1=\sum_i u_i^2\le(\max_i u_i)\sum_i u_i<s^2/2\), implying \(s>\sqrt2\). Consequently every generic central section at widths less than \(\sqrt2\) is quadrilateral. Multiplying the admissible angular length found in step 2 by \(2/(\pi\sqrt3)\) gives the first piece of \(f_4\) and the vanishing first piece of \(f_6\).

**4. Exactly measured competing arcs.** When \(s>\sqrt2\), the whole small circle is in the positive octant. The condition \(u_i>s/2\) becomes \(\cos(\phi-\phi_i)>q(s)/2\). It has an arc of angular length \(2\alpha(s)\) while \(q(s)<2\), equivalently \(s<\sqrt{8/3}\), and is empty above that threshold. The three such arcs are disjoint because two coordinates cannot both exceed half their sum. Thus the total quadrilateral angular length is \(6\alpha(s)\) on the intermediate interval and zero above it. The complement produces hexagonal sections. Multiplication by \(2/(\pi\sqrt3)\) gives both remaining subdensity pieces and the conditional formula.

**5. Sharpness, normalization, and strict monotonicity.** The density \(f_4+f_6\) is precisely the full small-circle density obtained in step 2, hence integrates to one over the whole positive octant. Its mean is the known cube mean width. Since \(q(s)\) is strictly increasing on \((1,\sqrt3)\) and \(\arccos\) strictly decreases, the intermediate conditional quadrilateral probability decreases strictly. It equals one as \(s\downarrow\sqrt2\) and zero as \(s\uparrow\sqrt{8/3}\). Both transition values arise from attainable limiting directions, so they cannot be enlarged. Integrating \(f_4\), or comparing the integral with the known average section-vertex count of Lonke, gives the stated marginal. This completes the joint-law proof.

## Verification

The independent standalone Python 3 program `verify.py` uses the standard library only. Execute `python3 verify.py` in the directory containing this document and the script. It computes adaptive numerical integrals of both subdensities and the first two width moments; compares the quadrilateral mass with the exact marginal deduced from Lonke's result; evaluates ten conditional small-circle angular lengths directly using an independent coordinate parametrization; and checks 350,000 Gaussian-sampled directions. Each sampled section type is computed independently by testing all twelve cube edges for opposite endpoint signs rather than using the triangle criterion. Twelve width-by-type bin probabilities are compared with the derived integrals. The program exits with `VERIFY_OK` on success.

These checks are finite and numerical; the theorem for every admissible width is established by the argument above. In particular, simulations do not establish the exact phase boundaries or the almost-everywhere statements.

## Relationship to prior work

Lonke (initial arXiv public version December 21, 1998) calculated the expected number of vertices of Haar-random central cube sections. In dimension three it determines the **unconditional** quadrilateral probability, but it does not provide the joint distribution with width. Finch (initial public arXiv version October 4, 2011) calculated cube-width moments and motivated its full distribution. Kabluchko–Litvak–Zaporozhets (first public version November 26, 2015) established all moments of random projection lengths, determining the width marginal on compact support, but not the coupling to section combinatorics.

Two closely related publicly available results give, respectively, the complete **marginal** width density for the three-cube and the **marginal** hexagon probability of central rectangular-box sections (including the cube). Their inspected theorem statements and proofs do not determine the conditional widths of four- and six-sided sections. The present result computes the missing joint allocation along each width circle, including two exact phase boundaries, while recovering both previously known marginals. Known marginal laws alone do not logically determine a joint distribution. Historical priority for the particular conditional law has not been independently established.

## Limitations

The claim applies only to uniformly oriented *central* sections of the unit cube. It does not cover randomly offset planes, unequal rectangular boxes, oblique parallelepipeds, or higher-dimensional cubes. Boundary-width conditional values can be defined arbitrarily and are not claimed. The proof does not establish historical priority against every unindexed source; the novelty comparison is qualified by the primary literature and published records listed below. No independent mathematical audit has been performed.

## References

1. Y. Lonke, *On random sections of the cube*, arXiv:math/9812123 (first public version 1998-12-21), especially Section 2 and the three-dimensional calculation; https://arxiv.org/abs/math/9812123.
2. S. R. Finch, *Width Distributions for Convex Regular Polyhedra*, arXiv:1110.0671 (first public version 2011-10-04), especially Section 4; https://arxiv.org/abs/1110.0671.
3. Z. Kabluchko, A. E. Litvak, D. Zaporozhets, *Mean width of regular polytopes and expected maxima of correlated Gaussian variables*, arXiv:1511.08479 (first public version 2015-11-26), especially Section 3.2; https://arxiv.org/abs/1511.08479.
4. *Exact directional width law of the cube and its first spherical-cap transition*, public published-finding corpus record (2026), scientific result and proof at https://github.com/published-finding corpus/2026/blob/main/2026/10/11/SCOPE-exact-directional-width-law-of-the-cube-and-its-first-spherical--c1e6aa54ecb2/RESULT.md.
5. *Exact Haar hexagon law and cubic rigidity for central sections of rectangular boxes*, public published-finding corpus record (2026), scientific result and proof at https://github.com/published-finding corpus/2026/blob/main/2026/10/11/SCOPE-exact-haar-hexagon-law-and-cubic-rigidity-for-central-sections-o--45d2a55425d4/RESULT.md.
