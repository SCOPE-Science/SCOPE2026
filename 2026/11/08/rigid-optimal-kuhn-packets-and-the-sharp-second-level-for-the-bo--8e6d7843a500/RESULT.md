# Rigid optimal Kuhn packets and the sharp second level for the body-centered cubic lattice

## Finding

Let \(\Lambda=\mathbb Z^3\cup(\mathbb Z^3+(1/2,1/2,1/2))\) and \(B_2^3\) be the Euclidean unit ball. For every ordered linearly independent triple \(B=(b_1,b_2,b_3)\) in \(\Lambda\), let
\[
\Delta_\sigma(B)=\operatorname{conv}\{0,b_{\sigma(1)},b_{\sigma(1)}+b_{\sigma(2)},b_1+b_2+b_3\},
\qquad
\kappa_B=\max_{\sigma\in S_3}\min_{c\in\mathbb R^3}\max_{x\in\Delta_\sigma(B)}\|x-c\|_2.
\]
This uses separate fitting-ball centers for different permutation simplices, but the same three lattice vectors. Set \(\kappa(B_2^3,\Lambda)=\inf_B\kappa_B\). Define the two tetrahedral half-diagonal sets
\[
H_\pm=\left\{\tfrac12(\varepsilon_1,\varepsilon_2,\varepsilon_3):\varepsilon_i\in\{-1,1\},\ \varepsilon_1\varepsilon_2\varepsilon_3=\pm1\right\}.
\]
**Complete first-two-level theorem.**

1. \(\kappa(B_2^3,\Lambda)=\sqrt5/4\).
2. An unordered independent triple is optimal if and only if it is any three of the four points of \(H_+\), or any three of the four points of \(H_-\). There are exactly eight unordered optimal frames (48 ordered frames), all lattice bases.
3. Every other independent frame satisfies \(\kappa_B\ge1/\sqrt2\), and this bound is attained. Thus the next possible packet radius after the optimal level is exactly \(1/\sqrt2\), with a nonzero gap \(1/\sqrt2-\sqrt5/4\).

## Assumptions and scope

All norms, distances, and minimizing balls are Euclidean. Lattice vectors may form a proper sublattice; no primitivity or basis assumption is imposed on admissible frames. Frame vectors must be linearly independent; permutations are those of the same three vectors. A fitting ball need contain only the given simplex, not the union of all six simplices. All cardinalities count actual lattice-vector triples, without dividing by rotations or reflections. An unordered triple is identified up to permutation but not simultaneous sign reversal.

## Proof

**1. The shortest possible subset-sum shell.** Every nonzero vector of \(\Lambda\) is either integral or has three half-odd-integral coordinates. Consequently, the nonzero vectors of squared length strictly below \(2\) form the fourteen-element set
\[
S=\{\pm e_1,\pm e_2,\pm e_3\}\ \cup\
\left\{\tfrac12(\varepsilon_1,\varepsilon_2,\varepsilon_3):\varepsilon_i=\pm1\right\}.
\]
The next possible squared length is \(2\). For any independent frame \(B\), each nonempty subset sum \(\sum_{i\in I}b_i\) joins two vertices in some permutation simplex. Since two points of a radius-\(r\) ball have distance at most \(2r\),
\[
\kappa_B<1/\sqrt2\quad\Longrightarrow\quad
\sum_{i\in I}b_i\in S\quad\text{for every nonempty }I\subseteq\{1,2,3\}.
\]
The same conclusion holds with \(\kappa_B\le\sqrt5/4\), because \(2\sqrt5/4<\sqrt2\).

**2. Classifying the shell-compatible frames.** Suppose every nonempty subset sum lies in \(S\). If a frame contains an axial vector, change coordinate signs and labels to write it as \(e_1\). A second independent axial vector has a pair sum of norm \(\sqrt2\), which is not in \(S\); the other two vectors must therefore be half diagonals with first coordinate \(-1/2\). Their own pair sum belongs to \(S\) and has first coordinate \(-1\). Since the only integral vector in \(S\) with that first coordinate is \(-e_1\), they sum to \(-e_1\), contradicting independence of the frame. Thus all three vectors are half diagonals.

Two half diagonals have sum in \(S\) exactly when their sign triples differ in two coordinates. Therefore all three sign triples have the same parity \(\varepsilon_1\varepsilon_2\varepsilon_3\), and are three distinct points of one four-point set \(H_+\) or \(H_-\). Conversely, every three distinct points of either set have all nonempty subset sums in \(S\). This proves there are precisely \(2\binom43=8\) shell-compatible unordered independent triples. Their pairwise inner products are \(-1/4\), each squared norm is \(3/4\), and their determinants have absolute value \(1/2=\det\Lambda\); hence they are lattice bases.

