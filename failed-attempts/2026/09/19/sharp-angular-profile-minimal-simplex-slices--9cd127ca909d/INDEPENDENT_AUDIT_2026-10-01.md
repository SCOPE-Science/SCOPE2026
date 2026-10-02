# Independent scientific audit — SCOPE-20260919-9cd127ca909d

Audited at: 2026-10-01T15:09:23.525185Z

Disposition: **failed**

## Correctness — PASS

Inside the one-vertex chamber the exact section-volume formula is correct. At fixed spherical angle, the product denominator becomes a positive \(n\)-tuple with fixed arithmetic mean and fixed variance. Rodin's sharp fixed-variance AM-GM theorem gives the stated product maximum, equality pattern, and therefore the displayed angular profile. The equality vectors map to the great-circle arcs toward the Webb normals, and differentiating the same exact factorization gives the isotropic Hessian \((2n+1)/(n+1)\,g\).

### Correctness sources

- assigned RESULT.md
- Rodin fixed-variance AM-GM theorem
- published SCOPE one-positive-chamber stability theorem

### Correctness risks

- The result is chamber-wise; no claim across other normal sign patterns is used in this correctness assessment.

## Originality — FAIL

A published SCOPE record dated 2026-09-18 already gives the exact one-positive-chamber section factorization, the angle coordinate, the \(\sec\theta\) bound, and the isotropic Hessian. Rodin's prior theorem gives the sharp maximum geometric mean for positive tuples with fixed mean and nonzero variance, with exactly the \(n-1\)-equal equality pattern. Fixed angle in the prior factorization fixes that variance, so the assigned sharp profile and equality arcs are mechanically obtained by applying Rodin's theorem.

### Equivalent formulations

The assigned \(\Phi_n\) is the Rodin extremal product substituted into the earlier exact factorization.

### Broader coverage

Those two broader ingredients jointly dominate the assigned sharp fixed-angle optimization.

### Exact database or table

This is a theorem implication rather than a precomputed table; the prior factorization plus Rodin theorem is decisive.

### Claim versus prior implication

The assigned main theorem is a direct optimization corollary of already-published ingredients.

### Sources inspected

- Quantitative one-positive-chamber stability for minimal regular-simplex slices — published SCOPE record 2026/09/18/one-positive-simplex-slice-stability--b3c9f941eb08. COVERING_INGREDIENT: It supplies the entire simplex-specific factorization and local geometry used by the assigned theorem.
- Variance and the Inequality of Arithmetic and Geometric Means — https://arxiv.org/abs/1409.0162. COVERING_INGREDIENT: This is precisely the remaining optimization after fixed angle fixes the variance.

### Checked sources

- published SCOPE 2026/09/18/one-positive-simplex-slice-stability--b3c9f941eb08
- https://arxiv.org/abs/1409.0162
- https://arxiv.org/abs/2609.12714
- Resultary semantic search

### Residual risks

- No residual literature uncertainty can restore originality because the assigned profile is mechanically implied by the two explicit prior ingredients.

## Value — FAIL

The closed profile and equality arcs are elegant, but once the earlier exact chamber factorization and Rodin's sharp theorem are available, obtaining them is a direct substitution exercise. Under the stated value standard, that is too mechanically implied to count as a separate validated research finding.

### Value sources

- published SCOPE one-positive-chamber theorem
- Rodin fixed-variance AM-GM theorem

### Value risks

- The formula can remain useful as an expository corollary.

## Limitations

- Scientific rejection is for originality and value, not correctness.
- The sharp profile applies only in the one-vertex-separating chamber and symmetric copies.
- No global deficit theorem across all normal sign patterns is asserted.
