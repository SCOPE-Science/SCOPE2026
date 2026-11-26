# Independent mathematical audit

## correctness

PASS

Block integration gives stationary weights (p,1-p), centered label eigenvalue lambda, and the stated admissible interval; at a zero diagonal with |lambda|<1 the other diagonal is positive, so irreducibility and aperiodicity still hold. The compensated bounded label differences have mean squared value v(1-lambda^2), giving knot variance v(1+lambda)/(1-lambda) in the limit. Conditional on the labels, observations can be drawn from two independent uniform sequences independent of the labels. Applying Donsker to each sequence at its random count, whose ratio to n converges to the corresponding block mass, gives two independent residual bridges independent of the limiting label fluctuation. Their linear knot interpolation adds h_p(s)h_p(t) times the knot variance, yielding the stated rank-one covariance perturbation. Given the knot y, each conditional bridge's survival is its killed transition density divided by its free density; the factor 1/z in the sine series follows from the eigenfunction squared norm z. Bridge maximum and minimum distributions are continuous at positive barriers, so open and closed events agree. Strictness follows by adding the independent nondegenerate normal increment when the variance increases: Anderson bounds each shift probability by its value at zero, and shifts of large enough magnitude have strictly smaller probability by the knot constraint, on a set of shifts of positive mass. Alternating labels give deterministic half proportions up to O(1/n), hence the squared CDF of two independent bridges with amplitude 1/sqrt(2). At the absorbing endpoint the conditional uniform-block empirical CDF converges uniformly to the block CDF, with discrepancies 1-p and p as stated.

## originality

PASS

Longla's published model, general spectral construction and specialized two-level parametrization are prior. Credit is confined to the full two-sided ordinary-EDF calibration: the exact one-dimensional law, strict parameter ordering and endpoint classification together. The closest inspected testing comparison uses weighted residual EDFs and simulation, and the closest distinct bridge record treats another observable. No statement-level coverage of the full calibration was established in the checked material.

## value

PASS

The asymptotic CDF is evaluable through one scalar integral, and strict stochastic ordering identifies the direction of the iid test's size error at every nontrivial threshold, not merely larger or smaller covariances. The endpoint calculations separate a nonmixing chain with useful scaled KS calibration from a stationary nonergodic one with an inconsistent EDF. These are concrete, independently useful claims for a known null model, beyond standard weak-limit existence or a change of parameters.

The dated certificate retains the supplied scientific assessment, sources and limitations.
