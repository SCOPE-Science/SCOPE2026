# Review of the alternating-coefficient theorem

## Correctness

**PASS (self-review).** The proof reconstructs the optimal trigonometric polynomial from the printed Fejér-extremal Fourier coefficients, with no positivity assumption on the shifted-basis coefficients. The product-to-sum identity yields a positive sine-vector spectral factor; multiplication by the fourth-order boundary factor produces the autocorrelation formula for every ordinary polynomial coefficient. All correlations are strictly positive, so the complex triangle inequality proves every-radius sharpness and uniqueness; a finite sine sum gives the exact endpoint. The independent expansion checker returned `VERIFY_OK 5394`, but the universal theorem depends on the proof, not these finite checks.

## Originality

**PASS, with historical-priority risk.** Ferrari (2026), Section 5.1 footnote 3, explicitly states the all-order supremum as a conjecture and verifies it only for orders two through six via a nonnegative-shifted-coefficient lemma. The present claim proves the full conjecture and stronger radial/alternating-coefficient statements by a different route. Banjai (2022), Section 6, gives the original truncated family and a finite numerical parameter choice; earlier related numerical work does not give the all-order optimized symbolic norm. The nearest mathematical-record hits concern positivity of convolution weights for specific low truncation orders, rather than the polynomial's maximum modulus. Search nonappearance alone is not evidence of uniqueness; unindexed or simultaneous proofs cannot be ruled out.

## Value

**PASS.** This resolves an explicit, naturally posed question about an A-stable multistep generator, and identifies a sharp worst-case contour location for every truncation order. The result matters to CQ symbol-range and perturbation estimates and is stronger than recomputing finite coefficient tables. The alternating-coefficient law supplies an independently useful structural explanation even when the original shifted coefficients change sign. No claim is made about sharp solution-error estimates.

## Scope and limitations

All-order proof covers only the uniquely optimal real TTR family with Ferrari's normalization. Finite computational checks cannot establish the theorem alone. No independent mathematical verification has been performed; historical priority has the usual unindexed-literature risk.

Self-review: passed. Independent audit: not yet performed.
