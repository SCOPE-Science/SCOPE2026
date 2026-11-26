# The seven-vertex deleted-product four-manifold is a connected sum of twenty sphere products

## Finding
Let \(K=\operatorname{sk}_2\Delta^6\) be the two-skeleton of the simplex on seven vertices, and let \(M=\operatorname{DConf}(K,2)\) denote its *ordered* two-point deleted-product cell complex. Then there is an orientation-preserving homeomorphism
\[
|M|\ \cong\ \#_{20}(S^{2}\times S^{2}),
\]
with the orientation on the target chosen compatibly. Equivalently, the integral middle-dimensional intersection lattice of \(M\) is \(H^{\oplus20}\), where \(H=\begin{pmatrix}0&1\\1&0\end{pmatrix}\) is the hyperbolic plane. In particular \(M\) is spin, and its signature is zero.

## Assumptions and scope
The vertices of \(\Delta^6\) are \(\{0,1,2,3,4,5,6\}\). A nonempty cell \((A,B)\) means the product of the simplex on \(A\) with the simplex on \(B\), where \(A\cap B=\varnothing\) and \(1\le |A|,|B|\le3\). Its dimension is \(|A|+|B|-2\). Factor order matters. Each factor simplex has the orientation induced by ascending vertex labels, and product cells have their product orientations.

The published manifold-recognition theorem of González, González and Pérez-Morales (2026, Theorem 1.1) establishes that \(|M|\) is an orientable connected closed combinatorial four-manifold. The earlier connectivity and integral homology theorem of González and González (2023 preprint; 2025 journal version, Theorem 1.2) establishes that it is simply connected and has torsion-free homology. These are invoked as identified published hypotheses, not claimed as new computations.

## Proof
**1. Cell count and rank.** Directly choosing disjoint nonempty vertex subsets of size at most three gives the numbers of cells in dimensions zero through four:
\[
(f_0,f_1,f_2,f_3,f_4)=(42,210,490,420,140).
\]
Thus \(\chi(M)=42\). For a simply connected closed oriented four-manifold, Poincaré duality gives \(b_0=b_4=1\), \(b_1=b_3=0\), so \(b_2=40\). Torsion-freeness follows from the cited homology theorem.

**2. A global signed fundamental cycle and a reversing symmetry.** For every top-dimensional cell, \(|A|=|B|=3\) and there is exactly one omitted vertex \(c\). Put \(\epsilon(A,B)=\operatorname{sgn}(A_\uparrow,B_\uparrow,c)\), the sign of the seven-symbol concatenation relative to \((0,1,\ldots,6)\). Then
\[
Z=\sum_{A\cap B=\varnothing,\ |A|=|B|=3}\epsilon(A,B)[A\times B]
\]
is an integral cycle. Each three-dimensional product cell has exactly two top-dimensional cofaces, contributing opposite signed incidences. Their total is zero. The orientation represented by \(Z\) is global and nonzero because \(M\) is a connected oriented closed four-manifold. A permutation \(\pi\) of the seven vertex labels sends \(Z\) to \(\operatorname{sgn}(\pi)Z\), taking the local ordering signs in the two factors into account. Hence a transposition is an orientation-reversing self-homeomorphism. Its pullback acts by an isometry from the intersection form to its negative. Consequently its real signature equals its own negative, and \(\sigma(M)=0\).

**3. Evenness by an exhaustive finite cochain lemma.** All calculations in this paragraph take place over \(\mathbb F_2\). The cochain differential is the mod-two transpose of the signed product-cell boundary. Direct Gaussian elimination gives the four consecutive coboundary ranks
\[
(41,169,281,139).
\]
Hence \(\dim C^2=490\) and \(\dim Z^2=490-281=209\), while \(\dim H^2=209-169=40\). The standalone script `verify.py` builds these matrices from the cell definition, checks differential composition, and produces a **full 209-vector nullspace basis**, not a sample of cocycles.

