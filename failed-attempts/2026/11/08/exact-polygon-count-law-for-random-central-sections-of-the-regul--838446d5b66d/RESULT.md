# Exact polygon-count law for random central sections of the regular truncated tetrahedron

## Finding
Let \(v_0=(1,1,1)\), \(v_1=(1,-1,-1)\), \(v_2=(-1,1,-1)\), and \(v_3=(-1,-1,1)\). Define the regular truncated tetrahedron
\[
K=\operatorname{conv}\left\{\frac{2v_i+v_j}{3}:0\le i,j\le3,\ i\ne j\right\}.
\]
Choose \(u\) uniformly from the unit sphere \(S^2\), and let \(N\) count the vertices of the central planar section \(K\cap u^\perp\). Define the four angles
\[
a=\arccos(1/11),\quad b=\arccos(5/11),\quad
c=\arccos(7/11),\quad d=\arccos(9/11).
\]
Then \(N\in\{4,5,6\}\) almost surely, with **exact** probabilities
\[
\begin{aligned}
\Pr(N=4)&=-3+\frac{12a+6b-12c-6d}{\pi},\\
\Pr(N=5)&=12+\frac{-24a-12b+6c+12d}{\pi},\\
\Pr(N=6)&=-8+\frac{12a+6b+6c-6d}{\pi}.
\end{aligned}
\]
To fifteen decimal places these are \(0.215936085312640\), \(0.520247465238937\), and \(0.263816449448424\), respectively. The first moment has the simpler form
\[
\mathbb E[N]=\frac{18}{\pi}\arccos(7/11)=5.047880364135783\ldots .
\]
These formulas describe uniformly oriented planes constrained to pass through the centroid, **not** isotropically translated cutting planes.

## Assumptions and scope
The polyhedron \(K\) is centered at the origin. The normal \(u\) has normalized spherical area measure; antipodal normals represent the same unoriented plane. Normals orthogonal to one or more vertices of \(K\) are excluded from the generic polygon classification, but form a finite union of great circles of spherical measure zero. All formulas are invariant under rescaling or rotating \(K\).

## Proof
**1. Polyhedron and edges.** Work in the magnified coordinates \(P=3K\) and put \(p_{ij}=2v_i+v_j\) for \(i\ne j\). The original tetrahedron is cut at one third of each of its six edges, and the resulting half-space description is
\[
P=\{x\in\mathbb R^3:-3\le v_i\cdot x\le5\ \text{for }i=0,1,2,3\}.
\]
The twelve \(p_{ij}\) are its vertices. They each lie on three independent supporting planes. Direct enumeration of all triples among the eight facet planes shows that no other feasible vertex exists. Two vertices of this simple polyhedron are adjacent exactly when they share two tight facet planes; hence it has eighteen edges. Every vertex has squared norm \(11\), and every adjacent pair has dot product \(7\). These statements also follow by tracking the twelve triangle edges formed by truncation and the six remnants of the original tetrahedron's edges; an exact rational H-representation enumeration is supplied in the verifier.

**2. From sections to the sphere.** A generic central plane intersects a polyhedron edge \([p,q]\) exactly when \((u\cdot p)(u\cdot q)<0\). It follows that its section has
\[
N(u)=\#\{[p,q]\in E(P):(u\cdot p)(u\cdot q)<0\}
\]
vertices; there are no additional section vertices. The twelve vertex-orthogonality great circles partition \(S^2\) into chambers. At each chamber the twelve signs and \(N\) are constant.

**3. Exact chamber certificate.** Each pair of distinct vertex vectors \(p_i,p_j\) determines two antipodal crossing points \(\pm(p_i\times p_j)/\|p_i\times p_j\|\). Every triple determinant \(\det(p_i,p_j,p_k)\) is nonzero (verified by complete integer enumeration of the \(\binom{12}{3}\) triples). Thus these are \(2\binom{12}{2}=132\) distinct, ordinary four-valent spherical arrangement vertices. Each of twelve great circles is divided into twenty-two arcs, so the spherical arrangement has \(264\) edges and \(134\) chambers by Euler's formula.

An exact finite enumeration of **all** chambers needs no floating-point geometry. For each unordered pair \(i,j\), form both integer rays \(r=\pm(p_i\times p_j)\). The other ten signs \(\operatorname{sgn}(p_k\cdot r)\) are fixed. Adjoin the four choices for the two signs belonging to \(i,j\). These are exactly the four chambers meeting the crossing. Deduplicate twelve-bit sign patterns, and compute their section counts from the eighteen-edge table. This enumerates all \(134\) chambers and gives \(30\), \(72\), and \(32\) chambers of section counts \(4\), \(5\), and \(6\), respectively. Because every chamber is a spherical polygon with at least three vertices, the crossing construction cannot miss a chamber. The standalone program performs all steps with integer arithmetic.

