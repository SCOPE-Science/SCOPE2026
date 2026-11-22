# A first-order maximum-section transition and a sharp contact cusp for capped paraboloids

## Finding
Let \(R,H>0\) and consider the closed circular capped paraboloid
\[
K_{R,H}=\{(x,y,z)\in\mathbb R^3: H(x^2+y^2)/R^2\le z\le H\}.
\]
Its volume centroid has axial coordinate \(2H/3\). For every plane through that centroid, let \(A\) denote the Euclidean area of its section with \(K_{R,H}\). Parameterize unoriented planes, up to axial rotation, by \(s\in[0,\infty]\): for finite \(s\), the plane is \(z=2H/3+(H/R)sx\), and \(s=\infty\) denotes a vertical plane. Put \(\kappa=H/R\).

Define \(c=2/3\), \(e=1/3\), \(\rho(s)=\sqrt{c+s^2/4}\), and
\[
S(s)=\begin{cases}
\pi\rho(s)^2,&0\le s\le e,\\
\rho(s)^2\left[\arccos(-q(s))+q(s)\sqrt{1-q(s)^2}\right],&s>e,
\end{cases}\qquad q(s)=\frac{e/s-s/2}{\rho(s)}.
\]
Then the complete section-area profile is
\[
A_\kappa(s)=R^2\sqrt{1+\kappa^2s^2}\,S(s)\quad (0\le s<\infty),
\qquad A_\kappa(\infty)=\frac43 RH.
\]
In particular, \(0<S(s)\) and \(sS(s)<4/3\) for every finite \(s>0\). The positive, continuous function
\[
T(s)=\left[\left(\frac4{3S(s)}\right)^2-s^2\right]^{-1}
\]
has \(T(0)=\pi^2/4\), \(\lim_{s\to\infty}T(s)=5/3\), and attains its global maximum at one or more finite parameters *strictly greater than* \(1/3\). Define the exact critical aspect ratio
\[
\kappa_*=\sqrt{\max_{s\ge0}T(s)}.
\]
There is precisely one height-to-radius threshold \(\kappa_*\) with the following complete global alternatives:

- If \(0<\kappa<\kappa_*\), every maximizing section is strictly oblique and crosses the top cap in a nondegenerate chord (\(s>1/3\)).
- If \(\kappa=\kappa_*\), vertical sections tie with at least one cap-crossing oblique section. The finite parameters giving equality are exactly the maximizers of \(T\).
- If \(\kappa>\kappa_*\), only vertical planes maximize section area (up to axial rotation).

Thus the maximizing inclination changes discontinuously at \(\kappa_*\); no uniqueness of the oblique maximizing inclination is asserted. Numerical quadrature suggests \(\kappa_*\approx1.98151821\), but the decimal is not a certified enclosure and is not used in the theorem.

A second sharp assertion concerns the top-cap contact. As \(s\downarrow1/3\) from above, the area deficit relative to continuation of the untruncated paraboloid section is
\[
\pi\rho(s)^2-S(s)=\frac{24\sqrt6}{5}\left(s-\frac13\right)^{3/2}
+O\left((s-\tfrac13)^{5/2}\right).
\]
For a Haar-uniform unoriented plane through the centroid, the exact probability of a nondegenerate top-cap crossing is
\[
\Pr(\text{top-cap chord})=\frac1{\sqrt{1+(H/(3R))^2}}.
\]
Hence this probability and the horizontal centroidal section area \(2\pi R^2/3\) reconstruct \(R\) and \(H\) uniquely.

## Assumptions and scope
All geometry is Euclidean in dimension three, with the *solid* paraboloid (not merely its boundary), a horizontal top disk, and planes required to pass through the volume centroid. Planes are sampled by normalized rotation-invariant probability on the unoriented Grassmannian only for the contact-probability assertion. Vertical sections are limits of the finite-slope family. The parameter \(s\) is dimensionless and is the physical plane slope divided by \(\kappa\). The phase transition is global in plane orientation; the cap cusp is a one-sided local statement at fixed positive \(R,H\). The exact definition of \(\kappa_*\) is variational rather than an asserted closed elementary constant.

