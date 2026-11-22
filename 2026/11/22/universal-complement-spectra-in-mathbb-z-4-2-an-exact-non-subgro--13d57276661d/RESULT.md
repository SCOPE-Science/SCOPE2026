# Universal complement spectra in \(\mathbb Z_4^2\): an exact non-subgroup obstruction census

## Finding
Let \(G=(\mathbb Z/4\mathbb Z)^2\), with characters \(\chi_\xi(x)=i^{\langle x,\xi\rangle}\). A translational tile is a nonempty \(A\subseteq G\) with at least one complement \(T\subseteq G\) satisfying \(A\oplus T=G\), where every element has exactly one representation as a sum. A *universal complement spectrum* for \(A\) is a frequency set \(\Lambda\subseteq\widehat G\) that is an orthogonal character basis on **every** such \(T\).

**Exact classification.** Every one of the \(2{,}155\) translational tiles \(A\subseteq G\) has a universal complement spectrum. Exactly \(1{,}168\) of these tiles admit **no** universal complement spectrum that is a translate of a subgroup of \(\widehat G\). The other \(987\) admit a subgroup spectrum. The complete classification consists of \(19\) affine orbits; \(10\) orbits require genuinely non-subgroup spectra. Explicit universal frequency sets and the number of subgroup choices are provided for all \(19\) orbit representatives in `orbit_witnesses.json`.

| Size of \(A\) | Tiles containing \(0\) | Of these, no subgroup spectrum | All tiles | Of these, no subgroup spectrum |
|---|---:|---:|---:|---:|
| \(1\) | 1 | 0 | 16 | 0 |
| \(2\) | 15 | 12 | 120 | 96 |
| \(4\) | 311 | 88 | 1,244 | 352 |
| \(8\) | 387 | 360 | 774 | 720 |
| \(16\) | 1 | 0 | 1 | 0 |
| **Total** | **715** | **460** | **2,155** | **1,168** |

For a concrete non-subgroup example, take \(A=\{(0,0),(1,0)\}\). Its eight-point complement sets all have the common spectrum
\[
\Lambda=\{(u,v):u\in\{0,1\},\ 0\leq v<4\}.
\]
No coset of any order-eight character subgroup is a universal complement spectrum for this \(A\). The first coordinate of \(\Lambda\) varies over two adjacent residues rather than a subgroup of \(\mathbb Z_4\).

## Assumptions and scope
All sets are ordinary subsets without multiplicities. The character pairing uses \(\langle (x_1,x_2),(\xi_1,\xi_2)\rangle=x_1\xi_1+x_2\xi_2\pmod 4\). No normalization of the Fourier sum is needed for detecting zeros. All complements of a fixed \(A\), not just complements in one isomorphism class, must share the *same* spectrum. A frequency translate of a subgroup is equivalent to a subgroup after shifting the entire spectrum, since orthogonality depends only on differences.

The integer encoding in the attached data and checkers is \(j=x+4y\), where \((x,y)\in\{0,1,2,3\}^2\). The affine group has \(16\cdot96=1{,}536\) transformations. An affine transformation of the tile acts contragrediently on character frequencies, preserving both universality and the property of being a subgroup spectrum.

## Proof
**Step 1: reduce to exact Fourier zeros.** For a set \(T\subseteq G\), let
\[
Z(T)=\bigl\{\xi\in\widehat G\setminus\{0\}:\sum_{t\in T}\chi_\xi(t)=0\bigr\}.
\]
For each tile \(A\) define the common zero set
\[
Z_*(A)=\bigcap_{T:\,A\oplus T=G} Z(T).
\]
A set \(\Lambda\) of size \(16/|A|\) is a universal complement spectrum if and only if \((\Lambda-\Lambda)\setminus\{0\}\subseteq Z_*(A)\). The forward implication is orthogonality; conversely, an orthogonal family of exactly \(|T|\) nonzero characters restricted to \(T\) forms a basis. Since shifting either \(T\) or \(\Lambda\) does not change the relevant zero/difference condition, it suffices to examine \(A,T,\Lambda\) containing \(0\).

A subgroup \(H\leq\widehat G\) is a universal spectrum exactly when \(|H|=16/|A|\) and \(H\setminus\{0\}\subseteq Z_*(A)\). This converts the purported impossibility of subgroup spectra into a finite exhaustion over the \(1,3,7,3,1\) subgroups of orders \(1,2,4,8,16\), respectively.

**Step 2: enumerate all possible tiles without sampling.** Any tile has cardinality \(1,2,4,8\), or \(16\). Of the subsets with \(0\in A\), there are
\[
\binom{15}{0}+\binom{15}{1}+\binom{15}{3}+\binom{15}{7}+\binom{15}{15}=6{,}907
\]
candidates. For each candidate \(A\), the exact-cover recursion starts with the translate \(A+0\), finds the least uncovered group element \(x\), and branches over all \(t=x-a\) for \(a\in A\). It rejects every branch where \(A+t\) intersects already covered points and records the translation set at a full cover. Induction on the number of uncovered points proves that each normalized complement containing \(0\) is found and none is invented. Duplicate branches are set-deduplicated.

