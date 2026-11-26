# Independent mathematical audit

## correctness

PASS

Independently reconstructed the functional and covariance limits. For attachment bit A_k, Y_k=1−(1−A_k)Y_{k−1} takes values 0,1, so H is terminal depth. The leaf increment is A_{k−1}(1−A_k). For μ=1/(1+q), sums of the centered increments from k=3 to m are, up to uniformly bounded endpoint terms, sums of martingale differences (A_k−p)(Y_{k−1}/(1+q), q−A_{k−1}). This follows by telescoping Y_k−μ+q(Y_{k−1}−μ)=Y_{k−1}(A_k−p) and shifting the one-step leaf term q(A_{k−1}−p). The finite-state chain (Y,A) forgets initialization at the first success; its stationary moments are E Y=μ, E A=p, E(YA)=p. Thus time-averaged predictable brackets converge to the asserted Σ by the ergodic theorem; the bounded differences satisfy Lindeberg for the martingale functional CLT. Orthogonality of differences gives covariance convergence separately, with endpoint terms negligible after division by n by Cauchy–Schwarz. Summing the expectation recursion gives the asserted height mean and counting the deterministic initial A_2 gives the stated leaf mean. The determinant factors as stated, and the sign changes at the unique root of q²+q−1 on (0,1). The line-96 characterization of Isaev et al. is bibliographically inaccurate (uniform labelled trees, not uniform recursive trees), not a mathematical defect. Packaged code was inspected, not executed; the large-n moment checks use floating point, despite a code comment calling them exact.

## originality

FAIL

A distinct Resultary record for exactly this model, with labels shifted by one, gives the same covariance, determinant and golden-ratio transition, and supplies the explicit iid regenerative reward representation. The present path-level extension follows directly from those same blocks by the iid invariance principle, the renewal law and the negligible maximal incomplete block. The exact means are elementary consequences of the identical increment recursions. The later catalogue date is not evidence of chronological priority over the assigned record; this decision is about demonstrated scientific coverage, not who discovered it first.

## value

FAIL

The exact tree-specific covariance and sign transition would be informative in isolation, but are already covered. The only material difference is the process statement obtained by standard iid renewal time change with unchanged rewards and covariance. No new path statistic or tree-specific conclusion beyond that routine upgrade is established as an independently valuable remainder.

The dated certificate retains the supplied scientific assessment, sources and limitations.
