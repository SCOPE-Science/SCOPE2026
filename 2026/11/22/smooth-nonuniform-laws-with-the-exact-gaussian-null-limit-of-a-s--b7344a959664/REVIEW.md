# Review of the polynomial blind-alternative theorem

## Correctness (C): PASS

The pair kernel matches the 2021 source's complete-data U-statistic. The population CDF integration identity, projected variance, all four critical derivatives, exact pure-perturbation values and the nonzero Jacobian were reconstructed. The analytic implicit-function theorem makes the two cancellations simultaneous and exact for all sufficiently small fixed nonzero perturbations. Positivity follows by uniform continuity of the polynomial derivative; midpoint CDF deviation shows strict nonuniformity. The nondegenerate bounded U-statistic CLT proves equality of the *first-order* normal laws, not finite-sample distributions. `verify.py` independently checks the algebra by symbolic exact integration.

## Originality (O): PASS, qualified

The complete-data sections, asymptotic theorems, numerical alternatives and conclusions of arXiv:2106.06368 and its 2023 open journal version were inspected. Both supply the signed scalar contrast and its null variance but not the two-cancellation polynomial family. The 2021 Ebner–Liebenberg–Visagie integral-square test is a distinct, omnibus-consistent statistic: its theorem does not dominate a claim about the scalar U-statistic. A separate indexed extropy blind-alternative construction addresses a different functional. Search is not proof of priority, and general U-statistic/implicit-function tools are standard. Residual risk: an unindexed or differently titled source could already give this exact family.

## Value (V): PASS

Matching just a population moment is a generic blind spot; matching both the moment and the *entire first-order Gaussian null distribution* is substantially stronger. The new construction shows that the published two-sided test has asymptotic power exactly \(\alpha\) for a continuum of smooth fixed alternatives, while the CDFs stay a positive Kolmogorov distance \(|c|/4\) from uniformity. This directly informs interpretation of this test's evidence and distinguishes it from genuinely omnibus integrated-square variants. The limit applies only to uncensored observations and the unstudentized normal cutoff.

## Closest sources and limitations

The source article is Kattumannil–Sreedevi (arXiv:2106.06368, 11 June 2021), revised as Sreedevi–Kattumannil (2023, doi:10.1007/s42952-023-00205-8). The nearby omnibus squared-characterization paper is Ebner–Liebenberg–Visagie (arXiv:2108.06391). Classical U-statistic and implicit-function results are acknowledged. No claim is made about censoring, a global analytic continuation, finite-sample equality or independent verification.

Self-review: passed. Independent audit: not yet performed.
