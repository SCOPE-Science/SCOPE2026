# Independent mathematical audit — 2026-10-01

## Final claim

For the stated \(t=2\) Heun family, every accessory parameter \(q\) fails Kovacic Case 1.

## Correctness — PASS

Direct normalization gives the finite double-pole coefficients \(-3/16\) at \(0,1,2\) and coefficient \(-1/4\) at infinity, all independent of \(q\). Hence the finite Case-1 alpha sets are \(\{1/4,3/4\}\), the infinity set is \(\{1/2\}\), and every candidate degree is one of \(-1/4,-3/4,-5/4,-7/4\). No nonnegative integer degree exists, so the Case-1 locus is empty for every \(q\). The argument also transfers between the original and normalized scalar equations at the Riccati level because the gauge contributes a rational logarithmic derivative.

## Originality — PASS

No exact prior statement of this accessory line was located. The closest primary source, Loray–van der Put–Ulmer, treats rank-two Lamé connections with local exponents \(1/4\) and \(-1/4\) at all four poles; the audited scalar Heun family has finite exponent differences \(1/2\) but repeated exponents at infinity, so it is not the same four-half-exponent family. Kovacic gives the general Case-1 criterion, but the exact \(q\)-independent obstruction is not tabulated in the inspected literature.

### Equivalent formulations

Case-1 solvability, rational Riccati solvability, and reducibility of the corresponding rank-two differential module are equivalent here after the rational logarithmic-derivative shift.

### Broader coverage

Loray's family is not the same local exponent data at infinity, while Kovacic is the general method rather than an exact parameter table.

### Exact database or table

No exact external table was found; best-knowledge originality therefore passes despite the result's low scientific value.

### Claim versus prior implication

The audited statement is not literally contained in Loray's family theorem, but it is a straightforward application of Kovacic's standard criterion. That makes the mathematical content routine for value purposes even though no exact published parameter row was found.

## Scientific value — FAIL

The entire conclusion follows immediately from the standard Case-1 local-degree test once four elementary pole coefficients are substituted; the accessory parameter drops out before any polynomial or Riccati equation needs to be solved. The record itself frames the result as an explicit specialization of established theory, and the cited Lamé-family motivation is not exact because the infinity exponent difference is 0 rather than \(1/2\). No separate extremality, boundary phenomenon, classification cutoff, or downstream mathematical need for this particular line was established. Under the shared value bar, this is a routine negative specialization rather than a worthwhile new gap.

## Sources inspected

- **Jerald J. Kovacic, An algorithm for solving second order linear homogeneous differential equations** — https://doi.org/10.1016/S0747-7171(86)80010-4. GENERAL_CRITERION: The audited proof is a direct specialization of this standard degree test.
- **Frank Loray, Marius van der Put, Felix Ulmer, The Lamé family of connections on the projective line** — https://doi.org/10.5802/afst.1187. RELATED_BUT_DIFFERENT_LOCAL_EXPONENT_DATA: The paper repeatedly requires local exponents \(1/4,-1/4\) at all four singular points, whereas the audited Heun equation has equal exponents at infinity.

## Checked evidence

- Assigned RESULT.md and artifacts/kovacic_case1_normalform.py from the exact Git tree.
- Fresh symbolic computation of all four pole coefficients and all eight Case-1 choices.
- Full-text comparison with Loray–van der Put–Ulmer and Kovacic's primary algorithm.
- Published-record semantic search.

## Residual risks

- Originality remains best-knowledge because an unindexed Heun parameter table could exist.
- The scientific failure is solely the value axis; the mathematical negative result itself is correct.

## Disposition

**failed**
