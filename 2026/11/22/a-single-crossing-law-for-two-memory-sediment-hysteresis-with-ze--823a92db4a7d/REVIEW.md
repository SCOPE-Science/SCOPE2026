# Self-review

## Correctness — PASS

The claim concerns exactly the explicitly defined piecewise-linear excess hydrograph and a positive two-exponential memory response, with arbitrary continuous positive discharge rating. Subtracting matched-discharge branches gives a positive factor times the difference of two strictly positive hyperbolic-sine expressions. The derivative of \(x\coth x\) is strictly positive for positive \(x\), establishing a strictly decreasing source ratio and **exactly** the three threshold regimes, including equality. Positively weighted averaging proves the zero-area ratio lies strictly inside the two-lobe regime. An elementary integral yields the explicit linear-rating formula; a strict differential inequality proves the same-time unique maxima. The checker's finite tests corroborate but do not replace these analytic arguments. The source-model assumptions, the transverse crossing, and the signed-area orientation are stated rather than inferred from data.

## Originality — PASS, with historical-priority uncertainty

The specific conclusion assessed is the full necessary-and-sufficient two-memory source-ratio trichotomy, source-rating-independent uniqueness, exact interior zero-area cancellation, and a simultaneous-single-peak construction. Williams (1989) gives a qualitative five-class loop taxonomy, not an inspected exact two-rate theorem; its full article text was unavailable. Mather and Johnson (2014) use an exponential supply term with a discharge-slope term and fit complex measured loops, rather than giving the two independently opposing exponential-memory ratio theorem. Perks and colleagues (2015) describe measured figure-eight events and multiple pathways but do not state the present mathematical classification. Landers and Sturm (2013) address sediment-versus-turbidity calibration, a different observable pair. Later reviews discuss zero scalar-index values and figure-eight loops; those phenomena **are not claimed as new**. Indexed mathematical results on runoff timing, multiple hydrograph peaks, and linear-reservoir hysteresis have different state variables, parameter questions and hypotheses and do not imply the exact branch-ratio thresholds. The plausible uninspected 1989 full text and additional unindexed hydrology literature remain priority risks; this is not a claim of proven historical uniqueness.

## Value — PASS

For a motivated two-source hydrological memory model, the result gives sharp boundaries separating one clockwise loop, a reverse-oriented two-lobe event, and one counterclockwise loop. It proves that discharge peak order and a single net signed-loop statistic can both conceal a real change in source dominance, even under a rigorously single-peaked response. The classification is invariant under arbitrary positive discharge-rating factors; the cancellation ratio is exact and computable for a linear rating. This provides a self-contained test case for interpreting storm-event hysteresis measurements and validating branch-aware diagnostic algorithms; no empirical superiority or source identifiability is asserted. The value is the structural, complete phase classification, not the mere existence of figure-eight events.

## Closest literature and limitations

- Williams, “Sediment concentration versus water discharge during single hydrologic events in rivers,” 1989, DOI 10.1016/0022-1694(89)90254-0 (abstract inspected; full article unavailable).
- Landers and Sturm, “Hysteresis in suspended sediment to turbidity relations due to changing particle size distributions,” 2013, DOI 10.1002/wrcr.20394 (full HTML inspected).
- Mather and Johnson, “Quantitative characterization of stream turbidity-discharge behavior using event loop shape modeling and power law parameter decorrelation,” 2014, DOI 10.1002/2014WR015417 (full HTML inspected).
- Perks et al., “Dominant mechanisms for the delivery of fine sediment and phosphorus to fluvial networks draining grassland dominated headwater catchments,” 2015, DOI 10.1016/j.scitotenv.2015.03.008 (author-accepted full PDF inspected).
- “A Review of Suspended Sediment Hysteresis,” 2024, DOI 10.1029/2024WR037216 (full HTML contextual comparison inspected).

The model is normalized, phenomenological, noise-free and not a mass-conserving sediment PDE. It does not certify priority or make predictions for unmodeled sediment dynamics. The analytic proof establishes infinite-parameter results only under its written assumptions. The finite checker is supplementary. Some older full texts could not be inspected. No independent scientific validation was performed.

Self-review: passed. Independent audit: not yet performed.
