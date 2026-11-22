# Sharp hemisphere-breakdown threshold for erased orthogonal regular-polygon spherical codes

## Finding
For integers \(p,q\ge3\), let \(S_{p,q}\subset S^3\) be the union of the unit vertices of centered regular \(p\)- and \(q\)-gons in perpendicular two-planes of \(\mathbb R^4\). For any nonempty surviving site set \(T\subset S_{p,q}\), define its *covering cosine*
\[
\mu(T)=\min_{x\in S^3}\max_{v\in T}\langle x,v\rangle,
\qquad \rho(T)=\arccos\mu(T).
\]
Thus \(\rho\) is the smallest common angular radius of caps centered at the survivors that covers the entire three-sphere. Both hemispherical and superhemispherical cases are included.

**Exact all-erasure formula.** Write the survivors as \(T=A\cup B\), with \(A\) and \(B\) in the first and second planes. For a nonempty subset \(A\) of the \(p\)-gon, list its retained indices cyclically; let \(g_A\) be the greatest number of *polygon edge steps* from one surviving vertex to the next. Set
\[
 r_A=\cos\frac{\pi g_A}{p};
 \qquad r_B=\cos\frac{\pi g_B}{q}
\]
with the analogous definition for \(B\). A singleton has gap \(p\) or \(q\), hence radius parameter \(-1\). If both groups are nonempty, then
\[
\boxed{\mu(A\cup B)=F(r_A,r_B),\qquad
F(r,s)=\begin{cases}
\dfrac{rs}{\sqrt{r^2+s^2}},&r>0,\ s>0,\\[4pt]
-\dfrac{rs}{\sqrt{r^2+s^2}},&r<0,\ s<0,\\[4pt]
0,&\text{otherwise}.
\end{cases}}
\]
If \(A=\varnothing\) and \(B\ne\varnothing\), the answer is \(\mu(T)=\min\{0,r_B\}\), and symmetrically if only \(A\) survives. Thus the complete covering radius for **every** nonempty erasure pattern is determined by only two largest cyclic gaps.

**Sharp minimal destructive erasures.** The smallest number of site deletions that can produce \(\rho(T)>\pi/2\) is
\[
\boxed{k_{\rm crit}=\lfloor p/2\rfloor+\lfloor q/2\rfloor.}
\]
At exactly this deletion count, there are **exactly \(pq\) destructive subsets**. They are precisely those obtained by deleting \(\lfloor p/2\rfloor\) consecutive vertices in the first polygon and \(\lfloor q/2\rfloor\) consecutive vertices in the second. Every such set has a *unique* deepest uncovered direction and identical covering cosine
\[
\boxed{\mu_*=-\frac{c_p c_q}{\sqrt{c_p^2+c_q^2}},\qquad
c_n=\begin{cases}\sin(\pi/n),&n\text{ even},\\\sin(\pi/(2n)),&n\text{ odd}.\end{cases}}
\]
Every other deletion pattern of this cardinality has covering cosine at least zero.

**Sharp nine-site specialization.** The unique maximum-four-volume inscribed nine-site four-polytope is \(S_{4,5}\) (Medgyes). For erasure counts \(k=0,1,2,3,4\), respectively, the numbers of subsets with covering cosine *positive, zero, negative* are
\[
\boxed{(1,0,0),\ (5,4,0),\ (5,31,0),\ (0,84,0),\ (0,106,20).}
\]
In the twenty four-erasure failures, two *adjacent* square sites and two *adjacent* pentagon sites have been deleted. Their angle is \(106.448803841\ldots^\circ\), with
\[
\mu_*=-c,\qquad c=\frac{\cos(2\pi/5)}{\sqrt{1+2\cos^2(2\pi/5)}}=0.283158486179\ldots.
\]
A single pentagon-site deletion has covering cosine \(+c\) and angle \(73.551196159\ldots^\circ\); the two angles add to \(\pi\). By contrast, deleting any one square site already yields covering radius exactly \(\pi/2\).

## Assumptions and scope
All two-plane vertices lie on the same unit sphere, and the two planes are orthogonal. Both polygons are regular and centered; rotation of either within its plane changes no conclusions. Erasures are arbitrary subsets without replacement. The covering radius is the maximum over the **whole sphere** of the minimum geodesic angular distance to survivors; it is not the Hausdorff distance of two polytopes and not an average nearest-neighbor angle. Full deletion of all \(p+q\) sites is excluded because the minimum over an empty site set has no finite covering radius. No assumption that the origin remains in the surviving convex hull is made. The primary subject is spherical covering by finite point sets (MSC2020 52C17).

