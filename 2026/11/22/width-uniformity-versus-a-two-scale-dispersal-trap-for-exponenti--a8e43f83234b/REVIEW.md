# Scientific review: two-band exponential dispersal geometry

## Correctness — PASS

The claim is restricted to one-seed exponential downstream travel and to the stated two-band geometries. The equal-width calculation gives an explicit logarithmic derivative whose derivative is strictly negative because \(\cosh(\delta x)>\sinh(\delta x)\ge\delta\sinh x\) for \(\delta\ge1\). The scaled-width calculation uses four sign inequalities, followed by the exact upper bound of three zeros of a four-term exponential polynomial. The extra rescaling comparison proves that the longer-range local maximum is the unique global maximum. Universal results are analytic; numerical calculations only supplement them. An extracted standalone checker passes exact bounds, a Sturm count at \(L=9\), root and objective comparisons, and illustrative curvature tests.

## Originality — PASS on inspected evidence

The closely related de Jager–Soons study (2022 preprint; 2023 published study) already reports simulated dispersal fitness valleys and evolutionary hysteresis in a different nonlinear habitat-cell model. The general *qualitative* phenomenon is not claimed as new. The present claim instead distinguishes arbitrary separations of equal-width habitats (global strict log-concavity, no local traps) from geometrically scaled two-band habitats (exactly three critical rates for every \(L\ge9\) and a strict global choice), with explicit mathematical hypotheses and a self-contained proof. Treep et al. (2021) analyze a two-dimensional Pareto kernel and complex dynamic patch mosaics, while Finand et al. (2023) analyze evolving metapopulations with competition/colonization tradeoffs. Searches for exponential-kernel, two-interval and bimodal-optimizer equivalents, and comparisons with public mathematical research summaries concerning dispersal and recruitment spectra, produced no inspected implication of the exact two-part theorem. Search non-retrieval is not proof of priority; unexamined literature remains a residual risk.

## Value — PASS

The gap is a meaningful width-versus-spacing distinction in a minimal, physically normalized seed deposition objective. In this model, merely separating two bands of equal width never creates a second dispersal optimum, however widely spaced; sufficiently heterogeneous widths can. This identifies which part of landscape geometry is responsible for a non-quasiconcave optimization landscape without relying on seed-number saturation or competition. The general equal-width theorem, a uniform sufficient regime \(L\ge9\), and the global ranking of both local peaks are reusable analytical benchmarks for subsequent, biologically richer transport and establishment models. The chosen family uses natural logarithmically similar habitat bands, not an arbitrary finite parameter list.

## Closest literature and limitations

The closest overlap is de Jager and Soons, *Ecology and Evolution* 13 (2023), e10147, DOI https://doi.org/10.1002/ece3.10147, originally circulated as https://doi.org/10.1101/2022.10.10.510956. Its numerical fitness-valley observations do not state the present exact two-band theorem. Further comparisons: Treep et al., *Movement Ecology* 9 (2021), 4, https://doi.org/10.1186/s40462-020-00239-1; Finand et al., *Oikos* (2024), https://doi.org/10.1111/oik.10490.

Only the sufficient range \(L\ge9\) is proved; the exact bifurcation location in \(2<L<9\) is not. The two geometrically scaled bands have unequal absolute widths, so isolated distance-versus-area causation is not claimed. No evolutionary hysteresis, demographic persistence, empirical calibration or priority certification is established.

Self-review: passed. Independent audit: not yet performed.
