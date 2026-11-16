# The sharp thirteen-sample threshold for quadratic harmonics on the regular dodecahedron

## Finding
Let \(X\subset S^2\) be the twenty vertices of a regular dodecahedron, and let \(\mathcal H_{\le2}=\mathcal H_0\oplus\mathcal H_1\oplus\mathcal H_2\), the nine-dimensional complex space of spherical harmonics of degree at most two. For every subset \(S\subseteq X\), let \(E_S:\mathcal H_{\le2}\to\mathbb C^S\) be evaluation.

**Sharp worst-case threshold.** Every set of at least thirteen vertices is unisolvent: \(\ker E_S=\{0\}\) for \(|S|\ge13\). The bound is sharp: there exist twelve-vertex subsets with nonzero kernel. Among the \(\binom{20}{12}=125970\) twelve-vertex subsets, **exactly twenty-five** fail unisolvency. Each of the twenty-five has evaluation rank exactly eight and hence a one-dimensional kernel. Every other twelve-vertex subset has rank nine. A suitable nine-point subset also has full rank, so the worst-case thirteen-point threshold is a property of *arbitrary erasures*, not the least possible number of carefully placed samples.

Equivalently, **any seven missing vertex values** can be tolerated when recovering an arbitrary degree-at-most-two spherical harmonic from the remaining values; exactly twenty-five patterns of eight missing vertices are fatal.

## Assumptions and scope
Write \(\varphi=(1+\sqrt5)/2\), \(\alpha=\varphi^{-1}\). The unnormalized coordinates of \(X\) are the twenty distinct vectors
\[
(\pm1,\pm1,\pm1),\quad(0,\pm\alpha,\pm\varphi),\quad(\pm\alpha,\pm\varphi,0),\quad(\pm\varphi,0,\pm\alpha),
\]
with independent choices of signs, all divided by \(\sqrt3\) to obtain unit spherical coordinates. The base field for ranks is \(\mathbb C\), equivalently \(\mathbb R\) because the evaluation matrix is real. Observations are noiseless point values; no uniform condition number is asserted.

For reproducible vertex indices \(0,\ldots,19\), enumerate each block above in its displayed order, taking the negative sign before the positive sign in every freely varying coordinate. For a bit mask \(m\in\{0,\ldots,2^{20}-1\}\), the associated observation set is \(S_m=\{v_i:(m\mathbin{\&}2^i)\ne0\}\). The twenty-five exceptional twelve-point masks are produced *without a supplied list* by the standalone verifier.

## Proof
**1. Reduction to a nine-column matrix.** For unnormalized coordinates \((x,y,z)\), the restrictions of
\[
1,\ x,\ y,\ z,\ xy,\ yz,\ zx,\ x^2-y^2,\ y^2-z^2
\]
are a basis of \(\mathcal H_{\le2}\) up to invertible column scalings. Let \(A\) be the \(20\times9\) evaluation matrix. Its entries lie in \(K=\mathbb Q(\sqrt5)\). In particular, the rank of a vertex-submatrix over \(K\) is its rank over \(\mathbb C\).

**2. An exact finite-field obstruction to thirteen zero values.** Clear the denominators by doubling all three coordinates; the resulting quadratic and linear columns merely undergo invertible rescalings. Their entries now belong to \(\mathbb Z[\sqrt5]\). Reduce coefficients through the ring homomorphism \(\mathbb Z[\sqrt5]\to\mathbb F_{101}\) sending \(\sqrt5\mapsto45\), which is valid since \(45^2\equiv5\pmod{101}\). Let \(\overline A\) be the resulting \(20\times9\) matrix.

The executable `verify_mod101.cpp` enumerates **all \(\binom{20}{8}=125970\) eight-element row subsets**. Exactly \(123030\) have rank eight and \(2940\) have smaller rank. Every rank-eight subset spans a hyperplane, represented by its unique one-dimensional normal vector in \(\mathbb F_{101}^9\). Computing the complete zero mask of that normal on all twenty rows gives \(40991\) distinct hyperplane closures. Their cardinality distribution is
\[
\begin{array}{c|rrrrr}
\text{closure size}&8&9&10&11&12\\\hline
\text{number}&35820&4420&546&180&25.
\end{array}
\]
No closure has more than twelve rows. This is a genuinely exhaustive finite combinatorial computation, rather than random testing or floating-point evidence.

Suppose thirteen rows of \(A\) were dependent in the sense that they had rank at most eight. Every \(9\times9\) minor of those rows would be exactly zero in \(K\); therefore the same thirteen reduced rows would have rank at most eight over \(\mathbb F_{101}\). Since \(\overline A\) has rank nine, their row span can be extended using rows of \(\overline A\) to an eight-dimensional hyperplane. Its closure would contain at least thirteen rows, contradiction. This proves unisolvency of every thirteen-point sample set; larger sets follow immediately.

