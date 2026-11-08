# Exact reciprocal-pair density and its sharp reflex-angle onset in Poisson directional nearest-neighbor graphs

## Finding

Fix a planar angular sector of aperture \(\alpha\in(0,2\pi]\), and join each vertex of a homogeneous Poisson point process to its Euclidean nearest neighbor lying in that sector. A *reciprocal pair* consists of vertices whose two directed nearest-neighbor arrows point to each other. Write \(p(\alpha)\) for the Palm probability that a typical vertex belongs to a reciprocal pair.

**Theorem.** The reciprocal-pair probability has a sharp onset at the half-plane aperture:

\[
p(\alpha)=0\quad(0<\alpha\le\pi),\qquad
p(\pi+\varepsilon)\sim \frac{\varepsilon}{2\pi/3+\sqrt3/4}
\quad(\varepsilon\downarrow0).
\]

For \(\pi<\alpha\le2\pi\), the entire density is given by the exact one-dimensional geometric quadrature

\[
p(\alpha)=\int_{\pi-\alpha/2}^{\alpha/2}\frac{d\theta}{U_\alpha(\theta)},
\quad
U_\alpha(\theta)=\operatorname{area}\bigl(A_\alpha\cup(v_\theta+A_\alpha)\bigr),
\]

where \(v_\theta=(\cos\theta,\sin\theta)\), and \(A_\alpha=\{z\in\mathbb R^2:0<|z|<1,\ |\operatorname{Arg}z|<\alpha/2\}\). In particular, the onset slope is \(0.3956623059818\ldots\). At the full-plane endpoint the formula agrees with the classical unrestricted-neighbor value:

\[
p(2\pi)=\frac{\pi}{4\pi/3+\sqrt3/2}=0.6215048968874\ldots.
\]

The same \(p(\alpha)\) is the thermodynamic limit of the fraction of vertices in directed two-cycles: for a Poisson process of intensity \(\lambda\) on the unit square, if \(N_\lambda\) is its vertex count and \(R_\lambda\) counts vertices in reciprocal pairs, then

\[
\frac{R_\lambda}{\max\{1,N_\lambda\}}\longrightarrow p(\alpha)
\qquad\text{in }L^2\text{ as }\lambda\to\infty.
\]

## Assumptions and scope

An angular sector is used in the literal sense of an arc of directions, including a *reflex sector* when \(\alpha>\pi\); it need not be a convex cone. Fix the sector with central ray along the positive first coordinate axis; rotational invariance makes the choice immaterial. On an infinite planar Poisson process of any positive intensity every vertex has a unique nearest eligible neighbor almost surely. The Palm probability is the probability after adding a distinguished vertex at the origin. For finite samples, a vertex with no eligible neighbor sends no arrow. The parameter \(\alpha\) is fixed before letting \(\lambda\to\infty\), and the limit \(\alpha\downarrow\pi\) is taken separately afterward. Sector boundaries and ties have probability zero, so open or closed conventions yield the same assertions.

## Proof

**1. Palm two-point calculation.** Under the Palm law at the origin, let \(y=r v_\theta\) be the proposed reciprocal neighbor. Both arrows are directionally eligible exactly when \(v_\theta\) and \(-v_\theta\) belong to the permitted sector. For such a candidate, reciprocity is equivalent to absence of all *other* Poisson points in the exclusion set

\[
E_{r,\theta}=(rA_\alpha)\cup(y+rA_\alpha).
\]

The two marked vertices lie only on the radial boundary of these exclusion sets, so they do not invalidate the void condition. By Euclidean scaling, \(\operatorname{area}(E_{r,\theta})=r^2U_\alpha(\theta)\). The Slivnyak–Mecke identity and the unit-intensity Poisson void probability give

\[
p(\alpha)=\int_{\Theta_\alpha}\int_0^\infty
 r e^{-r^2U_\alpha(\theta)}\,dr\,d\theta
=\frac12\int_{\Theta_\alpha}\frac{d\theta}{U_\alpha(\theta)},
\]

where \(\Theta_\alpha\) is the set of eligible reciprocal directions. This calculation counts each typical vertex exactly once: every vertex has at most one outgoing neighbor.

For \(\alpha\le\pi\), opposite directions cannot both lie in the sector except on a null boundary, hence \(\Theta_\alpha\) has zero angular measure. For \(\alpha>\pi\), \(\Theta_\alpha\) consists of two arcs of equal length \(\alpha-\pi\), one at positive and the other at negative near-vertical angles. Their respective positive-angle arc is \([\pi-\alpha/2,\alpha/2]\). Reflection across the horizontal axis sends the two arcs to one another without changing \(U_\alpha\). Consequently the preceding integral becomes the displayed exact single-interval quadrature. Notice \(U_\alpha(\theta)\ge\alpha/2>0\), so all integrals are finite.

**2. Endpoint singularity.** Put \(\alpha=\pi+\varepsilon\). The quadrature interval is \([\pi/2-\varepsilon/2,\pi/2+\varepsilon/2]\). Bounded convergence of sector indicators away from their boundary rays, followed by dominated convergence for planar area, shows that \(U_\alpha(\theta)\) tends uniformly on this shrinking interval to \(U_\pi(\pi/2)\). At the limit the two exclusion sets are right half-discs of unit radius whose centers are unit distance apart vertically. The area common to the full discs is \(2\pi/3-\sqrt3/2\); symmetry across the vertical line halves this lens in the right half-plane. Hence

