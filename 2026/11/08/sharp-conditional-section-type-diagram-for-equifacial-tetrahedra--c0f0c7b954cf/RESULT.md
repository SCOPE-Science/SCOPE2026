# Sharp conditional section-type diagram for equifacial tetrahedra

## Finding

Let \(T\) be a nondegenerate equifacial (disphenoid) Euclidean tetrahedron: its four triangular faces are congruent. Let \(G\) be its centroid. Choose an unoriented plane \(H\) through \(G\) by the rotation-invariant probability measure on planes, and let \(q(T)\) be the probability that \(T\cap H\) is a quadrilateral rather than a triangle. For each of the three pairs of opposite edges, the segment joining the edge midpoints is a *bimedian*. Let their positive lengths be \(2a,2b,2c\), and put

\[
p_1=\frac{a^2}{a^2+b^2+c^2},\quad p_2=\frac{b^2}{a^2+b^2+c^2},\quad p_3=\frac{c^2}{a^2+b^2+c^2},\qquad t=\max(p_1,p_2,p_3).
\]

Thus \(p_i>0\), \(\sum p_i=1\), and \(1/3\le t<1\). Define \(f(x)=\arcsin\sqrt{x}\) on \([0,1]\), and

\[
Q_-(t)=3-\frac4\pi\left[f(t)+2f\left(\frac{1-t}{2}\right)\right],
\]

\[
Q_+(t)=\begin{cases}
3-\frac4\pi\bigl[2f(t)+f(1-2t)\bigr],&1/3\le t<1/2,\\
1,&1/2\le t<1.
\end{cases}
\]

**Exact conditional range theorem.** For each fixed \(t\in[1/3,1)\), the attainable values of \(q(T)\) among all nondegenerate equifacial tetrahedra with this \(t\) are exactly

\[
\begin{cases}
[Q_-(t),Q_+(t)],&1/3\le t<1/2,\\
[Q_-(t),1),&1/2\le t<1.
\end{cases}
\]

The lower endpoint is attained exactly when the *other two* normalized squared bimedians coincide (up to permutation). If \(1/3<t<1/2\), the upper endpoint is attained exactly when the two largest normalized squared bimedians coincide. At \(t\ge1/2\), the upper bound \(1\) is a nonattained supremum, approached only by flattening a bimedian. At \(t=1/3\), only the regular tetrahedron occurs and the range is a singleton.

Both boundary functions are strictly increasing on \((1/3,1/2)\), and \(Q_-\) is strictly increasing on \((1/3,1)\). In particular,

\[
q(T)\ge q_{\mathrm{reg}}=3-\frac{12}{\pi}\arcsin\frac1{\sqrt3},
\]

with equality only for the regular tetrahedron; this unconditional inequality is **already implied by earlier work on equifacial solid-angle sums** and is included solely as context, not a novelty claim. The new result is the complete, sharp *fixed-dominant-bimedian* range, including its change of upper extremizer at \(t=1/2\).

Equivalently, the measured quadrilateral probability gives sharp inverse bounds on \(t\): for \(q_{\mathrm{reg}}<q<1\), let \(t_+(q)\in(1/3,1/2)\) be the unique solution of \(Q_+(t_+(q))=q\), and let \(t_-(q)\in(1/3,1)\) be the unique solution of \(Q_-(t_-(q))=q\). Then the exact feasible interval is \(t_+(q)\le t\le t_-(q)\); both endpoints occur in nondegenerate equifacial tetrahedra. This is a one-bit section-type inverse constraint, not complete shape reconstruction.

## Assumptions and scope

The tetrahedron is nondegenerate, Euclidean, and equifacial; no right-angle, symmetry-axis, or generic distinct-axis hypothesis is imposed. The normal direction of \(H\) is Haar-uniform on the sphere, with antipodal normals identified. Exceptional normals for which \(H\) contains a tetrahedral vertex have probability zero. The parameter \(t\) is intrinsic and scale-invariant because the three bimedians are determined by the tetrahedron. Every triple of positive \(p_i\) summing to one is realizable by a nondegenerate equifacial tetrahedron. The classification concerns the number of polygon sides, not section area, perimeter, or offset planes.

