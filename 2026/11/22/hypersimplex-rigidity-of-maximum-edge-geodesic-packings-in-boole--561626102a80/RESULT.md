# Hypersimplex rigidity of maximum edge-geodesic packings in Boolean cubes

## Finding
For integers \(d\ge 2\) and \(2\le t\le d\), let \(Q_d\) be the Boolean \(d\)-cube, and impose the edge-geodesic capacity \(t\): an edge set is feasible when every shortest path uses at most \(t\) of its edges. Let \(\Theta_i\) denote the class of the \(2^{d-1}\) edges flipping coordinate \(i\). Then **every** maximum-cardinality feasible edge set is
\[
S_I=\bigcup_{i\in I}\Theta_i,\qquad I\subseteq\{1,\ldots,d\},\quad |I|=t.
\]
Thus the (previously established) maximum cardinality is \(t2^{d-1}\), and the **complete new optimizer census** is \(\binom dt\) distinct edge sets.

The structural assertion has a fractional strengthening. Put \(w_e\in[0,1]\) on every edge and require \(\sum_{e\in E(P)}w_e\le t\) for every shortest path \(P\). The entire face maximizing \(\sum_e w_e\) consists exactly of assignments constant on coordinate classes, \(w_e=c_i\) for \(e\in\Theta_i\), where
\[
0\le c_i\le1,\qquad \sum_{i=1}^{d}c_i=t.
\]
Consequently the optimal face is affinely isomorphic to the hypersimplex \(\Delta(d,t)\), and its zero-one vertices are precisely the \(\binom dt\) maximum edge sets above. For \(t=d\) this is the singleton full-edge solution; for \(2\le t<d\) the face has dimension \(d-1\).

## Assumptions and scope
The simple graph \(Q_d\) has vertex set \(\{0,1\}^d\) and an edge between words differing in one coordinate. A geodesic is a shortest vertex-to-vertex path; its edge set is counted without multiplicity. Every geodesic changes each coordinate at most once. The result applies to *all* integer dimensions \(d\ge2\), capacities \(2\le t\le d\), and the specified bounded linear relaxation. In the terminology of edge \(k\)-general position, \(k=t+1\), so the theorem classifies all maximum sets throughout the previously studied range \(3\le k\le d+1\).

## Proof
**1. Sharp all-geodesic upper bound.** Choose a uniform vertex \(v\in\{0,1\}^d\) and a uniform permutation \(\pi\) of the coordinates, and form the antipodal geodesic \(P(v,\pi)\) that flips the bits of \(v\) in the order \(\pi\). Every such path contains \(d\) edges. Each of the \(d2^{d-1}\) cube edges occurs with equal probability by coordinate-permutation and translation symmetries. This probability is
\[
\frac{d}{d2^{d-1}}=2^{1-d}.
\]
For any feasible real weight vector \(w\), linearity of expectation yields
\[
2^{1-d}\sum_e w_e
=\mathbb E\left[\sum_{e\in E(P(v,\pi))}w_e\right]\le t,
\]
so \(\sum_e w_e\le t2^{d-1}\). Choosing \(c_i=1\) on any \(t\) coordinates and zero otherwise attains equality: every geodesic changes each coordinate at most once.

**2. Saturation forces equality on every antipodal path.** If the bound is attained, all values \(\sum_{e\in E(P(v,\pi))}w_e\) are at most \(t\) and have average \(t\). Therefore *every* antipodal geodesic contains total weight exactly \(t\). No limiting or probabilistic approximation is used: this is equality over a finite probability space.

**3. Opposite-square rigidity.** Fix any square obtained by varying coordinates \(i\ne j\) and holding the others fixed. Label the four corners \(00,10,01,11\), and let its edge weights be \(a=w_{00,10}\), \(b=w_{00,01}\), \(c=w_{10,11}\), and \(h=w_{01,11}\). The two two-edge paths \(00\to10\to11\) and \(00\to01\to11\) can be extended by the *same* sequence of flips in the other \(d-2\) coordinates to antipodal geodesics from \(00\). Their total weights are equal by step 2, hence
\[
a+c=b+h.\]
Likewise the two paths \(10\to00\to01\) and \(10\to11\to01\), followed by the same flips in all other coordinates, are antipodal geodesics from \(10\), hence
\[
a+b=c+h.\]
Subtracting shows \(b=c\), and substitution yields \(a=h\). Thus *opposite edges of every square have identical weights*.

