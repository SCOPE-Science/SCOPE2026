# Scientific review

## Correctness — PASS

The area variance \(1/3\) follows from bridge innovation isometry and independence. Direct covariance calculation yields the exact bilinear Gaussian projection coefficient \(C(s,t)\); the resulting risk is a closed form. For fixed temporal gap, the reciprocal-gain denominator splits into positive pieces, each minimized jointly by equal boundary margins and equal precisions using AM–GM, Cauchy–Schwarz, and a strictly convex square-root function. A monotone cubic numerator then yields the unique gap and both budget limits. The self-contained proof checks the full open parameter domain and equality cases; supplementary exact/symbolic and finite tests passed.

## Originality — PASS, qualified

Primary full-text comparisons with Foster–Habermann's Lévy-area series construction (2021 first preprint; open Cambridge 2022/2023) and Kastner–Rößler's numerical-algorithm analysis (2022) show different information models: their Gaussian expansion coefficients and truncation budgets are not two noisy asynchronous point observations with a fixed precision sum. Dickinson's broad linear-Gaussian-information approximation theorem (2007) is relevant, but only abstract material was accessible; the available statement and later citations concern unrestricted approximation/asymptotic bounds, not the precise finite resource-constrained classification. A related four-scalar two-planar-observation theorem in accessible earlier results uses a distinct information sigma-field and cannot imply strict joint optimal precision allocation. Published-result index searches for asynchronous scalar, area, covariance aliases and precision constraints found no direct covering record; this is not exhaustive publication-priority certification.

## Value — PASS

For a signed second iterated stochastic integral, a simultaneous cross-coordinate scalar pair contains no conditional area information, so the smallest nontrivial coordinate-specific sensing architecture must use different times. Under a continuous sensor-precision resource budget, the theorem resolves **both** when each channel should sample and how precision should be shared, globally rather than in a symmetric design subclass. The closed-form information ceiling below nine percent identifies a sharp architectural limit; the budget-dependent gap describes optimal placement from highly noisy to essentially exact sensing. This is a complete natural design classification, not merely an arbitrary parameter instance.

## Limits and closest sources

The fixed architecture, pinned bridge prior and independent Gaussian precision costs are essential. No claim about multi-observation, arbitrary linear sensing, or approximation algorithms beyond conditional-mean risk is made. The earliest motivating source is the 19 February 2021 arXiv version of Foster–Habermann. Relevant full-text source sections are their Section 5 (series approximation of Lévy area) and Kastner–Rößler Sections 2–4 (Fourier-based algorithms and precision), neither of which states a joint two-scalar time-and-precision theorem. Dickinson's full text was not accessible in this run and remains a concrete priority risk.

Self-review: passed. Independent audit: not yet performed.