**3. Exact witnesses and completeness of the twenty-five exceptions.** Each of the twenty-five modular twelve-row closures is invariant under the antipodal involution, and hence comprises six antipodal pairs. The additional checker `verify_exact_witnesses.py` derives (rather than assumes) those twenty-five masks, chooses five of the six antipodal representative rows in the six-column *even* evaluation basis
\[
1,\ xy,\ yz,\ zx,\ x^2-y^2,\ y^2-z^2,
\]
and constructs an exact nonzero null coefficient vector by signed \(5\times5\) cofactors. It computes all coefficients as pairs of integers \(a+b\sqrt5\), and proves by direct exact evaluation that each resulting quadratic vanishes on **precisely** the twelve indexed vertices. The vector is nonzero, so the twenty-five closures really are singular over \(K\), not artifacts of modular reduction. Each has rank at least eight over \(K\) because it contains eight rows independent modulo \(101\), and at most eight because of the exact null vector; thus its kernel has dimension one.

Any other singular twelve-point set would similarly reduce to twelve rows contained in a rank-eight modular hyperplane closure. Every such closure has at most twelve rows; the set would have to coincide with one of the twenty-five just certified. This proves the exact exception count. As a concrete witness, the nonzero harmonic
\[
F(x,y,z)=2\sqrt5(x^2-y^2)+(\sqrt5-3)(y^2-z^2)
\]
vanishes on the eight \((\pm1,\pm1,\pm1)\) vertices and the four \((0,\pm\alpha,\pm\varphi)\) vertices (in the unnormalized coordinates), and on none of the remaining eight.

**4. Carefully chosen smaller sets.** Rows indexed \(0,1,2,3,4,5,6,8,12\) have rank nine modulo \(101\), verified by the same exact modular elimination. Hence those nine points suffice if their positions may be chosen. The dimension of \(\mathcal H_{\le2}\) shows that fewer than nine point observations can never be injective.

## Verification
From the directory containing the two standalone files, execute `python3 verify_exact_witnesses.py`. A C++17 compiler (`g++`) and the Python standard library are required. The Python script compiles and runs `verify_mod101.cpp`, checks the exhaustive finite-field rank/closure counts, then performs independent \(\mathbb Z[\sqrt5]\) cofactor calculations for every claimed exceptional subset. It prints `DODECAHEDRAL_ERASURES_EXACT_CHECK_OK` only if all assertions succeed. The finite enumeration is exhaustive because exactly \(125970\) eight-element subsets exist and every lower-rank row set lies in a rank-eight hyperplane when the full row matrix has rank nine. The reduction implication is one-way only and is combined with exact characteristic-zero witnesses.

## Relationship to prior work
Zandieh, Han and Avron (2022) prove near-optimal randomized sampling rates for spherical-harmonic reconstruction in arbitrary dimensions, but not a fixed-design **worst-case erasure threshold** or a twelve-subset exception count. Previously published all-degree dodecahedral harmonic-sampling spectra determine the ranks for the **complete twenty-vertex set**, usually for a **single exact harmonic degree**; those statements do not imply that every thirteen-row submatrix of the combined degrees zero, one and two has full rank, nor do they classify exceptional twelve-row submatrices. The prior cuboctahedral erasure theorem concerns another vertex configuration and a different row matroid. The exact twenty-five-subset classification is not obtained merely by changing the name of that geometry. The full-text and abstract-level comparisons and unresolved bibliographic risks are specified in `REVIEW.md` and `AUDIT.json`.

## Limitations
This theorem concerns one fixed Platonic vertex configuration and the nine-dimensional *combined* degree-zero-to-two harmonic space. The modular computation is a finite exhaustive certificate, not a theorem about arbitrary point configurations or higher degrees. Unisolvency does not bound interpolation condition numbers or guarantee stability under noise. Specialist historical tables of dodecahedral polynomial interpolation could contain an equivalent finite classification; independent assessment of priority remains appropriate.

## References
- Amir Zandieh, Insu Han, Haim Avron, *Near Optimal Reconstruction of Spherical Harmonic Expansions*, arXiv:2202.12995v1, first posted 2022-02-25. https://arxiv.org/html/2202.12995v1
- Jean-Baptiste Bellet, Matthieu Brachet, Jean-Pierre Croisille, *Interpolation on the cubed sphere with spherical harmonics*, *Numerische Mathematik* 153 (2023), 249–278. https://doi.org/10.1007/s00211-022-01340-w
- *Exact harmonic-sampling spectra and the last interpolation gap of the regular dodecahedron*, publicly available research record, 2026. https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-exact-harmonic-sampling-spectra-and-the-last-interpolation-gap-o--fec69d22daff
- *The tetrahedral graphic matroid controls quadratic-harmonic sampling on the cuboctahedron*, publicly available research record, 2026. https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-the-tetrahedral-graphic-matroid-controls-quadratic-harmonic-samp--22932f55648e
