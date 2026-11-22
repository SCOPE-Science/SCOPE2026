# Scientific review

## Correctness — PASS
The assumptions fix the true Pareto parameter in \((0,1)\) and retain the null as all positive shape parameters. The proof uses a truncated strong law to show that the fitted moment shape tends to one, derives exact Kolmogorov and Cramér–von Mises discrepancies, and controls the refitted triangular bootstrap by bounded truncations plus DKW. Conditional quantile convergence and the false-rejection conclusion follow without wrongly applying a finite-mean central limit theorem. The 23 checker assertions independently confirm the algebra and reproduce the direction of the effect. No assertion about infinite-sample behavior rests solely on simulation.

## Originality — PASS, with residual historical-priority risk
Inspected primary materials include the 2023 Fourier-test preprint and full published open-access version, and the full 2022 Pareto comparative paper including its estimators, bootstrap specification and discussion of shape-one size distortion. The earlier paper already explicitly warns that moment fitting assumes finite mean and demonstrates a size problem at \(\beta=1\), which narrows the novelty. Its finite-sample warning does not state the full \(0<\beta<1\) exact discrepancy constants and joint refitted-bootstrap rejection theorem. published-finding corpus searches for the source, both statistics, infinite-mean moment fitting, exact gaps and bootstrap collapse revealed no directly equivalent archived claim. Search cannot establish uniqueness; an inaccessible related thesis and the broader infinite-mean bootstrap literature are residual risks.

## Value — PASS
This is a motivated calibration boundary for classical EDF tests explicitly used as comparators in a published Pareto-testing framework. It distinguishes failure under an actual member of the null from ordinary low power against an alternative and shows that resampling the estimated model does not resolve the defect. Exact nonzero limits for two distinct classical tests, together with conditional bootstrap collapse, provide a concrete diagnostic for test design and interpretation. The result does not impugn tests fitted by maximum likelihood or the original Fourier statistic.

Self-review: passed. Independent audit: not yet performed.
