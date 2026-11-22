# Scientific review: source-distance Petersen sandpile avalanche law

## Correctness (PASS)
The claim is an exact, finite, two-orbit, joint stationary distribution, with 2,000 recurrent configurations and the 44 counts in `JOINT_COUNTS.csv`. The recurrence count agrees with Kirchhoff's theorem using the graph's explicitly derived spectrum. Two independent graph constructions, two equivalent but separately implemented recurrence criteria, and sequential versus parallel integer topplings verify every coefficient without sampling. Graph automorphisms reduce nine sources to the two examined source classes. Monotonicity and the all-two recurrent configuration give analytic sharp upper bounds of 9 and 24; the verified legal toppling sequences attain them. The Laplacian inverse and conservation supply independent means. No infinite-volume assertion is made.

## Originality (PASS on examined evidence; historical priority not certified)
The closest established foundations are Dhar (1990), which derives general recurrent stationary measures and expected toppling Green functions, and Austin et al. (2016), which defines avalanche polynomials and solves several other graph families. Their examined full-text material does not provide the specific two-source Petersen joint data. The generic SageMath routine has general ability to compute avalanche polynomials, but its inspected Petersen example does not display the values here. Other indexed finite-graph sandpile findings examine the icosahedral graph, fan graphs, and complete bipartite graphs, and so have no direct implication covering this joint distribution. The known general maximal-avalanche count for sink-neighbor sources is credited as consistency, not novelty. There is residual priority risk from unlocated Petersen calculations and general-purpose symbolic software.

## Value (PASS)
This is a motivated exact finite statistical-mechanical observable: source-conditioned stationary activity and physical sink dissipation on the smallest bridgeless cubic non-three-edge-colorable graph. The full natural joint law is more informative than means or maximum activity alone, distinguishing a nine-toppling, one-wave regime from a rare 24-toppling multiple-firing regime with a four-size gap immediately before its maximum. It is a reproducible benchmark for finite self-organized critical dynamics; no unsupported large-system inference is necessary for that use.

## Scientific scope and limitations
The claims concern deterministic, undirected Abelian sandpiles, exactly one sink, one grain added at a specified source, and the uniform recurrent measure on the ten-vertex Petersen graph. Generic recurrence and Green-function facts are not novel. No independent scientific audit, historical-priority certification, or asymptotic interpretation is asserted.

Self-review: passed. Independent audit: not yet performed.
