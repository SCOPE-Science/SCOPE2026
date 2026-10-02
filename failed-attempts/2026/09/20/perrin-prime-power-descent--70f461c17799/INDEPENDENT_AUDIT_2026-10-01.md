# Independent mathematical audit — Prime-power descent for Perrin pseudoprimes

Audit date: 2026-10-01 (UTC) UTC

Scientific disposition: **failed**.

## Correctness

**PASS** — The Perrin companion matrix is integral and unimodular, so the positive- and negative-index trace formulas are valid. The general prime-power trace congruence gives the claimed exponent descent and the square criterion. The package verifier independently reproduces the three listed A173656 square lifts, their cube failures, and failure of the negative restricted congruence. The bounded classification still relies on A173656's completeness statement below ten billion rather than a new exhaustive search.

## Originality

**FAIL** — The central descent theorem is already a direct special case of the published matrix Dold/Gauss congruence. Byszewski–Graff–Ward Corollary 4.5 gives the same prime-power trace congruence for every integral square matrix; applying it to the Perrin companion matrix and its integral inverse yields both asserted Perrin congruences mechanically. The remaining finite classification combines the existing A173656 table with candidate residue checks.

### Equivalent formulations

Searches/sources: Byszewski–Graff–Ward 2021 Corollary 4.5; Zarelua matrix trace congruences; Perrin trace representation.

Evidence: The published corollary gives the prime-power trace congruence for every integral matrix. The Perrin companion matrix and its inverse are integral.

The Perrin theorem is a literal specialization of the broader matrix result.

### Broader coverage

Searches/sources: Dold sequences for traces of integer matrices; matrix Gauss congruence at prime powers.

Evidence: The prior theorem applies to every integer matrix and every prime power.

This strictly broader theorem dominates the claimed descent mechanism.

### Exact database or table

Searches/sources: OEIS A173656; OEIS A013998.

Evidence: A173656 lists 521, 190699, and 36944128783 and states there are no other terms below ten billion.

The finite classification uses an existing database frontier rather than a fresh exhaustive census.

### Claim versus prior implication

Searches/sources: apply the general trace congruence to the Perrin matrix and its inverse; combine with A173656.

Evidence: The two descent congruences and square criterion follow immediately. The bounded list then reduces to existing candidate data plus lift checks.

The main claim is mechanically implied by prior mathematics.

### Source inspections

- **Dold sequences, periodic points, and dynamics** — COVERING.
  Identifier: https://doi.org/10.1112/blms.12531
  Material read: full Wiley HTML including Corollary 4.5
  Evidence: Corollary 4.5 states the exact prime-power trace congruence.
- **OEIS A173656** — COVERING_DATABASE_INPUT.
  Identifier: https://oeis.org/A173656
  Material read: complete sequence entry and comments
  Evidence: The existing entry supplies the candidate list and completeness range.
- **Characterizing pseudoprimes for third-order linear recurrences** — CONTEXT.
  Identifier: https://doi.org/10.1090/S0025-5718-1987-0866094-6
  Material read: complete article PDF
  Evidence: The decisive coverage is already supplied by the general matrix theorem.

Residual originality risks:
- None identified.

## Scientific value

**FAIL** — After removing the covered descent mechanism, the remainder is a known-table reduction plus a few exact modular lift checks. That is useful verification but is a routine specialization/recomputation rather than a separately motivated mathematical contribution.

## Final assessment

The package is scientifically rejected because the final claim does not pass all three C/O/V axes. Correct calculations are retained as failed evidence.

This is a best-of-knowledge mathematical audit, not formal proof-assistant verification or a guarantee against undiscovered prior art.
