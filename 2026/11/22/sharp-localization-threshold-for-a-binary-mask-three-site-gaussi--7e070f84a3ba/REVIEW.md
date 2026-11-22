# Self-review

**Correctness — PASS.** Direct expansion gives \(\det K=(1-x^4)(1+x^4-2xy)\) on the stated domain. The strictly increasing cubic isolates a universal safety threshold, the explicit \(y_*(x)\) gives every singular member, and the derivative of \(1+x^4-2x^p\) proves fixed-ratio uniqueness. The rational example has an exact rank-two certificate; `verify.py` tests the algebra independently using rational arithmetic. The proof covers all positive widths within the claimed symmetric three-site family, not just computed samples.

**Originality — PASS (historically qualified).** The 2020 Chiu–Ling–McCourt paper explicitly shows three-site singular variable-shape Gaussian matrices, so mere singularity and minimal size are not original. The first 2026 source supplies the binary shape rule and analyzes ideal delta-column replacement, not the finite-width sharp symmetric-mask locus. The 2004 Bozzini–Lenarduzzi–Rossini–Schaback result supplies general sufficient perturbation conditions but not a necessary-and-sufficient cubic threshold for this family. The distinct result assessed here is the all-width sharp safety guarantee together with the unique fixed-ratio singular crossing. A special-case formula in less discoverable literature remains possible.

**Value — PASS.** A real, exactly characterized invertibility gap remains between finite adaptive Gaussian columns and the ideal column replacement that motivates the 2026 method. The theorem supplies a dimensionless safety criterion, a complete bad-parameter locus, and an exact small test matrix that can guide implementation checks. It does not claim a quantitative condition-number guarantee or that a particular finite data set generates the required indicator pattern.

**Limitation:** Three equispaced sites and a specified binary mask only; no extrapolation to arbitrary adaptive indicators or arbitrary larger grids. Exact arithmetic is assumed, with no independent validation.

Self-review: passed. Independent audit: not yet performed.
