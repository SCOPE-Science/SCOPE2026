# Complete optimal Kuhn-frame census for the three-dimensional taxicab octahedron

## Finding
Let \(O=\{x\in\mathbb R^3:\|x\|_1\le1\}\) and \(\Lambda=\mathbb Z^3\). For each unordered triple \(B=\{b_1,b_2,b_3\}\) of independent integer vectors, form the six Kuhn tetrahedra
\[
Q_\sigma(B)=\operatorname{conv}\{0,b_{\sigma(1)},b_{\sigma(1)}+b_{\sigma(2)},b_1+b_2+b_3\},\qquad \sigma\in S_3.
\]
Put \(r_1(Q)=\inf_{c\in\mathbb R^3}\max_{x\in Q}\|x-c\|_1\), and \(\rho(B)=\max_\sigma r_1(Q_\sigma(B))\). Centers for different permutations may differ. Then
\[
\min_B\rho(B)=\frac32,\qquad
\#\{B:\rho(B)=\tfrac32\}=928.
\]
For these \(928\) **unordered, independent, integer-column frames**, the absolute-determinant index distribution is
\[
\begin{array}{c|rrrr}
|\det B|&1&2&3&4\\\hline
\#\text{frames}&512&408&0&8
\end{array}
\]
and no index at least \(5\) occurs. The signed-coordinate-permutation group of order \(48\) partitions these into \(23\) orbits: \(12\) of index \(1\), \(10\) of index \(2\), and one of index \(4\). The exact orbit representatives and sizes appear in `orbit_classes.csv`.

## Assumptions and scope
The polytope and lattice have the indicated standard normalization. A frame is a set of three linearly independent vectors in \(\mathbb Z^3\): column permutations are identified, but simultaneous coordinate sign changes and coordinate permutations are **not** identified when counting the \(928\) frames. They are identified only in the separate \(23\)-orbit census. The frame need not generate the entire lattice: the index \(|\det B|\) may exceed one. The six tetrahedra each get their own fitting translation. All counts in the theorem refer to exact integral arithmetic, and no generalization to other dimensions or norms is asserted.

## Proof
**1. Exact tetrahedral Chebyshev criterion.** For a finite nonempty set \(S\subset\mathbb R^3\) put \(h_S(\varepsilon)=\max_{x\in S}\varepsilon\cdot x\), for the eight vectors \(\varepsilon\in\{\pm1\}^3\). As \(\|y\|_1=\max_\varepsilon\varepsilon\cdot y\), linear-programming duality gives
\[
r_1(S)=\max_{\lambda\ge0}\sum_\varepsilon\lambda_\varepsilon h_S(\varepsilon),\quad
\sum_\varepsilon\lambda_\varepsilon=1,\quad
\sum_\varepsilon\lambda_\varepsilon\varepsilon=0.
\]
The four affine constraints have rank four. Each extreme feasible \(\lambda\) has at most four nonzero coordinates and linearly independent corresponding columns \((1,\varepsilon)\). Checking the complete finite list of supports of size at most four among the eight sign vectors gives exactly six extremes: the four opposite pairs with weights \(1/2\) and the two regular parity tetrahedra with weights \(1/4\). The standalone exact-rational `extreme_sign_distributions` routine checks every such support, including degeneracy and positivity, without numerical optimization. Therefore
\[
r_1(S)=\max\left\{
\frac12\max_\varepsilon(h_S(\varepsilon)+h_S(-\varepsilon)),
\ \frac14\sum_{\varepsilon_1\varepsilon_2\varepsilon_3=1}h_S(\varepsilon),
\ \frac14\sum_{\varepsilon_1\varepsilon_2\varepsilon_3=-1}h_S(\varepsilon)
\right\}.
\]
For sets with integral vertices, radius at most \(m/2\) is equivalent to the four integer opposite-pair sums being at most \(m\) and both integer parity-quartet sums being at most \(2m\).

