# Independent mathematical audit

## correctness

PASS

For unit-row full-rank V the Gram G is PD, tr G=m, diagonal 1, and row sums off diagonal<=delta=(m-1)/R. Its eigenvalues lie in [1-delta,1+delta] by Gershgorin. Spectral/nuclear norm duality gives efficiency exactly m/(sqrt(lambda_max)*sum sqrt(lambda_i)); Cauchy bounds the denominator by H_m(lambda_max)=lambda_max+sqrt((m-1)lambda_max(m-lambda_max)). Its unique maximum lambda*=(m+sqrt m)/2 on [1,m] produces claimed Lambda and exact minimax. Positive equicorrelation Gram with rho=(Lambda-1)/(m-1) is full-rank, unit-diagonal, admissible and attains equality. Polar gap=max_i |sqrt(lambda_i)-1|, and signed equicorrelation matrices attain upper/lower branches or approach PD singular boundary as required. Independent eigenvalue formula calculations were performed at (m,R)=(2,1.1),(3,2),(5,2),(16,4),(256,16) and matched the expression; package verify.py was read, not merely its PASS count.

## originality

PASS

The March 2026 RMNP primary manuscript was read in full-text HTML and PDF sections: Section 3.2 and Appendix B define and empirically measure off-diagonal row ratios, Section 5 proves optimization convergence, not the sharp deterministic spectral-ball minimax under a prescribed unit-row Gram floor. Norm-constrained LMO work describes primal/dual norm steps without this constrained cross-norm frontier. A published PDNQP coherence obstruction treats a different step-initialization setting. No exact theorem in inspected sources implies the sharp Lambda saturation and signed-equicorrelation polar gap. Priority remains best-of-knowledge; a general matrix spectral extremum could give a reduction.

## value

PASS

The exact, attainable all-dimensional calibration replaces a qualitative high-row-ratio heuristic with a necessary-and-sufficient uniform condition delta=(m-1)/R->0, and reveals an m=q^2,R=q family where r_min grows but efficiency decays like q^{-1/2}. The sharply constrained diagnostic is motivated by a real matrix preconditioner, not an arbitrary tiny example. The result has deliberately limited one-step scope.

The dated certificate retains the supplied scientific assessment, sources and limitations.
