---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The decaying solution has exponents -k_i on the positive side and r_i on the negative side. Continuity removes the distributional delta-prime term, and the derivative jump fixes A_i=Q/S_i, with S_i=D(k_i+r_i). Dividing the quadratic for k_i by k_i gives w+u_i=lambda/k_i-D k_i, so V/Delta=D+lambda/(k_1 k_2). In particular the slope ordering is necessary. With z=D Delta^2/V, the positivity constraints are exactly 0<z<Delta and R=(k_1+z)/(k_2-z). This strictly increasing ratio has the stated open endpoint values. Reconstructing D and lambda by these relations, w by either slope, and Q=A_1 S_1 gives two positive widths S_i and reproduces both amplitudes and slopes; thus the inequalities suffice, including the strict exclusion of both boundary values. With one condition, D and lambda can vary freely while maintaining the whole downstream curve. In a 2+1 split the singly sampled curve admits an arbitrary sufficiently small slope perturbation compensated by its amplitude; feasibility is open and the inverse maps the perturbed invariants to distinct parameters. Repeated locations or fewer readings cannot improve identification. This is an independent algebraic check of RESULT.md, lines 50–108. The packaged run claimed in VERIFICATION.md was inspected as recorded evidence, not rerun or relied on.

## originality

PASS

To the best of the evidence compared, the distinct contribution is the global, sharp four-scalar identification and exact feasible-data interval with two known additive offsets and a fixed known source. The forward Green function and extracting an exponential slope are not new. The most relevant distinct same-day records have different unknowns or data, and the inspected forward literature does not imply the inverse. The title-only comparisons below leave an access risk, not evidence of coverage.

## value

PASS

The same idealized positive-side curve always compresses to two numbers. It matters experimentally whether a known shift of advection, without changing the other coefficients or sampling the other half-line, breaks that ambiguity. The theorem yields a minimal measurement design and an exact consistency test for all positive data, with a constructive local ambiguity for every smaller design. Those features go beyond a forward formula or an isolated inversion witness. The value is structural identifiability in the stated steady model, not a claim of conditioning, field feasibility, or performance with noise.

The dated certificate retains the supplied scientific assessment, sources and limitations.
