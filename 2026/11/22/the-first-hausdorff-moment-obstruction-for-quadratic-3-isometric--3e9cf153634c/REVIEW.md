# Independent mathematical audit

## correctness

PASS

The shift orbit norms are P(q+n)/P(q), so their third differences vanish and their second differences are positive; the bounded contractive Cauchy dual has moments 1/P(n) at the initial vector by telescoping. Factoring P and taking alternating differences of each reciprocal linear term gives k! divided by the product of the k+1 consecutive shifted factors. The conjugate products give the claimed positive-prefactor sine with the displayed sign. At fixed order the phase is largest at start zero. It diverges in order by harmonic comparison, and the first strict crossing of pi overshoots by at most the last summand, which is less than pi/2. Equality at pi therefore gives zero, not a negative witness, and all earlier orders are nonnegative at every start. At fixed u, expand arctangent uniformly with remainder bounded by a constant times v^5 times the convergent sum of (u+j)^(-5). The crossing and arctangent <= argument force K >= exp(pi/v-O_u(1)), and the overshoot divided by v is <= 1/(u+K). Using the finite-sum digamma identity and the O_u(K^(-2)) cubic-tail error gives log K = pi/v + psi(u) + v^2 zeta(3,u)/3 + O_u(v^4). Independent exact rational checks of the differences at (u,v)=(1,1) and orders 15 and 16 gave positive and negative signs respectively, corroborating the example K=16. The proof, not the numerical examples or the read-only bundled verifier, supplies the general result. It does not locate first failures of other positivity tests or give an asymptotic uniform in u.

## originality

PASS

Best-of-knowledge pass for the minimum scalar witness order across all starts and the sharp fixed-u onset law. The shift construction, qualitative discriminant criterion, conjugate-pole representation and the idea of concrete finite negative witnesses in related families have prior coverage. The review does not credit those ingredients as new.

## value

PASS

The known non-Hausdorff criterion gives no size for a certifying scalar test. The exact minimum across all starting indices proves that passing finitely many tests can mask failure up to an exponentially large order, and it identifies the exponential scale with a parameter-dependent prefactor and correction. This is an obstruction to detecting non-subnormality by this specific finite-difference hierarchy, not a claim about every possible test. The all-parameter threshold and near-boundary quantification have substance beyond the standard difference identity or isolated examples.

The dated certificate retains the supplied scientific assessment, sources and limitations.
