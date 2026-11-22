# Walsh recovery and the sharp range projection for Folkman dimers

## Finding

Let \(G\) be the 20-vertex, 40-edge Folkman graph (the subdivided double of \(K_5\)), with ten doubled vertices and ten edge-subdivision vertices. Let \(\mathcal M(G)\) be its perfect matchings. On the binary edge group \(H=\mathbb F_2^{E(G)}\), define \(f(x)=1\) when \(x\) is the incidence vector of a matching in \(\mathcal M(G)\) and zero otherwise, and let \(T_fh=f*h\) be **unnormalized** convolution.

There are exactly \(768\) matchings. Every Walsh multiplier
\[
 W(S)=\sum_{M\in\mathcal M(G)}(-1)^{|S\cap M|}\qquad(S\subseteq E(G))
\]
is divisible by \(32\). The full multiplier spectrum has \(1{,}262{,}164\cdot 2^{19}\) zeros and hence
\[
 \operatorname{rank} T_f=834{,}988\cdot 2^{19}=437{,}774{,}188{,}544,
 \quad\operatorname{nullity}T_f=661{,}737{,}439{,}232.
\]
Every nonzero multiplier has modulus at least \(32\), and that bound is attained. The positive-spectrum \(\ell^2\) condition number is \(768/32=24\); equivalently the convolution Moore--Penrose inverse has \(\ell^2\)-operator norm \(1/32\).

Among **all** real or complex linear projections onto the range of \(T_f\), the minimum induced \(\ell^1\)-norm and the minimum induced \(\ell^\infty\)-norm both equal
\[
 \boxed{\frac{56{,}520{,}123}{262{,}144}}.
\]
The orthogonal Fourier range projector attains both minima. This is a finite exact statement for the Folkman graph, not a family-uniform result for arbitrary semisymmetric graphs.

## Assumptions and scope

Define the doubled vertices \((i,a)\) for \(0\le i<5\) and \(a\in\{0,1\}\), and one subdivision vertex \(u_{ij}\) for every \(0\le i<j<5\). Connect \(u_{ij}\) to \((i,0),(i,1),(j,0),(j,1)\). These 40 distinct edges are ordered by lexicographic \((i,j)\), followed by the two clones at \(i\), then the two at \(j\). This specifies the graph independently of any drawing.

Counting convolution is taken on **all** \(2^{40}\) binary edge vectors, using the counting measure, with the nonunitary Walsh transform \(\widehat h(S)=\sum_x(-1)^{S\cdot x}h(x)\). Norms refer to the ordinary counting-measure \(\ell^p(H)\) norms. A Fourier multiplier of zero is invisible to convolution; the range is the span of characters with nonzero multipliers. The word condition number refers to the largest over smallest *nonzero* singular values, not an inverse of a singular operator.

## Proof

**1. Matching structure.** Every perfect matching uses one edge incident to each subdivision vertex \(u_{ij}\); assigning it to the \(i\)-clone pair or \(j\)-clone pair orients the corresponding edge of \(K_5\). Both clones of each \(i\) must be matched, so exactly two \(K_5\)-edges are oriented into \(i\). Thus the orientation is a regular tournament on five vertices. There are exactly 24 such labelled tournaments (confirmed by exhausting all \(2^{10}\) orientations, or by the unique five-vertex regular tournament with rotational stabilizer of order five). For each tournament, its two incoming edges at every \(i\) can be assigned to the two clones in exactly two ways, independently across five vertices. Hence \(|\mathcal M(G)|=24\cdot2^5=768\).

