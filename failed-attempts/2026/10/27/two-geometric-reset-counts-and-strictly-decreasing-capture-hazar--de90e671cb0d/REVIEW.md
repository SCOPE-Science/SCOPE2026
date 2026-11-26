# Independent mathematical audit

## correctness

PASS

The one-attempt kernel subtracts from the unrestricted gate transition law at the exponential clock the absorption-first event; the gate is open at absorption, and the residual independent clock is exponential, giving K=P-f e_1^T P. The two decaying generator modes and reflecting/absorbing boundary conditions give the displayed f_0,f_1 and 0<f_0<f_1<1. All entries of K are positive (there are surviving trajectories with either gate end state); the row sums are below one. Writing F=bar f, tr K=1+t-(1-t)F-t f_1 and det K=t(1-f_1). Thus det(I-K)=(1-t)F and det((1-F)I-K)=-pt(f_1-f_0)F. The positive determinant and trace and strict negative characteristic value at s=1-F place two distinct roots in (0,1) on either side of s. Strong Markov at position resets and the two initial tail values give exactly the positive two-geometric mixture. The strict identity S_n S_(n+2)-S_(n+1)^2=w_1w_2(lambda_1 lambda_2)^n(lambda_1-lambda_2)^2 proves the hazard ordering, and the dominant root gives the limit. The tail generating function gives m=(s-det K)/det(I-K). Total variance gives excess -2 det(sI-K)/det(I-K)^2, exactly the stated positive expression. The independent algebra check covers these quantities; the supplied verify.py and recorded verification were inspected, not executed. No claim about greater dispersion under an unspecified ordering or arbitrary initial gate laws is needed.

## originality

FAIL

A distinct indexed record has the same model, scope, transition kernel, exact mixture, strict hazard decrease and strict variance excess. Its characteristic identity is algebraically identical; the frozen excess in primitive parameters follows by immediate cancellation and is not a distinct surviving theorem. The 2026/11/8 catalogue path is later than the frozen 2026/10/27 path, but path dates do not establish priority or explain the relationship; this is a verdict on verified duplicate scientific coverage, not attribution or a claim that the other result appeared first. The older primary capture-time literature is not the source of the exact structural overlap.

## value

FAIL

The two-geometric law and its diagnostic hazard are intrinsically useful for modeling persistent gate memory, but they are already present in the exact overlapping result. In this submission the only apparent remainder is a routine evaluation of the same determinant, mean and excess variance in the given parameters. That substitution does not justify a separate exact-invariant claim or a repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
