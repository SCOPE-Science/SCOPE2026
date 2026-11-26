# Independent mathematical audit

## correctness

PASS

On the event of a reset before h, the terminal temperature depends only on the independent Poisson increments after time zero; conditioning gives C(h)=exp(-rh)Cov(f(A),f(A+h)) with A exponential of rate r. Integrating against the two gamma densities uses the same age A, and the difference r/(r+u+v)-r²/((r+u)(r+v)) gives the claimed strictly positive kernel. Its quotient by v is u/(r+u)² times (1+v/(r+u))^(-1)(1+v/r)^(-1), giving a uniform relative O(v) bound at the edge. The gamma tail dominates all rate moments. Laplace integration of the edge term gives the factor Γ(p+1)/Γ(p)=p; the ratio of first excess-rate moment to mass yields (p+1)/h+O(h^(-2)). The variance under the tilted density proves strict log-convexity and monotonicity of the log decay rate. With probability rh+O(h²) a reset makes the squared temperature increment (T0-f(A))²+O(h); on no reset the square is O(h²) by bounded f'. Stationarity relates the squared increment to 2(C(0)-C(h)), proving the jump formula. Dominated convergence and strict pointwise decrease in c for positive ages give the exact mean-based inversion.

## originality

FAIL

The core claim is not established as distinct from a separate published catalogue record. Its exact spectrum, edge coefficient, sharp tail, strict log-rate decrease, rate correction and recovery of r and p match that record under a parameter rename. The matching record is indexed November 8, later than the November 2 source path; this identifies equivalent coverage, not earlier priority, authorship, or provenance. The remaining jump identity and mean inversion are routine consequences and do not supply a distinct scientific contribution sufficient to pass the frozen joint finding.

## value

PASS

As mathematics, the full theorem connects an explicit positive covariance measure, a sharp edge response and identification of the cooling exponent. It quantifies a different lag exponent from the deterministic cooling exponent and gives the leading coefficient, beyond a rate bound. This value does not make the two routine additions independently sufficient for a repaired claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
