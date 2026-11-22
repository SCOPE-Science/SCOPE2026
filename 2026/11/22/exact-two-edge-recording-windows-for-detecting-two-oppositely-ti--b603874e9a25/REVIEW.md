# Scientific review of the two-species acoustic recording theorem

## Correctness — PASS

The two species' independent no-call probabilities yield the objective. Exact integration gives the two edge-window intensities. Their second derivatives and the strict concavity of the logarithmic detection factors prove a unique split inside the proposed family. The critical global step is not inferred from finite optimization: at that split, the positive weighted intensity is strictly convex over the night, and the chosen edge windows are precisely its unique top-measure set. The supporting-line inequality for the concave logarithmic objective proves global optimality and uniqueness among **all measurable recording sets**. One-sided derivative signs give nonoverlapping sharp thresholds. Reflection and a uniform small-budget expansion yield the two limiting statements. A standalone computational checker passed 11,846 finite assertions; no numerical result is used as an infinite proof.

## Originality — PASS, provisional to inspected evidence

Full article text inspected for Skalak et al. (2012, https://doi.org/10.1111/j.2041-210X.2011.00177.x), Stahlschmidt and Brühl (2012, https://doi.org/10.1111/j.2041-210X.2012.00188.x), Petitot et al. (2014, https://doi.org/10.1002/ece3.1207), and Balantic and Donovan (2019, https://doi.org/10.1002/ece3.5579). The closest is Balantic and Donovan's weighted hourly optimization, but that algorithm ranks hourly species-priority scores; it does not prove the exact global continuous optimum for the joint **both-species** detection probability under opposed exponential rates. The ecological survey papers discuss seasonal/diurnal detectability and empirical effort allocation, not the sharp three-regime theorem. Searches against published mathematical research records returned related single-species survey timing, Fisher-information experiments and Poisson counting optimizations, but no implication covering this stated result. The familiar threshold-set technique is not represented as independently novel. Residual risk remains from uninspected general variational theorems or historical scheduling results in other terminology.

## Value — PASS

Under a natural single-device data/storage budget and two temporally complementary targets, the theorem replaces arbitrary measurable-window search with one scalar equation and predicts an exact transition from split dusk/dawn monitoring to one-sided recording when one target is sufficiently common. This is a motivated complete classification, not merely a numerical optimum or a tiny improvement. It also proves that at vanishing recording budget the optimal split is asymptotically balanced regardless of fixed species intensity imbalance, revealing a counterintuitive regime transition. These claims are mathematical reference results; no real wildlife species is asserted to have the stipulated exponential time profile.

## Closest coverage and limitations

The closest inspected algorithmic source is Balantic and Donovan (2019); its weighted, discrete adaptive score is not the same objective. General supporting-hyperplane/bathtub principles provide proof tools and may offer a general theoretical framing, but an explicit competing classification was not found. Model restrictions: two independent Poisson calling species, exactly opposite exponential intensity shapes, perfect detection, fixed recording-time measure and no minimum window size/switching penalty. Priority should receive independent review.

Self-review: passed. Independent audit: not yet performed.
