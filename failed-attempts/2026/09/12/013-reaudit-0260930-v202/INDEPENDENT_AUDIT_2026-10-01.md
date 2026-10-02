---
{"schema_version":1,"audit_date_utc":"2026-10-01","status":"failed"}
---

# Independent mathematical audit

## Final claim

For the real quadratic field of discriminant 29 in its cyclotomic 5-adic tower, the 5-primary class groups at layers zero and one are trivial, and consequently the Iwasawa lambda and mu invariants vanish.

## Correctness — PASS

The base class number one calculation follows from the Minkowski bound and inertness of 2. The prime 5 splits, the fundamental unit is (5+sqrt(29))/2, and the two Hensel embeddings modulo 25 send it to 14 and 16, whose fourth powers are 16 and 11 rather than 1. This gives the required local norm obstruction. The exact Gaussian-period and compositum scripts verify the first cyclotomic layer and ramification setup. The Chevalley fixed-class argument then gives trivial 5-primary class group at the first layer, and the standard stabilization criterion yields vanishing Iwasawa invariants.

Checked sources: artifacts/minkowski_h1.py (blob 083e74d5597fe6fd7f2e2e41b865f8b67716bdb1); artifacts/unit_obstruction.py (blob f86149df8d1cfd476d9fdd73c63df22b60e44cb5); artifacts/period_Q1.py (blob 726e6c8bcd5e9ab13cc0a87ee1676a5a6f1f1a78); artifacts/compositum_k1.py (blob 1cfeb66365b5aa961610ef31e3ae0aa30e36e58c); Georges Gras, 2017, Theorem 3.4

Residual risks: The proof uses standard local norm and stabilization facts; the package computations consistently meet their hypotheses.

## Originality — FAIL

A published general criterion already covers the decisive vanishing conclusion. Gras, Theorem 3.4, states a sufficient criterion for lambda=mu=0 when p splits completely; for a real quadratic field it requires the p-class S-group to be trivial and the first-layer S-unit norm index to equal p. Here class number one gives the first condition and the package's own mod-25 unit calculation gives exactly the second. Thus the headline vanishing is a direct special case of a published theorem after a short arithmetic check.

### Equivalent formulations

The mod-25 non-fifth-power test is the local form of the norm-index condition used in the published criterion. Evidence: Gras expresses the criterion through the first-layer S-unit norm index; the package expresses the same obstruction through the fundamental unit modulo 25.

### Broader coverage

The published theorem is strictly broader than this field-prime instance. Evidence: Gras Theorem 3.4 covers all totally real Galois fields with p totally split under its class and norm-index hypotheses; the paper also reports large tables of quadratic cases including p=5.

### Exact database or table

Exact-table novelty cannot overcome direct theorem coverage. Evidence: Gras reports that among squarefree m up to 10^4 with p split, 2459 of 2534 p=5 cases satisfy the criterion, and points to more complete tables. The exact membership of m=29 need not be separately tabulated because the theorem-level implication is already decisive.

### Claim versus prior implication

The prior theorem therefore implies vanishing of the Iwasawa invariants for this instance; the first-layer triviality is the elementary fixed-class calculation behind the same criterion. Evidence: Class number one makes the S-class condition trivial; the audited unit has nontrivial Hasse symbol/local norm obstruction, so the S-unit norm index is 5.

### Source inspections

- **Approche p-adique de la conjecture de Greenberg pour les corps totalement réels** — https://www.numdam.org/item/10.5802/ambp.370.pdf. Trigger: Same Greenberg/Iwasawa problem with explicit real-quadratic criteria and tables. Material read: Theorem 3.4, its proof, the norm-symbol computational criterion in Section 5.2, and the p=5 table summary. Method: Primary full-text PDF inspection. Assessment: COVERING. Evidence: Theorem 3.4 gives lambda=mu=0 from the exact class/norm-index conditions verified by the package.
- **The Iwasawa lambda-invariants of Z_p-extensions of real quadratic fields** — Acta Arithmetica 69 (1995), 277-292. Trigger: Highly relevant earlier computational work on the same invariant and object class. Material read: Bibliographic record and later literature discussion; open full text was not obtainable in this run. Method: Open-access retrieval attempted; institutional retrieval also failed. Assessment: ACCESS_RISK. Evidence: The source is plausibly even closer historically, but the later covering theorem already decides originality.

Checked sources: https://www.numdam.org/item/10.5802/ambp.370.pdf; Takashi Fukuda and Hisao Taya, Acta Arith. 69 (1995), 277-292; https://doi.org/10.1090/S0002-9947-03-03357-9

Residual risks: The inaccessible 1995 paper may contain the exact field-prime pair explicitly; this would only strengthen the coverage conclusion.

## Scientific value — FAIL

Vanishing of the Iwasawa invariants for a concrete real quadratic field is a motivated question, but this particular instance is mechanically discharged by an existing general criterion once class number one and one local unit computation are supplied. The package does not add a new criterion, phenomenon, or boundary beyond the covered instance.

Checked sources: Gras 2017 Theorem 3.4; package class-number and unit calculations

Residual risks: A genuinely new first-layer phenomenon outside the published criterion could be valuable; that is not the audited claim.

## Disposition

FAILED. Acceptance requires PASS on correctness, originality, and scientific value.