## Proof

**1. Orthogonal bimedian coordinates.** Translate the centroid to the origin and label the four vertices \(v_1,v_2,v_3,v_4\). Put

\[
x=(v_1+v_2)/2,\quad y=(v_1+v_3)/2,\quad z=(v_1+v_4)/2.
\]

Since \(\sum v_i=0\), the four vertices become \(x+y+z,\ x-y-z,\ -x+y-z,\ -x-y+z\). Opposite-edge equality implies \(\|y+z\|=\|y-z\|\), \(\|x+z\|=\|x-z\|\), and \(\|x+y\|=\|x-y\|\). Therefore \(x,y,z\) are mutually perpendicular. Nondegeneracy makes all three nonzero. In an orthonormal basis the vertices are

\[
(a,b,c),\ (a,-b,-c),\ (-a,b,-c),\ (-a,-b,c),\qquad a,b,c>0.
\]

The three bimedian lengths are \(2a,2b,2c\). Conversely these vertices form an equifacial nondegenerate tetrahedron for every positive triple, proving realizability.

**2. Exact section probability.** For a unit normal \(u\), put \(\varepsilon_i=\operatorname{sgn}(u\cdot v_i)\). Outside a null set, \(\sum_i\varepsilon_i\) belongs to \(\{-2,0,2\}\): there must be vertices on both sides because their vector sum is zero. A plane separates either one vertex from three, giving a triangular section, or two from two, giving a quadrilateral section. The indicator of the latter event is exactly

\[
\mathbf1_{\mathrm{quad}}=1-\frac14\Big(\sum_i\varepsilon_i\Big)^2=-\frac12\sum_{i<j}\varepsilon_i\varepsilon_j.
\]

For two fixed nonzero vectors making angle \(\theta\in(0,\pi)\), a uniformly random plane normal yields opposite signs with probability \(\theta/\pi\), so \(\mathbb E(\varepsilon_i\varepsilon_j)=1-2\theta_{ij}/\pi\). Hence

\[
q(T)=\frac1\pi\sum_{i<j}\theta_{ij}-3.
\]

For each coordinate index \(k\), the pair angle with cosine \(2p_k-1\) occurs twice, giving

\[
q(T)=\frac2\pi\sum_{k=1}^3\arccos(2p_k-1)-3
=3-\frac4\pi\sum_{k=1}^3\arcsin\sqrt{p_k}.
\]

The last equality follows from \(\arccos(2p-1)=\pi-2\arcsin\sqrt p\). All constants are fixed by this normalized Haar measure.

**3. Sharp fixed-\(t\) extrema.** Relabel so \(p_1=t\ge p_2\ge p_3>0\). For every admissible \(t\), \(p_2,p_3\le1/2\), and \(p_2+p_3=1-t\). Direct differentiation gives

\[
f''(x)=\frac{2x-1}{4[x(1-x)]^{3/2}}<0\quad(0<x<1/2).
\]

Therefore \(f(p_2)+f(p_3)\), at fixed sum, is strictly maximized by \(p_2=p_3=(1-t)/2\). Since \(q\) has the opposite sign, this gives exactly \(Q_-(t)\) and its equality case. The same strict concavity makes the sum smallest at an extreme admissible split. For \(1/3\le t<1/2\), the extreme split is \((p_2,p_3)=(t,1-2t)\), giving the attained \(Q_+(t)\). For \(1/2\le t<1\), the extreme split is the excluded boundary \((p_2,p_3)=(1-t,0)\), and

\[
\lim_{p_3\downarrow0}q=3-\frac4\pi\bigl[f(t)+f(1-t)\bigr]=1,
\]

because \(f(t)+f(1-t)=\pi/2\). This limit is never attained by a nondegenerate tetrahedron. Every intermediate value follows from continuity along the one-dimensional admissible split interval, completing the exact range.

**4. Monotonicity and sharp inversion.** Write \(g(t)=f(t)+2f((1-t)/2)\). Then

