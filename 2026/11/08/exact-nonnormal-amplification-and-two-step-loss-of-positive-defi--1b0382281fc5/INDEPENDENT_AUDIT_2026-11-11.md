# Independent mathematical audit

## correctness

PASS

For SPD S=[[K,t sqrt(K)],[t sqrt(K),1]] and Z=diag(K,1), the exact frozen L_Z^{-1}(A-X^2) updates give X1=S+diag(t^2/2,Kt^2/2) and X2 diagonals K-t^4/(8K),1-K^2t^4/8 and offdiagonal t sqrt(K)(1-t^2/2). The second diagonal is negative for K>2 sqrt(2)/t^2 while first stays positive; X2 indefinite. Direct differentiation yields eigenvalues ±t,0,0 and Frobenius operator norm t sqrt((K+K^-1)/2); X1 error ratio t sqrt(K+K^-1)/(2sqrt(2)). Hence relative initial error tends zero but absolute error amplification unbounded. Checked exact rational K=16,t=1/2 witness and noncommuting conditions.

## originality

PASS

Gao–Kressner–Shao 2026 use the same fixed-Jacobian Sylvester update but impose a small absolute error for their sufficient local convergence estimates, which the exhibited ill-conditioned family violates uniformly. The computed nonnormal transient and positive-definite-cone exit do not contradict or follow from that sufficient result. Higham and Sra methods differ. No covering exact published family was found in Resultary. Full initiating primary text not completely available; priority remains qualified.

## value

PASS

Concrete counterexample to a tempting but false inference that spectral local stability, arbitrarily small relative Frobenius error and uniform Loewner-equivalence guarantee transient norm safety or positivity of exact frozen-Sylvester refinement. Exact K,t cone-exit threshold and Jacobian norm make the limitation useful for stability/safeguard analyses.

The dated certificate retains the supplied scientific assessment, sources and limitations.
