# Independent mathematical audit

## correctness

PASS

I reconstructed the line set independently by enumerating the 7462 reduced row echelon two-spaces over F_9 and testing the Hermitian pairing on the two basis rows. Completeness over the algebraic closure follows both from the published 112-line theorem and directly: vanishing of the four Hermitian coefficients on a line with vector space W gives W=(W^[3])^perp for the ordinary dot product; cubing gives W^[3]=(W^[9])^perp, so W=W^[9] and its unique row echelon matrix is over F_9. A two-by-two residual determinant tests geometric meeting of distinct lines. The independent calculation recovered 48 and 64, quotient ((14,16),(12,18)), characteristic polynomial (T−18)(T−2)^43(T+2)^6(T+6)^12(T+10)^2, and every one of the 48 augmented Gram ranks 22 modulo 101. Replay: python /workspace/branches/independent_fermat.py (SymPy); output /workspace/branches/independent_fermat.log. The modular ranks give rational lower bounds, which attain the Picard rank 22. By adjunction a line has square −2; in a smooth surface the distinct tangent directions of intersecting lines give local intersection one. For D the excess sum, D·H=64 and D²=64(18−2)=1024, so the H-orthogonal class D−16H has square zero. Hodge index forces it to be numerically trivial; a numerically trivial line bundle on a K3 is trivial by Riemann–Roch and duality, since neither sign of a nontrivial numerically trivial bundle has a nonzero effective divisor. Thus D=16H in NS, and the 21-dimensional Gram rank is the span dimension since the span contains H and the form restricts nondegenerately. No integral index or nondeformability assertion follows.

## originality

FAIL

The published full generalized quadrangle, the indexed exact classical-block spectrum and incidence rules, and the distinct indexed excess-orbit description determine all the submitted numerical and geometric conclusions by complementary compression of an orthogonal projection and elementary intersection theory. The excess polynomial need not be printed in earlier work to be a direct consequence. This is established implication, not a priority inference from the same-day dates, and not merely a suspicion about an unseen table.

## value

FAIL

The subset and its Picard span are intrinsically natural, but the exact narrow invariant submitted is a mechanical complementary compression of the tabulated classical block in the known full graph using the verified orbit description. The remaining divisor sum and one-line completion are elementary consequences of that calculation and full rank. No further independent useful invariant, such as integral saturation, is established by this record.

The dated certificate retains the supplied scientific assessment, sources and limitations.
