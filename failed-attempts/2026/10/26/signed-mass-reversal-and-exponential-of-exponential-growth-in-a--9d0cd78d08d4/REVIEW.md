# Independent mathematical audit

## correctness

PASS

Pezzella Eq. (3) and the GL(p) definition give forward Euler in the logarithms followed by one explicit trapezoid sweep at p=2. The predictor's weighted log increment is zero, so strict Jensen gives mass surplus away from equilibrium; the largest of the two predictor exponents gives its limit. Independent symbolic expansion of the corrected logarithms and re-exponentiation gives the normalized Taylor coefficients (1+r,0,0,-(1+r)(r-1)^4/(12r^2)). For r<1 the first log-endpoint is (sr/2) exp(s(1/r-r)) + O(s), the second is O(s); exchange components for r>1. This gives the boxed limit, and continuity plus the strict small-step sign gives a crossing but not uniqueness. At equilibrium both updates are constant. Positivity is exact-arithmetic positivity. Independently replay with python3 /workspace/audit_replay/exchange.py (SymPy); the script also proves the numerical example by rational exponential lower bounds. The recorded 324 assertions were inspected, not reused as independent evidence.

## originality

FAIL

The exact same exchange map and its defining large-step result are covered by the indexed all-sweep law, which contains this result's central claim as the one-correction case and gives identical closed endpoint formulas, including the example under a swap. The small-step cubic coefficient is not stated there, but follows by routine Taylor expansion of its exact formulas, and the crossing follows by continuity; no separate valuable revised claim was established. This is a coverage finding, not a determination of historical priority; the covering record has a later catalogue date.

## value

PASS

The whole mass-law phenomenon is substantive: it distinguishes unconditional positivity from conservation and quantifies failure on a smallest conservative coupled test. This does not make the routine Taylor specialization of the covered map a standalone contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