## Proof
**1. The one-circle gap lemma, including negative minima.** Let the surviving angles in one unit circle be \(0\le\alpha_1<\cdots<\alpha_m<2\pi\). Let \(G\) be the largest cyclic angular gap, counting the wrap-around gap; for \(m=1\), let \(G=2\pi\). For each unit direction \(u_\theta\), the support of the finite survivor set is
\[
h(u_\theta)=\max_j\langle u_\theta,u_{\alpha_j}\rangle
=\cos\bigl(\min_j d_{S^1}(\theta,\alpha_j)\bigr),
\]
where the circular angular distance lies in \([0,\pi]\). The greatest nearest-site angular distance is precisely \(G/2\), attained at the midpoint of every maximal empty gap. Because cosine decreases on \([0,\pi]\),
\[
\min_{\|u\|=1}h(u)=\cos(G/2).
\]
For survivors from a regular \(n\)-gon, \(G=2\pi g/n\), giving \(r=\cos(\pi g/n)\). In particular this formula remains valid when \(r\) is negative. A unique longest empty gap gives one and only one minimizing direction.

**2. Signed orthogonal-join lemma.** Write every \(x\in S^3\) as \(x=(a u,bv)\) with \(a,b\ge0\), \(a^2+b^2=1\), and \(u,v\in S^1\), using an arbitrary direction in any zero-length component. The support of \(A\cup B\) at \(x\) is \(\max\{a h_A(u),b h_B(v)\}\). The choices of \(u,v\) are independent; minimizing them first therefore leaves
\[
\mu(A\cup B)=\min_{a^2+b^2=1,\ a,b\ge0}\max\{a r_A,b r_B\}.
\]
If \(r_A,r_B>0\), the two competing positive expressions cross once and their maximum is minimized at \(a=r_B/\sqrt{r_A^2+r_B^2}\), \(b=r_A/\sqrt{r_A^2+r_B^2}\). The common value is \(r_A r_B/\sqrt{r_A^2+r_B^2}\). If both parameters are strictly negative, maximizing \(\min\{|r_A|a,|r_B|b\}\) gives the same balanced magnitudes but a *negative* common value; equivalently \(\mu=-r_A r_B/\sqrt{r_A^2+r_B^2}\). In a mixed-sign or zero case, one component's contribution is always nonnegative, so \(\mu\ge0\), while choosing a pure direction in the nonpositive component gives \(\mu\le0\). This proves the three branches. If \(A\) is absent, the support is \(b h_B(v)\) and \(b\) may range from zero to one, giving \(\min\{0,r_B\}\), as asserted.

**3. The minimum deletion count and exact equality patterns.** Suppose a nonempty part of a regular \(n\)-gon survives after deleting \(d\) vertices, with \(0\le d\le n-1\). Every empty cyclic gap between successive surviving vertices contains at most \(d\) deleted vertices, so its edge-step length is at most \(d+1\). Equality occurs exactly when the \(d\) deleted indices are consecutive (for \(d=0\) every gap is one edge; for \(d=n-1\) the unique surviving vertex has gap \(n\)). The support minimum becomes negative precisely when the largest gap exceeds a semicircle, equivalently \(g>n/2\). Thus the smallest deletions allowing a negative parameter in one polygon are \(d_n=\lfloor n/2\rfloor\), and at that threshold the \(n\) qualifying patterns are exactly the consecutive blocks of that length. Their unique longest gap has \(d_n+1\) steps, giving
\[
-\cos\frac{(d_n+1)\pi}{n}=
\begin{cases}\sin(\pi/n),&n\text{ even},\\\sin(\pi/(2n)),&n\text{ odd}.\end{cases}
\]
With both parts present, the signed-join lemma gives strictly negative covering cosine **if and only if** both planar gap parameters are negative. Therefore at least \(d_p+d_q\) deletions are required, and at exactly that count each part must have exactly its own minimum destructive consecutive block. Their independent cyclic starting indices give \(p\cdot q\) distinct patterns. An erasure of an entire factor cannot improve this threshold: if all \(p\) first-plane sites are deleted, a negative cosine requires at least another \(d_q\) deletions in the second plane, strictly more than \(d_p+d_q\); the symmetric case is identical. Each critical block has a unique longest gap, the signed radial balance is unique, and hence the deepest spherical direction is unique. Substituting the two negative parameters into the signed-join formula proves \(\mu_*\).

