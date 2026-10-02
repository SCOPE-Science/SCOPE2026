# Review status

Independent mathematical audit completed on 2026-10-01 UTC.

Scientific disposition: **failed**.

- Correctness: **PASS**. The leave-one-out algebra exactly transforms the externally studentized residual into a monotone threshold on the full-sample standardized coordinate. Conditional on an exchangeable orbit, the held-out coordinate is uniform among all coordinates. The finite-vector one-sided Cantelli count therefore gives the stated integer staircase, and two-level vectors realize the inclusive and strict integer bounds. The zero-variance convention correctly handles the single-high-coordinate endpoint.
- Originality: **FAIL**. The final tail theorem is already a direct corollary of published ingredients in Troffaes–Basu 2019. Their Lemma 5 gives the exact identities relating the training mean/variance residual to the full-sample standardized coordinate, and their Lemma 7 gives the needed one-sided finite-vector Cantelli count. Solving the Lemma 5 identity for the residual threshold and inserting it into Lemma 7 yields the audited staircase formula. The fact that the paper's main theorem instead introduces a range offset does not undo this implication under the audit rule that unstated corollaries are covered.
- Scientific value: **FAIL**. Once the published leave-one-out identities and one-sided count lemma are treated as prior, the remaining work is threshold algebra, integer rounding, and the standard two-level equality construction. Under the stated value bar that residual is a routine corollary rather than a distinct motivated mathematical contribution.

Detailed evidence is recorded in `INDEPENDENT_AUDIT_2026-10-01.md` and `INDEPENDENT_AUDIT_2026-10-01.json`. Earlier review evidence is preserved in `AUDIT.json` without being relabeled as fresh independent evidence.
