# Review of the three-monitor crosswind spacing theorem

## Correctness — PASS

The domain is \(d\geq0\), \(r,\sigma>0\), and \(0<p<1\) with conditional independence. The counts of covered intervals yield three complete Gaussian-CDF formulas, including continuity at \(d=r\) and \(d=2r\). Their derivatives have exactly one possible sign transition on each open geometry regime. The ratio \(\varphi_\sigma(r+d)/\varphi_\sigma(r-d)=e^{-2rd/\sigma^2}\) proves strict optimality, with both nonsmooth boundaries handled using one-sided derivatives. The checker independently tests integration against finite interval partitions; numerical tests are not offered as an infinite proof.

## Originality — PASS on inspected evidence

Litvak et al.'s published two-sensor overlap principle covers the elementary probability model but does not assert the triple-detector two-contact phase structure. The additional center instrument creates an exact plateau between two different Gaussian likelihood-ratio thresholds, which cannot be obtained by assigning the two-sensor optimizing separation to three instruments. Wettergren and Costa (2013) numerically design moving-target collaborative surveillance rather than a fixed binary three-device plume alarm. Frasca et al. use worst-distance coverage rather than single-event detection probability, and the closely ranked Gaussian-plume three-sensor Fisher-information finding optimizes parameter estimation, not binary alarms. The full historical priority search is necessarily incomplete; related uninspected sensor-design literature remains a risk. No exclusive novelty claim is inferred merely from unsuccessful queries.

## Value — PASS

The concrete scientific issue is how much to overlap *three* fallible finite-footprint monitors when a crosswind plume-center prediction is uncertain. An exact four-regime phase diagram supplies the unique best spacing within an operationally natural symmetric transect and identifies a stable design plateau spanning a nonzero reliability interval. This is a structural answer not contained in the generic motivation to balance redundant and new spatial coverage. It is explicitly not a validated field deployment prescription.

## Closest literature and limitations

Bittner et al. (2024), https://doi.org/10.1039/D3EA00170A, motivate localized smoke monitoring, but do not justify the idealized sensor response assumptions. Litvak et al., https://miis.maths.ox.ac.uk/268/2/thales-report.pdf, §5.2.1, are closest in objective but treat two instruments. Frasca et al. (2015), https://doi.org/10.1137/140968094, treat a different loss; Wettergren and Costa (2013), https://doi.org/10.1155/2013/145496, optimize moving-target surveillance numerically. No unconstrained location optimum or multi-period result is asserted; conditional independence, normal plume displacement, hard detection footprints and known parameters are substantive limits.

Self-review: passed. Independent audit: not yet performed.
