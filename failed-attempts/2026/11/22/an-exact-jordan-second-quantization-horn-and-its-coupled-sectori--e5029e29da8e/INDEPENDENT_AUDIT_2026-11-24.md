# Independent mathematical audit

## correctness

PASS

Nilpotence gives Q=e^(−az)(I+czN). Trace and determinant of Q*Q yield singular values e^(−at±arsinh(c|z|/2)). The nth symmetric power has top norm q^n, hence boundedness iff q≤1, with vacuum norm one; tensorized SVD supplies the product over all nonnegative mode counts. At q=1 the top vectors in different sectors prevent compactness. On q<1 finite-sector truncations converge locally uniformly in operator norm, proving holomorphy, and any open continuation agreeing on real time must agree with the entire finite-sector matrix elements. Strict contractions at t>0 and density of finite-particle vectors give strong continuity at the real origin. Rays near zero yield c≤2a cos θ for boundedness on a ray, with equality allowed. For the uniform joint limit, set D=(1−q²)(1−r²) on the real axis. Exact algebra gives D=e^(−2at)(4sinh²(at)−c²t²)=c²e^(−2at)b². Under c=2a(1−δ), the first bracket is 8a²δt²+4a⁴t⁴/3+O(δ²t²+t⁶); divided by the positive sum of leading terms the error vanishes uniformly. Since q,r→1, each (1−s^p)/(1−s²)→p/2 uniformly here, recovering both crossover constants and the fixed-c orders. Finally the triangular blocks have trace (n+1)e^(−ant). The numerical diagnostics were inspected only; the quantifiers are established by these exact arguments.

## originality

FAIL

A distinct earlier SCOPE record explicitly proves the same real-time symmetric Fock singular-value and all-p Schatten formulas up to a scalar, as well as the corresponding sharp Hilbert–Schmidt edge crossover. The stronger prior determinant identity and boundary expansion already imply the uniform all-path result; the new presentation's complex horn and its matching width are mechanical consequences, not evidence of separately established originality. Specifically, specialize that determinant to a=b and κ=c. For complex time the same triangular exponential has off-diagonal factor cz in place of ct and a unimodular scalar phase; in its two-by-two Gram trace, c²t² is simply replaced by c²|z|². Thus det(I−Q*Q)=e^(−2at)[4sinh²(at)−c²|z|²]. The known contraction criterion, with q r=e^(−2at), gives the exact horn. The horn-width identity b²=e^(2at)D(t,c)/c² and the universal p/2 factor at singular values tending to one transfer the already proved two-scale determinant asymptotics to both quantities, including paths with δ/t² unbounded. The ray angle follows by taking the tangent at zero, and the nonperiodicity follows from the sole boundary point at t=0. The earlier record is not asserted to print the horn or its angle verbatim. This is a direct-coverage/implication finding, not a verdict based on unavailable literature.

## value

FAIL

The Fock example is natural and the formulas are correct, but the proposed independent scientific gain is the coupled crossover or sharp complex-time diagram. The crossover reexpresses the already known real-time rank-one edge invariant, and the diagram follows from the standard boundedness criterion and the same 2×2 determinant with t² replaced by |z|². The angle and absence of periods add direct consequences of that inequality, not a further mechanism. No independently valuable new mathematical remainder is established in this record; this can serve as an illustration of the covered result, not as a new validated finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
