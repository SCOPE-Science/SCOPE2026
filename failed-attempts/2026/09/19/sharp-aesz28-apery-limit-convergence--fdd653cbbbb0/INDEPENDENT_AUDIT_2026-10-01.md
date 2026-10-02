# Independent scientific audit — SCOPE-20260919-fdd653cbbbb0

Audited at: 2026-10-01T15:09:23.525185Z

Disposition: **failed**

## Correctness — PASS

The positive double-binomial phase has a unique interior saddle at \((3/4,3/4)\); the Hessian and Stirling prefactor give \(A_n\sim(2\sqrt6/(3\pi^2))64^n/n^2\). Combining that with the exact positive Casoratian gives the increment asymptotic, and the geometric tail ratio \(1/64\) yields \(\zeta(3)/7-C_n/A_n\sim(\sqrt2\pi^3/84)64^{-n}\). The exact recurrence, binomial checks, Casoratian checks, and high-precision diagnostics corroborate the calculation.

### Correctness sources

- assigned RESULT.md
- assigned artifacts/verify.py
- Bachmann arXiv:2609.18271
- published stronger SCOPE AESZ-28 result

### Correctness risks

- The finite verifier does not prove the lattice Laplace asymptotic; correctness rests on the analytic saddle argument.

## Originality — FAIL

A separate published SCOPE record for the identical AESZ-28 recurrence states the same leading constant and strictly stronger asymptotics, including the first \(1/n\) correction, a sharp linear-form asymptotic, and an exact positive series. Therefore the assigned theorem is already contained as a special case of stronger published coverage.

### Equivalent formulations

Taking only the leading term gives exactly the assigned claim.

### Broader coverage

It strictly dominates the final claim on the same recurrence and normalization.

### Exact database or table

This exact same-object hit is decisive prior coverage.

### Claim versus prior implication

The final claim is a direct corollary of the stronger published result.

### Sources inspected

- Sharp convergence of the AESZ-28 Apéry approximants to \(\zeta(3)\) — published SCOPE record 2026/09/19/sharp-convergence-aesz28-apery-limit--b8f8144d73bc. COVERING: It strictly contains the assigned leading-equivalent claim.
- A q-recurrence for a finite Apéry limit — https://arxiv.org/abs/2609.18271. BACKGROUND: The decisive originality failure comes from the stronger published SCOPE theorem, not from Bachmann's source.

### Checked sources

- published SCOPE 2026/09/19/sharp-convergence-aesz28-apery-limit--b8f8144d73bc
- https://arxiv.org/abs/2609.18271
- Resultary semantic search

### Residual risks

- The exact publication ordering of two same-day internal records is not needed for the current audit: the stronger theorem is published coverage at the audited snapshot and strictly contains the assigned result.

## Value — FAIL

As a mathematical fact the leading constant is worthwhile, but this assigned record is redundant with a stronger published theorem on the identical recurrence. Re-validating a known leading term separately does not constitute a distinct new finding.

### Value sources

- published stronger SCOPE AESZ-28 theorem

### Value risks

- The proof remains a useful independent derivation, but reproducibility is not the same as new scientific value.

## Limitations

- Scientific rejection is for originality and value, not correctness.
- The result concerns only AESZ no. 28 and does not improve an irrationality measure for \(\zeta(3)\).
