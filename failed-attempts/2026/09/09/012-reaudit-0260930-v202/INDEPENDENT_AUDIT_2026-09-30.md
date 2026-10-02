# Independent mathematical audit — 2026-09-30

## Outcome

**FAILED** for the final finding as stated.

## Correctness — PASS

The left-invariant curvature formulas were checked against the committed exact Cartan computation. On the Berger line they reduce to principal sectional curvatures \(4-3s\) and \(s\), so positivity is exactly \(s<4/3\) and strict quarter pinching is exactly \(4/7<s<16/13\). The exact rational box estimates in the verifier are consistent. The systolic inequality follows from the closed principal geodesics and \(\min(a,b,c)^3\le abc\). RESULT contains one algebraic typo in the displayed normalization step: the factor should be \((\min^3/(abc))^{2/3}\), not exponent \(1/3\); the stated inequality and equality case remain correct.

Checked sources:
- actual committed `artifacts/verify_berger_pinching.py`; independent algebraic check of Berger thresholds and systolic scaling

Residual risks:
- The RESULT proof line has the noted exponent typo, although it does not change the theorem.
- The triaxial boxes are sufficient boxes, not a full classification.

## Originality — FAIL

The claimed “new exact” Berger quarter-pinching window is a direct algebraic corollary of the classical Berger-sphere curvature eigenvalues. Once the two sectional-curvature values \(s\) and \(4-3s\) are known, solving a ratio less than 4 gives the two endpoints immediately. Under the required implication-based originality rule, absence of the exact endpoint wording in a source does not make this corollary original. The remaining small triaxial boxes and systolic envelope are also direct elementary consequences of the same standard formulas/geodesic circles rather than an independent new theorem.

### equivalent_formulations

Searches: Berger sphere curvature eigenvalues / sectional curvature formula; Resultary search for Berger quarter pinching \(4/7,16/13\); Inoguchi–Munteanu arXiv:2406.15886

Evidence: Standard Berger-sphere references give the left-invariant connection/curvature description; the audited specialization gives exactly two principal values.

Reasoning: The endpoint statement is equivalent to applying the definition of strict quarter pinching to those classical curvature eigenvalues.

### broader_coverage

Searches: Besse, Einstein Manifolds, Berger sphere discussion; Cheeger–Ebin, Comparison Theorems in Riemannian Geometry; Olmos–Rodríguez-Vázquez Hopf-Berger literature

Evidence: Classical Berger/Hopf-Berger geometry already provides the curvature framework and positivity threshold.

Reasoning: The classical curvature formula is broader coverage and mathematically dominates Theorem A; the stated boxes are elementary interval bounds on the same formula.

### exact_database_or_table

Searches: Resultary semantic search for the exact endpoints and systolic envelope; standard Berger sphere references

Evidence: No separate database table is needed: the endpoints are mechanically implied by the known formula.

Reasoning: Exact-table absence is irrelevant because broader analytic coverage is decisive.

### claim_vs_prior_implication

Searches: From \(K_{\mathrm{hor}}=4-3s\), \(K_{\mathrm{mix}}=s\): solve \(\max/\min<4\); From principal closed geodesics: \(\mathrm{sys}\le2\pi\min(a,b,c)\) and \(\mathrm{Vol}=2\pi^2abc\)

Evidence: Both advertised sharp Berger endpoints and the volume-normalized upper bound follow by short algebra from standard inputs.

Reasoning: The final central statements are direct corollaries rather than scientifically independent claims.

### source_inspections

- **Berger sphere standard geometry (references include Besse and Cheeger–Ebin)** (https://en.wikipedia.org/wiki/Berger%27s_sphere): trigger=Direct source for the classical connection/curvature setup and standard references.; material read=Accessible geometry section and its cited standard references.; method=Secondary full-page inspection used to identify the standard formula provenance.; assessment=BROADER COVERAGE.; evidence=The Berger curvature operator/eigenvalue computation is classical; applying the pinching definition is immediate algebra.
- **Homogeneity of magnetic trajectories in the Berger sphere** (https://arxiv.org/abs/2406.15886): trigger=Recent primary Berger-sphere paper cited by the record.; material read=Accessible abstract and public full-text opening/background indicating the geometry is classical and well studied.; method=Primary-source inspection.; assessment=BACKGROUND, not the exact endpoint source.; evidence=It treats Berger spheres as established naturally reductive spaces and points to the classical geometric literature.
- **Committed Berger verifier** (artifacts/verify_berger_pinching.py): trigger=Critical algebra/certificate file.; material read=Complete source.; method=Line-by-line exact-rational inspection.; assessment=Confirms the corollary-level derivations.; evidence=The endpoint checks are literal rational substitutions into the two classical curvature values.

### checked_sources

- Besse, Einstein Manifolds
- Cheeger–Ebin, Comparison Theorems in Riemannian Geometry
- arXiv:2406.15886
- Resultary semantic search
- committed exact verifier

### residual_risks

- Normalization conventions for the Berger parameter vary across sources, but the implication is invariant after matching the audited \(s=\tau^2\) convention.

## Scientific value — FAIL

The exact Berger pinching endpoints are a two-case algebra exercise from the classical curvature formula; the triaxial boxes use arbitrarily chosen decimal neighborhoods around the round metric rather than a natural maximal region; and the systolic upper bound is the immediate comparison with a principal closed geodesic plus \(\min^3\le abc\). These are useful checks but do not clear the required bar against routine deductions and unmotivated slices.

Checked sources:
- classical Berger curvature/geodesic facts; committed verifier

Residual risks:
- A genuinely maximal triaxial positivity/pinching region or a nontrivial systolic sharpness theorem could be valuable, but those are not the final claim here.

## Limitations

- RESULT has a nonfatal exponent typo in the systolic derivation; the theorem itself remains correct.
- The full triaxial parameter region is not classified.
- Scientific rejection is originality/value based, not an access or transport failure.
