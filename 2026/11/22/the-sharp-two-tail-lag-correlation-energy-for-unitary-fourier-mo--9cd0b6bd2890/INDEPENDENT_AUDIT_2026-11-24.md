# Independent mathematical audit

## correctness

PASS

For each column, let A be its mass on rows 0,N-1, B on rows 1,N-2, and s=A+B. Cauchy–Schwarz bounds the lag N-2 energy by AB and AM–GM bounds lag N-1 by A²/4; the deficits expand to the three phase/amplitude terms stated in RESULT.md. The gap from AB+A²/4 to s(7A+3B)/16 is exactly 3(A-B)²/16. Since s≤1 and the row sums give ΣA=ΣB=2, summing gives 5/4. Equality forces s=0 or 1, and in the latter case A=B=1/2, all four moduli are 1/2, and the lag terms are in phase. Row normalization forces four active columns. Their inner products give precisely the stated product of antipodal factors; the interior block is free. The Walsh construction attains the bound, including at N=4, and Fourier columns give 5/N. Separately, AB≤s/4 and A²/4≤A/4 prove the single-lag values 1 and 1/2, attained by the Walsh block and by a two-row Hadamard block respectively. Independent proper symbols give the two covariance pairings plus the diagonal fourth-cumulant correction; with μ4<2 the statistical minimum follows with the claimed sign.

## originality

PASS

The joint equal-weight optimum for the two last lags in arbitrary dimension and its equality classification are distinct on the searched evidence. Single-lag optima, prefix optima and the fourth-moment formula are prior results, not part of this originality pass.

## value

PASS

The last two aperiodic lags are a natural adjacent tail window: they probe the overlap of only four extreme rows. The exact compatibility loss of 1/4 and equality family answer whether one orthonormal basis can realize both individually optimal sidelobes and identify precisely when the inverse DFT ceases to solve the selected-window design problem. This is not a re-evaluation of the prefix result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
