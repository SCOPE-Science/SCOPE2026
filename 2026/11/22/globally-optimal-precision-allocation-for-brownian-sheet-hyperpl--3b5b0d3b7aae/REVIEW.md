# Independent mathematical audit

## correctness

PASS

Tensor integration gives Var(J)=3^(-d), Cov(J,A_j)=3^(-(d-1))c(x_j), and Cov(A_j,A_k)=3^(-(d-2))c(x_j)c(x_k) for distinct axes. Projecting each slice onto J cancels all off-diagonal residual covariances; joint Gaussianity gives independent residuals and additive scalar information. At p>0 the derivative in x has sign 12(1-x)-ux(3x-2), u=p/3^(d-2); x=0 conveys no information and x=1 has negative derivative, so the single interior root is the unique maximum. At that root the optimized information derivative increases strictly with x (A<0 and Q>0 in the stated derivative factorization), and x decreases strictly with u. Continuity at zero extends strict concavity to the closed precision simplex. Strict Jensen therefore excludes zero-precision allocations, establishes the unique uniform split, and then the location root is forced on every axis. Substitution gives the asserted risk, crossover and fixed-d noiseless limit: at x=2/3 the scaled channel information is 72, hence total limiting precision 3^d(8d+1).

## originality

PASS

The supported distinction is the specific tensor-slice precision and location law, not Gaussian conditioning, integral sensors or the familiar coordinate location 2/3 by itself. The closest indexed Brownian-sheet record optimizes one noisy point value, and the closest external integral-sensor work does not solve this target/budget/geometry. Neither yields the independent-channel factorization with optimized strict concavity as an existing design theorem.

## value

PASS

The exact allocation is useful when measurement precision, rather than the number of slices, is the resource. Residual independence makes this an unusually tractable nontrivial joint-design problem, and the location scaling identifies the budget needed to prevent high-dimensional measurements from drifting toward the outer faces. The conclusions about boundaries, symmetry and attainable risk add information beyond generic covariance evaluation or a numerical design.

The dated certificate retains the supplied scientific assessment, sources and limitations.
