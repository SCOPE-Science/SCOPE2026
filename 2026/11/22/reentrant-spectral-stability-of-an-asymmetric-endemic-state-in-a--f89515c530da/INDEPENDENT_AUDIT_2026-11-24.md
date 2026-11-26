# Independent mathematical audit

## correctness

PASS

This PASS is for the repaired finding, not the frozen assertion of an exact if-and-only-if nonlinear local asymptotic stability criterion. The frozen wording was not established on the imaginary-pair locus; Routh–Hurwitz and linearization cannot decide nonlinear stability there. The repaired RESULT.md states the exact Hurwitz criterion, exponential stability or instability for the two strict signs, and explicitly withholds a nonlinear verdict at equality. On the interior of the simplex, the reduced variables are a valid chart; stationarity gives y=1/R, I_B=z I_A, I_A=u/[R(1+z)], and p=R^2u/[z(1+z)], with the full state positive and normalized. Independent differentiation and the characteristic coefficients give a1=-tr J>0, a3=-det J>0, and a1*a2-a3=u P_z/[z^2(1+z)^3]. At H=0 the cubic factors, a2=a3/a1>0, and the roots are distinct: -a1 and ±i sqrt(a2). A nonzero imaginary root conversely forces H=0, and a zero eigenvalue is excluded by a3>0, so H<0 implies a right-half-plane root. With C(z)>0, there are exactly two distinct positive zeros of P_z if and only if A>0, B<0 and B^2>4AC; each has nonzero H' at fixed z. Taking the real part of -partial_u p_char / partial_lambda p_char at i sqrt(a2) gives -H'/[2(a1^2+a2)], verifying transversality for both simple roots. At z=3/8 the independent rational coefficients yield the stated quadratic, positive roots and sign reversal. Here a2 is positive for all u>0, so positive real eigenvalues are impossible and the unstable eigenvalues are a complex pair. Replay `python /workspace/independent_checks.py 2` independently reconstructs the Jacobian characteristic coefficients, exact determinant combination and threshold decimals.

## originality

PASS

For the repaired spectral claim the source's asymmetric branch, sign-equivalent matrix inequality, and prior numerical stability maps are credited. The distinct mathematical contribution is resolution of the source's remaining sign condition into a fixed-ratio quadratic, an exact condition for two positive spectral crossings, and a rigorously transversal algebraic example. The evidence does not support claiming a new branch, a new Routh–Hurwitz criterion, or the first observation of oscillatory instability in SIS–opinion models.

## value

PASS

The repaired spectral theorem resolves a specific untreated sign question of the source model and proves that an admissible fixed-ratio family can have a finite open interval of oscillatory instability with stable open intervals on both sides. Exact boundaries and nonzero crossing slopes give more than a plotted example. The all-ratio two-root condition makes z=3/8 a witness for a structural phenomenon rather than an arbitrary isolated numerical slice. The narrowing at equality preserves this value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
