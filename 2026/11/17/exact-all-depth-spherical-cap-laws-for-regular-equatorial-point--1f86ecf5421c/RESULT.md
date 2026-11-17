# Exact all-depth spherical-cap laws for regular equatorial point sets

## Finding

Fix an integer \(n\ge3\) and equally spaced unit vectors
\[
 v_j=(\cos(2\pi j/n),\sin(2\pi j/n),0),\qquad 0\le j<n.
\]
For a spherical-area-uniform point \(X\in S^2\), let \(K_r(X)\) count those \(v_j\) within geodesic angular distance \(r\in[0,\pi]\) of \(X\). The **entire multiplicity distribution** \(p_k(r)=\Pr(K_r=k)\), for every integer \(0\le k\le n\) and every radius, is given by the following finite elementary formula.

For \(0<r<\pi/2\), put \(\alpha=\pi/n\), \(c=\cos r\), \(s=\sin r\), and define
\[
 z_j(r)=\begin{cases}
 \sqrt{1-c^2/\cos^2(j\alpha)},&j\alpha<r,\\
 0,&j\alpha\ge r
 \end{cases}\qquad(j=0,1,\ldots,n).
\]
Define the continuous elementary function
\[
 B_r(z)=\arctan\!\left(\frac{cz}{\sqrt{s^2-z^2}}\right)
 -c\arcsin(z/s),\quad 0\le z<s,
 \qquad B_r(s)=\frac\pi2(1-c).
\]
All inverse trigonometric functions take their principal values. The **exact at-least-\(k\) depth probabilities** are
\[
 \boxed{\quad T_k(r):=\Pr(K_r\ge k)
 =\frac{B_r(z_{k-1}(r))-B_r(z_k(r))}{\alpha}
 \quad(1\le k\le n).\quad}
\]
With \(T_0=1\) and \(T_{n+1}=0\), all exact multiplicity probabilities are
\[
 \boxed{p_k(r)=T_k(r)-T_{k+1}(r),\qquad 0\le k\le n.}
\]
The endpoint laws are \(p_0(0)=1\), \(p_n(\pi)=1\). At the hemisphere radius the complete distribution collapses to a **parity dichotomy**:
\[
 K_{\pi/2}=\begin{cases}
 n/2&\text{almost surely, if \(n\) is even},\\
 (n-1)/2\text{ or }(n+1)/2&\text{each with probability \(1/2\), if \(n\) is odd}.
 \end{cases}
\]
For \(\pi/2<r<\pi\) the exact complementary law is
\[
 \boxed{p_k(r)=p_{n-k}(\pi-r).}
\]

There is a **complete hierarchy of sharp higher-depth contact thresholds**. For every integer \(2\le k\le\lceil n/2\rceil\), positive area with coverage multiplicity at least \(k\) first appears at
\[
 r_k=\frac{(k-1)\pi}{n},
 \qquad T_k(r)=0\ \text{for }0\le r\le r_k,
\]
and it has the exact onset
\[
 \boxed{
 T_k(r_k+\varepsilon)=p_k(r_k+\varepsilon)
 =\frac{2n}{3\pi}\sqrt{2\tan r_k}\,\varepsilon^{3/2}
 +O_n(\varepsilon^{5/2})
 \quad(\varepsilon\downarrow0).
 }
\]
At the opposite, near-hemispherical end, the uncovered fraction has the **quadratic closing law**
\[
 \boxed{p_0(\pi/2-\varepsilon)
 =\frac{n}{2\pi}\tan\!\left(\frac\pi n\right)\varepsilon^2
 +O_n(\varepsilon^4).}
\]
Thus the number and location of all positive-area depth phases, their \(3/2\)-power openings, and the quadratic closing of the uncovered polar gaps are explicit for every cardinality.

## Assumptions and scope

The sphere is the unit two-sphere in Euclidean three-space, equipped with area measure normalized to one. The sites are exactly the equatorial regular \(n\)-gon. The result concerns the distribution of the number of equal closed spherical caps containing a uniform observation point, **not** an optimization over arbitrary site locations. Cap boundaries have zero area, so open-cap conventions lead to the same probabilities. The asymptotic error constants fix the integer \(n\). In the contact expansion, \(\varepsilon\) is sufficiently small that no subsequent depth threshold has been crossed.

