# Review: A fixed-point entropy rebound in generalized Petersen majority dynamics

## Correctness

**PASS.** The transfer-graph bijection checks each outer and inner cubic majority condition exactly for all admissible circumferences, not just a finite experiment. Exact cyclic SCC decompositions and integer characteristic polynomials give the all-size fixed-state count. Primitive Perron components and exact Collatz–Wielandt certificates give strict entropy intervals. The independent brute-force enumerator agrees through circumference eleven. The analytic claims apply to \(n\ge7\) and count only one-step fixed states.

## Originality

**PASS, with priority qualification.** The closest existing generalized Petersen inner-stride-two census already fixes the ninth-degree factors and associated entropy; that is comparison evidence, not a novel result here. Karami's published \(GP(n,3)\) perfect two-colorings require equitable color classes; a majority-fixed nonequitable coloring on \(GP(8,3)\) shows that classification does not cover all fixed points. General majority convergence, XOR-parity and matching-cut decision methods do not imply the new stride-three spectral decomposition. Unindexed matching-cut tables and incompletely accessible historical sources leave a priority risk.

## Mathematical value

**PASS.** The exact fixed-population entropy for the complete natural \(GP(n,3)\) family is motivated by locally stable binary spin states. Its comparison with strides one and two reveals a nonmonotone rebound in the exponential equilibrium population: \(lpha_2<lpha_3<lpha_1\). This distinguishes graph-network effects that are invisible from size or degree alone, without alleging a theorem about arbitrary strides or attraction basins.

## Evidence and limits

All fixed-point conditions, transfer matrices, roots and Perron inequalities are reproducible from `check_transfer.py`; independent direct enumeration is `direct_check.cpp`. Outputs are recorded in companion files, and required Python dependencies are stated in `requirements.txt`. Exact integer/algebraic verification supplies the proof steps; finite brute-force runs alone do not certify all sizes. Remaining limitations: unknown historical priority beyond accessible literature and no external independent review.

Self-review: passed. Independent audit: not yet performed.
