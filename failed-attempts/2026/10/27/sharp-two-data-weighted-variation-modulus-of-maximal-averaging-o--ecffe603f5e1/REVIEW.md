# Independent mathematical audit

## correctness

PASS

The center and leaf ball averages give the stated gradient map with μ=(Σg_i)/(m+1). Every gradient vector is realizable by positive data by raising the center baseline. Put a=1/(m+1). On an affine cell with center selector zero, column j has magnitude at most 1 in row j and a in every other row. With center selector μ the diagonal magnitude is at most 1−a and the other rows are still bounded by a. Multiplication by w_i and division by w_j gives the stated global bound by partitioning a line segment at the selector hyperplanes, with continuity for ties. At the displayed witness the center selects zero, the distinguished minimum-weight leaf selects itself, and all other leaves select μ=−a/2. A positive increment smaller than 1/2 has output gradient increments exactly t at that leaf and at each other leaf at; this realizes the bound. For one leaf the relative output is g_1/2 for either sign. With fixed W the bound for m≥2 is strictly decreasing in w_min, so equal weights uniquely minimize it. In the signed example the initial difference is constant but every output edge-gradient difference has magnitude 1/2+a. Perturbing one leaf of h by t makes the denominator w_1|t| and the numerator tend to W(1/2+a). The frozen checker was inspected, not executed; its formal-mask and finite data tests are not needed for the universal proof.

## originality

FAIL

The distinct indexed November 17 record covers the equal-weight theorem exactly. Although its headline is unweighted, its proof gives the same gradient map, selector rows, and a sharp secant along any distinguished coordinate, with the full output-increment vector specified. These data mechanically give the arbitrary-weight exact modulus by componentwise weighting and choosing a minimum-weight coordinate. The two-vertex and signed-domain conclusions are also covered or mechanically inherited. This is a determination of coverage, not an assertion that the November-labeled record was first or that the October-labeled frozen artifact was derived from it.

## value

FAIL

The distinction between one-input contraction and two-input expansion is meaningful, and unequal edge weights are a natural parameter. However the frozen new quantitative content is a direct weighted column sum of the already specified extremal secant and selector bounds. The minimizer, divergence and signed extension add no independent mathematical obstruction. Thus the claimed narrow invariant does not clear the value standard once the exact indexed proof is credited.

The dated certificate retains the supplied scientific assessment, sources and limitations.