## Proof
**1. Centroid and planar reduction.** At height \(z=Hw\), \(0\le w\le1\), the horizontal disk has area \(\pi R^2w\). Thus the centroid height divided by \(H\) is \(\int_0^1 w^2dw/\int_0^1 wdw=2/3\). Rotational symmetry reduces every nonvertical plane through the centroid to \(z=H(c+s x/R)\) with \(s\ge0\). With \(u=x/R\), \(v=y/R\), its projected section is
\[
\{(u,v):u^2+v^2\le c+su,\;c+su\le1\}.
\]
Completing the square gives the disk \((u-s/2)^2+v^2\le\rho(s)^2\), clipped by \(u\le e/s\) when \(s>0\). The upper clipping line first touches the disk at \(s=e=1/3\): its rightmost point is strictly left of the line for \(s<e\), equals the line for \(s=e\), and lies beyond it for \(s>e\). The standard circular-segment integral gives exactly the two branches of \(S(s)\). The graph metric multiplies projected planar area by \(R^2\sqrt{1+\kappa^2s^2}\). In the vertical limit \(x=0\), its area is \(\int_0^H2R\sqrt{z/H}\,dz=4RH/3\).

**2. Strict comparison with the vertical section.** For \(0<s\le e\), \(sS(s)=\pi s(c+s^2/4)\le25\pi/108<4/3\). For \(s>e\), set \(w=su\) in the original cross-section integral, and put
\[
w_-(s)=-\frac{2c}{1+\sqrt{1+4c/s^2}}>-c.
\]
Then
\[
sS(s)=2\int_{w_-(s)}^e\sqrt{c+w-w^2/s^2}\,dw
<2\int_{-c}^e\sqrt{c+w}\,dw=\frac43.
\]
(The inequality is strict because of the negative term under the square root on a positive-measure set.) Consequently \(T(s)\) is well-defined and positive. Squaring positive areas gives the exact equivalence
\[
A_\kappa(s)>A_\kappa(\infty)\quad\Longleftrightarrow\quad\kappa^2<T(s).
\]
Equality holds if and only if \(\kappa^2=T(s)\).

