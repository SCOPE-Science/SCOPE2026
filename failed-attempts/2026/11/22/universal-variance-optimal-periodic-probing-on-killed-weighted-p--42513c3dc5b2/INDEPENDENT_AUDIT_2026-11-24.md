# Independent mathematical audit

## correctness

PASS

The Rademacher cross terms from distinct unordered pairs are orthogonal, so the variance is four times the sum of G_ij² over monochromatic unordered pairs (equivalently twice the ordered sum). The homogeneous left and right solutions are strictly monotone by induction with positive killing; the interior equations conserve the conductance-weighted Wronskian. The piecewise product solves each inverse column: the single diagonal jump, including the one-sided endpoint cases, contributes precisely that Wronskian. Squaring the product and telescoping both positive increments gives the interval kernel, including its boundary coefficients. Each interval count-square sum is minimized by balanced counts, and residues balance every interval at once. Equality forces each length-k window to have all colors, hence entering and departing colors agree; k=1 is trivial, and k=n consists of singletons. A collision in a length-k window costs at least two count-square units, giving the stated factor four. Independent bounded replay: python /workspace/replay/checks.py 2 constructs a new rational five-site matrix, computes exact variances by averaging over all sign vectors, and checks interval gaps and k! labeled optima for each budget. It is a normalization and uniqueness check on that instance, not the proof for all paths.

## originality

FAIL

A distinct Resultary result proves the same optimization and exact interval gap for a larger class containing the assigned inverse. The explicit local lower bound is obtained simply by retaining the defective length-k interval terms. This is mathematical coverage, not a priority determination between same-date records.

## value

FAIL

The estimator design question is well motivated, but as a standalone contribution the proposed theorem is a point-mass specialization of the existing general interval balance result; the local bound merely discards nonnegative terms in the same exact gap. The audited scope supplies no independent new quantitative or structural conclusion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
