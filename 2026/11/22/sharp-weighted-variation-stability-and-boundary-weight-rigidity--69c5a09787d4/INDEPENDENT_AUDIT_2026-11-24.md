# Independent mathematical audit

## correctness

PASS

RESULT.md lines 35–67: on every strict order cell, the derivative is the half-sum of the two selector rows in each window and fixes constants. For the step basis of the input quotient the output is fixed at 0 and 1 outside the two mixed rows. At internal cut j the two mixed values lie in {0,1/2} and {1/2,1}; evaluating extremes in both triples at each of the four explicit adjacent quadruples on line 57 confirms all four profiles are jointly possible. In particular the profile is nondecreasing across the cut and the weighted variations are exactly the four expressions given. At cut 1 the endpoint response is 1/2, the second response is 1/2 or 1 according as index 1 is extreme or middle in its triple, and the later responses are 1. This yields max(w_1,w_2)/(2w_1); reflection gives the other boundary. With n=3 the two boundary columns give max(w_1,w_2)/(2 min(w_1,w_2)); with n=2 both windows are identical and the coefficient is zero, attained by any nonconstant perturbation. Weighted l1 column norms and subdivision of generic segments prove the global bound; continuity handles ties, and sufficiently small strict-order perturbations attain it. Each interior inequality F_j<=w_j forces both neighboring weights <=w_j; hence all interior weights equal c and the two endpoints lie below c. The boundary ratios then require both endpoints >=c/2; these constraints also suffice, independently at each end, including n=4. Independent replay `python3 -I /workspace/review-work/replay.py 4` calculated 34,406 exact pairs by directly reevaluating midpoint extrema at each perturbation for n=2–7, recovering the signed edge profiles. The frozen script was inspected but not executed; finite checks do not establish the all-length proof.

## originality

PASS

The mathematical contribution is the sharp weighted coefficient of the symmetric mean of the two selectors at every path length, and the exact independently tapered boundary regime. The filter itself and uniform-weight contractivity are prior or mechanically implied; neither is credited as new. The strongest distinct indexed statements provide the cyclic unweighted law, exact norms of the separate extrema, or an endpoint-preserving median law, not the stated sharp nonuniform truncated-path coefficient. The possible proof-level overlap with weighted median selector profiles remains limited by mirror access.

## value

PASS

The largest amplification of perturbation variation for this classical filter is a useful stability invariant. The sharp weighted classification gives a finite factor-of-two taper freedom at independently chosen boundaries and a rigid interior, and the constituent contrast shows why separate operator bounds would give the wrong admissible weights. The contribution is this full nonuniform classification and norm, not already-known unweighted contraction or a general claim about statistical performance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
