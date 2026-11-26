# Independent mathematical audit

## correctness

PASS

Polar integration gives an exponential-kernel radius /ℓ of law Gamma(d,1) and a Gaussian squared radius /[(d+1)ℓ²] of law χ²_d; both squared radii have mean d(d+1)ℓ². At ℓ=1 the ratio of radial Gaussian to radial exponential densities is the ratio of the spatial densities, with log a concave quadratic in r and maximum at d+1. Equal mass forces it to be positive somewhere. If its value at r=0 were nonnegative the density difference f_G−f_E would have exactly one positive sign change, from + to −; weighting by r² minus the squared change point would force a negative second-moment difference, a contradiction. There are exactly two positive density roots. The CDF difference rises, strictly falls, then rises to zero, and is already strictly negative at the second density root. This proves the two strict CDF orders and the unique nontrivial crossing. For the central gamma expansion, the standardized density at z is φ(z) times exp[(z³/3−z)/√n+O((1+|z|⁴)/n)] uniformly on |z|≤n^(1/12), by Stirling and Taylor expansion. Integration of the expanded density has error O(1/n), by Gaussian integrability of its polynomial remainder and exponentially small gamma and Gaussian tails outside the window. The correction integrated to 0 is φ(0)/(3√n), and replacing 0 by u/√n adds φ(0)u/√n; the argument also holds for half-integer shape. Evaluating at r=d+c uses gamma arguments d+c and d/2+c−1/2+O(1/d); the leading difference multiplied by √d is φ(0)[(1−√2)c+1/3+√2/6], whose sign on either side of its simple root brackets the unique crossover. Thus the stated constant is an additive limit, not an equality at finite d. Fresh 65-digit gamma-tail bisection at d=3,10,100,500,4000,20000 reproduces the quoted d=3 and d=100 roots and the limiting behavior; at d=20000 the offset exceeds the limit by about 9.37×10⁻⁷. Replay cd /workspace && python3 review-evidence/reproduce.py 4; output review-evidence/4.txt. The frozen SciPy checker was inspected, not executed; its finite tolerances cannot prove the strict signs or the limit.

## originality

PASS

The distinctive result is the higher-dimensional matched radial-kernel crossover with its explicit, sharp additive location limit. Neither comparison of the kernel shapes nor the Gaussian scale-mixture representation is new. The one-crossing mechanism itself is a simple consequence of broader scalar scale-mixture geometry, not a reason to claim priority for a generic crossing principle; the dimension-dependent location still needs a separate calculation.

## value

PASS

Matching the displacement moment is a natural control for comparing two canonical radial kernels. The unique radius supplies an exact benchmark for opposite ball-mass rankings, and the sharp O(1) displacement from d gives information absent from concentration at r/d≈1 or from a generic scale-mixture crossing. It is a structural mathematical benchmark, not an empirical prediction at high spatial dimension or for off-center targets.

The dated certificate retains the supplied scientific assessment, sources and limitations.
