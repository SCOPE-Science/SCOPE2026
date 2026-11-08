# The exact alternating-island area law for symmetric half-plane rotations

## Finding

For every angle \(0<\alpha<\pi\), consider the bijective piecewise isometry
\[
T_\alpha(z)=e^{i\alpha}\bigl(z-H(z)\bigr),\qquad
H(z)=\begin{cases}1,&\operatorname{Im}z\geq0,\\-1,&\operatorname{Im}z<0.\end{cases}
\]
Set \(\lambda=e^{i\alpha}\), \(c_\alpha=\lambda/(1+\lambda)\), and \(s_\alpha=\operatorname{Im}c_\alpha=\tfrac12\tan(\alpha/2)\). The points \(c_\alpha,-c_\alpha\) form a primitive two-cycle with strict upper/lower itinerary. Let \(U_\alpha\) be the **interior of the set of all points** following this strict alternating itinerary, starting in the upper half-plane. Thus \(U_\alpha\) is the maximal open alternating-itinerary cell containing \(c_\alpha\). Its second member is \(-U_\alpha=T_\alpha(U_\alpha)\).

**Theorem.** If \(\alpha/(2\pi)\) is irrational, \(U_\alpha\) is the open Euclidean disk of radius \(s_\alpha\) centered at \(c_\alpha\). If \(\alpha=2\pi p/q\), with \(p,q\) coprime positive integers and \(0<2p<q\), let
\[
N(p,q)=\operatorname{ord}(-e^{2\pi i p/q})=
\begin{cases}
2q,&q\text{ odd},\\
q,&q\equiv0\pmod4,\\
q/2,&q\equiv2\pmod4.
\end{cases}
\]
Then \(U_\alpha\) is the open regular \(N(p,q)\)-gon of inradius \(s_\alpha\), centered at \(c_\alpha\). The two alternating cells are disjoint, and the exact combined Euclidean area is
\[
\boxed{\mathcal A(\alpha)=\operatorname{area}(U_\alpha\cup -U_\alpha)=
\begin{cases}
2N(p,q)s_\alpha^2\tan(\pi/N(p,q)),&\alpha=2\pi p/q,\\
2\pi s_\alpha^2,&\alpha/(2\pi)\notin\mathbb Q.
\end{cases}}
\]
For rational \(\alpha=2\pi p/q\), the centers have least period \(2\), and every other point in these two open cells has least period \(2q/\gcd(q,2)\). At irrational angles, the centers are the only periodic points inside these cells; every noncentral point has a dense orbit on its corresponding circle under the second iterate.

The **resonant area excess** relative to the disk baseline is
\[
\Delta(\alpha)=\mathcal A(\alpha)-\frac{\pi}{2}\tan^2(\alpha/2).
\]
It equals zero at every irrational angle and is strictly positive at every rational angle. Consequently \(\mathcal A\) and \(\Delta\) are continuous precisely at the irrational values of \(\alpha/(2\pi)\), and discontinuous at every rational value. On any compact subinterval of \((0,\pi)\), rational excesses with \(N\to\infty\) obey the uniform expansion
\[
\Delta(\alpha)=\frac{2\pi^3s_\alpha^2}{3N^2}+O(N^{-4}).
\]
This classifies **one natural two-cell island family**, not the whole regular set or all periodic islands in the plane.

## Assumptions and scope

The half-open convention \(\operatorname{Im}z\geq0\) for the upper branch is fixed. All assertions about the cells and their areas concern open sets and thus exclude branch-switching boundaries. We use planar Lebesgue area without normalization; the ambient plane has infinite measure. The strictly alternating itinerary means \(\operatorname{Im}(T_\alpha^kz)>0\) for even \(k\geq0\) and \(\operatorname{Im}(T_\alpha^kz)<0\) for odd \(k\geq0\). A point on the boundary may or may not have this entire strict itinerary when the angle is irrational; it is **not** part of the maximal open cell. The parameter interval excludes \(\alpha=0,\pi\), where the geometry degenerates or the chosen center formula is undefined.

