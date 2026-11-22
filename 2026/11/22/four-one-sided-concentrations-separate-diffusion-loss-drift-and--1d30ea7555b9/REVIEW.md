# Scientific review: two-flow concentration identification

## Correctness

**PASS.** The Green-function solution on the full line satisfies the homogeneous characteristic equation, continuity at the source, decay at both infinities, and the distributional jump imposed by the point source. Each positive-side profile is exactly an exponential. Comparing two distinct known flow offsets yields two characteristic-root equations and two source-amplitude equations. Eliminating their common coefficients gives the globally monotone amplitude-ratio map \(R=(k_1+z)/(k_2-z)\) over exactly \(0<z<k_2-k_1\), which proves necessity, sufficiency and uniqueness of the strict feasible-data inequalities. Direct construction of a continuous ambiguity family establishes minimality of four scalar readings within two flow conditions. The exact witness and the seeded verification script corroborate the algebra; they are not substitutes for the proof.

## Originality

**PASS on the inspected literature, with historical-priority risk.** Baetscher et al. (2024) study distance- and tide-dependent eDNA detections, not global identification of four constant transport/source parameters. Kim (2020) provides forward analytic solutions, not the two-flow minimality or amplitude-ratio feasibility theorem. El Badia, Ha-Duong and Hamdi (2005) identify a moving/time-dependent unknown pollution source with specified transport coefficients from time traces, including stations on opposite sides, so their result does not imply this simultaneous unknown-coefficient steady, positive-side four-sample inverse. Research-record searches for two-flow steady advection–diffusion–reaction inversion and adjacent measurement-count theorems found no stated covering theorem. Andrle et al. (2011), a plausible source-identification predecessor, was accessible only in abstract form, and independent priority review has not been performed.

## Value

**PASS.** The motivating field study reports tide-dependent attenuation of marine eDNA away from a known hatchery source. Its setup makes it scientifically natural to ask whether two flow conditions actually separate longitudinal mixing, first-order loss, residual drift and shedding intensity. The theorem answers a complete parameter-identification and measurement-design question, including an exact feasibility test, an explicit inverse, and a sharp impossibility for one condition or three scalar readings. This is a benchmark for idealized experiments, not a prediction that four noisy samples suffice in a real tide or that the quasi-steady approximation is accurate.

## Closest literature and limitations

Baetscher et al., *Environmental DNA* (2024), DOI 10.1002/edn3.533; Kim, *Scientific Reports* (2020), DOI 10.1038/s41598-020-63982-w; El Badia et al., *Inverse Problems* (2005), DOI 10.1088/0266-5611/21/3/020; Andrle et al., *Inverse Problems* (2011), DOI 10.1088/0266-5611/27/2/025007. The last paper was not available in full text. Potential broader inverse-coefficient literature remains a priority risk. Real tidal transients, finite boundaries, condition-dependent emission, flow-dependent mixing/loss, detection censoring and measurement noise are outside the theorem.

Self-review: passed. Independent audit: not yet performed.
