---
{"schema_version":1,"audit_date_utc":"2026-10-01","status":"failed"}
---

# Independent mathematical audit

## Final claim

At the ML-KEM-768 modulus and the stated variance matching, the proposed uniform 8% characteristic-function envelope is false: at frequency 768 the centered-binomial to rounded-Gaussian ratio is below 0.92.

## Correctness — PASS

The exact certificate was reconstructed from the actual verifier. It brackets the variance-matched Gaussian scale in (0.955, 0.96), bounds the centered-binomial characteristic function from above and the rounded-Gaussian characteristic function from below at frequency 768, and proves the ratio is below 0.92. An independent high-precision recomputation gives scale about 0.9574271350 and ratio about 0.899631866, consistent with the rigorous witness.

Checked sources: artifacts/verify_counterexample.py (blob 6f26b771b8ca2051087c82a5d3c8680e032d5edb); NIST FIPS 203 parameter definitions

Residual risks: The certificate is a one-frequency refutation; it does not identify the optimal uniform constant.

## Originality — PASS

Searches of the relevant standard, Kyber documentation, a lattice-cryptography Gaussian comparison source, and the published mathematical corpus did not locate an earlier theorem giving this exact pointwise counterexample or a stronger bound that directly implies it. The standard fixes the parameters but does not state the disputed 8% envelope.

### Equivalent formulations

The claim was compared as a pointwise characteristic-function ratio statement, not merely by matching distribution names. Evidence: NIST FIPS 203 specifies the ML-KEM parameters but contains no pointwise 8% Fourier-envelope theorem.

### Broader coverage

No broader theorem located was shown to imply the certified violation. Evidence: General distribution-comparison literature was found, but no inspected statement dominates the concrete ratio bound at the audited frequency.

### Exact database or table

No exact external table was found that already records the counterexample. Evidence: The only direct record located was the present mathematical record; standards and parameter tables contain no such ratio table.

### Claim versus prior implication

The prior standard does not imply either the proposed 8% envelope or its refutation. Evidence: The standard supplies the parameter regime, not the disputed analytic inequality.

### Source inspections

- **FIPS 203: Module-Lattice-Based Key-Encapsulation Mechanism Standard** — https://doi.org/10.6028/NIST.FIPS.203. Trigger: Primary source for the ML-KEM parameter regime. Material read: Parameter definitions and the ML-KEM-768 parameter table. Method: Primary standard inspection. Assessment: NOT_COVERING. Evidence: The standard fixes the modulus and noise parameters but does not assert a uniform characteristic-function comparison with a rounded Gaussian.
- **Kyber specification, Round 2** — https://pq-crystals.org/kyber/data/kyber-specification-round2.pdf. Trigger: Primary scheme specification cited by the record. Material read: Noise-distribution and parameter context relevant to the centered-binomial model. Method: Primary specification inspection. Assessment: NOT_COVERING. Evidence: The inspected material defines the scheme distribution but does not state the audited 8% envelope.

Checked sources: https://doi.org/10.6028/NIST.FIPS.203; https://pq-crystals.org/kyber/data/kyber-specification-round2.pdf; https://eprint.iacr.org/2015/046

Residual risks: An unpublished or non-indexed engineering note could contain the same numerical observation; no such source was located.

## Scientific value — FAIL

The refutation is mathematically correct, but the audited final claim is a single-frequency negative check against an externally unmotivated 8% threshold. It supplies neither a corrected sharp envelope nor a cryptographic consequence showing that this particular discrepancy matters. Under the value bar for narrow negative checks, the exact witness alone is insufficient.

Checked sources: NIST FIPS 203; Kyber specification; package certificate

Residual risks: A demonstrated consequence for a proof reduction, estimator, or concrete security calculation could make a corrected result valuable, but no such consequence is part of the claim.

## Disposition

FAILED. Acceptance requires PASS on correctness, originality, and scientific value.
