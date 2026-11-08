# Scientific review

## Correctness (C): PASS

The iid geometric lag representation exactly matches the label-weighted attachment probability after conditional truncation, and bad lags are summably rare. The stationary count differs uniformly from the actual count by at most the maximum number of edges crossing a time cut, a logarithmic almost-sure quantity. The stationary one- and two-point leaf laws are independent product formulas with absolutely summable negative covariance. The explicit lower bound on the variance comes from exposing disjoint two-choice lag variables. An exponentially strongly mixing bounded process then satisfies the standard functional invariance principle. Geometric summation verifies the weak-preference variance limit. The `verify.py` replay passed 838 finite checks; this supplements but does not replace the proof.

## Originality (O): PASS, best-knowledge only

The 2026 leaf-statistics paper by Hartle and Krapivsky has a different, degree-proportional attachment mechanism (plus uniform and redirection comparisons). The 2025 article by Aguech et al. and the earlier March 2024 ALEA Days disclosure establish the *exponentially label-weighted model and single-vertex outdegrees*, not the total-leaf functional law or its inter-vertex covariance; none of those older contributions is claimed new. The closest published-finding corpus results address uniform recursive root-degree/leaf covariance and other tree observables. Fixed-vertex degree marginals cannot determine the total covariance or establish the singular limit; the exact joint indicator product is essential. Broader general invariance principles remain background. Priority risk persists because an equivalent result in unindexed age-biased growth literature is possible and the 2024 slides were not accessible for complete visual inspection.

## Value (V): PASS

The size of the leaf boundary and its variability are natural global observables in recursive networks. The explicit spatial anticorrelations, positive long-run variance and noncommuting near-uniform limits identify structural properties absent from the source individual-degree asymptotics. This informs comparison of young-age-biased trees to genuinely uniform recursive trees.

## Limitations

Fixed \(a>1\) only, no joint near-critical parameter/size regime, no full degree-profile process or concentration rate. Finite enumeration is diagnostic, and historical priority requires independent review.

Self-review: passed. Independent audit: not yet performed.
