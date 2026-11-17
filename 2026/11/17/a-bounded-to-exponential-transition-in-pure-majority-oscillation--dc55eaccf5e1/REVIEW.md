# Review of pure majority oscillations on cyclic clique strips

## Correctness — PASS
The claim specifies labelled \(C_n\square K_r\), \(n\ge3\), \(r\in\{3,4\}\), and incumbent tie retention. Every counted state satisfies \(F(x)=\bar x\), which is genuinely period two because complement equivariance gives \(F^2(x)=x\). The local same-neighbor threshold is at most one for width three and at most two for width four. This forces alternate complementary columns in the unbalanced cases; for balanced four-bit columns the condition is exactly the prohibition of a constant horizontal triple in each row. The resulting 36-state transfer matrix encodes a complete bijection to labelled cyclic words. Its characteristic polynomial is computed with exact integer arithmetic; rational cubic sign intervals and a strict integer Schur reduction establish the isolated dominant root. Direct vertex-level enumeration checked 20,292,096 initial states, independently of the transfer enumeration. No finite experiment is mistaken for an infinite-family proof.

## Originality — PASS, with historical limits
The relevant published fixed-state census on the same triangular cylinder proves a formula for \(F(x)=x\), and explicitly excludes the present pure-two-cycle population. A 1980 general period bound does not yield counts; the 2014 graph-majority paper concerns convergence and disagreement, and the 2022 classification of pure two-cycles assumes trees, not clique cylinders. Available prior local claims were compared by the counted dynamical condition and family; no same-object equivalent or stronger general result covering this width-three/four transition was identified. Unindexed or historically inaccessible publications remain a residual priority risk. Bibliographic comparison cannot prove universal uniqueness.

## Value — PASS
The two consecutive, natural clique-strip widths exhibit fundamentally different abundance of completely synchronous oscillations: at width three the count is uniformly bounded, whereas at width four it has positive entropy \(\log\lambda\). The matrix and full algebraic factorization give an exact count at every circumference, not a sampled table. This isolates a combinatorial mechanism for a local coordination-to-oscillation growth transition. It makes no claim about all-width behavior or complete oscillatory basins.

## Reproducibility and literature
Exact matrix checks, strict Schur root reductions, brute-force vertex checks, their output files, and explicit formulas are embedded. Closest sources are Goles–Olivos (1980), Benjamini et al. (arXiv:1405.2486), Turau (arXiv:2202.01580), and the full readable published published-finding corpus/2026 result `874a8ff5f9e5`. Independent mathematical validation has not been performed.

Self-review: passed. Independent audit: not yet performed.