**4. The square–pentagon counts and dual angle.** For the regular square, one deletion leaves a semicircular maximal gap, so its minimum is zero; two adjacent deletions give parameter \(-\cos(\pi/4)\), while deleting opposite square vertices gives zero. For the regular pentagon, one deletion leaves parameter \(\cos(2\pi/5)>0\); two adjacent deletions give \(-\cos(2\pi/5)\), whereas two nonadjacent deletions leave \(+\cos(2\pi/5)\). Three or more pentagon deletions leave a negative parameter, but fewer than two square deletions never make the square parameter negative. Apply the signed-join formula to the disjoint distribution of erasure counts across the two groups. Enumerating the combinations yields the five displayed triples. In particular the 20 failures at \(k=4\) are exactly \(4\cdot5\) adjacent-block pairs. The critical square and pentagon negative-parameter magnitudes equal the positive parameters of the intact square and once-erased pentagon, respectively; the signed and positive formulas are negatives of one another. Since \(\arccos(-c)=\pi-\arccos(c)\), this proves the claimed dual angular relation.

## Verification
Run `python3 verify.py` with Python 3. It enumerates all erasure subsets of size at most four in the nine-site example and checks the exact sign census, critical cosine, and angular complementarity. It also enumerates every one-circle erasure pattern for \(3\le n\le10\) and checks sharp thresholds, counts and the largest-gap formula, plus explicit spherical directions realizing the predicted four-dimensional minimax values. A second optional verifier `verify_hulls.py` uses NumPy/SciPy to compare the formula independently with convex-hull facet distances or quadratic projections for 1,213 full-dimensional examples across four pairs \((p,q)\). The analytic proof, not the finite tests, establishes the results for every integer pair.

## Relationship to prior work
Medgyes's work on nine- and ten-vertex maximum-volume inscribed four-polytopes identifies the orthogonal square–pentagon and pentagon–pentagon configurations and proves their volume optimality, but it does not address erasure resilience or covering radii of surviving sites. The published study *Sharp cubic deep-hole tails for orthogonal joins of regular spherical polygons* (2026) determines the complete nearest-site distribution **before deletions**, including its nonnegative covering cosine. The present argument uses a different signed regime: deletion can force one or both planar support minima to zero or negative values. Its contribution is the all-pattern signed formula, sharp first superhemisphere erasure threshold, classification and count of all extremal patterns, and the numerical-free square–pentagon failure spectrum. Existing work on Löwner-ellipse stability under erasure instead concerns minimum-enclosing ellipses of **one** planar polygon; its one-third threshold is not the hemispherical covering invariant here. Standard spherical-join geometry provides a conceptual framework, but no inspected source supplied this all-erasure classification. A historical equivalent outside the inspected literature remains possible.

## Limitations
The sharp threshold and pattern count require regular polygons in orthogonal planes, not arbitrary spherical codes. The complete signed formula holds for any residual subset of those regular vertices, including degenerate surviving hulls, but says nothing about perturbation stability of the sites themselves. For a deleted configuration, the nearest direction can fail to be unique away from the minimal destructive threshold. The finite verification is corroboration and does not certify novelty or replace the infinite proof. The literature comparison supports a provisional priority assessment, not independent validation.

## References
1. C. Medgyes, *The inscribed 4-polytope of maximal volume with nine vertices*, arXiv:2611.10078v1, first public 2026-11-06, https://arxiv.org/html/2611.10078v1 (Sections 2.4, 3, 5, 7).
2. C. Medgyes, *The inscribed 4-polytope of maximal volume with ten vertices*, arXiv:2611.14674v1, first public 2026-11-10, https://arxiv.org/html/2611.14674v1.
3. *Sharp cubic deep-hole tails for orthogonal joins of regular spherical polygons*, archived result (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-sharp-cubic-deep-hole-tails-for-orthogonal-joins-of-regular-sphe--3e844f44dce8.
4. *Universal two-level normal-cone angle inversion in orthogonal regular-polygon joins*, archived result (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-universal-two-level-normal-cone-angle-inversion-in-orthogonal-re--0fcd3e8e3622.
5. *Sharp one-third erasure threshold for the Löwner ellipse of a regular polygon*, archived result (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-sharp-one-third-erasure-threshold-for-the-l-wner-ellipse-of-a-re--14b6d47df448.
