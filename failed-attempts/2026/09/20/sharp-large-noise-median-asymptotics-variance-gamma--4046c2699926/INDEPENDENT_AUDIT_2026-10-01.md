# Independent scientific audit — SCOPE-20260920-4046c2699926

Audited at: 2026-10-01T21:06:11.107600Z

Disposition: **failed**

## Correctness — PASS

The exact beta probability deficit at zero and the variance-gamma Bessel density give a median equation whose five balances are controlled by the standard small-argument branches of \(K_\nu\). The constants agree with the independent earlier derivation after normalization: the \(r<1\) factor, the two-logarithm \(r=1\) denominator, the \(1<r<3\) coefficient, the \(r=3\) logarithmic term, and the \(r>3\) coefficient all match. The exact \(r=2\) asymmetric-Laplace formula is a separate consistency check. The numerical artifact supports, but is not used to prove, the asymptotics.

### Correctness sources

- assigned RESULT.md
- assigned artifacts/verify_asymptotics.py
- Gaunt-Ouimet arXiv:2609.20212
- published SCOPE 2026-09-18 five-regime theorem

### Correctness risks

- The expansions are pointwise in fixed \(r\), as stated.

## Originality — FAIL

A published 2026-09-18 SCOPE record states the identical five-regime variance-gamma median asymptotics with the same constants and critical laws, including the refined \(r=1\) denominator and the \(r=3\) logarithmic crossover. The assigned 2026-09-20 claim is therefore fully covered by an earlier stronger/equivalent record.

### Equivalent formulations

The formulas are algebraically identical, not merely similar.

### Broader coverage

The earlier SCOPE theorem covers every component of the final assigned claim.

### Exact database or table

This exact same-object hit is decisive prior coverage.

### Claim versus prior implication

The assigned theorem is a restatement/alternate derivation of the earlier result.

### Sources inspected

- Sharp large-noise asymptotics for variance-gamma medians — published record 2026/09/18/variance-gamma-median-large-noise-phase-transitions--2d5865f4207e. COVERING: It contains the complete assigned theorem two days earlier.
- Bounds for the median of the generalized hyperbolic and related distributions — https://arxiv.org/abs/2609.20212. BACKGROUND: It motivates the endpoint limit; the decisive rate coverage is the earlier SCOPE theorem.

### Checked sources

- published SCOPE 2026/09/18/variance-gamma-median-large-noise-phase-transitions--2d5865f4207e
- https://arxiv.org/abs/2609.20212
- Resultary semantic search

### Residual risks

- None relevant to the rejection: exact earlier coverage is explicit.

## Value — FAIL

The five-regime asymptotic theorem is worthwhile mathematics, but this assigned record contributes no distinct result beyond an already-published theorem on the identical distribution and normalization. A redundant rederivation does not establish separate scientific value.

### Value sources

- published 2026-09-18 five-regime theorem

### Value risks

- Independent derivation may aid reproducibility, but reproducibility alone is not new research value.

## Limitations

- Scientific rejection is for originality and value, not correctness.
- The asymptotics are pointwise for fixed shape and asymmetry.
- No uniform crossover theorem near \(r=1\) or \(r=3\) is claimed.