**Step 3: exact character arithmetic and exhaustive frequency sets.** Each character sum lies in the Gaussian integers. Computing the numbers of exponents congruent to \(0,1,2,3\pmod 4\) gives its real and imaginary parts as exact integers. Intersecting zero masks over all normalized complements yields \(Z_*(A)\). A backtracking clique search among the \(15\) nonzero characters gives an explicit spectrum containing \(0\) for every tiled \(A\). The same common-zero mask is tested against **every** subgroup of the requisite order. Thus the entire \(715\)-tile normalized census, including the \(460\) non-subgroup cases, is exhaustive and exact, not an experimental extrapolation.

**Step 4: affine-class independent check and restore translates.** A separate implementation directly enumerates all possible normalized complements of each of the \(19\) explicit affine representatives and checks the recorded frequency set against every one, using independent pairwise-sum and Gaussian-integer routines. It independently enumerates candidate subgroups and verifies their exact numbers. The \(96\) invertible linear maps, together with translations followed by normalizing an element of \(A\) to zero, yield \(19\) disjoint anchored affine orbits covering exactly \(715\) tiles. Their size distribution and absence-of-subgroup distribution reproduce Step 3.

For a fixed \(k=|A|\), exactly \(k/|\operatorname{Per}(A)|\) of the \(16/|\operatorname{Per}(A)|\) distinct translates of each translation orbit contain \(0\). Hence the full-to-anchored ratio is \(16/k\), including periodic tiles. Multiplying the normalized counts by \(16/k\) gives the full numbers \(2{,}155\) and \(1{,}168\).

## Verification
Run `python3 verify_all.py` and `python3 verify_orbits.py` in the same directory as `orbit_witnesses.json`; no third-party packages are required. The recorded result in `verify_output.txt` contains two successful independent checks. The first tests all \(6{,}907\) candidate anchored sets, exact complement covers and common spectra; the second checks all complements of \(19\) affine representatives by a separate combinatorial criterion and validates their union under all affine maps.

All calculations are finite over integer bitmasks and Gaussian-integer character sums. The code, enumeration bounds, orbit witnesses and verified outputs form the reproducible certificate. No numerical tolerance, stochastic step or floating-point rank calculation is used.

## Relationship to prior work
Lagarias and Wang establish the universal-spectrum criterion through factorization of finite abelian groups and prove broad cases for **cyclic** groups; their criterion is the starting definition here, not a classification of this noncyclic group. Farkas, Matolcsi and Móra show that universal spectra and the tiling-to-spectral implication are equivalent when asserted across **all finite groups of a given generator dimension**, using an enlargement to a different group; this does not turn a tile-to-spectrum census in one fixed finite group into its universal-complement classification. Kolountzakis and Matolcsi give counterexamples to universal spectra in larger-rank groups. Zhou's results address coprime product extensions and special subgroup-complement configurations, not the complete \(\mathbb Z_4^2\) orbit census.

An existing complete Fuglede census in \(\mathbb Z_4^2\) determines the \(2{,}155\) individual tiling/spectral sets and \(19\) affine classes. **Those baseline numbers are not claimed as new.** The additional statement here is the universal simultaneous choice for *all* complements of each tile, with the exact obstruction that \(1{,}168\) tiles cannot use a subgroup-coset frequency basis. The earlier spectrality of each complement individually does not, on its own, identify a common basis or rule out every subgroup basis.

## Limitations
This is an exact theorem for one group of order \(16\), not for arbitrary products of prime-power cyclic groups. A subgroup spectrum is not required by the definition of a universal spectrum; the \(1{,}168\) cases are positive examples requiring other geometry, not counterexamples to universality. The numerical census depends on exhaustive, self-contained integer programs whose branch-coverage arguments are provided above; no separate formal proof assistant or independent expert validation has been undertaken. Unindexed earlier equivalent classifications are a residual priority risk.

## References
1. J. C. Lagarias and Y. Wang, *Spectral Sets and Factorizations of Finite Abelian Groups*, Journal of Functional Analysis 145 (1997), 73–98; author manuscript: https://websites.umich.edu/lagarias/doc/fuglede.pdf .
2. M. N. Kolountzakis and M. Matolcsi, *Tiles with no spectra*, initial arXiv version dated 2004-06-07, https://arxiv.org/abs/math/0406127 .
3. B. Farkas, M. Matolcsi and P. Móra, *On Fuglede's conjecture and the existence of universal spectra*, manuscript dated 2005-11-10, https://math.bme.hu/~morap/fuglede3-1105.pdf ; J. Fourier Anal. Appl. 12 (2006), 483–494.
4. W. Zhou, *Universal Spectra in \(G\times\mathbb Z_p\)*, J. Fourier Anal. Appl. 30 (2024), article 17, https://zhou.ac.cn/articles/spectra.pdf .
5. W. Zhou, *An Equi-distribution Equality of Tiles* (originally *Mutual Annihilation of Tiles*), https://arxiv.org/abs/2412.16865 .
6. *Exact Fuglede census in the sixteen-point group \(\mathbb Z_4^2\)*, publicly available 2026 finite census, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-fuglede-census-in-the-sixteen-point-group-mathbb-z-4-2--27eae8f2814b .