## Proof

**1. The canonical two-cycle.** Since \(c_\alpha=\lambda/(1+\lambda)=\tfrac12+\tfrac i2\tan(\alpha/2)\), its imaginary part is \(s_\alpha>0\). Direct substitution on the correct branches gives \(T_\alpha(c_\alpha)=-c_\alpha\) and \(T_\alpha(-c_\alpha)=c_\alpha\). The two points are distinct.

**2. Explicit itinerary constraints.** For a perturbation \(w\in\mathbb C\), induction along the alternating branches gives
\[
T_\alpha^k(c_\alpha+w)=(-1)^kc_\alpha+\lambda^kw
\]
whenever all preceding branches alternate. The strict condition at step \(k\) is equivalent to
\[
\boxed{s_\alpha+\operatorname{Im}(( -\lambda)^kw)>0.}\tag{1}
\]
Conversely, if (1) holds for every nonnegative \(k\), the same induction proves that the actual orbit alternates. Thus the set of such perturbations is exactly the intersection of the open half-planes in (1); its interior is convex, contains \(0\), and is the maximal open alternating cell, translated by \(c_\alpha\).

**3. Irrational angles.** If \(\alpha/(2\pi)\) is irrational, the powers of \(-\lambda\) are dense on the unit circle. For every \(|w|<s_\alpha\), all inequalities (1) hold with uniform margin at least \(s_\alpha-|w|\). For every \(|w|>s_\alpha\), density supplies some \(k\) with \(\operatorname{Im}(( -\lambda)^kw)<-s_\alpha\); (1) fails. A point with \(|w|=s_\alpha\) cannot be interior since each neighborhood contains points with larger modulus. The required interior is exactly \(|w|<s_\alpha\).

**4. Rational angles and exact number of facets.** For \(\alpha=2\pi p/q\) in lowest terms, \(-\lambda=e^{2\pi i(2p+q)/(2q)}\) has order \(N=2q/\gcd(2p+q,2q)\). Reduction according to \(q\bmod4\) yields the three displayed cases. In the chosen range \(N\geq3\). The first \(N\) powers of \(-\lambda\) give all the distinct equally spaced normal directions; later inequalities repeat. Thus (1) describes precisely the open regular \(N\)-gon with all sides tangent to the centered circle of radius \(s_\alpha\). Every inequality defines an actual facet, since the equally spaced unit normals are vertices of a convex regular polygon. This proves both the exact facet count and the inradius without a generic-polygon assumption.

**5. Images and least periods.** The perturbation polygon/disk \(V_\alpha=U_\alpha-c_\alpha\) is invariant under multiplication by \(-\lambda\), so \(\lambda V_\alpha=-V_\alpha\). For \(z=c_\alpha+w\in U_\alpha\), its first image is \(-c_\alpha+\lambda w\in -U_\alpha\). Similarly the second image returns into \(U_\alpha\), and \(T_\alpha^2(c_\alpha+w)=c_\alpha+\lambda^2w\). The two cells are disjoint because one lies strictly above and the other strictly below the real axis. Hence return times to the same point are even. For \(w\ne0\), the order of \(\lambda^2\) is \(q/\gcd(q,2)\) in the rational case and infinite in the irrational case. In the irrational case the second-return orbit is dense on the concentric circle of radius \(|w|\).

**6. Areas.** A regular \(N\)-gon of inradius \(s\) has side length \(2s\tan(\pi/N)\), perimeter \(2Ns\tan(\pi/N)\), and area \(Ns^2\tan(\pi/N)\). An open disk of radius \(s\) has area \(\pi s^2\). Since the two open cells are disjoint and congruent, doubling gives the stated exact formula.

