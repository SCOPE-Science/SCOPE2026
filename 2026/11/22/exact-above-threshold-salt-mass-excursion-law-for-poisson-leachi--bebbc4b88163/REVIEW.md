# Scientific review

**Claim assessed:** exact Tricomi-\(U\) transform of the first strictly downward passage from a fixed positive threshold by the constant-input, Poisson-leaching Beta-multiplicative process; with a finite-threshold total-variation comparison to the first Poisson wait. This is a mathematical result about a specified stylized environmental model.

## Correctness: PASS

The event factors have distribution \(\Pr(R\le r)=r^a\). Conditioning on the jump gives a stopped generator integral from zero to the current mass, including the immediate-termination contribution below the threshold. The exact *right* boundary derivative, reduction to Kummer's ODE, exclusion of the exponentially growing solution, recovery of the original integral equation, and bounded stopped-martingale uniqueness together give the stated transform. First-event coupling supplies the rigorous high-threshold total-variation estimate. Four settings of \(30{,}000\) simulated paths passed independent numerical diagnostics against the transform and known mean, without replacing infinite-parameter proof. The scope is all strictly positive parameters with \(s>0\), extending to \(s=0\) by continuity.

## Originality: PASS, with historical-priority risks

Suweis et al. (2012) establish the input/leaching model and stationary gamma salt mass; Suweis et al. (2011) establish relevant jump prescriptions. Tamea et al. (2011) exactly give mean and infinitesimal-duration crossing quantities but **approximate** full excursion duration densities. Löpker and Stadje (2009), Section 4.2, give Kummer-\(M\) upward-hitting transforms for these jump factors, not this downward-exit transform with a distinct condition at infinity. Accessible older claims and published-finding corpus search results did not reveal the exact full-duration transform or a direct stronger implication. A 2005/2006 Boxma et al. source remains a genuine risk because its archived report link was inaccessible and institutional retrieval could not proceed. Existing level-crossing/ruin theory could also contain an equivalent formulation. Lack of a matching title or search result is not treated as uniqueness proof.

## Value: PASS

A static exceedance probability or mean episode duration does not determine uninterrupted salt-stress durations. The exact transform provides a self-contained starting point for time-dependent threshold-duration probabilities and moments, while the explicit error bound identifies when a single-storm waiting-time approximation is controlled. This addresses a recognizable gap between exact stationary modeling and approximated excursion distributions, rather than a renamed known formula or an arbitrary parameter slice.

## Limitations

The model is one-dimensional, has constant positive salt input and homogeneous independent Poisson leaching, and treats soil salt mass, not soil-water concentration. Numerical inversion may be needed to recover CDFs. Neither the model nor the checker constitutes a field calibration. Completeness against every historical first-passage result cannot be guaranteed; independent audit has not been performed.

Self-review: passed. Independent audit: not yet performed.
