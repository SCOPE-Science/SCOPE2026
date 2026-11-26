# Independent mathematical audit

## correctness

PASS

The central binomial Vandermonde identity gives the sum of squared four-part multinomials. Modulo five, the freshman's-dream digit factorization leaves only carry-free multinomials; their sum of squares factors across digits. The residues of D_0 through D_4 are (1,4,3,1,1), yielding weights (1,1,-1,1,1) and no zeros. Summing w_b w_(b+a mod 5) separately on no-carry and carry units b gives coefficient pairs (5,0),(0,1),(-1,2),(2,-1),(1,0). At lag one this gives raw sum 1 for every complete block [0,5^r); both marginal sums are 3^r because the right endpoint f(5^r) equals f(0)=1. The four indicator expansions give the exact cells. For h>=2 all nonzero terms of the correlation recursion use smaller lags; induction from h=0 and h=1 gives rational limits and O_h(5^(-r)) normalized complete-block errors, with the starting r=0 absorbed in the constant. An aligned block differs from an initial block at no more than h carry-boundary locations, so the arbitrary-cutoff error is O_h(log(2N)) on the RAW sum, i.e. O_h(log(2N)/N) on the average. Single-sign sums are bounded by the geometric sum of 3^r block contributions, and shifting by fixed h does not affect their zero limiting mean. Finally, for q>=1 the nonzero units digits map the interval [-1/5,2/5] strictly inside itself, while trailing zeros preserve the value. Removing the trailing zeros leaves only one-digit 2 and 3 as equality seeds. This checks the endpoints, normalizations and the all-shift quantifier.

## originality

PASS

Best of current knowledge, credit the digit/Lucas law and general carry-correlation method as known ingredients; the supported distinct result is the explicit Domb sign table and sharp Domb-specific autocorrelation classification with arbitrary-cutoff control. Inspected analogues use different digit weights or observables and do not yield that specific arithmetic and extremal conclusion by specialization alone. No historical-first claim is made.

## value

PASS

The quadratic character of the classical Domb sequence at this nonvanishing prime gives a natural binary observable. The complete two-point law distinguishes asymptotic nearest-neighbor independence with an exact finite-block bias from unique strong positive and negative correlations at other lags. A researcher studying digit correlations or testing arithmetic independence can use the full lag recursion, extrema and cutoff estimate without recreating a carry analysis. The value is the complete sharp spectrum, not recomputing a residue census or selecting a single tiny instance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
