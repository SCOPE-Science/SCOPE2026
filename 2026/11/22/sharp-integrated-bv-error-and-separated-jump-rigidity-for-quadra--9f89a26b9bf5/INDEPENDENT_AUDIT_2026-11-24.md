# Independent mathematical audit

## correctness

PASS

For canonical BV data the identity f(x)=c+Df((0,x]) holds, with the stated left trace at 1. Finite summation at the Greville sites and Fubini give the residual as an integral of step residuals, and taking absolute values reduces the norm to single jumps. This argument does not require the variation-norm convergence mentioned in RESULT.md line 28: a diffuse derivative is not a Bochner integral of the unit atoms in the variation norm. Differentiating the quadratic B-spline tail telescopes to 2 N_{j,1}/(t_{j+2}−t_j). For every j=2,…,n (including n=2) this is a triangular hat divided by h; integrating it gives the frozen two-piece quadratic. At the midpoint of its support the step error is h/3. As the step moves by v h, the derivative in v is h(2v−v|v|), so the error is h(1/3+v²−|v|³/3). On the half-open Greville cell, v is in (−1/2,1/2] and only 1/2 attains 13h/24. The left boundary tail is 1−(1−x/h)² on its active cell [0,h]; the error is at most h/3 because −s+2s²/h≤0 for s≤h/2. Reflection gives the other boundary bound away from the already-assigned knot s=xi_n. Equality requires the entire variation measure to be on the sharp sites. Nonconsecutive indices have essentially disjoint residual supports; consecutive supports overlap across xi_j, where one residual reverses sign and the other does not, so any nonzero signed pair forces strict triangle loss. Linear interpolation gives a ramp error h[w²+(1−w)²]/2 for fractional jump location w, yielding the claimed comparison including attainment at interior knots. The Python checker was read, not run: its count 1710 includes 1500 submaximal off-node tests plus 210 maximizing-node checks, rather than 1710 strict tests as described in the prose. This labeling discrepancy does not affect the proof.

## originality

PASS

Closest inspected exact results address a different norm or operator, including a same-day spectrum theorem for the very same Schoenberg operator. No inspected result supplies the sharp integrated defect together with the unrestricted signed nonadjacent-jump characterization.

## value

PASS

This is the natural integrated worst-case error budget for replacing discontinuous sampled data by a positive C1 quadratic reconstruction. The exact increase over the linear interpolant is 1/12 at the same mesh. The complete signed equality law distinguishes jump separation from amplitude or sign and works even in the smallest clamped meshes, giving more than an isolated exact calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
