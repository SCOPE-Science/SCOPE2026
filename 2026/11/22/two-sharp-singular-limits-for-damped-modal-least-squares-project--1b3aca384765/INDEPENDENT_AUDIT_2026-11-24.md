# Independent mathematical audit

## correctness

PASS

Scaling t by a gives damping one. Laplace integration in the basis e^(−t)cos(rt), e^(−t)sin(rt)/r yields inverse Gram 4[[1,−1],[−1,2+r²]]. In the unscaled basis the trace is 1/2 and determinant r²/[16(1+r²)], so its two eigenvalues are (1±1/sqrt(1+r²))/4, giving the asserted condition number. The real operator norm is the supremum of absolute row integrals: the sign input attains any chosen row evaluation, and output continuity identifies even the limiting endpoint value with a lower bound for the essential supremum. The endpoint row is 4/r times the derivative of e^(−y)sin(ry); the extrema are at (arctan r+kπ)/r, of absolute heights r exp(−(arctan r+kπ)/r)/sqrt(1+r²). Total variation doubles the geometric sum. For r≤1, Taylor bounds |cos(rz)−1|≤r²z²/2, |sin(rz)/r−z|≤r²z³/6 and |sin(rz)/r|≤z give the kernel error bounded by r²e^(−x−y) times a fixed polynomial, uniformly integrable in y and bounded in x after integration. The limiting row is 4e^(−x)J(x), J the absolute-affine exponential integral. J is convex, with J(0)=2/e and J(1/2)=1/2, so on [0,1/2] it does not exceed 2/e. On [1/2,1], J=x, and for x≥1 J≤3x−2, making the row ≤12e^(−5/3)<8/e there. Thus the exact confluent norm is 8/e and the uniform error is O(r²); at b=0 the rank-one kernel gives 2. At large r the kernel is 4e^(−x−y)cos(r(x−y)) with a row error O(e^(−x)/r). Since |cos|−2/π has a bounded periodic primitive, integration by parts against e^(−y) gives O(1/r) uniformly in the phase. This yields an upper bound for every row and the matching lower bound at zero. These are global limits; no finite-r endpoint rigidity is established or needed. projection_checks.py was read, not run.

## originality

PASS

Credit the 8/e and rank-one discontinuity as shared with real two-rate coalescence, not as uniquely oscillatory discoveries. Pass the frequency-dependent oscillatory endpoint law and the sharp large-frequency global norm with uniform error for this half-line projector, together with its rigorously controlled confluent limit. The directly checked real-rate and Fourier comparisons do not imply the changing kernel sign pattern and oscillatory endpoint law, or the required half-line global bounds. This is best-of-knowledge, not exhaustive priority.

## value

PASS

Sharp global operator norms measure worst-case noise amplification in least squares, not merely how badly its particular coordinates are conditioned. The sharp oscillatory endpoint amplification at finite r, bounded confluent projector despite a diverging Gram condition number, and controlled high-frequency norm distinguish three practically and mathematically different statements. The scope is naturally rank two, with no assertion of finite-frequency global optimization or of a general spectral theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
