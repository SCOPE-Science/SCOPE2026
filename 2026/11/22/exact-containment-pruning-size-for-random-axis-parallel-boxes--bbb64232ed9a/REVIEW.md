# Scientific notes — containment-minimal random boxes

## Correctness
The sampled side lengths are independent with density \(2(1-x)\), and conditional containment probability is the square of the sampled box's volume. The product density has the logarithmic singularity from simplex convolution; Gaussian scaling gives the leading constant, and the planar product density gives the second term. Deterministic pruning requires treating coincident labeled copies as one constraint before removing boxes that contain distinct sets. The count and asymptotics in the continuous model are unchanged, since coincidences have probability zero. The recorded finite checks do not prove the asymptotics.

## Originality and scope
The exact one-dimensional mean is equivalent to the known minimal-interval formula and is not claimed as a new result. The claim concerns the multidimensional expectation, its fixed-dimensional leading coefficient, and the planar second term. Tran's piercing number, Coffman et al.'s size of a disjoint packing, and Chao et al.'s union measure are different observables. Related multivariate-extrema formulas and auxiliary results in the literature remain possible; the comparisons do not establish historical priority.

## Value and limitations
The result quantifies the mean number of surviving constraints after a natural lossless preprocessing rule for piercing instances, including the logarithmic dimensional factor. It does not improve the optimal piercing bound, describe the retained-size distribution, or give a runtime guarantee.
