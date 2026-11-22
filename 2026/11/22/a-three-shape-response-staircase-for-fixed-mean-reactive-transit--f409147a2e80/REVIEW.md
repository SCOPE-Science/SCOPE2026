# Review of the three-shape transit-response theorem

## Correctness

**PASS.** The normalized gamma Laplace transform is derived from the assumed rate parameters, and all rates are positive. The three rational difference identities and their strictly negative logarithmic elasticities imply exactly one positive crossing for every pair. A polynomial division with an everywhere-positive remainder at the \(1\)-versus-\(2\) crossover forces the \(2\)-versus-\(3\) crossing to precede it; uniqueness places the remaining crossing in between. The exact response classification is a consequence of these inequalities, not a finite simulation. The supplementary standalone checker passes 438 deterministic assertions.

## Originality

**PASS under documented literature scope; priority provisional.** Established gamma transit-time distributions, consecutive first-order reaction models, and multi-tank cascade formulas are fully acknowledged. Green et al. (2010), Hrachowitz et al. (2010), van der Velde et al. (2010, 2012), and Frei et al. (2019) do not establish the specified all-positive-rate three-shape universal ordering. Mongelli (2018) studies optimized unequal vessel volumes for a fixed three-vessel cascade rather than comparing the 1-, 2- and 3-stage equal-mean cases. A broader reactor-design text could potentially contain the same ordering; this is an explicit residual risk, not an assertion that no such source exists.

## Value

**PASS.** The analytical classification supplies a complete change-of-optimum phase diagram and shows that pairwise crossings cannot arrive in arbitrary order. This is a meaningful structural benchmark for the ambiguous effect of residence-time dispersion on an activation-plus-attenuation response, with a distinctive intermediate regime that is not justified by covariance or variance comparisons alone.

## Limits and closest literature

The theorem applies to a stylized parcel-scale response and integer gamma shapes \(1\), \(2\), \(3\). It does not calibrate a catchment or prove engineering cost-optimality. Primary sources and comparisons: https://doi.org/10.1029/2009WR008903; https://doi.org/10.1029/2010WR009148; https://doi.org/10.1029/2010WR009105; https://doi.org/10.1029/2011WR011310; https://doi.org/10.1029/2019WR025540; https://doi.org/10.31031/RDMS.2018.05.000621.

Self-review: passed. Independent audit: not yet performed.
