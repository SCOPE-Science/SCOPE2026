# Independent mathematical audit

## correctness

PASS

For the exact nonovershooting Landweber iterate with one reused isotropic noise vector, diagonalizing A^T A yields sigma^2 omega f_K(omega lambda_i) with f_K(t)=[1-(1-t)^K]^2/t and f_K(0)=0. The derivative sign converts to 2K-sum_{j=0}^{K-1}u^{-j}, giving a unique interior peak for K>=2 (K=1 monotone). For ordered t<=s, unimodality and f_K(1)=1 imply f_K(t)<=M_K f_K(s). Selecting an omitted maximizer and the r retained modes supplies r+1 covariance eigenvalues >= error_B/M_K, so the (r+1)-st eigenvalue gives sharp norm quasi-optimality. The r+1 diagonal witness with r normal eigenvalues one and one t_K gives exact equality. K=1, null normal modes, ties, and optimal-error-zero are handled. The scaling bound f_K(t)/K<=min(Kt,1/(Kt)) and compact uniform limit prove Kt_K->tau_* and M_K/K->(1-e^-tau_*)^2/tau_*, tau_*>0 satisfying e^tau=1+2tau. Independent rational check K=2=32/27, numerical tau coefficient 0.407264377589 and 250 spectral samples at each of six K corroborated the statements; samples alone are not proofs.

## originality

PASS

Best-of-knowledge original sharp spectral-norm rank-competitiveness M_K, sharp all-rank diagonal witness and linear-K coefficient. The exact filter and its unimodality, as well as migration of optimal covariance ranks, have ALREADY been proved in the October 25 published single-crossing covariance spectrum theorem and are not independently new here. Abhishek–Holman supplies the same propagated covariance and low-rank normal-operator surrogate but does not derive its sharp spectral-rank competitive factor. Distinguish residual-corrected UQ, trace-retention loss and reconstruction error. Priority for a generic nonmonotone filter inequality remains a residual risk.

## value

PASS

Sharp, dimension- and rank-uniform quantitative comparison of two naturally competing covariance-compression subspace choices in early-stopped inversion, with explicit extremizers and iteration-dependent deterioration. The competitive factor is a motivated natural invariant of the Landweber spectral filter, not merely rederiving the known filter or a sampled instance; useful for interpreting and designing truncation choices while leaving residual-corrected UQ outside scope.

The dated certificate retains the supplied scientific assessment, sources and limitations.
