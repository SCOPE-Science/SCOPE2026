# Independent audit — Exact Jung-defect decomposition for minimum enclosing-ball certificates

Audited at: 2026-10-01T18:04:30Z

Disposition: **failed**

## Correctness

**PASS** — For a minimal enclosing-ball support with barycentric weights, the exact identity \(R^2=\sum_{i<j}\lambda_i\lambda_jd_{ij}^2\) follows from weighted variance. Adding and subtracting \(D^2\sum_{i<j}\lambda_i\lambda_j\) gives the stated three nonnegative terms. The support thresholds, weight estimates and edge bounds follow directly, and the volume estimate follows from the stated Gram-matrix perturbation bound.

## Originality

**FAIL** — A published SCOPE theorem, “Exact Jung-defect decomposition in constant-curvature space forms” (record 3a2f1fd32372), contains a strictly broader exact decomposition for Euclidean, spherical, and hyperbolic spaces. Its Euclidean specialization is algebraically the same deficit decomposition after zero-padding the support weights, and it already gives the sharp support hierarchy and componentwise weight/edge control.

### equivalent_formulations

Searches: Resultary: Jung deficit decomposition minimum enclosing ball contact certificate support cardinality barycentric edge deficit; SCOPE record 3a2f1fd32372.
Evidence: The broader record gives \(arepsilon_0=\sum_{i=1}^{n+1}(\lambda_i-1/(n+1))^2+2\sum_{i<j}\lambda_i\lambda_j(1-d_{ij}^2/D^2)\).
Reasoning: Expanding the zero-padded weight term into cardinality and within-support imbalance gives exactly the audited Euclidean three-term decomposition.

### broader_coverage

Searches: SCOPE record 3a2f1fd32372 full RESULT.md.
Evidence: The prior record proves the same identity simultaneously in Euclidean, spherical and hyperbolic space forms, with the same sharp support thresholds and weight/edge consequences.
Reasoning: This strictly dominates the principal theorem of the audited record.

### exact_database_or_table

Searches: Resultary published findings search.
Evidence: Resultary returns the broader constant-curvature SCOPE result as the nearest non-self match.
Reasoning: The issue is theorem-level implication rather than a finite table; the published database contains a stronger theorem.

### claim_vs_prior_implication

Searches: SCOPE record 3a2f1fd32372 full RESULT.md.
Evidence: Its Euclidean specialization yields the audited identity, equality case, full-support threshold, balance estimate and edge-shortfall bound.
Reasoning: The remaining volume consequence is a routine Gram-matrix perturbation corollary once every active edge is close to \(D\), and the Rips--Cech paragraph is an interpretation rather than an independent theorem. They do not restore originality of the final claim package.

### Source inspections

- **Exact Jung-defect decomposition in constant-curvature space forms** (SCOPE-20260920-3a2f1fd32372): COVERING and STRICTLY_BROADER. Material read: Complete RESULT.md at repository commit 92c7f26b45ce94be6cda0eafed44298c598d7b47. Trigger: Resultary returned a highly similar same-day theorem with broader curvature scope. Evidence: Equation (4) is the general deficit decomposition; equations (6)--(12) give the support hierarchy and quantitative balance/edge control.

Checked sources: SCOPE-20260920-3a2f1fd32372 complete RESULT.md; Resultary published findings search; Jung/minimum-enclosing-ball literature terms.
Residual risks: none identified beyond the stated comparisons.

## Scientific value

**FAIL** — The principal mathematical content is already supplied by the broader constant-curvature theorem. The added Euclidean volume estimate is a standard eigenvalue/Gram perturbation consequence and the Rips--Cech discussion is an interpretation of the same certificate. As a separate final claim, this package is therefore a covered restatement plus routine corollaries rather than a distinct motivated gap.

## Limitations

- Correctness of the Euclidean identity survives, but the final claim is scientifically rejected because a broader published theorem covers its principal content.
- The volume estimate is not claimed optimal.

This file records a scientific assessment only; it does not claim formal verification or expert attestation.
