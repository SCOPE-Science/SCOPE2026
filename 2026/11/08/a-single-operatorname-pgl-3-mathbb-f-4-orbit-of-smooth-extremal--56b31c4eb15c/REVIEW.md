# Scientific review: smooth extremal Frobenius-nonclassical sextics over \(\mathbb F_4\)

## Correctness — PASS

The precise claim is that all geometrically smooth degree-six Frobenius-nonclassical plane curves over \(\mathbb F_4\) form one rational-projective class, consisting of 960 normalized equations, and have rational projective stabilizer order 63. Theorem 1.6(3) of Asgarli–Duan–Lai supplies the exhaustive smooth-curve normal form. The gradient-zero locus of its fixed differential part consists exactly of 21 rational projective points, proving that the 21-point nonvanishing test is an *if and only if* geometric-smoothness test. Two independent exact-arithmetic enumerators return 960 of 1,048,576 forms. Independently, the C++ program enumerates all 181,440 invertible matrices and determines exactly 189 stabilizing the diagonal representative, with rank-10 interpolation establishing polynomial rather than only pointwise equality; this gives an orbit of 960. The projective action is recovered over the ten-dimensional coefficient space, checked at all 21 points on its basis, and its eight explicit maps connect all 960 solutions. Orbit–stabilizer supplies 63, with no assumption that the eight maps form all of \(\operatorname{PGL}_3(\mathbb F_4)\). Both independent counting and two distinct orbital-check methods were executed successfully. The direct diagonal representative argument corroborates the numerical work.

## Originality — PASS, subject to priority risk

The closest primary source is Asgarli–Duan–Lai, arXiv:2207.11981, Theorem 1.6(3) and Example 4.11: its complete normal form is prior, as is the absence of rational points. It does **not** give a field-specific count, projective orbit, or stabilizer order. Borges–Korchmáros–Speziali, arXiv:2202.05765, Theorem 4.21, is a stronger-looking comparison: it characterizes curves *already invariant under a specified Singer-normalizer* and permits projectivities over \(\mathbb F_{4^3}\). This is not the statement that every smooth Frobenius-nonclassical sextic has that symmetry or one \(\mathbb F_4\)-rational projective orbit. Targeted mathematics literature/database searches and accessible earlier scientific-claim comparisons for the form, its aliases, and the two numerical invariants showed no direct equivalence. Cossidente–Siciliano (2003) classifies smooth curves assuming a Singer group, but only its abstract was accessible directly; a partially overlapping older finite-geometry census remains a real priority risk; negative searches are not uniqueness certificates.

## Mathematical value — PASS

The first nonprime binary field is a natural test case for the published maximal-degree classification. The single-orbit conclusion gives a complete rational-field rigidity result for the entire smooth exceptional class, not a single witness or routine specialization. The sharp number 960 and order-63 stabilizer distinguish rational plane models from projectivity over extension fields, and the diagonal normal form is a compact concrete tool for future study. No extension to arbitrary even fields is asserted.

## Limitations and documentation

The two standalone source files provide complete finite reproducibility, but there has been no independent expert or formal audit. The computational proof pertains to the finite field and its specified projective action; its geometric-smoothness criterion has a complete algebraic justification. The earlier Singer-normalizer work is the most consequential residual priority comparison.

Self-review: passed. Independent audit: not yet performed.
