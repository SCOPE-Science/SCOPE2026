# Self-review

## Correctness — PASS

The four-state first-step equations in `RESULT.md` follow from competing exponential event clocks. Direct algebra gives the reported rational fixation probability with positive denominator. Exact factorization shows strict positive gain for all positive parameters except the neutral case, and the derivative numerator has exactly the stated quadratic sign pattern. The two-individual impossibility follows by conditioning on the first mutant-count event. The pure-Python rational verifier separately solves the generator equations over a finite parameter grid; that testing does not replace the full algebraic proof.

## Originality — PASS within searched evidence, historical priority provisional

Ashcroft, Altrock and Galla (arXiv:1406.5619v1, 2014) give a **more general process-level linear-system method** and discuss enhanced fixation through fluctuating environments, so neither the mechanism nor solvability by matrix inversion is new. The inspected original work considers general models and a numerical \(N=50\) example, but does not give the exact smallest-population witness, equal-frozen reciprocal rate family, all-positive-rate enhancement, or the event-rate threshold separating monotone neutral approach from unique finite overshoot. Cvijović et al. (2015) emphasize large-population fluctuating-selection phenomena; Cheong et al. (2016) use a sensor-mediated population-growth model rather than finite-state mutant fixation. Searches also compared generic environmental selection, finite fixation and Parrondo terminology. There remains a real risk that an uninspected specialized small-population treatment or an algebraic corollary in another source covers the full classification. The current priority assessment is not independent verification.

## Value — PASS

The exact boundary \(c=2d\) is an interpretable comparison of early and late mutant-count event rates, not a narrow arbitrary numerical calculation. For two environments with identical frozen fixation chances, the theorem distinguishes strict all-rate benefit, possible enhancement beyond neutral fixation, and whether an intermediate switching speed is uniquely best. The independent size-two obstruction establishes the smallest natural number of population stages that can display the effect. This is a structural analytic benchmark for fluctuating selection, not a field recommendation.

## Scope and residual risk

The family assumes symmetric independent environmental flipping, reciprocal stage biases, two absorbing boundaries, and a uniformly sampled initial environment. Arbitrary frequency dependence and other switching protocols are not classified. The 2014 general framework includes the requisite linear algebra, and a later or less easily discovered paper may already have extracted similar exact special-family thresholds.

Self-review: passed. Independent audit: not yet performed.
