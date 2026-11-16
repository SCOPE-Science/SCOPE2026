# Scientific review

## Correctness: PASS
The covariance is obtained independently from the transfer-current projection and spanning-tree enumeration. Fourier decomposition gives the finite spectrum. Algebraic limiting-symbol identities and a uniform rank-one perturbation argument prove the sharp linear condition coefficient. `check_mobius.py` passed direct pseudoinverse comparisons for sizes 3–30, direct enumeration for sizes 3–6, and further large-order numerical tests. `symbolic_certificate.py` passed exact radical identities. The theorem does not infer an infinite statement solely from finite computations.

## Originality: PASS (historical priority provisional)
Azimi–Farrokhi (2023, arXiv:2306.10497v1) gives Möbius-ladder pseudoinverses and tree counts; its Section 5 and corollaries were inspected. Those are inputs, but do not state the edge-occupation Fourier covariance conditioning law. The classical tree-determinantal formula is credited. A publicly indexed wheel-graph covariance result concerns a different graph and a quadratic law, so it does not imply the Möbius-ladder linear coefficient. Search coverage and source-specific implications are recorded in `AUDIT.json`. Potential unindexed structure-factor antecedents remain a priority risk.

## Mathematical value: PASS
The first-coordinate observation covariance of a natural spanning-tree ensemble has a nontrivial Fourier soft mode with exact \(1/(3n)\) decay, producing sharp \(\sqrt3/2\) linear conditioning rather than the quadratic wheel rate. The result also supplies all finite Fourier blocks, the exact rank, and reproducible independent covariance checks.

## Limitations
The theorem does not optimize the finite-dimensional largest-frequency labels at every size or address higher-order sampling. Historical priority is provisional and no independent mathematical audit has been performed.

Self-review: passed. Independent audit: not yet performed.
