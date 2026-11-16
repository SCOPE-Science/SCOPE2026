# Sharp eleven-sample recovery and four exceptional erasure types on the rhombic dodecahedron

## Finding
Let \(X\subset S^2\) be the fourteen radially normalized vertices of the regular rhombic dodecahedron,
\[
X=\{\pm e_1,\pm e_2,\pm e_3\}\cup
\{(\varepsilon_1,\varepsilon_2,\varepsilon_3)/\sqrt3:\varepsilon_j\in\{-1,1\}\}.
\]
Write \(\mathcal H_{\le2}=\mathcal H_0\oplus\mathcal H_1\oplus\mathcal H_2\) for the nine-dimensional real space of spherical harmonics of degrees at most two, and \(E_Y:\mathcal H_{\le2}\to\mathbb R^Y\) for evaluation on a surviving vertex subset \(Y\subseteq X\). Then:

1. **Every** \(Y\subseteq X\) with \(|Y|\ge11\) has \(\operatorname{rank}E_Y=9\). The number eleven is sharp as a worst-case guarantee.
2. Among the \(\binom{14}{10}=1001\) ten-vertex subsets, exactly **956** have rank nine and exactly **45** have rank eight. None has a lower rank.
3. The 45 defective ten-vertex subsets form **exactly four** orbits of sizes \(6,24,12,3\) under the 48 signed permutations of the coordinate axes. The kernel of \(E_Y\) for every defective ten-vertex set is one-dimensional. Four explicit representative kernel functions are exhibited in the proof.

These statements hold for complex harmonic coefficients as well because the sampling matrix is real and its rank is unchanged on extending scalars.

## Assumptions and scope
The geometric vertices are first radially normalized to the unit sphere. The eight body-diagonal points have coordinates \((\pm1,\pm1,\pm1)/\sqrt3\), while the six axis points are \(\pm e_j\). This is a fixed, noiseless, unweighted sampling problem; the goal is recovery of every member of \(\mathcal H_{\le2}\), not merely recovery of a particular harmonic degree or of generic functions.

Index the fourteen vertices as \(v_0=-e_1,v_1=e_1,v_2=-e_2,v_3=e_2,v_4=-e_3,v_5=e_3\), followed by \(v_6,\ldots,v_{13}\), the eight body diagonals in lexicographic sign order with \(-1\) before \(+1\). A bit mask \(b\) represents the *surviving* set \(Y_b=\{v_j:(b\mathbin{\&}2^j)\ne0\}\). Hexadecimal masks below are exact finite identifiers, not mathematical variables.

## Proof
**Harmonic basis.** The restrictions to the unit sphere of
\[
1,\ x,\ y,\ z,\ xy,\ xz,\ yz,\ x^2-y^2,\ x^2+y^2-2z^2
\]
form a basis of \(\mathcal H_{\le2}\). Let \(R\) denote their fourteen-by-nine evaluation matrix. Every entry lies in \(\mathbb Z[1/3,\sqrt3]\). In particular, on body diagonals the linear entries are \(\pm\sqrt3/3\), the mixed quadratic entries are \(\pm1/3\), and the two diagonal traceless quadratic entries vanish.

**Rigorous lower-rank certificates.** The ring \(\mathbb Z[1/3,\sqrt3]\) has homomorphisms to \(\mathbb F_{97}\) and \(\mathbb F_{109}\) sending \(\sqrt3\) to \(10\) and \(49\), respectively, since \(10^2\equiv3\pmod{97}\) and \(49^2\equiv3\pmod{109}\). Any minor of \(R\) whose reduction is nonzero is itself nonzero in characteristic zero. Thus every rank-nine test on one of these reduced matrices proves rank nine over \(\mathbb R\). A finite, exact Gaussian elimination on **all** \(\binom{14}{11}=364\) eleven-row submatrices gives rank nine, proving the universal recovery statement; adding rows cannot reduce rank. The same procedure tests all 1001 ten-row submatrices, finding exactly 956 of modular rank nine and 45 of modular rank eight. Both primes produce the same 45 masks.

**The complete four-orbit obstruction.** Coordinate sign changes and permutations preserve the node set and the full quadratic harmonic space. Their 48 permutations of the rows partition the 45 deficient masks into the following distinct orbits. Each displayed function is a nonzero member of \(\mathcal H_{\le2}\) on \(S^2\), vanishing at every vertex represented by the corresponding mask:

| Representative surviving mask | Orbit size | Vanishing quadratic-on-the-sphere function |
| --- | ---: | --- |
| `0x0f3f` | 6 | \(z(x+y)\) |
| `0x1bdb` | 24 | \((y+z)(y-z-1-\sqrt3x)\) |
| `0x1f8f` | 12 | \((x+z)(y+z)\) |
| `0x3fc3` | 3 | \((y-z)(y+z)\) |

