# Independent scientific audit — SCOPE-20260920-530e5145f9f6

Audited at: 2026-10-01T21:06:11.107600Z

Disposition: **failed**

## Correctness — PASS

The reversible spectral theorem reduces the observable autocorrelations to moments of a probability measure supported on \([0,\beta]\) with mean \(\rho\). Jensen gives \(\rho_k\ge\rho^k\), while \(\lambda^k\le\beta^{k-1}\lambda\) gives the simultaneous upper envelope. The finite-horizon kernel \(\Psi_n\) and the IAT kernel \((1+\lambda)/(1-\lambda)\) are convex, so the same one-point and endpoint two-point spectral measures give the exact expectation bounds. The refresh-product constructions realize these measures by finite-state positive reversible chains. Letting the upper atom tend to one proves the no-ceiling divergence without using a finite experiment as proof.

### Correctness sources

- assigned RESULT.md
- assigned artifacts/verify.py
- Berg and Song (2023) autocovariance moment representation
- Edmundson-Madansky convex expectation bound

### Correctness risks

- The randomized verifier is corroborative only; all infinite statements were checked from the analytic moment argument.

## Originality — FAIL

Once the published reversible-chain moment representation is combined with the classical fixed-mean convex expectation bounds, every displayed envelope is a direct specialization: Jensen supplies the lower endpoint and the endpoint chord supplies the upper endpoint. The no-ceiling statement is the same endpoint construction with an atom approaching one. The chain-specific finite-state realization is elementary. Under an implication-based originality bar this is covered by classical moment/convex-order machinery rather than a new theorem mechanism.

### Equivalent formulations

The assigned theorem is the one-moment convex-order interval applied to the functions \(x^k\), \(\Psi_n(x)\), and \((1+x)/(1-x)\).

### Broader coverage

The broader machinery immediately dominates the assigned formulas after inserting the relevant test functions.

### Exact database or table

Database absence cannot establish novelty and is not relied upon.

### Claim versus prior implication

No nonstandard lemma remains after the classical representation is exposed.

### Sources inspected

- Efficient shape-constrained inference for the autocovariance sequence from a reversible Markov chain — https://doi.org/10.1214/23-AOS2335. COVERING_INGREDIENT: It explicitly treats reversible autocovariances as moments of a positive spectral measure.
- Edmundson-Madansky convex expectation bound — classical bounded-support moment inequality. BROADER_COVERAGE: The upper bound used in the assigned proof is precisely this classical endpoint-chord inequality.

### Checked sources

- https://doi.org/10.1214/23-AOS2335
- Edmundson-Madansky fixed-mean convex expectation inequality
- published SCOPE two-lag reversible-chain record
- Resultary semantic search

### Residual risks

- No residual source-access issue affects the rejection; coverage is by standard general machinery.

## Value — FAIL

The Monte Carlo interpretation is useful, but the mathematical result is a textbook one-moment convexity specialization once the known spectral representation is written down. The stated value standard rejects such mechanically implied deductions even when the formulas are sharp and reproducible.

### Value sources

- Berg and Song (2023)
- classical Jensen and Edmundson-Madansky inequalities

### Value risks

- This is not a correctness objection and does not deny expository usefulness.

## Limitations

- Scientific rejection is for originality and value, not correctness.
- The formulas require nonnegative observable spectrum for the lower-envelope statements.
- The spectral ceiling is observable-specific unless strengthened to a chain-wide spectral assumption.
