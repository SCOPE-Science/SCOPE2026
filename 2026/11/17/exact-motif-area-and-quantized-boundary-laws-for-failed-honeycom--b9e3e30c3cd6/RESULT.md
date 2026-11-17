# Exact motif area and quantized boundary laws for failed honeycomb disk coverings

## Finding
In a regular honeycomb graph embedded with nearest-neighbor distance one, closed unit disks at all vertices cover the plane twice or three times almost everywhere. If any **finite** set of disk centers \(S\) is deleted, the area and perimeter of the resulting uncovered open set depend only on the number of deleted edges and length-two paths, not on the embedding details of the deletion pattern. In particular, the uncovered boundary length is an integer multiple of \(2\pi/3\). The same local identities imply exact uncovered-area and exposed-boundary densities under independent Bernoulli failures for every failure probability.

Write \(G\) for the embedded honeycomb graph, \(E=|E(G[S])|\), and
\[ P=\sum_{v\in S}\binom{d_S(v)}2,\qquad d_S(v)=|\{w\in S:vw\in E(G)\}|.\]
Let \(U_S=\mathbb R^2\setminus\bigcup_{v\in V(G)\setminus S}\overline{B}(v,1)\). Then
\[
|U_S|=\left(\frac{3\sqrt3}{2}-\frac{2\pi}{3}\right)E+
\left(\frac\pi3-\frac{\sqrt3}2\right)P,
\qquad
\mathcal H^1(\partial U_S)=\frac{2\pi}{3}(2E-P).
\]
Equivalently, with \(N_j=|\{v\in S:d_S(v)=j\}|\),
\[
\mathcal H^1(\partial U_S)=\frac{2\pi}{3}(N_1+N_2),\qquad
|U_S|+\left(\frac12-\frac{3\sqrt3}{4\pi}\right)\mathcal H^1(\partial U_S)=\frac{\sqrt3}{2}E.
\]
Thus one failed disk or two nonadjacent failures create no uncovered area, whereas deleting both endpoints of an edge creates area \(3\sqrt3/2-2\pi/3\) and perimeter \(4\pi/3\).

For independent site failures with probability \(q\in[0,1]\), the respective almost-sure Euclidean-area and boundary-length densities are
\[
\phi(q)=\left(3-\frac{4\pi}{3\sqrt3}\right)q^2+
\left(\frac{4\pi}{3\sqrt3}-2\right)q^3,
\qquad
\ell(q)=\frac{8\pi}{3\sqrt3}q^2(1-q).
\]

## Assumptions and scope
The honeycomb graph is the one-skeleton of the regular edge-one hexagonal tiling. For example its vertex set can be written
\[\Lambda\cup (\Lambda+(1,0)),\quad \Lambda=\mathbb Z(3/2,\sqrt3/2)+\mathbb Z(3/2,-\sqrt3/2).\]
Only nearest-neighbor graph edges of length one are used. All disks have **radius exactly one**, and finite-deletion formulas use a finite set \(S\). Areas use planar Lebesgue measure and perimeter is \(\mathcal H^1\) of the topological boundary; finitely many isolated tangencies contribute zero length. For Bernoulli deletions, densities are limits inside increasing concentric disks, or an increasing Følner sequence of lattice-period cells, almost surely. No assertion is made for unequal radii or arbitrary irregular networks.

## Proof
**1. The exact initial multiplicities.** Partition the plane into regular hexagonal faces of circumradius one. In a face with center \(o\), the six vertices are at \(o\pm u_1,o\pm u_2,o\pm u_3\), each unit length; every other honeycomb vertex lies at distance at least two from \(o\). Therefore no disk centered outside the six vertices covers a point in the *interior* of that hexagon: for such \(x\), \(|x-o|<1\). Subdivide the face into six triangles joining its center to adjacent vertices. The disk of radius one about either endpoint of any such triangle contains that entire triangle, by convexity and unit-distance checks at its three corners. Thus multiplicity \(M(x)\ge2\) almost everywhere. If vertex \(o+u\) covers \(x\), then \((x-o)\cdot u>|x-o|^2/2\) except on a zero-area boundary. At most one of the antipodal pair \(o\pm u\) can cover \(x\), hence \(M(x)\le3\). Consequently \(M(x)\in\{2,3\}\) almost everywhere.

**2. Cell areas and motif counts.** A honeycomb fundamental area contains two vertices and has area \(3\sqrt3/2\), so vertex density is \(\rho=4/(3\sqrt3)\). Integrating disk multiplicity gives \(\mathbb E_{\rm area}[M]=\rho\pi=4\pi/(3\sqrt3)\). Thus the area fractions covered by exactly two or exactly three disks are
\[f_2=3-\frac{4\pi}{3\sqrt3},\qquad f_3=\frac{4\pi}{3\sqrt3}-2.\]
A pair of disks can simultaneously be the only two covering a positive-area region exactly when their centers are adjacent in \(G\); any triple can be the only covering triple exactly when the three centers form a length-two path. Indeed, inside the nearest hexagon, the covered vertex directions are a contiguous two- or three-vertex arc; the three-vertex arcs are the length-two paths on the honeycomb graph. Conversely each edge or path has a nonempty corresponding region, by symmetry and the above positive fractions. Edges have spatial density \(3\rho/2=2/\sqrt3\) and length-two paths density \(3\rho=4/\sqrt3\). By the transitive symmetries of the honeycomb tiling, all edge regions have the same area \(a_2=f_2/(2/\sqrt3)=3\sqrt3/2-2\pi/3\), and all path regions the same area \(a_3=f_3/(4/\sqrt3)=\pi/3-\sqrt3/2\). Each point is uncovered after finite deletions precisely when **all** of its initially covering centers have been deleted; summing the disjoint two- and three-covering cells yields \(|U_S|=a_2E+a_3P\).

