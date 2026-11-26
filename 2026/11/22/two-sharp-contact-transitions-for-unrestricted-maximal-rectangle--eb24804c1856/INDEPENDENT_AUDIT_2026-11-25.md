# Independent mathematical audit

## correctness

PASS

For half-sides a≥b and center c, the vertical half-extent |u_y|+|v_y| is ≥b, and the maximum squared vertex norm is at least |c|²+a²+b²+2b|c| by the orthonormal component inequality. Hence a same-area feasible horizontal rectangle can be centered if h+b≤0, and can be placed with bottom h and top h+2b otherwise: the vertex bound then gives a²+(h+2b)²≤1 and h+2b>|h|. This proves the needed unrestricted reduction for every orientation and translation. With t the largest absolute endpoint height, the sharp area envelope is 2 sqrt(1−t²) min(2t,t−h). The interior optima of its two smooth branches are t=1/sqrt(2) and t=q; the second derivative test is not needed to select regimes because the branch derivatives change sign once and the second branch derivative at t=−h has sign 1−3h². This yields the three branches and the two transitions. Equality in the vertex bound plus the cutting constraint forces vertical half-extent b when h>−1/sqrt(2); in the centered comparison case use a²+b²=1, c=0 and b=−h. Thus the short side is vertical and the optimizer unique after the first threshold, including at the second. Before the first, equality of the disk bound gives exactly centered inscribed squares that pass the cut; at the first only the aligned square fits. Differentiation gives the stated one-sided second derivatives (on the last branch M′=−2 sqrt(1−q²), q′=q/(4q−h)); expansion q=1−(1−h)/3+O((1−h)²) and the cap-area integral yield the stated constants. Read VERIFICATION.md and checker.py: finite orientation samples, grid and quotients are diagnostic, not an unrestricted proof. Did not execute the uploaded script.

## originality

PASS

The strongest inspected theorem for axially symmetric sets applies but does not imply cut-parallel orientation, its equality cases, or the two exact contact transitions. The indexed exact match is this same record. No distinct covering statement was found in the compared sources; priority remains best-of-knowledge.

## value

PASS

For a classical curved family, the key obstruction is the free orientation, not finding a stationary height under a chosen axis. The same-area comparison resolves that obstruction and yields uniqueness and distinct contact thresholds as well as differentiability and thin-cap utilization for the actual unrestricted optimum. The result is more than an isolated semicircle value or a box-finding algorithm.

The dated certificate retains the supplied scientific assessment, sources and limitations.
