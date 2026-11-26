# Independent mathematical audit

## correctness

PASS

For the zero-based unshifted fixed point, p(2a)=0 and p(2a+1)=1−p(a). This excludes 11, then 0000, which would require adjacent parent 1s. Thus equal factors of length n>=4 have the same start parity, since opposite parities would force four zeros. Same-parity equality is exactly parent-factor equality at length floor(n/2) for even starts and ceil(n/2) for odd starts. The first even collision is at 2I(floor(n/2)), strictly before the first odd collision at 2I(ceil(n/2))+1 by length monotonicity, and its earlier position also doubles. The prefix 0100010 gives the base (i,j) pairs (0,2), (2,3), (0,4); uniqueness follows because every start before j has a distinct factor. Iteration yields the two dyadic branches and both witness coordinates. The two limits follow by taking n at the dyadic left endpoint and just before the right endpoint, respectively for the upper and lower limits. Analytic replay: RESULT.md:29–52. VERIFICATION.md and verify.py were inspected; their recorded finite checks do not replace the induction and were not rerun.

## originality

FAIL

A distinct indexed Resultary record now explicitly gives the same sequence, recurrence, staircase and two limit constants, with a proof whose decimation equations also mechanically give the two witness coordinates. The earlier-start coordinate is prominently stated in the frozen claim but is not a surviving distinct result. This is verified current equivalent coverage, not evidence that the later-dated record preceded or was independent of the frozen finding, or that the frozen result was already known on its date.

## value

PASS

As mathematics, the law gives a natural prefix statistic with an exact structural explanation for every length, not an arbitrary cutoff; the complete first collision profile and its witnesses are useful in comparing morphic words. This assessment of the result's intrinsic scope does not make the covered formula or the mechanically implied witness a distinct new contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
