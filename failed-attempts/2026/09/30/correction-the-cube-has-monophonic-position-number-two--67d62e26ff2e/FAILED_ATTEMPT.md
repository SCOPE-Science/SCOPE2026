# FAILED ATTEMPT — NOT A VALIDATED FINDING

## Scientific disposition

- Correctness: PASS. After translating one selected vertex to the empty set, write the other two as \(A,B\) and split coordinates into \(A\setminus B\), \(B\setminus A\), and \(A\cap B\). If one set is nested in the other, a geodesic contains all three. Otherwise, delete shared coordinates then private coordinates on the first half and add the other private coordinates then shared coordinates on the second half. Every nonzero vertex on opposite halves differs in at least one coordinate of each private block, so no cross-half chord exists. Thus every triple lies on an induced path and \(\operatorname{mp}(Q_n)=2\). The actual verifier exhaustively checks all triples through \(Q_7\), but the coordinate proof is infinite.
- Originality: FAIL. The corrected numerical formula is already a direct corollary of the later published Cartesian-product inequality \(\operatorname{mp}(G\square H)\le\max\{\operatorname{mp}(G),\operatorname{mp}(H)\}\): iterating from \(K_2\) gives \(\operatorname{mp}(Q_n)=2\). The earlier source does explicitly print the incompatible claim that the cube has monophonic position number four. Identifying that contradiction is useful, but under implication-level originality the mathematical theorem itself is covered.
- Value: PASS. The false cube value is used as a sharpness witness in the defining paper, so explicitly reconciling it with the later product theorem and supplying a direct elementary certificate removes a meaningful literature error. The record fails originality, not motivation.

Acceptance requires all three axes to pass. The complete original package is retained as failed evidence and is not a validated finding.

## Preserved evidence

The original result, slogan, metadata history, verification state, and reproducibility artifacts remain part of the archived package. The dated independent-audit files record the scientific comparison and residual risks.
