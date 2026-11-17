# Thirteen exact Euclidean corner-distance shells of the binary \([15,4,8]\) simplex-code polytope

## Finding
For the binary \([15,4,8]\) simplex-code polytope \(P\subset\mathbb R^{15}\), the squared distances from all 32,768 binary cube vertices to \(P\) occupy **exactly thirteen rational shells**. The following table gives the complete spectrum; the last column is the number of strictly positive barycentric coordinates of the unique nearest point in the fifteen-dimensional codeword simplex.

| Squared distance | Corners | Positive projection weights |
| ---: | ---: | ---: |
| \(49/15\) | 16 | 15 |
| \(18/7\) | 240 | 7 |
| \(12/5\) | 448 | 10 |
| \(25/11\) | 1680 | 11 |
| \(27/13\) | 560 | 13 |
| \(29/14\) | 6720 | 7 |
| \(2\) | 6720 | 4 |
| \(5/3\) | 7168 | 6 |
| \(3/2\) | 6720 | 3 |
| \(4/3\) | 560 | 3 |
| \(6/5\) | 1680 | 5 |
| \(7/9\) | 240 | 9 |
| \(0\) | 16 | 1 |

Exactly 16 cube corners maximize the distance, with squared maximum \(49/15\). They are the bitwise complements of the 16 codewords. Exactly 240 cube corners lie on the next deepest shell, with squared distance \(18/7\); these are exactly the single-coordinate flips of those complements. Thus the distance gap between the deepest two discrete shells is \(49/15-18/7=73/105\).

## Assumptions and scope
The code coordinates are indexed by the nonzero vectors \(v\in\mathbb F_2^4\). For each \(a\in\mathbb F_2^4\) define \(c_a(v)=a\cdot v\pmod2\) and \(C=\{c_a:a\in\mathbb F_2^4\}\). Let \(P=\operatorname{conv} C\subset\mathbb R^{15}\) with the ambient standard Euclidean norm. A *cube corner* means \(x\in\{0,1\}^{15}\), not an arbitrary point of \([0,1]^{15}\). The shell count concerns the finite multiset of all 32,768 corner-to-polytope squared distances, not the Hamming covering-radius distribution and not the distance to the discrete set of codewords.

## Proof
Any two distinct codewords have Hamming (hence squared Euclidean) distance eight, by the balanced-value property of nonzero binary linear forms. Consequently the 16 points of \(C\) form a full-dimensional regular simplex in \(\mathbb R^{15}\). Writing \(N=16\) and \(\overline c=N^{-1}\sum_a c_a=\tfrac12\mathbf1\), the centered Gram matrix is \(4(I-\mathbf1\mathbf1^\top/N)\). Every ambient \(x\) has unique affine barycentric coordinates \(\beta_a\) satisfying \(\sum_a\beta_a=1\), with
\[
\beta_a=\frac{b_a}{16},\qquad b_a=16-2\bigl(|c_a|+|x|\bigr)+4|\operatorname{supp}(c_a)\cap\operatorname{supp}(x)|.
\]
Here \(|z|\) is the number of ones in a binary vector. In particular \(\sum_ab_a=16\). By the Gram identity, for barycentric \(\alpha\) of any point of \(P\), its squared Euclidean distance from \(x\) is
\[
\|x-\sum_a\alpha_ac_a\|_2^2=4\sum_a(\alpha_a-\beta_a)^2,
\qquad \alpha_a\ge0,\quad \sum_a\alpha_a=1.
\]
Therefore orthogonal projection onto \(P\) is exactly the Euclidean projection of \(\beta\) to the probability simplex. Its unique Karush–Kuhn–Tucker solution is
\[
\alpha_a=\frac{(b_a-t)_+}{16},\qquad \sum_a(b_a-t)_+=16,
\quad \operatorname{dist}(x,P)^2=\frac1{64}\sum_a\bigl((b_a-t)_+-b_a\bigr)^2.
\]
The threshold \(t\) is uniquely determined, including at ties, by the mass equation; the number of positive weights is the number of \(b_a>t\).

The supplied standard-library-only `verify_spectrum.py` enumerates the integers from \(0\) through \(2^{15}-1\), interprets each as a cube corner, computes its 16 integer \(b_a\) values, determines \(t\) using exact rational arithmetic and a sorted active-set loop, and counts each squared-distance/support-size pair. At every iteration it checks \(\sum b_a=16\), \(\sum b_a^2=256\), primal feasibility, complementary-slackness/KKT conditions, and the distance formula. Its final assertions check every table entry and the total 32,768, as well as equality of the maximum shell with all codeword complements and of the second shell with their coordinate flips. The search visits every possible cube corner without pruning or numerical approximation; together with the preceding exact projection identity, the terminating program supplies a finite exhaustive proof of the displayed spectrum.

The complement set has 16 distinct corners. Since any two distinct simplex codewords differ in eight places, all their one-bit complement-neighbors are distinct, giving exactly \(16\cdot15=240\) points. The exact final set equalities establish the asserted two deepest shell classifications.

## Verification
Running `python verify_spectrum.py` produces `SIMPLEX15_EXACT_PASS inputs=32768 shells=13 max=16 next=240`; this was checked using the packaged source. A separate optional script `verify_secondary.py` uses the original 15-coordinate vertices and constrained numerical quadratic programming in SciPy for 37 specified corners, and prints `SIMPLEX15_QP_PASS samples=37`. These checks are different in purpose: the exhaustive rational checker certifies the finite case, while the nonlinear optimizer independently corroborates selected distances. The main proof uses exact arithmetic and does not infer an infinite-family theorem from enumeration.

## Relationship to prior work
The codeword-polytope viewpoint underlies Rosnes and Helmling (2017), which develops inequalities for single parity-check codes, and Coregliano, Jeronimo and Jones (2021), which develops linear-programming bounds for linear-code size. Their verified available abstracts describe neither the exact Euclidean corner-to-polytope spectrum for this binary simplex code nor the complete nearest-face support table. The binary Hamming code's convex-hull geometry concerns the dual code and does not directly imply the present simplex-code distances. The regular-simplex projection and threshold method are standard, not novel; the contribution asserted here is the complete exact specialized shell classification and its two outer level configurations. Full-text priority across coding-theory sources remains provisional.

## Limitations
The exact thirteen-shell result is for the canonical 15-coordinate code and all binary corners only. No claim of the same thirteen levels for longer simplex codes, no all-point distance distribution on the continuous cube, and no novel projection algorithm are made. The scientific significance lies in a complete finite geometric invariant for a natural coding polytope; it should not be conflated with a new broad code-theoretic decoding theorem. Independent scholarly audit and exhaustive historical priority checking have not been carried out.

## References
1. E. Rosnes and M. Helmling, “Adaptive Linear Programming Decoding of Nonbinary Linear Codes Over Prime Fields,” first public preprint 2017-08-23, arXiv:1708.06959. https://arxiv.org/abs/1708.06959
2. L. N. Coregliano, F. G. Jeronimo, and C. Jones, “A Complete Linear Programming Hierarchy for Linear Codes,” first public preprint 2021-12-16, arXiv:2112.09221. https://arxiv.org/abs/2112.09221
