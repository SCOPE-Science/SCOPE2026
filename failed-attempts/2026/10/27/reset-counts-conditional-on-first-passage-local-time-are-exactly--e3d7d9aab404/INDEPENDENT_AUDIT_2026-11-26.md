# Independent mathematical audit

## correctness

PASS

For one attempt, encode absorption and the independent exponential interruption as two distinct absorbing marks. Let Λ be the occupation-density local time at the common starting/reset point a before either terminal event. On {Λ>u}, the inverse local time at level u is before termination, has local time u by continuity, and is at a because dL is supported at a. By strong Markov and exponential-clock memorylessness, P(Λ>u+v,J=j)=P(Λ>u)P(Λ>v,J=j). The unmarked survival is exponential (the positive finite mean EΛ=G excludes a zero or infinite lifetime and forces P(Λ>0)=1). Setting v=0 proves independence of the terminal mark. EΛ=G follows by independent discounting of dL in the stated Lebesgue occupation normalization. The iid cycles then give P(N=n)=q(1-q)^n and L|N=n a sum of n+1 exponentials of mean G. Inverting this mixture gives exactly the claimed density, no atom at zero, L exponential of mean G/q, and the Poisson conditional distribution. Cov(N,L)=(1-q)Var(L)/G yields the stated correlation. The killed Brownian image Green kernel and bounded hitting transform give the displayed q, G and rate. No assertion here extends to nonexponential clocks or resetting to a site other than the local-time site.

## originality

FAIL

The claim is correct but is a direct rank-one specialization of an earlier marked occupation identity plus ordinary renewal. Fitzsimmons–Pitman (1999), §3.1 Eq. (21), permits an arbitrary future-path functional under dA. With A equal to local time at a in the process killed at absorption or interruption and the terminal cause encoded in the path, support at a makes the operator scalar at a. Applying Eq. (21) with future residual local time to power m times the terminal-mark indicator gives E_a[Λ^(m+1);J=j]=(m+1)G E_a[Λ^m;J=j]; the factor m+1 is the continuous additive-functional power identity. With m=0 as the initial mark probability this gives all marked exponential moments (moment determinacy follows from the exponential moment series for arguments less than 1/G). The remaining laws follow from iid attempts and Gamma–Poisson algebra. This is verified implication from an earlier general result, not a claim that its authors expressly discussed resetting. The separate later indexed record is equivalent coverage, not evidence for earlier priority.

## value

FAIL

The count prediction from local time is interpretable and the choice of a as the observation site is natural. However, the exact invariant is mechanically implied by the old marked occupation identity at the single support point and routine renewal; the additional correlation and Brownian parameters are direct algebra. The frozen claim does not establish a further nonroutine invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
