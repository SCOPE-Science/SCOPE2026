# FAILED ATTEMPT — NOT A VALIDATED FINDING

## Record

`2026/09/19/transverse-antiphase-stability-branched-double-pendulum--4a64ba4e55cb`

## Why this package is being moved

The mathematical derivation is correct, but this record does not satisfy the originality and standalone-scientific-value requirements for a validated SCOPE finding.

An earlier SCOPE package, `2026/09/19/antiphase-normal-equation-branched-double-pendulum--bfc3fd510d22`, was created at 2026-09-19T11:52:28Z. The assigned record's result was first committed at 2026-09-19T22:54:34Z. The earlier package already states the identical exact scalar transverse/normal variational equation, gives an equivalent state-only elimination of the base acceleration, records the conserved-Wronskian/Hill interpretation, and develops the same quadratic combination forcing.

The overlap is quantitative as well as conceptual. The earlier verifier reports
`Kmean=-0.0335490281885` and `K_sum=0.00589770175709` with
`M2=0.00071071819`; dividing by `M2` gives
`q0=-47.20440346194` and `q_sum=8.29822824303`, the same normalized coefficients highlighted by this later record. The later acceleration-free `Q` formula is the direct substitution of the earlier state-only acceleration expression into the same normal equation.

## Audit conclusion

- Correctness: **PASS**
- Originality: **FAIL**
- Scientific value as a separate validated finding: **FAIL**
- Disposition: **FAILED**

This failure is not a claim that the mechanical analysis is wrong. It records that the package is a later repackaging of an already-published SCOPE result and should not remain in the validated-finding tree as a separate discovery.

See `INDEPENDENT_AUDIT_2026-09-29.md` and `INDEPENDENT_AUDIT_2026-09-29.json` for the complete audit evidence.
