# Independent mathematical audit

## correctness

PASS

The normalized return follows by one power-law step and M−1 linear steps. The fixed point and derivative −1 equations give the stated z_* and K_*, and z_*>ν puts even the last intermediate linear-branch point strictly above the switch. A single nonlinear visit forces primitive period M. Along the nearby fixed-point branch, dρ/dz=−a(1−u)/(1−z)^2<0, dz/dK>0, and dK/dμ<0, so the flip is transverse. Independent composition yields A=−2(b₂²+b₃), B=−b₂A/2. At A=0, set v=2−a and d=1−z_*; in units of d the doubled coefficient is v²(2v−3)(v−3)/405. Dividing by d^4 with d=a(1−2a)/(2(1−a²)) gives the claimed negative quintic. The unique zero lies between 0 and 1/2 by monotonicity and the sign at the endpoints. Reciprocal fourth powers have increments tending to 4κ after local contraction, giving the exact nonfixed-orbit asymptotic. The rational obstruction follows from coprimality of s+r and s after clearing denominators. For the branch proof, one need not assume the displacement quotient is literally a smooth function of h²: center at the parameter-dependent fixed point, choose s=ρ²−1, and solve (P_s²(h)−h)/h=0 for s as a function of h. Its expansion is s=−A h²+O(h³), or s=−C h⁴+O(h⁵) at degeneracy, and it is strictly monotone on each side sufficiently close to 0. This gives two points paired by P_s and the asserted side and stability by differentiating the quotient. The generic repelling escape law follows from reciprocal-square decrements tending to 2A, with only a bounded number of iterates beyond any fixed smaller cutoff. This is local to the specified itinerary and exact recurrence, not a result for a physical flow or all orbits. The frozen replay is verify.py, inspected but not executed; its symbolic and numeric checks are not the universal proof.

## originality

PASS

The return construction, cubic sign information, and general mechanism of a quintic flip are prior. The supported distinct contribution is the exact negative fifth-order coefficient on the unique real cancellation locus for each finite M, its sharp model-specific critical law, and exclusion of every rational exponent on that locus. No inspected source covers that combination or directly implies the fifth-order computation from its stated result.

## value

PASS

The exact sign and first surviving coefficient resolve a natural boundary left open by the cubic diagnostic for every finite itinerary length, determine the attraction and sharp relaxation rate there, and establish that the boundary is never attained within the original rational family. The value is in this classification, not in claiming a generic fourth-root law or a physical prediction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
