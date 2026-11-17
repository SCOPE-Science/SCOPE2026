# Two distinct failure–radius crossovers for square-lattice disk coverage

## Finding
Let disks of radius \(R\) be centered at every site of \(\mathbb Z^2\), with each site independently deleted with probability \(q\). Write \(\Phi_R(q)\) for the almost-sure uncovered-area fraction and \(\Lambda_R(q)\) for the almost-sure uncovered-boundary length per unit area. The latter counts the geometric boundary of the union of surviving closed disks, and ignores window edges. Put
\[
c=1-\frac{\sqrt3}{4}-\frac\pi6>0.
\]
For \(\delta=1-R\downarrow0\), the two statistics have **different critical failure scales**: uniformly when \(\lambda\) ranges through compact subsets of \([0,\infty)\),
\[
\lim_{\delta\downarrow0}\frac{\Phi_{1-\delta}(\lambda\delta^2)}{\delta^4}
=4\lambda+4c\lambda^2,
\qquad
\lim_{\delta\downarrow0}\frac{\Lambda_{1-\delta}(\lambda\delta)}{\delta^2}
=8\lambda+\frac{4\pi}{3}\lambda^2.
\]
At the exact critical radius \(R=1\), for every \(0\le q\le1\),
\[
\Phi_1(q)=4cq^2(1-q)^2+4\left(1-\frac\pi4\right)q^3(1-q)+q^4,
\]
\[
\Lambda_1(q)=\frac{4\pi}{3}q^2(1-q)^2+2\pi q^3(1-q).
\]
Thus the area changes from leading linear dependence on \(q\) below the critical radius to quadratic dependence exactly at it, but the crossover is at \(q\asymp(1-R)^2\); perimeter changes on the larger scale \(q\asymp1-R\).

## Assumptions and scope
The lattice spacing is one, the radius lies in \(1/\sqrt2\le R\le1\), closed disks cover the plane at \(q=0\), erasures are independent Bernoulli variables of parameter \(q\), and \(R\) and \(q\) have the joint limits specified above. Area is two-dimensional Lebesgue measure; perimeter is one-dimensional Hausdorff measure. Spatial limits are over expanding square observation windows. All equalities for \(R=1\) hold without small-\(q\) assumptions. No assertion is made about a fixed finite grid's outer boundary or radii outside the stated interval.

## Proof
**1. Localization and existence of densities.** For every point in the interior of an elementary lattice square and \(R\le1\), no center outside its four corners can cover it: its distance to each external lattice site is strictly greater than one. For \(R\ge1/\sqrt2\), those four disks cover the square before erasures. Write \(k_R(x)\in\{1,2,3,4\}\) for the number of its four corners whose disks contain \(x\). Independence implies exactly
\[
\Phi_R(q)=\int_{[0,1]^2}q^{k_R(x)}\,dx=\sum_{j=1}^{4}a_j(R)q^j,
\quad a_j(R)=|\{x\in[0,1]^2:k_R(x)=j\}|.
\]
For the boundary law, consider the circle of one surviving site. For a point \(Re^{i\theta}\), let \(m_R(\theta)\) count **other** lattice centers within distance \(R\). Only finitely many sites contribute for \(R\le1\). A boundary arc is exposed exactly when its own center survives and all these other covering sites fail. Hence the exact finite polynomial
\[
\Lambda_R(q)=(1-q)R\int_0^{2\pi}q^{m_R(\theta)}\,d\theta.
\]
The spatial ergodic theorem for independent lattice erasures gives the almost-sure area and perimeter densities above; truncation to windows introduces only a vanishing boundary-to-area error. Tangencies and circular-arc intersections have zero Hausdorff length.

**2. Geometry at radius one.** For a square whose four corner sites have been deleted in a specified pattern, uncovered area is zero unless precisely two adjacent corners, three corners, or all four corners are deleted. In the adjacent-pair case the uncovered piece is bounded by two radius-one circular arcs and has area
\[
2\int_0^{1/2}\bigl(1-\sqrt{1-u^2}\bigr)\,du
=1-\frac{\sqrt3}{4}-\frac\pi6=c,
\]
with its internal curved boundary length \(\pi/3\). When three corners are deleted, the complement of the surviving quarter unit disk has area \(1-\pi/4\), with internal arc length \(\pi/2\). All four deleted leaves the full square uncovered, with no internal arc. With two deleted opposite corners there is no uncovered region; one deletion also leaves no area uncovered. Every interior arc is counted once; boundaries along lattice-square edges contribute no positive length to the uncovered boundary. The relevant face-pattern probabilities are \(4q^2(1-q)^2\), \(4q^3(1-q)\), and \(q^4\). Summing area and internal arc lengths proves the two exact \(R=1\) polynomials.