**2. Finite reduction and a sharp lower bound.** If \(\rho(B)\le m/2\), every pair of vertices in each Kuhn tetrahedron is at \(\ell_1\)-distance at most \(m\). Every nonempty subset sum of the three frame vectors is an edge difference in at least one of the six Kuhn tetrahedra. In particular, every individual column is a nonzero integral vector of \(\ell_1\)-norm at most \(m\), and all pair/triple sums satisfy the same bound. If \(\rho(B)<3/2\), integral pairwise distances are at most two, so the columns belong to the complete set of \(24\) nonzero integral triples of \(\ell_1\)-norm at most two. The exact checker examines all independent unordered triples in this finite set (and the necessary subset-sum restrictions) and all six permutations with the **strict** radius-below-\(3/2\) inequalities from step 1: integer opposite-pair widths are at most two, while each integer parity-quartet support sum is at most five. None qualifies. Hence every frame has \(\rho(B)\ge3/2\). The three standard basis vectors attain \(3/2\), as every tetrahedron is contained in the unit cube, which fits in the \(\ell_1\) ball of radius \(3/2\) centered at \((1/2,1/2,1/2)\).

**3. Complete optimizer census.** If \(\rho(B)=3/2\), the preceding subset-sum bound with \(m=3\) places each column in the complete list of \(62\) nonzero integer vectors of \(\ell_1\)-norm at most three. Select all three-element subsets of this list and discard dependent frames or those with any pair/triple sum of norm greater than three. Exactly \(1264\) frames remain, distributed by absolute determinant as \((512,408,288,56)\) for indices \((1,2,3,4)\). For every remaining frame, test all six permutations using the six *necessary and sufficient* integer support inequalities from step 1, now with \(m=3\). Exactly \(928\) remain, with determinant distribution \((512,408,0,8)\). Each exclusion follows from an explicit failed necessary inequality, and each inclusion from all sufficient inequalities. The included `verify_frames.py` independently regenerates every candidate from a rigorously bounded search domain; it assumes neither the orbit counts nor the claimed absence of index-three frames.

**4. Orbit census.** Apply each of the \(3!2^3=48\) signed coordinate permutations simultaneously to all three vectors in an accepted unordered frame. Re-sort the columns to obtain a canonical representative. This action preserves the six tetrahedra and the \(\ell_1\) fitting radius. The exact orbit partition yields \(23\) disjoint orbits, with the index counts stated above. `verify_frames.py` verifies that their union is precisely all \(928\) accepted frames; `orbit_classes.csv` lists their representatives and exact orbit sizes.

## Verification
Run `python3 verify_frames.py` from a directory containing the standalone packaged file. It uses only Python's standard library, exact integers for all support and frame tests, and rational fractions for the six dual extreme distributions. It checks the full bounded sets (\(24\) and \(62\) columns), the \(1264\) necessary candidates, the \(928\) passing frames, the index and orbit histograms, and the exact partition of every optimizer. The recorded output is reproducible from the script; no random sampling or solver tolerance enters the proof.

## Relationship to prior work
Fei Xue, *On \(\kappa\)-covering minima* (arXiv:2610.39034v1, October 28, 2026), defines the common-frame packet fitting radius and basic inequalities. Lian and Xue, *The lattice covering density of the regular octahedron* (arXiv:2609.23210v1, September 19, 2026; revised November 1), prove a sharp determinant estimate for the same six tetrahedra and exhibit a determinant-four equality frame. These results justify the natural invariant and its importance in octahedral lattice covering. They do not state the complete optimum-frame count \(928\), the absence of index-three optimal frames, or the complete \(23\)-orbit breakdown. The published determinant-four inequality is consistent with, and independently bounds, the finite census, but the classification is obtained here from exact support inequalities and exhaustive bounded arithmetic. Related optimal-frame classifications for other norms or lattices are different objects.

## Limitations
Originality reflects comparison with accessible full primary texts, targeted mathematical-record searches and recoverable earlier claims, not a proof of absolute publication priority. The general theorem is a complete finite exhaustion for the **fixed** standard three-dimensional octahedron and standard integer lattice. The checker relies on Python's exact integer and rational operations but is not independently audited. The formula does not classify fitting centers or all frames above the optimum and is not a statement about the ordinary covering radius of the lattice generated by each frame. Independent mathematical validation has not been performed.

## References
1. F. Xue, *On \(\kappa\)-covering minima*, arXiv:2610.39034v1 (2026-10-28), https://arxiv.org/abs/2610.39034.
2. Y. Lian and F. Xue, *The lattice covering density of the regular octahedron*, arXiv:2609.23210v1 (2026-09-19; v2 2026-11-01), https://arxiv.org/abs/2609.23210.