**3. Endpoint limits and existence of a finite critical orientation.** The first branch gives \(S(0)=2\pi/3\), so \(T(0)=\pi^2/4\). For \(s\to\infty\), dominated expansion in the integral above, with the moving lower endpoint contributing smaller order, yields
\[
sS(s)=\frac43-\frac{2}{5s^2}+o(s^{-2}).
\]
For completeness, the coefficient is obtained from
\[
\int_{-c}^e\frac{w^2}{\sqrt{c+w}}\,dw
=\int_0^1\frac{(t-2/3)^2}{\sqrt t}\,dt=\frac25.
\]
It follows that \((4/(3S(s)))^2-s^2\to3/5\) and \(T(s)\to5/3\). For \(0\le s\le e\), the derivative of \((4/(3S))^2-s^2\) is negative for \(s>0\), since \(S'(s)>0\); hence \(T\) increases strictly on \([0,e]\). At \(s=e\), \(S(e)=25\pi/36\), whence
\[
T(e)=\left[\left(\frac{48}{25\pi}\right)^2-\frac19\right]^{-1}>3>\max\{T(0),5/3\},
\]
using \(3<\pi<22/7\). By the contact expansion proved in step 5, \(S\) has the same first derivative from either side at \(e\), and thus \(T'(e+)>0\). Continuity, the endpoint limits, and this strict increase show that the maximum is achieved in a compact set contained in \((e,\infty)\).

**4. The global phase classification.** Set \(\kappa_*^2=\max T\). When \(\kappa<\kappa_*\), step 2 supplies some finite section exceeding the vertical area; since \(A_\kappa\) is continuous on the one-point compactification \([0,\infty]\), a finite maximizer exists. The untruncated profile \(A_\kappa(s)=\pi R^2(c+s^2/4)\sqrt{1+\kappa^2s^2}\) is strictly increasing on \((0,e)\), and remains increasing immediately beyond \(e\) because the cap deficit has zero first derivative there. Therefore no finite maximizer has \(s\le e\). At equality \(\kappa=\kappa_*\), step 2 identifies all finite ties with the maximizers of \(T\), in addition to the vertical section. For \(\kappa>\kappa_*\), every finite section has strictly smaller area than the vertical section. This proves the asserted unique critical aspect ratio and discontinuous switch without assuming a unique oblique parameter.

**5. Sharp contact coefficient.** For \(s>e\), let \(h(s)=s/2+\rho(s)-e/s\) be the height of the small circular cap removed from the untruncated projected disk. At \(s=e\), \(\rho(e)=5/6\), \(h(e)=0\), and direct differentiation gives \(h'(e)=18/5\). A circular cap of depth \(h\downarrow0\) on a radius-\(\rho\) disk has area \(\frac{4\sqrt2}{3}\sqrt\rho\,h^{3/2}+O(h^{5/2})\), by integrating \(2\sqrt{2\rho t-t^2}\) from \(0\) to \(h\). Substitution gives
\[
\frac{4\sqrt2}{3}\sqrt{\frac56}\left(\frac{18}{5}\right)^{3/2}
=\frac{24\sqrt6}{5},
\]
with the stated error. This also proves that \(S'(e+)=S'(e-)\), as used above.

**6. Haar contact probability and inverse.** Let \(\beta\in[0,\pi/2]\) be the angle between a plane and the horizontal, so \(\tan\beta=\kappa s\). Nondegenerate top-cap crossing occurs precisely when \(\tan\beta>\kappa/3\). For a uniform unoriented plane normal \(N\), \(|N_z|=\cos\beta\) is uniform on \([0,1]\), so the event probability is \(p=(1+\kappa^2/9)^{-1/2}\). Given the observed \(p\) and horizontal centroid-section area \(A_h\), the exact inverse is
\[
\kappa=3\sqrt{p^{-2}-1},\quad R=\sqrt{\frac{3A_h}{2\pi}},\quad H=\kappa R.
\]

## Verification
A standalone Python 3 standard-library program `checker.py` verifies the circular-segment profile against an independent Simpson integration of cross-sectional widths, evaluates the \(3/2\)-power coefficient at several small positive increments, tests the exact vertical-tie algebra and pre/post-transition examples, checks the inverse probability formula, and checks the large-s asymptotic coefficient. Run `python checker.py` in the directory containing this document. The recorded execution passed 91 deterministic checks. These numerical checks corroborate the formulas but do not establish the supremum or the global quantifiers; those follow from the analytic inequalities and compactness proof above.

## Relationship to prior work
The area of an unbounded paraboloid's oblique planar ellipse section is classical. Kim and Kim (2012, arXiv:1208.5361) derive tangent-parallel section-area identities and characterize elliptic paraboloids; these do not analyze a *flat capped* solid or centroidal orientation optimization. Kim, Yaskin and Zvavitch (2015, arXiv:1512.07289) develop general unlabeled distributions of central sections and exhibit nonuniqueness; they do not provide the present capped-paraboloid-specific critical profile or transition. The published capped-paraboloid John–Löwner result concerns extremal inscribed/enclosing ellipsoids of the same solid, not areas of its centroidal plane sections. The published central-section cap-contact law for Euclidean capsules treats a different body and a different contact exponent. The new claims are the exact global aspect-ratio criterion and top-cap contact signature for this body, not the elementary circle-segment integral itself. An earlier unindexed exact classification remains a historical-priority possibility.

## Limitations
No proof is asserted that the maximizing finite slope is unique or that the displayed numerical approximation to \(\kappa_*\) has a certified error bound. The result does not classify off-centroid affine sections, other quadratic caps, or dimensions above three. The probability statement presupposes Haar-distributed plane orientations and recognizes a top-cap chord; it does not claim statistical robustness under noise. Independent mathematical audit and exhaustive historical-priority certification have not been performed.

## References
1. D.-S. Kim and Y. H. Kim, *Some characterizations of spheres and elliptic paraboloids II*, arXiv:1208.5361, publicly submitted 2012-08-27, https://arxiv.org/abs/1208.5361 (full HTML text inspected).
2. J. Kim, V. Yaskin and A. Zvavitch, *Distribution functions of sections and projections of convex bodies*, arXiv:1512.07289v1, publicly submitted 2015-12-22, https://arxiv.org/html/1512.07289v1 (full HTML text inspected).
3. *Exact John–Löwner ellipsoids of capped paraboloids and an invariant cone enclosure*, published mathematical result at https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-exact-john-l-wner-ellipsoids-of-capped-paraboloids-and-an-invari--2cc8cfb763bd (RESULT.md inspected).
4. *A sharp cap-contact singularity in random central sections of capsules*, published mathematical result at https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-a-sharp-cap-contact-singularity-in-random-central-sections-of-ca--c05ab623ea0b (RESULT.md inspected).
