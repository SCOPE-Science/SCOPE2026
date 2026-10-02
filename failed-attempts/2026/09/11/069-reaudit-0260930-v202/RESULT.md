# Tropical independence of an explicit triple on a mixed-torsion genus-5 chain

## Context
The Jensen–Payne tropical independence program proves Gieseker–Petri and maximal-rank-for-quadrics theorems via shapes of divisors in tropical linear series, and states combinatorial conjectures about independence on chains of loops. Concrete correctly-quantified genus-5 shapes on mixed-torsion chains are recognized missing data points: they test which slope patterns impose independent conditions and give regression tests for independence checkers.

## Definitions
Let Gamma_MIX5 be the genus-5 chain of loops with loop lengths (1,2,5,7,11) (torsion profile 2,5,7,11 on loops 2–5), spine nodes v0=0, v1=8, v2=16, v3=24, v4=32, v5=40, bridges of length 8, and a midpoint kink m=20 on bridge B3=[16,24]. Let D = 2·v1 + 2·v3 + 2·v5 (degree 6). A piecewise-linear function psi with integer slopes lies in R(D) iff D + div(psi) is effective, where ord_p(psi) is the sum of outgoing slopes (Baker–Norine convention). A triple {psi0,psi1,psi2} ⊂ R(D) is tropically independent (Jensen–Payne) iff there do NOT exist constants b0,b1,b2 such that min_i(psi_i+b_i) is attained at least twice at every point; equivalently, for every constant triple the minimum is attained uniquely at some point.

## Result
On Gamma_MIX5 with D as above, the three functions constant on all loops and given on spine segments [v0v1,v1v2,v2m,mv3,v3v4,v4v5] with psi_i(v0)=0 by slopes psi0=(0,0,0,2,1,1), psi1=(0,1,1,1,1,1), psi2=(0,2,2,2,2,2) all lie in R(D) and are tropically independent. The certificate is translation-stable: for every (b0,b1,b2) in R^3, bridge B2=[8,16] contains a nonempty open interval on which exactly one of psi_i+b_i is strictly smallest, and any point there is a global unique-minimum witness. The largest such open piece has length at least 2.

## Proof / evidence
R(D) membership: with outgoing-slope convention, ord at interior spine vertices is right-slope minus left-slope; at v0 ord=s0; at v5 ord=−s5; at midpoint kink m ord=s3−s2. Vertex table: psi0 gives D+div (0,2,0,1,0,1) with m-ord +2 (valley 0→2); psi1 gives (0,3,0,2,0,1) with m-ord 0; psi2 gives (0,4,0,2,0,0) with m-ord 0. Every entry is ≥ 0; on loops the functions are constant so ord=0 where D=0. Each function has a genuine bend (psi0 at m; psi1, psi2 at v1) and distinct slope vectors, hence distinct mod constants. Envelope: on B2 the restrictions are affine lines of slopes 0,1,2. Two distinct lines meet at most once, so at most 3 tie points lie on the length-8 bridge; the complementary open pieces always include a nonempty interval where one line is strictly smallest, stable under all additive constants. Script output/artifacts/verify_target.py (stdlib only) replays MEMBERSHIP_OK, DISTINCT_SLOPES_OK, DISTINCT_FUNCTIONS_OK, GRID_OK over 21^3=9261 integer triples b_i in {−40,…,40 step 4} via an analytic tie-solver, RANDOM_OK over 20000 random float triples in [−100,100]^3, ending VERIFY_OK.

## Limitations
The torsion profile (2,5,7,11) enters the loop geometry, but the certificate is uniform in those lengths (loop-constancy for membership, bridge B2 only for the envelope). Loop-crossing variants of these functions would need torsion-specific monodromy checks, not claimed here. Only this explicit triple is decided; no general statement about all 0-1-2 patterns on mixed-torsion chains is claimed.

## Reproducibility
Run `python3 output/artifacts/verify_target.py` with the Python standard library only; expect final line VERIFY_OK. Segment nodes, slope table, divisor D, and the outgoing-slope ord formulas are documented in the script header.

## References
Jensen–Payne, Tropical independence I: Shapes of divisors and a proof of the Gieseker–Petri theorem, Algebra Number Theory 8 (2014), doi:10.2140/ant.2014.8.2043. Jensen–Payne, Tropical independence II: The maximal rank conjecture for quadrics, Algebra Number Theory 10 (2016), doi:10.2140/ant.2016.10.1601, arXiv:1505.05460. Cartwright–Jensen–Payne, Lifting divisors on a generic chain of loops.
