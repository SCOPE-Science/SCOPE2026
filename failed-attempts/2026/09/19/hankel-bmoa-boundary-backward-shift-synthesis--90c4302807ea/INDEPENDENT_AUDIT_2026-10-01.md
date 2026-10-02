# Independent audit — Hankel--BMOA boundary for backward-shift orbit synthesis

Audit date: 2026-10-01 (UTC) UTC

Scientific disposition: **failed**.

## Correctness

**PASS** — The coefficient formula is the Hankel matrix with entries \(lpha_{m+j}\). For coefficients \((n+1)^{-2/3}\), both inputs lie in \(\ell^2\), while the output coefficient is bounded below by a constant times \(m^{-1/3}\), so the output is not square summable. Classical Hankel theory gives the BMOA boundedness boundary. Thus the diagnosis of the universal all-\(H^2\) synthesis claim is mathematically correct.

## Originality

**FAIL** — Originality fails because the central correction and sharp boundary were already published one day earlier.

### Equivalent formulations
The audited record's central claim is an equivalent formulation of that earlier published result.

Evidence: A published 2026-09-18 record already identifies exactly the same Hankel matrix, the same BMOA threshold, an explicit \(H^2\) counterexample, finite-section blowup, and the resulting gap in Lemma 2.1/Proposition 2.2.

### Broader coverage
The remaining precursor observation does not constitute a broader independent theorem.

Evidence: The earlier record already gives the sharp boundary and source-specific correction; the audited record's additional application to the 2024 precursor uses the same obstruction mechanism.

### Exact database or table
This database comparison is decisive against originality.

Evidence: The exact prior record was located and its full proof inspected.

### Claim versus prior implication
Prior implication is decisive; disclaimers cannot rescue the original claim.

Evidence: The core audited conclusions are directly implied by the earlier result. Reusing the same non-Bessel orbit counterexample in an earlier paper is a routine application, not a distinct mathematical boundary.

### Source inspections

- **The sharp BMOA boundary for a backward-shift Hankel operator** — COVERING.
  Identifier: https://github.com/Resultary/2026/tree/main/2026/9/18/SCOPE-bmoa-boundary-backward-shift-hankel-operator--a39ad574fb44
  Material read: complete result and proof.
  Evidence: It proves the identical BMOA boundary, explicit counterexample and source-specific Lemma 2.1/Proposition 2.2 diagnosis one day earlier.
- **Projections and minimal invariant subspaces in the Hardy space over the bidisk** — PRIMARY_CONTEXT.
  Identifier: https://arxiv.org/abs/2609.19311
  Material read: abstract and accessible metadata.
  Evidence: The abstract confirms the projection-rigidity program; full text was not accessible in the available text interface.

### Residual risks

- The source preprint full text was not retrievable through the available text interface, but this access limitation does not override the decisive earlier published coverage.

## Scientific value

**FAIL** — Once the earlier exact correction is accounted for, the remaining contribution is essentially reuse of the same explicit non-Bessel orbit obstruction in a precursor argument. That is a routine application rather than a separately motivated structural result.

## Final assessment

The mathematics of the counterexample is correct, but the claim is rejected because originality and value do not survive the earlier covering result. The original package is retained as failed evidence.

This review does not constitute formal verification or a guarantee against undiscovered prior art.
