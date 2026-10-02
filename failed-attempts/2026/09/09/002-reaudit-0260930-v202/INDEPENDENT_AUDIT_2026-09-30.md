# Independent audit — SCOPE-20260909-002

Audited at: 2026-09-30T22:14:07Z

Disposition: **failed**

## Correctness

**PASS** — Independent reconstruction from the defining Jacobi sum at degree 6 reproduces all ten real-root sets and the five HOLD/BREAK classifications. For beta = -1.9 and -1.7 the second zero of the quasi-orthogonal polynomial lies below the Driver–Jordaan threshold and the two-zero/zero-zero separation witnesses are consistent; for beta = -1.5, -1.3 and -1.1 the strict alternating chains hold. The exact-rational Sturm verifier is internally coherent and its degree, endpoint-sign, root-count and ordering checks match the independent replay.

## Originality

**FAIL** — The scientific claim is a finite specialization of a pre-existing necessary-and-sufficient theorem for exactly this Askey pair. Driver and Jordaan, Theorem 3.1, classify interlacing of the degree-n Jacobi polynomial with parameters alpha and beta and the degree-n Jacobi polynomial with parameters alpha and beta+2 throughout alpha > -1 and -2 < beta < -1 by the threshold delta < x_2,n. Evaluating that theorem at n=6, alpha=0 and the five listed beta values implies the record’s HOLD/BREAK statements. Exact rational brackets improve reproducibility but do not create an original mathematical implication.

### Equivalent formulations

The record’s HOLD/BREAK predicate is exactly the interlacing predicate classified by Theorem 3.1; the five cases are parameter substitutions plus root evaluation.

Evidence: Driver–Jordaan, Zeros of Quasi-Orthogonal Jacobi Polynomials, SIGMA 12 (2016) 042, Theorem 3.1 gives the iff interlacing criterion for the same polynomial pair.

### Broader coverage

Broader prior coverage is decisive even though the prior paper does not print these exact five numerical root brackets.

Evidence: The theorem ranges over all n, alpha > -1 and -2 < beta < -1, strictly broader than n=6, alpha=0 and five beta values.

### Exact database or table

The absence of an identical table does not restore originality because a stronger theorem already implies the classified cases.

Evidence: No separate exact table matching these five values was found; Driver–Jordaan prints different numerical examples at n=5, alpha=2.35.

### Claim versus prior implication

The claim is a special case/corollary of the established theorem, so it is covered under an implication-based originality test.

Evidence: For each listed beta, the prior iff criterion plus the corresponding second zero decides precisely the same HOLD/BREAK conclusion.

## Scientific value

**FAIL** — The Askey problem is well motivated and the certificates are careful, but after the stronger necessary-and-sufficient theorem is taken into account this five-point grid is a routine specialization rather than a distinct unresolved boundary problem. The exact instances are mechanically obtained from the established criterion, so the narrow finite table does not meet the value bar as a standalone finding.

## Sources inspected

- **Zeros of Quasi-Orthogonal Jacobi Polynomials** (arXiv:1510.08599 / SIGMA 12 (2016) 042): Full article with focus on Section 3, Theorem 3.1 and the numerical examples in Remark 3.2. Assessment: COVERING. Evidence: Theorem 3.1 is necessary and sufficient for interlacing of the degree-n Jacobi polynomial with parameters alpha and beta and the degree-n Jacobi polynomial with parameters alpha and beta+2 in the same parameter window.

## Residual risks

- No residual access issue changes the decisive prior-theorem coverage.