**3. Boundary arcs and quantization.** Each surviving disk center \(v\) has its circumference partitioned, apart from six exceptional angular points, into six open arcs of central angle \(\pi/3\). A point on one arc is covered by precisely two disks other than the disk at \(v\); their centers form one honeycomb edge \(uw\), with \(v,u,w\) forming a length-two path, and no other disk contains that point. This is checked for a single arc by taking \(v=(0,0)\), directions \(0<\theta<\pi/3\) and other centers \(u=(1,0), w=(3/2,\sqrt3/2)\); the other five cases follow by sixfold rotation of the local arc pattern (with the two-sublattice translation and reflection symmetries). The arc belongs to the *uncovered region's boundary* exactly when \(u,w\in S\) but \(v\notin S\). Every deleted edge \(uw\) has four adjacent possible outside-center arcs, one for each third neighbor at either endpoint of the edge. Deleting a third center suppresses precisely one arc for each of the two edges of each resulting length-two deleted path. Hence the total number of exposed arcs is \(4E-2P\); each has length \(\pi/3\). Therefore \(\mathcal H^1(\partial U_S)=\pi(4E-2P)/3\). Since \(2E=\sum_{v\in S}d_S(v)\) and \(2P=\sum_{v\in S}d_S(v)(d_S(v)-1)\),
\[4E-2P=\sum_{v\in S}d_S(v)(3-d_S(v))=2(N_1+N_2),\]
as each graph degree is at most three. Eliminate \(P\) from the area and length formulas to obtain the displayed continuous-discrete identity.

**4. Bernoulli failures.** Under i.i.d. deletion with parameter \(q\), every point in a two-fold cell is uncovered with probability \(q^2\) and every point in a three-fold cell with probability \(q^3\). The stationary ergodic theorem therefore gives \(\phi(q)=f_2q^2+f_3q^3\) almost surely. The expected number of exposed boundary arcs per unit area is the density \(6\rho\) of possible arcs, multiplied by \((1-q)q^2\), since the center of that circle must survive and its two covering neighbors must fail. Multiplying by arc length \(\pi/3\) yields \(\ell(q)=2\pi\rho(1-q)q^2=8\pi q^2(1-q)/(3\sqrt3)\). Bounded finite-range local contributions satisfy the lattice ergodic theorem, including the endpoint values \(q=0,1\).

## Verification
A reproducible Python checker in `verify.py` reconstructs the honeycomb coordinates, compares two- and three-fold coverage fractions against numerical area quadrature, checks the Bernoulli uncovered fraction at four probabilities, and for six different finite deletion sets compares the predicted area and boundary length to independent Sobol quadrature and direct visible-circle-arc sampling. It also verifies the exact algebraic area–perimeter identity. Its successful output ends `HONEYCOMB_ERASURE_AREA_PERIMETER_CHECK_OK 6 finite deletion cases`. Numerical evidence is corroborative only: the proof above establishes the assertions for all finite sets and every failure probability.

## Relationship to prior work
Brown et al. (2007), *Geometric considerations for distribution of sensors in ad-hoc sensor networks*, construct the unit-radius three-disk-overlap honeycomb deployment and prove at least double covering; this **pre-existing deployment and redundancy** are not presented as new. Wang et al. (2015), *Node Placement for Long Bounded Belt Complete 2-Coverage in Wireless Sensor Networks*, independently develops sensor placements and explicitly discusses Brown's honeycomb arrangement. The new claim concerns the exact **arbitrary-erasure area and perimeter graph valuations**, their boundary quantization, and the resulting all-probability independent-failure densities; these are not provided in the inspected articles. Analogous deletion formulas for a triangular Bravais lattice have different minimum failure motifs and do not imply this honeycomb identity. The published research-record comparison likewise found no exact equivalent under the tested aliases, but search absence is not proof of global novelty.

## Limitations
The formulas depend critically on the radius being exactly the honeycomb nearest-neighbor spacing. General radii, inhomogeneous site failures, dependent failures, finite-network border corrections and the topology or number of connected uncovered components are outside the theorem. The historical-priority assessment is provisional: unindexed sensor reliability literature might contain related defect-area formulas. The numerical checker is not an independent mathematical audit.

## References
1. T. Brown, D. Sarioz, A. Bar-Noy, T. LaPorta, D. Verma, M. P. Johnson, H. Rowaihy, *Geometric considerations for distribution of sensors in ad-hoc sensor networks*, Proc. SPIE 6562 (2007), article 65620U, DOI: 10.1117/12.723534. Conference 9–10 April 2007; dated publication record 15 November 2007.
2. T. Wang, Y. Sun, Z. Xu, W. Zhai, R. Zhuo, *Node Placement for Long Bounded Belt Complete 2-Coverage in Wireless Sensor Networks*, Mathematical Problems in Engineering (first published 5 November 2015), article 672768, DOI: 10.1155/2015/672768.
