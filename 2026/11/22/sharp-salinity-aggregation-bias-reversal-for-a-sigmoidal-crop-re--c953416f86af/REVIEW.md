# Review of the exact salinity-aggregation threshold

## Correctness: PASS

The population law is an area-weighted distribution with finite positive support, not a measurement-error model. Factoring the distributed-minus-composite yield bias produces the difference of two positive Stieltjes-type integrals. Their ratio increases strictly because the pairwise cross-product numerator is positive for every salinity pair straddling the mean. Strict Jensen inequalities establish all endpoint signs and the single crossing for response exponent greater than one. Direct rational factorization gives the exact cubic two-class threshold; differentiating its contrast denominator proves the sharp unattained bounds. The supplied Python checks are supplementary and not substitutes for this proof.

## Originality: PASS (historical-priority qualification)

The 1993 van Genuchten–Gupta article was inspected in its lawful full-text copy. It establishes the original crop-response law and the cubic approximation, but does not address comparing spatial mean yield against yield at mean salinity. The accessible 2013 hydrosalinity and 2015/2016 regional aggregation sources motivate the effect without giving this exact conditional threshold in the material inspected. Broad total-positivity results already imply at-most-one changes for suitable kernels; this component is explicitly not new. The original contribution claimed here is the combination of the response-exponent sign classification with a directly evaluable cubic two-class threshold and sharp heterogeneity-contrast interval in the crop-salinity model. Material unresolved risk remains because the 2013 paper's full text and some aggregation literature were unavailable, and general machinery could be specialized to imply further parts of the statement.

## Value: PASS

The distinction between area-average predicted crop yield and crop yield predicted at mean soil salinity is a concrete issue in scaling heterogeneous irrigation fields. The theorem decides the bias direction for all common salinity scales, and the exact cubic two-class cutoff gives a measurable, dimensionless switch governed by salinity contrast. Knowing that a spatially aggregated model can switch between over- and underprediction prevents assigning a universal direction to aggregation error. No application to real crop management is claimed without calibration and spatial transport modeling.

## Closest literature and limits

Van Genuchten and Gupta (1993), *A Reassessment of the Crop Tolerance Response Function*, https://www.ars.usda.gov/arsuserfiles/20361500/pdf_pubs/P1295.pdf; Alzraiee, Gates and Garcia (2013), *Modeling Subsurface Heterogeneity of Irrigated and Drained Fields. II*, https://doi.org/10.1061/(ASCE)IR.1943-4774.0000587; Hoffmann et al. (2015), https://doi.org/10.3354/cr01326 and (2016), https://doi.org/10.1371/journal.pone.0151782; established variation-diminishing theorems described in https://doi.org/10.1016/j.jmaa.2015.03.002. The checked primary full text concerns a fitted local response curve, not an exact spatial threshold. Other potentially equivalent applications may exist. Independent validation and historical-priority certification have not occurred.

Self-review: passed. Independent audit: not yet performed.
