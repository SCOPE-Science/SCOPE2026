# Self-review

## Correctness — PASS

The assumptions specify high enough wet-period rainfall for infiltration to equal capacity, an initial normalized capacity of one, exponential wet decay and exponential unponded dry recovery, and fixed wet and dry time budgets. The exact recurrence for capacity deficits expands to an exponential pair sum. Adjacent pairs make the full objective strictly concave. Four equal wet bursts yield a strictly convex reversal-symmetric gap loss, forcing identical outer gaps. Its one-variable derivative is strictly increasing, has its unique boundary sign switch at \(D_c=r^{-1}\log(1+e^{-kw})\), and is positive at the opposite boundary. Therefore the displayed unique optimum and all equality cases follow. Three equal bursts cannot have the activation phenomenon. The standalone standard-library checker passed 51,770 supplementary assertions. The proof, not enumeration, establishes the complete continuous parameter statement.

## Originality — PASS, provisionally on inspected evidence

Closest domain papers are Karmeli and Peri (1974) on pulse-irrigation design, Bauer (1974) on intermittent Horton infiltration, Dunkerley (2015/2016) on rainfall intermittency and infiltration, Rossman and Huber (2016) on dry-capacity recovery, and Assouline (2019) on optimizing irrigation rate/duration. The accessible full 2019 article and relevant full manual chapter present other schedules/design variables without the fixed-three-dry-gap four-equal-burst threshold. The primary 1974 papers' full text and Dunkerley's 2016 full text were not obtained; no complete-document noncoverage finding is made for them. Relevant available published mathematical-result summaries concern rain-intensity ordering or finite runoff-storage networks, not this fixed-rest-budget control of a dynamically recovering infiltration capacity. Checked statements and implications, not merely headings. Broader past publication priority remains a residual risk; no independent originality certification is claimed.

## Value — PASS

With a fixed number and duration of high-intensity wet pulses and a fixed total recovery-time allocation, it is natural to ask which breaks actually maximize water entering soil. The exact result identifies a nontrivial support transition at the first nontrivial pulse count: a single central dry gap is uniquely optimal for short rest budgets, while two additional gaps activate together beyond an explicit threshold. Even in the long-rest regime, equal spacing is strictly suboptimal. This supplies an exact model benchmark rather than a trivial reparameterization of a monotone runoff calculation.

## Limitations and residual uncertainty

The model excludes dry-period evapotranspiration and hydraulic redistribution, infiltration equations with moving wetting fronts, rainfall intensities beneath capacity, hysteresis, and nonzero switching overhead. Model-rate measurements are not supplied. The accessible portions of older pulse-irrigation papers do not justify a claim that their full texts lack related theorems; historical priority deserves independent checking.

Self-review: passed. Independent audit: not yet performed.
