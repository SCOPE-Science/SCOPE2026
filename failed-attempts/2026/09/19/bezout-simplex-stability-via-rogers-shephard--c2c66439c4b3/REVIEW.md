# Review status

Fresh independent mathematical audit: **failed**.

- Correctness: **PASS** — The special-test proof was reconstructed. Mixed-volume monotonicity plus K_v^s+[0,sv] subset K yields the projected estimate; Minkowski and layer-cake integration give the lambda_n(c) chord bound. The covariogram identity g_K(-tv)=integral_t^ell P_s ds and polar integration give the difference-body inequality, with n B(n+1,n)=1/binom(2n,n). Applying the quoted Rogers-Shephard stability theorem then gives the displayed Banach-Mazur bound. No computational certificate is required.
- Originality: **FAIL** — A September 18 published result was inspected in full. Its stated theorem uses the full two-body Bezout coefficient beta(K), but the proof of its longest-chord and difference-body steps uses only the exact special tests A=K intersect (K-sv), B=[0,v]. Therefore the same proof already establishes a Banach-Mazur stability theorem under the restricted chord-test coefficient after replacing beta by that restricted supremum. Indeed its retained covariogram bound gives a stronger numerical lower bound than the simplified c^{-(n-1)} lambda_n(c)^n bound in the assigned record. The assigned theorem is thus mechanically contained in the earlier proof despite the weaker hypothesis not being named in its statement.
- Value: **FAIL** — Because the earlier published proof already works verbatim with the restricted test constant and yields at least as strong a quantitative conclusion, this record adds only a repackaging of which hypothesis the existing proof actually uses, plus a weaker simplification of the bound. That does not constitute an independently worthwhile new stability theorem under the stated value bar.

Detailed structured comparisons and residual risks are recorded in `INDEPENDENT_AUDIT_2026-10-01.md` and `INDEPENDENT_AUDIT_2026-10-01.json`.
Earlier scientific assessment evidence is preserved in sanitized form in `AUDIT.json`.
