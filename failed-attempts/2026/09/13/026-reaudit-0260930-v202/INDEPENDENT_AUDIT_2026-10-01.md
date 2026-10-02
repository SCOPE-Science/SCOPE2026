# Scientific audit — SCOPE-20260913-026

Date: 2026-10-01 UTC

## Final claim

The primes 5, 29, and 181 form a Borromean Rédei triple: they are pairwise quadratic residues in the required sense and the normalized Rédei symbol [5,29,181] equals -1, with an explicit D4 and Frobenius certificate.

## Correctness

**PASS** — The pairwise Legendre symbols were recomputed. The normalized conic identity 7 squared minus 5 times 2 squared minus 29 equals zero was checked, the associated quartic was independently tested irreducible modulo 3, and its 1+1+2 factorization modulo 11 excludes a cyclic C4 quartic group after the resolvent reduction. At 181, 27 is a square root of 5 and the two beta conjugates 61 and 134 are both quadratic nonsquares, giving Rédei symbol -1. These finite arithmetic checks reproduce the certificate.

Residual risk: The cohomological Massey interpretation is inherited from cited arithmetic-topology theory; the audit directly certifies only the arithmetic Rédei symbol.

## Originality

**PASS** — The exact triple {5,29,181} was not located in the compared primary literature or published-results corpus. General Rédei reciprocity and density theorems explain the family and guarantee many examples but do not identify this specific triple. The record correctly withdraws its former novelty and minimality claims, so the assessed claim is only the explicit certificate.

Residual risk: Best-of-knowledge only: explicit examples can occur in tables or dissertations not captured by the searches, and the record deliberately makes no priority claim.

### Equivalent formulations

General definitions and reciprocity were compared; no statement identifying the exact triple 5,29,181 was found.

### Broader coverage

Density theory shows Borromean triples are abundant but does not mechanically select this exact triple.

### Exact database or table

A dissertation source with explicit Borromean-prime examples was checked as a plausible table source; the exact triple was not located in the material compared.

### Claim versus prior implication

Positive density implies existence of many triples but not the identity or certificate of this particular one.

## Value

**FAIL** — Once the general Rédei-symbol theory is fixed, this is one unexceptional explicit example in a positive-density family, verified by short local residue calculations. The record supplies no minimality, extremality, new structural pattern, classification boundary, or demonstrated future need for this precise triple. Under the value bar, reproducibility and a clean certificate alone do not make an arbitrary instance scientifically valuable.

Residual risk: A later application that specifically needs this triple could change the value assessment, but none is established here.

## Sources inspected

- Rédei symbols and arithmetical mild pro-2-groups — https://arxiv.org/abs/1303.2608 — BACKGROUND_NOT_EXACT: Supplies general theory, not the exact 5,29,181 example.
- The Density of Borromean Primes — https://arxiv.org/abs/2403.17957 — BROADER_EXISTENCE_NOT_EXACT: Shows the phenomenon is abundant; does not identify this triple.
- Published finding SCOPE026 — https://github.com/Resultary/2026/tree/main/2026/9/13/SCOPE026 — SELF_MATCH_ONLY: The exact indexed match was the record itself.

## Disposition

FAILED