## Proof

**1. Conditional longitude lattice.** Parameterize a uniformly chosen spherical point as
\[
 X=(\sqrt{1-z^2}\cos\phi,\sqrt{1-z^2}\sin\phi,z),
 \qquad z\sim\operatorname{Unif}[-1,1],\quad \phi\sim\operatorname{Unif}[0,2\pi),
\]
independently. For \(0<r<\pi/2\), a cap centered at azimuth \(2j\alpha\) covers \(X\) precisely when
\[
 \sqrt{1-z^2}\cos(\phi-2j\alpha)\ge\cos r.
\]
For \(|z|\ge s\) no cap contains \(X\), up to null boundaries. For \(|z|<s\), each cap covers an azimuthal arc of halfwidth
\[
 L_r(z)=\arccos\left(\frac{c}{\sqrt{1-z^2}}\right),\qquad 0<L_r(z)\le r.
\]
The centers form a uniform circular lattice of spacing \(2\alpha\). For a uniform azimuth, the number of lattice-centered arcs of halfwidth \(L\) covering it is either \(\lfloor L/\alpha\rfloor\) or \(\lceil L/\alpha\rceil\), with interpolation determined by the fractional part. Consequently, **for every integer \(k\ge1\)** the conditional probability of at least \(k\) memberships is exactly
\[
 \Pr(K_r\ge k\mid z)
 =\max\left\{0,\min\left\{1,\frac{L_r(z)}\alpha-k+1\right\}\right\}.
\]
No independence assumption between the caps is used.

