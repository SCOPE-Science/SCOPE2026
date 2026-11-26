# Independent mathematical audit

## correctness

PASS

Reassessed the repeated-depth theorem in repairs/4/RESULT.md. Odd-order group-ring inversion gives the alternating sign kernel, hence its convolution powers; matching input signs in one row attains the l-infinity norm. Removing the alternating signs produces the stated antidifference and antiperiodic boundary equations. After scaling by N^{-(m-1)}, each step approximates the integral of the previous scaled profile with uniform O_m(1/N) error, and the boundary equation fixes the additive constant with the same error. This gives 2^{m-1} E_{m-1}(j/N)/(m-1)! and the absolute-value Riemann sum gives O_m(N^{m-1}) error in the norm. Euler reflection and the derivative identity give constant open-interval sign for positive even degree and exactly one midpoint sign change for odd degree; integrating via the derivative then gives A_m divided by m*2^{m-1} from the endpoint and midpoint generating functions. Exact symbolic checking verifies the low-depth recurrence, sign split and all sums, including a separate N=3 fourth-depth inversion. The character multiplier has minimum sin^m(pi/(2N)) for fixed odd N, and vanishes at frequency N/2 on even cycles. The tangent partial fractions identify the fixed-m ratio as K_m; 4/pi is only the subsequent limit of K_m.

## originality

PASS

The repaired finding is the quantitative finite odd-cycle law at repeated depths m>=2 and the exact formulas at m=2,3,4. The one-step bound and parity behavior, independently covered by the earlier midpoint sampling result, are baseline, not originality. The continuum Favard constant and 4/pi limit are known; the distinct relation is to this discrete inverse and its finite-size formulas and remainder. No inspected stronger statement subsumes the repaired claim.

## value

PASS

Repeated two-tap smoothing is a natural finite-cycle measurement operator. Its sharp worst-case uniform reconstruction error is neither the spectral error nor the power of the one-step uniform norm. Establishing the actual sharp fixed-depth law with a finite-size error order and exact norms for the first three repeated depths provides both structural and immediately usable information. The value is not the known m=1 calculation or the continuum constant itself.

The dated certificate retains the supplied scientific assessment, sources and limitations.
