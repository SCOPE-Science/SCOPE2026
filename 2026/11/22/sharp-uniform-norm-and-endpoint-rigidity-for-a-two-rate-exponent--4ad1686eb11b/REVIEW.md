# Self-review

## Correctness — PASS

The explicit Gram inverse is checked symbolically. The one-variable kernel has at most one zero, and the proof partitions all w in (0,1] into early, nonnegative, and late regimes; inequalities for the single-root bound, the strict late-time ratio bound, and monotonicity of the exact norm close all boundaries. The endpoint sign function gives equality. The standalone checker independently verified all three row formulas against high-precision split quadrature at 72 points; finite tests are supplementary.

The central nonstandard step is a complete and strict classification of the three kernel-sign regimes. It is proved in `RESULT.md` rather than inferred from plots. Assumptions and the rank-drop boundary are stated explicitly. The norming sign input belongs to \(L^\infty\), not necessarily \(L^2\).

## Originality — PASS (qualified)

Compared actual two-exponential derivative results (Protasov 2022), finite-interval polynomial-frame least squares (Adcock-Shadrin 2021), exponential L-spline projections (Kayumov 2004), and prior exact projection calculations. None inspected establishes the entire real two-decay half-line norm formula or endpoint rigidity. The coalescent constant \(8/e\) overlaps prior related work; no independent novelty is claimed for that isolated limit. Residual specialized historical priority risk remains.

Full-text HTML material was inspected in Protasov and Adcock–Shadrin. Accessible summary material, rather than the entire thesis proof, was inspected in Kayumov. The closest earlier projection formulas concern different domains or oscillatory spans, and a common coalescing limit is acknowledged rather than counted as novel. The detailed implication comparisons and remaining risks appear in `AUDIT.json`.

## Mathematical value — PASS

The formula completely resolves a natural two-rate least-squares stability benchmark, with no arbitrarily fixed rate ratio: it proves a unique norming time, strict ratio monotonicity and the exact universal sharp envelope 4. It separates high Gram coefficient conditioning from bounded projected-output amplification at both colliding and disparate rate limits; a sign-extremizer and rank-drop discontinuity make the threshold structurally interpretable.

The claim is an exact continuum theorem for all positive unequal rate pairs and includes extremizers, not just a numerical example. Its limit at equal rates must not be misread as the actual rank-one value.

## Verification and limitations

The exact kernel row, three-regime inequalities, monotonicity and boundary limits were checked against the written proof. The standalone `check.py` script passed 72 high-precision comparisons and symbolic normalization identities. Unresolved questions include extensions to more than two decays, weighted measures and historical priority in specialist approximation theory. No external validation is claimed.

Self-review: passed. Independent audit: not yet performed.
