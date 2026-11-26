# Independent mathematical audit

## correctness

PASS

For the real arithmetic-mean-zero input space and unrestricted Euclidean output, the zero Fourier block contributes squared gain g0²=T−1 and each nonzero block has Gram trace T and determinant |(1−a)(1−b)−ab exp(iθ)|². In fact g0²<T/2≤λmax of every nonzero Gram block, so the zero block never wins. The top eigenvalue grows with cos θ, maximizing at 2π/m, realized by real data using a conjugate pair or the real Nyquist block. Since T<2, the smaller eigenvalue is strictly below 1; det(I−B*B)=4ab(1−a)(1−b)sin²(θ/2)−(a−b)² decides all three signs of the gain defect. The first expanding integer follows from the strict inequality, including the equality and endpoint cases d=1 and d>1. The example crosses between sin(π/7)>5/12>sin(π/8). Stationarity and Jensen establish the weighted contraction, a different assertion. Reviewed the attached checker and its finite scope without executing it. 'Positive' refers to the specified edges and self-loops, not all matrix entries.

## originality

FAIL

The cited primary paper already establishes an exact norm theorem on the applicable general class, not merely a transform heuristic. The arithmetic-mean restriction is encoded exactly by PΠ where Π is orthogonal projection onto the input space. PΠ commutes with the two-site shift and is therefore itself in the paper's two-periodic circular-kernel class. Its one changed block is dominated, and evaluating the generic norm by the quadratic eigenvalue formula and monotonicity in cosine gives the entire proposed threshold. This is a direct specialization even though the printed paper does not state these parameters explicitly. The nearby Resultary records are distinct and are not the basis for the failure.

## value

FAIL

A one-step noise threshold for unweighted mean-zero data is a legitimate diagnostic, and the 16-site example illustrates the difference between weighted and unweighted stability. Here the exact diagnostic is obtained by projecting onto the input subspace inside a known exact norm theorem, taking the eigenvalues of a 2×2 Gram matrix and comparing one monotone scalar expression. The explicit cutoff is mechanically implied, and no independently valuable nonroutine remainder is established.

The dated certificate retains the supplied scientific assessment, sources and limitations.