**3. The exact first level.** For any one of the eight triples and any permutation \((a,b,c)\), the corresponding simplex has vertices \(0,a,a+b,a+b+c\). The preceding Gram identities imply that its centroid
\[
g=(3a+2b+c)/4
\]
is at squared distance \(5/16\) from all four vertices. The ball centered at \(g\) of radius \(\sqrt5/4\) therefore contains the simplex. Conversely, for any candidate center \(z\), the average squared distance of the four vertices from \(z\) equals \(5/16+\|z-g\|_2^2\), so every fitting ball has radius at least \(\sqrt5/4\). Every one of the eight frames thus has packet radius exactly \(\sqrt5/4\).

If any frame had smaller packet radius, Step 1 would put all its subset sums in \(S\), Step 2 would place it among those eight frames, and the preceding paragraph would contradict the strict inequality. This proves the global minimum and its complete optimizer classification.

**4. Sharp isolation of the first level.** If \(\kappa_B<1/\sqrt2\), Steps 1 and 2 force \(B\) to be one of the eight optimal frames. Every nonoptimal independent triple therefore has radius at least \(1/\sqrt2\). To prove sharpness, take the ordered frame
\[
u=-e_1,\qquad v=-e_2,\qquad w=\tfrac12(e_1+e_2-e_3).
\]
It is independent, with determinant of absolute value \(1/2\), but is not one of the eight optimal triples. The pair sum \(u+v\) has length \(\sqrt2\), so \(\kappa_{(u,v,w)}\ge1/\sqrt2\). For the six permutation orders, the following centers enclose the four simplex vertices in balls of squared radius at most \(1/2\):

| Order | Fitting center |
| --- | --- |
| \((u,v,w)\), \((v,u,w)\) | \((-1/2,-1/2,0)\) |
| \((u,w,v)\) | \((-1/2,0,-1/4)\) |
| \((v,w,u)\) | \((0,-1/2,-1/4)\) |
| \((w,u,v)\), \((w,v,u)\) | \((0,0,-1/2)\) |

Direct substitution into the four vertex-distance inequalities verifies the table. Hence \(\kappa_{(u,v,w)}=1/\sqrt2\), completing the theorem.

## Verification

The dependency-free `checker.py` uses exact rational arithmetic to enumerate the 14 short vectors, the 232 independent unordered triples of short vectors, and the eight shell-compatible triples. It verifies all 48 optimal packet simplices have centroid squared radius \(5/16\), and checks all six explicitly displayed second-level balls against their four vertices. Run `python3 checker.py`. The finite enumeration serves as a reproducible cross-check of the analytic shell classification, not as a replacement for the infinite-frame proof.

## Relationship to prior work

Fei Xue introduced the \(\kappa\)-covering minimum in arXiv:2610.39034 (first submitted 2026-10-28), establishing its relation to classical covering radius and the exact equality in planar lattice quotients. Those statements do not determine all optimizing frames or the first nonoptimal radius of the three-dimensional body-centered cubic lattice. The established Voronoi–Delaunay geometry of this lattice (for example, Koca et al., arXiv:1804.05836, Section 5) describes its truncated-octahedral Voronoi cell and fundamental simplices. It supplies the natural geometric setting, but the assertion here concerns optimization over **every independent lattice triple** and a sharp positive separation from all nonoptimal triples.

## Limitations

The result is restricted to the stated standard Euclidean body-centered cubic lattice. It does not establish equality between \(\kappa\) and classical covering radius for arbitrary three-dimensional lattices, or any general quantitative stability inequality under lattice deformation. The spectral gap applies to the discrete choice of lattice frame at fixed lattice and metric. Historical novelty is provisional despite the explicit comparisons; the proof and rational verifier have not received independent mathematical audit.

## References

1. Fei Xue, *On κ-covering minima*, arXiv:2610.39034v1, 2026-10-28, https://arxiv.org/abs/2610.39034 .
2. M. Koca, N. O. Koca, A. Al-Siyabi, R. Koc, *Explicit Construction of the Voronoi and Delaunay Cells of W(An) and W(Dn) Lattices and Their Facets*, arXiv:1804.05836, 2018, https://arxiv.org/abs/1804.05836 .