For an arrangement vertex at the intersection of the two bounding great circles, let \(s_i,s_j\in\{-1,1\}\) denote the **inward** hemisphere signs of its chamber. Its interior spherical angle is
\[
\theta=\arccos\left(-\frac{s_i s_j\,p_i\cdot p_j}{11}\right).
\]
The exact enumeration gives the following counts of corner angles \(\theta=\arccos(x/11)\); blank entries are zero:

| Section vertices | \(x=-9\) | \(x=-7\) | \(x=-5\) | \(x=-1\) | \(x=1\) | \(x=5\) | \(x=7\) | \(x=9\) | Total corners | Chambers |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 4 | 24 | 48 | 0 | 0 | 48 | 24 | 0 | 0 | 144 | 30 |
| 5 | 0 | 24 | 48 | 96 | 0 | 0 | 48 | 48 | 264 | 72 |
| 6 | 24 | 0 | 0 | 0 | 48 | 24 | 24 | 0 | 120 | 32 |

**4. Areas and probabilities.** For any convex spherical chamber with \(k\) corners, Gauss–Bonnet (spherical excess) gives area \(\sum\theta-(k-2)\pi\). Summing this identity over all chambers in each section class, the respective numbers of corners minus twice the numbers of chambers are \(84\), \(120\), and \(56\). Substituting the corner table and the identity \(\arccos(-t)=\pi-\arccos(t)\) gives the exact total spherical areas
\[
\begin{aligned}
A_4&=-12\pi+48a+24b-48c-24d,\\
A_5&=48\pi-96a-48b+24c+48d,\\
A_6&=-32\pi+48a+24b+24c-24d.
\end{aligned}
\]
Their sum is \(4\pi\). Uniform spherical orientation therefore yields \(\Pr(N=j)=A_j/(4\pi)\), exactly as stated.

**5. Independent expectation identity.** For any nonzero vectors \(p,q\in\mathbb R^3\), the probability that a Haar-uniform plane separates them is the angle between their rays divided by \(\pi\). Since each of the eighteen edges has endpoint angle \(\arccos(7/11)\), linearity of expectation gives \(\mathbb E[N]=18c/\pi\). This also follows algebraically from the three probabilities and independently checks their coefficients.

## Verification
Execute \`python3 verify_truncated_tetrahedron.py\` in the directory of this document. The program uses only the Python standard library. It independently enumerates every vertex of the eight-halfspace polyhedron using exact rational Cramer's rule, finds its eighteen edges, checks all \(220\) nonzero triple determinants, generates the exact \(134\) sign chambers and \(528\) corner incidences, and reproduces the corner-count table. It also checks the normalized area formulas and the independent mean identity. As a separate non-proof check, \(180000\) seeded random orientations produce all three section types with maximum absolute observed probability error \(0.001849783\). All general mathematical claims follow from the exact enumeration and spherical excess; finite sampling is merely corroborative.

## Relationship to prior work
Jiao and Torquato [1] explicitly construct and study packings of this non-centrally symmetric Archimedean solid, but do not calculate central-section polygon probabilities. Socha [2] treats the distribution of **angles** of sections generated by an isotropic family of affine planes, not polygon-count probabilities for central planes; its article was inspected in full. Voss [3] develops exact polygon-count frequencies for some families of polyhedra under random planar cutting, and is the nearest identifiable historical priority risk. Its full text could not be accessed, so the exact families and possible specializations are not established here. The abstract's random affine-plane model differs from the fixed-through-center orientation law treated here. Ohser and Mücklich [4] discuss stereological inversion and numerical section-profile distributions for prisms, rather than an exact central truncated-tetrahedron polygon law. Searches of the available literature did not identify these three specific exact probabilities; this is not a claim of exhaustively established historical priority.

## Limitations
The result applies only to the **regular** truncated tetrahedron and Haar-uniform central orientations. It does not give a law for randomly translated planes, random section area or perimeter, or deformed/irregular tetrahedra. It does not supply an independent audit or rule out older unavailable exact calculations, especially [3]. No assertion of statistical measurement stability is made.

## References
[1] Y. Jiao and S. Torquato, *Analytical Construction of A Dense Packing of Truncated Tetrahedra*, arXiv:1107.2300, initial public version 2011-07-12; later journal version, *J. Chem. Phys.* 135 (2011), 151101, doi:10.1063/1.3653938. https://arxiv.org/abs/1107.2300

[2] P. Socha, *Random Plane Section of a Polyhedron*, *Acta Stereologica* 7(1) (1988), 41–46. https://www.ias-iss.org/acta/ActaStereologica_pdf/Vol.1.2.5.7.8/VOL%207/NO%201/AS_7_n1_41_SOC.pdf

[3] K. Voss, *Frequencies of n-polygons in planar sections of polyhedrons*, *Journal of Microscopy* 128(2) (1982), 111–120, doi:10.1111/j.1365-2818.1982.tb00443.x. Full text not accessed.

[4] J. Ohser and F. Mücklich, *Stereology for some classes of polyhedrons*, *Advances in Applied Probability* 27(2) (1995), 384–396, doi:10.2307/1427832. Abstract and cited references consulted.