**2. Uniform dyadic divisibility.** Give every edge a sign \(\epsilon_e\in\{+1,-1\}\), corresponding to a Walsh character. Fix a regular orientation. If the two incoming base edges at \(i\) are \(e_i,e'_i\), summing the two clone assignments contributes
\[
  \epsilon_{i,0,e_i}\epsilon_{i,1,e'_i}
  +\epsilon_{i,1,e_i}\epsilon_{i,0,e'_i}
  \in\{-2,0,2\}.
\]
The five vertices contribute independently, so this orientation contributes a multiple of \(2^5=32\). Summing over the 24 orientations shows \(32\mid W(S)\) for every \(S\). Exact attainment of the magnitude \(32\) follows from the exhaustive calculation below, not from divisibility alone.

**3. Gauge compression.** Flipping the signs on every edge incident with any vertex multiplies the contribution of each matching by \(-1\), since every perfect matching meets that vertex once. The group of such vertex-star flips is the image of the binary vertex-edge incidence map and has rank \(20-1=19\) because \(G\) is connected. Consequently it preserves \(|W|\) and its zero set. Choose a spanning tree by breadth-first search starting at vertex zero with the prescribed edge order; it has 19 edges. Vertex-star flips uniquely set the signs of all tree edges to \(+1\), leaving exactly \(40-19=21\) independently signable chords. Thus the full spectrum is determined (up to signs) by \(2^{21}\) chord-sign frequencies; each has \(2^{19}\) full frequencies. As the vertex-star map has a nontrivial sign character on the matching orbit, nonzero full frequencies have signs equally split in each coset. The exact reduced signed histogram appears under Verification.

**4. Exact integer spectral certificate.** Enumerate the 24 regular orientations of \(K_5\). For each, enumerate all \(2^5\) clone assignments, project the corresponding ten matching edges to their 21 chord coordinates, and increment an array \(a\) of length \(2^{21}\). The 768 vectors in this array are distinct (also checked by a completely separate direct perfect-matching enumerator). The exact integer Walsh--Hadamard transform
\[
 A(t)=\sum_{z\in\mathbb F_2^{21}}(-1)^{t\cdot z}a(z)
\]
has the following complete signed level histogram. All entries are computed by integer additions and subtractions, with no floating-point operation.

| Reduced multiplier | Number of chord-sign characters |
|---:|---:|
| -384 | 16 |
| -256 | 153 |
| -192 | 210 |
| -160 | 484 |
| -128 | 3,332 |
| -96 | 9,516 |
| -64 | 70,730 |
| -32 | 332,872 |
| 0 | 1,262,164 |
| 32 | 333,368 |
| 64 | 70,822 |
| 96 | 9,364 |
| 128 | 3,268 |
| 160 | 476 |
| 192 | 190 |
| 256 | 162 |
| 384 | 24 |
| 768 | 1 |

The histogram sums to \(2^{21}\). The zero count is exactly \(1{,}262{,}164\), and the \(834{,}988\) nonzeros have least modulus \(32\). The unnormalized convolution is diagonal in the Walsh basis, so the rank, nullity and positive condition number follow. The inverse transform check certifies consistency of the exact spectrum with the original array.

**5. Sharp endpoint range projection.** Let \(\Lambda=\{t:A(t)\ne0\}\) and define the indicator \(b(t)=1_{t\in\Lambda}\). The orthogonal projection \(P\) onto \(\operatorname{ran}(T_f)\) has Fourier multiplier equal to that indicator (expanded along vertex-star cosets), hence is translation-invariant. Its convolution kernel is the inverse Walsh transform of \(b\); the \(\ell^1\)- and \(\ell^\infty\)-operator norms both equal the kernel's \(\ell^1\)-norm. Since the nonzero Fourier locus is invariant under the 19-dimensional vertex-star subgroup, the inverse Fourier kernel is supported on the 21-dimensional cycle space, and its \(\ell^1\)-norm reduces exactly to
\[
 \frac1{2^{21}}\sum_{z\in\mathbb F_2^{21}}
  \left|\sum_{t\in\mathbb F_2^{21}}(-1)^{z\cdot t}b(t)\right|
 =\frac{452{,}160{,}984}{2{,}097{,}152}
 =\frac{56{,}520{,}123}{262{,}144}.
\]
All terms are exact integers. For an arbitrary projection \(Q\) onto the same range, average its conjugates over all group translations. This does not increase either induced endpoint norm, retains the projection property and the range, and gives a translation-invariant projection. The unique translation-invariant projection onto a fixed collection of Walsh character subspaces is \(P\). Hence neither real nor complex projections can improve the endpoint norms.

## Verification

Two executable implementations, `folkman_spectrum.cpp` (standalone C++17) and `verify_independent.py` (Python 3 with NumPy), are included. The first enumerates perfect matchings directly as well as by regular-tournament orientations, compares both \(2^{21}\)-arrays, applies an exact integer Walsh transform, checks its inverse, and prints `FOLKMAN_WALSH_PASS`. The second independently constructs the graph, enumerates the 24 tournaments, checks Parseval's identity and fourteen direct signed-frequency sums, computes the complete histogram and range-projection norm, and prints `INDEPENDENT_FOLKMAN_WALSH_PASS`. Their output certificates are included. Compile/run with `g++ -std=c++17 -O2 folkman_spectrum.cpp -o folkman_spectrum && ./folkman_spectrum`; run the other with `python3 verify_independent.py`. Its only nonstandard dependency is NumPy. The reported 21-coordinate enumeration is exhaustive, and the gauge argument proves its coverage of all \(2^{40}\) characters.

## Relationship to prior work

Folkman's 1967 construction defines the semisymmetric graph. Kuperberg (1998) discusses perfect-matching enumeration and the permanent--determinant method. Pippenger (2001, made public as a September 10 technical report) enumerates matchings of incidence graphs of complete graphs, a related but **undoubled** construction. The 2025 matching-polynomial study of symmetric and semisymmetric graphs **already records the 768 perfect matchings of the Folkman graph**; neither that number nor the graph itself is claimed as new. A separate 2025 spectral-polynomial study determines the graph's adjacency spectrum, a different operator. The result here concerns signed incidence counts across **all 40 edge-character coordinates**, their complete Fourier zero set, sharp nonzero gap, and the optimal projection norm. Prior exact Walsh calculations on other matching graphs do not imply this spectrum without the present additional computation.

## Limitations

This is one exact finite object, not a theorem for arbitrary semisymmetric graphs or subdivided doubles. The exact 21-coordinate histogram and projection numerator are computer-assisted finite certificates supported by two executable verifiers, not short closed-form expressions. The 1967 original paper was available through bibliographic information and its abstract, not through fully inspected complete text; unindexed equivalent signed-matching computations remain possible. No independent external mathematical audit has occurred. The 2025 matching count and the general Fourier/projection methods are prior work.

## References

- J. Folkman, *Regular line-symmetric graphs*, Journal of Combinatorial Theory 3 (1967), 215--232. https://doi.org/10.1016/S0021-9800(67)80069-3
- G. Kuperberg, *An exploration of the permanent-determinant method*, arXiv:math/9810091, first public 1998-10-14. https://arxiv.org/abs/math/9810091
- N. Pippenger, *Enumeration of Matchings in the Incidence Graphs of Complete and Complete Bipartite Graphs*, UBC technical report TR-2001-12, public 2001-09-10. https://www.cs.ubc.ca/tr/2001/tr-2001-12
- *Matching Polynomials of Symmetric, Semisymmetric, Double Group Graphs, Polyacenes, Wheels, Fans, and Symmetric Solids in Third and Higher Dimensions*, Symmetry 17 (2025), article 133. https://www.mdpi.com/2073-8994/17/1/133
- *Spectral Polynomials and Spectra of Graphs Beyond Cubic and Icosahedral Symmetries*, Symmetry 17 (2025), article 247. https://www.mdpi.com/2073-8994/17/2/247
