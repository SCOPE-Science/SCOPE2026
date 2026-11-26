# Independent mathematical audit

## correctness

PASS

The antisymmetric derivative along the diagonal is 4(1−2x)−2ε. Under x=sin²(πt) with uniform t and time evolution by doubling, the centered logarithm is g(t)=log|2cos(2πt)−ε|. Factoring it into two circle logarithms shows it lies in L², has mean zero and has cosine coefficients a_k=−2cos(kφ)/k. Orthogonality gives C_m=(1/2)Σ_k a_k a_{2^m k}, dominated by (2/2^m)Σ_k k^{−2}. Stationarity gives Var(L_n)=nC_0+2Σ_{1≤m<n}(n−m)C_m. The absolutely convergent Green–Kubo sum groups by the odd parts of the frequencies into the asserted dyadic squares. The sine double-angle identity at ε=0 and 1+2cos(2u)=(2cos u−1)(1+2cos u) at ε=1 give the stated L² coboundaries and thus uniform variance bounds. At ε=−1 the ray sums are 2 for odd multiples of 3 and −1 for other odd indices, giving 2(4π²/72+π²/8−π²/72)=π²/3. This is a variance statement, not an entire finite-time probability law. The frozen script's comment on lower bounds is not true when the inner sums are also truncated, but no proof step relies on it.

## originality

FAIL

The earlier matrix-logistic result independently gives the identical centered scalar cocycle on an overlapping interval and the identical dyadic variance theorem there, including the bounded ε=0 and positive-rate ε=−1 cases under reparameterization. Its proof is already an arbitrary-phase doubling-map argument and explicitly isolates φ=π/3 as the only other potential zero. At that phase one checks the same even/odd-orbit atoms, or the elementary three-residue cosine table, directly in the existing formula. The boundedness follows from the earlier martingale/coboundary decomposition with zero martingale term; the present elementary transfer function verifies it but does not add a distinct variance result. The broader coupling interval and changed mean do not change the stationary centered process or require a new fluctuation mechanism. A later indexed covariance theorem verifies equivalent and stronger coverage independently of these priority considerations; it is not used as evidence of earlier publication.

## value

FAIL

The plateau versus variance effect is a mathematically meaningful question, but the frozen theorem as a contribution repeats the established scalar-cocycle contrast and presents the only extra cancellation as a direct phase specialization of the established variance and coboundary analysis. A new application requiring distinct nonlinear or statistical information could be valuable; the frozen result explicitly does not address such information. No substantively new remainder of this exact claim was identified.

The dated certificate retains the supplied scientific assessment, sources and limitations.
