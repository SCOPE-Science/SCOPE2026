# Scientific review: dispersion phase diagram for one-inflated zero-truncated negative-binomial counts

## Correctness (C): PASS

The law, domains, and mixture normalization are explicit. Both truncated factorial moments follow from the negative-binomial probability generating function and conditioning on positive counts. Their substitution gives the exact variance-minus-mean polynomial. The nonstandard all-parameter inequality has an elementary derivative proof via \(g_r\) and \(h_r\), with a strict sign switch at \(r=1\). The auxiliary cutoff is unique because the size-biased excess-count distribution forms a nondegenerate exponential family in \(\log q\), making the derivative of \(A/B\) its strictly positive variance. The global classification follows from these facts and exact quadratic endpoint signs. An exact rational example is cross-checked by a standalone checker. Remaining limitation: the checker samples parameters and is **not** an infinite proof; the written proof supplies that part.

## Originality (O): PASS, with historical qualification

The known object and moment formulas (Godwin 2012, Chapter Four, p.80), together with the 2023 excess-one formulation and later inference articles, are explicitly credited. The proposed result is not a rederivation of those formulas: it combines a strict shape-dependent curvature identity, a unique nontrivial rate boundary, and a full \(0/1/2\) equidispersion-transition classification. In the inspected sections of the accessible original dissertation and 2024 arXiv text, no such theorem was found. The 2022 equivalence and 2024 modelling articles provide mixture/likelihood results, not the shape-dependent sign diagram. Searches of related mathematical records and literature likewise returned no covering result. These comparisons support a provisional self-review, not definitive priority proof. The 2016 journal full text and the publisher's original 2023 PDF were unavailable; the 2023 indexed paper text has badly degraded formulas. Such limitations remain priority risks and do not establish noncoverage of inaccessible texts.

## Value (V): PASS

The unconditional dispersion index is a natural first diagnostic for positive count regression, sampling and capture–recapture models. A non-obvious operational effect is that adding an atom at one can turn an underdispersed zero-truncated negative-binomial law into an overdispersed law and then back into an underdispersed law, not merely move dispersion monotonically. The criterion gives exact parameter regions and sharp equidispersion boundaries, including an explicit rational witness. This can prevent incorrectly inferring dispersion direction from the baseline family or the amount of one-inflation. The contribution is a complete mathematical phase classification, not a claim of new probability model or estimation method.

## Closest literature and limitations

Godwin (2012) gives exactly the same probability model and first two moments, but the inspected mathematical development concerns distributional specification, inference and testing rather than this global dispersion partition. Godwin (2016) is a particularly plausible priority source whose accessible abstract cannot exclude overlap. Jolayemi–Aderoju (2023) is the date-qualified literature lead, and Godwin (2024) and Böhning–Friedl (2024) supply related probability representations and inference. The accessible 2012 and 2024 primary texts and indexed 2023 source were compared at the claim level; historical novelty remains subject to human literature review. This theorem is unconditional, does not concern fitted-model residuals, and its numerical thresholds are illustrative.

Self-review: passed. Independent audit: not yet performed.