\[
U_\pi(\pi/2)=\pi-\frac12\left(\frac{2\pi}{3}-\frac{\sqrt3}{2}\right)
=\frac{2\pi}{3}+\frac{\sqrt3}{4}.
\]

The mean-value estimate for a continuous integrand on an interval of length \(\varepsilon\) yields the claimed positive, finite onset slope. When \(\alpha=2\pi\), both exclusion sets are entire unit discs; their union has area \(4\pi/3+\sqrt3/2\), independent of \(\theta\), giving the displayed classical endpoint.

**3. Empirical law.** Rescale the intensity-\(\lambda\) unit-square process by \(\sqrt\lambda\), obtaining unit intensity on a square of side \(L=\sqrt\lambda\). Let \(\xi(x)\) indicate reciprocity of a vertex \(x\). For fixed \(T>0\), define \(\xi_T(x)\) to be \(\xi(x)\) when the nearest eligible neighbor is at distance at most \(T\), and zero otherwise. The value \(\xi_T(x)\) is determined solely by the points within distance \(2T\) of \(x\): the first arrow is settled inside radius \(T\), and whether the destination points back is decided by its closer eligible candidates, all inside radius \(2T\) of \(x\). Restrict to vertices at distance greater than \(2T\) from the square boundary.

The sum of these truncated interior scores has variance \(O_T(L^2)\): apply the one- and two-point Mecke identities, and observe that, for two inserted vertices separated by more than \(4T\), their local score regions are disjoint and their two-point covariance vanishes. Its mean per unit area converges to the full-plane Palm mean \(p_T=\mathbb E^0\xi_T(0)\). For the infinite-plane process, the nearest eligible distance \(D\) satisfies exactly

\[
\Pr^0(D>T)=\exp(-\alpha T^2/2),
\]

because the eligible sector within radius \(T\) has area \(\alpha T^2/2\). Thus \(0\le p(\alpha)-p_T\le e^{-\alpha T^2/2}\). The expected boundary strip vertex count is \(O(TL)\), while interior contributions omitted by truncation have mean at most \(L^2e^{-\alpha T^2/2}\). First let \(L\to\infty\) and then \(T\to\infty\): the original reciprocal-vertex count divided by \(L^2\) converges in probability to \(p(\alpha)\). Independently, \(N_\lambda/\lambda\to1\) in probability. Hence \(R_\lambda/\max(1,N_\lambda)\to p(\alpha)\) in probability. Since this ratio is bounded between zero and one, its convergence also holds in \(L^2\).

## Verification

The standalone `verify.py` evaluates sector-union areas using high-resolution polygon geometry, performs numerical quadrature, checks both exact endpoint formulas and the half-plane-lens identity, verifies geometric reflection symmetry, and compares against a seeded finite point-cloud diagnostic. It completed 40 finite assertions using Python with NumPy, SciPy and Shapely. Representative calculations are \(p(3\pi/2)\approx0.39892694\) and the half-plane onset coefficient \(0.39566230598\). The finite point-cloud comparisons are diagnostics only; the Palm and local-score arguments above prove the infinite assertions.

## Relationship to prior work

Georgiou, Tawhari and Wade (2026, arXiv:2610.40140v1) define the directional nearest-neighbor model for apertures strictly below \(\pi\) and expressly identify reflex apertures \((\pi,2\pi)\) as a natural extension in Section 1.4. Their results address fluctuations of total edge length, not reciprocal directed pairs. The full-plane mutual-nearest-neighbor density is classical; it is treated in Rohrmann and Zurbriggen (2011, arXiv:1109.6664), whose Section V.4 credits earlier exact calculations by Dacey and Cox. Its specialization at \(\alpha=2\pi\) is included here only as a consistency check, not a new result. Generic Poisson stabilization theory supplies broad methods for spatial local-score limits, but does not evaluate this reflex-sector reciprocal-pair density or its sharp aperture coefficient. The contribution is the exact reflex-sector formula, the positive threshold slope and their empirical interpretation.

## Limitations

The theorem concerns homogeneous planar Poisson inputs, a fixed sector orientation, and fixed aperture in the large-intensity limit. It does not address total edge-length central limit laws for reflex sectors, rate of convergence of empirical frequencies, joint fluctuations, non-Poisson inputs, or uniformity when the aperture depends on intensity. The exact intermediate-aperture density is given as a geometric quadrature rather than an elementary closed form. Literature comparisons are not an exhaustive historical-priority certificate.

## References

1. N. Georgiou, Q. M. Tawhari, and A. Wade, *Gaussian and non-Gaussian limits for the total edge-length of random directional nearest-neighbour graphs*, arXiv:2610.40140v1 (first submitted 29 October 2026). https://arxiv.org/html/2610.40140v1
2. R. D. Rohrmann and E. Zurbriggen, *Conditional pair distributions in many-body systems: Exact results for Poisson ensembles*, arXiv:1109.6664 (first submitted 29 September 2011), especially Sections IV–V. https://arxiv.org/abs/1109.6664
3. T. F. Cox, *Nearest neighbours to nearest neighbours*, *Statistics & Probability Letters* **1** (1983), 161–166. https://ideas.repec.org/a/eee/stapro/v1y1983i4p161-166.html
4. M. D. Penrose and A. R. Wade, *Multivariate normal approximation in geometric probability*, *Journal of Statistical Theory and Practice* **2** (2008), 293–326. https://strathprints.strath.ac.uk/13397/
