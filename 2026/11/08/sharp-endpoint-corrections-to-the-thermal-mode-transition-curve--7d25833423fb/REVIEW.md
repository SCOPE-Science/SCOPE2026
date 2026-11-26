# Independent mathematical audit

## correctness

PASS

Re-audited the endpoint-only RESULT.md. The normalizations s=D*kappa/v^2 and lambda=1/(2s) lead to the curvature integral H=-2lambda J'-J. The hypergeometric ODE gives g'= (1-a)/lambda at a zero of g=H/J, while H(0)<0 and its fixed-a large-lambda leading term is (1-a)sqrt(pi)lambda^(-3/2). At small a the endpoint-subtracted J has uniform leading term exp(-lambda)/a and the numerator of 1-m differs from its a=0 value by O(a). The sign bracket places the root near 1/2; s_c=m at that root makes lambda=1/2+O(a), allowing evaluation of the first coefficient at 1/2 with O(a^2) error. Near a=1, H_1=-2 exp(-lambda) exactly, the first perturbative gamma integral is epsilon sqrt(pi)lambda^(-3/2), and the error on [1/2,1) is uniformly O(epsilon(1+lambda)exp(-lambda/2)) by the integrable logarithmic bound. This preserves the epsilon factor needed at the exponentially small crossing. Comparing at (1±delta)L brackets the root; taking logarithms and refining gives the 3/2 coefficient, constant and O(log(L)/L) remainder. Separate endpoint-subtracted quadrature and critical moment checks passed at four shapes including a=10^-4 and 1-a=10^-16 (`python3 /workspace/audit_evidence/reproduce.py 1`). The frozen script was inspected, not run; the repair retains its verification front matter verbatim and updates the scientific notes only.

## originality

PASS

The corrected finding claims only the small-a slope of s_c and the log-log and constant correction for lambda_a near a=1, with remainder bounds. It explicitly credits the already-established boundary geometry and quartic coefficient, along with the curvature equation and the leading inverse-log behavior. No equivalent statement or covering result for the surviving increments was found in the strongest inspected sources.

## value

PASS

The narrowing retains two distinguished asymptotic regimes, set by approach to the persistent two-state limit and disappearance of the thermal transition. An explicit slope quantifies the first departure from the limiting variance; near disappearance the unbounded subleading log-log term and the fixed normalization constant refine a slowly converging leading prediction. These precise, proved corrections are useful in comparing theory and numerical phase diagrams without re-claiming the previously established mode geometry.

The dated certificate retains the supplied scientific assessment, sources and limitations.
