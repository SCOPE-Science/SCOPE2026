# Scientific review: sharp endpoint-cluster tail of the recursive product of spacings

## Correctness — PASS

The claim is confined to fixed sample size and a fully specified continuous null. Exact normalization is reconciled with the published algorithm by binomial convolutions; the Dirichlet density and Jacobian are explicit. The critical moment threshold follows from a sector-coordinate power-count criterion, including a matching divergent endpoint neighborhood. Near either endpoint the exact \(n(n+1)/2\) vanishing factors and uniform control of all normalization denominators yield the integral coefficient. Integrability on the angular simplex supplies domination. Outside the two endpoint neighborhoods a stronger exponential moment renders the remaining tail lower order. This establishes an actual asymptotic equivalent, rather than merely a log-rate or a finite experiment.

The attached checker passed 8,568 exact and numerical assertions covering normalization, combinatorial interval counts, the explicit three-spacing product, and the beta/gamma constant. The 25-million-draw rare-event diagnostic tends toward the predicted small-sample coefficient but does not prove the asymptotic.

## Originality — PASS, with residual priority risk

The closest primary study is Eller and Shtembari, arXiv:2111.02252 (first posted 3 November 2021), equations (2.1)–(2.6), Algorithm 1, section 3 and conclusion. The actual open preprint was inspected from its definition through its concluding discussion, including PDF page images. It provides an exact law for \(n=1\) and a simulation/spline calibration for \(n\ge2\), explicitly noting the lack of an analytic distribution at those sizes. Neither it nor its stated result implies the exact new upper-tail equivalent for all fixed \(n\), the coefficient integral, the critical exponential moment, or the two-vertex dominance proof. The \(n=1\) specialization is acknowledged as a consistency check and is not the source of scientific novelty.

The 2023 multivariate follow-up of Shtembari and Caldwell was compared at the level of its published abstract/introduction and product-of-complementary-spacings formulation: it addresses a distinct statistic and transformation problem. Searches for recursive-spacing extreme tails, equivalent reciprocal-score essential tails, Dirichlet adjacent-window products, and published research-record analogues found no statement covering the claim. One potentially relevant 2023 doctoral thesis was identified bibliographically but not located in verifiable full text; it remains a historical-priority uncertainty. General simplex sector decompositions and Mellin-type power counting are classical tools and are not asserted to be new.

## Value — PASS

The published RPS test is specifically calibrated by simulated extreme quantiles and used for rare-event signal detection. The sharp exponential rate, exact positive leading constant and endpoint localization resolve a natural unanswered fixed-sample tail question and provide an analytic asymptotic benchmark beyond the simulation range, including an essential-exponential small-score law. This is not a routine substitute of a parameter into an existing distribution: recursive normalization changes the singularity order, and identifying the exclusive dominant boundary configurations is a structural issue. No unsupported finite-threshold accuracy or high-sample asymptotics are claimed.

## Limitations

No finite-threshold error bound, large-sample uniformity, fitting correction or exact general-size elementary coefficient is established. The related thesis was not accessible in full; independent mathematical review and historical priority certification remain unperformed.

Self-review: passed. Independent audit: not yet performed.