\[
g'(t)=\frac1{\sqrt{1-t}}\left(\frac1{2\sqrt t}-\frac1{\sqrt{1+t}}\right)<0\quad(t>1/3).
\]

Thus \(Q_-\) is strictly increasing. On \((1/3,1/2)\), the derivative of \(2f(t)+f(1-2t)\) is \(2[f'(t)-f'(1-2t)]<0\) because \(0<1-2t<t<1/2\) and \(f'\) is strictly decreasing there. Thus \(Q_+\) is also strictly increasing in that range, from the common regular value to \(1\). Both functions have the stated domains and endpoints, so their inverses give the precise feasible \(t\)-interval; endpoint attainment was proved in step 3.

## Verification

The accompanying standalone script `verify.py` checks 18,000 randomly chosen positive normalized axis triples against both sharp envelopes. It independently computes the triangular-section probability by summing the four solid vertex angles of the polar disphenoid; this agrees with the complementary formula to floating-point accuracy in five test configurations. It also performs 540,000 Gaussian-direction Monte Carlo plane sections, checks the predicted equality families and degenerating limits, and checks the local quadratic behavior near the regular tetrahedron. The completed run reports `DISPHENOID_SECTION_OK`. These finite calculations support the analytic proof but do not establish the universal inequalities.

## Relationship to prior work

The probability–angle interpretation of random simplex *orthogonal projections* appears in Feldman and Klain (2008), especially their Theorem 1. Via polarity, central sections of a tetrahedron correspond to projections of the polar tetrahedron, so this is a close antecedent for the basic section-count formula. A disphenoid's orthogonal-box realization is classical and appears in Hajja and Walker's study of equifacial tetrahedra and in Katsuura (2020). Katsuura proves that the sum of the four solid vertex angles of an equifacial tetrahedron is largest for the regular tetrahedron. Applying that result to the polar (also equifacial) tetrahedron recovers the **unconditional** regular extremum of section-type probability; no independent originality is claimed for that implication. The currently asserted refinement is the exact two-sided *conditional* probability interval at a fixed largest normalized squared bimedian, its attained/nonattained endpoints and the transition at \(t=1/2\). Neither the inspected complete text of Feldman–Klain nor Katsuura gives these fixed-parameter sharp bounds. A closed-form section probability is not itself a claim of novelty.

The general silhouette and projection literature is relevant but differs in its objects and conditioning. Related published exact laws for rectangular-box central sections concern six-sided sections of boxes rather than four-sided sections of equifacial tetrahedra. A complete external bibliographic priority certification is not asserted.

## Limitations

No claim is made about arbitrary tetrahedra, noncentral sections, nonuniform orientation sampling, or the full section-area distribution. The known regular extremum is distinguished explicitly from the newly derived sharp conditional range. The use of an angular statistic does not reconstruct all three bimedians; it gives optimal bounds on the dominant one. The strict upper boundary \(1\) for \(t\ge1/2\) requires a degenerate limiting tetrahedron and is excluded for nondegenerate bodies. All source comparisons are subject to the residual risk of historical results not indexed or freely accessible, particularly the complete Hajja–Walker text. Independent mathematical review has not been performed.

## References

1. D. V. Feldman and D. A. Klain, *Angles as probabilities*, arXiv:0809.3459 (first version 2008-09-19), https://arxiv.org/abs/0809.3459.
2. H. Katsuura, *Solid Angle Sum of a Tetrahedron*, Journal for Geometry and Graphics **24** (2020), 29–34, https://www.heldermann-verlag.de/jgg/jgg24/j24h1kats.pdf.
3. M. Hajja and P. Walker, *Equifacial tetrahedra*, International Journal of Mathematical Education in Science and Technology **32** (2001), 501–508, DOI 10.1080/00207390110038231; abstract accessible, complete text not inspected.
4. S. Ciccariello, *The intersect distribution of the regular tetrahedron*, Journal of Applied Crystallography **38** (2005), 97–106, DOI 10.1107/S0021889804028328; concerns random line-intercept lengths, not orientation-uniform plane-section types.