**4. Global rigidity.** For a fixed coordinate \(i\), an \(i\)-edge is identified by its other \(d-1\) bits. Any two such identifiers are connected by one-bit flips; each flip passes across a square in coordinates \(i\) and \(j\). Step 3 therefore makes all \(i\)-edge weights equal to some \(c_i\). Every antipodal path contains one edge of each direction, so its saturated weight equals \(\sum_i c_i=t\). The edge bounds give \(0\le c_i\le1\). Conversely, any such \((c_i)\) is feasible because an arbitrary geodesic visits only a subset of coordinates and all \(c_i\) are nonnegative, so its weight is at most \(\sum_i c_i=t\). This proves the entire fractional optimal-face description.

**5. Integrality and enumeration.** If each \(w_e\in\{0,1\}\), then each \(c_i\in\{0,1\}\) and exactly \(t\) coordinates have value one. Distinct choices yield distinct edge sets. Hence precisely \(\binom dt\) integral maxima exist. Since \(\Delta(d,t)\) is the convex hull of these zero-one vectors (its vertices have no two fractional coordinates, by a small opposite-coordinate perturbation), the fractional face statement also follows geometrically. \(\square\)

## Verification
The proof is valid for all specified dimensions and capacities. The accompanying standalone scripts independently reconstruct all relevant shortest paths and check the optimum classification by exhaustive enumeration on \(Q_2,Q_3\) for every admissible \(t\), and by a bounded mixed-integer linear-programming enumeration on \(Q_4\) for \(t=2,3\). The integer program excludes each discovered optimum and terminates with a strictly smaller next-best objective, which certifies completeness of the finite enumeration. The scripts are finite consistency checks, not substitutes for the general proof. Their exact stdout is embedded in `verify/CHECKS.txt`.

## Relationship to prior work
Manuel, Prabha and Klavžar (2021) first established the numerical equality \(\operatorname{gp}_e(Q_d)=2^d\) and the feasibility of unions of two coordinate classes, but their hypercube proof does not classify *every* maximum set. The same authors (2022 preprint; later publication) established the numerical all-capacity formula \(\operatorname{gp}^{(t+1)}_e(Q_d)=t2^{d-1}\) and gave coordinate-class constructions; their stated theorem and proof do not describe the full equality face or enumerate all optima. Klavžar and Tan (2023) study related Fibonacci and Lucas partial cubes and recall the hypercube cardinality. Tian, Klavžar and Tan (2024) study different extremal graph families. An earlier finite four-cube enumeration with six maxima is consistent with \(\binom42=6\) but does not imply the all-dimension and all-capacity rigidity theorem. The result here is the **classification and fractional hypersimplex structure**, not a rediscovery of the known maximum value.

## Limitations
The theorem concerns ordinary unweighted binary hypercubes and a fixed capacity \(t\) between two and \(d\), with the specific box-constrained fractional relaxation. It does not characterize arbitrary edge-general-position sets, nonoptimal facets, other partial cubes, or alternative weighted geodesic inequalities. Literature-search incompleteness can affect historical-priority assessment; the mathematical proof is self-contained and no independent external validation is claimed.

## References
1. P. Manuel, R. Prabha and S. Klavžar, *Edge General Position Problem* (first public preprint 2021-05-10), arXiv:2105.04292, https://arxiv.org/html/2105.04292v1, Section 3, Theorem 3.2.
2. P. Manuel, R. Prabha and S. Klavžar, *Generalization of Edge General Position Problem* (first public preprint 2022-07-15), arXiv:2207.07357, https://arxiv.org/html/2207.07357v1, Section 4, Theorem 4.2.
3. S. Klavžar and E. Tan, *Edge General Position Sets in Fibonacci and Lucas Cubes*, Bull. Malays. Math. Sci. Soc. 46 (2023), article 120, https://doi.org/10.1007/s40840-023-01517-y.
4. J. Tian, S. Klavžar and E. Tan, *Extremal Edge General Position Sets in Some Graphs*, Graphs Combin. 40 (2024), article 40, https://doi.org/10.1007/s00373-024-02770-z.
