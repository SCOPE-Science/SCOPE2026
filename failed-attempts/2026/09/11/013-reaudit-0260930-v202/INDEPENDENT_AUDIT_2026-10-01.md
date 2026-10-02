---
{"schema_version":1,"audit_date_utc":"2026-10-01","status":"failed"}
---

# Independent mathematical audit

## Final claim

For A=F_7[x,y,z]/(x^2+yz,y^3+xz^2,z^3), the Hilbert function is (1,3,5,5,3,1); x+y+z is not Lefschetz, y is Lefschetz, and the displayed Macaulay-dual second-Hessian determinant identity holds.

## Correctness — PASS

Independent quotient-space computation over F_7 gives Hilbert function (1,3,5,5,3,1), multiplication ranks for y equal to (1,3,5,3,1), and middle rank 4 for x+y+z. A separate symbolic calculation over Q verifies det Hess^2(F)=-24883200000 D_Q. The repository verifiers check useful subsets but do not by themselves establish the whole stated rank profile or symbolic identity; those were reconstructed independently.

Checked sources: artifacts/verify_fallback.py (blob 643a354cfedfcd4a68aa03cc74dfdf96b36f02e0); artifacts/verify_hessian.py (blob 70b322adb6a50fe77c25993d44e0079ed0240091d); independent exact finite-field quotient computation; independent symbolic Hessian determinant computation

Residual risks: The package verifier named verify_fallback.py does not itself compute every multiplication rank claimed in prose.

## Originality — PASS

No inspected source gives this exact finite-field non-monomial complete intersection, its specific Lefschetz witnesses, or the displayed second-Hessian identity. The closest broad literature is characteristic-zero or, in a recent inaccessible item, formulated for infinite fields, so it does not presently imply the F_7 instance.

### Equivalent formulations

WLP and higher-Hessian formulations were both checked; no equivalent published statement for this algebra was found. Evidence: The exact algebra appears only in the current record among the searched published findings.

### Broader coverage

Neither inspected source presently yields the finite field F_7 witness. Evidence: The inspected non-Lefschetz-locus paper assumes characteristic zero. The recent arbitrary-characteristic item was not accessible in full and its available description concerns infinite fields.

### Exact database or table

The claim is an explicit algebra-level certificate, and no exact pre-existing row was located. Evidence: No table containing this exact ideal or its Lefschetz-element row was found.

### Claim versus prior implication

The y witness and determinant computation are not mechanically supplied by the inspected general results. Evidence: Available broad statements do not directly force WLP for this finite-field, non-monomial algebra.

### Source inspections

- **The non-Lefschetz locus** — https://arxiv.org/abs/1609.00952. Trigger: General complete-intersection/non-Lefschetz framework closest to the claim. Material read: Assumptions and main complete-intersection discussion. Method: Primary full-text inspection. Assessment: NOT_COVERING. Evidence: The paper works in characteristic zero rather than the finite field F_7 case.
- **On the weak Lefschetz property of Artinian Gorenstein algebras of codimension three in arbitrary characteristic** — https://arxiv.org/abs/2608.27232. Trigger: Highly relevant modern arbitrary-characteristic result. Material read: Only accessible bibliographic/abstract-level material; full text could not be inspected. Method: Access attempt after open-source search. Assessment: RESIDUAL_RISK. Evidence: Available description refers to infinite fields; F_7 applicability was not established.

Checked sources: https://arxiv.org/abs/1609.00952; https://arxiv.org/abs/2608.27232

Residual risks: The inaccessible 2026 arbitrary-characteristic paper is a plausible source; no assertion of noncoverage beyond the material actually available is made.

## Scientific value — FAIL

The exact coefficient choice is an isolated, easily certified example: y is visibly a Lefschetz element in the displayed quotient bases, and no independent mathematical reason was established for needing this particular F_7 algebra rather than a broader boundary, classification, or structurally distinguished family. Correctness and possible novelty therefore do not by themselves meet the value bar.

Checked sources: package motivation; general WLP literature inspected above

Residual risks: A future classification could make this example useful as a test case, but that prospective role is not presently substantiated.

## Disposition

FAILED. Acceptance requires PASS on correctness, originality, and scientific value.
