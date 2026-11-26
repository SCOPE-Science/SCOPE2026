# Independent mathematical audit

## correctness

PASS

Reconstructed the orbit in RESULT.md lines 47–111 directly from the norming functional: its real center is δH, real phase radius C, and imaginary signed radius S. Compactness handles the zero-coordinate cases, and p=2 has S identically zero. The derivative of |S| on (0,1) has the stated numerator with constant sign factor sgn(p−2); differentiating that numerator gives a strictly one-signed derivative, since 2t^p−(p−2)−pt² has the sign of 2−p there. The endpoint signs and this strict derivative give a unique nondegenerate maximum up to reciprocal symmetry. The top witnesses have real parts ±δH(τ_p), so for nonzero split their missing midpoint proves strict axial loss and nonconvexity. Solving the real-part constraint gives the stated scalar objective; choosing t close to 1 but not equal proves positivity. The squared split is a smooth perturbation near the strict maximum; stationarity gives O_p(δ²) displacement, and the unperturbed deficit away from those neighborhoods excludes all other maximizers. Taylor expansion gives the quadratic coefficient with O_p(δ⁴) remainder. For the large-split limit, r=H/C vanishes only at 1 and diverges in magnitude at the two ends. It is locally invertible with derivative −p/2. In the feasible coordinate y=|δ|r, uniformly on [−1,1] the imaginary radius is |p−2||y|/(p|δ|)+O_p(|δ|^(−2)); multiplying by √(1−y²) and maximizing gives the claimed factor 1/2. At p=4 the squared objective is u(1−(1+4δ²)u)/(1+u)²; its derivative has numerator 1−(3+8δ²)u and changes sign at an interior feasible point. Its value, both modulus ratios and their phase conditions agree with the finding, also at δ=0. Read VERIFICATION.md and CHECK.py as finite diagnostics, not as proofs or certifications. The asymptotics are fixed-p and the large-split rate is for the axis height rather than its gap.

## originality

PASS

Qualitative nonconvexity for δ≠0 is already in Mandal et al., and the δ=0 quartic height belongs to the known unsplit body. The distinct supported contribution is the exact positive-split quartic axial height and extremizers, together with the fixed-p small-gap coefficient and strong-split decay. This is a best-of-current-knowledge judgment.

## value

PASS

The axial height measures a natural obstruction to convexity: two top points place the missing midpoint on the imaginary axis. The theorem quantifies how that failure opens under a small perturbation and how the height decays under large splitting. Exact quartic extremizers and the full interpolation add useful information beyond the already known qualitative obstruction and the previously known unsplit body.

The dated certificate retains the supplied scientific assessment, sources and limitations.