The second function may be viewed as the product of a plane through the origin and an affine plane, and the other three are products of planes through the origin. To verify the third polynomial using the displayed harmonic basis, use \(x^2+y^2+z^2=1\) to rewrite \(-3(x+z)(y+z)=-1-3(xy+xz+yz)+(x^2+y^2-2z^2)\) on the sphere. The other functions are likewise linear combinations of the nine displayed basis elements.

The standalone certificate directly evaluates one nonzero harmonic-coordinate null vector on every selected row in each representative mask, **using exact arithmetic in** \(\mathbb Q(\sqrt3)\). It generates all 48 signed coordinate permutations, checks that the four orbits have sizes \(6,24,12,3\) and are disjoint, and verifies that their union equals the **entire** list of 45 modular-rank-eight ten-row subsets. Therefore every one of these 45 subsets has characteristic-zero rank at most eight. The modular rank-eight computation supplies the opposite inequality, hence each has rank **exactly** eight and a one-dimensional nullspace. Every remaining ten-row subset has rank nine. Since some ten-row sets are deficient but every eleven-row set has rank nine, eleven is the sharp worst-case sample threshold. \(\square\)

## Verification
The complete finite proof is in the standalone file `rhombic_erasure_certificate.py`. Run `python3 rhombic_erasure_certificate.py` with Python 3.9 or newer. It uses only the standard library, no network access and no other input. It constructs all fourteen points, represents the nine harmonic-basis evaluations as exact rational pairs in \(\mathbb Q(\sqrt3)\), verifies all four exact vanishing witnesses, enumerates all 48 node symmetries and all 1365 ten- and eleven-point subsets, and performs independent reductions at primes 97 and 109. The successful final line is `QUADRATIC_RHOMBIC_ERASURE_CERTIFICATE_OK; four orbit sizes 6,24,12,3`.

The code verifies a **finite complete** set of masks, not a random sample. The proof does not rely on a floating-point rank tolerance or on an unchecked inference from the number of partitions.

## Relationship to prior work
Zandieh, Han and Avron (arXiv:2202.12995, version one, February 25, 2022) prove near-optimal recovery of spherical-harmonic expansions by uniformly randomized sampling and a dimension lower bound. Their Theorems 14 and 15 do not supply an arbitrary-survivor worst-case threshold for this fourteen-node deterministic grid. A published all-degree harmonic analysis of the **same** radially normalized rhombic dodecahedron establishes ranks and stability of *exact-degree* evaluation on the full grid, not the rank of cumulative-degree evaluation on every ten- and eleven-vertex subset. This distinction is substantive: separate full-grid ranks do not determine the erasure matroid of the direct sum. The published cuboctahedral quadratic erasure classification covers **twelve different vertices** and uses a tetrahedral graphic matroid; duality of the underlying polyhedra does not identify their quadratic evaluation matrices. Bellet, Brachet and Croisille study harmonic interpolation on an equiangular cubed-sphere grid, not the node set here, but only their abstract and bibliographic material were accessible for comparison.

## Limitations
The result treats degree at most two, the specified radially normalized fourteen-point set, noiseless exact evaluation and removal of sampling nodes. It does not bound singular values or noise amplification, generalize to arbitrary perturbed vertices, or classify every smaller cardinality. The modular and exact-witness argument is a complete proof for the stated finite case, not a claim of historical uniqueness. Literature priority is provisional where specialized spherical-grid tables were inaccessible or unindexed. No independent external mathematical audit has been performed.

## References
1. A. Zandieh, I. Han and H. Avron, *Near Optimal Reconstruction of Spherical Harmonic Expansions*, arXiv:2202.12995v1, publicly posted February 25, 2022. https://arxiv.org/pdf/2202.12995
2. *All-degree harmonic sampling and sharp stability on the radially normalized rhombic dodecahedron*, published 2026, https://github.com/published-finding corpus/2026/blob/main/2026/11/2/SCOPE-all-degree-harmonic-sampling-and-sharp-stability-on-the-radially--d466d2d286c1/RESULT.md
3. *The tetrahedral graphic matroid controls quadratic-harmonic sampling on the cuboctahedron*, published 2026, https://github.com/published-finding corpus/2026/blob/main/2026/10/18/SCOPE-the-tetrahedral-graphic-matroid-controls-quadratic-harmonic-samp--22932f55648e/RESULT.md
4. J.-B. Bellet, M. Brachet and J.-P. Croisille, *Interpolation on the cubed sphere with spherical harmonics*, Numer. Math. 153 (2023), 249–278, first published December 28, 2022. https://doi.org/10.1007/s00211-022-01340-w
5. M. A. Valdez, A. J. Yuffa and M. B. Wakin, *On Grid Compressive Sampling for Spherical Field Measurements in Acoustics*, arXiv:2206.11311, first posted June 22, 2022. https://arxiv.org/abs/2206.11311