**7. Arithmetic discontinuity and asymptotics.** For every finite \(N\geq3\), \(\tan(\pi/N)>\pi/N\), so the excess at any rational angle is positive. At irrational angles it is zero. If distinct reduced rational angles converge to any fixed angle, their denominators tend to infinity, hence \(N\geq q/2\to\infty\). Taylor expansion \(\tan u=u+u^3/3+O(u^5)\) gives
\[
N\tan(\pi/N)-\pi=\frac{\pi^3}{3N^2}+O(N^{-4}).
\]
The factor \(s_\alpha\) is continuous and bounded on compact parameter intervals. It follows that rational excesses vanish when their denominators grow; the function is continuous at irrational parameters. Approaching any rational parameter through irrational parameters gives the disk baseline, strictly below its value there, proving a jump at every rational parameter. This also proves the displayed uniform expansion.

## Verification

The self-contained `verify.py` executes finite computations of the branch-defined map rather than assuming the formula for its dynamics. It tests all 153 reduced rational angles \(2\pi p/q\) with \(3\leq q\leq31\) and \(0<2p<q\), checking explicit two-cycles, order and facet-count arithmetic, sign itineraries for randomized interior/exterior points, the predicted least return period at an off-center interior point, and area identities. It also tests 400 strict interior/exterior cases for one irrational angle. Executing `python3 verify.py` returned `ALTERNATING_ISLAND_CHECK_OK rational_angles=153 rational_interior_samples=21215 irrational_samples=400`. These numerical checks are **not** used to prove density for irrational rotations or universal quantification over angles; those rely on Steps 3, 4, and 7.

## Relationship to prior work

Cima, Gasull, Mañosa and Mañosas [1] defined this half-plane map in the same normalization and proved that, for rational angles, connected components of its regular set are periodic and have convex polygonal boundaries (Theorems A and B). Their bounds distinguish at most \(q\) or \(2q\) sides, and their discussion notes circular cells for irrational rotations. Goetz and Quas [2, Section 2] established the general cell framework and disk-versus-polygon phenomenon, including circle radii controlled by distances from the discontinuity. Cima et al. [3] analyzed the particular angles \(\pi/3\), \(\pi/2\), and \(2\pi/3\), so those individual triangle, square, and hexagon cases are not asserted to be new.

The claim here is narrower in object but stronger quantitatively: for the distinguished alternating two-cycle, it specifies the center, exact full-angle \(q\bmod4\) facet count, exact common inradius, complete two-cell period law, exact area as an arithmetic function of the rotation angle, and a dense rational/irrational discontinuity classification with sharp large-denominator excess. None of [1]–[3] states that complete quantitative all-angle law. General disk/polygon statements and the three classical special cases are credited, not rediscovered. This is an explicit **derived quantitative classification**, not a claim that it is independent of the general theory or that related results cannot exist elsewhere.

## Limitations

The theorem concerns the maximal open strictly alternating two-cell component and its image only; it neither describes other periodic or nonperiodic components nor measures the full periodic set. Boundary points are deliberately excluded. Irrational angles have no periodic noncentral points inside the two cells, but other points of the plane may have periodic orbits. Numerical tests cannot establish irrational density or exclude unpublished exact-area formulas. Relevant older general literature gives many ingredients of the proof, so the publication novelty of the explicit area-discontinuity law remains subject to specialist comparison. No independent mathematical audit has been performed.

## References

[1] A. Cima, A. Gasull, V. Mañosa and F. Mañosas, *On some rational piecewise linear rotations*, arXiv:2306.17543 (first publicly posted 2023-06-30), Sections 1–4. https://arxiv.org/abs/2306.17543

[2] A. Goetz and A. Quas, *Global properties of a family of piecewise isometries*, Ergodic Theory and Dynamical Systems **29** (2009), 545–568, especially Section 2, doi:10.1017/S0143385708080280. Author-posted text: https://www.researchgate.net/publication/243031508_Global_properties_of_a_family_of_piecewise_isometries

[3] A. Cima, A. Gasull, V. Mañosa and F. Mañosas, *Pointwise periodic maps with quantized first integrals*, arXiv:2010.12901, first publicly posted 2020-10-24, especially the angle-specific Sections 2–5. https://arxiv.org/abs/2010.12901
