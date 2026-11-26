# Independent mathematical audit

## correctness

FAIL

The stated ordered boundary (RESULT.md line 30) is not a closed parametrized path: the first edge ends at b(0), so the next arc has to run from b(0) to b(2m), not in reverse. For example r=k has b'(theta)=(k-1/2)v_theta with k<1/2 and distinct endpoints. The printed Green identity at lines 39–48 uses the forward orientation of both arcs: det(a,a')+det(b,b')=2r c·u+1/2 and the two edge determinants sum to sin(2m)/2. With that local correction, closure, support-function convexity, the complementary width cos(z)+cot(m)sin(z), reducedness by singleton active faces, and the area/strict-concavity/dual-certificate proof all check. The resulting theorem is not disproved. The numerical bracket was independently reproduced by exact rational Taylor bounds and sine bisection, using /workspace/branches/8fadda2c-4e70-49ad-9f28-fe40bf3a3f7e/repro_fixed_m.py (not the frozen script). It brackets the formula, not the universal optimum by itself. The orientation correction alone cannot leave a distinct surviving claim given the indexed coverage below.

## originality

FAIL

The distinct 2026/11/1 indexed paired-arc theorem covers the same construction, optimizer, area formula and the stated Poincaré stability bound, in a larger signed and nonsymmetry-restricted feasible class; it additionally optimizes the angle. This is demonstrable current coverage, not a finding that the November record precedes the October frozen record or that either copied the other. The earlier Kominers construction and two affine-cosine optimizations do not by themselves imply the infinite-dimensional optimizer.

## value

PASS

The fixed-angle optimizer and area gap resolve a natural variational question over measurable profiles in a concrete reduced-body construction; the discontinuous optimizer explains why smooth cosine tuning misses achievable area. This structural value is separate from the failure of distinctness and from any claim of a current best unrestricted lower bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
