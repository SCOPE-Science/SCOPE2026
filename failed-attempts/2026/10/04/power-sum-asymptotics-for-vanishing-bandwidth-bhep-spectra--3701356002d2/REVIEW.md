# Independent mathematical audit

## correctness

PASS

The Gaussian Mercer spectrum gives the exact trace of every power of B. With R=B-A positive trace class, its trace is order beta^{-d}, and both A and B have operator norm order beta^{-d}; the noncommutative telescoping identity therefore gives an order beta^{-dr} trace-power error. The weighted chi-square cumulant formula then gives the constants, including excess kurtosis 12 beta^{-d}. Applying Berry–Esseen to finite truncations and passing by L2 convergence gives the stated rate. These steps are mathematically sound.

## originality

FAIL

The 2026 spectral paper already gives every premise needed for the assigned theorem and in Section 6 proves the same beta-to-infinity Gaussian limit: it diagonalizes the Gaussian operator with geometric eigenvalues, writes the BHEP operator as a positive finite-rank subtraction, gives the exact trace, proves the variance asymptotic and bounds the largest eigenvalue. The assigned all-r power sum follows from these displayed facts by the standard noncommutative telescoping identity and trace-ideal norm inequality; its cumulants are then the standard weighted-chi-square formula, and the Berry–Esseen rate is obtained by replacing the paper's Lyapunov estimate with the classical Berry–Esseen inequality. This is a quantitative corollary of the same published proof architecture rather than a new spectral mechanism.

## value

FAIL

The unified coefficient hierarchy is tidy, but it is obtained from the source's exact Mercer spectrum, positive finite-rank correction and existing vanishing-bandwidth CLT by standard trace-norm, cumulant and Berry–Esseen estimates. Under the common bar this is a routine quantitative extraction rather than an independently substantive result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
