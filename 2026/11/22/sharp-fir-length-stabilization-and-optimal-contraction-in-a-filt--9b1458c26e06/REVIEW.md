# Self-review

## Correctness — PASS

The exact stationary quadratic and the scalar delay recurrence give the full \(n\)-dimensional companion characteristic polynomial. Evaluation at \(1\) fixes \(P_+(1)=\sqrt\Delta\), yielding the universal Schur-radius bound \(\sqrt\Delta\le(1+\rho)^n\), with equality only for a repeated negative real root. Coefficient comparison verifies the unique all-positive binomial-corrected tap construction. A delayed-selector perturbation covers positive-gain cases where \(\sqrt\Delta\le1\). The negative branch has \(P_-(1)<0\), which forces a real root greater than one. Exact symbolic identities and sampled companion spectra were checked using the included code. No finite experiment is used as an infinite proof.

## Originality — PASS within inspected literature

The full accessible 2024 arXiv version of Borges–Silva–Eisencraft gives the arbitrary-length model, fixed-point formulas, appendix Jacobians and numerical studies of selected filters. The 2022 Borges–Eisencraft full paper studies a two-tap version and a numerical stability region. Neither inspected text provides the sharp all-filter gain frontier, exact optimum across all real tap choices, or unique attaining positive tap profile. Targeted mathematical-literature searches for the identical filtered map, equivalent polynomial root-placement statements and stronger delay-stabilization coverage returned no direct statement of this claim. This does not establish absolute priority. The earliest 2023 SSRN text could not be read in full, and unindexed general optimal pole-placement results could cover the abstract polynomial inequality; the application-specific optimality comparison remains provisional pending independent literature review.

## Value — PASS

A fixed-gain FIR feedback map has an entire coefficient simplex of possible local stability behaviors. The theorem settles its natural sharp optimal-design question simultaneously at every length, not just a sampled filter family: it provides a gain cutoff growing exponentially with memory length, the exact fastest local contraction factor in the high-feedback regime, and a unique positive-tap recipe. It gives a reproducible design bound where prior publications were numerical. The claim does not imply preservation of a chaotic signal, any global basin estimate, or practical bandwidth-performance guarantees.

Self-review: passed. Independent audit: not yet performed.