**2. Integrating each depth tail.** The function \(L_r(z)\) decreases strictly for \(z\in(0,s)\). Its level \(L_r(z)=j\alpha\) is attained at \(z=z_j(r)\), whenever \(j\alpha<r\). By symmetry in the two hemispheres and the uniform distribution of \(z\),
\[
 T_k(r)=z_k+\frac1\alpha\int_{z_k}^{z_{k-1}}
 \bigl(L_r(z)-(k-1)\alpha\bigr)\,dz.
\]
This also holds when one or both endpoints vanish. A direct differentiation shows
\[
 \frac{d}{dz}\bigl(z L_r(z)+B_r(z)\bigr)=L_r(z),
\]
using \(L'_r(z)=-cz/((1-z^2)\sqrt{s^2-z^2})\). Since \(L_r(z_j)=j\alpha\) when \(z_j>0\), the endpoint terms cancel, leaving exactly
\(T_k=[B_r(z_{k-1})-B_r(z_k)]/\alpha\). Differences of successive tails give the whole distribution, including zero coverage.

**3. Higher-depth contact and its coefficient.** Fix \(k\ge2\) with \(r_k=(k-1)\alpha<\pi/2\). If \(r\le r_k\), the largest azimuthal halfwidth satisfies \(L_r(z)\le r\le r_k\), hence the clipped conditional probability for depth \(k\) is zero everywhere. For \(r=r_k+\varepsilon\) and small \(\varepsilon>0\), depth \(k+1\) remains impossible. Uniformly in the active boundary layer \(|z|=O(\sqrt\varepsilon)\), expansion of the defining arccosine gives
\[
 L_{r_k+\varepsilon}(z)
 =r_k+\varepsilon-\tfrac12\cot(r_k)z^2
 +O_n(\varepsilon^2+\varepsilon z^2+z^4).
\]
Thus the active latitude extends to
\(z=\sqrt{2\tan(r_k)\varepsilon}\,(1+O_n(\varepsilon))\).
Integrating the truncated parabola and using the evenness of the spherical area density gives
\[
 T_k=\frac1\alpha\int_0^{\sqrt{2\tan(r_k)\varepsilon}}
 \left(\varepsilon-\tfrac12\cot(r_k)z^2\right)dz
 +O_n(\varepsilon^{5/2})
 =\frac{2}{3\alpha}\sqrt{2\tan(r_k)}\varepsilon^{3/2}
 +O_n(\varepsilon^{5/2}).
\]
Since \(T_{k+1}=0\) in this neighborhood, this is also the probability of exactly \(k\) memberships. The coefficient is strictly positive.

**4. Hemisphere, antipodal duality, and uncovered polar gaps.** At \(r=\pi/2\), the azimuthal arcs have halfwidth \(\pi/2\) for every nonpolar point. Consequently the depth equals \(n/2\) a.e. when \(n\) is even, while for odd \(n\) it alternates between the adjacent integers on equal angular fractions. For every site \(v_j\), a point is inside its radius-\(r\) cap if and only if it is outside (up to boundary) the radius-\((\pi-r)\) cap centered at \(-v_j\). The antipodal sites form a rotation of the original regular \(n\)-gon, giving the complementary distribution.

For \(r=\pi/2-\varepsilon\) and the uncovered probability \(p_0=1-T_1\), the first-tail formula above can equivalently be written
\[
 T_1=\frac1\alpha\int_0^\alpha
 \sqrt{1-\cos^2r\sec^2t}\,dt
 \quad\text{when }r>\alpha.
\]
As \(n\ge3\), \(\alpha<\pi/2\), and the integrand has the uniform expansion
\(1-\tfrac12\varepsilon^2\sec^2t+O_n(\varepsilon^4)\).
Since \(\int_0^\alpha\sec^2t\,dt=\tan\alpha\), this proves the quadratic uncovered-area law.

## Verification

The accompanying self-contained Python 3 program `verify.py` compares the elementary tail formula to an independently numerically integrated conditional-longitude formula across multiple cardinalities, radii, and depth values. It separately enumerates dot-product cap memberships on deterministic equal-area latitude-azimuth grids, checks probability normalization and the expected depth \(n(1-\cos r)/2\), checks parity at the hemisphere, and compares sharp onset coefficients at two small scales. The actual extracted verifier prints `ALL_CHECKS_PASSED 490`. Finite calculations corroborate but do not replace the preceding exact derivation.

## Relationship to prior work

Litvak, Sonnleitner and Szczepanski study minimal spherical-cap dispersion and covering radii; they do not supply the complete local membership-depth distribution for a fixed equatorial regular \(n\)-gon. Existing exact multiplicity formulas for four **tetrahedral** cap centers concern a different noncoplanar configuration and do not imply the arbitrary-\(n\) equatorial law. A circular-disk union theorem shows that equal angular spacing maximizes **union area** for planar disks with circle-constrained centers, even under radial weights. By stereographic projection, this informs the depth-zero coverage problem for equatorial caps but does not furnish the higher depth tails, the complete distribution, or the infinitely many cardinality-dependent contact coefficients here. The elementary angular-lattice two-level observation is used as an ingredient and is not claimed as independently novel. The novelty claim is restricted to the full all-depth elementary law and its complete threshold hierarchy.

## Limitations

The site set must be exactly an equatorial regular \(n\)-gon; arbitrary latitudes, multiple rings, unequal radii, and random-site distributions are not treated. This is not a sharp covering arrangement among arbitrary spherical configurations. The depth-zero and first-pair-contact phenomena are closely related to established circular disk coverage and lens geometry. Full mathematical priority against every possible older source remains unverified; the most relevant available texts and published records were compared. No independent validation is asserted.

## References

1. A. E. Litvak, M. Sonnleitner, and T. Szczepanski, *Minimal dispersion on the sphere*, arXiv:2505.10929, first public 2025-05-16. https://arxiv.org/abs/2505.10929
2. *Sharp packing-to-rigidity transition for unions of circularly placed congruent disks*, published mathematical result, 2026-11-01, identifier `40eb6dde4fff`, https://github.com/published-finding corpus/2026
3. *Exact coverage multiplicities and dual contact exponents of tetrahedral spherical caps*, published mathematical result, 2026-10-25, identifier `b1ad9ef47248`, https://github.com/published-finding corpus/2026
4. H. Maehara, *A threshold for the size of random caps to cover a sphere*, Ann. Inst. Stat. Math. 40 (1988), 665–670, https://doi.org/10.1007/BF00049424 (random cap model, not the deterministic depth law).
