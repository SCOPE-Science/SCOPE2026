# Independent mathematical audit

## correctness

PASS

Folding circle doubling sends a point to the same tent coordinate precisely when the two circle inputs differ by sign. Thus for the Nth iterate the denominators are m+1 and m-1, m=2^N. Folding gives the stated two grids, meeting only at zero. The difference formulas for consecutive interlaced nodes, including the terminal interval to 1, show the unique largest gap is [0,2/(m+1)]. The least positive point from each smaller k is strictly larger, and 1/2 lies outside that first gap for N>=2. For h=g-T, absolute continuity and the slope bound give |h(x)|<=delta times the distance to the nearest mesh endpoint on each gap. A triangle with slopes +/-delta on the first gap attains the bound, and g remains monotone onto [0,1] on each branch. Each inverse word of length k is contracting. It has one fixed point, and different words cannot share one because the only point common to both branch domains is the critical point, which is preperiodic to zero and not periodic. The 2^k fixed points therefore exhaust the preserved reference orbits, and the maps have identical actions on them (same next point and ordering). A Lipschitz triangle supported strictly inside the first gap, smoothed by nonnegative convolution with sufficiently small support, retains the slope bound and approaches the same height. It agrees on neighborhoods of the entire observed set, hence preserves every defined jet and multiplier, with endpoint derivatives interpreted one-sidedly. In that subclass the bound cannot be attained: vanishing near zero shortens the only extremizing gap. An independent exact rational inverse-word enumeration checked the unique largest gap for N=2..12; the supplied checker was inspected, not executed. The all-N proof is analytic.

## originality

PASS

The supported distinct result is the exact ambiguity for the all-periods-through-N geometric map data in the normalized slope-constrained class, with absence of extra short orbits and the same sharp supremum under local agreement at all observed points. The rational grids, Lipschitz recovery envelopes and broad finite-period nonuniqueness are related prior ingredients, not separate novelty claims.

## value

PASS

In the natural fixed-height two-branch model, the theorem gives an exact worst-case spatial resolution at every cutoff, not just an asymptotic rate or a construction changing the number of branches. The same supremum after matching every observed orbit locally makes the constant relevant even when positional measurements are supplemented by all local derivatives and multipliers. This is a specific finite-data complement to complete-spectrum rigidity, not an upper bound for unlabelled measurements or noisy data.

The dated certificate retains the supplied scientific assessment, sources and limitations.
