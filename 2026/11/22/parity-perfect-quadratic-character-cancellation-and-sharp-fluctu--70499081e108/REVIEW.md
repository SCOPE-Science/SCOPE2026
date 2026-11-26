# Independent mathematical audit

## correctness

PASS

The complete half-open rows propagate under (a,b)↦(a,a+b),(a+b,b) modulo 5 from (1,1). An exact independent replay produced all 24 zero Cayley–Hamilton defects D_j=B_{j+4}−B_{j+2}+4B_j, j=0,…,23, and the four initial values 1,0,−2,0 (replay: /workspace/branches/205f41a5-0617-4437-8dc1-b6ef0ab5b8b9/replay_24state.py; frozen code not executed). Independently, symmetrize the observable to h=(χ_5(a)+χ_5(b))/2, which gives identical evaluation at the swap-invariant root after any number of steps. Symmetric functions with f(ta,tb)=χ_5(t)f(a,b) are determined by g_0,g_1,g_2,g_4 at (1,0),(1,1),(1,2),(1,4): the missing slope values obey g_∞=g_0 and g_3=−g_2. The backward transfer sends this vector to (g_0+g_1,2g_2,−g_2−g_4,2g_0), of characteristic polynomial X^4−X²+4, and h has coordinates (1/2,1,0,1). Evaluation at the root is g_1. This proves the scalar recurrence and initial values directly and gives the stated rational generating function. Parity follows from its even powers; starting with B_2=−2, reduction of the even recurrence modulo four gives B_{2j}≡2 for every j≥1. The characteristic roots and initial values give c and α as stated. If α/2 were a root of unity, 2Re(α/2)=1/2 would be a rational algebraic integer. Hence the angle is an irrational rotation, so the even normalized values are dense in the interval with endpoints ±2|c|=±sqrt(8/3). The odd values are zero, and the endpoints are limsup and liminf, not asserted to be attained at finite depth.

## originality

PASS

The exact character projection on complete dyadic rows, its perfect parity law, and its oscillation constant are distinct from all checked statements. The transfer mechanism, square-root spectral scale and quartic factor are not credited as novel. The full consecutive-pair spectrum on the same modulus is substantive overlapping evidence, but does not identify the active scalar component, its initial values or amplitude.

## value

PASS

The quadratic character directly measures a natural residue bias. Exact equality at every odd depth and nonzero even discrepancies with both sharp signed accumulation endpoints cannot be inferred from equidistribution or from a bound on the growth rate of individual-pair discrepancies. The result separates a parity cancellation law from an active square-root oscillation and supplies the precise finite-row statistic, not merely a recomputation of an eigenvalue modulus.

The dated certificate retains the supplied scientific assessment, sources and limitations.
