# Scientific review

## Correctness

PASS. The proof explicitly establishes the rare-event localization, uses density rescaling under a dimension-matched integrable domination, computes the condition-number sublevel set using the determinant-to-trace squared ratio, and obtains the exact geometric volume. The Gaussian special cases independently agree with exact-rational evaluations and seeded importance-sampling checks. Full singular limits rest on the proof, not simulations.

## Originality

PASS, qualified. The principal source arXiv:2607.10354 introduces sketch-conditioned adaptive restarting; arXiv:2306.03592 studies conditioning and basis selection; the established Wishart literature provides iid-Gaussian condition-number distributions and correlated-Gaussian eigenvalue laws. Those scopes do not imply the distribution-free coefficient involving an arbitrary continuous density at the origin and the independent second vector's radial moment. Search coverage cannot prove historical uniqueness; incomplete complete-text access to the principal paper and unindexed small-noise literature are residual historical-priority risks.

## Value

PASS. The theorem quantifies a natural false-acceptance event for an ill-conditioned raw Krylov basis from a random sketch and identifies a sharp exponent and constant. Its universality across broad non-Gaussian column laws is structurally useful and not an arbitrary numeric example or routine parameter substitution. It is deliberately limited to two columns, a fixed threshold, and one inspection, and does not claim full adaptive-algorithm performance.

## Literature and limits

Closest sources: Güttel–Liu–Nyman (arXiv:2607.10354), Güttel–Simunec (arXiv:2306.03592), Edelman (1988), Anderson–Wells (2009), and Wirtz–Guhr (arXiv:1306.4790). The broader correlated-Wishart formulas are important for the Gaussian specialization but do not dominate the non-Gaussian universality statement. Independent validation and full exhaustive historical priority determination are outside this review.

Self-review: passed. Independent audit: not yet performed.