**3. First erasure at radius just below one.** With only the origin's disk deleted, denote the uncovered hole by \(H_R\). As \(R\uparrow1\), it shrinks to the origin: the other lattice disks cover the plane at \(R=1\), and the origin is the sole point at which their covering-distance is exactly one. Set \(x=\delta u\), \(\delta=1-R\). For the four nearest surviving sites \(\pm e_1,\pm e_2\), the inequalities \(\|x\mp e_i\|>1-\delta\) become \(\pm u_i<1+O(\delta)\) on bounded sets. All more distant centers are irrelevant in a neighborhood of the origin. These inequalities uniformly trap \(\delta^{-1}H_{1-\delta}\) between squares of side lengths tending to two. Their circular boundaries converge as rectifiable arcs to the four sides of \([-1,1]^2\). Therefore
\[
|H_{1-\delta}|=4\delta^2+o(\delta^2),\qquad
\mathcal H^1(\partial H_{1-\delta})=8\delta+o(\delta).
\]
The coefficient \(a_1(R)\) equals the area of an isolated deleted-site hole per lattice site, so \(a_1(1-\delta)=4\delta^2+o(\delta^2)\). Likewise the coefficient of \(q\) in \(\Lambda_R(q)\), obtained by exposing one erased site's cavity, is \(b_1(1-\delta)=8\delta+o(\delta)\).

**4. Pair failure and continuity.** The \(q^2\) coefficient \(a_2(R)\) is the area of points covered by precisely two disks. Except on finitely many circle arcs of zero area, \(k_R(x)\to k_1(x)\), hence dominated convergence and the radius-one face classification give \(a_2(R)\to4c\). Writing \(\Lambda_R(q)=b_1(R)q+b_2(R)q^2+O(q^3)\) uniformly for \(R\) sufficiently close to one, the circle formula implies
\[
b_1(R)=R|\{\theta:m_R(\theta)=1\}|,
\quad b_2(R)=R\bigl(|\{\theta:m_R(\theta)=2\}|-|\{\theta:m_R(\theta)=1\}|\bigr).
\]
Angular indicator convergence holds almost everywhere as \(R\uparrow1\). At \(R=1\), the angle set with \(m_1=1\) has zero measure; with \(m_1=2\), the four quadrants each contribute two angular intervals of length \(\pi/6\). Thus \(b_2(R)\to4\pi/3\). All higher coefficients are uniformly bounded because they come from a fixed finite number of covering sites. Substituting \(q=\lambda\delta^2\) into the area expansion and \(q=\lambda\delta\) into the perimeter expansion proves both crossover limits. Uniformity in bounded \(\lambda\)-ranges follows from bounded coefficients and the preceding convergence statements.

## Verification
The standalone checker `checker.py` uses direct circular-arc integration for a single missing-site hole, midpoint enumeration of angular covering multiplicities around surviving disks, and planar midpoint enumeration of unit-square covering counts. Its printed sequence confirms isolated-hole area divided by \(\delta^2\) tends to four, the isolated-hole perimeter divided by \(\delta\) tends to eight, and the radius-one quadratic coefficients agree with \(4c\) and \(4\pi/3\). The checker is corroborative; the preceding analytic arguments supply the infinite-limit proof.

## Relationship to prior work
Shakkottai, Srikant and Shroff analyze unreliable square-grid networks, but their results give full-coverage and connectivity scaling rather than the present local uncovered-area and perimeter crossover. Balister and Kumar compare random and lattice deployment reliability using *hole-count intensity*, which is different from either geometric area or boundary-length density. Yan and collaborators analyze homology-based detection of geometric coverage holes, focusing on algorithmic detection and missed-hole area bounds under other deployment models. An earlier triangular-lattice disk-erasure result yields a cubic-failure area law at a distinct fixed lattice geometry; it does not imply the two separate \(q\)-versus-radius windows for the square lattice.

## Limitations
This is an exact mathematical result for an infinite aligned square grid with independent point erasures and identical round disks, not a statement for correlated failures, location jitter, or finite boundary effects. The almost-sure densities require growing windows. The distinguished radii and failure scales cannot be transferred to triangular or random sensor layouts without separate analysis. Historical priority needs independent corroboration; numerical checks are not independent proof.

## References
1. F. Yan, A. Vergne, P. Martins, L. Decreusefond, *Homology-based Distributed Coverage Hole Detection in Wireless Sensor Networks*, arXiv:1302.7289, initially public 2013-02-28.
2. S. Shakkottai, R. Srikant, N. B. Shroff, *Unreliable Sensor Grids: Coverage, Connectivity and Diameter*, *Ad Hoc Networks* 3 (2005), 702–716, DOI:10.1016/j.adhoc.2004.02.001.
3. P. Balister, S. Kumar, *Random vs. Deterministic Deployment of Sensors in the Presence of Failures and Placement Errors*, IEEE INFOCOM (2009), 2896–2900, DOI:10.1109/INFCOM.2009.5062254.
