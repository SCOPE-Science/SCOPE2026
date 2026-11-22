# Scientific evaluation

## Correctness — PASS

For each integer \(d\ge2\), tensor Walsh diagonalization gives the stated rational formula for the opposite-corner inverse entry. Its numerator has degree exactly \(d-1\), as the first nonzero term at large \(t\) is negative and proportional to \(t^{-2}\). A binomial finite difference of the logistic function has vanishing moments through degree \(d-2\), forcing at least \(d-1\) distinct sign changes on the real line. The degree bound makes all zeros simple and exhausts them. Reciprocal symmetry and the three-dimensional explicit example follow by direct algebra. The bundled standard-library exact-arithmetic checker returned `VERIFY_OK 261` for finite test dimensions; no infinite assertion rests on the checker.

## Originality — PASS, with residual risk

The eligible motivating paper (Krzysik, Southworth and Wimmer, arXiv:2607.12138) develops local mass inverse and additive Schwarz spectral estimates but not a complete, dimension-uniform count of blended inverse-entry sign reversals. A later exact hexahedral mixed-inverse paper (Hanukah, arXiv:2611.21820, publicly released after the eligibility anchor) already implies the specific \(d=3\) two-zero example, which is expressly **not** claimed as novel. Bernstein mass inversion (Allen and Kirby, arXiv:1907.05773) treats different mass families. The closest mathematical-record findings concern time-dependent FE heat propagation and do not imply zero counting as the mass-blend parameter changes. An unindexed equivalent finite-difference or rational-function theorem cannot be ruled out.

## Mathematical value — PASS

Signed inverse couplings of positive-definite blended mass matrices are a natural numerical-algebra question in element-local mass inversion and positivity-sensitive computation. An exact \(d-1\) count for every tensor dimension, with simple crossing and reciprocal pairing, clarifies how inverse-entry signs can oscillate arbitrarily many times without any loss of positive definiteness. The theorem is structural, not a claim of solver instability. It requires a pure tensor-product orthotope; ordinary physical elements are two- or three-dimensional, while larger dimensions are a natural mathematical benchmark.

## Limits

No assembled-mesh, runtime, physical positivity, or error/stability statement is inferred. Historical priority depends on the literature available and is not independently certified. The precise \(d=3\) special case is already covered by a later accessible paper; novelty is assessed only for the all-dimensional zero-count and involution.

Self-review: passed. Independent audit: not yet performed.