For two degree-two cochains \(u,v\), the Alexander–Whitney diagonals on the two ordered simplex factors give the following evaluation on the mod-two fundamental cycle:
\[
\big\langle u\smile v,[M]_2\big\rangle
=\sum_{\substack{A\cap B=\varnothing\\ |A|=|B|=3}}
\sum_{i=0}^{2}
 u(A_{\le i},B_{\le 2-i})\,
 v(A_{\ge i},B_{\ge 2-i})\quad\text{in }\mathbb F_2.
\]
Here \(A_{\le i}\) means the first \(i+1\) ascending elements, \(A_{\ge i}\) the suffix from index \(i\), and similarly for \(B\). The expression is the usual product-cell cup product; signs disappear over \(\mathbb F_2\). Exhaustive evaluation yields zero self-pairing on **each** of the 209 nullspace-basis cocycles. By graded commutativity of cohomology over \(\mathbb F_2\), the evaluated square \(u\mapsto\langle u\smile u,[M]_2\rangle\) is additive on cocycles. Therefore every mod-two degree-two cocycle squares to zero. In particular, reducing any integral class modulo two shows that the integral intersection form has even diagonal values. As a separate cross-check, the computed mod-two pairing on a 40-vector quotient basis of \(H^2\) is alternating and has rank 40.

**4. Integral lattice and homeomorphism.** Poincaré duality makes the free integral intersection lattice unimodular. It is even (Step 3), has rank 40 (Step 1), and signature zero (Step 2), hence is indefinite with 20 positive and 20 negative directions. Classification of even indefinite unimodular symmetric integer bilinear forms identifies it with \(H^{\oplus20}\). The target \(\#_{20}(S^2\times S^2)\) has precisely that form. By Freedman's classification of simply connected closed topological four-manifolds (the even-form case), \(M\) is homeomorphic to that target. This establishes the claimed topological, **not differential**, classification.

## Verification
Run `python3 verify.py` in the directory containing this result. No third-party modules or downloaded datasets are required. Its exact recorded output is in `CHECK_OUTPUT.txt`. Reproduction performs explicit enumeration, four mod-two boundary ranks, differential-squared checks, a complete signed top-cycle boundary check, orientation-reversal checks for a transposition, a full kernel-basis test of 209 cocycles, all 209 mod-two cup squares, and a 40-by-40 alternating intersection-pairing rank test.

The finite computation is exhaustive because the seven-vertex cell enumeration covers every disjoint nonempty ordered pair of faces of size at most three, and binary elimination constructs a basis for the *entire* cocycle kernel. The topological passage from those finite identities to a homeomorphism uses the separately identified manifold, simple-connectivity, Poincaré duality, integral-form and Freedman theorems.

## Relationship to prior work
The 2023/2025 González–González paper computes connectivity and Betti numbers, including the 40 middle-dimensional generators, but does not determine the middle intersection form or homeomorphism class. The November 9, 2026 paper of González, González and Pérez-Morales proves the four-manifold property and specifically identifies the intersection form as the missing datum in dimension four. Its Conjecture 1.6 predicts the homotopy type of connected sums of sphere products for all parameters. The present calculation supplies the missing evenness and signature in the first higher-dimensional middle-skeleton case, and proves that conjectured type up to **homeomorphism** at parameters \((p,q)=(2,2)\).

Classical van Kampen–Flores work on embedding obstructions involves the same underlying two-skeleton, but its obstruction lives in the particle-exchange quotient and does not determine the covering four-manifold's integral intersection form. No claim is made that the full all-parameter conjecture follows.

## Limitations
Only the seven-vertex two-skeleton and **ordered** two-point deleted product are classified. The calculation does not prove a diffeomorphism classification, an equivariant classification under factor exchange, or a corresponding assertion in higher even dimensions or unequal skeleton dimensions. The proof uses the published manifold and connectivity theorems as prerequisites and a finite, independently replayable cochain computation for the new intersection-parity fact. A separate mathematical audit is outstanding; an exact search cannot rule out unpublished or differently indexed equivalent work.

## References
1. E. J. González, J. González and M. C. Pérez-Morales, *Discrete Configuration Spaces of Simplex Skeleta: a Middle-Dimensional Manifold Phenomenon*, arXiv:2611.12847v1, first posted November 9, 2026. https://arxiv.org/html/2611.12847v1
2. E. J. González and J. González, *An algorithmic discrete gradient field for non-colliding cell-like objects and the topology of pairs of points on skeleta of simplexes*, arXiv:2307.14454v1, first posted July 26, 2023; *Selecta Mathematica* 31 (2025), article 60. https://arxiv.org/abs/2307.14454 ; https://doi.org/10.1007/s00029-025-01043-8
3. M. H. Freedman, *The topology of four-dimensional manifolds*, *Journal of Differential Geometry* 17 (1982), 357–453. https://doi.org/10.4310/jdg/1214437136
4. J. Milnor and D. Husemoller, *Symmetric Bilinear Forms*, Springer, 1973 (classification of indefinite unimodular forms).
