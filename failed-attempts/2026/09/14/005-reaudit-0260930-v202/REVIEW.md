# Review status

Independent mathematical audit date: 2026-10-01 UTC.

Disposition: **failed**.

Correctness: **PASS**. Direct normalization gives the finite double-pole coefficients \(-3/16\) at \(0,1,2\) and coefficient \(-1/4\) at infinity, all independent of \(q\). Hence the finite Case-1 alpha sets are \(\{1/4,3/4\}\), the infinity set is \(\{1/2\}\), and every candidate degree is one of \(-1/4,-3/4,-5/4,-7/4\). No nonnegative integer degree exists, so the Case-1 locus is empty for every \(q\). The argument also transfers between the original and normalized scalar equations at the Riccati level because the gauge contributes a rational logarithmic derivative.

Originality: **PASS**. No exact prior statement of this accessory line was located. The closest primary source, Loray–van der Put–Ulmer, treats rank-two Lamé connections with local exponents \(1/4\) and \(-1/4\) at all four poles; the audited scalar Heun family has finite exponent differences \(1/2\) but repeated exponents at infinity, so it is not the same four-half-exponent family. Kovacic gives the general Case-1 criterion, but the exact \(q\)-independent obstruction is not tabulated in the inspected literature.

Scientific value: **FAIL**. The entire conclusion follows immediately from the standard Case-1 local-degree test once four elementary pole coefficients are substituted; the accessory parameter drops out before any polynomial or Riccati equation needs to be solved. The record itself frames the result as an explicit specialization of established theory, and the cited Lamé-family motivation is not exact because the infinity exponent difference is 0 rather than \(1/2\). No separate extremality, boundary phenomenon, classification cutoff, or downstream mathematical need for this particular line was established. Under the shared value bar, this is a routine negative specialization rather than a worthwhile new gap.

Evidence: `INDEPENDENT_AUDIT_2026-10-01.md` and `INDEPENDENT_AUDIT_2026-10-01.json`.
